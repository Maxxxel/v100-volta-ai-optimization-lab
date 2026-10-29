# Jarvis — three frozen model baselines

**Dated research selection through R585; not production approval or a universal model ranking.** Three concrete configurations are retained for the next controlled harness phase. Official Agent benchmarks remain NOT MEASURED.

Role-complementary judgment using complete official coding/tools plus separately scoped authored agent, policy and resource observations. Not a statistically unique global ranking. No missing category is zero; no screening-only quality exclusion.

| Frozen model/configuration | Intended role | HumanEval+164 | BFCL parallel200 | User mean / official coverage | Separate authored Agent33 |
|---|---|---|---|---|---|
| [OmniCoder-9B · bartowski Q6](configuration-profiles/cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf.md) | Balanced Jarvis sandbox baseline | 134/164 | 178/200 | 85.35% ·2/3 | 28/33; policy 29/33 [R536](experiments/R536.md) |
| [Gemma4 12B IT QAT](configuration-profiles/cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625.md) | Coding-quality specialist | 156/164 | 154/200 | 86.06% ·2/3 | NOT MEASURED at selected8K |
| [Nexus 9B CodeCore Merge](configuration-profiles/cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba.md) | Fast coding/tool worker | 130/164 | 178/200 | 84.13% ·2/3 | 25/33; policy 29/33 [R531](experiments/R531.md) |

The arithmetic mean is user-defined and unofficial; only the two complete official categories enter it. Agent33 is not the missing third official category. Original coding/tool capture IDs remain separate and preserve their adapters and audit hashes.


## Same-task paired quality comparison

CPU-only reanalysis of existing qualified captures; **no inference rerun**. Same task identities and scorer within each category. Results compare whole native profiles, not a model-only causal effect.

| Category | Model profile | Passes | Capture · runtime profile |
|---|---|---|---|
| Coding · HumanEval+164 | OmniCoder | 134/164 | R516 · cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf |
| Coding · HumanEval+164 | Gemma4 | 156/164 | R464 · cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625 |
| Coding · HumanEval+164 | Nexus | 130/164 | R488 · cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba |
| Coding · HumanEval+164 | Qwen3.5 | 135/164 | R465 · cfg-9fcb6193898540f39890fcfb16525895409d6b08f8de5165231fcbc0c17d2653 |
| Coding · HumanEval+164 | Qwen3.8 | 151/164 | R548 · cfg-a4e9c9254a524b23fdc69375ec9877659abc32781e5119545b2accd73aedbc09 |
| Tools · BFCL parallel_multiple200 | OmniCoder | 178/200 | R517 · cfg-ef44057a9355a2b971bac6e5dcf6f018050b972a796a26c03d68c09af2e52049 |
| Tools · BFCL parallel_multiple200 | Gemma4 | 154/200 | R472 · cfg-aebfa2c88282523db04a6e6e6b802fcb8eb8912f4c2715d30c53e52ed40096e7 |
| Tools · BFCL parallel_multiple200 | Nexus | 178/200 | R489 · cfg-694b972dbae1a38c201067e11a2e410c6a002052b4f225c2ac9c158445b1ef9b |
| Tools · BFCL parallel_multiple200 | Qwen3.5 | 176/200 | R474 · cfg-aae586a5fa23e08f528cfec90a0d3e1817a681b815a4b5329c4326467b848a55 |
| Tools · BFCL parallel_multiple200 | Qwen3.8 | 169/200 | R549 · cfg-8cd6433abaeb5e09d17a8b974cd6d3fe69ef3954760daeda19447b24d6b1a91a |

Each profile has one response per task. Paired task intervals describe task-set uncertainty, not run-to-run variability; task-family clustering and multiple-comparison adjustment are not applied. This analysis does not change the R585 frozen roles.

<details markdown="1"><summary>Coding: all 10 paired profile comparisons</summary>

| A | B | B−A pp | Paired-task 95% CI pp | A-only / B-only passes | Unadjusted McNemar p |
|---|---|---|---|---|---|
| OmniCoder | Gemma4 | +13.41 | [+7.66, +19.17] | 2 / 24 | 1.049e-05 |
| OmniCoder | Nexus | -2.44 | [-8.05, +3.17] | 13 / 9 | 0.5235 |
| OmniCoder | Qwen3.5 | +0.61 | [-4.61, +5.83] | 9 / 10 | 1 |
| OmniCoder | Qwen3.8 | +10.37 | [+4.59, +16.14] | 4 / 21 | 0.0009105 |
| Gemma4 | Nexus | -15.85 | [-21.71, -10.00] | 27 / 1 | 2.161e-07 |
| Gemma4 | Qwen3.5 | -12.80 | [-18.21, -7.40] | 22 / 1 | 5.722e-06 |
| Gemma4 | Qwen3.8 | -3.05 | [-6.61, +0.52] | 7 / 2 | 0.1797 |
| Nexus | Qwen3.5 | +3.05 | [-2.42, +8.52] | 8 / 13 | 0.3833 |
| Nexus | Qwen3.8 | +12.80 | [+7.14, +18.47] | 2 / 23 | 1.943e-05 |
| Qwen3.5 | Qwen3.8 | +9.76 | [+4.34, +15.18] | 3 / 19 | 0.0008554 |

Exploratory, unadjusted pairwise statistics; they are not a population ranking or replacement decision.

</details>

<details markdown="1"><summary>Tools: all 10 paired profile comparisons</summary>

| A | B | B−A pp | Paired-task 95% CI pp | A-only / B-only passes | Unadjusted McNemar p |
|---|---|---|---|---|---|
| OmniCoder | Gemma4 | -12.00 | [-17.48, -6.52] | 29 / 5 | 3.856e-05 |
| OmniCoder | Nexus | +0.00 | [-3.11, +3.11] | 5 / 5 | 1 |
| OmniCoder | Qwen3.5 | -1.00 | [-4.93, +2.93] | 9 / 7 | 0.8036 |
| OmniCoder | Qwen3.8 | -4.50 | [-8.50, -0.50] | 13 / 4 | 0.04904 |
| Gemma4 | Nexus | +12.00 | [+6.52, +17.48] | 5 / 29 | 3.856e-05 |
| Gemma4 | Qwen3.5 | +11.00 | [+5.14, +16.86] | 8 / 30 | 0.000472 |
| Gemma4 | Qwen3.8 | +7.50 | [+2.70, +12.30] | 5 / 20 | 0.004077 |
| Nexus | Qwen3.5 | -1.00 | [-5.39, +3.39] | 11 / 9 | 0.8238 |
| Nexus | Qwen3.8 | -4.50 | [-8.50, -0.50] | 13 / 4 | 0.04904 |
| Qwen3.5 | Qwen3.8 | -3.50 | [-8.19, +1.19] | 15 / 8 | 0.21 |

Exploratory, unadjusted pairwise statistics; they are not a population ranking or replacement decision.

</details>

Protocol identities, task-set hashes, per-profile audit hashes and aggregate pair counts: [download the analysis JSON](assets/paired-quality-analysis-2026-10-29.json). Raw task-level response records are not included in this public export.

## Reserved 8+8 profile validation · non-official

These locally measured cases are supplementary evidence only; they do not enter the official scores or user mean above. The same fixed 8 coding + 8 tool tasks were reused across five profiles, so the small samples are correlated across models and cannot establish a general ranking. They were independently CPU-replayed with no changed judgments.

| Profile | Coding · 8 tasks | Tools · 8 tasks | Total task phase · peak VRAM | Evidence |
|---|---|---|---|---|
| [Qwen3.5-9B](experiments/R509.md) · parent [R474](experiments/R474.md) | 8/8 · 93.2 tok/s · 624–637 GPU J/success | 6/8 · 55.2 tok/s · 276–293 GPU J/success | 26.8s · 5956 MiB | [audit](experiments/R509.md) · `c32f1defdd71` |
| [Gemma4-12B](experiments/R510.md) · parent [R472](experiments/R472.md) | 7/8 · 69.3 tok/s · 627–642 GPU J/success | 7/8 · 35.2 tok/s · 195–208 GPU J/success | 26.2s · 8118 MiB | [audit](experiments/R510.md) · `4b3e693eb56c` |
| [OmniCoder-9B](experiments/R511.md) · parent [R478](experiments/R478.md) | 8/8 · 76.4 tok/s · 667–680 GPU J/success | 6/8 · 49.4 tok/s · 324–337 GPU J/success | 27.7s · 7356 MiB | [audit](experiments/R511.md) · `dbceec90e287` |
| [Nexus-9B · OFF/T0](experiments/R526.md) · parent [R489](experiments/R489.md) | 6/8 · 74.6 tok/s · 559–574 GPU J/success | 5/8 · 55.8 tok/s · 496–509 GPU J/success | 22.4s · 7356 MiB | [audit](experiments/R526.md) · `240fa31ab141` |
| [Ornith-1.5-9B · OFF/T0](experiments/R527.md) · parent [R496](experiments/R496.md) | 7/8 · 74.5 tok/s · 476–493 GPU J/success | 5/8 · 57.4 tok/s · 530–546 GPU J/success | 22.7s · 7356 MiB | [audit](experiments/R527.md) · `032c85b436c2` |

Completion tokens, response time, validity, descriptive Wilson intervals, and full audit hashes are available in the [validation aggregate](assets/validation16.json). No task prompts, IDs, outputs, or per-task results are published. Do not interpret per-category GPU joules per success as whole-task energy; the meter brackets only the selected category request group.

## Post-freeze evidence through R630

The R585 selection above remains frozen and unchanged. These later measurements are appended evidence, not a retroactive rewrite or an automatic replacement decision.

- [R614](experiments/R614.md) Nexus-9B Q6 · prompt cache enabled: versus [R531](experiments/R531.md) on the same exposed33 tasks, task success 25/33→25/33; task wall 320.0→255.4s (20.18% observed), completed output 16,392→16,777 tokens, GPU counter energy 87.16–87.24→69.69–69.79kJ, policy passes 29/33→28/33. Cache candidates remain **NOT QUALIFIED**: the small exposed set has an observed policy-gate loss; output lengths differ; cache causality is unresolved.
- [R616](experiments/R616.md) OmniCoder-9B bartowski Q6 · prompt cache enabled: versus [R536](experiments/R536.md) on the same exposed33 tasks, task success 28/33→27/33; task wall 401.7→328.4s (18.24% observed), completed output 22,528→22,309 tokens, GPU counter energy 109.46–109.57→89.46–89.57kJ, policy passes 29/33→28/33. Cache candidates remain **NOT QUALIFIED**: the small exposed set has an observed policy-gate loss; output lengths differ; cache causality is unresolved.
- [Qwen3.8 MTP ON/OFF: R618/R625](experiments/R618.md): both completed the same reserved authored set at 27/33 and 27/33. Observed task wall 625.0s ON vs 761.5s OFF; outputs 12,110 vs 12,069 tokens, 8/150 matched requests produced different sequences, peak VRAM 13602 vs 12454MiB, GPU energy 162.02–162.13 vs 208.76–208.86kJ. Separate sessions, exposed correlated tasks: **exploratory profile comparison only**, not causal speedup, quality equivalence or Champion qualification.
- [R627](experiments/R627.md) Gemma KV-cache diagnostic: F16 and Q8 each repeated identically within arm on 3/3 exposed prompts; the two cache precisions differed on 2/3, first-token divergence on those cases. Three-case CPU EvalPlus replay is diagnostic only. No task-quality, safety or Champion qualification.
- [R620](experiments/R620.md) OmniCoder exact exposed R616 prompt: no-cache A/A outputs matched 4/4 at 558 tokens; cache-hit outputs differed from baseline at token 0 in 4/4 after 1,675 cached tokens. This is one request across two sessions, not task/policy causality or an internal GDN/numerical diagnosis; R616 remains **NOT QUALIFIED**.
  R630 independently repeated the unchanged no-cache R536 profile: all 154 request/token sequences and 33/33 exposed task outcomes matched. This makes the R536 baseline result reproducible in one same-profile pair, but does not estimate broad run-to-run variability. Together with R620, divergence is associated with the cache-enabled path; cache causation for the task/policy outcome remains unresolved, so R616 stays **NOT QUALIFIED**.
- [R630 same-profile A/A](reproducibility.md#same-profile-aa-repeatability-r536-r630): R536/R630 generated identical request/token sequences in 154/154 turns and identical outcomes in 33/33 exposed tasks (both 28/33 solved; policy gates 29/33). TASK time 401.663→401.311s (−0.088%, one descriptive pair); peak VRAM 7680.5 MiB both. Whole-phase energy bounds overlap (109,461.5–109,572.7 vs 109,447.6–109,549.6 J): no speed/energy winner or Champion change. Same exposed set, not an independent quality sample.
These measurements do not change the R585 roles. Full cache/state evidence and limitations are in [Reproducibility](reproducibility.md); incomplete causal and population-level conclusions remain explicit.

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
