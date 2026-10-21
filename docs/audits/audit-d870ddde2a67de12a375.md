# Public audit excerpt

Original SHA256: `d870ddde2a67de12a375be63d4b35ab072ce8e4fca52e63a858995f23539437e`

Original file: `AUDIT.json`; 20630 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "Q8KV_ROUTING_SCREEN_PROMISING_NEEDS_FRESH_CONFIRMATION_AND_BROADER_QUALITY",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "B-only screen against recent exactsameQ8Q8configuration;onlyrouter0->1.",
    "Original12 and synthetic long decode only, no full coding/tool/agent or semantic32K qualification.",
    "A synthetic improvement needs fresh balanced control and independent taskquality before any champion.",
    "Native outputIDchanges recorded, not automatically a semanticregression or a losslessclaim.",
    "NVML board joules are not whole-system energy or energy per successful agent task."
  ],
  "measurement_type": "GPU_Q8KV_ROUTING_ON_SINGLE_FACTOR_SCREEN"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "comparison": {
    "decode": {
      "decode_phase_latency_change_percent": -0.38819980378731467,
      "e2e_change_percent": -0.33166371015854734,
      "gpu_energy_change_percent": 1.3029281526454994
    },
    "long32512": {
      "decode_phase_latency_change_percent": -9.439320178987998,
      "e2e_change_percent": -0.961250299992511,
      "gpu_energy_change_percent": 0.6504559988153913
    },
    "prefill": {
      "e2e_change_percent": 0.21009761700625518,
      "gpu_energy_change_percent": -11.618238033061079
    },
    "prefill2048": {
      "e2e_change_percent": 0.5054550820853709,
      "gpu_energy_change_percent": -1.6612860292419596
    },
    "prefill4096": {
      "e2e_change_percent": 0.2618458110803523,
      "gpu_energy_change_percent": 2.5079645454851196
    }
  },
  "model_starts": 1,
  "native_metrics": {
    "decode": {
      "decode_tokens_per_s": {
        "mad": 0.004320338774306265,
        "median": 78.0777863779469
      },
      "e2e_s": {
        "mad": 0.0006862640000000475,
        "median": 1.693786218
      },
      "gpu_energy_j_approx": {
        "mad": 4.298089489487609,
        "median": 454.35418145888855
      }
    },
    "long32512": {
      "decode_tokens_per_s": {
        "mad": 0.06702553880974449,
        "median": 67.95761157355582
      },
      "e2e_s": {
        "mad": 0.009217951000000113,
        "median": 15.904204135
      },
      "gpu_energy_j_approx": {
        "mad": 28.654144840750632,
        "median": 4285.953153877503
      }
    },
    "prefill": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 6.461399999999062e-05,
        "median": 0.196570465
      },
      "gpu_energy_j_approx": {
        "mad": 6.448268796011654,
        "median": 49.43502018520257
      }
    },
    "prefill2048": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 0.0011302199999999596,
        "median": 0.717619431
      },
      "gpu_energy_j_approx": {
        "mad": 3.5873592583667744,
        "median": 196.96565864024535
      }
    },
    "prefill4096": {
      "decode_tokens_per_s": {
        "mad": 0.0,
        "median": 0.0
      },
      "e2e_s": {
        "mad": 0.00046062499999988127,
        "median": 1.414204759
      },
      "gpu_energy_j_approx": {
        "mad": 1.228788964111743,
        "median": 391.84932487760676
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
