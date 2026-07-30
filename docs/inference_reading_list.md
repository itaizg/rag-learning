# Inference Optimization Reading List

The roadmap this curriculum is built against says, bluntly: read inference research instead of model release news. Release notes tell you what shipped; papers tell you *why* it works, what it costs, and what it doesn't solve — which is what actually transfers to a system you didn't build from a tutorial.

This list is opinionated on purpose: it's the minimum set of papers that explain the mechanisms taught hands-on across notebooks 10b, 11, 13, 13b, 13c, 13d, and P5, plus a few (FlashAttention, DistServe, Splitwise) that underlie those mechanisms without a dedicated notebook of their own. Each entry links straight to the paper (every link below was checked to actually resolve before being included here — not recalled from training), says what to actually take from it, and points at the notebook that builds the idea by hand.

## Serving systems: batching and memory management

**[PagedAttention / vLLM](https://arxiv.org/abs/2309.06180)** — Kwon et al., *"Efficient Memory Management for Large Language Model Serving with PagedAttention"* (SOSP 2023).
What to take from it: the core insight is embarrassingly simple once you see it — stop allocating one contiguous KV-cache block per request (which wastes 60–80% of GPU memory to fragmentation and over-reservation) and hand out small fixed-size pages on demand instead, exactly like OS virtual memory. That one idea is most of why vLLM exists and why it improved throughput 2–4x over prior systems. Read the "internal/external fragmentation" section closely — it's the same argument an OS course makes about physical RAM, just applied somewhere you didn't expect it.
**Taught in:** 13b (vLLM & PagedAttention) builds a toy block-table allocator by hand.

**[Orca](https://www.usenix.org/conference/osdi22/presentation/yu)** — Yu et al., *"Orca: A Distributed Serving System for Transformer-Based Generative Models"* (OSDI 2022).
What to take from it: this is the paper that introduced **continuous (iteration-level) batching** — scheduling at the granularity of one decode step, not one whole request, so a request that finishes early doesn't hold its batch-mates hostage until the slowest one is done. It predates vLLM and reported a 36.9x throughput improvement over the batching schemes that came before it; almost every modern serving engine's batching strategy traces back to this paper. Read it to understand why "just batch requests together" was never as simple as it sounds for autoregressive generation.
**Taught in:** 13b's continuous-batching demo builds this exact idea (batch changes every decode step, not every request).

**[SGLang / RadixAttention](https://arxiv.org/abs/2312.07104)** — Zheng et al., *"SGLang: Efficient Execution of Structured Language Model Programs"* (NeurIPS 2024).
What to take from it: PagedAttention manages memory *within* one request; RadixAttention's contribution is reusing KV cache *across* requests that share a prefix (a system prompt, a few-shot example set, a multi-turn conversation's history) via a prefix tree, reporting up to 6.4x throughput on shared-prefix workloads. The paper is also worth reading for the broader "structured LM program" framing — it treats prompting patterns (branching, few-shot, agent loops) as a first-class execution model, not just strings.
**Taught in:** 13d builds a prefix-trie cache simulator and measures hit rate on a realistic shared-prompt workload.

## Attention and KV-cache efficiency

**[FlashAttention](https://arxiv.org/abs/2205.14135)** — Dao et al., *"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"* (NeurIPS 2022).
What to take from it: this paper's insight isn't algorithmic (it computes the exact same attention, not an approximation) — it's about where the bottleneck actually lives. Naive attention is *memory-bandwidth-bound*, not compute-bound: it reads/writes the full N×N attention matrix to slow GPU HBM. FlashAttention tiles the computation to stay in fast on-chip SRAM instead, and is the unglamorous kernel-level reason every serving engine you've used is as fast as it is. Worth reading specifically for the "IO-awareness" framing — it's a lesson in profiling the RIGHT bottleneck, not the obvious one.
**Taught in:** underlies the throughput of every serving system in this curriculum (13b, 13d) without a dedicated notebook of its own — the mechanism is a GPU-kernel-level detail below where these notebooks build by hand.

**[StreamingLLM (attention sinks)](https://arxiv.org/abs/2309.17453)** — Xiao et al., *"Efficient Streaming Language Models with Attention Sinks"* (ICLR 2024).
What to take from it: the counterintuitive finding is that the first few tokens of *any* sequence absorb a disproportionate share of attention regardless of their actual content — the model uses them as an attention "sink" it can safely dump unneeded attention mass into. Keep those tokens plus a sliding window and a model can generate stably at effectively unbounded length with a small, constant KV cache, even though it was never trained for that.
**Taught in:** 13c implements this as one of three eviction policies and measures retained-attention-mass directly.

**[H2O (heavy hitters)](https://arxiv.org/abs/2306.14048)** — Zhang et al., *"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of LLMs"* (NeurIPS 2023).
What to take from it: a small set of tokens receive most of a sequence's *cumulative* attention over time — not just the first few (StreamingLLM's story) but whichever tokens turn out to matter for this specific sequence. H2O tracks running attention scores and evicts low-cumulative-score tokens, framing KV eviction as a dynamic submodular optimization problem. Compare directly against StreamingLLM: sinks are cheap and content-blind, H2O is more expensive to track but content-aware — the paper's ablations show exactly when that extra cost is worth it.
**Taught in:** 13c's Apply exercise has you implement the H2O scoring function yourself.

## Quantization

**[AWQ](https://arxiv.org/abs/2306.00978)** — Lin et al., *"AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"* (MLSys 2024).
What to take from it: not all weights matter equally, and you can find out which ones do *without touching the weights at all* — just look at activation magnitudes during a small calibration pass, and protect (via a per-channel scale) the ~1% of weight channels that see the largest activations. That's the entire method, and it's why AWQ calibrates faster than Hessian-based approaches while staying competitive on accuracy.
**Taught in:** 10b implements activation-aware per-channel scaling from scratch and measures a genuine error-vs-alpha "protection valley."

**[GPTQ](https://arxiv.org/abs/2210.17323)** — Frantar et al., *"GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"* (ICLR 2023).
What to take from it: instead of deciding in advance which weights to protect, quantize everything column-by-column and use the *inverse Hessian* (a measure of how much each remaining column's error can be corrected by adjusting weights that haven't been quantized yet) to compensate for each column's rounding error using the columns you haven't touched yet. This is the OBQ/OBC update rule, and it's the single easiest place to introduce a real bug — using the raw Hessian instead of its inverse makes compensation *worse* than doing nothing, which this curriculum found out the hard way while building 10b.
**Taught in:** 10b implements the restricted-inverse-Hessian update and compares it directly against AWQ on the same tiny layer.

## Speculative decoding

**[Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)** — Leviathan et al. (ICML 2023).
What to take from it: the core trick is a small, fast "draft" model proposes several tokens autoregressively, and the large target model verifies all of them in **one parallel forward pass** instead of one sequential pass per token — accepting draft tokens that match what the target model would have generated anyway, with a rejection-sampling correction that keeps the output distribution *exactly* identical to greedy/sampled decoding from the target model alone. It's a genuinely free lunch on latency (not accuracy) when the draft model is cheap and roughly aligned with the target.
**Taught in:** 11 builds a draft-and-verify loop and measures real acceptance rates and speedup.

**[EAGLE](https://arxiv.org/abs/2401.15077)** — Li et al., *"EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty"* (ICML 2024).
What to take from it: EAGLE's draft model operates at the *feature* level (the target model's own last-layer hidden states) rather than being a fully separate small LM — it autoregresses over features, then reuses the target model's own LM head to turn those features into draft tokens. The result is a much better-aligned draft signal than an independently-trained small model can offer, and it's currently one of the fastest speculative methods in the family (reported ~3x over vanilla decoding).
**Taught in:** a follow-on to 11's basic draft-and-verify loop — 11 builds the mechanism EAGLE optimizes.

**[Medusa](https://arxiv.org/abs/2401.10774)** — Cai et al., *"Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"* (ICML 2024).
What to take from it: a different way to get draft tokens without a separate model at all — attach several extra lightweight prediction heads directly on top of the target model's last hidden state, each head predicting one future token position in parallel, then verify the resulting tree of candidates in one pass. Compare against EAGLE and the original Leviathan et al. approach: three genuinely different ways to generate a draft, same verification idea underneath.
**Taught in:** another follow-on to 11 — worth reading once you understand *why* draft-then-verify works, to see a structurally different way to produce the draft.

## Prefill/decode disaggregation

**[DistServe](https://arxiv.org/abs/2401.09670)** — Zhong et al., *"DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving"* (OSDI 2024).
What to take from it: prefill (compute-bound, processes the whole prompt at once) and decode (memory-bandwidth-bound, one token at a time) have such different resource profiles that running them on the *same* GPU means one phase's batching decisions constantly interfere with the other's latency — a large incoming prefill can stall decode for requests already streaming tokens back to users. DistServe's fix is to physically separate the two phases onto different GPU pools, transferring the KV cache between them, and optimizes for "goodput" (throughput that actually meets a latency SLO) rather than raw throughput.
**Taught in:** not a dedicated notebook here — a genuine frontier topic past what this curriculum builds by hand; 29b/29d's goodput and queueing framing is the closest hands-on preparation for understanding why this paper's metric choice matters.

**[Splitwise](https://arxiv.org/abs/2311.18677)** — Patel et al., *"Splitwise: Efficient Generative LLM Inference Using Phase Splitting"* (ISCA 2024).
What to take from it: the same phase-splitting idea as DistServe, argued from a hardware-economics angle — decode doesn't need the newest, most expensive GPUs (it's memory-bandwidth-bound, not compute-bound), so routing decode to older/cheaper hardware and prefill to the latest GPUs can cut cost 20%+ at higher throughput than a homogeneous cluster. Read DistServe and Splitwise back to back: same underlying observation, one paper argues it from a latency-interference angle and the other from a cost-per-GPU-hour angle.
**Taught in:** same as DistServe — a frontier topic, not built hands-on here.

## How to read an inference paper

A systems paper is not a math paper — the payoff is usually in a different place than you'd expect from an algorithms course. A working approach:

1. **Read the evaluation section first**, before the method. What hardware? What model sizes? What's the baseline being compared against, and is that baseline still relevant, or a strawman nobody actually runs anymore? A "2-4x improvement" over an already-obsolete baseline is a different claim than 2-4x over the current state of the art.
2. **Find the workload assumption.** Every serving paper implicitly assumes something about the traffic pattern it's optimizing for — request-size distribution, prefix-sharing rate, burstiness, SLO target. A technique that wins decisively on one workload shape can lose on another (notebook 29d's own finding — that partial overprovisioning can be *worse* than none — is exactly this kind of workload-dependent surprise). The paper's gains are conditional on its workload; check whether your workload looks anything like it.
3. **Separate the algorithmic idea from the systems engineering.** PagedAttention's algorithmic idea (paging) is maybe a paragraph; the engineering to make it fast in a real CUDA kernel is most of the paper's actual effort. Both matter, but they transfer differently — the idea generalizes to your own system; the specific kernel engineering usually doesn't without redoing the work.
4. **Check what's NOT compared.** Papers compare against contemporaneous baselines, not everything that came after. Reading AWQ (2023) without also knowing GPTQ (2023, earlier) and where the field went next (llm-compressor's current recommendations, per notebook 10b) gives an incomplete, dated picture of "how do I actually quantize a model in 2026."
5. **Trust benchmarks you can rerun over benchmarks you can only read.** Every technique in this reading list has a hands-on notebook in this curriculum that reproduces its core mechanism (however simplified) and measures a real number from real, executed code — that's deliberately the same discipline notebook 25 teaches for eval numbers, applied to systems claims: a number you derived yourself is worth more than a number you're trusting secondhand.

---

*Every notebook number above is followed hands-on in this curriculum — see the [main README](../README.md) for the full curriculum map. Suggestions for additions are welcome; the bar for inclusion is "explains a mechanism this curriculum builds or should build," not "recent."*
