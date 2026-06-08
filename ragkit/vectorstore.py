"""
Thin ChromaDB helpers.

build_collection(name, docs, metadatas)  -> chroma Collection
query_collection(collection, text, k)    -> list[Hit]

Hit = {"text": str, "metadata": dict, "score": float, "rank": int}
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class Hit:
    text: str
    metadata: dict = field(default_factory=dict)
    score: float = 0.0
    rank: int = 0

    def __repr__(self):
        src = self.metadata.get("source", "?")
        return f"Hit(rank={self.rank}, score={self.score:.3f}, source={src!r})"


def get_client(persist_dir: str = ".chroma"):
    import chromadb
    return chromadb.PersistentClient(path=persist_dir)


def build_collection(
    name: str,
    docs: list[str],
    metadatas: list[dict] | None = None,
    persist_dir: str = ".chroma",
    reset: bool = True,
) -> Any:
    """
    Build (or rebuild) a ChromaDB collection from documents.
    Uses sentence-transformers embeddings computed outside Chroma for visibility.
    """
    import chromadb
    from ragkit.embeddings import embed

    client = get_client(persist_dir)
    if reset:
        try:
            client.delete_collection(name)
        except Exception:
            pass

    collection = client.get_or_create_collection(name, metadata={"hnsw:space": "cosine"})
    metadatas = metadatas or [{"source": f"doc_{i}"} for i in range(len(docs))]

    vecs = embed(docs).tolist()
    ids = [f"{name}_{i}" for i in range(len(docs))]
    collection.add(ids=ids, documents=docs, embeddings=vecs, metadatas=metadatas)
    return collection


def query_collection(
    collection,
    text: str,
    k: int = 5,
) -> list[Hit]:
    """Query a collection, return ranked Hit objects."""
    from ragkit.embeddings import embed

    vec = embed([text]).tolist()
    results = collection.query(
        query_embeddings=vec,
        n_results=min(k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    docs_list = results["documents"][0]
    metas_list = results["metadatas"][0]
    dists_list = results["distances"][0]

    for rank, (doc, meta, dist) in enumerate(zip(docs_list, metas_list, dists_list)):
        score = 1.0 - dist          # cosine distance → similarity
        hits.append(Hit(text=doc, metadata=meta, score=score, rank=rank + 1))

    return hits
