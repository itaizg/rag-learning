# RAG Learning — 7 Design Patterns

Hands-on Jupyter notebooks covering every pattern from the **RAG Design Patterns** infographic, from Naive RAG through to Multi-Agent RAG.

Each notebook is fully runnable with **two backends**:
- **Claude** (uses your `ANTHROPIC_API_KEY`) — best quality
- **Fully local / offline** via Ollama + sentence-transformers — runs on your Mac GPU (MPS/Metal)

---

## Quick start

### 1. Install dependencies

```bash
uv sync
uv run python -m ipykernel install --user --name rag-learning --display-name "RAG Learning (Python)"
```

### 2. Start Ollama (for local backend)

```bash
brew services start ollama
ollama pull llama3.1:8b          # text model (~4.7 GB)
ollama pull llama3.2-vision       # vision model for notebook 03 (~7.9 GB)
```

### 3. Start Neo4j in Docker (for notebooks 04 and 05)

```bash
docker run -d --name helios-neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/helios-rag-2025 \
  -e NEO4J_PLUGINS='["apoc"]' \
  neo4j:5
```

Neo4j Browser → http://localhost:7474 (user: `neo4j`, pass: `helios-rag-2025`)

### 4. Launch JupyterLab

```bash
uv run jupyter lab
```

Open notebooks in order, starting with `notebooks/00_setup_and_foundations.ipynb`.

---

## Notebooks

| Notebook | Pattern | Key Concepts |
|---|---|---|
| [00 — Setup & Foundations](notebooks/00_setup_and_foundations.ipynb) | — | Embeddings, cosine similarity, chunking, vector DB, prompt templates |
| [01 — Naive RAG](notebooks/01_naive_rag.ipynb) | Basic RAG | Bi-encoder retrieval, ChromaDB, failure modes |
| [02 — Retrieve-and-Rerank](notebooks/02_retrieve_and_rerank.ipynb) | Reranking | Cross-encoder, bi-encoder vs cross-encoder, before/after |
| [03 — Multimodal RAG](notebooks/03_multimodal_rag.ipynb) | Multimodal | CLIP embeddings, text→image, vision LLM |
| [04 — Graph RAG](notebooks/04_graph_rag.ipynb) | Graph | Neo4j, entity extraction, multi-hop traversal, Cypher |
| [05 — Hybrid RAG](notebooks/05_hybrid_rag.ipynb) | Dense+Sparse | BM25, Reciprocal Rank Fusion, exact code retrieval |
| [06 — Agentic RAG (Router)](notebooks/06_agentic_rag_router.ipynb) | Agentic | Tool-calling, routing decisions, agentic loop |
| [07 — Agent RAG (Multi-Agent)](notebooks/07_agent_rag_multi_agent.ipynb) | Multi-Agent | Planner, parallel dispatch, Slack/ServiceNow integrations |

---

## The backend toggle

Every notebook has this cell near the top:

```python
import ragkit.config as cfg
cfg.BACKEND = "claude"   # "claude" | "local"
```

- `"claude"` — uses Anthropic API (`ANTHROPIC_API_KEY` env var required)
- `"local"` — uses Ollama (fully offline, Metal-accelerated on your Mac)

Embeddings and reranking always run locally on MPS regardless of this toggle — only text/vision *generation* switches.

---

## The Helios Robotics dataset

A fictional robotics company dataset that threads through all 7 notebooks:

```
data/
├── corpus/                     18 documents:
│   ├── spec_arm_v2.txt          HeliosArm V2 spec (part: HR-ARM-V2-6DOF)
│   ├── spec_mobile_base.txt     HeliosBase M1 spec (part: HR-MOB-M1-AMR)
│   ├── spec_controller_hc400.txt HC-400 controller (part: HC400-CTRL)
│   ├── spec_gripper_ee01.txt    Standard gripper (part: HR-EE-GRIP-01)
│   ├── spec_firmware_release_notes.txt firmware history
│   ├── team_engineering.txt     Engineering team directory
│   ├── team_field_service.txt   Field service team
│   ├── project_titan.txt        HeliosArm V3 development project
│   ├── project_fleet_ai.txt     AI fleet management project
│   ├── incident_inc2024031.txt  Joint 4 thermal issue (high severity)
│   ├── incident_inc2024047.txt  Firmware config management issue
│   ├── incident_inc2024019.txt  Battery SOC drift issue
│   ├── incident_inc2024011.txt  Gripper reed switch false signal
│   ├── proc_arm_commissioning.txt commissioning procedure
│   ├── proc_battery_replacement.txt battery swap procedure
│   ├── faq_general.txt          General FAQ
│   └── faq_software.txt         Software/controller FAQ
└── images/                    4 technical diagrams
    ├── spec_arm_v2_joint_diagram.png
    ├── spec_mobile_base_topview.png
    ├── spec_battery_capacity_chart.png
    └── spec_controller_hc400_panel.png
```

The dataset is designed so that:
- **Part numbers** (`HR-REED-UPGRADE`, `HC400-CTRL`) stress-test exact-match retrieval (hybrid RAG)
- **Multi-hop questions** require connecting incidents → specs → projects → people (graph RAG)
- **Images** are needed to answer certain questions fully (multimodal RAG)

---

## Shared library: `ragkit/`

```
ragkit/
├── config.py       BACKEND, DEVICE detection (mps/cuda/cpu), Neo4j/Ollama config
├── llm.py          generate() + generate_tools() — works identically for Claude and Ollama
├── embeddings.py   embed() for text, clip_embed_*() for multimodal (sentence-transformers)
├── vectorstore.py  ChromaDB helpers: build_collection(), query_collection(), Hit dataclass
├── rerank.py       rerank() via cross-encoder (ms-marco-MiniLM-L-6-v2)
├── data.py         load_corpus(), load_images(), chunk_text(), build_chunked_corpus()
└── pretty.py       Rich-formatted display: show_hits(), show_prompt(), compare_rankings()
```

The notebooks keep all pattern-specific logic **inline and visible** — `ragkit` only holds
repetitive plumbing so you can see every algorithm clearly.

---

## Hardware & MLX alternative

Embeddings and reranking run on **MPS (Metal)** automatically on your Mac.

For local generation, this repo uses **Ollama** (easiest setup). If you prefer Apple's MLX framework for even faster inference on Apple Silicon:

```bash
pip install mlx-lm
mlx_lm.generate --model mlx-community/Llama-3.1-8B-Instruct-4bit --prompt "Hello"
```

Then in `ragkit/config.py`, set `OLLAMA_TEXT_MODEL` to your MLX server endpoint or adapt `llm.py`.

---

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Required for Claude backend |
| `ANTHROPIC_BASE_URL` | api.anthropic.com | Override if using a proxy |
| `RAG_BACKEND` | `claude` | Project-wide default (`claude`/`local`) |
| `NEO4J_URI` | `bolt://localhost:7687` | Neo4j connection |
| `NEO4J_USER` | `neo4j` | Neo4j username |
| `NEO4J_PASSWORD` | `helios-rag-2025` | Neo4j password |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama host |
