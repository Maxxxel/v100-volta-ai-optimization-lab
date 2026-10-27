# Lean Jarvis harness

Controlled harness experiments; frozen model baselines remain unchanged. These exposed development tasks are **not official benchmarks or independent holdout validation**.

## R586 · compact system instructions

**Decision: rejected — observed quality and policy regression.** Original tools, inference profile and scoring retained; only reviewed system prose changed. One model start, alternating AB/BA across33 paired cases /11 correlated task families.

| Arm | Solved | Policy violations | Input + output tokens | Task wall s | GPU J / success bounds | Peak MiB | Model calls |
|---|---|---|---|---|---|---|---|
| reference | 28/33 | 4 | 301561 | 402.025 | 3892.59–3981.9 | 7680.5 | 154 |
| compact-system-v1 | 25/33 | 6 | 293897 | 347.055 | 3759.13–3858.12 | 7680.5 | 155 |

Paired outcomes: 1 gained, 4 lost; 3 new policy-failure cases. Token reduction 2.54%; task-wall reduction 13.67%. These savings **do not qualify the candidate**.

Reasoning tokens: **NOT MEASURED**. GPU-energy intervals bracket cumulative NVML counter readings, not confidence intervals or calibration error. Failed tasks remain in cost numerators; model loading, warm-up and host CPU energy excluded. No population-equivalence claim.

Transformation CPU seconds (including preservation/audit): reference 0.078495, compact-system-v1 0.078844. Shared TASK phase: 749.095s /1200s. Independent isolated CPU replay reproduced all66 outcomes without model inference.

[Experiment and audit hashes](experiments/R586.md). Model SHA256: `a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052`; captured profile SHA256: `213872c0f5259b8fa4b2966a9dfab0513622e8444994a0a0bcaa9b9ed7f9d681`; scorer SHA256: `0f878d4627a4468f7c8102f73318c31fbff010fa01c52565252d87c731f3cd7b`.

## Next gate

Retain the original reference. Evaluate other isolated, source-reviewed harness changes before combinations or transfer. Reserve fresh fixtures for independent confirmation; no optimized harness has been adopted.

[Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17) · [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18)
