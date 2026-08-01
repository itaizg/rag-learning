"""A response cache keyed by embedding similarity rather than exact text —
"semantic caching": if a new query is close enough in meaning to one already
answered, replay the stored answer instead of calling the model again.

Namespace is a first-class argument by design: on its own this is just a
cache (used with the default namespace in the inference-economics notebook);
passing a real per-tenant namespace is what the multi-tenant isolation
notebook adds on top, without changing this class at all.
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Callable

import numpy as np


@dataclass
class CacheHit:
    response: str
    similarity: float
    age_s: float
    key_query: str
    namespace: str


@dataclass
class _Entry:
    vector: np.ndarray
    query: str
    response: str
    created_at: float
    last_used: float
    hits: int = 0


class SemanticCache:
    def __init__(
        self,
        embed_fn: Callable[[list[str]], np.ndarray],
        threshold: float = 0.90,
        ttl_s: float | None = None,
        max_entries: int = 256,
        eviction: str = "lru",
        clock: Callable[[], float] = time.monotonic,
    ):
        if eviction not in ("lru", "fifo"):
            raise ValueError(f"unknown eviction policy '{eviction}' (expected 'lru' or 'fifo')")
        self.embed_fn = embed_fn
        self.threshold = threshold
        self.ttl_s = ttl_s
        self.max_entries = max_entries
        self.eviction = eviction
        self._clock = clock
        self._store: dict[str, list[_Entry]] = {}
        self._stats = {"lookups": 0, "hits": 0, "expired": 0, "evictions": 0}

    def get(self, query: str, namespace: str = "default") -> CacheHit | None:
        self._stats["lookups"] += 1
        entries = self._store.get(namespace, [])
        if not entries:
            return None

        now = self._clock()
        query_vec = self.embed_fn([query])[0]
        best_entry, best_sim = None, -1.0
        for entry in entries:
            sim = _cosine(query_vec, entry.vector)
            if sim > best_sim:
                best_entry, best_sim = entry, sim

        if best_entry is None or best_sim < self.threshold:
            return None

        if self.ttl_s is not None and (now - best_entry.created_at) > self.ttl_s:
            entries.remove(best_entry)
            self._stats["expired"] += 1
            return None

        best_entry.last_used = now
        best_entry.hits += 1
        self._stats["hits"] += 1
        return CacheHit(
            response=best_entry.response,
            similarity=float(best_sim),
            age_s=now - best_entry.created_at,
            key_query=best_entry.query,
            namespace=namespace,
        )

    def put(self, query: str, response: str, namespace: str = "default") -> None:
        now = self._clock()
        vector = self.embed_fn([query])[0]
        entries = self._store.setdefault(namespace, [])
        entries.append(_Entry(vector=vector, query=query, response=response, created_at=now, last_used=now))
        self._evict_if_needed(entries)

    def _evict_if_needed(self, entries: list[_Entry]) -> None:
        while len(entries) > self.max_entries:
            if self.eviction == "lru":
                victim = min(entries, key=lambda e: e.last_used)
            else:  # fifo
                victim = min(entries, key=lambda e: e.created_at)
            entries.remove(victim)
            self._stats["evictions"] += 1

    def invalidate(self, namespace: str | None = None) -> int:
        if namespace is None:
            count = sum(len(v) for v in self._store.values())
            self._store.clear()
            return count
        count = len(self._store.get(namespace, []))
        self._store.pop(namespace, None)
        return count

    def stats(self) -> dict:
        lookups, hits = self._stats["lookups"], self._stats["hits"]
        return {
            **self._stats,
            "hit_rate": hits / lookups if lookups else 0.0,
            "namespaces": {ns: len(entries) for ns, entries in self._store.items()},
        }


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) or 1e-9
    return float(np.dot(a, b) / denom)
