# Public audit excerpt

Original SHA256: `1e481b9ad01b4b62af2188084d18fbdb74e9314be9c8f420351627f726bfd63f`

Original file: `AUDIT.json`; 3576 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MTP_GRAFT_SCREEN_SURVIVES_NEEDS_INDEPENDENT_PRACTICAL_QUALIFICATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Single candidate process versus stored max3; no fresh drift control, no winner promotion",
    "Grafted target427tensor spans and originaltokenizer metadata byte-preserved; shared draftembedding/output may alter acceptance, numerical decisions, or practical success",
    "Original12 skipped after deterministic native regression or futility stop",
    "Native token identity applies only observed frozen samples, not universal losslessness"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "memory_saved_mib": 1032.0,
  "metrics": {
    "decode": {
      "latency_reduction_percent_vs_A0": 47.81318293516076,
      "latency_reduction_percent_vs_MTP3": 1.7502701045998603,
      "latency_reduction_percent_vs_native_C": 47.93115727672669,
      "median_e2e_s": 0.875036987,
      "median_gpu_energy_j_approx": 240.1151074738905,
      "range_percent": 1.02677214031868
    },
    "prefill": {
      "latency_reduction_percent_vs_A0": -9.539608053207637,
      "latency_reduction_percent_vs_MTP3": -1.1544679016274095,
      "latency_reduction_percent_vs_native_C": -18.304453643676876,
      "median_e2e_s": 0.234653172,
      "median_gpu_energy_j_approx": 46.29431943500183,
      "range_percent": 2.0566374444748554
    },
    "prefill2048": {
      "latency_reduction_percent_vs_A0": -12.356476507467672,
      "latency_reduction_percent_vs_MTP3": -1.1858171555199526,
      "latency_reduction_percent_vs_native_C": -22.656182065942776,
      "median_e2e_s": 0.820925434,
      "median_gpu_energy_j_approx": 158.74796869205886,
      "range_percent": 0.9543237029247547
    },
    "prefill4096": {
      "latency_reduction_percent_vs_A0": -11.293167588031716,
      "latency_reduction_percent_vs_MTP3": -0.23813253965327963,
      "latency_reduction_percent_vs_native_C": -20.792268237006194,
      "median_e2e_s": 1.585489113,
      "median_gpu_energy_j_approx": 418.1181767761099,
      "range_percent": 0.5085922655591296
    }
  },
  "model_starts": 1,
  "peak_device_vram_mib": 7976.5,
  "quality": {
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
  "requests": 28
}
```

</details>
