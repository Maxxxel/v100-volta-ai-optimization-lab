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

## OmniCoder two-session pilot

| Fixed request | No-cache A/A across sessions | Cache-on variants different from baseline | Cache hits | First difference, zero-based |
|---|---|---|---|---|
| 1 | YES | 0 | 2 | same |
| 2 | YES | 0 | 4 | same |
| 3 | YES | 4 | 4 | 0 |

[R620](experiments/R620.md) used identical input token IDs and wire order in two adjacent model sessions. The third request reproduced a cache-associated token divergence; this is not a whole-task safety evaluation or an identified kernel cause. The [R619](experiments/R619.md) preflight failure was traced separately to reordered JSON object keys and remains preserved.
