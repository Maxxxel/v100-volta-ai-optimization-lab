# Public audit excerpt

Original SHA256: `6eb33e7ef42a9ca0e9b0de8ffeb0f474226cfae53d07ea8afaffa24878650cb1`

Original file: `AUDIT.json`; 798596 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "PLANNING_SCREEN_QUALITY_OR_COST_GATE_NOT_PASSED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One planning-policy screen/18development tasks, no heldout or independent winner",
    "Same model process, no second agent/model/worker;all actions simulated",
    "Planner overhead included in full task wall/GPU-J;GPU inference only,notwhole system",
    "Original simulator/task/package hashes and actor output cap unchanged",
    "No MTP/cache/power/quant/model combination and no production actions"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 35,
  "gpu_energy_j_approx": 17838.34180144297,
  "model_starts": 1,
  "original12": {
    "complete": false,
    "no_grade_loss": false,
    "observed": 0
  },
  "peak_device_vram_mib": 7356.5,
  "solved": 0,
  "wall_s": 67.75197886699999
}
```

</details>
