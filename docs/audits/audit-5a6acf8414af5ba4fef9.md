# Public audit excerpt

Original SHA256: `5a6acf8414af5ba4fef9683bdd4dbe0e130a319e208976cf08f249cd0ffdcf89`

Original file: `AUDIT.json`; 92529 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "PROMISING_OMNI_EXTERNAL_MTP_AGENT_SCREEN_NEEDS_CONFIRMATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "18existing development cases,12multi-step HA/PVE/code workflows and6read/reasoning cases; no holdout or full assistant superiority claim",
    "Original v080 simulator/policy/static code evaluator reused unchanged; generated tools affect only temporary/in-memory fixtures, no arbitrary code execution or production endpoints",
    "Full case wall includes template/token proof and simulation; full case GPUenergy includes failed cases and GPUidle between requests, excludes CPU/system/load/idle outside cases",
    "One greedyseed/process; fresh drift confirmation and stability required for any champion; original12 separate controls",
    "Separate base-Qwen MTP-only head is the sole treatment; unchanged original target weights/engine/300W and cacheoff. No universal lossless guarantee or automatic champion."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 106,
  "metrics": {
    "gpu_energy_j": 44600.54124378858,
    "gpu_j_per_success": 3430.810864906814,
    "solved": 13,
    "successes_per_second": 0.07368241988182897,
    "tasks": 18,
    "total_wall_s": 176.43285903
  },
  "original12": [
    {
      "e2e_s": 0.165709531,
      "gpu_energy_j": 30.836726901638855,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.193368659,
      "gpu_energy_j": 46.133196655688174,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.445387307,
      "gpu_energy_j": 112.40491862312749,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.276678409,
      "gpu_energy_j": 57.091146346169324,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.22826007,
      "gpu_energy_j": 52.29730716735223,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.33463195,
      "gpu_energy_j": 69.05618193596126,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 1.102544561,
      "gpu_energy_j": 274.8654437688543,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.253946784,
      "gpu_energy_j": 51.8507302660267,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.227593289,
      "gpu_energy_j": 53.560548890967,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.196100206,
      "gpu_energy_j": 38.54389415249094,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.377268936,
      "gpu_energy_j": 89.37751889051016,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.277171712,
      "gpu_energy_j": 64.90025408659007,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    }
  ],
  "peak_process_vram_mib": 8758
}
```
