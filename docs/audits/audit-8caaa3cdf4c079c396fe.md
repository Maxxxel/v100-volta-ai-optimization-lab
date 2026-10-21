# Public audit excerpt

Original SHA256: `8caaa3cdf4c079c396fe7a40ed7d98d55ac3ded64728ba8d0568b4dcbadec284`

Original file: `AUDIT.json`; 18887 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "MATCHED_Q8Q8_ROUTER_OFF_CONTROL_CALIBRATED_CANDIDATE_PENDING",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Control calibration only; no new optimization or champion.",
    "Original12 and synthetic long decode only, no full coding/tool/agent or semantic32K qualification.",
    "Exact Q8/Q8 router-off identity is required for later isolated router-on B screen.",
    "NVML board joules are not whole-system energy or energy per successful agent task."
  ],
  "measurement_type": "GPU_Q8KV_ROUTER_OFF_MATCHED_PROFILE_CALIBRATION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "model_starts": 1,
  "native_metrics": {
    "decode": {
      "decode_tokens_per_s": {
        "mad": 0.04931251436863704,
        "median": 77.77468856442623
      },
      "e2e_s": {
        "mad": 0.0011824379999998413,
        "median": 1.699422586
      },
      "gpu_energy_j_approx": {
        "mad": 6.4356975218568095,
        "median": 448.51041302010304
      }
    },
    "long32512": {
      "decode_tokens_per_s": {
        "mad": 0.01948060635299953,
        "median": 61.542875031134884
      },
      "e2e_s": {
        "mad": 0.0013076269999992007,
        "median": 16.05856716
      },
      "gpu_energy_j_approx": {
        "mad": 5.428139532988098,
        "median": 4258.255078275995
      }
    },
    "prefill": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 6.739800000002405e-05,
        "median": 0.196158341
      },
      "gpu_energy_j_approx": {
        "mad": 0.2191817505305167,
        "median": 55.933508322333275
      }
    },
    "prefill2048": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 0.0005750300000000319,
        "median": 0.714010429
      },
      "gpu_energy_j_approx": {
        "mad": 4.778563227593935,
        "median": 200.293099926866
      }
    },
    "prefill4096": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 0.0017527319999999236,
        "median": 1.410511394
      },
      "gpu_energy_j_approx": {
        "mad": 1.5503285258292294,
        "median": 382.2623213864853
      }
    }
  },
  "original12_nonregression": true,
  "peak_device_vram_mib": 7756.5,
  "quality": [
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "reference_grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "reference_grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "reference_grade": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    },
    {
      "grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "reference_grade": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      },
      "regression": false
    }
  ],
  "requests": 32
}
```
