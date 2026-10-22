# Public audit excerpt

Original SHA256: `cd8eb8e97cb00d82a151afd35bd6e0d38cbd6e8eac1eadbaecebfa8baf450c80`

Original file: `AUDIT.json`; 5755 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GEMMA32K_NEW_CASE_CAPACITY_VALIDATION_PASSED_SCOPE_ONLY",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "New12syntheticrecords, fixedsamefamily/position/row-countstrata, sourcegenerator/oracles frozen beforeoutputs; notmodeltrainingholdout.",
    "Unchanged32Kmodel/runtime/template/T1P95K64/native256cap; originalQAandcommon14K validR430evidence reused, notgeneratedagain.",
    "Capacity-validation scope only, no speedup fromdifferentinputs and no overallmodel/agent/productionChampion.",
    "Known source11/12extended failure and nativeTool84/100/agent9/18policynegatives retained; one outputtrajectory percase, no population/repeated-run uncertainty.",
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
      "maximum_tokens": 29490,
      "minimum_tokens": 29119
    }
  },
  "context_tokens": 32768,
  "full_12_semantic_score_claimed": true,
  "gpu_energy_j_approx": 72487.35421607949,
  "gpu_j_per_success": 6589.759474189044,
  "model_starts": 1,
  "observed_cases": 12,
  "peak_device_vram_mib": 8526.5,
  "planned_cases": 12,
  "scopes": {
    "validation": {
      "full12": true,
      "gpu_energy_j_approx": 72487.35421607949,
      "gpu_j_per_success": 6589.759474189044,
      "observed": 12,
      "planned": 12,
      "solved": 11,
      "wall_s": 266.1359924
    }
  },
  "solved": 11,
  "wall_s": 266.1359924
}
```
