# Public audit excerpt

Original SHA256: `5f1297cfa36346cd5b2bcb919bb80fe9416169245021178bdcc276e5289f432c`

Original file: `AUDIT.json`; 14385 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "225W_INDEPENDENT_STABILITY_PASSED_SCOPE_ONLY",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Independent3cycle stability vs freshR436300W, narrowlonginventory energyprofile only; canonicalqualification requires independentreview.",
    "Same12synthetic read-only inventories repeated3cycles, not36independenttasks; ownnativeT1, no agent/coding energy claim.",
    "GPUboard inferencewindows only; excludes startup/CPU/system/warmup.",
    "Allhistoricalnativeformat and agentpolicynegatives remain."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 52,
  "completed_cycles": 3,
  "context_tokens": 16384,
  "energy_saving_percent_vs_stored": 13.696529647648237,
  "energy_stability_cycles": [
    {
      "cycle": 0,
      "energy_saving_percent": 14.457022484901072,
      "gpu_energy_j_approx": 28627.93581138441,
      "gpu_j_per_success": 2385.6613176153674,
      "observed": 12,
      "passed": true,
      "solved": 12,
      "wall_change_percent": 8.057573073665235,
      "wall_s": 134.328988545
    },
    {
      "cycle": 1,
      "energy_saving_percent": 13.107908911881738,
      "gpu_energy_j_approx": 29079.43209889495,
      "gpu_j_per_success": 2423.286008241246,
      "observed": 12,
      "passed": true,
      "solved": 12,
      "wall_change_percent": 8.64874808464049,
      "wall_s": 135.063892532
    },
    {
      "cycle": 2,
      "energy_saving_percent": 13.524657546161956,
      "gpu_energy_j_approx": 28939.962401928296,
      "gpu_j_per_success": 2411.6635334940247,
      "observed": 12,
      "passed": true,
      "solved": 12,
      "wall_change_percent": 8.781000198738687,
      "wall_s": 135.228298341
    }
  ],
  "full_36_executions_claimed": true,
  "gpu_energy_j_approx": 86647.33031220766,
  "gpu_j_per_success": 2406.870286450213,
  "model_starts": 1,
  "observed_cases": 36,
  "original12": {
    "format": 1,
    "observed": 12,
    "semantic": 10
  },
  "peak_device_vram_mib": 8254.5,
  "planned_cases": 36,
  "planned_cycles": 3,
  "qualification_candidate_passed": true,
  "solved": 36,
  "unique_tasks": 12,
  "wall_change_percent_vs_stored": 8.495773785681472,
  "wall_s": 404.621179418
}
```
