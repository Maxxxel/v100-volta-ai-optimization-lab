# OmniCoder2 9B · cfg-dcd62ae86d4f

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-dcd62ae86d4fd1495269a27c2c0ca5efdbbbadd67dff4db4a7b8fd4d48997644`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

```json
{
  "architecture": null,
  "artifact_sha256": "78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82",
  "family_id": "omni",
  "hf_repository": null,
  "hf_revision": null,
  "name": "OmniCoder2 9B",
  "quantization": "Q6_K",
  "tensor_precision_map": null,
  "variant": null,
  "weight_transformations": {
    "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
    "description": "MTP_BEARING_OR_GRAFTED_GGUF",
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
    "--spec-draft-n-max": "3",
    "--spec-draft-n-min": "1",
    "--spec-type": "draft-mtp"
  },
  "draft_sha256": null,
  "flash_attention_requested": "on",
  "other_explicit_knobs": {
    "GGML_CUDA_GRAPH_OPT": "0"
  },
  "prefix_reuse": null,
  "quantization_calibration": null,
  "speculation_type": "draft-mtp"
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
    "llama-server",
    "--model",
    "[artifact:78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82]",
    "--alias",
    "[session-local value]",
    "--host",
    "[session-local value]",
    "--port",
    "[session-local value]",
    "--no-webui",
    "--offline",
    "--ctx-size",
    "8192",
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
    "on",
    "--cache-type-k",
    "f16",
    "--cache-type-v",
    "f16",
    "--jinja",
    "--chat-template-file",
    "[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
    "--log-verbosity",
    "4",
    "--no-log-prefix",
    "--no-log-timestamps",
    "--spec-type",
    "draft-mtp",
    "--spec-draft-n-max",
    "3",
    "--spec-draft-n-min",
    "1",
    "--spec-draft-ngl",
    "99",
    "--spec-draft-threads",
    "6",
    "--spec-draft-threads-batch",
    "6"
  ],
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0"
  },
  "exact_private_launch_sha256": "a25b855495c259c47b3c70d227592f523c679367444b6a59efb8e8aa2c95c3e5",
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
| R200 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | MTP_GRAFT_SCREEN_SURVIVES_NEEDS_INDEPENDENT_PRACTICAL_QUALIFICATION | [audit-1e481b9ad01b4b62af21](../audits/audit-1e481b9ad01b4b62af21.md) |

## Immutable full profile and measurements

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-f5074ef22f9e5c0a496caa6a749d6cb3561c4e0c84e3b70b7c96c1f3e29dd84f",
      "audit_hash": "1e481b9ad01b4b62af2188084d18fbdb74e9314be9c8f420351627f726bfd63f",
      "audit_id": "audit-1e481b9ad01b4b62af21",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R200",
      "lab_metrics": {
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
      },
      "model_family_id": "omni",
      "model_name": "OmniCoder2 9B",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-dcd62ae86d4fd1495269a27c2c0ca5efdbbbadd67dff4db4a7b8fd4d48997644",
      "scientific_status": "MTP_GRAFT_SCREEN_SURVIVES_NEEDS_INDEPENDENT_PRACTICAL_QUALIFICATION"
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
      "artifact_sha256": "78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82",
      "family_id": "omni",
      "hf_repository": null,
      "hf_revision": null,
      "name": "OmniCoder2 9B",
      "quantization": "Q6_K",
      "tensor_precision_map": null,
      "variant": null,
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "MTP_BEARING_OR_GRAFTED_GGUF",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-92d8d830b5d4c82e11f1a0afb2d1715975fbd14b09533982f39004187af877fd",
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
        "--spec-draft-n-max": "3",
        "--spec-draft-n-min": "1",
        "--spec-type": "draft-mtp"
      },
      "draft_sha256": null,
      "flash_attention_requested": "on",
      "other_explicit_knobs": {
        "GGML_CUDA_GRAPH_OPT": "0"
      },
      "prefix_reuse": null,
      "quantization_calibration": null,
      "speculation_type": "draft-mtp"
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
    "runtime_configuration_id": "cfg-dcd62ae86d4fd1495269a27c2c0ca5efdbbbadd67dff4db4a7b8fd4d48997644",
    "schema_version": 1,
    "source_plan_sha256": "3ac836e9c87346a99be86370d3c08bdf82215e94327c3e0ee8d70282ff1a5b39",
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:78af5105675a93f2909d625288a87be86ceef620985ab255f72dc028e0290e82]",
        "--alias",
        "[session-local value]",
        "--host",
        "[session-local value]",
        "--port",
        "[session-local value]",
        "--no-webui",
        "--offline",
        "--ctx-size",
        "8192",
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
        "on",
        "--cache-type-k",
        "f16",
        "--cache-type-v",
        "f16",
        "--jinja",
        "--chat-template-file",
        "[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
        "--log-verbosity",
        "4",
        "--no-log-prefix",
        "--no-log-timestamps",
        "--spec-type",
        "draft-mtp",
        "--spec-draft-n-max",
        "3",
        "--spec-draft-n-min",
        "1",
        "--spec-draft-ngl",
        "99",
        "--spec-draft-threads",
        "6",
        "--spec-draft-threads-batch",
        "6"
      ],
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0"
      },
      "exact_private_launch_sha256": "a25b855495c259c47b3c70d227592f523c679367444b6a59efb8e8aa2c95c3e5",
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
