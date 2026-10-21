# Public audit excerpt

Original SHA256: `07e0c748aa3ce4016cab4354d6364f769c4fdd672c0076c8a20e266dd3dd3e43`

Original file: `AUDIT.json`; 92638 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "OMNICODER2_AGENT_200W_ENERGY_TRADEOFF_CONFIRMED_NEEDS_QUALIFICATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "18existing development cases,12multi-step HA/PVE/code workflows and6read/reasoning cases; no holdout or full assistant superiority claim",
    "Original v080 simulator/policy/static code evaluator reused unchanged; generated tools affect only temporary/in-memory fixtures, no arbitrary code execution or production endpoints",
    "Full case wall includes template/token proof and simulation; full case GPUenergy includes failed cases and GPUidle between requests, excludes CPU/system/load/idle outside cases",
    "One greedyseed/process; fresh drift confirmation and stability required for any champion; original12 separate controls"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 106,
  "metrics": {
    "gpu_energy_j": 62473.069935924075,
    "gpu_j_per_success": 4805.6207643018515,
    "solved": 13,
    "successes_per_second": 0.056463804166515114,
    "tasks": 18,
    "total_wall_s": 230.235992631
  },
  "original12": [
    {
      "e2e_s": 0.182514993,
      "gpu_energy_j": 43.1082888329721,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.239835032,
      "gpu_energy_j": 58.03326778471457,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.670552996,
      "gpu_energy_j": 177.2802882532852,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.357994865,
      "gpu_energy_j": 88.82116715716221,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.295077155,
      "gpu_energy_j": 75.07022374281999,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.46925306,
      "gpu_energy_j": 118.79168466023675,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 1.0795176,
      "gpu_energy_j": 286.5267454108613,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.353559961,
      "gpu_energy_j": 85.94331974928319,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.241498116,
      "gpu_energy_j": 54.20206188421929,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.23897504,
      "gpu_energy_j": 55.752292479107666,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.567783795,
      "gpu_energy_j": 149.9051548463771,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.371181574,
      "gpu_energy_j": 94.96788913783759,
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
