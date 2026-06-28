"""
Embedding helpers using sentence-transformers (MPS-accelerated on Mac).

Text embeddings:  embed(texts)  -> np.ndarray  shape (N, D)
CLIP embeddings:  clip_embed_text(texts), clip_embed_images(images)
"""
from __future__ import annotations

from functools import lru_cache
from typing import Union
from pathlib import Path

import numpy as np

from ragkit.config import (
    CLIP_MODEL,
    DEVICE,
    EMBED_BACKEND,
    EMBED_MODEL,
    VOYAGE_EMBED_MODEL,
)


# ── Text embeddings ───────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _get_embed_model():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL, device=DEVICE)
    return model


@lru_cache(maxsize=1)
def _get_voyage_client():
    """Lazily import + construct the Voyage client. Returns None if unavailable."""
    import os

    if not os.environ.get("VOYAGE_API_KEY"):
        print("⚠️  EMBED_BACKEND=voyage but VOYAGE_API_KEY is not set — falling back to local (MiniLM).")
        return None
    try:
        import voyageai
    except ImportError:
        print("⚠️  EMBED_BACKEND=voyage but the `voyageai` package isn't installed — falling back to local (MiniLM).")
        return None
    return voyageai.Client()


def _embed_local(texts: list[str]) -> np.ndarray:
    model = _get_embed_model()
    vecs = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    return vecs.astype(np.float32)


def _embed_voyage(texts: list[str], input_type: str | None) -> np.ndarray | None:
    """Returns None (caller falls back to local) if the Voyage client is unavailable."""
    client = _get_voyage_client()
    if client is None:
        return None
    result = client.embed(texts, model=VOYAGE_EMBED_MODEL, input_type=input_type)
    vecs = np.array(result.embeddings, dtype=np.float32)
    # Voyage embeddings are not pre-normalized — normalize to honor embed()'s contract.
    norms = np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-10
    return vecs / norms


def embed(texts: list[str], input_type: str | None = None) -> np.ndarray:
    """
    Embed a list of strings.  Returns float32, L2-normalized array of shape
    (N, embedding_dim). Automatically batches and runs on DEVICE (mps/cuda/cpu)
    when using the local (MiniLM) backend.

    input_type: optional "query" | "document" — only used by the Voyage
    backend (asymmetric embeddings); ignored by the local backend.
    """
    if isinstance(texts, str):
        texts = [texts]
    if EMBED_BACKEND == "voyage":
        vecs = _embed_voyage(texts, input_type)
        if vecs is not None:
            return vecs
        # fall through to local on any unavailability
    return _embed_local(texts)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Cosine similarity between a query vector and a matrix of document vectors.
    a: shape (D,) or (1, D)
    b: shape (N, D)
    Returns: shape (N,)
    """
    a = a.flatten() / (np.linalg.norm(a) + 1e-10)
    norms = np.linalg.norm(b, axis=1, keepdims=True) + 1e-10
    b_norm = b / norms
    return b_norm @ a


# ── CLIP (multimodal) embeddings ──────────────────────────────────────────────

@lru_cache(maxsize=1)
def _get_clip_model():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(CLIP_MODEL, device=DEVICE)
    return model


def clip_embed_texts(texts: list[str]) -> np.ndarray:
    """Embed text with CLIP for cross-modal retrieval."""
    if isinstance(texts, str):
        texts = [texts]
    model = _get_clip_model()
    vecs = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    return vecs.astype(np.float32)


def clip_embed_images(images: list) -> np.ndarray:
    """
    Embed images with CLIP.
    images: list of file paths (str/Path) or PIL Images.
    """
    from PIL import Image

    pil_images = []
    for img in images:
        if isinstance(img, (str, Path)):
            pil_images.append(Image.open(img).convert("RGB"))
        else:
            pil_images.append(img.convert("RGB"))

    model = _get_clip_model()
    vecs = model.encode(pil_images, convert_to_numpy=True, normalize_embeddings=True)
    return vecs.astype(np.float32)
