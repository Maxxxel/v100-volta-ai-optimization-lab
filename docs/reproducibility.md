# Reproducibility and variability

These are archived, hash-verified observations; no new GPU execution. Fixed seeds do not establish deterministic results.

## Seed propagation and sampler behavior

| Profile | Audit | Configured seed | Request → server seed match | Temperature | Requests | Greedy-path condition | Same-prompt A/A evidence |
|---|---|---|---|---|---|---|---|
| Nexus | [R531](experiments/R531.md) | 1001 | 153/153 request → server | 0.0 | 153 | 153 | R621 · 4 exposed requests; [R631](#same-profile-aa-repeatability-r531-r631) · 153/153 turns and 33/33 tasks |
| OmniCoder | [R536](experiments/R536.md) | 1001 | 154/154 request → server | 0 | 154 | 154 | R620 · 1 exposed request; [R630](#same-profile-aa-repeatability-r536-r630) · 154/154 turns and 33/33 exposed tasks |
| Gemma 4 | [R534](experiments/R534.md) | 1001 | 177/177 request → server | 1.0 | 177 | 0 | R622/R627 · 3 exposed requests each; [R633](#same-profile-aa-repeatability-r534-r633) · 177/177 turns and 33/33 tasks |
| Qwen3.8 MTP | [R550](experiments/R550.md) | 1001 | 150/150 request → server | 0 | 150 | 150 | R623/R626 · 3 exposed requests each |
| Qwen3.5-9B | [R535](experiments/R535.md) | 1001 | 162/162 request → server | 0.0 | 162 | 162 | Task A/A NOT MEASURED · 162 unique prompts; synthetic warm-up text repeated in 4 runs |

For every listed profile, each archived request seed matches the server-reported generation setting; request count and seed histogram are checked against raw captures. The pinned schema starts from server defaults and applies request fields, then the server initializes a sampler for each task. A `n > 1` request creates child tasks with offset seeds. This verifies configured-seed propagation and source-level reset behavior, not hidden RNG state.

R614/R616 each meet the pinned greedy-selection condition on all requests: temperature 0, `n_probs=0`, backend sampling off, temperature as the final sampler, and zero dynamic-temperature range. Their observed token divergence is therefore not explained by the sampler RNG seed alone; differing logits or another runtime/state path remain possible. This does not prove deterministic GPU computation or identify cache causality. Gemma at temperature 1 remains stochastic even with a fixed per-request seed.

Qwen3.5-9B R535 confirms seed propagation in 162/162 task requests, but all 162 task prompts are unique. **Task-level baseline A/A remains NOT MEASURED.** A separate archive cross-check found two identical synthetic warm-up requests in four distinct GPU experiments (R501/R509/R519/R535); both returned identical output-text hashes each time. The model SHA, llama.cpp runtime asset hashes, launch arguments, template and warm-up settings match. This is limited warm-up text-repeatability evidence, not task-quality evidence: token IDs and logits were not captured; the 128-token output is capped by its warm-up request. Audit/profile hashes: `r501 9e9b0f0375c9, r509 c32f1defdd71, r519 2256e0b376af, r535 d3b5588718f9`.

Pinned source: [request seed field](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-schema.cpp#L175), [per-task sampler initialization](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L1925), [greedy sampler selection](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/common/sampling.cpp#L403), [temperature-zero argmax](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/src/llama-sampler.cpp#L265), [multi-choice seed offsets](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-task.h#L287). Source hashes: `common/sampling.cpp b6a1f963fd75, tools/server/server-context.cpp 6b5fdf2b2460, tools/server/server-schema.cpp 1f9d7b73b436`.

## Token-probability diagnostic feasibility

R616 archived 156 non-stream requests with tools; none requested logprobs. The pinned API accepts this combination because its restriction is limited to `tools + stream`. It can return up to 20 top-token probabilities/logprobs per generated token—not a full raw-logit vector or internal state. Captures did not enable this instrumentation. A future measurement needs a separate reviewed broker profile and identical instrumentation in both cache arms; R616 remains untouched and no GPU run was made.

**Instrumentation changes the sampler chain:** Requesting probabilities disables the n_probs==0 greedy fast-path and selects the distribution sampler in this pinned build; temperature zero remains in the chain. Identical output versus the original uninstrumented profile is not established. Compare the instrumented profile separately with its uninstrumented reference before attributing differences to caching. Pinned [sampler source](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/common/sampling.cpp#L403), SHA-256 `b6a1f963fd75fd17d12bafb59351a1009d2358dd789dba7ed10943340f8e5553`.

Pinned [request parser and stream guard](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-common.cpp#L1455). Source SHA-256: `c4d53b4c72ca825434a035a4b632c8bc71e709d22fe33ca149fde95cee8460a1`.

## Historical matched requests

| Profile | No cache / cache | Matching requests | Different input token sequences | Identical output sequences | Different output sequences |
|---|---|---|---|---|---|
| Nexus | [R531](experiments/R531.md) / [R614](experiments/R614.md) | 153 | 0 | 124 | 29 |
| OmniCoder | [R536](experiments/R536.md) / [R616](experiments/R616.md) | 145 | 0 | 111 | 34 |
| Gemma 4 | [R534](experiments/R534.md) / [R617](experiments/R617.md) | 164 | 0 | 134 | 30 |

The requests match except for the cache flag and use the same input token IDs. Each pair comes from different sessions; results do not isolate cache causality. Outputs are correlated, and these are not independent task-quality samples. Logits and internal RNG state are **NOT MEASURED**. The failed policy gates remain in force. See [R615](experiments/R615.md) for the limited Nexus in-session ABBA diagnostic and its historical baseline divergence.

Source review SHA-256: `319375870744b2c6a3d35ab109e8ad3ba2e81b1af0b60ca444a665c7be5943b0`. Pinned source commit: `097cf33d9499b1eade67d51e16d7c75427e7b267`.

## Timing with identical input and output tokens

| Profile | Matched requests | Output tokens each | Prefill seconds off / on | Decode seconds off / on | Cached input tokens on |
|---|---|---|---|---|---|
| Nexus | 124 | 8726 | 86.6 / 34.2 | 110.4 / 110.0 | 159514 |
| OmniCoder | 111 | 7037 | 76.3 / 31.3 | 89.7 / 89.6 | 138159 |
| Gemma 4 | 134 | 5658 | 169.6 / 80.8 | 79.8 / 79.6 | 176680 |

Historical server timings, not kernel counters or a balanced causal experiment. Input/output-identical subsets are selected retrospectively; they do not establish task quality, safety or a universal speedup.

## Paired agent task outcomes · prefix-cache profiles

| Historical profile | Task successes · 33 paired | Policy-gate passes | Observed task wall time | Completion tokens | GPU energy bounds | Decision |
|---|---|---|---|---|---|---|
| [Nexus · R531 → R614](experiments/R614.md) | 25 both · +0 / −0 | 29 → 28 / 33 | 320.0 → 255.4 s | 16,392 → 16,777 | 87,163–87,237 → 69,685–69,786 J | CAUSE UNCONFIRMED · NOT QUALIFIED |
| [OmniCoder · R536 → R616](experiments/R616.md) | 27 both · +0 / −1 | 29 → 28 / 33 | 401.7 → 328.4 s | 22,528 → 22,309 | 109,462–109,573 → 89,456–89,571 J | CAUSE UNCONFIRMED · NOT QUALIFIED |

Same 33 exposed tasks (11 related families), one response per arm; exact paired McNemar p=1.0 in both pairs. This tiny test does not establish equivalence or noninferiority. Subsequent baseline A/A pairs [R536/R630](#same-profile-aa-repeatability-r536-r630) and [R531/R631](#same-profile-aa-repeatability-r531-r631) each matched all 33 task outcomes; one pair per profile cannot estimate general variability. Nexus gained no task successes and emitted more tokens; OmniCoder lost one task success while emitting 0.97% fewer tokens, too little to explain the observed wall-time change by itself. Both candidates lost one policy-gate pass. Cache-associated output divergence is separately documented; task-level causality remains unconfirmed. These historical whole-task profiles are not independent repeats.

## Gemma prefix-cache A/A and A/B pilot

| Fixed request | No-cache A/A across sessions | Cache-on variants different | Cache hits | First difference, zero-based |
|---|---|---|---|---|
| 1 | YES | 0 | 2 | NONE |
| 2 | YES | 0 | 4 | NONE |
| 3 | YES | 0 | 4 | NONE |
| 4 | YES | 4 | 4 | 7 |

[R624](experiments/R624.md) tests four exposed requests from the R617 policy-loss case. Cache-hit token divergence was reproduced on the fourth request with a stable no-cache baseline. Whole-task causality, internal state and general equivalence remain unproven; the R617 failed safety gate remains in force.

## Qwen3.8 MTP: paired agent outcomes

| Profile | Success | Policy pass | Task time | GPU energy bounds | Peak VRAM | Completion tokens |
|---|---|---|---|---|---|---|
| MTP off · R625 | 27/33 | 31/33 | 761.5 s | 208758–208860 J | 12454 MiB | 12069 |
| MTP on · R618 | 27/33 | 31/33 | 625.0 s | 162025–162133 J | 13602 MiB | 12110 |

[R625](experiments/R625.md): 8/150 matched request/input-token pairs generated different output sequences. These are previously exposed tasks in separate sessions, not a balanced causal comparison or an independent holdout. Two policy cases fail in both profiles; equal observed counts do not establish quality or safety equivalence. No new champion is qualified.

| Identical-input/output subset | Prompt tokens | Generated tokens | Prefill off / on | Decode off / on | Request E2E off / on | Draft accepted |
|---|---|---|---|---|---|---|
| 142 | 251890 | 10508 | 387.7 / 426.0 s | 299.9 / 143.9 s | 689.2 / 571.6 s | 7526/8604 |

Retrospectively selected matched outputs; separate sessions. Server timings do not establish a causal kernel speedup. Subset energy is NOT MEASURED.

Safety review: both profiles attempted denied simulated climate changes in the same 2 cases; 10/10 matching requests had identical output tokens. External authorization rejected the calls; no production tools were connected. This is one correlated task family and cannot establish general safety equivalence.

## Qwen3.8 integrated MTP A/A pilot

| Fixed request | Within-session repeats equal | Across-session equal |
|---|---|---|
| 1 | YES | YES |
| 2 | YES | YES |
| 3 | YES | YES |

[R623](experiments/R623.md) used three short, previously exposed tool requests with seed 1001 and integrated MTP in two sessions. This restricted A/A observation does not prove general determinism, task quality, safety or a causal MTP improvement.

## Qwen3.8 MTP-off A/A and historical ON comparison

| Fixed request | MTP-off across sessions | MTP-on across sessions | Same output ON/OFF |
|---|---|---|---|
| 1 | YES | YES | 8/8 |
| 2 | YES | YES | 8/8 |
| 3 | YES | YES | 8/8 |

[R626](experiments/R626.md) reused three exposed requests over two fresh MTP-off sessions. R623 ON and R626 OFF are separate jobs; identical outputs in this small correlated sample do not establish general determinism, losslessness, task quality or safety equivalence.

## Gemma Q8 value-cache coding forensics

[R608](experiments/R608.md) and its historical F16 control had 164 matching request/input-token pairs. 58 outputs matched; 106 diverged. All 9 observed losses had different output tokens; first divergences occurred at zero-based positions 0, 0, 1, 24, 136, 143, 176, 194, 350. Temperature 1 and seed 1001 were preserved. Separate sessions cannot establish whether Q8 caused these changes; the quality gate remains failed and a fresh A/A–A/B diagnosis is needed.

## Gemma F16/Q8 value-cache repeatability diagnostic

| Exposed request | F16 A/A repeats | Q8 A/A repeats | F16 vs Q8 output | First divergence |
|---|---|---|---|---|
| 1 | IDENTICAL | IDENTICAL | DIFFERENT | token 0 |
| 2 | IDENTICAL | IDENTICAL | DIFFERENT | token 0 |
| 3 | IDENTICAL | IDENTICAL | IDENTICAL | none |

[R627](experiments/R627.md) captured 24 requests across four ABBA sessions (seed 1001, temperature 1.0; 169.3 s task phase, 8118 MiB peak VRAM). The whole-task GPU energy-counter bound was 36.90–36.93 kJ; per-success energy cannot be calculated because task success was not scored. F16 and Q8 each repeated token-identically across both sessions on all three exposed requests; their outputs differed at token zero on two requests and matched on one. This is repeatable output divergence associated with the cache setting in this small diagnostic, not a quality or safety regression finding. Logits were not measured; no promotion.

Post-hoc CPU EvalPlus replay of three exposed requests (not leaderboard data):

| Task | F16 base / plus | Q8 base / plus |
|---|---|---|
| HumanEval/54 | pass · 7/7 / pass · 999/999 | fail · 0/7 / fail · 0/999 |
| HumanEval/95 | fail · 0/14 / fail · 0/510 | fail · 4/14 / fail · 4/510 |
| HumanEval/0 | pass · 7/7 / pass · 999/999 | pass · 7/7 / pass · 999/999 |

HumanEval/54 reproduced the historical F16-pass/Q8-fail pair; HumanEval/95 failed in both fresh arms although the historical R608 control passed that task. The latter demonstrates run-to-run baseline variation in this targeted sample. These previously exposed cases do not establish a general causal quality effect or qualify Q8; R608 remains unqualified.

## Gemma fixed and distinct seed pilot

| Fixed request | Seed | Within-session repeat equal | Across-session equal | Distinct outputs across seeds |
|---|---|---|---|---|
| 1 | 1001 | YES | YES | 1 |
| 1 | 1002 | YES | YES | 1 |
| 1 | 1003 | YES | YES | 1 |
| 2 | 1001 | YES | YES | 1 |
| 2 | 1002 | YES | YES | 1 |
| 2 | 1003 | YES | YES | 1 |
| 3 | 1001 | YES | YES | 1 |
| 3 | 1002 | YES | YES | 1 |
| 3 | 1003 | YES | YES | 1 |

[R622](experiments/R622.md) tested three short, constrained and previously exposed tool requests, using three seeds twice per session across two sessions. Identical outputs in this small sample do not establish general determinism or quality/safety equivalence. The R617 failed policy gate remains in force.

## Nexus two-session pilot

| Fixed request | No-cache A/A across sessions | Cache-on variants different | Cache hits | First difference, zero-based |
|---|---|---|---|---|
| 1 | YES | 2 | 2 | 6 |
| 2 | YES | 0 | 4 | NONE |
| 3 | YES | 0 | 4 | NONE |
| 4 | YES | 4 | 4 | 0 |

[R621](experiments/R621.md) verifies actual input token IDs across two adjacent sessions. The fourth request diverged at output token zero in all four cache-hit trials; two other requests matched and the first differed only when cache hits occurred. This does not establish whole-task safety causation or an implementation-level cause. The R614 failed safety gate remains in force.

## OmniCoder two-session pilot

| Fixed request | No-cache A/A across sessions | Cache-on differs from baseline | Cache-on distinct outputs / lengths | Cache hits | First difference, zero-based |
|---|---|---|---|---|---|
| 1 | YES | 0 | NOT MEASURED | 2 | same |
| 2 | YES | 0 | NOT MEASURED | 4 | same |
| 3 | YES | 4 | 4 repeats / 2 sequences; 164/166/166/164 tokens | 4 | 0 |

[R620](experiments/R620.md) used identical input token IDs and wire order in two adjacent model sessions. On the exact R616 divergent request, no-cache A/A outputs matched in 4/4 trials (558 tokens); cache-on outputs produced two distinct sequences in 4/4 trials (164/166 tokens), each differing at output token 0 after 1,675 reported cache tokens. **BASELINE_VARIABILITY_NOT_OBSERVED; CANDIDATE_VARIABILITY_OBSERVED** for this single exposed request. This narrows the repeatability concern but does not establish whole-task or policy causality, or an internal kernel/state cause. The pinned llama.cpp server-context reuses common prompt prefixes and may use a different prompt-processing batch path. The [R619](experiments/R619.md) preflight failure from reordered JSON keys remains preserved.

## Cache and recurrent-state source-path review

CPU-only inspection of the pinned source and hash-verified server logs; no model requests or GPU runs.

| Run | Requests with cache_prompt=true | Checkpoint restores logged | Full-prompt fallbacks logged | Partial removal unsupported | Host RAM cache disabled |
|---|---|---|---|---|---|
| [R614](experiments/R614.md) | 155 | 57 | 32 | 1 | 1 |
| [R616](experiments/R616.md) | 156 | 40 | 33 | 1 | 1 |

The pinned [`server-context.cpp` source](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp) reuses a matching prefix and stores target, draft and speculative state in context checkpoints. It explicitly notes recurrent state cannot be rewound from the final state alone (source SHA-256 `6b5fdf2b246017b074c239e8f0b93f9d6952b4715501269627fec7a11b00bab7`). If a usable checkpoint is unavailable, it falls back to full prompt re-processing.

| Code path | Pinned source |
|---|---|
| Common-prefix match | [line 3600](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3600) |
| Prefix chunk reuse | [line 3653](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3653) |
| Target state checkpoint | [line 2584](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L2584) |
| Draft state checkpoint | [line 2585](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L2585) |
| Speculative state checkpoint | [line 2587](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L2587) |
| Recurrent-state rewind limitation | [line 2596](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L2596) |
| Target checkpoint restore | [line 3760](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3760) |
| Draft checkpoint restore | [line 3761](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3761) |
| FULL-only checkpoint path | [line 3360](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3360) |
| pos_min == -1 guard | [line 3692](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3692) |
| Full-prompt fallback | [line 3781](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/tools/server/server-context.cpp#L3781) |
| PARTIAL_ONLY attention guard | [hybrid.cpp line 191](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/src/llama-memory-hybrid.cpp#L191) |
| Recurrent checkpoint write after guard | [hybrid.cpp line 194](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/src/llama-memory-hybrid.cpp#L194) |
| Recurrent checkpoint restore after guard | [hybrid.cpp line 205](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/src/llama-memory-hybrid.cpp#L205) |
| Recurrent tensor-state serialization | [recurrent.cpp line 866](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/src/llama-memory-recurrent.cpp#L866) |
| Default chunk-shift threshold | [common.h line 634](https://github.com/ggml-org/llama.cpp/blob/097cf33d9499b1eade67d51e16d7c75427e7b267/common/common.h#L634) |

Pinned source hashes: `llama-memory-hybrid.cpp` `907b769206d9b29b8ee2dd0f04ead29e99810843edaecb722ddbbac852d0bf1e`; `llama-memory-recurrent.cpp` `51172be188d0eece2267c9105dc5a8d2c3ef7ebd58e88a6f562ac6ee36326f98`. In this build, `PARTIAL_ONLY` omits attention-memory state but still writes and restores the recurrent state, including cell/tensor data. **A missing GDN/recurrent checkpoint is not supported as the explanation by this code path.** The source TODO about checkpoint position coverage is specifically for SWA; R614/R616 both logged `n_swa=0`. The mapped divergent R616 request had neither checkpoint restore nor full-prompt fallback, so that TODO does not explain this request. This narrows hypotheses; it does not establish actual runtime-state equality or explain the first-token divergence. Logits and recurrent tensors were not captured.

For the divergent R616 request, `cache_prompt=true`, the recorded launch omitted `--cache-reuse`, and the pinned default `n_cache_reuse=0` disables the separate chunk-shift branch (common-header SHA-256 `2a2d084f28932b04ca0a26687bd4c4744bd68e504956d50f8f5719cbbecca4cd`). Together with the request-level logs showing no checkpoint restore or full-prompt fallback, this narrows the observed path to ordinary same-slot common-prefix continuation. Chunk shifting and checkpoint rollback are unsupported explanations for this request; the first-token divergence itself remains unexplained. The full-prompt and suffix-only processing paths may differ numerically, but logits and recurrent-state snapshots were not captured. This remains source-path evidence, not a local state-correctness qualification.

The upstream [issue #22940](https://github.com/ggml-org/llama.cpp/issues/22940) claims FULL-only memory permanently disables prompt-cache restore when `pos_min == -1`; it was closed as not planned. That blanket claim is **not established for our pinned build**: source has a FULL-only checkpoint path and an explicit `pos_min == -1` abort guard, while R614/R616 logs record 57/40 checkpoint restores. This does not map restore/fallback events to the divergent requests or explain their token differences.

### R614 policy-loss case · exact request repeated in R621

| Evidence | Observed result |
|---|---|
| Paired task outcome | One policy-gate loss; task success unchanged (failed in both). Policy passes: 1 → 0; rejected calls: 0 → 1. |
| Matched request | Turn 4; 1785 input tokens; exact token IDs and request fields match except `cache_prompt`; seed 1001, temperature 0, output limit 4096. |
| R621 no-cache A/A | 4/4 generated sequences matched the R531 baseline exactly (368 tokens; cache_n=0). |
| R621 cache-hit repeats | 4/4 generated sequences matched R614 exactly (65 tokens; cache_n=1711). |
| Earliest difference | Generated token 0. Two sessions; four repetitions per cache condition. |
| Server execution path | Exact input/completion-token alignment: 153/153 baseline and 155/155 candidate turns. Matched turn: initial reusable context 0 vs 1711; server evaluated 1785/1785 vs 74/1785 input tokens. Checkpoint restore/reprocess fallback logged: False/False baseline; False/False candidate. |
| Disposition | REPRODUCIBLE_CACHE_ASSOCIATED_DIVERGENCE; ONE_POLICY_LOSS_OBSERVED; WHOLE_TASK_CAUSALITY_NOT_ESTABLISHED |

Server task records align one-to-one with every captured agent request by exact input and completion token counts. For the matched request, baseline began with no reusable context and evaluated all 1,785 input tokens; candidate began with 1,711 reusable prefix tokens and evaluated 74. Neither selected server task logged checkpoint restore or full-prompt fallback. This confirms the common-prefix compute path for this request, not why its first generated token changed or whether caching caused the complete-task policy outcome. The R614 case trace records one additional policy-rejected call in the same case; all actions were simulated and no production tool was connected. The balanced R621 prompt replay reproduces the cache-associated output path, but it does not rerun the complete agent or policy evaluator. This localizes the observed policy loss; it does not prove the exact response-to-policy causal link or an internal numerical/state mechanism. R614 remains **NOT QUALIFIED**. [R531](experiments/R531.md) · [R614](experiments/R614.md) · [R621](experiments/R621.md).

### R616 lost-task first-divergence mapping

A CPU-only pairing of retained R536/R616 request captures maps the sole case that passed in R536 and failed in R616. Model SHA, runtime, template, server arguments and environment match; request options differ only in `cache_prompt`. Task ID and prompt content remain private.

| Turn | Input tokens | Input IDs match | Outputs identical | Cache tokens · baseline / candidate | Output tokens · baseline / candidate | First changed output token |
|---|---|---|---|---|---|---|
| 1 | 1505 | YES | YES | 0 / 0 | 39 / 39 | NONE |
| 2 | 1637 | YES | YES | 0 / 1543 | 39 / 39 | NONE |
| 3 | 1790 | YES | NO | 0 / 1675 | 558 / 166 | 0 |


Server-task alignment: 154/154 baseline and 156/156 candidate turns match captured input/completion token counts. On the divergent third turn, initial reusable context was 0 vs 1675 tokens; server input evaluation was 1790/1790 vs 115/1790. Checkpoint restore/reprocess fallback logged: False/False baseline; False/False candidate. Server task logs align one-to-one with every captured scored request by exact input and completion token counts. On the lost task’s divergent third turn, baseline began with no reusable context and evaluated all 1,790 input tokens; candidate began with 1,675 reusable prefix tokens and evaluated 115. Neither selected server task logged checkpoint restore or full-prompt fallback. This verifies the common-prefix compute path, not whole-task cache causality or an internal state/numerical mechanism.

On turn 3, the same 1,790-token prompt had a first-token difference: uncached baseline `cache_n=0`, candidate `cache_n=1675`. That response was shorter (166 vs558 tokens), but the candidate then used two additional model turns; total captured output for this case was 744 vs636 tokens. The task-time difference therefore cannot be explained as a simple decode-throughput gain. R620 supplies exact-prompt no-cache A/A repetition: 4/4 outputs matched; cache-on varied across two sequences in 4/4 trials. This confirms scoped candidate variability, not that caching caused the task/policy outcome or an internal numerical/state path.

The `host RAM cache disabled` log is distinct from request-level `cache_prompt=true`.

**Interpretation:** the R616 lost-task divergence is mapped to a cache-hit response, consistent with a cache/recompute numerical-path effect; corrupted GDN state is not established. Per-request server input evaluation is now mapped, but exact checkpoint restore/fallback attribution, logits, per-layer state and kernel traces remain unmeasured. The R614/R616 task-level policy causes remain **UNRESOLVED**, and neither candidate is qualified.

## Same-profile A/A repeatability · R536 / R630

R630 repeated the unchanged OmniCoder bartowski Q6 profile on the same exposed 33-task validation set. Independent CPU replay confirmed all task outcomes and effects. Prompt identities, requests and generated token sequences matched in **154/154** turns; task outcomes matched in **33/33**.

| Run | Solved | Policy gates | Task phase s | Whole-phase GPU energy bounds J | Gross GPU J / success bounds | Peak VRAM MiB |
|---|---|---|---|---|---|---|
| R536 | 28/33 | 29/33 | 401.663 | 109,461.5–109,572.7 | 3,909.3–3,913.3 | 7,680.5 |
| R630 | 28/33 | 29/33 | 401.311 | 109,447.6–109,549.6 | 3,908.8–3,912.5 | 7,680.5 |

The cumulative NVML counter is monotonic and brackets the full task phase; the per-case power integral remains incomplete because sample gaps exceed its 0.25 s validity limit. Counter ranges overlap. One A/A pair establishes neither a speed nor an energy winner. These are whole-phase GPU-board values, not CPU/system or isolated per-task energy. This is not an official benchmark, unseen holdout, or Champion qualification. Original prompts and task contents are not published.

Audit SHA-256: R536 `c43fcc568c66cf86604b715ef6d094774cbf13888890daad0fae27711173b391` · R630 `4e20c6da6fe47fbceba2a448ca4ee65e296a7c307bbf132a6b71f458bfbdd5b2`. Raw capture SHA-256: R536 `ac3b4ac10aba8d98b8b12d3b29c63b1add2ffc294a2f2383a84c683b4ba1daa5` · R630 `3a2fc8e6f74dfb6585a87e2b7edaf4260ad066027cc1e6b2c5cc811acffa2599`. Counter addendum SHA-256: `e9e20f6c79d05cbfc56b3a3ee89554345e18a45e797dbec53c338892ca966437`.

## Same-profile A/A repeatability · R531 / R631

R631 repeated the unchanged Nexus Q6_K, thinking-off, T=0 profile on the same exposed 33-task validation set as R531. Independent CPU replay reproduced all task outcomes and effects. Prompt-token sequences and generated-token sequences matched **153/153**; task outcomes matched **33/33**. This is one A/A pair, not a determinism proof or model qualification.

| Run | Solved | Policy gates | Task phase s | Prefill tok/s | Decode tok/s | Whole-phase GPU energy bounds J | GPU J / success bounds | Peak VRAM MiB | Per-case energy coverage |
|---|---|---|---|---|---|---|---|---|---|
| R531 | 25/33 | 29/33 | 319.983 | 2,532.1 | 78.90 | 87,162.7–87,236.7 | 3,486.5–3,489.5 | 7,356.5 | 16/33 |
| R631 | 25/33 | 29/33 | 320.860 | 2,523.6 | 78.76 | 87,524.8–87,631.7 | 3,501.0–3,505.3 | 7,356.5 | 0/33 |

Energy bounds come from the cumulative NVML GPU-board counter bracketing the task phase. R631 per-case energy is **NOT MEASURED (0/33)** because telemetry sampling gaps invalidated case-level integration. Aggregate task-phase energy is not CPU/system or per-task energy. Differences are descriptive; no performance winner or Champion change. The earlier R614/R621 cache-associated cause remains unresolved.

Audit SHA-256: R531 `fc856a19b65377ec96c861e97812ed84801a3a9bc908262a882a0fdf63b86e12` · R631 `35b5ccc8057f043b64f6dd1de2f77b40528c21a92e01aa740b89f35a7c2ca89a`. Raw capture SHA-256: R531 `982925508cc69aac82a82cf3ca92eec62fea24654a7537ee29caa116dfde244d` · R631 `962180aff5a406998cbe1cf9f8323e31b3b96abbc213592827f7a87c529da831`. CPU replay receipt SHA-256: `a6da916e5a94b6b3ceaac677b212358ea5aecc4ad0a252698ecc6f2db8225940`.

## Same-profile A/A repeatability · R534 / R633

R633 repeated the Gemma 4 QAT profile at temperature 1.0 and seed 1001 on the same exposed 33-case internal validation set. Independent isolated CPU replay reproduced all 33 case scores and effects. All 177 request bodies, input-token sequences and generated-token sequences matched; task and policy outcomes matched in all 33 cases.

| Run | Solved | Policy gates | Case window s | GPU energy bounds J | GPU J / success bounds | Peak VRAM MiB | Per-case energy coverage |
|---|---|---|---|---|---|---|---|
| R534 | 17/33 | 29/33 | 444.220 | 106,777.9–106,859.2 | 6,281.1–6,285.8 | 8,254.5 | 1/33 |
| R633 | 17/33 | 29/33 | 445.573 | 106,883.1–106,995.5 | 6,287.2–6,293.9 | 8,254.5 | 0/33 |

Energy bounds are cumulative GPU-board counter brackets from the first case start to the last case end, including time between cases; startup and CPU/system energy are excluded. Per-case energy coverage is incomplete. A single pair of exposed correlated cases establishes neither general determinism nor quality equivalence and does not qualify a Champion. The cache candidate remains unqualified.

Audit SHA-256: R534 `38904a4aac691bd22747808c81e38ab9030c893a17723b073bacab29acdd9038` · R633 `e8d9b89292bd433016bcba571492b072ccf09c2800f50f9c426c1486cdee6ebb`. [Aggregate results and hashes](assets/r633-aa.json).

## Distinct-seed pilot · R634

Three previously exposed Gemma requests were selected for longer baseline outputs. Seeds 1001, 1002 and 1003 each ran twice in each of two sessions; the frozen input token IDs matched. Fixed-seed repetitions were identical, while every cross-seed pair differed. Positions below are zero-based output-token indices.

| Request | Fixed-seed repeats | Seed 1001 matches R633 | 1001 vs 1002 | 1001 vs 1003 | 1002 vs 1003 |
|---|---|---|---|---|---|
| 1 | 4/4 per seed | yes | 66 | 66 | 67 |
| 2 | 4/4 per seed | yes | 64 | 64 | 66 |
| 3 | 4/4 per seed | yes | 68 | 102 | 68 |

The 36 requests took 151.925 s including two starts and warmups; peak VRAM was 8,254.5 MiB. The GPU counter bounded the request window at 33,934.4–34,054.4 J, excluding system energy. These selected prompts are not a representative task-quality or safety test; no tools were executed and no Champion was qualified.

Audit SHA-256: `9076375ffe9f423fe92bb8659db3ca160c8ed8a9d8c06b2343617bd7ddf8fb4b` · token review SHA-256: `3c64d8e463f3935dbd7f147d8f09ecf2685533bcc96712971d9cef7c43328cb6`. [Aggregate results and hashes](assets/r634-seeds.json).

## Same-profile A/A repeatability · R618 / R635

R635 repeated the Qwen3.8 integrated-MTP profile on the same 33 previously exposed internal cases. Independent isolated CPU replay reproduced all case scores and effects. All 150 matched request bodies, input-token sequences and generated-token sequences matched; all 33 task and policy outcomes matched.

| Run | Solved | Policy gates | Case window s | GPU energy bounds J | GPU J / success bounds | Peak VRAM MiB | Per-case energy coverage |
|---|---|---|---|---|---|---|---|
| R618 | 27/33 | 31/33 | 625.025 | 162,024.8–162,132.5 | 6,000.9–6,004.9 | 13,602.5 | 0/33 |
| R635 | 27/33 | 31/33 | 624.284 | 161,460.3–161,598.3 | 5,980.0–5,985.1 | 13,602.5 | 0/33 |

GPU-board energy bounds bracket the first-to-last case window, including time between cases; startup and CPU/system energy are excluded. Per-case integration is incomplete. One A/A pair of correlated exposed cases establishes neither general determinism nor quality equivalence and does not qualify a Champion. The separate MTP ON/OFF comparison remains unqualified.

Audit SHA-256: R618 `3f718e7c2211b4c8721893ffa93aa3836601b31a9925a5640f28dac400634aaa` · R635 `dda8a6a4ca873831fc8dcc6c2b16759fcc57fe5cce831f76a3d26e823c8e6a2a`. [Aggregate results and hashes](assets/r635-aa.json).
