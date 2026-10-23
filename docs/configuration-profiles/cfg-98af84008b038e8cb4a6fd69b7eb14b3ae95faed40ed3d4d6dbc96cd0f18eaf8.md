# OmniCoder2 9B · cfg-98af84008b03

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-98af84008b038e8cb4a6fd69b7eb14b3ae95faed40ed3d4d6dbc96cd0f18eaf8`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

```json
{
  "architecture": null,
  "artifact_sha256": "b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b",
  "family_id": "omni",
  "hf_repository": null,
  "hf_revision": null,
  "name": "OmniCoder2 9B",
  "quantization": "Q6_K",
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
  "build_id": "r235-adaptive-draft",
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
  "draft_head_or_model": "Qwen3.5-9B-MTP-ONLY-Q6_K.gguf",
  "draft_parameters": {
    "--spec-draft-n-max": "3",
    "--spec-draft-n-min": "1",
    "--spec-type": "draft-mtp"
  },
  "draft_sha256": "a794337c734d5536b150dbed898d7c3b406fb6f34dc65f53f5309e6fa4efb623",
  "flash_attention_requested": "on",
  "other_explicit_knobs": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
  },
  "prefix_reuse": false,
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
  "execution_deadline_s": 900,
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
    "[artifact:b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b]",
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
    "6",
    "--spec-draft-model",
    "[artifact:a794337c734d5536b150dbed898d7c3b406fb6f34dc65f53f5309e6fa4efb623]"
  ],
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
  },
  "exact_private_launch_sha256": "478fbfa3934307244f8a3c64d8ee6232f1ed2737cf36e6670913833378bbeba7",
  "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
  "redacted_argument_positions": [
    0,
    2,
    4,
    6,
    8,
    47,
    65
  ]
}
```

## Results and original audits

| Experiment | Benchmark / scope | Success | Wall s | GPU J / success | Peak VRAM MiB | Original audits |
| --- | --- | --- | --- | --- | --- | --- |

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R236 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | ADAPTIVE1TO3_AGENT_SCREEN_NOT_QUALIFIED | [audit-3bbcbd54e7cb734a5ce0](../audits/audit-3bbcbd54e7cb734a5ce0.md) |

## Immutable full profile and measurements

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-af94bfa0d1da6a952af33479a82171661a3e58eb593a5f3ed18472652cb0950e",
      "audit_hash": "3bbcbd54e7cb734a5ce0207189602a9cf624daf07109f3b22cb39717a9738e90",
      "audit_id": "audit-3bbcbd54e7cb734a5ce0",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R236",
      "lab_metrics": {
        "full18_score_claimed": true,
        "gpu_energy_j_approx": 44182.21261186184,
        "model_requests": 90,
        "model_starts": 1,
        "observed_tasks": 18,
        "original12_nonregression": true,
        "peak_device_vram_mib": 9000.5,
        "solved": 13
      },
      "model_family_id": "omni",
      "model_name": "OmniCoder2 9B",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-98af84008b038e8cb4a6fd69b7eb14b3ae95faed40ed3d4d6dbc96cd0f18eaf8",
      "scientific_status": "ADAPTIVE1TO3_AGENT_SCREEN_NOT_QUALIFIED"
    }
  ],
  "profile": {
    "engine": {
      "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
      "build_id": "r235-adaptive-draft",
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
      "artifact_sha256": "b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b",
      "family_id": "omni",
      "hf_repository": null,
      "hf_revision": null,
      "name": "OmniCoder2 9B",
      "quantization": "Q6_K",
      "tensor_precision_map": null,
      "variant": null,
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-b7fe1fe79de3c5514edb2214ee88101a21451eae1d2ebb94c9c1489387f8a445",
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
      "draft_head_or_model": "Qwen3.5-9B-MTP-ONLY-Q6_K.gguf",
      "draft_parameters": {
        "--spec-draft-n-max": "3",
        "--spec-draft-n-min": "1",
        "--spec-type": "draft-mtp"
      },
      "draft_sha256": "a794337c734d5536b150dbed898d7c3b406fb6f34dc65f53f5309e6fa4efb623",
      "flash_attention_requested": "on",
      "other_explicit_knobs": {
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
      },
      "prefix_reuse": false,
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
      "execution_deadline_s": 900,
      "max_output": null,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": null,
      "thinking_reasoning_requested": "off",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-98af84008b038e8cb4a6fd69b7eb14b3ae95faed40ed3d4d6dbc96cd0f18eaf8",
    "schema_version": 1,
    "source_plan_sha256": "c0c1e25a8feb026b02ba91da2095e34bcc62833ed85f0f6a57b79002a72d1d14",
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b]",
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
        "6",
        "--spec-draft-model",
        "[artifact:a794337c734d5536b150dbed898d7c3b406fb6f34dc65f53f5309e6fa4efb623]"
      ],
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
      },
      "exact_private_launch_sha256": "478fbfa3934307244f8a3c64d8ee6232f1ed2737cf36e6670913833378bbeba7",
      "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
      "redacted_argument_positions": [
        0,
        2,
        4,
        6,
        8,
        47,
        65
      ]
    }
  },
  "runs": []
}
```
