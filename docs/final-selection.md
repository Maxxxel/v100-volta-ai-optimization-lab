# Jarvis — three frozen model baselines

**Dated research selection through R585; not production approval or a universal model ranking.** Three concrete configurations are retained for the next controlled harness phase. Official Agent benchmarks remain NOT MEASURED.

Role-complementary judgment using complete official coding/tools plus separately scoped authored agent, policy and resource observations. Not a statistically unique global ranking. No missing category is zero; no screening-only quality exclusion.

| Frozen model/configuration | Intended role | HumanEval+164 | BFCL parallel200 | User mean / official coverage | Separate authored Agent33 |
|---|---|---|---|---|---|
| [OmniCoder-9B · bartowski Q6](configuration-profiles/cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf.md) | Balanced Jarvis sandbox baseline | 134/164 | 178/200 | 85.35% ·2/3 | 28/33; policy 29/33 [R536](experiments/R536.md) |
| [Gemma4 12B IT QAT](configuration-profiles/cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625.md) | Coding-quality specialist | 156/164 | 154/200 | 86.06% ·2/3 | NOT MEASURED at selected8K |
| [Nexus 9B CodeCore Merge](configuration-profiles/cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba.md) | Fast coding/tool worker | 130/164 | 178/200 | 84.13% ·2/3 | 25/33; policy 29/33 [R531](experiments/R531.md) |

The arithmetic mean is user-defined and unofficial; only the two complete official categories enter it. Agent33 is not the missing third official category. Original coding/tool capture IDs remain separate and preserve their adapters and audit hashes.

## Balanced Jarvis sandbox baseline

OmniCoder bartowski Q6, MTP OFF combines134/164 coding,178/200 parallel tools and the separate28/33 authored agent result. Against Nexus it buys four more coding cases and three more local agent cases at greater cost; against Qwen3.5 it trades one coding case and more memory for two tool cases and five local agent cases. These finite differences are not population superiority or a safety certificate.

Frozen runtime ID: `cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf`. Weight SHA256: `a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052`.

| Category | Original capture | Exact profile |
|---|---|---|
| R516 | [R516](experiments/R516.md) | [cfg-9e79c90dcc63…](configuration-profiles/cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf.md) |
| R517 | [R517](experiments/R517.md) | [cfg-ef44057a9355…](configuration-profiles/cfg-ef44057a9355a2b971bac6e5dcf6f018050b972a796a26c03d68c09af2e52049.md) |

## Coding-quality specialist

Gemma4 nonthinking QAT8K has156/164 coding, the highest observed full coding count in this cohort, and154/200 tools. The separate16K Agent33 result is not assigned to this8K baseline. Coding work still requires external tests; tool/agent use is not its selected role.

Frozen runtime ID: `cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625`. Weight SHA256: `93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b`.

| Category | Original capture | Exact profile |
|---|---|---|
| R464 | [R464](experiments/R464.md) | [cfg-b3afa206e961…](configuration-profiles/cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625.md) |
| R472 | [R472](experiments/R472.md) | [cfg-aebfa2c88282…](configuration-profiles/cfg-aebfa2c88282523db04a6e6e6b802fcb8eb8912f4c2715d30c53e52ed40096e7.md) |

## Fast coding/tool worker

Nexus native Thinking disabled by template, temperature0 has130/164 coding and178/200 tools, with separate25/33 authored agents. Lower observed coding latency/energy than the balanced profile and stronger observed task quality than Ornith justify the worker role. Qwen3.5 remains a meaningful lower-memory alternative with135/164 coding and176/200 tools; Nexus is selected for its tool count, observed task latency and local-agent evidence, not universal Pareto dominance.

Frozen runtime ID: `cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba`. Weight SHA256: `b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c`.

| Category | Original capture | Exact profile |
|---|---|---|
| R488 | [R488](experiments/R488.md) | [cfg-7f520b133082…](configuration-profiles/cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba.md) |
| R489 | [R489](experiments/R489.md) | [cfg-694b972dbae1…](configuration-profiles/cfg-694b972dbae1a38c201067e11a2e410c6a002052b4f225c2ac9c158445b1ef9b.md) |

Requested/native controls are preserved verbatim in the packet. In Nexus, the engine reasoning flag is recorded ON while native `enable_thinking=false` selects the OFF template; neither field is silently rewritten. Cache/graph flags are requests, not proof of executed kernels. Unknown metadata stays unknown.

## Why the alternatives were not selected

These are role/resource decisions for this dated selection, not permanent bans. All exact runs, including losing variants, remain in the [candidate matrix and complete Pareto comparison](final-qualification.md).

| Alternative | Decision / scope |
|---|---|
| Canonical OmniCoder | The bartowski artifact has134 vs132 coding,178 vs177 tools and28 vs26 authored agent successes. Canonical remains a lower-cost alternative; this is not a causal quantizer comparison. |
| Qwen3.5 9B | Strong lower-VRAM alternative:135 coding,176 tools,23 local agents. Retained for resource-sensitive use; three role slots favor Omni for observed agent/tool outcomes and Nexus for worker latency/tool count. No global dominance claimed. |
| Qwen3.8 27B | MTP3 has151 coding,169 tools and26 agents/policy31. Gemma has higher observed coding, Omni has higher tool/agent counts, and the27B profile uses substantially more VRAM. Its better observed policy count is retained, not called a proven safety advantage. |
| Ornith1.5 | Fast measured responses remain useful;117 coding,170 tools and18 agents are below the selected worker counts130/178/25. Tiny latency differences do not prove a population speed ranking. |
| Slopus / Opus Distill | Complete OFF coding/tools remain archived. See the explicit observed category-quality/resource tradeoffs and deferred agent questions in the candidate matrix; screening was not the exclusion basis. |
| MiMo / LFM8 | Full categories are retained. Their observed quality/resource tradeoffs do not improve the selected role set; unmeasured Agent33 capabilities remain unknown. |
| LFM24 / Qwen3.6 / Bonsai | Current parallel-tool result6/200, budget-limited partial suites, historical over-budget coding or missing applicable qualifications prevent replacing the measured role baselines. Exact technical reasons and reopening conditions remain in the candidate matrix. |
| Qwen0.8 | Full17/164 and79/200 confirm the low-memory/quality tradeoff. Lowest memory alone does not meet the selected coding/agent roles; no rejection from its small development screen. |
| Ministral14 / Ministral8 | Full categories and authored agents measured:135/163/16 and128/153/17. Useful low task-time/energy alternatives, but weaker observed tool/agent outcomes than the balanced profile. No quality-preserving speedup is inferred. |
| Devstral24 / Mistral Small3.2 | Full122/175 and129/147 coding/tools respectively; Devstral22/33 local agents. Current resource/quality tradeoffs do not improve the three roles. Missing Mistral agent quality remains unknown. |
| GLM Flash | Default-thinking tools168/200, coding partial; native-off109/164 and154/200 is separate. High memory and the documented R581 resource confound limit an efficiency claim; no retry or profile pooling. |
| Phi4 | Coding134/164 is valid; current tool bridge produced repetition, length stops and3/32 partial within the task budget. Defer until a justified bridge/profile fix; no general model incapability claim. |
| gpt-oss20B | Parser-fixed150/164 coding is retained. Gemma has better observed coding, time, energy and memory on the compatible full protocol. Parallel-tool grammar remains limited; old0/200 and new coding have different builds. |
| Nemotron3 Nano | Startup180 gate was reached before tasks; no authorized extension, no proven OOM or quality score. Technically blocked rather than quality-rejected. |
| Other quantizations, MTP and engine variants | Every exact profile remains visible. Tool-scoped OmniMTP3 wins do not erase its coding/agent regression gates; GemmaQ8-key coding regression is retained. Historical or partial variants cannot borrow missing categories from another build or context. |
| Source-only derivatives / OxCoder | The pinned Issue16 feasibility/source review remains linked in open questions. No verified local advantage or unreviewed download is promoted. OxCoder stays stopped by owner instruction after weight-identity concerns; that is not a measured model-quality rejection. |

## Architecture and handoff to Issues17/18

Use the balanced single-model sandbox baseline first. The two specialists are measured alternatives for controlled routing/harness evaluation. Multi-model routing gains, cold-switch overhead and system-wide energy benefits are NOT MEASURED; do not claim routing superiority.

Begin with retained traces and CPU contract tests from [Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17), then the separately admitted lean-harness comparisons in [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18). Keep these frozen model baselines untouched; each harness or inference change gets its own profile and evidence. No exhaustive engine/MTP/quantization/kernel campaign is started by this selection.

## Frozen data and limits

[Download the three frozen baseline packets](https://raw.githubusercontent.com/Maxxxel/v100-volta-ai-optimization-lab/main/data/frozen-baselines.json). They contain ordered redacted launch arguments, environment, native sampling/template controls, model/build/library hashes and original benchmark references. They grant no execution authority; asset mapping and the existing broker are mandatory.

Selection SHA256: `cdee544e235958d72c0d36eb2ce11d5cdf1146a4509811a73e9904c1b5d17443`; frozen at `2026-10-27T09:51:14.086038+00:00`. New measurements append history and must not regenerate this dated freeze.

- Official Terminal-Bench remains technically blocked; no selected profile has3/3 official category coverage.
- Agent33 contains33 authored correlated cases/11 families and observed policy failures, not a safety certificate. External deterministic authorization and sandboxing remain mandatory.
- Selected Gemma8K has no Agent33 measurement at that exact context; its16K result remains adjacent evidence only.
- Unknown historical tokenizer, model revision, exact engine version or actual kernel-dispatch fields remain unknown; hashes and source receipts do not manufacture missing measurements.
- No continuous-uptime, production-stability, independent bit-identical rebuild or multimodel-routing qualification is asserted.
