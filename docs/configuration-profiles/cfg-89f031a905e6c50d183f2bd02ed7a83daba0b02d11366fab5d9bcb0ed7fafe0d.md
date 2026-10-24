# Qwen3.5 9B · cfg-89f031a905e6

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-89f031a905e6c50d183f2bd02ed7a83daba0b02d11366fab5d9bcb0ed7fafe0d`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "architecture": null,
  "artifact_sha256": "02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d",
  "family_id": "q35",
  "hf_repository": null,
  "hf_revision": null,
  "name": "Qwen3.5 9B",
  "quantization": "Q4_K_M",
  "tensor_precision_map": null,
  "variant": null,
  "weight_transformations": {
    "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
    "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
    "proof": null
  }
}
```

</details>

## Engine and backend

<details class="lab-evidence"><summary>Structured evidence</summary>

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

</details>

## Optimizations

<details class="lab-evidence"><summary>Structured evidence</summary>

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
  "draft_parameters": {},
  "draft_sha256": null,
  "flash_attention_requested": "on",
  "other_explicit_knobs": {
    "GGML_CUDA_GRAPH_OPT": "0"
  },
  "prefix_reuse": false,
  "quantization_calibration": null,
  "speculation_type": null
}
```

</details>

## Runtime and sampler

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "CPU_budget": null,
  "CPU_threads": "6",
  "GPU_offload": "99",
  "RAM_budget": null,
  "VRAM_budget_mib": 14336,
  "batch": "2048",
  "chat_template_sha256": null,
  "context": "8192",
  "execution_deadline_s": 840,
  "max_output": null,
  "microbatch": "512",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": null,
  "thinking_reasoning_requested": "off",
  "tokenizer_identity": null
}
```

</details>

## Ordered startup parameters

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "argv": [
    "llama-server",
    "--model",
    "[artifact:02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d]",
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
    "--no-log-timestamps"
  ],
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0"
  },
  "exact_private_launch_sha256": "cb3643b0ec38e5f2b73efdf7b8b84b81444cc19559f76632725da4a4589c0417",
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

</details>

## Verified engine source revision

The original profile remains immutable. This matched build receipt supplies a source-base revision plus local patch lineage, not a reconstructed upstream release tag.

<details class="lab-evidence"><summary>Structured evidence</summary>

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

</details>

[audit-ad26886527c71fef3b59](../audits/audit-ad26886527c71fef3b59.md)

## Results and original audits

| Experiment | Benchmark / scope | Success | Wall s | GPU J / success | Peak VRAM MiB | Original audits |
| --- | --- | --- | --- | --- | --- | --- |

Separate benchmark qualification audits:

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R228 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | QWEN35_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL | [audit-f48de8313838adc8b3b4](../audits/audit-f48de8313838adc8b3b4.md) |

## Immutable full profile and measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-9f4e30cf32584f4daf44457dc89d3aed5ed9e3abf61d085e5f9cf483c6acfc4d",
      "audit_hash": "f48de8313838adc8b3b4940143dd90a7822a1e350aca33f67feaafb6318cebf3",
      "audit_id": "audit-f48de8313838adc8b3b4",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R228",
      "lab_metrics": {
        "actual_generation_requests": 102,
        "full18_score_claimed": true,
        "gpu_energy_j_approx": 56164.790740286684,
        "gpu_j_per_success": 7020.5988425358355,
        "model_requests": 98,
        "model_starts": 1,
        "observed_tasks": 18,
        "peak_device_vram_mib": 5956.5,
        "solved": 8
      },
      "model_family_id": "q35",
      "model_name": "Qwen3.5 9B",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-89f031a905e6c50d183f2bd02ed7a83daba0b02d11366fab5d9bcb0ed7fafe0d",
      "scientific_status": "QWEN35_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL"
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
      "artifact_sha256": "02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d",
      "family_id": "q35",
      "hf_repository": null,
      "hf_revision": null,
      "name": "Qwen3.5 9B",
      "quantization": "Q4_K_M",
      "tensor_precision_map": null,
      "variant": null,
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-746fdcd66312ce53203c34a7952cbce807c07699299bb6f495c758500e947c06",
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
      "draft_parameters": {},
      "draft_sha256": null,
      "flash_attention_requested": "on",
      "other_explicit_knobs": {
        "GGML_CUDA_GRAPH_OPT": "0"
      },
      "prefix_reuse": false,
      "quantization_calibration": null,
      "speculation_type": null
    },
    "provenance_status": "KNOWN_FIELDS_ONLY; null means NOT MEASURED",
    "runtime": {
      "CPU_budget": null,
      "CPU_threads": "6",
      "GPU_offload": "99",
      "RAM_budget": null,
      "VRAM_budget_mib": 14336,
      "batch": "2048",
      "chat_template_sha256": null,
      "context": "8192",
      "execution_deadline_s": 840,
      "max_output": null,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": null,
      "thinking_reasoning_requested": "off",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-89f031a905e6c50d183f2bd02ed7a83daba0b02d11366fab5d9bcb0ed7fafe0d",
    "schema_version": 1,
    "source_plan_sha256": "fa8712f46e5cc987775cecd5fe3662414cd31b252b614f51c550946f5f704cb1",
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d]",
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
        "--no-log-timestamps"
      ],
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0"
      },
      "exact_private_launch_sha256": "cb3643b0ec38e5f2b73efdf7b8b84b81444cc19559f76632725da4a4589c0417",
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

</details>
