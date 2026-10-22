# Public audit excerpt

Original SHA256: `d8e1609bb2632a6b88cfd55c530a935c3916a66913cdcb4dcc8b8bc2ba485cd9`

Original file: `AUDIT.json`; 5794 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "QWEN38_NO_MTP32K_NEW_CASE_CAPACITY_VALIDATION_PASSED_SCOPE_ONLY",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "New12syntheticrecords, fixedsamefamily/position/row-countstrata, sourcegenerator/oracles frozen beforeoutputs; notmodeltrainingholdout.",
    "Unchanged32Kmodel/runtime/template/T1P95K64/native256cap; originalQAandcommon14K validR433evidence reused, notgeneratedagain.",
    "Capacity-validation scope only, no speedup fromdifferentinputs and no overallmodel/agent/productionChampion.",
    "SourceR43312/12extended andR260nativeagent14/18withadditionalpolicynegatives retained; one outputtrajectory percase, no population/repeated-run uncertainty.",
    "GPUboardtaskinferenceenergyonly; startup,warmup,CPU/systemexcluded; no actualtools."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 16,
  "context_profile_token_ranges": {
    "validation": {
      "maximum_tokens": 27777,
      "minimum_tokens": 27415
    }
  },
  "context_tokens": 32768,
  "full_12_semantic_score_claimed": true,
  "gpu_energy_j_approx": 147942.93721426307,
  "gpu_j_per_success": 12328.57810118859,
  "model_starts": 1,
  "observed_cases": 12,
  "peak_device_vram_mib": 14010.5,
  "planned_cases": 12,
  "scopes": {
    "validation": {
      "full12": true,
      "gpu_energy_j_approx": 147942.93721426307,
      "gpu_j_per_success": 12328.57810118859,
      "observed": 12,
      "planned": 12,
      "solved": 12,
      "wall_s": 548.199342112
    }
  },
  "solved": 12,
  "wall_s": 548.199342112
}
```
