# Public audit excerpt

Original SHA256: `c3cec6097613bd4e93c7aaa2331af5ffd4f4771ad2e1b0b9aa06bc2a203804cc`

Original file: `AUDIT.json`; 3643 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "Q6_SM70_PREFETCH_B_SCREEN_NOT_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "B-onlyscreen versus retained matching8KA0, no freshcontrol unless meaningfulsurvivor; no drift-independent winnerclaim",
    "Cuses6GiBweightcache, descriptive comparison, not isolatedprefetchcontrol",
    "Builtin24Q6CPUreferencecases coverm127/128,n1/2/4/8,k256/512/4096; n8otherkernelroute is control, no broadkernelproof",
    "CompiledSM70prefetch plusQ6CUDAexecution/maps shown; no direct measurementofL2cachehit benefit or physicalHBMbandwidth",
    "Original12/nativeoutputIDs unchanged required; no newcoding/BFCL/agentquality or production qualification"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 28,
  "decode_e2e_reduction_percent_vs_A0": -0.6872010737992262,
  "model_starts": 1,
  "native_metrics": {
    "decode": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": -0.6872010737992262,
          "tokens_per_second_gain_percent": -1.9667620237051486
        },
        "C": {
          "e2e_reduction_percent": -0.45958599936308797,
          "tokens_per_second_gain_percent": -1.7569693255385377
        }
      },
      "median_e2e_s": 1.688262094,
      "range_percent": 0.4631314076047773,
      "tokens_per_second": 78.24904514600225
    },
    "prefill": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 9.044929388824219,
          "tokens_per_second_gain_percent": 0.042825889540143436
        },
        "C": {
          "e2e_reduction_percent": 1.7671313051397464,
          "tokens_per_second_gain_percent": -7.899077119621789
        }
      },
      "median_e2e_s": 0.194841813,
      "range_percent": 0.44582011767669283,
      "tokens_per_second": 2605.671592503921
    },
    "prefill2048": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 2.83327565770074,
          "tokens_per_second_gain_percent": 0.15431292628416138
        },
        "C": {
          "e2e_reduction_percent": -6.073987029027261,
          "tokens_per_second_gain_percent": -8.418392325588986
        }
      },
      "median_e2e_s": 0.709942478,
      "range_percent": 0.4058290761973415,
      "tokens_per_second": 2891.4261027444545
    },
    "prefill4096": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 1.6994633926050495,
          "tokens_per_second_gain_percent": 0.4066570146725734
        },
        "C": {
          "e2e_reduction_percent": -6.69068949205649,
          "tokens_per_second_gain_percent": -8.119147327391051
        }
      },
      "median_e2e_s": 1.400395316,
      "range_percent": 0.2889372703385888,
      "tokens_per_second": 2929.9333897955917
    }
  },
  "numerical": {
    "CPU_reference": true,
    "max_nmse": 0.0005,
    "original_tester_unchanged": true,
    "q6_mentions": 24,
    "returncode": 0
  },
  "original12_nonregression": true,
  "peak_device_vram_mib": 7356.5
}
```
