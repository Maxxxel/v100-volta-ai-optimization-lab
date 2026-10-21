# Public audit excerpt

Original SHA256: `b02ace8b7df4b0eef8481ae4a1797af01a3edef807b5d7a4a3f1479cc522e5eb`

Original file: `AUDIT.json`; 4964 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "MANAGED_MEMORY_NATIVE_SCREEN_NO_QUALIFIED_PRACTICAL_GAIN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Resident fixed8KQ6workload only; no oversubscription/large-context/unseen-agent claim.",
    "Only existing managed-memory allocation/free-memory treatment; runtime/model math unchanged. Actual allocation calls verified, but GPU page-migration traffic not measured.",
    "Observer adds CPU allocation-time logging only, no added CUDA calls/pointer/result modification; fresh instrumentation-matched controls required for any positive qualification.",
    "NVML process/device VRAM may account managed pages differently; cumulative allocated bytes are not peak residency or host memory saving.",
    "Original12/nativeoutputIDs required; no coding/BFCL/agent/coldstart or champion qualification."
  ],
  "measurement_type": "GPU_H10_MANAGED_ALLOCATION_RESIDENT_NATIVE_SCREEN"
}
```

## Selected aggregate measurements

```json
{
  "CT_memory_observed": {
    "maximum_new_swap_bytes": 0,
    "minimum_available_bytes": 16037945344
  },
  "actual_generation_requests": 28,
  "actual_managed_allocator": {
    "calls": 5,
    "cumulative_bytes_not_peak": 7005214976,
    "managed_bytes_are_not_residency": true,
    "successful_calls": 5
  },
  "decode_e2e_reduction_percent_vs_A0": 0.7328111396422421,
  "model_starts": 1,
  "native_metrics": {
    "decode": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 0.7328111396422421,
          "tokens_per_second_gain_percent": -0.32462895073809284
        },
        "C": {
          "e2e_reduction_percent": 0.9572161120771638,
          "tokens_per_second_gain_percent": -0.1113220615150845
        }
      },
      "median_e2e_s": 1.664452188,
      "range_percent": 0.0785466839735899,
      "tokens_per_second": 79.55977758343754
    },
    "prefill": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 7.39091253583365,
          "tokens_per_second_gain_percent": -1.7133790572359975
        },
        "C": {
          "e2e_reduction_percent": -0.019232217499776105,
          "tokens_per_second_gain_percent": -9.51586567919085
        }
      },
      "median_e2e_s": 0.198385009,
      "range_percent": 0.6981797702264936,
      "tokens_per_second": 2559.9302482371963
    },
    "prefill2048": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 1.4754366720500234,
          "tokens_per_second_gain_percent": -1.2351969883023672
        },
        "C": {
          "e2e_reduction_percent": -7.556298961701113,
          "tokens_per_second_gain_percent": -9.688967182919683
        }
      },
      "median_e2e_s": 0.719863442,
      "range_percent": 0.29188938865435465,
      "tokens_per_second": 2851.311352618668
    },
    "prefill4096": {
      "comparison": {
        "A0": {
          "e2e_reduction_percent": 0.26594286924276345,
          "tokens_per_second_gain_percent": -1.0242597104065276
        },
        "C": {
          "e2e_reduction_percent": -8.246563939104323,
          "tokens_per_second_gain_percent": -9.428560992906798
        }
      },
      "median_e2e_s": 1.420817335,
      "range_percent": 0.1667670390578367,
      "tokens_per_second": 2888.1782829582676
    }
  },
  "original12_nonregression": true,
  "peak_device_vram_mib": 7452.5,
  "peak_process_vram_mib": 478.0
}
```
