# Public audit excerpt

Original SHA256: `f48de8313838adc8b3b4940143dd90a7822a1e350aca33f67feaafb6318cebf3`

Original file: `AUDIT.json`; 4387 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "QWEN35_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "18frozendevelopmenttasks;nonewholdoutorfinalmodelwinner",
    "OwnnativeQwentemplate/tokenizer,sharedtaskbodies/evaluation/budget/sampling;noTok/s-onlyrank",
    "CompleteGPUboardcasecostincludesfailedtasks;noCPU/system/loadenergy",
    "540scase-boundarybudgetmaystopbefore18;partialresultsneverfullscore",
    "OriginalQwen35noMTP/noCachebaseprofile;viablemodelmayreceiveseparateoptimization;no productiontools"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 102,
  "full18_score_claimed": true,
  "gpu_energy_j_approx": 56164.790740286684,
  "gpu_j_per_success": 7020.5988425358355,
  "model_requests": 98,
  "model_starts": 1,
  "observed_tasks": 18,
  "peak_device_vram_mib": 5956.5,
  "solved": 8
}
```

</details>
