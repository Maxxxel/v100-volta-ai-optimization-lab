# LFM2.5 8B A1B · cfg-8bfe42a9350f

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-8bfe42a9350f4d8844e78fde74e71eea4caceca9fdb3280fb2a3aabbce5aa9b3`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "architecture": null,
  "artifact_sha256": "7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6",
  "family_id": "lfm25_8b_a1b_q6",
  "hf_repository": "LiquidAI/LFM2.5-8B-A1B-GGUF",
  "hf_revision": "49c14831707011e64d70b2ebd8462ba08d608434",
  "name": "lfm25_8b_a1b_q6",
  "quantization": "NOT MEASURED",
  "tensor_precision_map": null,
  "variant": "official_Q6_native_T02_K80_repeat105_2048",
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
  "flash_attention_requested": "on",
  "other_explicit_knobs": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
  },
  "prefix_reuse": null,
  "quantization_calibration": null,
  "speculation_type": "none"
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
  "chat_template_sha256": "c5b67247c9f736f6c40eaa91ae1ef27dc67f5b041eedaadb97a1bea5030fb0ff",
  "context": "8192",
  "execution_deadline_s": 840,
  "max_output": 2048,
  "microbatch": "512",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": {
    "repeat_penalty": 1.05,
    "temperature": 0.2,
    "top_k": 80
  },
  "thinking_reasoning_requested": "on",
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
    "[artifact:7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6]",
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
    "on",
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
    "[artifact:ccc1313fcd230362eff59f61ef19bfcc9e1c676821500c62ccffed543687500a]",
    "--log-verbosity",
    "4",
    "--no-log-prefix",
    "--no-log-timestamps",
    "--spec-type",
    "none",
    "--reasoning-format",
    "deepseek"
  ],
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
  },
  "exact_private_launch_sha256": "711122d35da8f9ca80d2ca4da72df41da287d2f62e271962c5d8f71fd45e4863",
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
| R418 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | PARTIAL_CONTROLLER_LITERAL_PROMPT_ASSERTION_NOT_MODEL_FAILURE | [audit-40189731a53dcdc5b414](../audits/audit-40189731a53dcdc5b414.md) |

## Immutable full profile and measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-8843c1085b4d109a34d1f271433f152f12e4c36bc9de8c152fb3dddeb7e08899",
      "audit_hash": "40189731a53dcdc5b414a5a52605595b30cae98015dee9d1733ad7e3bfa7d582",
      "audit_id": "audit-40189731a53dcdc5b414",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R418",
      "lab_metrics": {
        "actual_generation_requests": 4,
        "model_starts": 1,
        "observed_original_QA_cases": 3,
        "original12_full_score_claimed": false,
        "peak_device_vram_mib": 7432.5
      },
      "model_family_id": "lfm25_8b_a1b_q6",
      "model_name": "lfm25_8b_a1b_q6",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-8bfe42a9350f4d8844e78fde74e71eea4caceca9fdb3280fb2a3aabbce5aa9b3",
      "scientific_status": "PARTIAL_CONTROLLER_LITERAL_PROMPT_ASSERTION_NOT_MODEL_FAILURE"
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
      "artifact_sha256": "7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6",
      "family_id": "lfm25_8b_a1b_q6",
      "hf_repository": "LiquidAI/LFM2.5-8B-A1B-GGUF",
      "hf_revision": "49c14831707011e64d70b2ebd8462ba08d608434",
      "name": "lfm25_8b_a1b_q6",
      "quantization": "NOT MEASURED",
      "tensor_precision_map": null,
      "variant": "official_Q6_native_T02_K80_repeat105_2048",
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-85f6f0945eea822c99d3d8627ef0ec8f41c0fa815fecf3b3f2bffb977039033b",
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
      "flash_attention_requested": "on",
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
      "chat_template_sha256": "c5b67247c9f736f6c40eaa91ae1ef27dc67f5b041eedaadb97a1bea5030fb0ff",
      "context": "8192",
      "execution_deadline_s": 840,
      "max_output": 2048,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": {
        "repeat_penalty": 1.05,
        "temperature": 0.2,
        "top_k": 80
      },
      "thinking_reasoning_requested": "on",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-8bfe42a9350f4d8844e78fde74e71eea4caceca9fdb3280fb2a3aabbce5aa9b3",
    "schema_version": 1,
    "source_plan_sha256": "013c54184bbe7ee12d146967724e7e9695eea85019b7833e1a3ed13e00b014c5",
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6]",
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
        "on",
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
        "[artifact:ccc1313fcd230362eff59f61ef19bfcc9e1c676821500c62ccffed543687500a]",
        "--log-verbosity",
        "4",
        "--no-log-prefix",
        "--no-log-timestamps",
        "--spec-type",
        "none",
        "--reasoning-format",
        "deepseek"
      ],
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
      },
      "exact_private_launch_sha256": "711122d35da8f9ca80d2ca4da72df41da287d2f62e271962c5d8f71fd45e4863",
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
