# Reproducibility and variability

These are archived, hash-verified observations; no new GPU execution. Fixed seeds do not establish deterministic results.

## Seed propagation

| Profile | Audit | Seed | Temperature | Requests | Server reports seed 1001 |
|---|---|---|---|---|---|
| Nexus | [R531](experiments/R531.md) | 1001 | 0.0 | 153 | 153 |
| OmniCoder | [R536](experiments/R536.md) | 1001 | 0 | 154 | 154 |
| Gemma 4 | [R534](experiments/R534.md) | 1001 | 1.0 | 177 | 177 |
| Qwen3.8 MTP | [R550](experiments/R550.md) | 1001 | 0 | 150 | 150 |

The pinned engine source shows per-request sampler initialization and passes the parsed seed to the distribution sampler when that sampler is used. Server-reported generation settings establish parsed configuration; internal RNG state is not measured. Temperature zero can use greedy sampling under the recorded source conditions.

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

## Qwen3.8 integrated MTP A/A pilot

| Fixed request | Within-session repeats equal | Across-session equal |
|---|---|---|
| 1 | YES | YES |
| 2 | YES | YES |
| 3 | YES | YES |

[R623](experiments/R623.md) used three short, previously exposed tool requests with seed 1001 and integrated MTP in two sessions. This restricted A/A observation does not prove general determinism, task quality, safety or a causal MTP improvement.

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

| Fixed request | No-cache A/A across sessions | Cache-on variants different from baseline | Cache hits | First difference, zero-based |
|---|---|---|---|---|
| 1 | YES | 0 | 2 | same |
| 2 | YES | 0 | 4 | same |
| 3 | YES | 4 | 4 | 0 |

[R620](experiments/R620.md) used identical input token IDs and wire order in two adjacent model sessions. The third request reproduced a cache-associated token divergence; this is not a whole-task safety evaluation or an identified kernel cause. The [R619](experiments/R619.md) preflight failure was traced separately to reordered JSON object keys and remains preserved.
