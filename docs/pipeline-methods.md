# Benchmark pipeline decision

**CPU retrospective study · 2026-10-24 · no new GPU runs.**

Keep normal full benchmark comparisons and add small independent development diagnostics before justified tuning. **Do not introduce automatic quality elimination or a screening highscore.**

## What the archived data show

15 complete category profiles; the fixed family-hash split leaves 2 coding and 4 tool validation profiles. The table shows **counterfactual additional request time**, not measured GPU savings. Screened development tasks are followed by a fresh full confirmation; original official tests are never reused as development prompts.

| Category | Sampling | Tasks | Unique correct top set · MC95 | Projected request-time overhead | Projected added GPU-counter energy |
| --- | --- | --- | --- | --- | --- |
| coding | random without replacement | 16 | 74.1% (71.3–76.7%) | +9.51% | +36.0–+39.5 kJ |
| coding | random without replacement | 24 | 81.3% (78.8–83.6%) | +14.67% | +55.8–+60.6 kJ |
| coding | random without replacement | 32 | 89.9% (87.9–91.6%) | +19.23% | +73.4–+79.3 kJ |
| coding | calibration difficulty quartiles | 16 | 74.3% (71.5–76.9%) | +9.73% | +36.8–+40.3 kJ |
| coding | calibration difficulty quartiles | 24 | 81.6% (79.1–83.9%) | +14.62% | +55.6–+60.4 kJ |
| coding | calibration difficulty quartiles | 32 | 87.9% (85.7–89.8%) | +19.56% | +74.6–+80.6 kJ |
| tools | random without replacement | 16 | 36.7% (33.8–39.7%) | +6.80% | +46.2–+53.6 kJ |
| tools | random without replacement | 24 | 45.3% (42.2–48.4%) | +10.88% | +75.2–+85.5 kJ |
| tools | random without replacement | 32 | 49.2% (46.1–52.3%) | +14.08% | +97.1–+109.9 kJ |
| tools | calibration difficulty quartiles | 16 | 39.1% (36.1–42.2%) | +8.03% | +56.4–+63.8 kJ |
| tools | calibration difficulty quartiles | 24 | 48.0% (44.9–51.1%) | +12.02% | +84.8–+95.1 kJ |
| tools | calibration difficulty quartiles | 32 | 51.0% (47.9–54.1%) | +16.01% | +113.4–+126.3 kJ |


MC95 describes resampling-frequency uncertainty, not unseen-model quality. All 24000 subset draws reuse fixed archived answers; they are not GPU runs or independent model seeds. A tied first place is not counted as a unique correct winner. Zero observed rejection of the true validation winner does not establish zero future risk.

<details><summary>All sizes, rules and calibration split</summary>

| Category | Sampling | Tasks | Unique correct top set · MC95 | Projected request-time overhead | Projected added GPU-counter energy |
| --- | --- | --- | --- | --- | --- |
| coding | random without replacement | 8 | 59.0% (55.9–62.0%) | +4.04% | +15.2–+17.1 kJ |
| coding | random without replacement | 48 | 95.5% (94.0–96.6%) | +28.91% | +110.9–+118.7 kJ |
| coding | random without replacement | 64 | 98.9% (98.0–99.4%) | +38.96% | +150.2–+159.1 kJ |
| coding | calibration difficulty quartiles | 8 | 58.0% (54.9–61.0%) | +4.82% | +18.2–+20.1 kJ |
| coding | calibration difficulty quartiles | 48 | 95.0% (93.5–96.2%) | +29.06% | +111.4–+119.2 kJ |
| coding | calibration difficulty quartiles | 64 | 98.7% (97.8–99.2%) | +39.51% | +152.5–+161.3 kJ |
| tools | random without replacement | 8 | 17.8% (15.6–20.3%) | +3.75% | +25.7–+30.0 kJ |
| tools | random without replacement | 48 | 63.7% (60.7–66.6%) | +19.42% | +132.1–+149.2 kJ |
| tools | random without replacement | 64 | 70.7% (67.8–73.4%) | +26.14% | +179.5–+199.9 kJ |
| tools | calibration difficulty quartiles | 8 | 18.8% (16.5–21.3%) | +4.02% | +28.0–+32.2 kJ |
| tools | calibration difficulty quartiles | 48 | 62.0% (59.0–65.0%) | +23.87% | +170.0–+187.2 kJ |
| tools | calibration difficulty quartiles | 64 | 71.3% (68.4–74.0%) | +32.00% | +229.3–+249.7 kJ |


**coding**: reference R471; calibration R466, R464, R452; validation R454, R465.

**tools**: reference R478; calibration R477, R479, R472, R482; validation R476, R480, R474, R484.

Random sampling is without replacement. Stratification uses calibration-profile difficulty quartiles and reference prompt lengths as tie-breakers. The rejection rule is a one-sided exact finite-population hypergeometric upper bound below the fixed reference by more than10 percentage points, alpha0.01; stratified bounds use a simultaneous per-stratum allocation. This is a retrospectively evaluated rule, **not an activated admission policy**. Hardware startup, CPU scoring and orchestration overhead are excluded from the cost projection and may increase real costs.

</details>

## Evidence census — distinct units

| Unit | Verified value |
| --- | --- |
| Registered capture profiles | 283 |
| Profiles with benchmark evidence | 63 |
| Recorded model-family IDs with results (aliases possible) | 15 |
| Model artifact IDs with results | 51 |
| Exported result views | 78 |
| Deduplicated task-set observations | 63 |
| Qualified complete task-set observations (includes archived protocols) | 31 |
| Partial task-set observations | 11 |
| Hash-registered captures with explicit GPU execution evidence | 54 |
| Other/legacy capture directories not classified by this reader | 197 |
| Completed protected task clocks | 24 |
| Recorded task-window seconds, not GPU busy seconds | 16997.813959022 |
| Recorded startup-window seconds | 2092.278287809 |
| Original variant fields | 355 |
| Variant fields with recorded hardware scope | 181 |
| Global GPU busy time / total project energy | NOT MEASURED |
| Avoidable repeats / developed but unexecuted implementations | NOT ESTABLISHED |


These counts describe the frozen study-input snapshot; later experiment additions belong to the live history. The inventories overlap and must never be summed. The 54 explicit GPU capture witnesses are a verified subset, not the project total. A review, build, submission, start marker or export is not an additional GPU test. No legacy record was relabelled to force a complete census.

## Executed independent development comparisons

| Experiment | Model | Matched development tasks | Completed requests |
|---|---|---|---|
| [R487](experiments/R487.md) | Nexus9B Q6_K · controlled Thinking development | 32 | 96/96 |


These are actual independent development-task runs, separate from the retrospective resampling above. This list does not establish screening validity across models. A model absent here has no recorded result on this development set; its official benchmark answers must not be substituted as a development reference. No candidate-selection or cross-model screening claim follows from Nexus-only A/B/C evidence.

## Nexus: first controlled development comparison

| Arm | Thinking | Temperature | Output tokens |
| --- | --- | --- | --- |
| A | True | 0.6 | 4096 |
| B | False | 0.6 | 4096 |
| C | False | 0 | 4096 |


A→B changes only native Thinking; B→C changes only temperature. Keep weights, engine/kernel, template bytes, remaining sampler settings and scorer fixed. Start with16 newly frozen coding and16 mock-tool development cases, covering four declared task/error types per category. This is a low-cost diagnostic design, **not proof of ranking reliability or a basis for rejecting small score differences**. At the methods-audit snapshot, workload freezing, CPU scorer controls and broker admission remained pending; each is a separate pre-execution gate.

One shared1,200-second task clock covers all three arms and all parts. Predeclare counterbalanced task triples; no token-limit reduction or clock reset. Report successes, valid final responses, completion/reasoning tokens, latency, GPU energy including failures and VRAM. If capped, disclose matched task IDs and actual coverage. Temperature0 requests greedy sampling; bitwise deterministic CUDA execution is not assumed.

## Budget and scheduling

The current owner-authorized budget is **1,200 seconds for the whole task phase**. The admitted class separately bounds startup180 s, cleanup60 s and outer wall1,440 s. All 24 completed protected task clocks in this snapshot use1,200 s. The actual systemd wrapper can end a run earlier; record it separately. Legacy900-second contracts and code paths remain historical and are not rewritten or repurposed for new task-phase tests.

CPU work may accompany only prepared, broker-approved GPU research: one GPU lease, bounded CPU/RAM/I/O, no overlapping heavy jobs, no manufactured utilization. No automatic screening launch, new GPU scheduler or broker-policy change is introduced here.

## Jarvis role evaluation — plan only

| Comparison | Controlled resource |
| --- | --- |
| Single agent | Same task fixtures and model profile; equal TOTAL token/task-time budget across all roles |
| Planner + worker | Same task fixtures and model profile; equal TOTAL token/task-time budget across all roles |
| Planner + worker + reviewer | Same task fixtures and model profile; equal TOTAL token/task-time budget across all roles |
| Role-specialized model routing, only after same-model controls | Same task fixtures and model profile; equal TOTAL token/task-time budget across all roles |


Use one centrally scheduled GPU worker and reuse the loaded model. Compare whole-task success, calls, all generated tokens, wall time, GPU J/success, failed delegations, duplicate work, context loss, reviewer corrections/false alarms and permission violations. Development tools are mocks in isolated coding/automation tests; no real home, virtualization or GitHub write actions and no additional Codex agents.

[MultiAgentBench (Zhu et al.,2025)](https://aclanthology.org/2025.acl-long.421/) motivates separate task-outcome and coordination measurements; [MARBLE source at 8d60fa17b559](https://github.com/ulab-uiuc/MARBLE/tree/8d60fa17b5596b44458a52d4296061b9fc13d6f2) is pinned as external evidence. Its code, judge and remote APIs are not executed. No official MultiAgentBench or Terminal-Bench score is claimed.

## Limits and original evidence

- Only6 full coding and9 full parallel-tool profiles; family-hash split leaves2 coding and4 tool validation profiles. Shared architectural/training lineage may remain.
- All24,000 draws reuse archived fixed responses. They are CPU simulations, not24,000 GPU runs, independent seeds, unseen tasks or measured future savings.
- Confidence bounds describe the finite official task population under the specified random design. Monte Carlo intervals quantify resampling-frequency error, not quality generalization or unseen-model risk.
- Request-window cost projection assumes unchanged replies under subset/order changes; startup, extra CPU scoring, orchestration and cache effects can further increase real cost. No actual GPU-hours saved claim.
- Incomplete profiles, including Nexus and Slopus coding prefixes, are excluded from this full-task retrospective. Diagnosing timeout/thinking failures remains necessary before model rejection.
- Study inputs and task-level responses remain in the local private archive. Public hashes and aggregates do not make withheld raw responses publicly reproducible.
- No comparable total of project-wide GPU-busy seconds, joules, avoidable repetitions or developed-but-unexecuted implementations is established by this bounded census.

CPU controls: **5 unit tests, 3486 exact finite-population coverage controls and 16 comparisons with the reviewed counter-bound function**.

[audit-e27136a1a8fadb74ef27](audits/audit-e27136a1a8fadb74ef27.md), [audit-c0841e498189e24dc746](audits/audit-c0841e498189e24dc746.md), [audit-0b536a5614264eb5e25c](audits/audit-0b536a5614264eb5e25c.md), [audit-a49a6cebc54822e25a33](audits/audit-a49a6cebc54822e25a33.md), [audit-543fb9745a67c9c58b9e](audits/audit-543fb9745a67c9c58b9e.md), [audit-bd72425d4fcd1c6575db](audits/audit-bd72425d4fcd1c6575db.md), [audit-0725b527fc77fa0b1bc3](audits/audit-0725b527fc77fa0b1bc3.md), [audit-7bfd00d2fcca7e4c767d](audits/audit-7bfd00d2fcca7e4c767d.md), [audit-89329075d5e77e4cc223](audits/audit-89329075d5e77e4cc223.md), [audit-fd5e36fba5b2d3f8f325](audits/audit-fd5e36fba5b2d3f8f325.md), [audit-249c3e61da453d096d87](audits/audit-249c3e61da453d096d87.md), [audit-9facd2474e8be80aa0fa](audits/audit-9facd2474e8be80aa0fa.md), [audit-ae71481c7169f4a37b52](audits/audit-ae71481c7169f4a37b52.md), [audit-2b900d67234b3bf493bc](audits/audit-2b900d67234b3bf493bc.md), [audit-a7f63146ef37d27560d5](audits/audit-a7f63146ef37d27560d5.md), [audit-b0dcae0da912bdcab55d](audits/audit-b0dcae0da912bdcab55d.md)

| Frozen identity | SHA256 |
| --- | --- |
| Methods audit | e27136a1a8fadb74ef273477fc2d9bed087126f6bffe7fc75381a6888a10d7bc |
| Analysis plan | 9d73c8186d1ba92c1107fc5e4597932290ae335794361ef00939729d519d4a64 |
| Analysis result | 8faf68972992cbde07bd146b1b0820cd4f8bb88ca101bb785a3391ff7c4de2aa |
| Analysis code | 9f70de0e38af05ed492e0248d55fb3a2e619388c893c5b6cb86d624f45e09d44 |


<!-- paired-coding:start -->
<details><summary>Archived paired coding evidence · 2026-10-24</summary>

Reference: [R471](experiments/R471.md). All 164 exact HumanEval+ task identities and the registered official scorer are shared. These are whole-profile observed overlaps, not a second ranking or a new benchmark.

| Profile | Experiment | Configuration | Both pass | Candidate only | Reference only | Neither passes |
| --- | --- | --- | --- | --- | --- | --- |
| LFM2.5 8B A1B | [R452](experiments/R452.md) | [Exact profile](configuration-profiles/cfg-bf94708017e31716c460eed85be81ce58b6a502ac82268cb793930118de990ae.md) | 106 | 10 | 26 | 22 |
| MiMo V2.6 Distill Qwen 9B | [R454](experiments/R454.md) | [Exact profile](configuration-profiles/cfg-6fee55e4cd29ef463b21160ec81c870ad503865bd3fa368fefb0b64d6c8b830e.md) | 110 | 9 | 22 | 23 |
| Gemma4 12B IT QAT | [R464](experiments/R464.md) | [Exact profile](configuration-profiles/cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625.md) | 131 | 25 | 1 | 7 |
| Qwen3.5 9B | [R465](experiments/R465.md) | [Exact profile](configuration-profiles/cfg-9fcb6193898540f39890fcfb16525895409d6b08f8de5165231fcbc0c17d2653.md) | 124 | 11 | 8 | 21 |
| Qwen3.8 27B | [R466](experiments/R466.md) | [Exact profile](configuration-profiles/cfg-1bc9cefba6ba7b1aed15ea85f4d7bd445c08f43fd9328a4f727dbd9276051cb0.md) | 129 | 20 | 3 | 12 |
| Nexus 9B CodeCore Merge | [R488](experiments/R488.md) | [Exact profile](configuration-profiles/cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba.md) | 122 | 8 | 10 | 24 |
| OmniCoder Opus Distill 9B | [R490](experiments/R490.md) | [Exact profile](configuration-profiles/cfg-f13e4e7609cb14c796219e155df1c036e56bbc0457fc2fb9295ee5c6c6442770.md) | 121 | 10 | 11 | 22 |
| Slopus 9B | [R493](experiments/R493.md) | [Exact profile](configuration-profiles/cfg-c55eca0a22e298680cf6a73c62c0f7732aaa8ee23ab8d2f0682fda8a312d3db7.md) | 119 | 7 | 13 | 25 |


[Public aggregate-replay data](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json): the `paired_coding_reviews` records contain only the official task IDs and pass/fail booleans needed to reproduce these counts. No model responses or solutions.

Descriptive task overlap of whole configurations; no causal model-training, significance, unseen-task or router-performance claim. Admission annotations are not independent repetitions. No new inference, official result or Champion qualification. Public official task IDs and pass/fail booleans support aggregate replay. Model responses, solutions and private inputs are withheld.

[audit-6ac57713d46c60a692ce](audits/audit-6ac57713d46c60a692ce.md) · [Frozen public input](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/c7b76a53dba1cedbbff3b1f22422286fdfcc60a4/data/configuration-history.json)

</details>
<!-- paired-coding:end -->

## Jarvis qualification

Screening is complete. This is a provisional shortlist, **not a new ranking**. [Existing complete benchmark results](configuration-comparison.md) remain unchanged.

- **OmniCoder-9B · canonical Q6_K**: [R471](experiments/R471.md), [R478](experiments/R478.md). Official agent qualification: NOT MEASURED.
- **OmniCoder-9B · bartowski Q6_K**: [R516](experiments/R516.md), [R517](experiments/R517.md). Official agent qualification: NOT MEASURED.
- **Nexus-9B · OFF/T0**: [R488](experiments/R488.md), [R489](experiments/R489.md). Official agent qualification: NOT MEASURED.
- **Ornith-1.5-9B · OFF/T0**: [R495](experiments/R495.md), [R496](experiments/R496.md). Official agent qualification: NOT MEASURED.
- **Qwen3.8-27B**: [R466](experiments/R466.md), [R473](experiments/R473.md); incomplete evidence remains PARTIAL. Official agent qualification: NOT MEASURED.
- **Gemma4-12B**: [R464](experiments/R464.md), [R472](experiments/R472.md). Official agent qualification: NOT MEASURED.
- **Qwen3.5-9B · efficiency reference**: [R465](experiments/R465.md), [R474](experiments/R474.md). Official agent qualification: NOT MEASURED.

### Frozen agent validation

33 frozen cases / 11 related-task groups; all tools simulated. Native profiles may differ. This is separate validation evidence, **not Terminal-Bench or an official Agents score**.

| Profile | Success | Task time | Completion tok/s¹ | GPU J/success² | Peak VRAM MiB | Evidence |
|---|---:|---:|---:|---:|---:|---|
| OmniCoder-9B | 26/33 | 447.17s | 59.18 | 4747.50–4755.14 | 7356.50 | [R530](experiments/R530.md) |
| Nexus-9B · OFF/T0 | 25/33 | 319.98s | 51.70 | 3486.51–3489.47 | 7356.50 | [R531](experiments/R531.md) |
| Ornith-1.5-9B · OFF/T0 | 18/33 | 328.88s | 48.65 | 4982.84–4994.09 | 7356.50 | [R532](experiments/R532.md) |
| Qwen3.8-27B | 26/33 | 759.43s | 15.88 | 7992.09–7996.41 | 12454.50 | [R533](experiments/R533.md) |
| Gemma4-12B · ctx16K | 17/33 | 444.22s | 32.40 | 6281.06–6285.84 | 8254.50 | [R534](experiments/R534.md) |

¹ Includes reasoning where reported; not pure decode. ² Counter-bracketed GPU energy. One pass over11 authored families does not establish population superiority. Private fixtures/oracles are not exported.

Evaluator correction: replay preserves the exact captured fixture mapping order after checking equality with the frozen archive. Original replies and scoring rules are unchanged; no additional GPU run. [Correction evidence](audits/audit-32864b8cd9dbed81059c.md).

**Terminal-Bench 2.1:** 89 tasks verified at revision `7131e4375048a0e408a8fb404b5f499d726b695b`; Harbor 0.24.0 source inspected. [Official dataset](https://hub.harborframework.com/datasets/terminal-bench/terminal-bench-2-1). No local official score; isolated container/evaluator/broker execution remains unadmitted.

**Gemma context:** [R528](experiments/R528.md) failed during startup, before any task. The bridge fix passed 21 direct transport controls. This is not a negative model-quality result.

Corrected GPU run [R529](experiments/R529.md): 18 cases completed, 0 context-preflight errors and 0 request errors; 9/18 solved versus 9/18 at8K. Task time changed by +7.62%, peak VRAM by +136MiB. Technical fix confirmed; no task-success gain or Champion claim.

The corrected run made 125 model requests versus 119 before. The task-time difference includes those additional turns; it is not an isolated decode-speed comparison.

**Slopus diagnosis:** [R524](experiments/R524.md) recorded 10 rejected simulated policy proposals and 1 length-stopped response. Complete coding/tools results remain valid; no global model exclusion.

**Orchestration:** Single-Agent, Planner + Worker, and Planner + Worker + Reviewer are planned with one shared 1200s task allowance (400s per arm), identical model/tasks and one GPU job. Recovery/delegation controls remain pending; no orchestration result is claimed. Keep deterministic permissions outside all model roles.

Next: source-admit the existing runner for the reserved validation, finish context/wrapper diagnostics, then select optimization candidates. Other models and all negative results remain in the archive.

## Independent native-profile validation

Frozen8coding+8mock-tool reserved tasks, no parameter tuning. Tasks were already exposed on the original three profiles; additional fixed-profile measurements are not a globally unseen holdout. Small descriptive validation, not an official benchmark or model-superiority proof.

| Profile | Coding /8 | Mock tools /8 | Evidence |
|---|---|---|---|
| Qwen3.5-9B | 8/8 | 6/8 | [R509](experiments/R509.md) · [Exact inference profile](configuration-profiles/cfg-aae586a5fa23e08f528cfec90a0d3e1817a681b815a4b5329c4326467b848a55.md) |
| Gemma4-12B | 7/8 | 7/8 | [R510](experiments/R510.md) · [Exact inference profile](configuration-profiles/cfg-aebfa2c88282523db04a6e6e6b802fcb8eb8912f4c2715d30c53e52ed40096e7.md) |
| OmniCoder-9B | 8/8 | 6/8 | [R511](experiments/R511.md) · [Exact inference profile](configuration-profiles/cfg-21e92fd73d60a2aea4381051b00148063e4e562f95a71a0c1c558ea7b511cb1a.md) |
| Nexus-9B · OFF/T0 | 6/8 | 5/8 | [R526](experiments/R526.md) · [Exact inference profile](configuration-profiles/cfg-694b972dbae1a38c201067e11a2e410c6a002052b4f225c2ac9c158445b1ef9b.md) |
| Ornith-1.5-9B · OFF/T0 | 7/8 | 5/8 | [R527](experiments/R527.md) · [Exact inference profile](configuration-profiles/cfg-13b1445d3933a9d3782b6fa406707d0326ae263338b8c3a82f51c4e33656967c.md) |

Full official coding/tools qualifications were reused. No original benchmark score changed.

Original three-profile cohort: all three profiles proposed a simulated tool call despite explicit denial in one frozen case. No tool was executed. Qwen3.5 and OmniCoder also refused an unsupported request without the required status JSON; Gemma failed one coding task. These are profile-specific observations, not population safety rates. Keep permission enforcement outside model responses.

Additional fixed-profile validation: Retain Nexus and Ornith alongside existing references. Existing complete coding/tool qualifications remain valid; these additional fixed-profile responses do not establish superiority or warrant small-sample exclusion. Both proposed simulated tools in denial/version-conflict cases and failed required final-status formatting in the unsupported case. Enforce permissions/version checks outside model responses. No productive tool executed. No parameter tuning on these responses or new Champion.

## Native Agent18 development evidence

Previously used frozen simulated coding, automation and read workflows. **Not Terminal-Bench, unseen validation, a production safety certificate or a Champion qualification.** Native model profiles are preserved; the required/single-tool-call envelope is explicit.

| Experiment | Native model profile | Solved / completed | Task phase s | GPU J/success bounds | Peak VRAM MiB | Preflight / HTTP failures |
|---|---|---|---|---|---|---|
| [R518](experiments/R518.md) | OmniCoder-9B | 13/18 | 258.25 | 5447.82–5455.78 | 7356.50 | 0 / 0 |
| [R519](experiments/R519.md) | Qwen3.5-9B | 8/18 | 214.93 | 7042.30–7051.75 | 5956.50 | 0 / 0 |
| [R520](experiments/R520.md) | Gemma4-12B | 9/18 | 300.07 | 8036.58–8047.35 | 8118.50 | 2 / 0 |
| [R521](experiments/R521.md) | Qwen3.8-27B | 14/18 | 476.02 | 9276.77–9283.12 | 12454.50 | 0 / 0 |
| [R522](experiments/R522.md) | Nexus-9B · OFF/T0 | 14/18 | 258.38 | 5011.18–5015.32 | 7356.50 | 0 / 0 |
| [R523](experiments/R523.md) | Opus Distill-9B · OFF/T0 | 12/18 | 185.37 | 4166.33–4173.76 | 7356.50 | 0 / 0 |
| [R524](experiments/R524.md) | Slopus-9B · OFF/T0 | 4/18 | 241.39 | 16556.26–16573.40 | 7356.50 | 0 / 0 |
| [R525](experiments/R525.md) | Ornith-1.5-9B · OFF/T0 | 14/18 | 200.71 | 3896.18–3903.78 | 7356.50 | 0 / 0 |
| [R529](experiments/R529.md) | Gemma4-12B · ctx16K bridge-v2 | 9/18 | 322.93 | 8625.59–8637.81 | 8254.50 | 0 / 0 |

The 18 tasks share 10 original generalization groups. [Group-aware sensitivity review](experiments/R525.md) preserves the original case-wise statistics and independently verifies group-level sign flips. All p-values are exploratory and unadjusted across model comparisons; no population-superiority or independent-task claim follows.


Quality is independently replayed from the actual retained replies in a non-root CPU jail using the original simulator and oracle. No productive tools execute. Technical context/transport failures remain separate in the linked audit; incomplete captures remain partial. Energy covers the measured case window, including failed tasks and setup between cases, excluding load/warmup and CPU/system energy. Nonstream output-token rate is not pure decode speed or TTFT. No scores are added to the official model table or its mean.

Admission retains the trusted broker, immutable source/execution review, exact asset hashes, one GPU lease and all power, VRAM, temperature, ECC and throttling guards. A source hash alone grants no trust. The development runner and independent CPU replay were checked with original simulator controls before actual inference.
