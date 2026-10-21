# Public audit excerpt

Original SHA256: `7ea265b5613fdf6bd79c6760b4925284a8c3d434edace84ad822e0982651cf0d`

Original file: `AUDIT.json`; 4324 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "QWEN38_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "18frozendevelopmenttasks;nonewholdoutorfinalmodelwinner",
    "OwnnativeQwentemplate/tokenizer,sharedtaskbodies/evaluation/budget/sampling;noTok/s-onlyrank",
    "CompleteGPUboardcasecostincludesfailedtasks;noCPU/system/loadenergy",
    "540scase-boundarybudgetmaystopbefore18;partialresultsneverfullscore",
    "ProviderQwen38noMTP/noCachebaseprofile;viablemodelmayreceiveseparateoptimization;no productiontools"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 97,
  "gpu_j_per_success": 9306.04318588106,
  "model_starts": 1,
  "peak_device_vram_mib": 12454.5,
  "solved": 14
}
```
