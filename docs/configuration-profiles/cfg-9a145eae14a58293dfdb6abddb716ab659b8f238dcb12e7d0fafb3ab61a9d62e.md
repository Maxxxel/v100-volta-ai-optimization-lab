# OmniCoder 9B · cfg-9a145eae14a5

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-9a145eae14a58293dfdb6abddb716ab659b8f238dcb12e7d0fafb3ab61a9d62e`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

```json
{
  "architecture": null,
  "artifact_sha256": "4043e6d2eff5faeb3b49853ec90abefa49190cc7171787497420198ef2bace5d",
  "family_id": "omnicoder2",
  "hf_repository": null,
  "hf_revision": null,
  "name": "omnicoder2",
  "quantization": "NOT MEASURED",
  "tensor_precision_map": null,
  "variant": null,
  "weight_transformations": {
    "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
    "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
    "proof": null
  }
}
```

## Engine and backend

```json
{
  "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
  "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
  "cuda_version": null,
  "driver_version": null,
  "executed_kernel_backend_path": null,
  "fork_repository": null,
  "ggml_backend_version": null,
  "git_commit": null,
  "kernel_library_file": "libggml-cuda.so.0.26.0",
  "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
  "name": "llama.cpp-compatible",
  "patches": null,
  "version": null
}
```

## Optimizations

```json
{
  "GDN_state_changes": null,
  "HBM_conversion_weight_cache_limit_mib": null,
  "KV_precision": {
    "k": "f16",
    "v": "f16"
  },
  "cuda_graphs": {
    "actual_capture_replay": null,
    "disable_knob": null,
    "optimization_knob": "0"
  },
  "draft_head_or_model": null,
  "draft_parameters": {
    "--spec-type": "none"
  },
  "draft_sha256": null,
  "flash_attention_requested": "auto",
  "other_explicit_knobs": {
    "GGML_CUDA_GRAPH_OPT": "0"
  },
  "prefix_reuse": null,
  "quantization_calibration": null,
  "speculation_type": "none"
}
```

## Runtime and sampler

```json
{
  "CPU_budget": null,
  "CPU_threads": "6",
  "GPU_offload": "99",
  "RAM_budget": null,
  "VRAM_budget_mib": null,
  "batch": "2048",
  "chat_template_sha256": null,
  "context": "8192",
  "execution_deadline_s": null,
  "max_output": null,
  "microbatch": "512",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": null,
  "thinking_reasoning_requested": "off",
  "tokenizer_identity": null
}
```

## Ordered startup parameters

```json
{
  "argv": [
    "python3",
    "[artifact:5faeb2abd1e795ad3e33f611705f7164ac499d8d6547d1c30fa389cd018de10a]",
    "[artifact:08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54]",
    "--model",
    "[artifact:4043e6d2eff5faeb3b49853ec90abefa49190cc7171787497420198ef2bace5d]",
    "--alias",
    "[session-local value]",
    "--ctx-size",
    "8192",
    "--n-gpu-layers",
    "99",
    "--parallel",
    "1",
    "--host",
    "[session-local value]",
    "--port",
    "[session-local value]",
    "--jinja",
    "--chat-template-file",
    "[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
    "--threads",
    "6",
    "--threads-batch",
    "6",
    "--batch-size",
    "2048",
    "--ubatch-size",
    "512",
    "--seed",
    "1001",
    "--ctx-checkpoints",
    "2",
    "--cache-ram",
    "0",
    "--no-cache-idle-slots",
    "--reasoning",
    "off",
    "--no-reasoning-preserve",
    "--verbosity",
    "4",
    "--flash-attn",
    "auto",
    "--cache-type-k",
    "f16",
    "--cache-type-v",
    "f16",
    "--load-mode",
    "mmap",
    "--spec-type",
    "none"
  ],
  "environment": {},
  "exact_private_launch_sha256": "c6f15422ebdea58dbff91ddd3d12ae9992c65b8c9f7914161d6304531cd53223",
  "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
  "redacted_argument_positions": [
    0,
    1,
    2,
    4,
    6,
    14,
    16,
    19
  ]
}
```

## Verified engine source revision

The original profile remains immutable. This matched build receipt supplies a source-base revision plus local patch lineage, not a reconstructed upstream release tag.

```json
{
  "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
  "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
  "comparison_upstream_commit": "ea0c4c2c85fb183ec0fbd30a1af4e4275a18a064",
  "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
  "local_variant": "local patches",
  "patch_sha256": "69fd43355a882451812995e5cfb6eae8af2c01224c0c3d41ef75c73fbd6e8b45",
  "release_version": null,
  "source_base_commit": "097cf33d9499b1eade67d51e16d7c75427e7b267",
  "source_inputs_sha256": "9e3f8d55281b16afdd88a51c1e51f2c658ae1958caf88fdf1537601b35245213",
  "source_repository": "https://github.com/ggml-org/llama.cpp",
  "source_version_label": "097cf33 + local patches"
}
```

[audit-ad26886527c71fef3b59](../audits/audit-ad26886527c71fef3b59.md)

## Results and original audits

| Experiment | Benchmark / scope | Success | Wall s | GPU J / success | Peak VRAM MiB | Original audits |
| --- | --- | --- | --- | --- | --- | --- |

Separate benchmark qualification audits: 

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R132 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | MATCHED_OMNICODER2_Q4_ORIGINAL_NATIVE_A0_CALIBRATED | [audit-cc4a0b8610c091844255](../audits/audit-cc4a0b8610c091844255.md) |

## Immutable full profile and measurements

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-30a59af102e259a0c52f6826960b703533fdf22225ca685a66b75d2058be93ce",
      "audit_hash": "cc4a0b8610c0918442555b436714cf8f67cdbd27abf7a8e02a7cd0c0ab391363",
      "audit_id": "audit-cc4a0b8610c091844255",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R132",
      "lab_metrics": {
        "actual_generation_requests": 34,
        "original12": [
          {
            "e2e_s": 0.15884886,
            "gpu_energy_j": 31.825402663636876,
            "grades": {
              "format_pass": true,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.148424993,
            "gpu_energy_j": 30.294757841342722,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": false
            }
          },
          {
            "e2e_s": 0.526417463,
            "gpu_energy_j": 130.36926963600024,
            "grades": {
              "format_pass": true,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.306907579,
            "gpu_energy_j": 71.81202539120457,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": false
            }
          },
          {
            "e2e_s": 0.253567405,
            "gpu_energy_j": 56.28443921443843,
            "grades": {
              "format_pass": true,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.398177521,
            "gpu_energy_j": 88.27877764478977,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 1.021011086,
            "gpu_energy_j": 265.5898487906164,
            "grades": {
              "format_pass": true,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.350909329,
            "gpu_energy_j": 82.3299952812138,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.228650258,
            "gpu_energy_j": 51.10443234643959,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": false
            }
          },
          {
            "e2e_s": 0.207737731,
            "gpu_energy_j": 46.45054445205362,
            "grades": {
              "format_pass": true,
              "raw_preserved": true,
              "semantic_pass": true
            }
          },
          {
            "e2e_s": 0.496860176,
            "gpu_energy_j": 120.80617875813817,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": false
            }
          },
          {
            "e2e_s": 0.314075031,
            "gpu_energy_j": 73.8160339502637,
            "grades": {
              "format_pass": false,
              "raw_preserved": true,
              "semantic_pass": false
            }
          }
        ],
        "peak_process_vram_mib": 5714
      },
      "model_family_id": "omnicoder2",
      "model_name": "omnicoder2",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-9a145eae14a58293dfdb6abddb716ab659b8f238dcb12e7d0fafb3ab61a9d62e",
      "scientific_status": "MATCHED_OMNICODER2_Q4_ORIGINAL_NATIVE_A0_CALIBRATED"
    }
  ],
  "profile": {
    "engine": {
      "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
      "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
      "cuda_version": null,
      "driver_version": null,
      "executed_kernel_backend_path": null,
      "fork_repository": null,
      "ggml_backend_version": null,
      "git_commit": null,
      "kernel_library_file": "libggml-cuda.so.0.26.0",
      "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
      "name": "llama.cpp-compatible",
      "patches": null,
      "version": null
    },
    "evaluation_exposure": "Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.",
    "incomplete_identity_run": null,
    "model": {
      "architecture": null,
      "artifact_sha256": "4043e6d2eff5faeb3b49853ec90abefa49190cc7171787497420198ef2bace5d",
      "family_id": "omnicoder2",
      "hf_repository": null,
      "hf_revision": null,
      "name": "omnicoder2",
      "quantization": "NOT MEASURED",
      "tensor_precision_map": null,
      "variant": null,
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-b01031d3595ae33ab120d5d1ab471b9560d53d8f21c1aa7361b4baf45fae91ed",
    "optimizations": {
      "GDN_state_changes": null,
      "HBM_conversion_weight_cache_limit_mib": null,
      "KV_precision": {
        "k": "f16",
        "v": "f16"
      },
      "cuda_graphs": {
        "actual_capture_replay": null,
        "disable_knob": null,
        "optimization_knob": "0"
      },
      "draft_head_or_model": null,
      "draft_parameters": {
        "--spec-type": "none"
      },
      "draft_sha256": null,
      "flash_attention_requested": "auto",
      "other_explicit_knobs": {
        "GGML_CUDA_GRAPH_OPT": "0"
      },
      "prefix_reuse": null,
      "quantization_calibration": null,
      "speculation_type": "none"
    },
    "provenance_status": "KNOWN_FIELDS_ONLY; null means NOT MEASURED",
    "runtime": {
      "CPU_budget": null,
      "CPU_threads": "6",
      "GPU_offload": "99",
      "RAM_budget": null,
      "VRAM_budget_mib": null,
      "batch": "2048",
      "chat_template_sha256": null,
      "context": "8192",
      "execution_deadline_s": null,
      "max_output": null,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": null,
      "thinking_reasoning_requested": "off",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-9a145eae14a58293dfdb6abddb716ab659b8f238dcb12e7d0fafb3ab61a9d62e",
    "schema_version": 1,
    "source_plan_sha256": "4ab833427f4a002c4a4af0585538e79141188042810c0a2ca650e0c524453157",
    "start_parameters": {
      "argv": [
        "python3",
        "[artifact:5faeb2abd1e795ad3e33f611705f7164ac499d8d6547d1c30fa389cd018de10a]",
        "[artifact:08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54]",
        "--model",
        "[artifact:4043e6d2eff5faeb3b49853ec90abefa49190cc7171787497420198ef2bace5d]",
        "--alias",
        "[session-local value]",
        "--ctx-size",
        "8192",
        "--n-gpu-layers",
        "99",
        "--parallel",
        "1",
        "--host",
        "[session-local value]",
        "--port",
        "[session-local value]",
        "--jinja",
        "--chat-template-file",
        "[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
        "--threads",
        "6",
        "--threads-batch",
        "6",
        "--batch-size",
        "2048",
        "--ubatch-size",
        "512",
        "--seed",
        "1001",
        "--ctx-checkpoints",
        "2",
        "--cache-ram",
        "0",
        "--no-cache-idle-slots",
        "--reasoning",
        "off",
        "--no-reasoning-preserve",
        "--verbosity",
        "4",
        "--flash-attn",
        "auto",
        "--cache-type-k",
        "f16",
        "--cache-type-v",
        "f16",
        "--load-mode",
        "mmap",
        "--spec-type",
        "none"
      ],
      "environment": {},
      "exact_private_launch_sha256": "c6f15422ebdea58dbff91ddd3d12ae9992c65b8c9f7914161d6304531cd53223",
      "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
      "redacted_argument_positions": [
        0,
        1,
        2,
        4,
        6,
        14,
        16,
        19
      ]
    }
  },
  "runs": []
}
```
