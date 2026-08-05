
```markdown
# CLAUDE.md — AI Learning Notebook Repository

## Project Purpose

This repository is a self-paced, hands-on AI learning curriculum built from curated expert content.
Each notebook teaches one concept with clear explanations, working code, and practical exercises.
The goal is to take someone from "I use AI tools" to "I understand and build AI systems."

The curriculum is organized into 5 tiers that mirror a natural learning progression:
1. Foundations — how AI/LLMs actually work
2. Training & Improvement — how models are trained and aligned
3. Building with LLMs — RAG, caching, inference optimization
4. Agent Engineering — building systems that use LLMs
5. Evaluation & Production — measuring and shipping AI systems
6. All the existing notebooks from rag_learning
---

## Repository Structure

```
ai-learning-notebooks/
├── CLAUDE.md                        ← this file
├── README.md                        ← auto-generate from curriculum map
├── environment.yml                  ← conda env (or requirements.txt)
├── .env.example                     ← API key placeholders
│
├── 00_setup/
│   └── 00_environment_check.ipynb
│
├── 01_foundations/
│   ├── 01_neural_networks.ipynb
│   ├── 02_tokenization.ipynb
│   ├── 03_embeddings.ipynb
│   ├── 04_attention_mechanism.ipynb
│   ├── 05_transformer_architecture.ipynb
│   └── 06_how_llms_work.ipynb
│
├── 02_training/
│   ├── 07_pretraining_and_scaling.ipynb
│   ├── 08_fine_tuning_and_lora.ipynb
│   ├── 09_rlhf_and_alignment.ipynb
│   ├── 10_quantization.ipynb
│   └── 11_speculative_decoding.ipynb
│
├── 03_building/
│   ├── 12_prompt_engineering.ipynb
│   ├── 13_context_windows_and_kv_cache.ipynb
│   ├── 14_rag_fundamentals.ipynb
│   ├── 15_vector_databases.ipynb
│   ├── 16_rag_vs_cag.ipynb
│   └── 17_chain_of_thought.ipynb
│
├── 04_agents/
│   ├── 18_what_is_an_agent.ipynb
│   ├── 19_agent_loop_from_scratch.ipynb
│   ├── 20_multi_agent_patterns.ipynb
│   ├── 21_harness_engineering.ipynb
│   ├── 22_context_engineering.ipynb
│   └── 23_loop_engineering.ipynb
│
├── 05_evaluation/
│   ├── 24_llm_evals_fundamentals.ipynb
│   ├── 25_benchmark_hygiene.ipynb
│   ├── 26_llm_as_judge.ipynb
│   ├── 27_production_monitoring.ipynb
│   └── 27b_agent_evals.ipynb
│
├── 06_projects/
│   ├── P1_train_llm_from_scratch.ipynb
│   ├── P2_build_rag_pipeline.ipynb
│   ├── P3_build_agent_from_scratch.ipynb
│   └── P4_multi_agent_research_system.ipynb
│
├── 08_production/
│   ├── 28_structured_outputs.ipynb
│   ├── 29_serving_llm_apps.ipynb
│   ├── 30_security_and_guardrails.ipynb
│   ├── 31_mcp.ipynb
│   ├── 32_cost_engineering.ipynb
│   └── 33_ci_for_ai.ipynb
│
├── 09_frontier/
│   ├── 34_computer_use_and_browser_agents.ipynb
│   ├── 35_voice_and_realtime.ipynb
│   └── 36_data_engineering_for_ai.ipynb
│
└── 10_classic_ml/                       ← 🚧 planned, see its README + plan file
    ├── 37_ml_foundations_the_folk_wisdom.ipynb
    ├── 38_optimization_from_backprop_tricks_to_adam.ipynb
    ├── 39_trees_forests_and_boosting.ipynb
    ├── 40_the_sklearn_way.ipynb
    ├── 41_model_interpretability_shap.ipynb
    └── 42_spark_and_distributed_data.ipynb
And all the existing notebooks in 07_rag_learning.
```

---

## Notebook Standard

Every notebook MUST follow this exact structure:

### 1. Header Cell (Markdown)
```
# [Number]. [Topic Name]

**Tier:** [Foundations / Training / Building / Agents / Evaluation / Production / Frontier]
**Estimated time:** [X minutes]
**Prerequisites:** [list notebook numbers]
**Priority:** [🔴 Crucial / 🟡 Important / 🟢 Nice-to-have] — [one-line why]. *If skipped, revisit when:* [trigger].
**Source material:** [tweet author + URL this content is drawn from]

## What You'll Learn
- [bullet 1]
- [bullet 2]
- [bullet 3]

## Why This Matters
[2–3 sentences on the real-world relevance of this concept]
```

### 2. Concept Explanation (Markdown + minimal code)
- Explain the concept in plain English first
- Use analogies before formulas
- If math is involved, explain it in words before showing it symbolically
- Keep each explanation cell under 300 words

### 3. Minimal Working Example
- The simplest possible code that demonstrates the concept
- Every variable named descriptively
- Every non-obvious line has a comment
- Print or visualize output so the learner sees something happen

### 4. Visualization (where applicable)
- Use matplotlib, seaborn, or plotly
- Every plot has a title, axis labels, and a 1-sentence caption in the cell below it

### 5. Exercises
Each notebook must include exactly 3 exercises:
- **Exercise 1 (Warm-up):** Modify a parameter in the example and observe what changes
- **Exercise 2 (Apply):** Implement a small variation of the concept from scratch
- **Exercise 3 (Extend):** Connect this concept to a real-world use case or a later notebook topic

Exercises use this format:
```python
# Exercise 2: [Title]
# Task: [clear 1-sentence description]
# Hint: [one hint that doesn't give it away]

# YOUR CODE HERE
```

### 6. Key Takeaways (Markdown)
```
## Key Takeaways
- [3–5 bullet points that could stand alone as a study guide]

## What's Next
[One sentence connecting this to the next notebook in the sequence]
```

---

## Content Source Map

These are the primary sources this curriculum is built from. Use these as the intellectual foundation for each notebook.

### Foundations
- **Neural networks, tokenization, embeddings, attention, transformers, LLMs, context window, temperature, hallucination, prompt engineering, RLHF, fine-tuning, LoRA, quantization, RAG, vector databases, agents, chain-of-thought, diffusion models:** Full breakdown in @sairahul1's "20 AI Concepts You Must Understand in 2026" — https://x.com/sairahul1/status/2057740928908161461

### Stanford Curriculum (9-lecture series — free)
These lectures are the academic backbone of the curriculum. Use them as the authoritative source for notebook content in tiers 1 and 2.
- Lecture 1: Transformer fundamentals
- Lecture 2: Advanced transformer techniques (RoPE, ALiBi, sparse attention, BERT)
- Lecture 3: LLMs & inference optimization (MoE, KV cache, PagedAttention, prompting)
- Lecture 4: LLM training & fine-tuning (scaling laws, Flash Attention, LoRA, QLoRA)
- Lecture 5: LLM tuning (RLHF, PPO, DPO, preference tuning)
- Lecture 6: LLM reasoning (reasoning models, RL for reasoning, GRPO, scaling)
- Lecture 7: Agentic LLMs (RAG, function calling, agents, ReAct)
- Lecture 8: LLM evaluation (LLM-as-judge, biases, pitfalls)
- Lecture 9: Recap & current trends
- Source tweet: https://x.com/ajitcodes/status/2057043965317165490
- Detailed lecture summaries: https://x.com/technmak/status/2058129210733117602

### Speculative Decoding
- Core concept: GPU pipeline stalls solved by a small model guessing K tokens ahead, large model verifying in one forward pass (same CPU branch-prediction insight from the 1990s)
- Source: @_avichawla — https://x.com/_avichawla/status/2059192394713899228

### RAG vs. CAG
- RAG = dynamic retrieval from vector DB; CAG = static knowledge cached in KV memory
- Combining both: "cold" (cacheable) vs. "hot" (retrievable) data layers
- Claude achieves 92% cache hit-rate
- Source: @akshay_pachaar — https://x.com/akshay_pachaar/status/2056714042455343160

### LLMs as Compression Machines
- Pre-training is not just next-token prediction — it is learning the most efficient compression of human knowledge
- Compression → abstraction → reasoning
- Source: @hesamation summarizing 3Blue1Brown — https://x.com/hesamation/status/2064011673636147277

### Harness Engineering
- Agent = Model + Harness (Model is CPU, Context Window is RAM, Harness is OS)
- 5 harness artifacts: CLAUDE.md/AGENT.md files, JSON feature lists, session initialization routines, sprint contracts, structured task templates
- 5 universal principles: context beats instructions, separate planning from execution, feedback loops are non-negotiable, one thing at a time, the codebase IS the documentation
- Same model + better harness = up to +36 points on benchmarks
- Build to delete: harness components become overhead as models improve
- Source: @sairahul1 — https://x.com/sairahul1/status/2063544956158185927

### Loop Engineering
- The shift from prompting to designing *systems that prompt*
- 6 loop patterns: Fan-Out & Synthesize, Adversarial Verification, Tournament, Loop Until Done, Generate & Filter, Deep Verification
- Why solo prompting fails: agentic laziness, self-preferential bias, goal drift
- Source: @humzaakhalid — https://x.com/humzaakhalid/status/2064996712910041409
- Karpathy framing: @suryanshti777 — https://x.com/suryanshti777/status/2057389330625339902

### Multi-Agent Systems
- 3 patterns: pipeline (sequential), fan-out (parallel chunks), specialist team (domain collaboration)
- Design order: plan on paper first → define role/tools/output format per agent → build orchestration → enable dreaming → define outcome rubric → start with 2 agents
- Source: @akasheth_ — https://x.com/akasheth_/status/2063593827672461346

### LLM Engineering Projects Roadmap (build-first path)
- Build a tokenizer → embeddings → RoPE/ALiBi → attention → MHA → transformer block → train a mini-former → sampling → speculative decoding → KV cache → FlashAttention → LoRA → SFT/DPO/RLHF → RAG → agents → evals
- Source: @theahmadosman — https://x.com/theahmadosman/status/2062343535144436073

### Benchmark Hygiene & Evals
- Why training on test sets is a "cardinal sin" — it destroys the test set's purpose
- Contamination pathways: pretraining, instruction tuning, preference data, synthetic data, retrieval corpora, prompt overfitting
- Classical split discipline: split before preprocessing, freeze protocol before testing, separate dev evals from audit evals
- Source: @theahmadosman — https://x.com/theahmadosman/status/2064724789952958663

### Training LLM From Scratch (Project)
- Repo: "Train LLM From Scratch" by Fareed Khan — MIT license, builds a 2B parameter model on a single GPU using The Pile dataset
- Topics: transformer end-to-end in PyTorch, multi-head attention from scratch, training without OOM, text generation
- Source: @heynavtoor — https://x.com/heynavtoor/status/2056307663634612373
- `GITHUB_REPO_URL = "https://github.com/FareedKhan-dev/train-llm-from-scratch"` (MIT license, confirmed via GitHub API; found via WebSearch rather than the tweet's comments). Full pipeline: Data → Pretraining → SFT → Reward Model → DPO → PPO → GRPO, all hand-written PyTorch (no `trl`/`peft`/`transformers`). P1 draws on its pretraining/tokenizer/attention structure at a much smaller (~13M param, CPU-scale) size — see P1's own header for the adaptation.

### Agent Eval Gates
- Six-step architecture for gating agent-produced changes on evidence rather than trust: (1) judge bias hygiene — cross-family judging, panels for high-stakes calls, route objectively checkable facts to code not a judge; (2) verdicts wired into control flow — a score that doesn't change what runs next is a report, not a gate; (3) three-level grading (end-to-end / trajectory / component) since each catches a different failure class, with faithfulness as the metric that hides; (4) mine production traces for eval cases instead of inventing them, and verify the verifier before trusting it; (5) pin the judge version and log it with every score, one-line observable-outcome rubrics, never reward answer shape; (6) gate on blast radius not confidence — lanes by how expensive a mistake is to undo, evidence priority deterministic > trajectory > rollback history > model self-report, irreversible lanes never auto-open, shadow mode before enforcement.
- Source: shared via X (Twitter) thread, 2026 — exact author/URL not recovered by web search (the article's own distinctive closing lines did not surface a matching post).
- Built as `05_evaluation/27c_agent_eval_gates.ipynb` (🔴) + `agentkit/gates.py`, completing the CI-gate sketch left open in 27b's Exercise 3.

### Classic ML Papers (Tier 10 — planned)
Ten foundational papers supplied 2026-08-01; 8 map to the planned `10_classic_ml/` tier, 2 are transformer papers handled as cross-links. Full build plan: `~/.claude/plans/classic-ml-section.md`.
- **Efficient BackProp** — LeCun, Bottou, Orr, Müller 1998 — https://cseweb.ucsd.edu/classes/wi08/cse253/Handouts/lecun-98b.pdf → nb 38
- **Adam** — Kingma & Ba 2014 — https://arxiv.org/pdf/1412.6980 → nb 38
- **A Few Useful Things to Know About Machine Learning** — Domingos, CACM 2012 — https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf → nb 37
- **Random Forests** — Breiman 2001 — https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf → nb 39
- **XGBoost** — Chen & Guestrin 2016 — https://arxiv.org/pdf/1603.02754 → nb 39
- **Scikit-learn: Machine Learning in Python** — Pedregosa et al., JMLR 2011 — https://www.jmlr.org/papers/volume12/pedregosa11a/pedregosa11a.pdf → nb 40
- **A Unified Approach to Interpreting Model Predictions (SHAP)** — Lundberg & Lee, NeurIPS 2017 — https://proceedings.neurips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf → nb 41
- **Spark: Cluster Computing with Working Sets** — Zaharia et al., HotCloud 2010 — https://www.usenix.org/legacy/event/hotcloud10/tech/full_papers/Zaharia.pdf → nb 42
- **Attention Is All You Need** — Vaswani et al. 2017 — https://arxiv.org/pdf/1706.03762 → already taught (nb 04/05); add paper URL to their Source-material headers
- **BERT** — Devlin et al. 2018 — https://arxiv.org/pdf/1810.04805 → cross-link + planned small "encoder-only & MLM" concept cell in nb 05b

### AI Engineer Roadmap
- What AI engineers actually do in 2026: design agent loops, engineer context, write tools, add memory/durability/sandboxing, wire evals and CI regression gates
- 4 context primitives: Write, Select, Compress, Isolate
- Source: @sairahul1 — https://x.com/sairahul1/status/2062809249064141017

### Agentic AI Engineer 6-Month Roadmap
- 12-stage practitioner roadmap: async Python → LLM fundamentals → tool calling/structured outputs → memory & state → single-agent ReAct → multi-agent supervisor → human-in-the-loop → evals → observability → security → production deployment → ship in public
- Root-cause framing for real agent failures: blocking code under load, no eval suite, no tracing — in that order
- Source: @sairahul1 — "How To Become an Agentic AI Engineer in 6 Months" — https://x.com/sairahul1/status/2074790798584062278
- Gap analysis (2026-07-08) found 9/12 stages already covered (usually deeper) by the existing curriculum; 3 genuine gaps closed as notebooks 19c (async patterns, 🔴), 22b (agent memory, 🟡), 30b (human-in-the-loop, 🟡). Full plan: `~/.claude/plans/agentic-roadmap-gap-notebooks.md`.

### Real-World Source Repos (OpenViking & Citadel)
Two production/experimental systems studied source-level to find depth the curriculum lacked. We teach their *patterns* and write original code (both are copyleft — OpenViking AGPL-3.0, Citadel GPL-3.0 — so no code is copied).
- **OpenViking** (Volcengine) — production context database for AI agents: hierarchical/recursive retrieval, tiered L0/L1/L2 context loading, memory hotness lifecycle, session memory extraction, LOCOMO/LongMemEval memory benchmarks. https://github.com/volcengine/OpenViking (`retrieve/`, `session/`, `benchmark/`).
- **The Sovereign Imperia Citadel** — deterministic engineering brain: AST symbol index + import DAG (zero-token retrieval), capability-based security (`fasces`/leases/pomerium/dual-validator gate), content-addressed `.legion` cache + Bloom filter, leased verify-before-count worker pool. https://github.com/Hvuj/The-Soverign-Imperia-citadel (`services/index/`, `services/authority/`, `services/compile/`, `services/army/`).
- Gap analysis (2026-07-21) closed 5 notebooks: **16b** deterministic retrieval (🔴), **30c** capability-based security (🔴), **07_rag_learning/08** hierarchical+tiered retrieval (🟡), **22c** memory lifecycle+extraction (🟡), **32b** content-addressed caching (🟢). Full plan: `~/.claude/plans/command-name-model-command-name-command-polymorphic-meadow.md`.


---

## API Keys & Environment

**USER ACTION REQUIRED:** Before Claude Code begins generating notebooks, create a `.env` file in the repo root with the following. Claude Code will read `.env.example` as the template but will NOT write real keys anywhere.

```
# .env.example — copy this to .env and fill in your keys

# Anthropic (required for agent notebooks 18–23)
ANTHROPIC_API_KEY=your_key_here

# OpenAI (optional, used for comparison examples)
OPENAI_API_KEY=your_key_here

# Hugging Face (required for local model notebooks 08, 10, P1)
HF_TOKEN=your_token_here

# Pinecone (optional, used in notebook 15 — vector databases)
PINECONE_API_KEY=your_key_here
PINECONE_ENV=your_environment_here

# LangSmith (optional, used in notebook 21 — harness engineering)
LANGSMITH_API_KEY=your_key_here
LANGSMITH_PROJECT=ai-learning-notebooks
```

For notebooks that require an API key the user hasn't provided, include a clearly marked cell:
```python
# ⚠️ THIS NOTEBOOK REQUIRES AN API KEY
# Set ANTHROPIC_API_KEY in your .env file before running
# If you don't have one yet, the concept explanation cells will still work —
# skip the API call cells and return when you have a key.
```

---

## Python Environment

Target: Python 3.11+

Core dependencies (include in `environment.yml` and `requirements.txt`):
```
torch>=2.2.0
transformers>=4.40.0
anthropic>=0.25.0
openai>=1.20.0
langchain>=0.2.0
langgraph>=0.1.0
numpy>=1.26.0
pandas>=2.2.0
matplotlib>=3.8.0
plotly>=5.20.0
scikit-learn>=1.4.0
datasets>=2.18.0          # Hugging Face datasets
tokenizers>=0.19.0
faiss-cpu>=1.8.0          # for vector search in notebook 15
python-dotenv>=1.0.0
jupyter>=1.0.0
ipywidgets>=8.1.0
tqdm>=4.66.0
```

---

## How to Generate Notebooks

Build notebooks in tier order. Do not skip ahead — later notebooks depend on earlier ones.

### Phase 1: Foundations (Tier 1)
Start here. These notebooks have no API key requirements and run fully locally.
Build: notebooks 01–06 + 00_setup

### Phase 2: Training (Tier 2)
Build: notebooks 07–11
Note: notebook 10 (quantization) and P1 (train from scratch) require a GPU or a free Google Colab session. Include Colab-compatible code.

### Phase 3: Building with LLMs (Tier 3)
Build: notebooks 12–17
Requires ANTHROPIC_API_KEY for notebooks 13, 16.

### Phase 4: Agent Engineering (Tier 4)
Build: notebooks 18–23
All require ANTHROPIC_API_KEY.

### Phase 5: Evaluation (Tier 5)
Build: notebooks 24–27
Requires ANTHROPIC_API_KEY for 26–27.

### Phase 6: Projects
Build: P1–P4
These are capstone notebooks that synthesize multiple tiers. Build after all tier notebooks are complete.

---

## Specific Notebook Instructions

### Notebook 04: Attention Mechanism
This is the most important notebook in Tier 1. Spend extra care here.
- Start with the "Google Maps for words" analogy (words as locations, attention as finding what's nearby in meaning-space)
- Implement scaled dot-product attention from scratch in NumPy before using PyTorch
- Visualize the attention matrix as a heatmap for a sample sentence
- Show how "Apple" attends differently in "I ate an Apple" vs "I bought Apple stock"
- Exercise 3: implement multi-head attention and show how different heads attend to different relationships

### Notebook 11: Speculative Decoding
- Open with the CPU branch prediction analogy from @_avichawla (1990s CPU pipeline stalls → GPU decoding stalls)
- Diagram: show the standard decode loop (one token at a time, GPU idle) vs speculative decode (small model guesses K tokens, large model verifies in one pass)
- Implement a toy version: a small n-gram model as the "draft model," a simple transformer as the "verifier"
- Show that output distribution is mathematically identical regardless of whether speculation was accepted
- Include a timing benchmark cell

### Notebook 14: RAG Fundamentals
- Use a concrete example: a company handbook the model wasn't trained on
- Build the full pipeline from scratch: chunking → embedding → storing → retrieving → generating
- Visualize similarity scores for a query against document chunks
- Show a hallucination happening without RAG, then the same query corrected with RAG

### Notebook 16: RAG vs. CAG
- Source: @akshay_pachaar
- Implement both patterns side-by-side using the Anthropic API
- Use a concrete split: "static" = product documentation (cached), "dynamic" = recent support tickets (retrieved)
- Measure and display latency and token cost for each approach
- Show the 92% cache hit-rate concept with a simulated workload

### Notebook 19: Agent Loop From Scratch
- Build without any framework — raw Anthropic SDK only (~100 lines of Python)
- The loop: call model → parse tool_use blocks → execute tool → append tool_result → repeat until stop_reason == "end_turn"
- Tools to include: web_search (mock), read_file, write_file
- Print every step of the trace so the learner sees exactly what's happening
- Exercise 3: add a budget limit — if more than N tool calls, the agent should summarize and stop

### Notebook 21: Harness Engineering
- Source: @sairahul1
- This is the conceptual centrepiece of Tier 4
- Start with the OS analogy: Model = CPU, Context = RAM, Harness = OS
- Demonstrate the harness performance gap: show two equivalent agent prompts, one with proper CLAUDE.md + session initialization, one without — compare output quality
- Implement: a CLAUDE.md loader, a JSON feature list tracker, a session initialization routine
- Exercise 3: implement the "build to delete" test — toggle a harness component on/off and measure whether output quality changes

### Notebook 23: Loop Engineering
- Source: @humzaakhalid + @suryanshti777 (Karpathy framing)
- Show the 3 failure modes of solo prompting with concrete examples: agentic laziness, self-preferential bias, goal drift
- Implement all 6 loop patterns with working code:
  1. Fan-Out & Synthesize
  2. Adversarial Verification (two separate Claude calls: maker + checker)
  3. Tournament (generate 5, judge against rubric, pick winner)
  4. Loop Until Done (iterate until condition is satisfied)
  5. Generate & Filter
  6. Deep Verification
- The adversarial verification pattern is the most important — spend the most time on it

### Notebook 25: Benchmark Hygiene
- Source: @theahmadosman
- Open with: "If a student gets the final exam while studying, a perfect score no longer measures mastery. It measures access."
- Demonstrate train/validation/test split contamination visually — show how a model can appear to improve while actually just memorizing
- Cover the contamination taxonomy: exact, near-duplicate, semantic, translation, synthetic-data, retrieval, prompt-overfitting
- Include a checklist cell the learner can use before publishing any model evaluation

### Project P1: Train LLM From Scratch
- Based on Fareed Khan's GitHub repo (MIT license)
- **USER ACTION REQUIRED:** Paste the GitHub repo URL here after finding it in the tweet comments: https://x.com/heynavtoor/status/2056307663634612373
- Build step by step: tokenizer → embeddings → multi-head attention → transformer block → training loop → text generation
- Target: a 13M parameter model on CPU, with notes on how to scale to 2B on a single A100
- Make the notebook Colab-compatible (include a GPU check cell at the top)

### Project P3: Build Agent From Scratch
- Synthesizes notebooks 18–23
- Full agent with: raw SDK loop + CLAUDE.md loading + session initialization + JSON progress tracking + adversarial verification loop + budget enforcement
- Target task: a research agent that takes a question, searches for sources, synthesizes findings, verifies its own output, and writes a structured report to disk

---

## Style Guidelines

- **Voice:** Clear, direct, never condescending. Write to someone smart who is new to this specific topic.
- **Analogies first:** Always explain what something *is like* before explaining what it *is*.
- **Show, don't just tell:** If you claim X is faster than Y, include a timing cell that demonstrates it.
- **Honest about limits:** If an exercise requires a paid API key the user may not have, say so clearly and provide a mock/stub alternative.
- **No magic:** Never use `import magic_library; magic_library.do_the_thing()` without first showing the learner what's happening inside.
- **Progressive complexity:** Each notebook assumes the user has completed all prior notebooks in the tier. Don't re-explain concepts covered earlier — link back instead.

---

## README Generation

After all notebooks are complete, generate a `README.md` that includes:
- A visual curriculum map (ASCII or Mermaid diagram)
- Time estimates per tier
- Setup instructions (conda env + .env file)
- A "Start Here" section for three different learner profiles:
  - "I use AI tools but don't understand them" → start at notebook 01
  - "I understand the basics but want to build" → start at notebook 12
  - "I want to build production agent systems" → start at notebook 18

---

## What Claude Code Should Ask Before Starting

Before generating any notebook, confirm with the user:

1. **Preferred API:** Anthropic (Claude) or OpenAI (GPT)? This determines which SDK is used in Tier 3+ notebooks. Default: Anthropic.

2. **Local model support:** Do you have a GPU available locally, or should GPU-required notebooks (08, 10, P1) be Colab-compatible? Default: Colab-compatible.

3. **Depth preference:** Should exercises include full solutions, partial hints only, or no solutions? Default: partial hints with full solutions in a collapsed cell.

4. **Starting point:** Which tier do you want to generate first? Default: Tier 1.

5. **Missing GitHub URL:** The "Train LLM From Scratch" repo URL by Fareed Khan is referenced in Project P1. Find it in the comments of https://x.com/heynavtoor/status/2056307663634612373 and paste it here before Project P1 is generated.

---

## Build Status & Established Conventions

> This section records decisions made while building, so future sessions stay consistent. Update it as tiers are completed.

### Progress
- ✅ **Scaffolding** — tier directories (`00_setup` … `06_projects`), `.env.example`, `requirements.txt`, `environment.yml`, curriculum `README.md`. Existing RAG notebooks moved to `07_rag_learning/`.
- ✅ **Tier 1 — Foundations (00–06)** — built and executed clean: `00_setup/00_environment_check`, `01_foundations/01_neural_networks` … `06_how_llms_work`.
- ✅ **Tier 2 — Training (07–11)** — built and executed clean: `02_training/07_pretraining_and_scaling` … `11_speculative_decoding`.
- ✅ **Tier 3 — Building (12–17, +13b)** — built and executed clean: `03_building/12_prompt_engineering` … `17_chain_of_thought`. RAG notebooks (14/15/16) reuse `ragkit` and link out to `07_rag_learning/` rather than re-teaching it. **13b `vllm_inference_serving`** added (serving lens after KV cache): PagedAttention as OS paging, fragmentation/utilization sim, continuous vs static batching, OpenAI-compatible `vllm serve`. Fully offline-safe (no GPU/`vllm` install needed — `vllm` requires CUDA/Linux); live OpenAI-client cell guarded by a localhost:8000 `/health` probe (`HAS_VLLM_SERVER`).
- ✅ **Tier 4 — Agents (18–23, +19b)** — built and executed clean. Introduces three lenses: **Claude SDK** agents (18/19/19b), **LangGraph** orchestration (20), **LangSmith** tracing (21+). 19 = in-depth raw loop; 19b = ~20-line minimal version (user asked for both). 21 harness, 22 context primitives, 23 six loop patterns.
- ✅ **Tier 6 capstone — `06_projects/P3_build_agent_from_scratch.ipynb`** — research agent synthesizing all of Tier 4 (raw budgeted loop + LangGraph 5-stage graph + adversarial verify→revise cycle + harness + LangSmith trace), writes a sourced report to disk. Built & executed clean.
- ✅ **Tier 5 — Evaluation (24–27, +27b)** — built and executed clean: `05_evaluation/24_llm_evals_fundamentals` (golden dataset + exact/rubric/model-graded scorers + pass@k + error taxonomy) … `27_production_monitoring` (LangSmith tracing, cost/latency, drift detection, canary rollout) … `27b_agent_evals` (trajectory scoring, tool-call correctness, mini task suite, cost-per-solved-task, measures the harness +36-point claim directly). Every notebook's header now carries a **Priority** line (🔴/🟡/🟢 + why + when-to-revisit-if-skipped) — see the gap-filling plan for the full rationale.
- ✅ **Tier 8 — Production & Safety (28–33)** — built and executed clean: `08_production/28_structured_outputs` (tool-forced schema + Pydantic + validate→repair) … `29_serving_llm_apps` (real FastAPI+uvicorn subprocess, SSE streaming, timeout/fallback, concurrency) … `30_security_and_guardrails` (lethal trifecta, live prompt-injection demo against notebook 19's shape, least-privilege/guardrails/sandboxing/human-gate defenses) … `31_mcp` (FastMCP server over stdio + client, wired into an agent loop) … `32_cost_engineering` (model routing, prompt-cache economics, batch API, token budgets) … `33_ci_for_ai` (regression gate reusing nb24's harness, GitHub Actions example, canary rollout — explicitly mapped to this repo's own `.claude/checks/` + `/loop`).
- ✅ **Tier 9 — Frontier (34–36)** — built and executed clean: `09_frontier/34_computer_use_and_browser_agents` (real vision+tool-use loop clicking through a PIL-rendered mock calculator; accessibility-tree vs. pixel action-space comparison) … `35_voice_and_realtime` (STT→LLM→TTS latency budgeting, real OpenAI TTS/STT round trip, barge-in state machine) … `36_data_engineering_for_ai` (incremental embedding sync, corpus dedup/chunk-QA, synthetic-data generation with notebook-25 contamination scanning, trace-storage schema design).
- ✅ **Tier 6 — Projects, all four capstones built and executed clean:**
  - `P1_train_llm_from_scratch` — real GitHub URL found via WebSearch and recorded above. A genuine ~14.3M-param decoder-only transformer (char tokenizer, hand-written causal multi-head attention, transformer blocks, `forward_hidden()` seam) trained 300 steps on MPS (~30s), loss 3.39→0.08, with a clean before/after generation comparison (trained model reproduces corpus phrases; untrained model produces gibberish).
  - `P2_build_rag_pipeline` — composes existing `ragkit` pieces (no new retrieval code) into one pipeline function, then adds what Tier 3/`07_rag_learning` never had: retrieval evals (hit-rate@k, MRR) against a golden (question → expected source file) set, faithfulness judging (notebook 26's pattern), and a chunk-size regression gate (notebook 33's exact shape). All real metrics: 100% hit-rate, 0.75 MRR, 100% faithfulness on the Helios corpus.
  - `P4_multi_agent_research_system` — extends P3 into a LangGraph researcher→writer→critic team with a GRAPH-WIDE tool budget, notebook 28 structured output (Pydantic-validated report via forced tool call), notebook 30's `sanitize_tool_output` guardrail against a poisoned mock-KB entry, LangSmith tracing, and a notebook 27b-style eval suite (solve rate, trajectory score, cost-per-solved-task).
- ✅ **Agentic-roadmap gap notebooks — CLOSED (2026-07-08).** All 3 gaps found vs. the @sairahul1 "6-month agentic engineer" PDF (see Content Source Map entry above) are built and executed clean:
  - `04_agents/19c_async_agents.ipynb` (🔴) — `asyncio.gather` fan-out, semaphore-bounded concurrency, backoff+jitter retry, batch failure isolation, async-ified notebook-19 tool execution; live `AsyncAnthropic` calls verified.
  - `04_agents/22b_agent_memory.ipynb` (🟡) — unified `AgentMemory` class (short-term/working/long-term/episodic), persisted to disk; a two-session demo (`session_1` writes facts + logs an episode then is deleted, a fresh `session_2` pointed at the same directory recalls both by exact key and by similarity via notebook 22's `embed`/`cosine_similarity`) proves cross-session persistence rather than just asserting it.
  - `08_production/30b_human_in_the_loop.ipynb` (🟡) — risk-tiered `assess_risk()`, a headless-safe scripted `ApprovalPolicy` (no `input()`, so `notebooks.sh` can't hang), a JSONL audit trail, and pause/resume via state-file serialization (a genuinely different process can `resume_run()` off disk with no reference to the original run).
  - README.md's Tier 4/8 tables, mermaid map, and 🔴-only fast path (19c only — 22b/30b are 🟡) all updated to match. Full plan: `~/.claude/plans/agentic-roadmap-gap-notebooks.md`.
- ✅ **Gap-filling plan — CLOSED.** Every tier from the original audit (Tier 5 evals, Tier 8 production/safety, Tier 9 frontier, Tier 6 capstones) is built, and each notebook plus each tier-batch has been executed clean individually (`tools/run_nb.py` per notebook; `.claude/checks/notebooks.sh <tier>/*.ipynb` per tier — all 52 notebooks passed). `README.md` carries a full priority-labeled triage table for every notebook across every tier (existing tiers 1–4/7 labeled retroactively in the README; new tiers 5/6/8/9 labeled in both their own headers and the README), plus the curriculum map mermaid diagram, "🔴-only fast path" reading order, and a 4th learner profile. **A combined full-repo sweep (`.claude/checks/notebooks.sh` with no args, all 52 in one run) was attempted but deliberately not completed** — Python block-buffers stdout when redirected to a file, so a run gives no visible progress until it finishes or the buffer fills; after ~11 minutes with zero PASS/FAIL lines there was no way to tell "working through slow notebooks" from "hung," and the earlier two silent-death attempts were likely the same blind spot rather than an actual failure. Given every notebook already passed individually, a blind multi-hour combined run (live API calls + model loads × 52) wasn't judged worth it — decided with the user 2026-07-05. If ever revisited: rerun with `PYTHONUNBUFFERED=1`, and note the nohup'd python detaches from the wrapper bash, so kill the underlying `python -` heredoc pid (and any `ipykernel_launcher` children) directly, not just the `notebooks.sh` bash pid. Full plan at `~/.claude/plans/write-a-plan-to-zippy-meerkat.md`.
- ✅ **OpenViking/Citadel gap notebooks — CLOSED (2026-07-21).** 5 notebooks built from a source-level study of two real-world systems (see Content Source Map > "Real-World Source Repos"), each executed clean individually via `.claude/checks/notebooks.sh`: `03_building/16b_deterministic_retrieval` (🔴, AST symbol index + import DAG + Tarjan, zero-token vs embedding), `08_production/30c_capability_based_agent_security` (🔴, fasces tokens + attenuation + leases + zone policy + dual-validator gate wired into the nb19 loop shape), `07_rag_learning/08_hierarchical_and_tiered_retrieval` (🟡, recursive convergence/dominance + intent planning + L0/L1/L2 degradation), `04_agents/22c_memory_lifecycle_and_extraction` (🟡, hotness/eviction + typed session extraction + LOCOMO-style recall eval), `08_production/32b_content_addressed_caching` (🟢, hash-keyed store + Bloom filter + leased verify-before-count pool). README triage tables (Tiers 3/4/7/8), mermaid map, and 🔴 fast path (added 16b + 30c) all updated. **Env note for THIS session:** fresh clone needs `uv sync` (no `.venv` on checkout); ANTHROPIC_API_KEY absent and HF/embeddings are proxy-blocked here, so all 5 notebooks were written offline-safe — real `ragkit.embed` is guarded and falls back to a deterministic char-n-gram vector (`ProxyError` → fallback), and the one live LLM path (22c extraction) has a rule-based fallback. All 5 execute clean regardless.
- ✅ **ai-engineering-from-scratch gap notebooks — CLOSED (2026-07-23).** Compared this curriculum against `rohitg00/ai-engineering-from-scratch` (503 lessons, 20 phases — a much broader textbook covering math/CV/speech/RL this repo never scoped). Three genuine gaps sat inside this repo's own LLM/agent-engineering lane and were closed, each executed clean individually via `.claude/checks/notebooks.sh` then `tools/run_nb.py` for persisted outputs: `02_training/07b_distributed_training` (🟡, real multi-process gloo collectives via subprocess workers — `all_reduce`/`all_gather`/`reduce_scatter`, a numerically-verified DDP gradient-equals-single-process proof, hand-rolled ZeRO-1 sharding, real `FullyShardedDataParallel`, pipeline `send`/`recv` + GPipe bubble-fraction sim, grad accumulation + activation checkpointing), `01_foundations/05b_moe_and_attention_variants` (🟡, real top-k gated MoE with a measured load-balancing-loss effect on router collapse, one parameterized MHA/MQA/GQA module + KV-cache bytes, a from-scratch RoPE verified to have relative-position-only scores to 1e-7, sliding-window + ALiBi masks, FlashAttention-vs-naive equivalence, live HF `config.json` grounding against Mistral-7B/Mixtral-8x7B/Phi-3-mini), `04_agents/20b_agent_framework_tradeoffs` (🟡, the identical tool-using task run through raw SDK + LangGraph in-kernel and CrewAI/AutoGen/OpenAI-Agents-SDK in an isolated subprocess venv, all measured through one shared metering gateway). README triage tables (Tiers 1/2/4), mermaid map, and Setup section all updated; fast path unchanged (all three are 🟡).
  - **Isolated `.venv-frameworks` + metering-gateway pattern (new for this repo):** `crewai` requires `rich<15`; this repo pins `rich>=15.0.0` (used by `ragkit.pretty`) — confirmed via `uv pip compile`, not assumed, and a combined resolution also drags `torch`/`transformers`/`chromadb` to different versions across every other notebook. Built via `tools/setup_frameworks_venv.sh` (creates `.venv-frameworks`, gitignored, NOT part of `uv sync`) — `crewai` + `autogen-agentchat` + `autogen-ext[anthropic]` + `openai-agents[litellm]` + `anthropic` + `python-dotenv`, 146 packages, zero conflicts with the main `.venv`. 20b's gateway (a small FastAPI proxy to `api.anthropic.com`, logging real `usage` blocks) is the metering ground truth every implementation is measured against — every client, in-kernel or isolated, is configured with a **dummy** API key, and the gateway substitutes the real one server-side, so no framework subprocess ever holds the real credential. Per-framework routing quirks discovered empirically: CrewAI's `anthropic/` model prefix routes through its **native** SDK (not litellm) and only honors `ANTHROPIC_BASE_URL` as an env var, not the `LLM(api_base=...)` field; `autogen-ext`'s `AnthropicChatCompletionClient` needs an explicit `model_info` dict for any model string not in its built-in registry (`claude-haiku-4-5-20251001` isn't) or it raises "model does not support function calling"; `crewai`'s `Crew(tracing=False)` + `CREWAI_TRACING_ENABLED=false` env var together are required to keep a first run fully headless (otherwise it prints an interactive-looking "Tracing Preference Saved" console box).
  - **gloo-on-macOS findings (07b):** `torch.distributed` gloo collectives work natively on this Mac (`dist.init_process_group("gloo")` + `all_reduce`/`reduce_scatter`/`all_gather` all verified across up to 4 real subprocesses) — `nccl` is unavailable (expected, GPU-only). `FullyShardedDataParallel` on CPU/gloo raises `AttributeError: module 'torch.mps' has no attribute 'current_device'` unless constructed with an explicit `device_id=torch.device("cpu")` — FSDP otherwise auto-detects MPS as the accelerator and tries to query it even for a CPU-only job. Once passed, FSDP shards correctly (170/340 params per rank on a 2-rank job — exact 50/50 split, verified not assumed).
  - **`nbclient`'s actual cwd, corrected:** the earlier "confirmed empirically" note that `nbclient` runs with cwd = the notebook's own directory was wrong in general — `.claude/checks/notebooks.sh` explicitly `cd`s to the repo root first, and `tools/run_nb.py` inherits whatever cwd it's invoked from (verified directly: a bare `NotebookClient(nb).execute()` with no `resources` reports `os.getcwd()` as wherever the *calling process* started, not the notebook's path). P2's `sys.path.insert(0, "..")` happened to work because of how that session invoked the runner, not because of an nbclient guarantee. Any notebook that needs to locate the repo root (20b does, to find `.venv-frameworks`) should search upward for a marker file (e.g. `pyproject.toml`) rather than hardcode a relative `..` — see 20b's `find_repo_root()` helper.
  - **RoPE plane-selection gotcha (05b):** `rope_freqs()[0]` is `theta**0 == 1.0` for every `theta` by construction — sweeping `theta` and reading the angle off the *first* frequency plane shows no effect at all (a real bug caught by checking the printed numbers, not assumed correct). `theta`'s effect only shows on later (slower) planes — use `freqs[-1]` to demonstrate the long-context-extension lever.
- ✅ **Content-gap notebooks + `agentkit` — CLOSED (2026-07-27).** A coverage audit against a 22-topic "AI Engineer must-learn" list found 14 topics fully covered, 5 partial, 3 fully missing. Closed with a new top-level importable package (`agentkit/` — mirrors `ragkit/`, ~350 lines, pure numpy+stdlib, no torch/chroma/anthropic imports since embed fns are injected) plus 4 notebooks, each executed clean individually via `.claude/checks/notebooks.sh`: **`03_building/13c_inference_economics`** (🔴, prefill-vs-decode measured live on real GPT-2 on MPS via `torch.mps.synchronize()`, FP8/INT8/NF4 grid-error comparison, a *measured* "when quantization hurts" — naive INT4 raised GPT-2 perplexity ~24x, AWQ-style salient-channel protection recovered most of it — a real Hinton-distillation demo on sklearn moons, `agentkit.SemanticCache` built and used for the first time with its false-hit/staleness failure modes demonstrated on real Helios-corpus embeddings, and a capstone fine-tune/ICL/RAG/distillation decision framework), **`05_evaluation/24b_retrieval_and_citation_evals`** (🟡, precision@k/recall@k/nDCG@k with graded relevance built from scratch, a real embedding-vs-BM25 divergent-metric example found empirically over a hand-graded Helios chunk corpus, a stale-vs-fresh-chunk retrieval demo with a recency rescore, live citation-validity/support/coverage scoring), **`08_production/28b_tool_contracts_and_reliability`** (🔴, hardens nb19's bare `TOOL_IMPLEMENTATIONS[name](**args)` line with `agentkit.contracts.checked_execute` — hallucinated-tool detection, schema+semantic validation, a real idempotency-key proof against a `REFUND_LEDGER` double-fire, a measured retries-vs-fallback success-rate staircase 26%→58%→100% on a seeded flaky backend), **`08_production/30d_multi_tenant_isolation`** (🟡, the *same* `SemanticCache` from 13c reused as the cross-tenant attack surface — measured contamination persisting at 71% even at threshold=0.99, proving threshold tuning is not a structural fix — `NamespacedStore` contamination@k, a cross-user memory-leak demo, and `CostLedger` per-tenant-per-journey attribution wired into 28b's `checked_execute` via a `pre_hooks` budget gate). README triage tables (Tiers 3/5/8), mermaid map, and 🔴 fast path (added 13c, 28b) all updated. Full plan: `~/.claude/plans/write-a-plan-to-eager-flame.md`.
  - **`agentkit` design rule:** plumbing learners REUSE and exercises MUTATE goes in the package (`ToolContract`/`checked_execute`, `SemanticCache`, `TenantContext`/`NamespacedStore`/`CostLedger`); one-off demos, golden sets, and workloads stay in-notebook. One-directional interlock, no back-edges: `semcache` built in 13c → attack surface in 30d; `contracts` built in 28b → budget-gated in 30d via `CostLedger.make_budget_hook` as a `checked_execute` `pre_hook`. `24b` has no agentkit dependency at all.
  - **`lint.sh` was extended** (not edited-to-pass — a coverage extension, same commit that created `agentkit/`) to parse `agentkit/**/*.py` alongside `ragkit/**/*.py`. No other check script or `uv add` was needed — every dependency (torch, transformers, rank_bm25, pandas, matplotlib, anthropic, sentence-transformers) was already present.
  - **MPS timing gotcha (13c):** `torch.mps.synchronize()` must bracket every prefill/decode timer or the GPU queue reports near-zero elapsed time for enqueued-but-not-yet-run work; a warmup call (pays a one-time JIT cost) must run and be discarded before the measured sweep, or the first data point is polluted. GPT-2's 1024-token context caps how long a `_source_text` needs to be for a `prompt_len=512` slice — repeat the source string enough times up front rather than discovering a silent truncation mid-sweep.
  - **Validator ordering gotcha (28b):** `agentkit.contracts.validate_args` always runs the schema type-check AND the contract's semantic `validator` — it does not short-circuit after a schema failure. A hand-written validator that assumes a field is already the right type (e.g. `0 < amount <= 100` on a value that might be the string `"fifty"`) will raise inside the validator itself instead of returning a clean error string; guard with `isinstance` first. Caught by actually running the notebook, not by inspection.
  - **Golden-set grading needs real chunk boundaries, not assumed ones (24b):** `chunk_text`'s word-count-based chunking splits FAQ Q&A pairs mid-answer unpredictably — hand-authoring a `{chunk_id: grade}` golden set requires dumping the ACTUAL chunk boundaries first (`chunk_text(doc, chunk_size=80, overlap=15)` and print each chunk) rather than guessing which chunk a fact landed in; several planned grades were wrong on the first pass until checked against real output.
  - **Cross-tenant contamination needs near-identical phrasing to survive high thresholds (30d):** loosely-worded cross-tenant paraphrases got filtered out by a 0.90+ similarity threshold, weakening the "threshold tuning doesn't fix contamination" claim; real persistence (71% contamination at threshold=0.99) only showed up once the two tenants' questions were worded almost identically — which is also the *realistic* case, since unrelated customers of the same product genuinely do phrase the same category of question the same way.
- ✅ **Agent eval gates — CLOSED (2026-08-02).** Completes the CI-gate sketch left open in 27b's Exercise 3 (see Content Source Map > "Agent Eval Gates" above for the six-step architecture and source). Added `agentkit/gates.py` (191 lines, stdlib+numpy only, no anthropic import — `JudgeConfig.call_fn` is injected, same rule as every other agentkit module): `BlastRadius`/`EvidenceSource` enums + `EVIDENCE_WEIGHTS` (deterministic > trajectory > rollback history > model self-report), `Evidence`/`Verdict`/`JudgeConfig` dataclasses, `cross_family_warnings`, `judge_verdict`, `Action` enum + `verdict_to_action` (the thermostat mapping: schema errors → BLOCK_EDGE, fabrication → QUARANTINE, low grounding → REJECT_HANDOFF, verified completion → END_RUN), `LanePolicy`/`DEFAULT_LANES`, `GateDecision`/`MergeGate` (shadow-mode scoring + `disagreement_rate`, with the IRREVERSIBLE lane's `auto_open=False` checked structurally before any evidence score). New notebook `05_evaluation/27c_agent_eval_gates.ipynb` (🔴, 26 cells) re-inlines 27b's agent/scorers, adds four `CANNED_RUNS` (good / ungrounded / schema-violating / fabricated-completion) so every gate/pipeline/mining/viz cell is offline-exercised regardless of API key, then walks the six steps end to end: judge-family-collision detection + routing an objective fact to a deterministic check instead of a judge call; a control-flow pipeline mapping each canned run to its correct `Action` (verified via printed output: end_run / reject_handoff / block_edge / quarantine); a three-level `grade_run` with a matplotlib bar chart showing the fabrication run passing end-to-end while failing faithfulness; trace mining into archetypes + a verify-the-verifier assertion pair; a `grounding-v1` vs `grounding-v2` rubric comparison plus a self-report-on-a-fabrication demo; and a `MergeGate` walkthrough over three simulated changes by blast radius, where `shared_config_change` lands exactly on `REVERSIBLE_WIDE`'s evidence floor (0.85) and `prod_data_deletion` never opens despite a perfect evidence score. Executed clean via `tools/run_nb.py` with no `ANTHROPIC_API_KEY` present (all live-judge cells report `[skipped: ...]`, control-flow/gate results unaffected). README triage table (Tier 5), mermaid map, and 🔴 fast path (added 27c) all updated; 27b's "What's Next" cell now points at 27c before Tier 8. No new dependencies; `lint.sh`/`notebooks.sh` glob coverage (`agentkit/**`, `0[0-9]_*`) already covers both new files.

- ✅ **Tier 10 — Classic ML (37–42) — CLOSED (2026-08-02).** All 6 notebooks built from 8 papers and executed clean individually via `.claude/checks/notebooks.sh`, fully offline (sklearn datasets only, no API keys): `37_ml_foundations_the_folk_wisdom` (🔴 Domingos — generalization/bias-variance decomposed numerically via fresh-draw resampling, not bootstrap-of-fixed-sample, which blows up a degree-15 polynomial's conditioning; curse of dimensionality; ensembling cuts variance ~100% on a toy overfit case), `38_optimization_from_backprop_tricks_to_adam` (🔴 LeCun + Kingma & Ba — real regression Hessian condition number ~975,000 unnormalized vs ~1.2 normalized; SGD's usable lr window is 3.3x vs Adam's 82x on the same anisotropic toy bowl; from-scratch Adam matched `torch.optim.Adam` to 1.67e-16; Adam's memory tax tied numerically to 07b's ZeRO-1), `39_trees_forests_and_boosting` (🔴 Breiman + XGBoost — single unconstrained tree overfits exactly like nb37's degree-15 polynomial; OOB tracks held-out test accuracy; feature importance separates 2 real features from 4 pure-noise ones ~4-5x; gradient boosting from scratch on nb37's sine problem; XGBoost regularization sweep shrinks train-test gap 0.14→0.05 at flat test accuracy; closes with an explicit "when NOT to reach for an LLM" section), `40_the_sklearn_way` (🟡 Pedregosa — fit/predict contract framed as the same idea as 28b's tool contracts, proven by dropping a from-scratch `NearestMeanClassifier` into the same model-comparison loop; a REAL SelectKBest-before-split leak measured at ~70% "accuracy" on 1000 pure-noise features with random labels, `Pipeline`+`cross_val_score` correctly returns ~50% chance-level; StratifiedKFold vs plain KFold on class-grouped data — 4/5 folds with zero minority-class examples without it), `41_model_interpretability_shap` (🟡 Lundberg & Lee — exact Shapley values via brute-force 3!-permutation enumeration on a 3-feature interaction toy model, additivity verified to machine precision; `shap.TreeExplainer` on nb39's own random forest, additivity re-verified against real `predict_proba`; a real numpy attention demo where the highest-attention token (91% weight) contributes LESS to the output than a low-attention token (4% weight) with a much larger value vector — attention weight vs. `weight×value` contribution, tied to nb04 and the Jain & Wallace "Attention is not Explanation" line of work), `42_spark_and_distributed_data` (🟢 Zaharia — a ~60-line from-scratch RDD class with real lazy evaluation and lineage-replay-without-cache (call counts literally double per repeated action), then a REAL (not simulated) disk-read-vs-in-memory-cache timing experiment on real temp files — measured 15.1x speedup training iterative logistic regression, both paths converging to identical weights; guarded optional real-pyspark cell, same pattern as 13b's vLLM guard, pyspark NOT added to the main env). Also per the plan: added the arxiv URL for Vaswani et al. 2017 to notebooks 04/05's Source-material lines, and added a new "encoder-only & MLM" concept cell (BERT vs. decoder-only, referencing notebook 04's own DistilBERT usage) plus the BERT 2018 citation to notebook 05b — both re-executed clean. README: Tier 10 flipped to ✅ in the tier list, triage table, and mermaid map (new `T10` subgraph); 🔴-fast-path gained an explicit "coming from data science" prefix branch (37→38→39); a 5th learner-profile line added to "Start here"; Setup's offline-tiers line extended to include Tier 10. **Check-glob fix (must NOT be lost in future edits):** `notebooks.sh`/`lint.sh` globs were widened from `0[0-9]_*` to `[0-9][0-9]_*` in the SAME commit as the first Tier 10 notebook — narrowing them back would silently stop checking this entire tier. Full plan and build-time numerical-stability notes: `~/.claude/plans/classic-ml-section.md`.
  - **Numerical-stability lessons (apply to any future notebook fitting high-degree/high-capacity models to small samples):** bootstrapping a FIXED small sample for a bias-variance decomposition (rather than drawing a fresh sample from the same distribution each resample) creates duplicate x-values that make a high-degree polynomial's Vandermonde matrix nearly singular — variance can explode to the billions/trillions even with `numpy.polynomial.Polynomial.fit`'s domain-scaling. Fresh draws per resample avoid this and are also the textbook-correct definition of the bias-variance decomposition, not just a numerical workaround. Similarly, a learning-curve sweep that lets a high-degree model's parameter count get close to the sample size (near-exact interpolation) produces astronomically unstable single-sample MSE outliers at the small end — start the size sweep far enough above the parameter count (empirically, ~2x the model's parameter count was not enough; needed ~2x that again) rather than truncating the story or silently switching to median aggregation, which just relocates the same instability to a different sample size.

- ✅ **RL loop & GRPO substrate — CLOSED (2026-08-05).** Closes an **in-scope** gap and explicitly does **not** open an RL tier. Line 512 above records that RL as a field "this repo never scoped" — that still holds. The gap this closes is narrower and sits entirely inside the existing LLM/post-training lane: notebook `09_rlhf_and_alignment` teaches the alignment *objective* (Bradley–Terry reward model, PPO-with-KL-leash, DPO) but never the machinery PPO runs inside, and this file's Stanford source map (~line 180) lists Lecture 6 as covering "RL for reasoning, GRPO, scaling" — yet GRPO/RLVR appeared nowhere in the curriculum except two passing mentions in `P1_train_llm_from_scratch`'s source-material line and pipeline table. Built `02_training/09b_rl_loop_and_grpo.ipynb` (🟡, 37 cells), executed clean via `tools/run_nb.py` in ~12s, **fully offline on CPU with only numpy + matplotlib** — no API keys, no new dependencies, and deliberately **no `gymnasium`/`stable-baselines3`** (a ~40-line hand-rolled `Corridor` env plus a `VecCorridor` wrapper stand in, so the auto-reset convention is the genuine article rather than a description of one). Sections: the five-noun loop → batched envs and the auto-reset convention → `terminated` vs `truncated` → returns/baselines/GAE(λ) → policy gradient to PPO's clip (linking back to 09 rather than re-deriving it) → GRPO → an honest RLVR vocabulary map. Slots between 09 and 10; touches no other notebook. README Tier 2 triage table and the T2 mermaid subgraph updated (`N09 --> N09b --> N10`); 🔴 fast path unchanged (09b is 🟡); the "Tiers 1–2 and 10 run fully offline" Setup line already covers it.
  - **Every numerical claim is measured against an exactly-solvable ground truth, not asserted.** The corridor's value function for the fixed policy is solved as a 4×4 linear system, so the centerpiece cell is a real measurement: tabular TD(0) driven by the vec env recovers V\* to RMSE **0.098** with correct handling, **7.506** when `terminated` and `truncated` are collapsed into one `done` (~3x underestimate on every state), and **4.915** when bootstrapping the post-auto-reset observation instead of `info["final_observation"]`. Both bugs are silent — no exception, loss still descends. Same for GAE: 20 imperfect critics drawn once and **reused (paired) across every λ** so the sweep is smooth, giving a monotone |bias| 2.63→1.93 against a variance climb 0→33.7. And for GRPO: the two group-relative runs are bit-identical under a meaningless `+5` verifier offset (0.998 both) while raw-reward REINFORCE degrades 0.993→0.826 — plus the honest cost, ~**97% dead groups** (all G completions scoring alike → zero within-group signal) once the policy converges, which is why real runs need difficulty curricula.
  - **Env-design notes, if this is ever extended:** the bias/variance story is fragile to setup choices and several plausible ones silently destroy it. (1) A *uniform-random* start distribution makes the auto-reset bug look harmless — bootstrapping the reset observation is accidentally near-correct because the reset state's value sits close to the typical truncation state's. A **fixed** low-value start (position 1) is what separates the two bugs into visibly different wrong answers. (2) A *proportional* critic error (V̂ = c·V\*) makes GAE's |bias| **increase** with λ, not decrease, because the −V̂(s₀) term present at every λ partially cancels the λ=0 bootstrap error; per-state additive noise (V̂ = V\* + ε) is what produces the textbook curve, and it's also the more honest model of a real critic. (3) The forced first action is what makes λ=0 have exactly zero variance, which is the cleanest possible illustration of the dial's left end.
  - **Three `TODO (Itai):` markdown cells are intentionally left empty** (bolded one-line prompts only, no invented content) — after the batched-envs section, after terminated-vs-truncated, and inside Key Takeaways — for the repo owner to fold in their own war stories from a 3-hour on-site RL-infrastructure exercise. Do not fill these in on their behalf.

### Tier 3–4 conventions (added this build)
- **New deps (via `uv add`):** `langgraph`, `langchain-anthropic`, `langsmith`. Added to `imports.sh` (now 15 pkgs). `.env.example` notes `LANGCHAIN_TRACING_V2`.
- **LangGraph gotcha:** `ChatAnthropic` does NOT auto-resolve the key here — pass `api_key=os.environ["ANTHROPIC_API_KEY"]` explicitly. Build the graph unconditionally (offline-safe); guard only `.invoke()` / node LLM calls. `draw_ascii()` needs `grandalf` (absent) — print `get_graph().nodes/edges` instead. Fan-out needs a reducer: `Annotated[list, operator.add]`.
- **LangSmith:** guard with `HAS_LANGSMITH`; wrap with `@traceable`; ships traces in a background thread and fails silently, so it never breaks a run. Enable via `LANGSMITH_TRACING=true`.
- **Live API calls:** key IS present → `notebooks.sh` makes REAL calls. Shared guarded `ask()` helper (`HAS_ANTHROPIC` + try/except → graceful skip string); `TEACH_MODEL = "claude-haiku-4-5-20251001"` for cheap calls (`claude-opus-4-8` = production). Keep prompts tiny, sample counts low (n≈3).
- **macOS crash guard:** torch + sentence-transformers + faiss can segfault the kernel at shutdown. In embed+faiss notebooks (15) set `KMP_DUPLICATE_LIB_OK=TRUE`, `OMP_NUM_THREADS=1`, `TOKENIZERS_PARALLELISM=false` BEFORE imports + `faiss.omp_set_num_threads(1)`. Don't embed huge batches in-kernel — use NumPy random vectors for scaling demos and keep real `embed()` calls small. P3 avoids torch entirely (mock keyword search).
- **dotenv gotcha (testing only):** `load_dotenv()` from a `python - <<EOF` heredoc raises `AssertionError` in `find_dotenv()` (empty call stack). Use `load_dotenv("/abs/path/.env")` when smoke-testing from stdin; notebooks/`-c` are unaffected.

### Decisions confirmed with the user (apply to all remaining tiers)
1. **API:** **Both side-by-side** — Anthropic (`anthropic`, model `claude-opus-4-8` / latest) as primary, with OpenAI (`openai`) comparison cells where useful. Use the "no-key" guard pattern (see `00_environment_check` §5) so concept cells run without keys.
2. **Compute:** **Local GPU assumed** (no Colab scaffolding). Still use the device-agnostic `pick_device()` helper (cuda → mps → cpu) so notebooks run on the user's Mac (MPS). Keep any training tiny so it executes in seconds on CPU/MPS.
3. **Exercises:** exactly 3 (warm-up / apply / extend), each a stub with a `# YOUR CODE HERE`, followed by a single **collapsed `<details>` cell** holding all solutions.
4. **Scope cadence:** build a tier or two, then check in.

### Technical conventions (match these in later tiers)
- **Environment:** repo uses `uv` (Python 3.13); `.venv` was relocated so its console-script shebangs are broken. Run tools as `.venv/bin/python -m <tool>` — **`jupyter`/`nbconvert` CLIs do NOT work directly.** Execute notebooks with `.venv/bin/python tools/run_nb.py <nb...>` (in-repo now, not `/tmp` — survives session/tmp cleanup), not `jupyter nbconvert`.
- **Notebook generation:** build with `tools/nbgen.py` (`md()`, `code()`, `write_nb()` — adds cell ids, nbformat 4.5), driven by a disposable per-notebook `tools/build_NN.py` script (write it, run it, execute the notebook, delete the build script — only `nbgen.py`/`run_nb.py` persist in-repo). Every notebook is **executed and verified** before being considered done.

### Tier 5 conventions (added this build)
- **New deps (via `uv add`):** `fastapi`, `uvicorn`, `httpx`, `mcp` (added ahead of Tier 8, harmless to have present now). Added to `imports.sh` (now 19 pkgs). Check globs (`notebooks.sh`, `lint.sh`) extended from `0[0-6]_*`/`0[0-6]_*/**` to `0[0-9]_*` to cover Tiers 5/8/9 as they land.
- **Eval harness shape (notebook 24), reused verbatim downstream:** golden dataset (list of dicts) → `run_variant(system_prompt)` → one of three scorers (exact-match / rubric / model-graded `judge_score`) → aggregate with `np.mean`. Notebooks 26, 27, 27b, and both P2/P4 capstones lean on this exact shape rather than reinventing it.
- **Agent-eval shape (notebook 27b):** a task = `{prompt, required_tools, forbidden_tools, answer_check}`; `run_agent()` returns a trajectory (list of tool calls) + final answer + token cost; score with `trajectory_score()` (path quality) and `tool_call_correctness()` (per-call validity) separately — don't conflate them, they catch different failure classes.
- **Judge calibration gotcha (notebook 26):** an uncalibrated judge is worse than no eval — always correlate judge scores against a small hand-labeled set (target >0.7 correlation) before trusting one in a pipeline.
- **Gate shape (notebook 27c):** an `Evidence`-weighted `MergeGate` with `IRREVERSIBLE` structurally never auto-opening (checked before the evidence score, not via a threshold); judge calls are always injected into `JudgeConfig.call_fn`, never imported by `agentkit` itself.

### Tier 8 conventions (added this build)
- **Triple-quote nesting trap (bit us twice — notebooks 29 and 31):** `code("""...""")` in a build script cannot contain ANY literal `"""` inside the generated content, even nested inside an inner `'''...'''` string one level down — Python's tokenizer doesn't understand logical nesting, it just scans for the next `"""`. Any generated-source docstrings inside a build script must use `#` comments or a `description=` kwarg instead of a triple-quoted docstring. Check with `python -c "import ast; ast.parse(open('build_NN.py').read())"` before running.
- **Regex escape gotcha:** `r"[0-9+\\-*/(). ]+"` written inside a *non-raw* outer string (e.g. `SERVER_SOURCE = '''...'''`) triggers a `SyntaxWarning: invalid escape sequence` when that generated code is later parsed as Python — reorder the char class so `-` is first/last (`[0-9+*/(). -]`) instead of escaping it.
- **ipykernel already runs an event loop:** any notebook using `asyncio` (nb31/MCP) MUST use top-level `await` inside a cell, NOT `asyncio.run()` — the latter raises `RuntimeError: asyncio.run() cannot be called from a running event loop`.
- **Real subprocess servers (nb29 FastAPI, nb31 MCP):** launch via `subprocess.Popen` + `atexit.register(proc.terminate)` as a safety net, health-probe with a polling loop before making requests, and ALWAYS add an explicit cleanup cell that terminates + waits so `notebooks.sh` doesn't leak processes. Use `find_free_port()` (bind to port 0) rather than a hardcoded port to avoid CI collisions.
- **MCP tool descriptions:** use `@mcp.tool(description="...")` rather than a function docstring when the server source is being generated from within a build script (avoids the triple-quote trap above); FastMCP accepts either.
- **Honesty over drama (notebook 30):** the live prompt-injection demo against Claude Haiku often gets RESISTED by the model's own safety training — don't force a fake "attack succeeded" narrative. Report the real live outcome, then use a clearly-labeled deterministic mock (`naive_unsafe_agent_simulator`) to make the underlying mechanism unambiguous regardless of what the live call did. This is more honest AND more convincing than a scripted "gotcha."

### Tier 9 conventions (added this build)
- **Vision-agent pixel accuracy (notebook 34):** small rendered images (~80px buttons) cause real, non-scripted misclicks from the model's own coordinate estimation — this isn't a bug in the harness, it's an authentic finding about pixel-based computer use being brittle. Fix by enlarging the render (160x120px buttons, `ImageFont.truetype` at 32-36pt) rather than faking a clean result; keep the goal prompt unambiguous ("click X, then Y, then =, stop once the display shows the numeric result") so a correct vision-agent run actually reaches a clean answer.
- **OPENAI_API_KEY present but out of quota** in this environment (`insufficient_quota` / 429) — the guarded try/except pattern already handles this gracefully (reports `[skipped: RateLimitError...]`), same as a missing key. Don't assume `HAS_OPENAI = bool(env var)` means calls will succeed; the try/except is doing real work, not just decoration.
- **Synthetic-data contamination check (notebook 36) is genuinely convincing, not staged:** asking Claude to generate "world capitals" Q&A spontaneously reproduced the exact "What is the capital of France?" eval question (ratio=1.00) — a real, unprompted illustration of why notebook 25's contamination scanner matters for synthetic data specifically.
- **MCP/subprocess/async notebooks:** see Tier 8 conventions above (triple-quote nesting, top-level `await`, subprocess cleanup) — all apply equally here.

### Tier 6 capstone conventions (added this build)
- **P1 model-size/timing tradeoff:** prototype param count and per-step timing OUTSIDE the notebook first (`d_model=384, n_heads=6, n_layers=8, block_size=192` → 14.3M params, ~103ms/step on MPS, 300 steps ≈ 31s) before committing to a config — avoids discovering a too-slow config only after writing the full notebook.
- **P1 corpus choice:** use a clearly SYNTHETIC repeated-phrase corpus (proverbs/idioms), not a real copyrighted text reconstructed from memory — avoids both reproduction-accuracy risk and copyright concerns, and still gives a tiny model enough structure to visibly learn (loss 3.39→0.08, coherent phrase completion vs. untrained gibberish).
- **P2 reuses `ragkit` unmodified** (`load_corpus`, `chunk_text`, `build_collection`, `query_collection`, `generate`) — a capstone's job is composition + evaluation, not reinventing retrieval. `sys.path.insert(0, "..")` from `06_projects/` works the same way it does from `03_building/` (confirmed empirically — nbclient runs with cwd = the notebook's own directory).
- **P4's graph-wide budget:** track `tool_calls_used` in the LangGraph `TeamState` itself (not inside one node's closure) so the budget check in the routing function (`after_critic`) sees total usage across every node, not just one sub-agent's private counter — this is what makes it a TEAM budget instead of P3's single-agent budget.
- **P4's injection defense held up as designed:** the poisoned mock-KB entry got redacted at the tool boundary before ever reaching the writer LLM — the report honestly said "sources were redacted, cannot answer" rather than hallucinating, which is the correct and desired outcome of notebook 30's guardrail pattern, not a failure to work around.
- **Models used (all small, cached, guarded with try/except + offline fallback):** GPT-2 (generation/tokenizer), DistilBERT (attention viz), `all-MiniLM-L6-v2` (embeddings, already cached). HF is reachable in this environment.
- **Add new deps via `uv add`** (already added: `openai`, `datasets`, `plotly`). `torch`, `transformers`, `sentence-transformers`, `scikit-learn`, `matplotlib`, `anthropic` are present.
- **Plots:** start viz cells with `%matplotlib inline`; every plot gets a title + axis labels + a one-sentence italic caption in the following markdown cell.
- **Forward references:** link concepts to their notebook number (e.g. "see notebook 14"); don't re-teach earlier material.
```

---

## Working in a Loop (do → check → repeat)

Most agents run once and hand back broken work. This repo ships a reusable
**do, check, repeat until done** skeleton so the loop is the same for any goal —
only the check changes.

- **The loop command:** `/loop <task>` (`.claude/commands/loop.md`). It establishes
  what "done" means, does the work, runs the check, and repeats until the check
  passes or a stop rule fires.
- **The pluggable checks** live in `.claude/checks/` — point the loop at whichever
  one matches the goal. Each is a short script that prints PASS/FAIL and exits
  non-zero on failure:
  - `notebooks.sh [nb …]` — execute notebook(s) clean (the repo's real "tests green").
  - `lint.sh` — fast syntax gate over all notebook cells + `ragkit` modules.
  - `imports.sh` — core stack imports clean (use when fixing the env/deps).

  Swap the check and the bug-fixer becomes an env-fixer; the skeleton never changes.
  A new goal is a new short script in `.claude/checks/`, not a new agent.

### Loop stop rules

Stop the loop when any of these is true:

- The goal check passes. Stop, report success with the check output.
- 5 cycles used. Stop, report what's left and what was tried.
- The check result hasn't improved in two cycles. The agent is
  stuck. Stop and show me, don't burn cycle 4 and 5 guessing.
- A cycle makes the check worse than the cycle before. Something
  is going backwards. Stop and surface it.

Never report success without the check's output from the final cycle.
Never edit the check itself to make it pass.
