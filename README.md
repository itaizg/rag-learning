# AI Learning Notebooks

A self-paced, hands-on curriculum that takes you from *"I use AI tools"* to *"I understand and build AI systems."* Every notebook teaches one concept with a plain-English explanation, working code you can run, a visualization, and three exercises (with solutions).

The curriculum is organized into tiers that mirror a natural learning progression. Plus a bonus 7th tier: the original **RAG Design Patterns** notebooks.

```
Tier 1  Foundations          how AI/LLMs actually work          (00–06)   ✅
Tier 2  Training             how models are trained & aligned   (07–11)   ✅
Tier 3  Building with LLMs   RAG, caching, inference            (12–17)   ✅
Tier 4  Agent Engineering    systems that use LLMs              (18–23)   ✅
Tier 5  Evaluation & Prod    measuring & shipping AI            (24–27)   [planned]
Tier 6  Projects             capstones (train/RAG/agents)       (P1–P4)   P3 ✅
Tier 7  RAG Design Patterns  the original rag_learning series   (01–07)   ✅
```

---

## Curriculum map

```mermaid
graph TD
    subgraph T1["Tier 1 — Foundations ✅"]
        N00[00 Environment Check] --> N01[01 Neural Networks]
        N01 --> N02[02 Tokenization] --> N03[03 Embeddings]
        N03 --> N04[04 Attention] --> N05[05 Transformer Arch] --> N06[06 How LLMs Work]
    end
    subgraph T2["Tier 2 — Training ✅"]
        N07[07 Pretraining & Scaling] --> N08[08 Fine-tuning & LoRA]
        N08 --> N09[09 RLHF & Alignment] --> N10[10 Quantization] --> N11[11 Speculative Decoding]
    end
    subgraph T3["Tier 3 — Building ✅"]
        N12[12 Prompt Eng] --> N13[13 Context & KV Cache] --> N13b[13b vLLM Serving] --> N14[14 RAG]
        N14 --> N15[15 Vector DBs] --> N16[16 RAG vs CAG] --> N17[17 Chain of Thought]
    end
    subgraph T4["Tier 4 — Agents ✅"]
        N18[18 What Is an Agent] --> N19[19 Agent Loop] --> N20[20 Multi-Agent + LangGraph]
        N20 --> N21[21 Harness + LangSmith] --> N22[22 Context Eng] --> N23[23 Loop Eng]
    end
    subgraph T6["Tier 6 — Projects"]
        P3[P3 Research Agent Capstone]
    end
    N06 --> N07
    N11 --> N12
    N17 --> N18
    N23 --> P3
```

---

## Status

| Tier | Notebooks | Status |
|------|-----------|--------|
| 1 — Foundations | `00_setup/`, `01_foundations/` (00–06) | ✅ Built & executed |
| 2 — Training | `02_training/` (07–11) | ✅ Built & executed |
| 3 — Building | `03_building/` (12–17) | ✅ Built & executed |
| 4 — Agents | `04_agents/` (18–23, +19b) | ✅ Built & executed |
| 5 — Evaluation | `05_evaluation/` (24–27) | ⬜ Planned |
| 6 — Projects | `06_projects/` (P1–P4) | 🟡 P3 built (capstone) |
| 7 — RAG Patterns | `07_rag_learning/` (00–07) | ✅ Pre-existing |

### Tier 1 — Foundations
| # | Notebook | Key concepts |
|---|----------|--------------|
| 00 | [Environment Check](00_setup/00_environment_check.ipynb) | device detection (cuda/mps/cpu), `.env`, package checks |
| 01 | [Neural Networks](01_foundations/01_neural_networks.ipynb) | forward/backprop from scratch in NumPy, gradient descent, autograd |
| 02 | [Tokenization](01_foundations/02_tokenization.ipynb) | BPE from scratch, GPT-2 tokenizer, tokens vs words |
| 03 | [Embeddings](01_foundations/03_embeddings.ipynb) | cosine similarity, meaning maps (PCA), semantic search |
| 04 | [Attention Mechanism](01_foundations/04_attention_mechanism.ipynb) | scaled dot-product attention, contextual "Apple" demo, multi-head |
| 05 | [Transformer Architecture](01_foundations/05_transformer_architecture.ipynb) | blocks, residuals, layer norm, positional encoding, TinyGPT |
| 06 | [How LLMs Work](01_foundations/06_how_llms_work.ipynb) | next-token prediction, temperature, top-k/p, hallucination |

### Tier 2 — Training
| # | Notebook | Key concepts |
|---|----------|--------------|
| 07 | [Pretraining & Scaling](02_training/07_pretraining_and_scaling.ipynb) | next-token pretraining, compression, scaling laws (measured) |
| 08 | [Fine-tuning & LoRA](02_training/08_fine_tuning_and_lora.ipynb) | LoRA from scratch, adapter swapping/merging, QLoRA |
| 09 | [RLHF & Alignment](02_training/09_rlhf_and_alignment.ipynb) | reward model (Bradley–Terry), PPO + KL leash, DPO |
| 10 | [Quantization](02_training/10_quantization.ipynb) | symmetric/per-channel int8/int4, error cliff, memory |
| 11 | [Speculative Decoding](02_training/11_speculative_decoding.ipynb) | draft→verify, accept/reject identity proof, speedup |

### Tier 3 — Building with LLMs
| # | Notebook | Key concepts |
|---|----------|--------------|
| 12 | [Prompt Engineering](03_building/12_prompt_engineering.ipynb) | system vs user, delimiters, few-shot, structured output |
| 13 | [Context Windows & KV Cache](03_building/13_context_windows_and_kv_cache.ipynb) | token budget, O(n²) attention, KV cache, Anthropic prompt caching |
| 13b | [Serving LLMs at Scale with vLLM](03_building/13b_vllm_inference_serving.ipynb) | KV-cache bottleneck, PagedAttention, fragmentation, continuous batching, OpenAI-compatible server |
| 14 | [RAG Fundamentals](03_building/14_rag_fundamentals.ipynb) | chunk→embed→retrieve→generate, hallucination vs grounded (reuses `ragkit`) |
| 15 | [Vector Databases](03_building/15_vector_databases.ipynb) | brute-force vs ANN (FAISS HNSW/IVF), Chroma, Pinecone |
| 16 | [RAG vs CAG](03_building/16_rag_vs_cag.ipynb) | cold/cacheable vs hot/retrievable, cache hit-rate, cost/latency |
| 17 | [Chain of Thought](03_building/17_chain_of_thought.ipynb) | zero-shot/few-shot CoT, self-consistency voting |

### Tier 4 — Agent Engineering
Introduces **Claude SDK agents**, **LangGraph** (orchestration), and **LangSmith** (tracing).
| # | Notebook | Key concepts |
|---|----------|--------------|
| 18 | [What Is an Agent](04_agents/18_what_is_an_agent.ipynb) | agent vs workflow, the tool-call round-trip (raw SDK) |
| 19 | [Agent Loop From Scratch](04_agents/19_agent_loop_from_scratch.ipynb) | full raw loop, multi-tool, traced, budget enforcement |
| 19b | [Agent Loop (Minimal)](04_agents/19b_agent_loop_minimal.ipynb) | the same loop in ~20 lines, copy-paste ready |
| 20 | [Multi-Agent Patterns](04_agents/20_multi_agent_patterns.ipynb) | **LangGraph**: pipeline, fan-out, specialist-team routing |
| 21 | [Harness Engineering](04_agents/21_harness_engineering.ipynb) | Model=CPU/Context=RAM/Harness=OS, CLAUDE.md loader, **LangSmith** tracing |
| 22 | [Context Engineering](04_agents/22_context_engineering.ipynb) | Write / Select / Compress / Isolate primitives |
| 23 | [Loop Engineering](04_agents/23_loop_engineering.ipynb) | 6 loop patterns; adversarial maker/checker in depth |

### Tier 6 — Projects
| # | Notebook | Key concepts |
|---|----------|--------------|
| P3 | [Build a Research Agent (Capstone)](06_projects/P3_build_agent_from_scratch.ipynb) | synthesizes Tier 4: raw loop + LangGraph + LangSmith + harness + verify loop, writes a sourced report |

### Tier 7 — RAG Design Patterns (pre-existing)
See [07_rag_learning/](07_rag_learning/) — Naive RAG → Rerank → Multimodal → Graph → Hybrid → Agentic → Multi-Agent. These run with a Claude **or** fully-local (Ollama) backend on the "Helios Robotics" dataset. (Setup for Ollama/Neo4j is documented inside the first notebook.)

---

## Setup

This repo is managed with [`uv`](https://docs.astral.sh/uv/) (Python 3.13). Plain `pip` works too.

```bash
# Option A — uv (recommended)
uv sync

# Option B — pip
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Option C — conda
conda env create -f environment.yml && conda activate ai-learning
```

API keys (only needed from Tier 3 onward):

```bash
cp .env.example .env     # then fill in ANTHROPIC_API_KEY / OPENAI_API_KEY
```

**Tiers 1–2 run fully offline** — no API key required. A few notebooks download small open models (GPT-2, DistilBERT, MiniLM) on first run; they cache locally and fall back gracefully if you're offline. **Tiers 3–4 use `ANTHROPIC_API_KEY`** (and optionally `LANGSMITH_API_KEY` for tracing in notebooks 21–23 + P3) — but every live cell is guarded, so concept and code cells still run without a key. Live teaching calls default to a small, cheap model (`claude-haiku-4-5`); swap to `claude-opus-4-8` for production.

Launch:

```bash
uv run jupyter lab      # or: jupyter lab
```

---

## Start here

- **"I use AI tools but don't understand them"** → start at notebook **01** (Neural Networks) and go in order.
- **"I understand the basics, I want to build"** → skim Tier 1, then start at **12** (Prompt Engineering) and work through Tier 3.
- **"I want to build production agent systems"** → start at **18** (What Is an Agent), work through Tier 4, then build the **P3** capstone. Introduces Claude SDK agents, LangGraph, and LangSmith.

Every notebook lists its prerequisites in the header cell, so you always know what to read first.

---

## Notebook standard

Each notebook follows the same shape: **header** (tier, time, prerequisites, source) → **plain-English concept** → **minimal working example** → **visualization** → **3 exercises** (warm-up / apply / extend, with collapsed solutions) → **key takeaways + what's next**. See [.claude/CLAUDE.md](.claude/CLAUDE.md) for the full spec and content sources.
