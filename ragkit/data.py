"""
Corpus loader for the Helios Robotics dataset.

load_corpus()         -> list[dict]   each dict: {text, source, category, ...}
load_images()         -> list[dict]   each dict: {path, caption, category}
chunk_text(text, ...)  -> list[str]   split by sentence/size
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent / "data"
CORPUS_DIR = DATA_DIR / "corpus"
IMAGES_DIR = DATA_DIR / "images"


def load_corpus(category: str | None = None) -> list[dict[str, Any]]:
    """
    Load all .txt files from data/corpus/.
    Returns list of dicts with keys: text, source, category, filename.
    Optionally filter by category (parsed from filename prefix, e.g. 'spec_', 'incident_').
    """
    docs = []
    for path in sorted(CORPUS_DIR.glob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()
        # Derive category from filename prefix (e.g. spec_arm_v2.txt → "spec")
        stem = path.stem
        cat = stem.split("_")[0] if "_" in stem else "general"
        doc = {
            "text": text,
            "source": path.name,
            "category": cat,
            "filename": str(path),
        }
        if category is None or cat == category:
            docs.append(doc)
    return docs


def load_images() -> list[dict[str, Any]]:
    """Load image metadata from data/images/. Returns list of {path, caption, category}."""
    items = []
    caption_file = IMAGES_DIR / "captions.txt"
    captions: dict[str, str] = {}
    if caption_file.exists():
        for line in caption_file.read_text().splitlines():
            if "|" in line:
                fname, cap = line.split("|", 1)
                captions[fname.strip()] = cap.strip()

    for ext in ("*.png", "*.jpg", "*.jpeg"):
        for path in sorted(IMAGES_DIR.glob(ext)):
            stem = path.stem
            cat = stem.split("_")[0] if "_" in stem else "image"
            items.append({
                "path": str(path),
                "caption": captions.get(path.name, stem.replace("_", " ")),
                "category": cat,
                "filename": path.name,
            })
    return items


def chunk_text(
    text: str,
    chunk_size: int = 200,
    overlap: int = 40,
) -> list[str]:
    """
    Split text into overlapping word-based chunks.
    chunk_size: approximate number of words per chunk.
    overlap: number of words to repeat at chunk boundaries.
    """
    words = text.split()
    if len(words) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))
        if end == len(words):
            break
        start += chunk_size - overlap
    return chunks


def build_chunked_corpus(
    chunk_size: int = 200,
    overlap: int = 40,
    category: str | None = None,
) -> tuple[list[str], list[dict]]:
    """
    Load corpus, chunk each doc, return (texts, metadatas) ready for Chroma.
    """
    docs = load_corpus(category=category)
    texts, metas = [], []
    for doc in docs:
        chunks = chunk_text(doc["text"], chunk_size=chunk_size, overlap=overlap)
        for i, chunk in enumerate(chunks):
            texts.append(chunk)
            metas.append({
                "source": doc["source"],
                "category": doc["category"],
                "chunk": i,
            })
    return texts, metas
