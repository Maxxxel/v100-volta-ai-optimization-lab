# Gemma4 12B IT QAT · cfg-14c6c5ce741a

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-14c6c5ce741ace10eeb28ee482973e7cf91c016ba3aab8120fdcd5eb1acec059`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

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
  "variant": "official_QAT_fast_T1_P095_K64_native_agents1400",
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
  "prefix_reuse": false,
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
  "context": "8192",
  "execution_deadline_s": 840,
  "max_output": 1400,
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
    "auto",
    "--cache-type-k",
    "f16",
    "--cache-type-v",
    "f16",
    "--jinja",
    "--chat-template-file",
    "[artifact:631c146a2c1da52b96fa393b75e2fdc769198e18d52933d2c9d3243060ae5ea1]",
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
  "exact_private_launch_sha256": "be600a3393f692fa246c753ce80ce74bd848a548b45dc3a9f5e419be0cadc07a",
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
| R426 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | GEMMA4_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL | [audit-021cfb8ba15cb4471b11](../audits/audit-021cfb8ba15cb4471b11.md) |

## Immutable full profile and measurements

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-859f4f4389cc99fb1efc5044d07749b6d2b24a49305ad2c8a46cd9d2087e4401",
      "audit_hash": "021cfb8ba15cb4471b111ebcbe44088d2d26d06809f01981d24db6cde1b6f4a5",
      "audit_id": "audit-021cfb8ba15cb4471b11",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R426",
      "lab_metrics": {
        "actual_full_GPU_offload": true,
        "actual_generation_requests": 129,
        "full18_score_claimed": true,
        "gpu_energy_j_approx": 79448.26361013179,
        "gpu_j_per_success": 8827.5848455702,
        "model_requests": 125,
        "model_starts": 1,
        "observed_tasks": 18,
        "peak_device_vram_mib": 8118.5,
        "solved": 9
      },
      "model_family_id": "gemma4",
      "model_name": "Gemma4 12B IT QAT",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-14c6c5ce741ace10eeb28ee482973e7cf91c016ba3aab8120fdcd5eb1acec059",
      "scientific_status": "GEMMA4_AGENT_MODEL_SCREEN_NO_PRACTICAL_WIN_OR_PARTIAL"
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
      "variant": "official_QAT_fast_T1_P095_K64_native_agents1400",
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-ec4bea88be3efa0b31280272b9d85839b91fd90909052b235ab6f6982f4eb1da",
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
      "prefix_reuse": false,
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
      "context": "8192",
      "execution_deadline_s": 840,
      "max_output": 1400,
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
    "runtime_configuration_id": "cfg-14c6c5ce741ace10eeb28ee482973e7cf91c016ba3aab8120fdcd5eb1acec059",
    "schema_version": 1,
    "source_plan_sha256": "bc06f49a06e3fa99d8cc16a1f3c8e91dc2f4ba6aa60405198febff6dd0244d94",
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
        "auto",
        "--cache-type-k",
        "f16",
        "--cache-type-v",
        "f16",
        "--jinja",
        "--chat-template-file",
        "[artifact:631c146a2c1da52b96fa393b75e2fdc769198e18d52933d2c9d3243060ae5ea1]",
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
      "exact_private_launch_sha256": "be600a3393f692fa246c753ce80ce74bd848a548b45dc3a9f5e419be0cadc07a",
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
