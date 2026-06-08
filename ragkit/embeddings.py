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

from ragkit.config import CLIP_MODEL, DEVICE, EMBED_MODEL


# ── Text embeddings ───────────────────────────────────────────────────────────

@lru_cache(maxsize=1)
def _get_embed_model():
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL, device=DEVICE)
    return model


def embed(texts: list[str]) -> np.ndarray:
    """
    Embed a list of strings.  Returns float32 array of shape (N, embedding_dim).
    Automatically batches and runs on DEVICE (mps/cuda/cpu).
    """
    if isinstance(texts, str):
        texts = [texts]
    model = _get_embed_model()
    vecs = model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
    return vecs.astype(np.float32)


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
