
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
└── 09_frontier/
    ├── 34_computer_use_and_browser_agents.ipynb
    ├── 35_voice_and_realtime.ipynb
    └── 36_data_engineering_for_ai.ipynb
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

### Inference Optimization Deep Dive (AWQ, GPTQ, KV eviction, SGLang, load testing, K8s, edge)
Gap analysis (2026-07-30) against an 18-item "LLM inference optimization" roadmap found existing coverage of vLLM/PagedAttention/continuous batching (13b), speculative decoding (11), quantization fundamentals (10), KV cache + prompt caching (13), cost engineering (32), and Ollama (ragkit) — but named quantization formats, KV eviction, SGLang, load testing, K8s autoscaling, edge deployment, and a reading list were missing or only cross-referenced. Closing this in 4 waves (see `~/.claude/plans/write-a-plan-to-glowing-yao.md`).
- **AWQ** — Lin et al., *"AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"* (MLSys 2024). Core mechanism: scale up weight channels with large activation magnitude before quantizing, scale activations down to compensate — protects salient channels without mixed precision.
- **GPTQ** — Frantar et al., *"GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"* (ICLR 2023). Column-by-column quantization with inverse-Hessian error compensation for not-yet-quantized columns (the OBQ/OBC update rule).
- **StreamingLLM (attention sinks)** — Xiao et al., *"Efficient Streaming Language Models with Attention Sinks"* (ICLR 2024) — https://arxiv.org/abs/2309.17453. The first few tokens of any sequence absorb outsized attention regardless of content; keeping them plus a sliding window enables stable unbounded-length generation.
- **H2O (heavy hitters)** — Zhang et al., *"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs"* (NeurIPS 2023) — https://arxiv.org/abs/2306.14048. A small set of tokens receive most of a sequence's cumulative attention; KV eviction formulated as a dynamic submodular problem.
- **SGLang / RadixAttention** — Zheng et al., *"SGLang: Efficient Execution of Structured Language Model Programs"* (NeurIPS 2024) — https://arxiv.org/abs/2312.07104. Prefix-tree KV cache reuse *across* requests (vs. vLLM's PagedAttention, which manages memory *within* one request); reports up to 6.4x throughput on shared-prefix workloads.
- 2026 tooling landscape (via WebSearch, 2026-07-30): AWQ has overtaken GPTQ as vLLM's default INT4 recommendation (faster Marlin kernel support); both typically built via `llm-compressor` rather than the original research repos; FP8 W8A8 needs no calibration data and is the default on Hopper+ GPUs; GGUF/Ollama `Q4_K_M` is the community-default local quant, `Q8_0` is near-lossless.
- Gap analysis closed 3 notebooks so far (Wave 1, 2026-07-30): **10b** quantization in practice — AWQ/GPTQ/FP8/GGUF (🟡), **13c** KV cache eviction — sliding window/sinks/H2O (🟡), **13d** SGLang & request scheduling — RadixAttention prefix cache + FCFS/SJF/priority queueing with aging (🟡). All three built fully offline-safe (HF and Ollama are proxy-blocked in this environment — `HAS_HF`/`HAS_OLLAMA`/`HAS_SGLANG_SERVER` probes all guard against it) using synthetic-but-faithful demos rather than live model calls; every numeric claim in prose was empirically verified against the notebook's own executed output before being written (two demos — AWQ's alpha sweep and GPTQ's compensation — initially produced results contradicting the intended narrative due to quantization-granularity and Hessian-vs-inverse-Hessian bugs; both were root-caused and fixed rather than the prose being adjusted to match wrong numbers).
- Wave 3 (2026-07-30) research findings: current per-token pricing came from the `claude-api` skill's live model table (Haiku 4.5 $1/$5, Sonnet 5 $3/$15 intro $2/$10, Opus 5 $5/$25 per 1M tokens); **LiteLLM**'s `Router` supports `routing_strategy="cost-based-routing"` over 100+ providers behind one OpenAI-compatible call shape; **LM Studio** and **Ollama** both expose local OpenAI-compatible servers (`:1234`, `:11434`) a router can address identically to a cloud tier; **ONNX Runtime**'s `quantize_dynamic` (module `onnxruntime.quantization.quantize`) needs no calibration data, vs. `quantize_static` which does; PyTorch 2.9+ made the `torch.export`-based `dynamo=True` path the default ONNX exporter (needs the `onnxscript` package; the legacy TorchScript tracer via `dynamo=False` still works but is deprecated); **TensorRT-LLM** (confirmed via its own GitHub repo, `onnxruntime.ai` and `nvidia.github.io` both 403 the sandbox's fetch proxy) compiles GPU-and-precision-locked engines delivering ~2-4x throughput over vLLM/TGI on the same NVIDIA hardware, at the cost of 10-30 min build times and needing 1000+ calibration samples to keep FP4 accuracy loss near 2-3% (vs. 5-8% uncalibrated); **WebLLM** (`@mlc-ai/web-llm`, confirmed via its GitHub repo) runs entirely in-browser via WebGPU with an OpenAI-compatible call shape, installable via `npm install @mlc-ai/web-llm` or CDN (`https://esm.run/@mlc-ai/web-llm`); `mlc-ai/Llama-3.2-1B-Instruct-q4f16_1-MLC` confirmed as a real, small (~879MB) WebLLM-compatible model ID.
- Gap analysis closed 2 more notebooks (Wave 3, 2026-07-30): **32c** gateway routing & unit economics (🟡, cost-per-user distribution modeling + a from-scratch `ModelRouter` scorecard + LiteLLM/LM Studio/Ollama as the off-the-shelf version), **37** edge deployment (🟢, real ONNX export/dynamic-INT8-quantize/benchmark on CPU + TensorRT-LLM taught analytically + a real runnable `deploy/webllm/index.html`). See the Wave 3 conventions section below for two bugs found and fixed while building these (a shared-RNG-state bug in 32c producing three identical quality scores, and an ONNX Runtime benchmark-noise issue in 37 that made an initial "~1.4-1.5x" latency claim unreproducible).


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
- 🚧 **Inference optimization deep dive — Waves 1–3 CLOSED (2026-07-30), wave 4 in progress.** See Content Source Map > "Inference Optimization Deep Dive" for the full plan/paper list. Wave 1 built 3 notebooks, each executed clean individually via `.claude/checks/notebooks.sh` and together via `lint.sh`: `02_training/10b_quantization_in_practice` (🟡, AWQ/GPTQ/FP8/GGUF — from-scratch per-group INT4, activation-aware AWQ scaling with a genuine alpha valley, inverse-Hessian GPTQ compensation, FP8-vs-INT8 error comparison), `03_building/13c_kv_cache_eviction` (🟡, sliding window vs. StreamingLLM sinks vs. H2O heavy-hitters over a synthetic-but-faithful sink/recency/heavy-hitter attention generator), `03_building/13d_sglang_and_request_scheduling` (🟡, a prefix-trie RadixAttention simulator reaching ~79% cache hit rate on a shared-system-prompt workload, plus a discrete-event queue simulator comparing FCFS/SJF/priority/SJF+aging). Wave 2 built 3 more: `08_production/29b_load_testing_inference` (🟡, real FastAPI+uvicorn mock GPU server with a semaphore standing in for batch slots; closed-loop concurrency sweep from 1→1024 finds a genuine throughput knee (~101 req/s at concurrency=128, P99 climbing to 13s by concurrency=1024); an open-loop Poisson generator — the Apply exercise — proves latency grows *unboundedly* over a sustained-overload run (282ms→13.6s across 20s) in a way no closed-loop concurrency level can ever produce), `08_production/29c_inference_observability` (🟡, `prometheus_client` Counter/Histogram/Gauge instrumentation, a hand-rolled Prometheus exposition-format parser + `rate()` + `histogram_quantile()` validated against real percentiles, a live tokens→$/hour conversion using Claude Haiku 4.5's published pricing, and an empirical demo that default `Histogram` buckets erase 8/28 overloaded requests into one indistinguishable `+Inf` bucket), `08_production/29d_kubernetes_for_ai_workloads` (🟢, real `deploy/k8s/*.yaml` manifests + a from-scratch HPA v2 algorithm and fluid-queue simulator showing pod-startup-delay-driven queue spikes, plus the non-monotonic finding that partial min-replicas overprovisioning can be *worse* than none). README triage tables (Tiers 2/3/8), mermaid map updated. New direct dependency: `prometheus-client` (was already transitive; added via `uv add` + `imports.sh`). New top-level dirs: `deploy/observability/` (docker-compose.yml, prometheus.yml, grafana-dashboard.json) and `deploy/k8s/` (deployment.yaml, service.yaml, hpa.yaml) — validated with `yaml.safe_load`/`json.loads` in-notebook, not run (no Docker daemon or cluster in this sandbox). Environment note: this session's remote sandbox needed a fresh `uv sync` (~9GB of CUDA wheels — the base image has no GPU, so this was pure download overhead but not worth reconfiguring the shared torch source for one session); HF and Ollama are both proxy-blocked here (confirmed via direct probe, not assumed), so all notebooks use fast `urllib`-based reachability probes (`HAS_HF`, `HAS_OLLAMA`, `HAS_SGLANG_SERVER`, matching 13b's `HAS_VLLM_SERVER` pattern) rather than attempting a live call and catching the failure — a raw `transformers.from_pretrained()` call was observed to hang for minutes retrying before failing, so the probe-first pattern is a correctness requirement here, not just a style preference.
- ✅ **Wave 3 built 2 more:** `08_production/32c_gateway_routing_and_unit_economics` (🟡, Part 1 models cost-per-user as a distribution over a 2000-user lognormal population, not an average — finding ~1.85% of users already loss-making on a $20/mo plan at median usage; Part 2 builds a `ModelRouter` scorecard (measured latency, real cost, quality scored via notebook 24's exact eval-harness shape) and routes against declared constraints (`cheapest_above_quality_bar`, `cheapest_under_latency_ceiling`); Part 3 shows LiteLLM's `Router(routing_strategy="cost-based-routing")` config plus guarded LM Studio/Ollama port-reachability probes as the off-the-shelf version), `09_frontier/37_edge_deployment` (🟢, exports a real 4.2M-param hand-built transformer to ONNX via `torch.onnx.export(dynamo=True)`, applies `quantize_dynamic` INT8 (measured: ~3.84x smaller file, output cosine similarity >0.999 vs. FP32), benchmarks PyTorch-CPU vs. ORT-FP32 vs. ORT-INT8 with multi-trial median timing, teaches TensorRT-LLM analytically (no GPU here), and ships a real runnable `deploy/webllm/index.html` chat page). README triage tables (Tier 8/9), mermaid map updated. New direct dependencies: `onnx`, `onnxruntime` (onnxruntime was already transitive via `chromadb`), `onnxscript` (needed by the dynamo ONNX exporter; not itself imported by notebook code, so not added to `imports.sh`) — `onnx`/`onnxruntime` added to `imports.sh`. New top-level dir: `deploy/webllm/index.html` (validated by parsing with `html.parser`, not run — needs a real WebGPU browser).
- ⚠️ **Latent bug found in existing notebook 29, and the general fix for any future FastAPI-app-in-a-string-template notebook:** when a cell does `APP_SOURCE = textwrap.dedent('''...''')` and the template body contains an escape sequence like `"\n\n"` (e.g. building an SSE line terminator), that `'''...'''` is a *second* level of Python string parsing (build script → cell source → cell execution) — a plain (non-raw) triple-quoted string interprets `\n` as a real newline **at cell-execution time**, corrupting the generated file with a literal blank line inside a regular string literal (a `SyntaxError` in the generated file) and, as a side effect, breaking `textwrap.dedent`'s common-prefix detection so the leading indentation is never stripped either. Found while building 29b: the identical `APP_SOURCE = textwrap.dedent('''...return "data: " + json.dumps(payload) + "\\n\\n"...''')` pattern already exists in notebook 29's own build history, and reproducing it in isolation confirms notebook 29's server has never actually started in this kind of environment — its demos are silently skipped by their own `if server_up:` guards, so the notebook still shows PASS. **The fix:** write `textwrap.dedent(r'''...''')` (add `r` before the inner triple-quote) so the cell's own execution doesn't re-interpret escape sequences the outer build script already resolved once. Not fixed in notebook 29 itself (out of scope for this batch — flagging for whoever next touches it); 29b and 29c were both built with the `r'''` form from the start and verified to actually launch, parse, and dedent correctly by exec'ing the generated cell in isolation before running the full notebook.

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

### Inference-optimization conventions (Wave 1, added this build)
- **Verify every synthetic demo's actual printed output before writing the prose that describes it — don't trust the intended narrative.** Two of 10b's demos initially produced results that contradicted the story: (1) naive AWQ scaling with `quantize_int4_per_group` made error *worse* as `alpha` rose, because a shared per-group scale means protecting one channel inflates the step size for every other channel in its group — fixed by switching to per-OUTPUT-ROW quantization (`quantize_int4_per_row`) with many rows, so a salient channel only occasionally sets any one row's max; (2) a naive GPTQ compensation using the raw Hessian (`H[j,i]/H[j,j]`) instead of its *inverse* made error worse than no compensation at all — the OBQ/GPTQ update rule requires `H^{-1}` restricted to the remaining unquantized columns, not raw `H`. Both were root-caused with a scratch script before being baked into the notebook; the fix was the math, never the prose.
- **`urllib.request.urlopen(..., timeout=N)` reachability probes are a correctness requirement here, not a style choice.** A direct `transformers.from_pretrained("distilgpt2")` call was observed to hang for minutes (internal retry logic) before failing with a 403 from the sandbox's proxy, which would blow past `run_nb.py`'s 600s per-cell timeout on a bad day. A fast probe first (matching 13b's `HAS_VLLM_SERVER` / `vllm_server_up()` pattern) fails in ~1s and lets the rest of the notebook execute deterministically offline.
- **Discrete-event queue simulation pattern (13d, reusable for 29b's load-testing notebook):** a `heapq` of `(time, kind, request_id)` events (`"arrival"` / `"departure"`), a `waiting` list, and a `try_admit(now)` closure called after every event that pulls from `waiting` via a policy function whenever a slot is free — cleanly supports FCFS/SJF/priority/aging by swapping only the policy function, no change to the event loop. `np.percentile` on the resulting per-request latency dict gives P50/P99 directly.

### Inference-optimization conventions (Wave 2, added this build)
- **`textwrap.dedent(r'''...''')` — use the raw-string form by default for any generated-app-source template.** See the CLAUDE.md progress entry above for the full failure mode (a second level of escape processing at cell-execution time). Applied in 29b and 29c from the start; verify by `exec()`-ing the generated cell in isolation with stub globals and asserting the written file `ast.parse()`s before running the full notebook — cheaper than discovering it via a 15s `wait_for_health` timeout.
- **A fluid-queue model (`queue += (arrivals - capacity) * dt`, clamped at 0) is enough to demonstrate autoscaling lag** — no need for a full discrete-event simulation when the question is "how does aggregate queue depth respond to a capacity change," as opposed to 13d's per-request scheduling-policy question, which genuinely needs per-request events.
- **The HPA formula's own math can make partial fixes backfire, and this is worth testing empirically before writing the takeaway.** `desired = ceil(current_replicas × (metric/current_replicas) / target)` algebraically reduces to `ceil(metric/target)` — replica count cancels out — so raising `min_replicas` a little doesn't just add a cushion, it changes *when* the control loop concludes more capacity is needed, sometimes making the reactive gap arrive later and no smaller (29d found `min_replicas=4` producing a *worse* peak queue depth than `min_replicas=2`; only `min_replicas=9`, sized to the actual peak, helped). Verified with a scratch script sweeping `[2, 4, 9]` before committing to the "overprovisioning only works if sized to the peak" framing.
- **Default `use_stabilization`/keyword defaults matter for reproducibility across a notebook's cells.** An early draft of 29d's `simulate()` defaulted to `use_stabilization=False`, while the scratch-tested prototype numbers assumed stabilization on (matching real K8s HPA, which always has *some* scale-down stabilization) — the mismatch produced a different, more chaotic peak-queue number (1310 vs. 875) than the validated prototype and than the surrounding prose. Fixed by making `use_stabilization=True` the default (the honest real-world default) and keeping the `False` case for the exercise that specifically demonstrates flapping.

### Inference-optimization conventions (Wave 3, added this build)
- **Never let two unrelated sections of one notebook share a single `rng` object.** 32c's Part 1 (unit economics) drew 2000+ lognormal samples from `rng = np.random.default_rng(0)` before Part 2 reused the SAME advanced `rng` for `router.evaluate_quality()` — at that specific point in the PRNG stream, `rng.random()` happened to return values below every tier's accuracy threshold, producing three identical `quality=1.000` scores that silently matched nothing about the tiers' actual (very different) `true_accuracy` values. Fixed with a dedicated `router_rng = np.random.default_rng(1)` for the router's own draws. The corrected, genuinely-differentiated result then surfaced a *second*, more interesting finding worth keeping rather than hiding: with only 8 golden items, quality is quantized to multiples of 1/8, and sonnet (0.90 true accuracy) outscored opus (0.97 true accuracy) purely from small-sample noise — written up in-notebook as the real lesson (a router's ranking is only as good as its golden set), not patched away by re-seeding until the "expected" ordering appeared.
- **`torch.onnx.export(..., external_data=False)` for small pedagogical models, or the size comparison lies.** The default (`external_data=True`) splits weights into a companion `.onnx.data` file, so `os.path.getsize()` on the `.onnx` file alone can show quantization *increasing* file size (a small graph-only FP32 file vs. a fully-self-contained quantized file) purely because the FP32 comparison forgot to include its own external weights. `external_data=False` keeps a small demo model in one file for an honest, apples-to-apples before/after comparison; real multi-GB models should keep the default `True`.
- **The dynamo ONNX exporter is chatty in a way that pollutes notebook output** (torchvision-not-installed warnings, `[torch.onnx] ... ✅` progress prints) — suppress with `warnings.filterwarnings("ignore")` + `logging.disable(logging.WARNING)` + `verbose=False` on the export call, all three together (any one alone leaves noise).
- **CPU microbenchmarks on a shared/multi-tenant sandbox are noisy enough that a single-measurement claim doesn't reproduce.** An initial single-trial ORT-INT8-vs-ORT-FP32 benchmark in 37 showed a clean ~1.4-1.5x speedup; re-running the exact same code minutes later (still valid, just resampled) gave 1.08-1.23x on a `median`-of-5-trials methodology, and a bare single run without even that hygiene swung as low as 1.08x. Fixed two ways: (1) the benchmark helper itself now runs a warmup plus several independent timed trials and reports the **median**, per notebook 25's own benchmark-hygiene discipline; (2) the surrounding prose was rewritten to state a defensible range ("roughly 1.1-1.5x, treat as directional") instead of a specific number, while keeping the ~4x file-size reduction — which is deterministic, not sampled — as the claim actually worth trusting. Don't tune prose to match one lucky run; either make the measurement robust or state the honest range.
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
