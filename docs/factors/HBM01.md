# HBM01 — Effective bandwidth and roofline

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Roofline analysis compares actual arithmetic and memory traffic. Model bytes divided by time are an estimate, not a measured HBM transaction count.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-c915993a806f0b95c0f6.md)
- [Original audit hash and public excerpt](../audits/audit-d7fc97756655a4112227.md)
- [Original audit hash and public excerpt](../audits/audit-e2e30ac7c1edebb0842f.md)
- [Original audit hash and public excerpt](../audits/audit-fe73faa6d74ccb07bdc1.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| baseline | PARTIALLY_IMPLEMENTED | PARTIAL | False |
| measured_roofline | PARTIALLY_IMPLEMENTED | DEFERRED | False |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "baseline"
      },
      {
        "historical_states": [
          "PARTIALLY_IMPLEMENTED"
        ],
        "signed_window_signatures": [],
        "value": "measured_roofline"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant baseline

```json
[
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 180912008,
        "copies": 100,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 21930685
      },
      {
        "copied_bytes": 56690688,
        "copies": 70,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 7041193
      },
      {
        "copied_bytes": 23199744,
        "copies": 2,
        "copy_kind_numeric": 8,
        "summed_copy_ns_not_E2E": 69728
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 230,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 60,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 27,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 3278040
      },
      "matrix_matrix": {
        "launches": 76,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 247,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 3454579
      },
      "other": {
        "launches": 94,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 411098
      }
    },
    "summed_kernel_ns_not_E2E": 7143717
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 7233284224,
        "copies": 3318,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 787584056
      },
      {
        "copied_bytes": 894517248,
        "copies": 840,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 97162224
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 282018,
    "observed_kernel_families": {
      "attention": {
        "launches": 4464,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 67584,
        "summed_kernel_ns_not_E2E": 235912367
      },
      "dequantization": {
        "launches": 6370,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 999432754
      },
      "matrix_matrix": {
        "launches": 7350,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 250,
        "max_shared_bytes_per_block": 65536,
        "summed_kernel_ns_not_E2E": 2339186488
      },
      "other": {
        "launches": 199228,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 56,
        "max_shared_bytes_per_block": 17920,
        "summed_kernel_ns_not_E2E": 1181559973
      },
      "quantized_matrix_vector": {
        "launches": 57598,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 96,
        "max_shared_bytes_per_block": 3072,
        "summed_kernel_ns_not_E2E": 2579147721
      },
      "recurrent_GDN": {
        "launches": 7008,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 95,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 297312268
      }
    },
    "summed_kernel_ns_not_E2E": 7632551571
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 80871424,
        "copies": 8,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 8972138
      },
      {
        "copied_bytes": 67108864,
        "copies": 7,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 8142283
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 16,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 2,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 225055
      },
      "matrix_matrix": {
        "launches": 5,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 236,
        "max_shared_bytes_per_block": 32768,
        "summed_kernel_ns_not_E2E": 1791707
      },
      "other": {
        "launches": 7,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 18,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 156095
      },
      "quantized_matrix_vector": {
        "launches": 2,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 56,
        "max_shared_bytes_per_block": 128,
        "summed_kernel_ns_not_E2E": 59520
      }
    },
    "summed_kernel_ns_not_E2E": 2232377
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 1032519680,
        "copies": 92,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 122186024
      },
      {
        "copied_bytes": 201392128,
        "copies": 23,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 24525792
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 34,
    "observed_kernel_families": {
      "attention": {
        "launches": 34,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 67584,
        "summed_kernel_ns_not_E2E": 21254154
      }
    },
    "summed_kernel_ns_not_E2E": 21254154
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 105671496,
        "copies": 49,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 13451872
      },
      {
        "copied_bytes": 28279808,
        "copies": 33,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 3515095
      },
      {
        "copied_bytes": 13762560,
        "copies": 1,
        "copy_kind_numeric": 8,
        "summed_copy_ns_not_E2E": 40672
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 110,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 29,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 1398624
      },
      "matrix_matrix": {
        "launches": 36,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 241,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 1716989
      },
      "other": {
        "launches": 45,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 200063
      }
    },
    "summed_kernel_ns_not_E2E": 3315676
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 20998984,
        "copies": 42,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 2206843
      },
      {
        "copied_bytes": 3113984,
        "copies": 21,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 336288
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 75,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 18,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 166561
      },
      "matrix_matrix": {
        "launches": 24,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 241,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 405535
      },
      "other": {
        "launches": 33,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 119486
      }
    },
    "summed_kernel_ns_not_E2E": 691582
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 20998984,
        "copies": 42,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 2270106
      },
      {
        "copied_bytes": 3113984,
        "copies": 21,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 402461
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 63,
    "observed_kernel_families": {
      "matrix_matrix": {
        "launches": 42,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 54864,
        "summed_kernel_ns_not_E2E": 1261659
      },
      "other": {
        "launches": 21,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 21,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 75295
      }
    },
    "summed_kernel_ns_not_E2E": 1336954
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 454165504,
        "copies": 138,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 49682058
      },
      {
        "copied_bytes": 249626624,
        "copies": 46,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 29256594
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 23,
    "observed_kernel_families": {
      "recurrent_GDN": {
        "launches": 23,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 95,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 11242979
      }
    },
    "summed_kernel_ns_not_E2E": 11242979
  }
]
```

### Variant measured_roofline

```json
[
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 180912008,
        "copies": 100,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 21930685
      },
      {
        "copied_bytes": 56690688,
        "copies": 70,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 7041193
      },
      {
        "copied_bytes": 23199744,
        "copies": 2,
        "copy_kind_numeric": 8,
        "summed_copy_ns_not_E2E": 69728
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 230,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 60,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 27,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 3278040
      },
      "matrix_matrix": {
        "launches": 76,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 247,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 3454579
      },
      "other": {
        "launches": 94,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 411098
      }
    },
    "summed_kernel_ns_not_E2E": 7143717
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 7233284224,
        "copies": 3318,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 787584056
      },
      {
        "copied_bytes": 894517248,
        "copies": 840,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 97162224
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 282018,
    "observed_kernel_families": {
      "attention": {
        "launches": 4464,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 67584,
        "summed_kernel_ns_not_E2E": 235912367
      },
      "dequantization": {
        "launches": 6370,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 999432754
      },
      "matrix_matrix": {
        "launches": 7350,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 250,
        "max_shared_bytes_per_block": 65536,
        "summed_kernel_ns_not_E2E": 2339186488
      },
      "other": {
        "launches": 199228,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 56,
        "max_shared_bytes_per_block": 17920,
        "summed_kernel_ns_not_E2E": 1181559973
      },
      "quantized_matrix_vector": {
        "launches": 57598,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 96,
        "max_shared_bytes_per_block": 3072,
        "summed_kernel_ns_not_E2E": 2579147721
      },
      "recurrent_GDN": {
        "launches": 7008,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 95,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 297312268
      }
    },
    "summed_kernel_ns_not_E2E": 7632551571
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 80871424,
        "copies": 8,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 8972138
      },
      {
        "copied_bytes": 67108864,
        "copies": 7,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 8142283
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 16,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 2,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 225055
      },
      "matrix_matrix": {
        "launches": 5,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 236,
        "max_shared_bytes_per_block": 32768,
        "summed_kernel_ns_not_E2E": 1791707
      },
      "other": {
        "launches": 7,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 18,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 156095
      },
      "quantized_matrix_vector": {
        "launches": 2,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 56,
        "max_shared_bytes_per_block": 128,
        "summed_kernel_ns_not_E2E": 59520
      }
    },
    "summed_kernel_ns_not_E2E": 2232377
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 1032519680,
        "copies": 92,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 122186024
      },
      {
        "copied_bytes": 201392128,
        "copies": 23,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 24525792
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 34,
    "observed_kernel_families": {
      "attention": {
        "launches": 34,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 67584,
        "summed_kernel_ns_not_E2E": 21254154
      }
    },
    "summed_kernel_ns_not_E2E": 21254154
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 105671496,
        "copies": 49,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 13451872
      },
      {
        "copied_bytes": 28279808,
        "copies": 33,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 3515095
      },
      {
        "copied_bytes": 13762560,
        "copies": 1,
        "copy_kind_numeric": 8,
        "summed_copy_ns_not_E2E": 40672
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 110,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 29,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 1398624
      },
      "matrix_matrix": {
        "launches": 36,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 241,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 1716989
      },
      "other": {
        "launches": 45,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 200063
      }
    },
    "summed_kernel_ns_not_E2E": 3315676
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 20998984,
        "copies": 42,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 2206843
      },
      {
        "copied_bytes": 3113984,
        "copies": 21,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 336288
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 75,
    "observed_kernel_families": {
      "dequantization": {
        "launches": 18,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 22,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 166561
      },
      "matrix_matrix": {
        "launches": 24,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 241,
        "max_shared_bytes_per_block": 45392,
        "summed_kernel_ns_not_E2E": 405535
      },
      "other": {
        "launches": 33,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 32,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 119486
      }
    },
    "summed_kernel_ns_not_E2E": 691582
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 20998984,
        "copies": 42,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 2270106
      },
      {
        "copied_bytes": 3113984,
        "copies": 21,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 402461
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 63,
    "observed_kernel_families": {
      "matrix_matrix": {
        "launches": 42,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 255,
        "max_shared_bytes_per_block": 54864,
        "summed_kernel_ns_not_E2E": 1261659
      },
      "other": {
        "launches": 21,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 21,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 75295
      }
    },
    "summed_kernel_ns_not_E2E": 1336954
  },
  {
    "CUDA_copy_API_activity": [
      {
        "copied_bytes": 454165504,
        "copies": 138,
        "copy_kind_numeric": 1,
        "summed_copy_ns_not_E2E": 49682058
      },
      {
        "copied_bytes": 249626624,
        "copies": 46,
        "copy_kind_numeric": 2,
        "summed_copy_ns_not_E2E": 29256594
      }
    ],
    "HBM_bytes_transactions_bandwidth_occupancy_measured": false,
    "kernel_launches": 23,
    "observed_kernel_families": {
      "recurrent_GDN": {
        "launches": 23,
        "max_local_bytes_per_thread": 0,
        "max_registers_per_thread": 95,
        "max_shared_bytes_per_block": 0,
        "summed_kernel_ns_not_E2E": 11242979
      }
    },
    "summed_kernel_ns_not_E2E": 11242979
  }
]
```

## Decision and remaining research

Acht konservierte CUDA-Traces erneut read-only geprüft. Kernel-/Memcpy-Ereignisse und Ressourcenmetadaten vorhanden, aber keine HBM-Transaktions-/Bandbreiten-/Occupancy-Hardwarecounter. Keine LLM-Roofline aus Copy-Bytes oder summierter Kerneldauer ableiten.

**Remaining scope:** Neue Profilierung nur für konkrete Patchfrage: tatsächlich verfügbare SM70-Counter, Bytes-Konvention, GPU-Workload-Korrelation und Profiling-Overheadkontrolle vorab belegen. Aktuell keine Hardwarebandbreite erfinden.

**Reopening condition:** Neue Profilierung nur für konkrete Patchfrage: tatsächlich verfügbare SM70-Counter, Bytes-Konvention, GPU-Workload-Korrelation und Profiling-Overheadkontrolle vorab belegen. Aktuell keine Hardwarebandbreite erfinden.

**Next action:** Neue Profilierung nur für konkrete Patchfrage: tatsächlich verfügbare SM70-Counter, Bytes-Konvention, GPU-Workload-Korrelation und Profiling-Overheadkontrolle vorab belegen. Aktuell keine Hardwarebandbreite erfinden.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R374](../experiments/R374.md), [R391](../experiments/R391.md), [R87](../experiments/R87.md)
