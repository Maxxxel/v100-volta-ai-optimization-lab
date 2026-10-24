# Public audit excerpt

Original SHA256: `8e5cb3c1e38c63ee92608ec958bca8b6d25f9c1ae9e92942da7a351960fecb23`

Original file: `AUDIT.json`; 5696 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "GRAFT_225W_AGENT_ENERGY_SCREEN_PASSED_NEEDS_INDEPENDENT_STABILITY",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Single225Wadditionalfactor onqualifiedgraftnocache/max3;300Wfoundationsandcachecomboalreadyqualified, noR04/cachechange",
    "18developmentagenttasks plusunchanged12, no newholdout or225Wcoding/BFCLquality/energyclaim",
    "Screenonly vsstoredA0/currentenergyC/fresh300Wgraft; independent3cycleenergyqualification/postcontrolrequiredforpromotion",
    "Actualpower200duringmeasurement,original300restoredwithjournalandnativeExecStopPost; no clocks/fan/compute/serviceconfigurationchanges",
    "GrossGPUcaseenergyincludesfailedcases,excludesCPU/system/load; balancedlatencybudget10%,notmaximumthroughputclaim"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "full18_score_claimed": true,
  "gpu_energy_j_approx": 36454.653202649606,
  "gpu_j_per_success": 2804.204092511508,
  "model_requests": 90,
  "model_starts": 1,
  "observed_tasks": 18,
  "original12": {
    "code": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "energy": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "filtering": {
      "format_pass": false,
      "raw_preserved": true,
      "semantic_pass": false
    },
    "german": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "ha_sim": {
      "format_pass": false,
      "raw_preserved": true,
      "semantic_pass": false
    },
    "jarvis_memory": {
      "format_pass": false,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "long_context": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "math": {
      "format_pass": false,
      "raw_preserved": true,
      "semantic_pass": false
    },
    "pve_sim": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "sorting": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    },
    "time": {
      "format_pass": true,
      "raw_preserved": true,
      "semantic_pass": true
    }
  },
  "peak_device_vram_mib": 7966.5,
  "solved": 13
}
```

</details>
