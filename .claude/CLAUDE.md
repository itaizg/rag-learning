
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
│   └── 27_production_monitoring.ipynb
│
└── 06_projects/
    ├── P1_train_llm_from_scratch.ipynb
    ├── P2_build_rag_pipeline.ipynb
    ├── P3_build_agent_from_scratch.ipynb
    └── P4_multi_agent_research_system.ipynb
And all the existing notebooks in 07_rag_learning.
```

---

## Notebook Standard

Every notebook MUST follow this exact structure:

### 1. Header Cell (Markdown)
```
# [Number]. [Topic Name]

**Tier:** [Foundations / Training / Building / Agents / Evaluation]
**Estimated time:** [X minutes]
**Prerequisites:** [list notebook numbers]
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
- **ACTION REQUIRED:** Find the GitHub repo link in the comments of the tweet above and paste it here: `GITHUB_REPO_URL = "___"`

### AI Engineer Roadmap
- What AI engineers actually do in 2026: design agent loops, engineer context, write tools, add memory/durability/sandboxing, wire evals and CI regression gates
- 4 context primitives: Write, Select, Compress, Isolate
- Source: @sairahul1 — https://x.com/sairahul1/status/2062809249064141017


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
- ✅ **Tier 3 — Building (12–17)** — built and executed clean: `03_building/12_prompt_engineering` … `17_chain_of_thought`. RAG notebooks (14/15/16) reuse `ragkit` and link out to `07_rag_learning/` rather than re-teaching it.
- ✅ **Tier 4 — Agents (18–23, +19b)** — built and executed clean. Introduces three lenses: **Claude SDK** agents (18/19/19b), **LangGraph** orchestration (20), **LangSmith** tracing (21+). 19 = in-depth raw loop; 19b = ~20-line minimal version (user asked for both). 21 harness, 22 context primitives, 23 six loop patterns.
- ✅ **Tier 6 capstone — `06_projects/P3_build_agent_from_scratch.ipynb`** — research agent synthesizing all of Tier 4 (raw budgeted loop + LangGraph 5-stage graph + adversarial verify→revise cycle + harness + LangSmith trace), writes a sourced report to disk. Built & executed clean.
- ⬜ **Tier 5 (24–27), Tier 6 (P1, P2, P4)** — not yet built.

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
- **Environment:** repo uses `uv` (Python 3.13); `.venv` was relocated so its console-script shebangs are broken. Run tools as `.venv/bin/python -m <tool>` — **`jupyter`/`nbconvert` CLIs do NOT work directly.** Execute notebooks with the nbclient runner at `/tmp/nbgen/run_nb.py` (or equivalent), not `jupyter nbconvert`.
- **Notebook generation:** notebooks were built programmatically with `/tmp/nbgen/nbgen.py` (`md()`, `code()`, `write_nb()` — adds cell ids, nbformat 4.5). Every notebook is **executed and verified** before being considered done.
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
