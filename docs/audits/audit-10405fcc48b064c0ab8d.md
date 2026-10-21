# Public audit excerpt

Original SHA256: `10405fcc48b064c0ab8d0761fed5207c0c832ff59e7c54c5334a08f74ed27052`

Original file: `AUDIT.json`; 1889786 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "POLICY_POSITION_SCREEN_QUALITY_OR_COST_GATE_NOT_PASSED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "18developmentcases, noholdout/modelwinner",
    "All original system text retained once, same first-system role;moving system role later is forbidden by original template and not tested",
    "Original template file untouched;derived private candidate only",
    "Input ID order/token-boundary counts can differ as intended;not same-token kernel speedup",
    "Cold KV/noMTP/noextraPlanner;unchanged simulator/staticcodechecker and no productiontools"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 88,
  "gpu_j_per_success": 3603.640378894384,
  "model_starts": 1,
  "original12": {
    "complete": false,
    "no_grade_loss": false,
    "observed": 0
  },
  "peak_device_vram_mib": 7356.5,
  "solved": 13,
  "wall_s": 173.162904627
}
```
