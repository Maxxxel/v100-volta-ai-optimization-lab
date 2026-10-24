# HBM14 — Host/PCIe/HBM staging

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Host-side KV offload trades device capacity for transfers and CPU work. It requires a real capacity problem and bounded host memory.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-3a0b0ee463a9a6eaaab3.md)
- [Original audit hash and public excerpt](../audits/audit-b5b72880a82c7c178bfd.md)
- [Original audit hash and public excerpt](../audits/audit-c915993a806f0b95c0f6.md)
- [Original audit hash and public excerpt](../audits/audit-fe73faa6d74ccb07bdc1.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| gpu_reference | READY_LINKED | PARTIAL | False |
| kv_cpu | READY_LINKED | TESTED_NEGATIVE | True |
| partial_cpu | READY_LINKED | TESTED_NEGATIVE | True |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "gpu_reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "kv_cpu"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "partial_cpu"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "gpu_reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "kv_cpu"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "partial_cpu"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "gpu_reference"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "kv_cpu"
      },
      {
        "historical_states": [
          "READY_LINKED"
        ],
        "signed_window_signatures": [],
        "value": "partial_cpu"
      }
    ],
    "model": "qwen38"
  }
]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant gpu_reference

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "archive": {
      "sha256": "160570a3e1a753f4b5a377b4794b8b94b0565ba0f384ebe1834baf0c1510d6bf"
    },
    "historical_change_exercised": true,
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2595.3070256740925,
        "QA_request_wall_sum_s": 10.127546391,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 3967.1880444053236,
        "QA_request_wall_sum_s": 32.269538957,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 6670.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 269.17040872357813,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 54.59244358322663,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -72.73818794296632,
        "ttft_change_pct": 324.903580220389
      },
      "prefill": {
        "e2e_change_pct": 66.66007299696737,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 22.27398348848928,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -40.191647235121486,
        "ttft_change_pct": 66.79322889992775
      },
      "prefill2048": {
        "e2e_change_pct": 63.16234732362673,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 20.700008144303062,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -38.733953767248366,
        "ttft_change_pct": 63.17190865158977
      },
      "prefill4096": {
        "e2e_change_pct": 66.1749703157808,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 19.05596329669219,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -39.85739084630819,
        "ttft_change_pct": 66.19838424017874
      }
    },
    "plan": {
      "sha256": "e2312b84d01688894d16d8c006e9ad18e85fc15fea3efbc859039e8d0b9759cc"
    },
    "raw_members": [
      {
        "sha256": "b45dfb43510703e6b004bcec6fee27bb388f029068ca59264059aa4d120eb733"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3a6af7792ee8c4dd80426779b7738428123c0b3db4914b2008a875bf66c7d2fe"
      },
      {
        "sha256": "8046b600a94f8b6637fa21c567ab04ed7d1458b1feb50caace9fc57d80498a6c"
      },
      {
        "sha256": "36b1aa80642e5bd3adb5fa2574a5e70ea3105f2a4661aaa507a9e42065719c57"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "b639355903991efe319eaa5158a78b1c6981597b65f68f28e2ef8d503bd4d8a0"
      },
      {
        "sha256": "e65279b1ed25d7f23d451e0f420cbd97f4c58f79957c3ddabcfcf286567af95d"
      },
      {
        "sha256": "ea9bd23f550f5387863114d541888dc55b6a9d657595f8aa14ee607d83aa30b7"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "eda696cbf405071d7527b4e9658c26cff048f53021452a871282dcf09eee5948"
      },
      {
        "sha256": "2d26028cf748bb736e479f340c8b7abee2d9dbfd715e3cd6d3b2e7b999632ec5"
      },
      {
        "sha256": "c2e932eaa9135dbd1768eb05dbe0d995bd21dfa9fc1042a27ac23623f040d3e5"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3cd4200f7beea5c4aaba3907f006a2032a914f4234edd795d01d89c58c9e1898"
      },
      {
        "sha256": "8571360f4c739b0a638344d1e3eb9ca7948753e3ee008829bb667b14073b4609"
      },
      {
        "sha256": "028e2d492b023138c5d416fd1fd361a9e12238ac97fb53e6ec2637ca8b54a3c9"
      }
    ],
    "residency": {
      "arms": {
        "A": {
          "gpu_owned_peak_bytes": 7459569664,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728553984,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        },
        "B": {
          "gpu_owned_peak_bytes": 6740246528,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728476160,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        }
      },
      "change_exercised": true,
      "note": "Both arms same original engine, verbosity5 for actual layer assignment evidence, six threads and unchanged frozen quality/speed probes. Output stays on GPU, first4repeating layers move to CPU. Paired A/B isolates offload; original-baseline comparison also includes the shared diagnostic verbosity difference."
    },
    "results": {
      "sha256": "3a0b0ee463a9a6eaaab393f708e2288aa07cb7efee787b59dd330c9b81ef2d20"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728553984,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402753500774029
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728476160,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402843005933316
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728398336,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402931677007563
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728549888,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402976686469767
          }
        }
      }
    ]
  },
  {
    "archive": {
      "sha256": "734f9bf9116775b1a3eb0bcc2a9f26426d0dac2f7e23824093f3ca573048d593"
    },
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2591.1921987178803,
        "QA_request_wall_sum_s": 10.101557431,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 4047.742048849017,
        "QA_request_wall_sum_s": 27.205148439,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7068.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 202.06573658964385,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 62.708176513812994,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -67.25571254281095,
        "ttft_change_pct": 125.81431936681628
      },
      "prefill": {
        "e2e_change_pct": 69.87995300890088,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 26.769155789201825,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -41.026799517888875,
        "ttft_change_pct": 69.93877927005383
      },
      "prefill2048": {
        "e2e_change_pct": 63.101247107769545,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 25.28028260326827,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -38.71887663553538,
        "ttft_change_pct": 63.12187552664603
      },
      "prefill4096": {
        "e2e_change_pct": 60.48594417411943,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 23.80257001313155,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -37.69850776663397,
        "ttft_change_pct": 60.511609739398644
      }
    },
    "plan": {
      "sha256": "9790439927f39416c2beebf20e9c99848141c42d49b93f02907345e0fdb92f40"
    },
    "raw_members": [
      {
        "sha256": "85cb3db1933259ef7f6cca97adfef9df604ef5bc0de2638c720a0c7ba18df340"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "c0071a9ee69147995c52a004a89e6d8f9fc3501e668c9d5dec585bae2409379b"
      },
      {
        "sha256": "9714ec1cc42b06340ed314e3380a324aa4d61d8a9a68c4246b3adebe4a75934b"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "afe99c61cccfe43df24ebbe3ae5f774f2bd36a94dc07b311aa74fa4797c0df40"
      },
      {
        "sha256": "3e8f4afed81e6958ab2d3fae21eb0393e883ced91361c56b8243c5eb717c27ac"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "40bb67ee94085e9ab355dfacaa628cbc2838b9ea10d0dff8ca7ff61581b20075"
      },
      {
        "sha256": "2e056cf46b4ce129042386085bd17a068ea1b4196c8b03bb8b835ee0abdb272f"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "1f826506da5b59e8e642c13111d736ac779c8a7b9e55f6b957cda981c9de377b"
      },
      {
        "sha256": "5f6b853d185ec261cb73b1a7a2fd99b98bc7d8f5baba55a19d7bc036a229c2cb"
      }
    ],
    "results": {
      "sha256": "b5b72880a82c7c178bfd48d06cbdfa1b0fddda1cce229a5df18e2ca8f51ac67b"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      }
    ]
  }
]
```

</details>

### Variant kv_cpu

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "archive": {
      "sha256": "160570a3e1a753f4b5a377b4794b8b94b0565ba0f384ebe1834baf0c1510d6bf"
    },
    "historical_change_exercised": true,
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2595.3070256740925,
        "QA_request_wall_sum_s": 10.127546391,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 3967.1880444053236,
        "QA_request_wall_sum_s": 32.269538957,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 6670.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 269.17040872357813,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 54.59244358322663,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -72.73818794296632,
        "ttft_change_pct": 324.903580220389
      },
      "prefill": {
        "e2e_change_pct": 66.66007299696737,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 22.27398348848928,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -40.191647235121486,
        "ttft_change_pct": 66.79322889992775
      },
      "prefill2048": {
        "e2e_change_pct": 63.16234732362673,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 20.700008144303062,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -38.733953767248366,
        "ttft_change_pct": 63.17190865158977
      },
      "prefill4096": {
        "e2e_change_pct": 66.1749703157808,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 19.05596329669219,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -39.85739084630819,
        "ttft_change_pct": 66.19838424017874
      }
    },
    "plan": {
      "sha256": "e2312b84d01688894d16d8c006e9ad18e85fc15fea3efbc859039e8d0b9759cc"
    },
    "raw_members": [
      {
        "sha256": "b45dfb43510703e6b004bcec6fee27bb388f029068ca59264059aa4d120eb733"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3a6af7792ee8c4dd80426779b7738428123c0b3db4914b2008a875bf66c7d2fe"
      },
      {
        "sha256": "8046b600a94f8b6637fa21c567ab04ed7d1458b1feb50caace9fc57d80498a6c"
      },
      {
        "sha256": "36b1aa80642e5bd3adb5fa2574a5e70ea3105f2a4661aaa507a9e42065719c57"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "b639355903991efe319eaa5158a78b1c6981597b65f68f28e2ef8d503bd4d8a0"
      },
      {
        "sha256": "e65279b1ed25d7f23d451e0f420cbd97f4c58f79957c3ddabcfcf286567af95d"
      },
      {
        "sha256": "ea9bd23f550f5387863114d541888dc55b6a9d657595f8aa14ee607d83aa30b7"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "eda696cbf405071d7527b4e9658c26cff048f53021452a871282dcf09eee5948"
      },
      {
        "sha256": "2d26028cf748bb736e479f340c8b7abee2d9dbfd715e3cd6d3b2e7b999632ec5"
      },
      {
        "sha256": "c2e932eaa9135dbd1768eb05dbe0d995bd21dfa9fc1042a27ac23623f040d3e5"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3cd4200f7beea5c4aaba3907f006a2032a914f4234edd795d01d89c58c9e1898"
      },
      {
        "sha256": "8571360f4c739b0a638344d1e3eb9ca7948753e3ee008829bb667b14073b4609"
      },
      {
        "sha256": "028e2d492b023138c5d416fd1fd361a9e12238ac97fb53e6ec2637ca8b54a3c9"
      }
    ],
    "residency": {
      "arms": {
        "A": {
          "gpu_owned_peak_bytes": 7459569664,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728553984,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        },
        "B": {
          "gpu_owned_peak_bytes": 6740246528,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728476160,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        }
      },
      "change_exercised": true,
      "note": "Both arms same original engine, verbosity5 for actual layer assignment evidence, six threads and unchanged frozen quality/speed probes. Output stays on GPU, first4repeating layers move to CPU. Paired A/B isolates offload; original-baseline comparison also includes the shared diagnostic verbosity difference."
    },
    "results": {
      "sha256": "3a0b0ee463a9a6eaaab393f708e2288aa07cb7efee787b59dd330c9b81ef2d20"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728553984,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402753500774029
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728476160,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402843005933316
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728398336,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402931677007563
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728549888,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402976686469767
          }
        }
      }
    ]
  },
  {
    "archive": {
      "sha256": "734f9bf9116775b1a3eb0bcc2a9f26426d0dac2f7e23824093f3ca573048d593"
    },
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2591.1921987178803,
        "QA_request_wall_sum_s": 10.101557431,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 4047.742048849017,
        "QA_request_wall_sum_s": 27.205148439,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7068.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 202.06573658964385,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 62.708176513812994,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -67.25571254281095,
        "ttft_change_pct": 125.81431936681628
      },
      "prefill": {
        "e2e_change_pct": 69.87995300890088,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 26.769155789201825,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -41.026799517888875,
        "ttft_change_pct": 69.93877927005383
      },
      "prefill2048": {
        "e2e_change_pct": 63.101247107769545,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 25.28028260326827,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -38.71887663553538,
        "ttft_change_pct": 63.12187552664603
      },
      "prefill4096": {
        "e2e_change_pct": 60.48594417411943,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 23.80257001313155,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -37.69850776663397,
        "ttft_change_pct": 60.511609739398644
      }
    },
    "plan": {
      "sha256": "9790439927f39416c2beebf20e9c99848141c42d49b93f02907345e0fdb92f40"
    },
    "raw_members": [
      {
        "sha256": "85cb3db1933259ef7f6cca97adfef9df604ef5bc0de2638c720a0c7ba18df340"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "c0071a9ee69147995c52a004a89e6d8f9fc3501e668c9d5dec585bae2409379b"
      },
      {
        "sha256": "9714ec1cc42b06340ed314e3380a324aa4d61d8a9a68c4246b3adebe4a75934b"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "afe99c61cccfe43df24ebbe3ae5f774f2bd36a94dc07b311aa74fa4797c0df40"
      },
      {
        "sha256": "3e8f4afed81e6958ab2d3fae21eb0393e883ced91361c56b8243c5eb717c27ac"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "40bb67ee94085e9ab355dfacaa628cbc2838b9ea10d0dff8ca7ff61581b20075"
      },
      {
        "sha256": "2e056cf46b4ce129042386085bd17a068ea1b4196c8b03bb8b835ee0abdb272f"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "1f826506da5b59e8e642c13111d736ac779c8a7b9e55f6b957cda981c9de377b"
      },
      {
        "sha256": "5f6b853d185ec261cb73b1a7a2fd99b98bc7d8f5baba55a19d7bc036a229c2cb"
      }
    ],
    "results": {
      "sha256": "b5b72880a82c7c178bfd48d06cbdfa1b0fddda1cce229a5df18e2ca8f51ac67b"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      }
    ]
  }
]
```

</details>

### Variant partial_cpu

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "archive": {
      "sha256": "160570a3e1a753f4b5a377b4794b8b94b0565ba0f384ebe1834baf0c1510d6bf"
    },
    "historical_change_exercised": true,
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2595.3070256740925,
        "QA_request_wall_sum_s": 10.127546391,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 3967.1880444053236,
        "QA_request_wall_sum_s": 32.269538957,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 6670.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 269.17040872357813,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 54.59244358322663,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -72.73818794296632,
        "ttft_change_pct": 324.903580220389
      },
      "prefill": {
        "e2e_change_pct": 66.66007299696737,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 22.27398348848928,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -40.191647235121486,
        "ttft_change_pct": 66.79322889992775
      },
      "prefill2048": {
        "e2e_change_pct": 63.16234732362673,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 20.700008144303062,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -38.733953767248366,
        "ttft_change_pct": 63.17190865158977
      },
      "prefill4096": {
        "e2e_change_pct": 66.1749703157808,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 19.05596329669219,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "throughput_comparison_eligible": true,
        "tokens_per_s_change_pct": -39.85739084630819,
        "ttft_change_pct": 66.19838424017874
      }
    },
    "plan": {
      "sha256": "e2312b84d01688894d16d8c006e9ad18e85fc15fea3efbc859039e8d0b9759cc"
    },
    "raw_members": [
      {
        "sha256": "b45dfb43510703e6b004bcec6fee27bb388f029068ca59264059aa4d120eb733"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3a6af7792ee8c4dd80426779b7738428123c0b3db4914b2008a875bf66c7d2fe"
      },
      {
        "sha256": "8046b600a94f8b6637fa21c567ab04ed7d1458b1feb50caace9fc57d80498a6c"
      },
      {
        "sha256": "36b1aa80642e5bd3adb5fa2574a5e70ea3105f2a4661aaa507a9e42065719c57"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "b639355903991efe319eaa5158a78b1c6981597b65f68f28e2ef8d503bd4d8a0"
      },
      {
        "sha256": "e65279b1ed25d7f23d451e0f420cbd97f4c58f79957c3ddabcfcf286567af95d"
      },
      {
        "sha256": "ea9bd23f550f5387863114d541888dc55b6a9d657595f8aa14ee607d83aa30b7"
      },
      {
        "sha256": "f06a4375a35d75d51f4992037afec3d3d1fd3d014f68d5f559cafbba0683375f"
      },
      {
        "sha256": "eda696cbf405071d7527b4e9658c26cff048f53021452a871282dcf09eee5948"
      },
      {
        "sha256": "2d26028cf748bb736e479f340c8b7abee2d9dbfd715e3cd6d3b2e7b999632ec5"
      },
      {
        "sha256": "c2e932eaa9135dbd1768eb05dbe0d995bd21dfa9fc1042a27ac23623f040d3e5"
      },
      {
        "sha256": "afe2906f805e1ad986d577e2712fc4f3742e4bf88ddc27b71ec770a15e709a0c"
      },
      {
        "sha256": "3cd4200f7beea5c4aaba3907f006a2032a914f4234edd795d01d89c58c9e1898"
      },
      {
        "sha256": "8571360f4c739b0a638344d1e3eb9ca7948753e3ee008829bb667b14073b4609"
      },
      {
        "sha256": "028e2d492b023138c5d416fd1fd361a9e12238ac97fb53e6ec2637ca8b54a3c9"
      }
    ],
    "residency": {
      "arms": {
        "A": {
          "gpu_owned_peak_bytes": 7459569664,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728553984,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        },
        "B": {
          "gpu_owned_peak_bytes": 6740246528,
          "memory_limit_bytes": 8589934592,
          "rss_peak_bytes": 7728476160,
          "starts": 2,
          "swap_peak_bytes": 0,
          "verified_starts": 2
        }
      },
      "change_exercised": true,
      "note": "Both arms same original engine, verbosity5 for actual layer assignment evidence, six threads and unchanged frozen quality/speed probes. Output stays on GPU, first4repeating layers move to CPU. Paired A/B isolates offload; original-baseline comparison also includes the shared diagnostic verbosity difference."
    },
    "results": {
      "sha256": "3a0b0ee463a9a6eaaab393f708e2288aa07cb7efee787b59dd330c9b81ef2d20"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728553984,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402753500774029
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728476160,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402843005933316
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 6740246528,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728398336,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 1472.76
                },
                {
                  "mib": 5535.12
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402931677007563
          }
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "layer_slots": 33,
          "residency_proof": {
            "memory": {
              "gpu_owned_peak_bytes": 7459569664,
              "memory_limit_bytes": 8589934592,
              "reserve_bytes": 2147483648,
              "rss_peak_bytes": 7728549888,
              "swap_peak_bytes": 0,
              "verified": true
            },
            "model": "omnicoder2",
            "placement": {
              "buffers": [
                {
                  "mib": 795.7
                },
                {
                  "mib": 6212.17
                }
              ],
              "note": "Actual unique mmap load only; load_mode=none fit probes excluded. Output is the final layer slot and remains GPU resident. Even full-offload keeps input embeddings in a CPU model buffer.",
              "verified": true
            },
            "telemetry_end_ns": 402976686469767
          }
        }
      }
    ]
  },
  {
    "archive": {
      "sha256": "734f9bf9116775b1a3eb0bcc2a9f26426d0dac2f7e23824093f3ca573048d593"
    },
    "metrics": {
      "A": {
        "QA_request_GPU_j": 2591.1921987178803,
        "QA_request_wall_sum_s": 10.101557431,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7356.5
      },
      "B": {
        "QA_request_GPU_j": 4047.742048849017,
        "QA_request_wall_sum_s": 27.205148439,
        "QA_unique_tasks": 12,
        "peak_device_VRAM_mib": 7068.5
      }
    },
    "native_comparison": {
      "decode": {
        "e2e_change_pct": 202.06573658964385,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 62.708176513812994,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -67.25571254281095,
        "ttft_change_pct": 125.81431936681628
      },
      "prefill": {
        "e2e_change_pct": 69.87995300890088,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 26.769155789201825,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -41.026799517888875,
        "ttft_change_pct": 69.93877927005383
      },
      "prefill2048": {
        "e2e_change_pct": 63.101247107769545,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 25.28028260326827,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -38.71887663553538,
        "ttft_change_pct": 63.12187552664603
      },
      "prefill4096": {
        "e2e_change_pct": 60.48594417411943,
        "format_pass_change": 0,
        "gpu_energy_change_pct": 23.80257001313155,
        "same_token_counts": true,
        "semantic_pass_change": 0,
        "tokens_per_s_change_pct": -37.69850776663397,
        "ttft_change_pct": 60.511609739398644
      }
    },
    "plan": {
      "sha256": "9790439927f39416c2beebf20e9c99848141c42d49b93f02907345e0fdb92f40"
    },
    "raw_members": [
      {
        "sha256": "85cb3db1933259ef7f6cca97adfef9df604ef5bc0de2638c720a0c7ba18df340"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "c0071a9ee69147995c52a004a89e6d8f9fc3501e668c9d5dec585bae2409379b"
      },
      {
        "sha256": "9714ec1cc42b06340ed314e3380a324aa4d61d8a9a68c4246b3adebe4a75934b"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "afe99c61cccfe43df24ebbe3ae5f774f2bd36a94dc07b311aa74fa4797c0df40"
      },
      {
        "sha256": "3e8f4afed81e6958ab2d3fae21eb0393e883ced91361c56b8243c5eb717c27ac"
      },
      {
        "sha256": "272489a87a65e7b57dea1cb3b1aca53c4ce1ccab55aa79cb2cdd0645fd55b558"
      },
      {
        "sha256": "40bb67ee94085e9ab355dfacaa628cbc2838b9ea10d0dff8ca7ff61581b20075"
      },
      {
        "sha256": "2e056cf46b4ce129042386085bd17a068ea1b4196c8b03bb8b835ee0abdb272f"
      },
      {
        "sha256": "d96b2a488bce0548b7a94e03637712ccf1d3ddbc91cb44372db1935e91e6e87a"
      },
      {
        "sha256": "1f826506da5b59e8e642c13111d736ac779c8a7b9e55f6b957cda981c9de377b"
      },
      {
        "sha256": "5f6b853d185ec261cb73b1a7a2fd99b98bc7d8f5baba55a19d7bc036a229c2cb"
      }
    ],
    "results": {
      "sha256": "b5b72880a82c7c178bfd48d06cbdfa1b0fddda1cce229a5df18e2ca8f51ac67b"
    },
    "runs": [
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      },
      {
        "CUDA_device_and_library_mapped": true,
        "actual_configuration": {
          "KV_mib": 256.0,
          "recurrent_RS_mib": 50.25
        }
      }
    ]
  }
]
```

</details>

## Decision and remaining research

Bereits gemessen: vier CPU-Schichten verlangsamen Decode etwa72,7%, CPU-KV verlagert auch recurrentRS und verlangsamt etwa67,3%. Das sind Kapazitäts-/Latenz-Tradeoffs, kein neuer asynchroner Staging-Gewinn.

**Remaining scope:** Neue Überlappungsvariante braucht echten Transfer-/Compute-Overlap-Patch, gemessene Transfergrenzen und identische Warm-/Cold-Inputs; R13/K06 nicht wiederholen.

**Reopening condition:** Neue Überlappungsvariante braucht echten Transfer-/Compute-Overlap-Patch, gemessene Transfergrenzen und identische Warm-/Cold-Inputs; R13/K06 nicht wiederholen.

**Next action:** Neue Überlappungsvariante braucht echten Transfer-/Compute-Overlap-Patch, gemessene Transfergrenzen und identische Warm-/Cold-Inputs; R13/K06 nicht wiederholen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R374](../experiments/R374.md), [R391](../experiments/R391.md)
