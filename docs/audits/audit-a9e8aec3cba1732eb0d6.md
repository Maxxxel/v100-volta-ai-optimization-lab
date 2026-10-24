# Public audit excerpt

Original SHA256: `a9e8aec3cba1732eb0d60366ef0adc83d9b733e8d53eab5abd163b63167c8798`

Original file: `AUDIT.json`; 68064 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "PROMISING_EVENT_HISTORY_COMPACTION_NEEDS_FRESH_QUALIFICATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Current-state snapshot/patch/delete event semantics only; no historical-query/freeform-summary/vector-RAG or general model/agent superiority",
    "Query-independent exact source-event subset for all entities; all final states checked equal. No generated summaries or extra LLM calls; no actual tools executed",
    "R1613observations/task are one session, not36independent tasks. R162 oneB observation/task is only triage, fresh independent confirmation/stability required for a winner",
    "Full-case timing and GPU energy include compaction/tokenization/scoring; exclude CPUjoules/source-load/model-load/network. Buffered visibleTTFT unavailable; temperature telemetry only"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 28,
  "metrics": {
    "full_case_wall_s": 16.888403496,
    "gpu_energy_j": 4347.517882020604,
    "gpu_j_per_success": 362.2931568350503,
    "solved": 12,
    "successful_tasks_per_second": 0.7105467371644802,
    "tasks": 12
  },
  "original12": [
    {
      "e2e_s": 0.182190917,
      "gpu_energy_j": 36.778221707826425,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.233741973,
      "gpu_energy_j": 54.25258513521035,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.666850673,
      "gpu_energy_j": 175.248718413557,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.35781502,
      "gpu_energy_j": 88.21099552798437,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.295281674,
      "gpu_energy_j": 74.88243384327052,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.470707198,
      "gpu_energy_j": 117.7153822385937,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 1.074569889,
      "gpu_energy_j": 288.3046211515974,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.353167965,
      "gpu_energy_j": 88.75805282985425,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.241680876,
      "gpu_energy_j": 53.90576723346309,
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "e2e_s": 0.238881059,
      "gpu_energy_j": 53.07978634776387,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.56815871,
      "gpu_energy_j": 145.2046604549764,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "e2e_s": 0.371867643,
      "gpu_energy_j": 94.45774181117399,
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    }
  ],
  "peak_process_vram_mib": 7906
}
```

</details>
