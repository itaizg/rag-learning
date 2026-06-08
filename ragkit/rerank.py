"""
Cross-encoder reranker (sentence-transformers).
Scores each (query, passage) pair jointly — much more accurate than bi-encoder
for picking the best k from a larger candidate set.
"""
from __future__ import annotations

from functools import lru_cache

from ragkit.config import DEVICE, RERANK_MODEL
from ragkit.vectorstore import Hit


@lru_cache(maxsize=1)
def _get_reranker():
    from sentence_transformers import CrossEncoder
    model = CrossEncoder(RERANK_MODEL, device=DEVICE)
    return model


def rerank(query: str, hits: list[Hit], top_k: int | None = None) -> list[Hit]:
    """
    Rerank a list of Hit objects using a cross-encoder.
    Returns a new list sorted by cross-encoder score (descending).
    """
    model = _get_reranker()
    pairs = [(query, h.text) for h in hits]
    scores = model.predict(pairs)

    reranked = sorted(
        zip(scores, hits),
        key=lambda x: x[0],
        reverse=True,
    )

    result = []
    for new_rank, (score, hit) in enumerate(reranked):
        result.append(Hit(
            text=hit.text,
            metadata=hit.metadata,
            score=float(score),
            rank=new_rank + 1,
        ))

    return result[:top_k] if top_k else result
