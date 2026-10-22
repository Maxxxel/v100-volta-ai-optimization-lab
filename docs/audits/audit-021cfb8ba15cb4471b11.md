# Public audit excerpt

Original SHA256: `021cfb8ba15cb4471b111ebcbe44088d2d26d06809f01981d24db6cde1b6f4a5`

Original file: `AUDIT.json`; 4921 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GEMMA4_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "18frozendevelopmenttasks;nonewholdoutorfinalmodelwinner",
    "Own native Gemma template/tokenizer and publishedT1/P95/K64; shared task bodies/effect/policy scorer/1400cap;noTok/s-onlyrank",
    "CompleteGPUboardcasecostincludesfailedtasks;noCPU/system/loadenergy",
    "540scase-boundarybudgetmaystopbefore18;partialresultsneverfullscore",
    "GemmaQATQ40fastnoMTP/noCachebaseprofile;viablemodelmayreceiveseparateoptimization;no productiontools"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 129,
  "full18_score_claimed": true,
  "gpu_energy_j_approx": 79448.26361013179,
  "gpu_j_per_success": 8827.5848455702,
  "model_requests": 125,
  "model_starts": 1,
  "observed_tasks": 18,
  "peak_device_vram_mib": 8118.5,
  "solved": 9
}
```
