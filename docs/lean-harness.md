# Lean Jarvis harness

Controlled harness experiments; frozen model baselines remain unchanged. These exposed development tasks are **not official benchmarks or independent holdout validation**. All tools are offline simulators; policy violations count rejected proposals, not production actions.

## R586 · compact system instructions

**Decision: rejected — observed quality and policy regression.** Original tools, inference profile and scoring retained; only reviewed system prose changed. One model start, alternating AB/BA across33 paired cases /11 correlated task families.

| Arm | Solved | Policy violations | Input + output tokens | Task wall s | GPU J / success bounds | Peak MiB | Model calls |
|---|---|---|---|---|---|---|---|
| reference | 28/33 | 4 | 301561 | 402.025 | 3892.59–3981.9 | 7680.5 | 154 |
| compact-system-v1 | 25/33 | 6 | 293897 | 347.055 | 3759.13–3858.12 | 7680.5 | 155 |

Paired outcomes: 1 gained, 4 lost; 3 new policy-failure cases. Token reduction 2.54%; task-wall reduction 13.67%. These differences **do not qualify the candidate**.

Reasoning tokens: **NOT MEASURED**. GPU-energy intervals bracket cumulative NVML counter readings, not confidence intervals or calibration error. Failed tasks remain in cost numerators; model loading, warm-up and host CPU energy excluded. No population-equivalence claim.

Transformation CPU seconds (including preservation/audit): reference 0.078495, compact-system-v1 0.078844. Shared TASK phase: 749.095s /1200s. Independent isolated CPU replay reproduced all66 outcomes without model inference.

Captured implementation: transform SHA256 `815681cc326b87a7a6012e1bda85839eb2f3476d466ff24a6e93934ffce563bf`; engine binary SHA256 `08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54`. Transport and simulator identities are retained in the [public experiment data](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/experiments.json). Source commit for the local transform: **not recorded at execution**; binary hashes are not version numbers. [Frozen model settings](final-selection.md).

[Experiment and audit hashes](experiments/R586.md). Model SHA256: `a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052`; captured profile SHA256: `213872c0f5259b8fa4b2966a9dfab0513622e8444994a0a0bcaa9b9ed7f9d681`; scorer SHA256: `0f878d4627a4468f7c8102f73318c31fbff010fa01c52565252d87c731f3cd7b`.

## R587 · compact tool-result JSON

**Decision: rejected — observed quality and policy regression.** Original tools, inference profile and scoring retained; only insignificant JSON whitespace outside tool-result strings changed. One model start, alternating AB/BA across33 paired cases /11 correlated task families.

| Arm | Solved | Policy violations | Input + output tokens | Task wall s | GPU J / success bounds | Peak MiB | Model calls |
|---|---|---|---|---|---|---|---|
| reference | 28/33 | 4 | 301561 | 402.138 | 3924.56–4014.95 | 7680.5 | 154 |
| compact-tool-json-v1 | 26/33 | 6 | 301598 | 407.192 | 4271.64–4368.67 | 7680.5 | 156 |

Paired outcomes: 0 gained, 2 lost; 1 new policy-failure cases. Token reduction -0.01%; task-wall reduction -1.26%. These differences **do not qualify the candidate**.

Reasoning tokens: **NOT MEASURED**. GPU-energy intervals bracket cumulative NVML counter readings, not confidence intervals or calibration error. Failed tasks remain in cost numerators; model loading, warm-up and host CPU energy excluded. No population-equivalence claim.

Transformation CPU seconds (including preservation/audit): reference 0.063391, compact-tool-json-v1 0.065691. Shared TASK phase: 809.344s /1200s. Independent isolated CPU replay reproduced all66 outcomes without model inference.

CPU postprocessing required a byte-identical readable plan binding and restored permissions on empty sandbox mountpoints. Failed CPU receipts remain preserved; no GPU rerun or scoring-rule change. [Correction evidence](audits/audit-17506b61d17dea89357e.md).

Captured implementation: transform SHA256 `520d70a1f58c373e3a2bce3cca58cb083845f011bad18c7a07de75a8262383cb`; engine binary SHA256 `08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54`. Transport and simulator identities are retained in the [public experiment data](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/experiments.json). Source commit for the local transform: **not recorded at execution**; binary hashes are not version numbers. [Frozen model settings](final-selection.md).

[Experiment and audit hashes](experiments/R587.md). Model SHA256: `a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052`; captured profile SHA256: `b75d892abc3763779d7de5ec8e65ab14a8d5b4e7b44e7729ca1e2dd7b0b10446`; scorer SHA256: `a44040c1553f322dd3e8f00881352871cd7e243e5cbe829d4dc9c83ec6501d4e`.

## Next gate

Retain the original reference. Evaluate other isolated, source-reviewed harness changes before combinations or transfer. Reserve fresh fixtures for independent confirmation; no optimized harness has been adopted.

[Issue17](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17) · [Issue18](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18)
