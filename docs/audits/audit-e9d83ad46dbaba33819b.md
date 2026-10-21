# Public audit excerpt

Original SHA256: `e9d83ad46dbaba33819bc756999744fd5ef4903c781fc827a3fb19e2efdd3089`

Original file: `AUDIT.json`; 864748 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "REFLECTION_SCREEN_QUALITY_OR_COST_GATE_NOT_PASSED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One post-tool reflection screen on original18developmentcases; no holdout or independent winner",
    "Same model process, no second agent/model/worker;all actions simulated",
    "All reflection overhead included in full task wall/GPU-J; GPU-only, not whole-system energy.",
    "Original simulator/task/package hashes and actor output cap unchanged",
    "No MTP/cache/power/quant/model combination and no production actions"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 29,
  "model_starts": 1,
  "original12": {
    "complete": false,
    "no_grade_loss": false,
    "observed": 0
  },
  "peak_device_vram_mib": 7356.5,
  "solved": 0,
  "wall_s": 77.504046832
}
```
