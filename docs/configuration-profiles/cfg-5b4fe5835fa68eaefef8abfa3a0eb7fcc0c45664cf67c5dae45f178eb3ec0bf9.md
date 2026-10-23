# Gemma4 12B IT QAT · cfg-5b4fe5835fa6

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-5b4fe5835fa68eaefef8abfa3a0eb7fcc0c45664cf67c5dae45f178eb3ec0bf9`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

```json
{
  "architecture": null,
  "artifact_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b",
  "family_id": "gemma4",
  "hf_repository": "google/gemma-4-12B-it-qat-q4_0-gguf",
  "hf_revision": "29d097773436b69ff9feafd636ab4cf873786537",
  "name": "Gemma4 12B IT QAT",
  "quantization": "Q4_0",
  "tensor_precision_map": null,
  "variant": "official_QAT_fast_T1_P095_K64_ctx32K_native_functions256",
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
  "HBM_conversion_weight_cache_limit_mib": "0",
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
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
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
  "VRAM_budget_mib": 14336,
  "batch": "2048",
  "chat_template_sha256": "ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4",
  "context": "32768",
  "execution_deadline_s": 800,
  "max_output": 256,
  "microbatch": "512",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": {
    "min_p": 0.0,
    "presence_penalty": 0.0,
    "repeat_penalty": 1.0,
    "temperature": 1.0,
    "top_k": 64,
    "top_p": 0.95
  },
  "thinking_reasoning_requested": "off",
  "tokenizer_identity": null
}
```

## Ordered startup parameters

```json
{
  "argv": [
    "llama-server",
    "--model",
    "[artifact:93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b]",
    "--alias",
    "[session-local value]",
    "--host",
    "[session-local value]",
    "--port",
    "[session-local value]",
    "--no-webui",
    "--offline",
    "--ctx-size",
    "32768",
    "--parallel",
    "1",
    "--n-gpu-layers",
    "99",
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
    "--cache-reuse",
    "0",
    "--no-cache-idle-slots",
    "--reasoning",
    "off",
    "--no-reasoning-preserve",
    "--load-mode",
    "mmap",
    "--flash-attn",
    "auto",
    "--cache-type-k",
    "f16",
    "--cache-type-v",
    "f16",
    "--jinja",
    "--chat-template-file",
    "[artifact:bb793ca4bf45ea99eae6c39b934cee094b23d4219ac8c8b4727efd98f72d9824]",
    "--log-verbosity",
    "4",
    "--no-log-prefix",
    "--no-log-timestamps",
    "--spec-type",
    "none"
  ],
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
  },
  "exact_private_launch_sha256": "7ea67d136cb54d768ce6db2c5c41ee9db64ba9e26731cf6bc1891a3a01e19903",
  "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
  "redacted_argument_positions": [
    0,
    2,
    4,
    6,
    8,
    47
  ]
}
```

## Results and original audits

| Experiment | Benchmark / scope | Success | Wall s | GPU J / success | Peak VRAM MiB | Original audits |
| --- | --- | --- | --- | --- | --- | --- |

Separate benchmark qualification audits: 

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R431 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | GEMMA32K_NEW_CASE_CAPACITY_VALIDATION_PASSED_SCOPE_ONLY | [audit-cd8eb8e97cb00d82a151](../audits/audit-cd8eb8e97cb00d82a151.md) |

## Immutable full profile and measurements

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-9b363bf680b98966587a3477c997552b9ebb4cc4db9dda897f0b88b6b77c209f",
      "audit_hash": "cd8eb8e97cb00d82a151afd35bd6e0d38cbd6e8eac1eadbaecebfa8baf450c80",
      "audit_id": "audit-cd8eb8e97cb00d82a151",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R431",
      "lab_metrics": {
        "actual_GPU_execution": true,
        "actual_generation_requests": 16,
        "context_profile_token_ranges": {
          "validation": {
            "maximum_tokens": 29490,
            "minimum_tokens": 29119
          }
        },
        "context_tokens": 32768,
        "full_12_semantic_score_claimed": true,
        "gpu_energy_j_approx": 72487.35421607949,
        "gpu_j_per_success": 6589.759474189044,
        "model_starts": 1,
        "observed_cases": 12,
        "peak_device_vram_mib": 8526.5,
        "planned_cases": 12,
        "scopes": {
          "validation": {
            "full12": true,
            "gpu_energy_j_approx": 72487.35421607949,
            "gpu_j_per_success": 6589.759474189044,
            "observed": 12,
            "planned": 12,
            "solved": 11,
            "wall_s": 266.1359924
          }
        },
        "solved": 11,
        "wall_s": 266.1359924
      },
      "model_family_id": "gemma4",
      "model_name": "Gemma4 12B IT QAT",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-5b4fe5835fa68eaefef8abfa3a0eb7fcc0c45664cf67c5dae45f178eb3ec0bf9",
      "scientific_status": "GEMMA32K_NEW_CASE_CAPACITY_VALIDATION_PASSED_SCOPE_ONLY"
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
      "artifact_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b",
      "family_id": "gemma4",
      "hf_repository": "google/gemma-4-12B-it-qat-q4_0-gguf",
      "hf_revision": "29d097773436b69ff9feafd636ab4cf873786537",
      "name": "Gemma4 12B IT QAT",
      "quantization": "Q4_0",
      "tensor_precision_map": null,
      "variant": "official_QAT_fast_T1_P095_K64_ctx32K_native_functions256",
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-b4898c643e7d80e027b1234ff16b0aefd109c74e29b1fef6a3c3321ce6c13c80",
    "optimizations": {
      "GDN_state_changes": null,
      "HBM_conversion_weight_cache_limit_mib": "0",
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
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
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
      "VRAM_budget_mib": 14336,
      "batch": "2048",
      "chat_template_sha256": "ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4",
      "context": "32768",
      "execution_deadline_s": 800,
      "max_output": 256,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": {
        "min_p": 0.0,
        "presence_penalty": 0.0,
        "repeat_penalty": 1.0,
        "temperature": 1.0,
        "top_k": 64,
        "top_p": 0.95
      },
      "thinking_reasoning_requested": "off",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-5b4fe5835fa68eaefef8abfa3a0eb7fcc0c45664cf67c5dae45f178eb3ec0bf9",
    "schema_version": 1,
    "source_plan_sha256": "1712592a47c05ef398bdf9acf30ee365b78fb402f952cc1c7283fac6014c6955",
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b]",
        "--alias",
        "[session-local value]",
        "--host",
        "[session-local value]",
        "--port",
        "[session-local value]",
        "--no-webui",
        "--offline",
        "--ctx-size",
        "32768",
        "--parallel",
        "1",
        "--n-gpu-layers",
        "99",
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
        "--cache-reuse",
        "0",
        "--no-cache-idle-slots",
        "--reasoning",
        "off",
        "--no-reasoning-preserve",
        "--load-mode",
        "mmap",
        "--flash-attn",
        "auto",
        "--cache-type-k",
        "f16",
        "--cache-type-v",
        "f16",
        "--jinja",
        "--chat-template-file",
        "[artifact:bb793ca4bf45ea99eae6c39b934cee094b23d4219ac8c8b4727efd98f72d9824]",
        "--log-verbosity",
        "4",
        "--no-log-prefix",
        "--no-log-timestamps",
        "--spec-type",
        "none"
      ],
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
      },
      "exact_private_launch_sha256": "7ea67d136cb54d768ce6db2c5c41ee9db64ba9e26731cf6bc1891a3a01e19903",
      "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
      "redacted_argument_positions": [
        0,
        2,
        4,
        6,
        8,
        47
      ]
    }
  },
  "runs": []
}
```
