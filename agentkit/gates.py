"""Evidence-based merge-gate primitives: verdicts that steer control flow
instead of landing on a dashboard, and a blast-radius-first policy for
deciding what an agent's change may do next.

Taught in 05_evaluation's agent-eval-gates notebook; builds on `contracts.py`
(schema validation feeds `verdict_to_action`'s BLOCK_EDGE path) and on the
trajectory/tool-call scorers from the agent-evals notebook (feed `Evidence`).

Judge calls are never made here — `JudgeConfig.call_fn` is injected by the
caller, the same way ragkit's embed functions are injected into agentkit's
other modules. This module has no anthropic/openai import.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class BlastRadius(Enum):
    REVERSIBLE_CONTAINED = "reversible_contained"
    REVERSIBLE_WIDE = "reversible_wide"
    IRREVERSIBLE = "irreversible"


class EvidenceSource(Enum):
    DETERMINISTIC_CHECK = "deterministic_check"
    EVAL_TRAJECTORY = "eval_trajectory"
    ROLLBACK_HISTORY = "rollback_history"
    MODEL_SELF_REPORT = "model_self_report"


# Priority order, as data: deterministic checks outweigh trajectory evals,
# which outweigh rollback history, which outweighs the model grading itself —
# the one input the model can influence, so it gets the least weight.
EVIDENCE_WEIGHTS: dict[EvidenceSource, float] = {
    EvidenceSource.DETERMINISTIC_CHECK: 1.0,
    EvidenceSource.EVAL_TRAJECTORY: 0.6,
    EvidenceSource.ROLLBACK_HISTORY: 0.3,
    EvidenceSource.MODEL_SELF_REPORT: 0.1,
}


@dataclass
class Evidence:
    source: EvidenceSource
    passed: bool
    detail: str = ""


@dataclass
class Verdict:
    score: float
    passed: bool
    judge_id: str
    rubric_version: str
    rubric: str
    rationale: str = ""


@dataclass
class JudgeConfig:
    judge_id: str
    rubric_version: str
    rubric: str
    call_fn: Callable[[str], str]
    judge_family: str = ""


def cross_family_warnings(judge: JudgeConfig, target_model_id: str, target_family: str) -> list[str]:
    """Non-empty when the judge shares a model or family with the system under
    test — same-family judging is the setup behind self-preference inflation."""
    warnings = []
    if judge.judge_id == target_model_id:
        warnings.append(f"judge '{judge.judge_id}' IS the model under test — self-review, not judging")
    elif judge.judge_family and judge.judge_family == target_family:
        warnings.append(f"judge family '{judge.judge_family}' matches target family '{target_family}'")
    return warnings


def judge_verdict(judge: JudgeConfig, prompt: str, pass_threshold: float = 0.7) -> Verdict:
    """Run a rubric judge and stamp the result with judge_id + rubric_version —
    a score without both is unreproducible the moment the judge's version moves."""
    raw = judge.call_fn(prompt)
    match = re.findall(r"\d+(?:\.\d+)?", raw)
    score = float(match[0]) / 10.0 if match else 0.0
    score = max(0.0, min(1.0, score))
    return Verdict(
        score=score,
        passed=score >= pass_threshold,
        judge_id=judge.judge_id,
        rubric_version=judge.rubric_version,
        rubric=judge.rubric,
        rationale=raw,
    )


class Action(Enum):
    PROCEED = "proceed"
    RETRY = "retry"
    REJECT_HANDOFF = "reject_handoff"
    BLOCK_EDGE = "block_edge"
    QUARANTINE = "quarantine"
    END_RUN = "end_run"


def verdict_to_action(
    verdict: Verdict,
    *,
    grounding_floor: float = 0.7,
    schema_errors: list[str] | None = None,
    fabrication_suspected: bool = False,
    completion_verified: bool = False,
) -> Action:
    """The thermostat step: a verdict alone changes nothing until it's mapped
    to a structural action on the run in progress."""
    if schema_errors:
        return Action.BLOCK_EDGE
    if fabrication_suspected:
        return Action.QUARANTINE
    if verdict.score < grounding_floor:
        return Action.REJECT_HANDOFF
    if completion_verified:
        return Action.END_RUN
    return Action.PROCEED if verdict.passed else Action.RETRY


@dataclass
class LanePolicy:
    lane: BlastRadius
    evidence_floor: float
    auto_open: bool = True


DEFAULT_LANES: dict[BlastRadius, LanePolicy] = {
    BlastRadius.REVERSIBLE_CONTAINED: LanePolicy(BlastRadius.REVERSIBLE_CONTAINED, evidence_floor=0.6),
    BlastRadius.REVERSIBLE_WIDE: LanePolicy(BlastRadius.REVERSIBLE_WIDE, evidence_floor=0.85),
    BlastRadius.IRREVERSIBLE: LanePolicy(BlastRadius.IRREVERSIBLE, evidence_floor=1.0, auto_open=False),
}


@dataclass
class GateDecision:
    opened: bool
    lane: BlastRadius
    evidence_score: float
    shadow: bool
    reasons: list[str] = field(default_factory=list)


@dataclass
class MergeGate:
    policies: dict[BlastRadius, LanePolicy] = field(default_factory=lambda: dict(DEFAULT_LANES))
    shadow_mode: bool = True
    decisions: list[GateDecision] = field(default_factory=list)

    def evidence_score(self, evidence: list[Evidence]) -> float:
        if not evidence:
            return 0.0
        weighted = sum(EVIDENCE_WEIGHTS[e.source] * (1.0 if e.passed else 0.0) for e in evidence)
        total_weight = sum(EVIDENCE_WEIGHTS[e.source] for e in evidence)
        return weighted / total_weight

    def evaluate(self, lane: BlastRadius, evidence: list[Evidence]) -> GateDecision:
        policy = self.policies[lane]
        score = self.evidence_score(evidence)
        reasons = [f"{e.source.value}: {'pass' if e.passed else 'fail'} ({e.detail})" for e in evidence]

        # Structural invariant, checked before any evidence: an irreversible
        # lane never opens on score alone, no matter how strong the evidence.
        if not policy.auto_open:
            decision = GateDecision(opened=False, lane=lane, evidence_score=score,
                                     shadow=self.shadow_mode, reasons=reasons + ["lane never auto-opens"])
        else:
            opened = score >= policy.evidence_floor
            decision = GateDecision(opened=opened, lane=lane, evidence_score=score,
                                     shadow=self.shadow_mode, reasons=reasons)

        self.decisions.append(decision)
        return decision

    def disagreement_rate(self, human_calls: list[bool]) -> float:
        """Fraction of logged shadow decisions where the gate's `opened` call
        differs from a human reviewer's call on the same change."""
        paired = list(zip(self.decisions, human_calls))
        if not paired:
            return 0.0
        disagreements = sum(1 for d, human in paired if d.opened != human)
        return disagreements / len(paired)
