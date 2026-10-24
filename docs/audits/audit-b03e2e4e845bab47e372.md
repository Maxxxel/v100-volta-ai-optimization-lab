# Public audit excerpt

Original SHA256: `b03e2e4e845bab47e37271d3c63b86f61639ebec0d3e80f121327f205fe0f31e`

Original file: `AUDIT.json`; 114725 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MATCHED_OMNICODER2_AGENT_A0_CALIBRATED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "18existing development cases,12multi-step HA/PVE/code workflows and6read/reasoning cases; no holdout or full assistant superiority claim",
    "Original v080 simulator/policy/static code evaluator reused unchanged; generated tools affect only temporary/in-memory fixtures, no arbitrary code execution or production endpoints",
    "Full case wall includes template/token proof and simulation; full case GPUenergy includes failed cases and GPUidle between requests, excludes CPU/system/load/idle outside cases",
    "One greedyseed/process; fresh drift confirmation and stability required for any champion; original12 separate controls"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 106,
  "metrics": {
    "gpu_energy_j": 61685.34166161673,
    "gpu_j_per_success": 4745.026281662826,
    "solved": 13,
    "successes_per_second": 0.0565061763256302,
    "tasks": 18,
    "total_wall_s": 230.063346086
  },
  "original12": [
    {
      "e2e_s": 0.182074424,
      "gpu_energy_j": 35.16934352725614,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.233276457,
      "gpu_energy_j": 53.45056706657241,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.665787314,
      "gpu_energy_j": 174.25413707123514,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.356850482,
      "gpu_energy_j": 88.84109953748357,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.299289423,
      "gpu_energy_j": 74.71535231451396,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.472865426,
      "gpu_energy_j": 115.36180293217633,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 1.069936572,
      "gpu_energy_j": 287.67477135057146,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.353043967,
      "gpu_energy_j": 85.1899145588257,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.241720387,
      "gpu_energy_j": 58.95599747102791,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.238394542,
      "gpu_energy_j": 55.0753818248193,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.567988685,
      "gpu_energy_j": 147.0941375164251,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.370597148,
      "gpu_energy_j": 93.47486917267653,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    }
  ],
  "peak_process_vram_mib": 7114
}
```

</details>
