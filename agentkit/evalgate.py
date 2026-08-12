"""CI/CD eval-gate policy primitives: measure a suite's run-to-run noise
before setting a threshold against it, apply dual (absolute floor + baseline
delta) thresholds with slice awareness, stage coverage by trigger, and stamp
a reproducible release-evidence record.

Taught in 08_production's eval-gate-policy notebook; hardens the naive
single-sample `regression_gate` from the CI-for-AI notebook and hands its
`GateOutcome` to `gates.MergeGate` via `gate_evidence()`. Depends on `gates`
(one direction only — `gates` does not import this module). No scoring
function or judge call lives here: `measure_variance`/`evaluate_candidate`
take scores the caller already computed, the same injection rule every other
agentkit module follows.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np

from agentkit.gates import Evidence, EvidenceSource


@dataclass
class VarianceProfile:
    mean: float
    std: float
    n: int
    ci95_low: float
    ci95_high: float
    lo: float
    hi: float


def measure_variance(score_fn: Callable[[], float], n_repeats: int = 8) -> VarianceProfile:
    """Call `score_fn` (a full suite run against an UNCHANGED system)
    `n_repeats` times and summarize the spread. This is "measure the noise
    floor before you set a threshold against it" as code — a single run
    can't tell you whether a 0.03 drop is a regression or ordinary sampling
    noise, only a distribution can.
    """
    scores = np.array([score_fn() for _ in range(n_repeats)])
    mean, std = float(scores.mean()), float(scores.std(ddof=1)) if n_repeats > 1 else 0.0
    # 95% CI on the mean via the normal approximation (n_repeats is small and
    # fixed in this notebook's demos — good enough for a teaching gate, not a
    # substitute for a real statistical test in a high-stakes pipeline).
    margin = 1.96 * std / np.sqrt(n_repeats) if n_repeats > 1 else 0.0
    return VarianceProfile(
        mean=mean, std=std, n=n_repeats,
        ci95_low=mean - margin, ci95_high=mean + margin,
        lo=float(scores.min()), hi=float(scores.max()),
    )


@dataclass
class ThresholdPolicy:
    absolute_floor: float
    max_baseline_drop: float
    min_pass_of_n: tuple[int, int] | None = None  # (k, n): at least k of n generations must pass
    slice_floor: float | None = None  # per-slice floor; defaults to absolute_floor if unset

    def calibrated(self, profile: VarianceProfile, sigmas: float = 2.0) -> "ThresholdPolicy":
        """Return a copy whose `max_baseline_drop` is widened to at least
        `sigmas * profile.std` — a tolerance narrower than the system's own
        measured noise will fail on ordinary variance, not real regressions.
        """
        floor_for_noise = sigmas * profile.std
        return ThresholdPolicy(
            absolute_floor=self.absolute_floor,
            max_baseline_drop=max(self.max_baseline_drop, floor_for_noise),
            min_pass_of_n=self.min_pass_of_n,
            slice_floor=self.slice_floor,
        )


@dataclass
class GateOutcome:
    passed: bool
    reasons: list[str] = field(default_factory=list)
    candidate_mean: float = 0.0
    baseline_mean: float = 0.0
    per_slice: dict[str, float] = field(default_factory=dict)


def slice_means(scores: list[float], slice_keys: list[str]) -> dict[str, float]:
    """Mean score per slice label, given parallel `scores`/`slice_keys` lists."""
    if len(scores) != len(slice_keys):
        raise ValueError(f"scores and slice_keys must be the same length: got {len(scores)} vs {len(slice_keys)}")
    buckets: dict[str, list[float]] = {}
    for score, key in zip(scores, slice_keys):
        buckets.setdefault(key, []).append(score)
    return {key: float(np.mean(vals)) for key, vals in buckets.items()}


def evaluate_candidate(
    candidate_scores: list[float],
    baseline_scores: list[float],
    policy: ThresholdPolicy,
    slices: list[str] | None = None,
) -> GateOutcome:
    """The dual-threshold gate: an absolute floor stops consistently-poor
    quality from passing regardless of the baseline; a baseline delta catches
    a fresh regression even when the candidate is still above the floor.
    Both checks run independently and both reasons are reported — a gate
    that stops at the first failure hides the second one from the reviewer.
    """
    candidate_mean = float(np.mean(candidate_scores))
    baseline_mean = float(np.mean(baseline_scores))
    reasons: list[str] = []
    passed = True

    if candidate_mean < policy.absolute_floor:
        passed = False
        reasons.append(f"below absolute floor: {candidate_mean:.3f} < {policy.absolute_floor:.3f}")

    drop = baseline_mean - candidate_mean
    if drop > policy.max_baseline_drop:
        passed = False
        reasons.append(f"regressed past baseline delta: dropped {drop:.3f} > {policy.max_baseline_drop:.3f}")

    if policy.min_pass_of_n is not None:
        k, n = policy.min_pass_of_n
        n_pass = sum(1 for s in candidate_scores[:n] if s >= policy.absolute_floor)
        if n_pass < k:
            passed = False
            reasons.append(f"min-pass rule failed: {n_pass}/{n} generations passed, needed {k}")

    per_slice: dict[str, float] = {}
    if slices is not None:
        per_slice = slice_means(candidate_scores, slices)
        floor = policy.slice_floor if policy.slice_floor is not None else policy.absolute_floor
        for name, score in per_slice.items():
            if score < floor:
                passed = False
                reasons.append(f"slice '{name}' below floor: {score:.3f} < {floor:.3f}")

    if not reasons:
        reasons.append(f"passed: {candidate_mean:.3f} >= floor {policy.absolute_floor:.3f}, drop {drop:.3f} <= {policy.max_baseline_drop:.3f}")

    return GateOutcome(passed=passed, reasons=reasons, candidate_mean=candidate_mean,
                        baseline_mean=baseline_mean, per_slice=per_slice)


def gate_evidence(outcome: GateOutcome) -> Evidence:
    """Convert a GateOutcome into `gates.Evidence` for `MergeGate.evaluate` —
    the hand-off from this module's threshold policy to 27c's blast-radius
    lanes. Always DETERMINISTIC_CHECK: the gate itself is arithmetic on
    already-computed scores, not a model judging its own output.
    """
    return Evidence(
        source=EvidenceSource.DETERMINISTIC_CHECK,
        passed=outcome.passed,
        detail="; ".join(outcome.reasons),
    )


@dataclass
class StagePolicy:
    name: str
    case_filter: Callable[[dict], bool]
    repeats: int
    blocking: bool


DEFAULT_STAGES: list[StagePolicy] = [
    StagePolicy(name="pull_request", case_filter=lambda case: case.get("tag") == "critical", repeats=1, blocking=True),
    StagePolicy(name="nightly", case_filter=lambda case: True, repeats=5, blocking=True),
    StagePolicy(name="pre_release", case_filter=lambda case: True, repeats=8, blocking=True),
]


def select_cases(cases: list[dict], stage: StagePolicy) -> list[dict]:
    return [case for case in cases if stage.case_filter(case)]


@dataclass
class ReleaseEvidence:
    candidate_id: str
    dataset_version: str
    dataset_hash: str
    metric_version: str
    judge_id: str
    scores: list[float]
    per_slice: dict[str, float]
    decision: bool
    reasons: list[str]
    approver: str = ""

    def to_dict(self) -> dict:
        return {
            "candidate_id": self.candidate_id,
            "dataset_version": self.dataset_version,
            "dataset_hash": self.dataset_hash,
            "metric_version": self.metric_version,
            "judge_id": self.judge_id,
            "scores": self.scores,
            "per_slice": self.per_slice,
            "decision": self.decision,
            "reasons": self.reasons,
            "approver": self.approver,
        }

    def to_json(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), indent=2, sort_keys=True))

    @classmethod
    def from_json(cls, path: str | Path) -> "ReleaseEvidence":
        return cls(**json.loads(Path(path).read_text()))


def dataset_hash(cases: list[dict]) -> str:
    """A stable sha256 over the sorted, serialized case list — makes "was
    this the same benchmark?" a check instead of an assertion. Sorting keys
    means insertion order doesn't change the hash.
    """
    canonical = json.dumps(cases, sort_keys=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
