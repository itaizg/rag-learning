# Source Map — X links & images → curriculum

This document maps 58 sources (54 X/Twitter links + 4 pasted images) collected 2026-07-30, read and
evaluated against the full 66-notebook AI Learning curriculum plus `ragkit/` and `agentkit/`. It
answers two questions: **what does each source teach, and where does that land in this branch** (§1,
§2), and **which notebooks does this batch reinforce or extend, and by how much** (§3). §5 summarizes
the gap findings; the full build recommendations live in a separate plan file (see below).

**Companion documents:**
- Build plan for the ranked gaps: `~/.claude/plans/x-links-gap-build.md`
- Raw per-source harvest notes (not committed): `<scratchpad>/links/L01–L54.md`, `<scratchpad>/ledger.md`

**Headline counts:** 58 sources processed, 0 unreadable-and-discarded, 3 unverified claims from one
repeat-offender account (one flagged by X's own Community Notes), ~15 substantive gap candidates
found, 3 sources form a single verified chain (a pasted paper → a real GitHub implementation → a
third confirming tweet).

---

## Verdict legend

| Verdict | Meaning |
|---|---|
| ✅ Covered | The repo already teaches this, at equal or greater depth. |
| ➕ Covered-deeper | The repo goes further than the source. |
| 🟨 Partial | The topic exists in this repo, but this specific angle/technique/number doesn't. |
| ❌ Missing | No notebook touches it — candidate gap. |
| 📌 Already mapped | Already recorded in `.claude/CLAUDE.md`'s Content Source Map from a prior gap analysis. |
| ♻️ Redundant | Restates content already covered by an earlier, canonical source in this same batch. |
| ⛔ Off-curriculum | Real content, but outside this repo's scope (career advice, finance/trading domain, generic DevOps). |
| ⚠️ Unverified | Claim could not be confirmed — no name, no link, or flagged by the platform itself. |

---

## 1. Source inventory

### Pasted images

| ID | Source | Media | Topic | What it says | Coverage | Notebook(s) |
|----|--------|:----:|-------|------|:----:|-------------|
| IMG-1 | n8n "first AI agent" template | 🖼 | `no-code-automation` | Chat trigger → AI agent node → Gemini model + memory + weather/news tools; a no-code state-machine/graph | ✅ | [20](04_agents/20_multi_agent_patterns.ipynb) (graph concept); cross-refs L53 |
| IMG-2 | "11 AI Protocols" chart | 🖼 | `mcp-and-protocols` | MCP, A2A, ACP, AG-UI, ANP / LSP, OpenAPI, OAuth2-for-Agents, OpenTelemetry-AI, JSON Schema, JSON-RPC 2.0 | 🟨 | [31](08_production/31_mcp.ipynb) covers MCP only; AG-UI confirmed used in L09; A2A/ACP/ANP not covered anywhere |
| IMG-3 | Karpathy, "LLM-WIKI.md" paper | 🖼 | `knowledge-management` | 3-layer (raw/schema/wiki) self-maintaining personal KB; ingest/query/lint primitives; compile-not-retrieve thesis | ❌→✅verified | **Resolved by L28** (real MIT repo) and L54 (3rd confirmation) |
| IMG-4 | "How to Design Good APIs" cheat sheet | 🖼 | `api-design` | Idempotency keys, URL/query-param versioning, noun-based resources, JWT structure, offset/limit pagination | ❌ | No notebook in this repo teaches general API design |

### X links (L01–L54)

| ID | Source | Author | Topic | Coverage | Notebook(s) / Notes |
|----|--------|--------|-------|:----:|-------------|
| L01 | [link](https://x.com/hanakoxbt/status/2065807526268920103) | @hanakoxbt | `loop-engineering` | ♻️ | Redundant with L03 (official source); cron/routines framing |
| L02 | [link](https://x.com/0x_kaize/status/2073743517155774641) | @0x_kaize | `loop-engineering`, `harness-engineering` | 🟨 | Outbound OpenAI "Harness engineering" essay → [21](04_agents/21_harness_engineering.ipynb): monolith-CLAUDE.md failure modes, docs-as-table-of-contents |
| L03 | [link](https://x.com/robj3d3/status/2074210108373119234) | @robj3d3 (→@ClaudeDevs) | `loop-engineering` | 🟨 | **Canonical**: official Claude Code 4-loop-type taxonomy → [23](04_agents/23_loop_engineering.ipynb) |
| L04 | [link](https://x.com/_avichawla/status/2074410748537889232) | @_avichawla | `loop-engineering` | ✅/🟨 | **Canonical synthesis**; no-progress detection, agent-facing errors → [19](04_agents/19_agent_loop_from_scratch.ipynb), [28b](08_production/28b_tool_contracts_and_reliability.ipynb) |
| L05 | [link](https://x.com/free_ai_guides/status/2074586339098730969) | @free_ai_guides | `harness-engineering` | 🟨 | `.claude/` anatomy: `rules/`, `agents/` absent from this repo's own `.claude/` and from [21](04_agents/21_harness_engineering.ipynb) |
| L06 | [link](https://x.com/sairahul1/status/2074790798584062278) | @sairahul1 | `career-and-roadmap` | 📌 | Already in CLAUDE.md; closed as 19c/22b/30b |
| L07 | [link](https://x.com/_avichawla/status/1911306413932163338) | @_avichawla | `rag`, `multi-agent`, `training` | ✅/🟨 | 2025 project listicle; mostly ✅; GRPO angle resolved by L15 |
| L08 | [link](https://x.com/saboo_shubham_/status/2075284848022114770) | @Saboo_Shubham_ | `multi-agent`, `cost` | ✅ | GPT-5.6 launch; orchestrator/advisor/workers role pattern ≈ [32](08_production/32_cost_engineering.ipynb) |
| L09 | [link](https://x.com/free_ai_guides/status/2075268642833674718) | @free_ai_guides | `agent-memory` | 🟨 | fact/case/rule taxonomy not in [22b](04_agents/22b_agent_memory.ipynb)/[22c](04_agents/22c_memory_lifecycle_and_extraction.ipynb) |
| L10 | [link](https://x.com/undefinedki/status/2075291386673233955) | @undefinedKi | `harness-engineering` | 🟨 | Verified `agency-agents` repo (MIT) — corroborates L05's `agents/` finding |
| L11 | [link](https://x.com/jeyxbt/status/2075451952700293353) | @0xJeyx | `career-and-roadmap` | ⛔ | No notebook gap |
| L12 | [link](https://x.com/rewind02/status/2075520067450589291) | @rewind02 | `agent-memory`, `harness-engineering` | 🟨 | procedural/semantic/episodic taxonomy; consolidation-via-cheaper-model pattern |
| L13 | [link](https://x.com/0xcodez/status/2074865699214741897) | @0xCodez | `agent-memory`, `loop-engineering` | ⚠️ | Video playback failed; chapter titles only, plausibly ✅ |
| L14 | [link](https://x.com/free_ai_guides/status/2075541620439814185) | @free_ai_guides | `loop-engineering` | ♻️ | Caption/image mismatch found; event-driven-vs-scheduled nuance |
| L15 | [link](https://x.com/akshay_pachaar/status/2075579659878854709) | @akshay_pachaar | `training` | ❌ | **GRPO + RULER** — verified `openpipe/art` (Apache-2.0). Real gap in [09](02_training/09_rlhf_and_alignment.ipynb) |
| L16 | [link](https://x.com/mikenevermiss/status/2075569898994946423) | @mikenevermiss (→@sairahul1) | `loop-engineering` | 🟨 | **Richest single loop source**: 4-condition test, STATE.md/VISION.md, "Ralph Wiggum Loop" failure mode |
| L17 | [link](https://x.com/nicos_ai/status/2075650259858915629) | @nicos_ai | `harness-engineering` | 🟨 | 3rd `.claude/` corroboration: `hooks/`, named `agents/verifier`, `.mcp.json` |
| L18 | [link](https://x.com/_avichawla/status/2075888860115120424) | @_avichawla | `cost` | ❌ | **Routing invalidates caching** — verified `katanemo/plano` (Apache-2.0). Gap in [32](08_production/32_cost_engineering.ipynb) |
| L19 | [link](https://x.com/milesdeutscher/status/2076348868229484597) | @milesdeutscher | `off-curriculum` | ⛔ | Trading domain |
| L20 | [link](https://x.com/akshay_pachaar/status/2076312850180739322) | @akshay_pachaar | `training` | ❌ | **RL environments** — verified `PrimeIntellect-ai/verifiers` (MIT). Companion gap to L15 |
| L21 | [link](https://x.com/0xmorlex/status/2076319852407517204) | @0xMorlex | `multi-agent` | ✅ | Specialist-team pattern, domain instance only |
| L22 | [link](https://x.com/saboo_shubham_/status/2076380344631398606) | @Saboo_Shubham_ | `tooling-and-products` | 🟨 | `/last30days` skill-marketplace pattern; ecosystem-level note |
| L23 | [link](https://x.com/archiveexplorer/status/2076666622043963789) | @ArchiveExplorer | `loop-engineering`, `harness-engineering` | ✅ | 5 real named Anthropic essay titles — see §6 action item |
| L24 | [link](https://x.com/eng_khairallah1/status/2075862184299565100) | @eng_khairallah1 | `loop-engineering`, `llm-as-judge` | ♻️/🟨 | "Taste as reward function" framing; reward-hacking example |
| L25 | [link](https://x.com/0xtatara/status/2077766829875839095) | @0xTatara | `training` | ⚠️ | Unverified "Stanford professor"; classical RL math, likely out of curriculum scope |
| L26 | [link](https://x.com/suryanshti777/status/2077829322778563013) | @Suryanshti777 | `loop-engineering`, `security` | 🟨 | Path-denylist guardrail ≈ [30c](08_production/30c_capability_based_agent_security.ipynb) |
| L27 | [link](https://x.com/cyrilxbt/status/2077603379036176605) | @cyrilXBT | `training` | 🟨 | 5-stage LLM pipeline; behavior→stage diagnostic framework |
| L28 | [link](https://x.com/nainsidwiv50980/status/2077668825731133908) | @NainsiDwiv50980 (→@Suryanshti777) | `knowledge-management` | ❌→verified | **Verifies IMG-3**: `AgriciDaniel/claude-obsidian` (MIT). Anchor finding of the batch |
| L29 | [link](https://x.com/akshay_pachaar/status/2077753829526056985) | @akshay_pachaar | `rag`, `cost` | ❌ | **"Retrieval tax"** — measured 4x cost gap in agent web search |
| L30 | [link](https://x.com/_vmlops/status/2077652116173426924) | @_vmlops | `mcp-and-protocols` | ⚠️ | Unverified Andrew Ng course; skills-vs-MCP distinction flagged conditionally |
| L31 | [link](https://x.com/mikenevermiss/status/2077594958656061623) | @mikenevermiss | `agent-frameworks` | ✅ | Already covered (Building Effective Agents via L23) |
| L32 | [link](https://x.com/sairahul1/status/2078004461218484440) | @sairahul1 | `agent-frameworks` | ⚠️ | "Agentic Design Patterns" plausible-but-unverified |
| L33 | [link](https://x.com/maxxfuu/status/2078056064906658113) | @maxxfuu | `inference-optimization` | 🟨 | vLLM internals naming precision vs [13b](03_building/13b_vllm_inference_serving.ipynb) |
| L34 | [link](https://x.com/bcherny/status/2077929379661844559) | @bcherny | `loop-engineering`, `security` | ✅ | **Real Boris Cherny**; "Steps of AI Adoption" artifact captured partially |
| L35 | [link](https://x.com/learnwithbrij/status/2078719046489649490) | @LearnWithBrij | `off-curriculum` | ⛔ | Generic CI/CD, zero AI content |
| L36 | [link](https://x.com/archiveexplorer/status/2078794082004963530) | @ArchiveExplorer | `agent-frameworks` | ❌ | **Google ADK** — verified `google/adk-python` (Apache-2.0). Gap in [20b](04_agents/20b_agent_framework_tradeoffs.ipynb) |
| L37 | [link](https://x.com/sairahul1/status/2078729934441435169) | @sairahul1 | `agent-frameworks`, `rag` | ✅ | `awesome-llm-apps` repo verified; practical reference, no gap |
| L38 | [link](https://x.com/akshay_pachaar/status/2078819660980764975) | @akshay_pachaar | `rag`, `data-engineering` | ❌ | **Chunk-as-unit critique / IdeaBlocks** — resolves this repo's own documented 24b chunking gotcha |
| L39 | [link](https://x.com/beamnxw/status/2081022966645535079) | @beamnxw | `loop-engineering`, `harness-engineering` | 🟨 | **⭐⭐ Symptom→layer→fix diagnostic table** — best synthesis in batch |
| L40 | [link](https://x.com/0xcodila/status/2080689998848778523) | @0xCodila | `multi-agent`, `agent-memory` | ⚠️ | Flagged by X Community Notes; typed-graph-memory divergence noted |
| L41 | [link](https://x.com/_avichawla/status/2080924298571813101) | @_avichawla | `evals`, `observability` | ❌ | **Opik self-repairing harness** — verified `comet-ml/opik`. Extends [33](08_production/33_ci_for_ai.ipynb) |
| L42 | [link](https://x.com/mdancho84/status/2081464099003641936) | @mdancho84 | `off-curriculum` | ⛔ | Career/portfolio advice |
| L43 | [link](https://x.com/akshay_pachaar/status/2081356379026280677) | @akshay_pachaar | `loop-engineering`, `harness-engineering` | 🟨 | **⭐⭐ "Unit of work" nesting + debugging heuristic** — cleanest artifact in batch |
| L44 | [link](https://x.com/0xcodila/status/2081477948134011284) | @0xCodila | `rag` | ⚠️ | Same unreliable account as L40 |
| L45 | [link](https://x.com/zodchiii/status/2081675600213745845) | @zodchiii (→@0x_rody) | `cost`, `agent-memory` | ❌ | **Graph-memory cost mechanics** — verified `getzep/graphiti` (Apache-2.0). "Effort is part of the cache key" gotcha |
| L46 | [link](https://x.com/sairahul1/status/2081737872579908017) | @sairahul1 | `prompting` | ✅ | Real Anthropic docs URL cited; process note, not a gap |
| L47 | [link](https://x.com/_avichawla/status/2082022230180118801) | @_avichawla | `rag`, `inference-optimization` | ❌ | **Binary quantization for RAG** — verified code + benchmark (32x memory, <30ms/36M vectors) |
| L48 | [link](https://x.com/elune0x/status/2082133200386555918) | @elune0x | `loop-engineering`, `harness-engineering` | 🟨 | 3rd disambiguation; real tool map; **diverges from L43 on nesting order** |
| L49 | [link](https://x.com/amitiitbhu/status/2082489293852008549) | @amitiitbhu | `foundations/architecture` | ✅/🟨 | 6/7 topics ✅; RMSNorm minor gap |
| L50 | [link](https://x.com/0xcodila/status/2082515252445655186) | @0xCodila | `loop-engineering` | ⚠️ | 3rd unverified claim, same account |
| L51 | [link](https://x.com/lunarresearcher/status/2082439168123138155) | @LunarResearcher | `multi-agent` | ⚠️ | Unverified "ICML" claim, disclosed-sponsored account |
| L52 | [link](https://x.com/techbyarti/status/2082403009385091318) | @TechByArti | `off-curriculum` | ⛔ | Generic interview coaching |
| L53 | [link](https://x.com/femke_plantinga/status/2082375583363944873) | @femke_plantinga | `multi-agent`, `no-code-automation` | ♻️ | 4th graph primer; **IMG-1 cross-reference found** |
| L54 | [link](https://x.com/rvaniaaaa/status/2082405530899808644) | @rvaniaaaa | `knowledge-management` | ✅verified | 3rd confirmation of IMG-3/L28, closes the batch |

---

## 2. Topic clusters — consensus, divergence, redundancy

### Loop / Harness / Graph Engineering (the dominant cluster — 24 of 58 sources)
**Sources:** IMG-1, L01–L04, L09, L12, L14, L16, L23, L24, L26, L27, L31, L34, L39, L40, L43, L44, L48, L50, L51, L53.

**Consensus:** the field converged mid-2026 on "stop hand-prompting, design the system that prompts
itself." A single 6-line agentic loop is a commodity; the real engineering lives one level up, in how
the loop is verified, terminated, and (once several loops must coordinate) organized as a graph.
Verifier-before-generator, evidence-not-confidence stop conditions, and mechanical enforcement over
prose instructions recur across nearly every independent source.

**Canonical sources** (read in full, most complete, least redundant): **L03** (official 4-type
taxonomy), **L04** (best single synthesis of "why loops are hard"), **L16** (richest artifact — the
4-condition build/don't-build test, file templates, 4th failure mode), **L39** and **L43** (the two
best disambiguations of harness vs. loop vs. graph, from independent authors, each with a distinct
useful framing — a diagnostic table and a "unit of work" nesting model respectively).

**Divergence — genuinely unresolved, not silently picked a winner:**
- **"Ralph Wiggum Loop" means opposite things** in two sources: L02's outbound OpenAI essay uses it
  for a *good* pattern (iterate a PR until every reviewer is satisfied); L16 uses it for a *failure
  mode* (an agent declaring a half-finished job done).
- **Harness/loop/graph nesting order conflicts** between L43 and L48. L43: prompt/context ⊂ harness
  (one pass) ⊂ loop (repeats a pass) ⊂ graph (coordinates loops) — graph is outermost. L48: prompt ⊂
  loop ⊂ graph ⊂ harness — harness is outermost. Both are internally coherent; they use "harness" to
  mean two different things (one execution pass's machinery vs. the total operating environment).

**Redundancy:** L01, L14, L24, L31, L44, L50, L53 are ♻️ substantially redundant with the canonical
four above — logged for completeness, contributing no unique technical content once graded against L03/L04/L16/L39/L43.

**Repo status:** `04_agents/23_loop_engineering.ipynb`, `21_harness_engineering.ipynb`, and
`20_multi_agent_patterns.ipynb` collectively cover most of the mechanics. The genuine additions — the
diagnostic table (L39), the unit-of-work debugging heuristic (L43), the 4-condition build test and
file templates (L16), and graph engineering as a *named, distinct* layer with its own failure modes
(not just "using LangGraph") — are not currently in any single notebook.

### `.claude/` Harness Structure (5 sources, 3-way corroborated)
**Sources:** L05, L10, L17, L22 (partial).
**Consensus:** Claude Code's `.claude/` directory has grown beyond CLAUDE.md into a five-to-seven
artifact family — `rules/` (modular instructions), `skills/` (SKILL.md procedures), `agents/`
(persona files, sometimes with a *named* `verifier` role), `hooks/` (event-driven automation),
`.mcp.json` (tool config), `MEMORY.md`. **This repo's own `.claude/` has none of `rules/`, `agents/`,
or `hooks/`** — a repo-hygiene finding, separate from curriculum content (see §5).
**No divergence** — all sources describe compatible, additive pieces of the same convention.

### Personal Knowledge Management / "Compile, don't retrieve" (3 sources, verified chain)
**Sources:** IMG-3, L28, L54.
**Consensus:** RAG re-derives knowledge every query; a compilation-layer wiki (raw sources → schema
→ generated pages, with ingest/query/lint as core operations) accumulates instead. **L28 verifies
this is a real, working, MIT-licensed system** (`AgriciDaniel/claude-obsidian`), and independently
confirms this repo's own `07_rag_learning/08` tiered-read pattern is production-proven. **A genuine
divergence surfaced in L28's own reply thread**, not from a different source: personal note-graphs
suit solo research; team/production context lives in services, PR history, and issue threads instead
— the pattern doesn't generalize past personal use without modification.

### Training-tier: GRPO, RL Environments, RL Math (4 sources)
**Sources:** L07 (partial), L15, L20, L25.
**Consensus:** GRPO (group-relative advantage, no separate reward model) is now the standard RL
technique for LLM reasoning training, and "environments" (dataset + harness + rubric, formalizable and
reusable) are the current bottleneck labs compete on. **Both L15 and L20 point to real, verified,
differently-licensed open-source projects** (`openpipe/art`, `PrimeIntellect-ai/verifiers`).
**L25's classical-RL-math angle is a different, deeper layer** (MDPs, Bellman equations, value
iteration) that this curriculum's applied focus has consistently chosen not to derive from scratch —
flagged as a scope call for the user, not a clean gap, given weak sourcing (unnamed "Stanford
professor," no link).

### Hidden Agent-Loop Costs (4 sources, all independently verified)
**Sources:** L18, L29, L45, L47.
**Consensus:** naive optimization at one layer can silently defeat savings at another — model routing
invalidates prompt caching (L18); raw web search returns pointers, not content, so a research loop
re-pays a "retrieval tax" on every hop (L29); graph-memory extraction bills at full frontier rates
unless caching/effort/batch levers are used correctly, and effort level is itself part of the cache
key (L45); naive chunking wastes 2-4x the achievable retrieval accuracy and memory footprint (L38, L47).
**All four cite real, verified open-source tools** (`katanemo/plano`, `getzep/graphiti`, and code
repos for the other two) and real measured numbers — the strongest, most consistently well-evidenced
cluster in the batch.

### Agent Memory Taxonomies (proliferation, no consensus)
**Sources:** L09, L12, L13 (unverified), L40.
**Divergence, not consensus**: four different classification schemes appear — fact/case/rule
(content-type, L09), procedural/semantic/episodic (cognitive-science, L12), short/persistent/long
(unverified, L13), typed-graph-triples (L40, unverified sourcing but real underlying pattern via
L45's Graphiti). None matches `22b`'s duration-based (short/working/long/episodic) scheme exactly.
Recorded as genuine terminological plurality in the field, not resolved to one "correct" taxonomy.

### Career & Roadmap (off-curriculum, consistent verdict)
**Sources:** L06 (📌), L11, L19, L35, L42, L52.
Consistently ⛔/📌 across the whole batch — portfolio advice, interview coaching, and one link with
zero AI content at all (generic CI/CD). No notebook gaps proposed from this cluster.

### Model Launches / Product News
**Sources:** L08 (GPT-5.6), L46 (Opus 5 prompting guide).
L08 is ~95% marketing with two extractable engineering patterns (Programmatic Tool Calling,
default multi-agent mode) already conceptually covered by nb22/nb20. L46 cites a real Anthropic docs
URL — the one piece of genuinely fast-moving, version-specific content in the batch, better suited to
this repo's `claude-api` skill than a static notebook.

---

## 3. Reverse map — notebook → reinforcing / extending sources

| Notebook | Reinforced by | Extended by (partial gaps) |
|---|---|---|
| [02_training/09_rlhf_and_alignment.ipynb](02_training/09_rlhf_and_alignment.ipynb) | L07 | **L15 (GRPO+RULER), L20 (RL environments), L25 (unverified — scope call)** |
| [03_building/14_rag_fundamentals.ipynb](03_building/14_rag_fundamentals.ipynb) | L07, L21 | **L38 (IdeaBlocks/chunk-unit critique)** |
| [03_building/15_vector_databases.ipynb](03_building/15_vector_databases.ipynb) | — | **L47 (binary quantization, verified benchmark)** |
| [03_building/13b_vllm_inference_serving.ipynb](03_building/13b_vllm_inference_serving.ipynb) | — | L33 (internal component naming, minor) |
| [04_agents/18_what_is_an_agent.ipynb](04_agents/18_what_is_an_agent.ipynb) | L31, L39, L43 | — |
| [04_agents/19_agent_loop_from_scratch.ipynb](04_agents/19_agent_loop_from_scratch.ipynb) | L03, L04, L16 | **L04 (no-progress detection), L29 (real web-search tool design)** |
| [04_agents/20_multi_agent_patterns.ipynb](04_agents/20_multi_agent_patterns.ipynb) | L07, L21 | **L39/L43/L48 (graph engineering as a distinct layer)**, IMG-1/L53 (n8n-as-graph example) |
| [04_agents/20b_agent_framework_tradeoffs.ipynb](04_agents/20b_agent_framework_tradeoffs.ipynb) | L37 | **L36 (Google ADK), L02 (PydanticAI/OpenHands)** |
| [04_agents/21_harness_engineering.ipynb](04_agents/21_harness_engineering.ipynb) | L23, L34 | **L02 (monolith-CLAUDE.md failure modes), L05/L10/L17 (rules/agents/hooks/.mcp.json), L39 (6-component checklist), L26 (path-denylist guardrails)** |
| [04_agents/22_context_engineering.ipynb](04_agents/22_context_engineering.ipynb) | L02, L04 | — |
| [04_agents/22b_agent_memory.ipynb](04_agents/22b_agent_memory.ipynb) | — | **L09, L12 (memory taxonomy plurality)** |
| [04_agents/22c_memory_lifecycle_and_extraction.ipynb](04_agents/22c_memory_lifecycle_and_extraction.ipynb) | L28, L54 | **L09 (trace-vs-fix signal distinction), L12 (consolidation-via-cheaper-model), L40/L45 (graph memory + cost)** |
| [04_agents/23_loop_engineering.ipynb](04_agents/23_loop_engineering.ipynb) | L01, L03, L04, L14, L24, L31 | **L16 (4-condition test, STATE.md/VISION.md, 4th failure mode), L39 (diagnostic table), L43 (unit-of-work + debug heuristic), L48 (tool map)** |
| [05_evaluation/26_llm_as_judge.ipynb](05_evaluation/26_llm_as_judge.ipynb) | — | **L41 (G-Eval, LLM juries — needs grep-check)** |
| [05_evaluation/27b_agent_evals.ipynb](05_evaluation/27b_agent_evals.ipynb) | — | L20 (task-suite ≈ RL-environment framing) |
| [07_rag_learning/00_setup_and_foundations.ipynb](07_rag_learning/00_setup_and_foundations.ipynb) | — | **L38 (chunk-unit critique — directly resolves a documented gotcha)** |
| [07_rag_learning/08_hierarchical_and_tiered_retrieval.ipynb](07_rag_learning/08_hierarchical_and_tiered_retrieval.ipynb) | **L28, L54 (independent production confirmation)** | — |
| [08_production/28b_tool_contracts_and_reliability.ipynb](08_production/28b_tool_contracts_and_reliability.ipynb) | L04 | — |
| [08_production/30_security_and_guardrails.ipynb](08_production/30_security_and_guardrails.ipynb) | L34 | — |
| [08_production/30c_capability_based_agent_security.ipynb](08_production/30c_capability_based_agent_security.ipynb) | L34 | L26 (loop-specific path-denylist instance), L38 (metadata-as-governance in RAG) |
| [08_production/31_mcp.ipynb](08_production/31_mcp.ipynb) | IMG-2, L28, L54 | L17 (`.mcp.json` as harness artifact), L30 (skills-vs-MCP, unverified) |
| [08_production/32_cost_engineering.ipynb](08_production/32_cost_engineering.ipynb) | L08 | **L18 (routing-invalidates-caching), L45 (effort-is-cache-key)** |
| [08_production/33_ci_for_ai.ipynb](08_production/33_ci_for_ai.ipynb) | L16 | **L41 (auto-growing regression suites, agent-assisted diagnosis)** |
| [09_frontier/36_data_engineering_for_ai.ipynb](09_frontier/36_data_engineering_for_ai.ipynb) | — | L38 (semantic dedup specificity, needs grep-check) |
| [01_foundations/04_attention_mechanism.ipynb](01_foundations/04_attention_mechanism.ipynb) | L49 | — |
| [01_foundations/05_transformer_architecture.ipynb](01_foundations/05_transformer_architecture.ipynb) | L49 | L49 (RMSNorm, minor) |
| [01_foundations/05b_moe_and_attention_variants.ipynb](01_foundations/05b_moe_and_attention_variants.ipynb) | L49 | — |
| [01_foundations/06_how_llms_work.ipynb](01_foundations/06_how_llms_work.ipynb) | — | L27 (stage→behavior diagnostic framework) |
| `claude-api` skill (not a notebook) | — | L46 (Opus 5 prompting guide, real docs URL) |

**Notebooks in this batch's scope but untouched by any source**: `00_setup/00_environment_check`,
most of Tier 1 (01–03), `02_training/07`, `07b`, `08`, `10`, `11`, `03_building/12`, `13`, `13c`,
`16`, `16b`, `17`, `04_agents/19b`, `19c`, `06_projects/P1–P4`, `05_evaluation/24`, `24b`, `25`,
`27`, `08_production/28`, `29`, `30b`, `32b`, `09_frontier/34`, `35`. Not a gap signal — this batch's
content simply clusters around agent loops/harnesses, RAG, training, and cost, not these tiers.

---

## 4. Unreadable & excluded

| ID | Reason |
|---|---|
| L13 | Video playback stalled on the opening frame through multiple retries; chapter titles recovered from the caption, no depth beyond that |
| L25 | "Stanford professor" claim — no name, course number, or link found; one video frame showed a presenter at a whiteboard, nothing confirming the claim |
| L30 | "Andrew Ng dropped a masterclass" — no link found; video did not render a usable frame |
| L32 | "Senior Google engineer... Agentic Design Patterns" — plausible (a real resource by this name exists in the wild) but not independently confirmed in this pass |
| L40, L44, L50 | Same account (@0xCodila), same "Google just released..." pattern repeated 3 times with no link each time; L40 additionally carried an active X Community Notes flag |
| L51 | "ICML researchers just published..." — no paper title/authors; account bio discloses all its content is sponsored |
| L19, L35, L42, L52 | ⛔ Off-curriculum — trading/finance domain, generic CI/CD, portfolio advice, and interview coaching respectively; none touch AI/LLM engineering |
| L34 (partial) | Boris Cherny's linked first-party Claude Artifact ("Steps of AI Adoption") repeatedly failed to render past step 2 of ~4 in this automated browser session; recommend the user open it directly: `https://claude.ai/code/artifact/bfdfaef9-bc62-4dfe-ba9e-c58a26c9accf` |

No video in this batch required tier V1/V2 (caption track or outbound transcript) to resolve — the
few videos read successfully were screen-recordings with legible static frames (V3); the rest were
either talking-head-with-no-slides (declined per the plan's cost guidance) or failed to render
technically. No source was skipped as unsafe.

---

## 5. Gap summary

**~15 gap-list candidates found**, split across confidence tiers:

**High-confidence, verified (real OSS + measured numbers), ranked by strength:**
1. GRPO + RULER (L15) — `openpipe/art`, Apache-2.0
2. RL environments (L20) — `PrimeIntellect-ai/verifiers`, MIT
3. Chunk-as-retrieval-unit critique (L38) — resolves this repo's own documented `24b` gotcha
4. Routing-invalidates-caching (L18) — `katanemo/plano`, Apache-2.0
5. Graph-memory cost mechanics + "effort is part of the cache key" (L45) — `getzep/graphiti`, Apache-2.0
6. "Retrieval tax" in agent web search (L29) — measured 4x cost gap
7. Binary quantization for RAG (L47) — measured 32x memory reduction, verified benchmark
8. Self-repairing observability / auto-growing regression suites (L41) — `comet-ml/opik`
9. Google ADK missing from framework comparison (L36) — `google/adk-python`, Apache-2.0
10. `.claude/` structure — `rules/`, `agents/`, `hooks/`, `.mcp.json` (L05, L10, L17 — 3-source corroborated; repo-hygiene, not curriculum content)

**Strong synthesis candidates (no new mechanics, but valuable framing not currently taught):**
11. Symptom→layer→fix diagnostic table (L39)
12. "Unit of work" nesting + debugging heuristic (L43)
13. Loop 4-condition build/don't-build test + STATE.md/VISION.md artifacts (L16)

**Minor / low-priority:**
14. RMSNorm as a named LayerNorm alternative (L49) — grep-confirmed absent from all notebooks
15. G-Eval / LLM-juries naming in `26_llm_as_judge` (L41) — grep-confirmed absent (the only "jury"
    matches repo-wide are base64 image data and the word "injuries")

**Grep verification (2026-07-30, post-map review):** the top ❌ verdicts were checked against actual
notebook content, not just the inventory: GRPO appears nowhere except P1's citation of Fareed Khan's
pipeline stages (so nb09's gap is real); "binary quant"/"packbits"/"hamming" appear in no notebook
(L47's gap is real); "affinity" appears in no notebook (L18's gap is real); RMSNorm appears nowhere.

**Considered and explicitly rejected** (looked like gaps, turned out covered):
- Memory taxonomies beyond nb22b's — recorded as a **divergence**, not a gap; four incompatible
  schemes across sources means there's no single "correct" one to adopt.
- L25's classical RL math (MDPs, Bellman equations) — a scope call, not a gap; would be a genuine
  depth expansion beyond this curriculum's consistently applied-first pattern, and the sourcing is
  too weak to build a citation on.
- "Agentic Design Patterns" (L32) and the Andrew Ng course (L30) — plausible but unverified; not
  built into the gap list without independent confirmation.

**Full build-ready plan** (priorities, prerequisites, notebook sections, exercises) is in
`~/.claude/plans/x-links-gap-build.md`. **Project memory entry** recording this analysis for future
sessions is at `x-links-gap-analysis.md` in this project's memory directory.

---

## 6. One process finding, not a content gap

If the five Anthropic essay titles cited in L23's outbound article are real (**"Building Effective AI
Agents," "Building agents with the Claude Agent SDK," "Effective context engineering for AI agents,"
"Effective harnesses for long-running agents," "Equipping agents for the real world with Agent
Skills"** — plausible, all Anthropic-plausible titles, not independently re-verified against
anthropic.com in this pass), this curriculum's Content Source Map currently cites these concepts only
through third-party tweets, never Anthropic's own posts directly. Worth a follow-up check.

---

## Addendum, 2026-08-02: Agent Eval Gates

A six-step agent eval-gate architecture (judge bias hygiene → verdicts wired into control flow →
three-level grading → trace-mined evals → judge pinning/rubrics → blast-radius merge gate) was shared
directly in conversation from an X (Twitter) thread. Web searches on several of the article's
distinctive verbatim lines (e.g. "the score you are reading is partly about your judge," "a verdict
that does not change the run is a report," "open the gate on blast radius, not on confidence") did not
surface the original post — X is poorly indexed by web search and not fetchable unauthenticated, so
the exact author/URL could not be recovered independently. It extends `05_evaluation/26_llm_as_judge`
and `27b_agent_evals`, and feeds `08_production/33_ci_for_ai`; built as
`05_evaluation/27c_agent_eval_gates.ipynb` + `agentkit/gates.py`. This is a standalone addition, not
part of the 58-source snapshot audited above.

---

## Addendum, 2026-08-12: CI/CD Eval Gate Policy

Two URLs were supplied directly in conversation:

| Source | Verdict | Coverage before this build | Notebook(s) |
|---|:---:|---|-------------|
| Confident AI, ["Best AI Evaluation Tools for CI/CD"](https://www.confident-ai.com/knowledge-base/compare/best-ai-evaluation-tools-for-ci-cd) | ❌ Missing | `08_production/33_ci_for_ai`'s `regression_gate` was a single-sample, zero-tolerance comparison — no variance calibration, no absolute floor, no slice check. The article's dual-threshold and variance-first design was genuinely absent. | `08_production/33b_eval_gate_policy.ipynb` |
| CircleCI, ["CI/CD Testing Strategies for Generative AI Apps"](https://circleci.com/blog/ci-cd-testing-strategies-for-generative-ai-apps/) | 🟨 Partial | 5 of its 6 strategy families were already covered (hallucination/faithfulness in 26 & 27c, bias in 26, drift in 27, latency in 13c/29, adversarial in 30) — its own contribution is the failure-mode-to-check framing, not new mechanics. Contains no code. | `08_production/33b_eval_gate_policy.ipynb` §A (orientation only) |

**Caveat carried into the notebook:** the Confident AI piece is a vendor comparison that ranks its
own product first among 9 tools (Confident AI, Noveum, Promptfoo, MLflow 3, Arize Phoenix, LangSmith,
Braintrust, Ragas, LangWatch). The gate-policy mechanics (variance calibration, dual thresholds,
min-pass-of-n, slice checks, staged coverage, versioned release evidence) are sound and were built as
real, executable code; the 9-tool ranking itself is treated as marketing and presented with an
explicit skepticism note in the notebook's tool-landscape section rather than restated as fact.

Built as `08_production/33b_eval_gate_policy.ipynb` (🟡) + `agentkit/evalgate.py`, hardening
`33_ci_for_ai.ipynb`'s gate and feeding `05_evaluation/27c_agent_eval_gates.ipynb`'s `MergeGate` via a
new `gate_evidence()` conversion. This is a standalone addition, not part of the 58-source snapshot
audited above.
