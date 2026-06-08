"""
Global configuration: backend selection and hardware device detection.

Set BACKEND = "claude" | "local" at the top of any notebook (or here for a
project-wide default).  Notebooks override this with their own toggle cell.
"""
import os

# ── Backend ──────────────────────────────────────────────────────────────────
# "claude"  → generation via Anthropic API (uses ANTHROPIC_API_KEY)
# "local"   → generation via Ollama (fully offline, Metal-accelerated on Mac)
BACKEND: str = os.environ.get("RAG_BACKEND", "claude")

# ── LLM model names ──────────────────────────────────────────────────────────
CLAUDE_TEXT_MODEL  = "claude-sonnet-4-6"
CLAUDE_VISION_MODEL = "claude-sonnet-4-6"       # same model handles vision
OLLAMA_TEXT_MODEL  = "llama3.1:8b"
OLLAMA_VISION_MODEL = "llama3.2-vision"

# ── Embedding model (used by sentence-transformers) ───────────────────────────
EMBED_MODEL = "all-MiniLM-L6-v2"               # ~90 MB, fast on MPS
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
CLIP_MODEL = "clip-ViT-B-32"                   # for multimodal notebook

# ── Hardware device detection (MPS > CUDA > CPU) ─────────────────────────────
def _detect_device() -> str:
    try:
        import torch
        if torch.backends.mps.is_available():
            return "mps"
        if torch.cuda.is_available():
            return "cuda"
    except ImportError:
        pass
    return "cpu"

DEVICE: str = _detect_device()

# ── Neo4j (Graph RAG) ─────────────────────────────────────────────────────────
NEO4J_URI      = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER     = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "helios-rag-2025")

# ── Ollama ────────────────────────────────────────────────────────────────────
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
