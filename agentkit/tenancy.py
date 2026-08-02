"""Multi-tenant isolation primitives: a principal identity that must reach
every storage call ("no ambient tenant"), a namespaced vector store with a
deliberate breach switch for teaching contamination, and a cost ledger that
attributes spend by tenant, user, journey, and feature.

Built on top of contracts.checked_execute (via make_budget_hook) and
semcache.SemanticCache (via TenantContext.namespace()) — see the multi-tenant
isolation notebook for how those interlock.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    user_id: str
    journey_id: str | None = None

    def namespace(self) -> str:
        """The value that should scope every cache/store lookup for this principal."""
        return f"{self.tenant_id}/{self.user_id}"

    def scoped_key(self, key: str) -> str:
        return f"{self.namespace()}:{key}"


@dataclass
class _Doc:
    vector: np.ndarray
    text: str
    owner_tenant: str


class NamespacedStore:
    """A minimal vector store with tenant isolation as an explicit, toggleable
    property rather than an assumed one. `enforce_isolation=False` is the
    deliberate breach switch used to demonstrate cross-tenant contamination.
    """

    def __init__(self, embed_fn: Callable[[list[str]], np.ndarray]):
        self.embed_fn = embed_fn
        self._docs: list[_Doc] = []

    def add(self, ctx: TenantContext, docs: list[str], shared: bool = False) -> None:
        owner = "shared" if shared else ctx.tenant_id
        vectors = self.embed_fn(docs)
        for text, vector in zip(docs, vectors):
            self._docs.append(_Doc(vector=vector, text=text, owner_tenant=owner))

    def query(self, ctx: TenantContext, text: str, k: int = 3, enforce_isolation: bool = True) -> list[dict]:
        candidates = self._docs
        if enforce_isolation:
            candidates = [d for d in candidates if d.owner_tenant in (ctx.tenant_id, "shared")]

        query_vec = self.embed_fn([text])[0]
        scored = [(_cosine(query_vec, d.vector), d) for d in candidates]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [
            {"text": d.text, "score": float(score), "owner_tenant": d.owner_tenant}
            for score, d in scored[:k]
        ]


class CostLedger:
    """Attributes spend by tenant/user/journey/feature, on top of nb32's
    PRICE = {tier: {"input": $/M tok, "output": $/M tok}} shape.
    """

    def __init__(self, price_table: dict):
        self.price_table = price_table
        self._records: list[dict] = []

    def record(self, ctx: TenantContext, feature: str, tier: str, in_tok: int, out_tok: int) -> float:
        price = self.price_table[tier]
        cost = (in_tok / 1e6) * price["input"] + (out_tok / 1e6) * price["output"]
        self._records.append(
            {
                "tenant_id": ctx.tenant_id,
                "user_id": ctx.user_id,
                "journey_id": ctx.journey_id,
                "feature": feature,
                "tier": tier,
                "in_tok": in_tok,
                "out_tok": out_tok,
                "cost": cost,
            }
        )
        return cost

    def total(
        self,
        tenant_id: str | None = None,
        user_id: str | None = None,
        journey_id: str | None = None,
        feature: str | None = None,
    ) -> float:
        filters = {"tenant_id": tenant_id, "user_id": user_id, "journey_id": journey_id, "feature": feature}
        matches = self._filter(filters)
        return sum(r["cost"] for r in matches)

    def report(self, by: str = "tenant_id"):
        import pandas as pd

        if not self._records:
            return pd.DataFrame(columns=[by, "cost"])
        df = pd.DataFrame(self._records)
        return df.groupby(by)["cost"].sum().sort_values(ascending=False).reset_index()

    def make_budget_hook(self, ctx: TenantContext, daily_ceiling_usd: float) -> Callable[[str, dict], str | None]:
        """Return a contracts.checked_execute pre_hook that rejects a tool
        call once this tenant's recorded spend exceeds the daily ceiling.
        """

        def hook(name: str, args: dict) -> str | None:
            spent = self.total(tenant_id=ctx.tenant_id)
            if spent >= daily_ceiling_usd:
                return (
                    f"error: tenant '{ctx.tenant_id}' has exceeded its daily budget "
                    f"(${spent:.4f} >= ${daily_ceiling_usd:.4f}) — call rejected"
                )
            return None

        return hook

    def _filter(self, filters: dict) -> list[dict]:
        active = {k: v for k, v in filters.items() if v is not None}
        return [r for r in self._records if all(r[k] == v for k, v in active.items())]


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) or 1e-9
    return float(np.dot(a, b) / denom)
