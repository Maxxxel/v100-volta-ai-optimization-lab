# GLM-4.7-Flash · cfg-9def619a67b0

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "architecture": null,
  "artifact_sha256": "21d16834f428215926466ce44862fccbd3337008b49ea4ac2f58abdd8ddd1e91",
  "family_id": "glm47_flash",
  "hf_repository": "unsloth/GLM-4.7-Flash-GGUF",
  "hf_revision": "0d32489ecb9db6d2a4fc93bd27ef01519f95474d",
  "name": "GLM-4.7-Flash",
  "quantization": "Q3_K_S",
  "tensor_precision_map": null,
  "variant": "GLM-4.7-Flash",
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

</details>

## Runtime and sampler

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "CPU_budget": null,
  "CPU_scoring_limit_s": 120,
  "CPU_threads": "6",
  "GPU_offload": "99",
  "GPU_wrapper_limit_s": 1440,
  "RAM_budget": null,
  "VRAM_budget_mib": 14336,
  "batch": "2048",
  "benchmark_task_limit_s": 1200,
  "chat_template_sha256": "d63ad536c3c81880043e22ec7fd08db42b4d8fb7c89c7138bc562bfa25281375",
  "context": "8192",
  "execution_deadline_s": 1200,
  "max_output": 4096,
  "microbatch": "512",
  "native_HTTP_timeout_policy": "REMAINING_TASK_TIME",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": {
    "min_p": 0.0,
    "seed": 1001,
    "temperature": 1.0,
    "top_k": 0,
    "top_p": 0.95
  },
  "startup_limit_s": 180,
  "thinking_reasoning_requested": null,
  "timing_scope": "TASK_PHASE_ONLY",
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
    "[artifact:21d16834f428215926466ce44862fccbd3337008b49ea4ac2f58abdd8ddd1e91]",
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
    "[artifact:d63ad536c3c81880043e22ec7fd08db42b4d8fb7c89c7138bc562bfa25281375]",
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
  "environment": {
    "GGML_CUDA_GRAPH_OPT": "0",
    "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0",
    "OMP_NUM_THREADS": "6"
  },
  "exact_private_launch_sha256": "822cc397458db01aa8893a767fea63d104a7e3553cfe27d8935babfb694a2614",
  "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
  "redacted_argument_positions": [
    0,
    2,
    4,
    12,
    14,
    17
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
| R574 | bfcl-v4-parallel-multiple-full200 / FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED | 168/200 | 1038.246775357 | NOT MEASURED | 13716.5 | [audit-d68ff6f2d825024dde4c](../audits/audit-d68ff6f2d825024dde4c.md), [audit-d9785d63f2b201f8ae10](../audits/audit-d9785d63f2b201f8ae10.md), [audit-e4ec23028c58a6695f7d](../audits/audit-e4ec23028c58a6695f7d.md) |

Separate benchmark qualification audits: [audit-e8db2aaaa470124b01cf](../audits/audit-e8db2aaaa470124b01cf.md)

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R574 / 0 | INFERENCE_OBSERVED_IN_BROKER_CAMPAIGN; FULL_BENCHMARK_NOT_IMPLIED | BOUNDED_NATIVE_EXECUTION_OBSERVED | [audit-d9785d63f2b201f8ae10](../audits/audit-d9785d63f2b201f8ae10.md) |

## Additional hash-bound execution evidence

These observations supplement the original immutable profile; they do not assign a release version to an unidentified historical build. Declared plan controls, observed request settings and executed sampler settings remain separate.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "evidence_id": "evidence-1dfc24d77c44992115bf7ee26b478fcf7f945664a38f606d45503ba01c58fe22",
    "fields": {
      "engine.reported_build_number": 0,
      "engine.reported_compiled_CUDA_archs": "700",
      "engine.version_provenance_note": "Pinned historical server log reports build 0 (unknown); no identifiable upstream version or commit. Binary and CUDA-library hashes remain authoritative.",
      "model.architecture": "deepseek2",
      "runtime.native_tool_choice_requested": "auto",
      "runtime.observed_generation_settings.backend_sampling": false,
      "runtime.observed_generation_settings.frequency_penalty": 0.0,
      "runtime.observed_generation_settings.ignore_eos": false,
      "runtime.observed_generation_settings.min_p": 0.0,
      "runtime.observed_generation_settings.mirostat": 0,
      "runtime.observed_generation_settings.mirostat_eta": 0.10000000149011612,
      "runtime.observed_generation_settings.mirostat_tau": 5.0,
      "runtime.observed_generation_settings.n_discard": 0,
      "runtime.observed_generation_settings.n_keep": 0,
      "runtime.observed_generation_settings.n_predict": 4096,
      "runtime.observed_generation_settings.presence_penalty": 0.0,
      "runtime.observed_generation_settings.reasoning_format": "deepseek",
      "runtime.observed_generation_settings.reasoning_in_content": false,
      "runtime.observed_generation_settings.repeat_last_n": 64,
      "runtime.observed_generation_settings.repeat_penalty": 1.0,
      "runtime.observed_generation_settings.seed": 1001,
      "runtime.observed_generation_settings.stream": false,
      "runtime.observed_generation_settings.temperature": 1.0,
      "runtime.observed_generation_settings.top_k": 0,
      "runtime.observed_generation_settings.top_p": 0.949999988079071,
      "runtime.observed_generation_settings.typical_p": 1.0,
      "runtime.observed_request_sampling.min_p": 0.0,
      "runtime.observed_request_sampling.seed": 1001,
      "runtime.observed_request_sampling.temperature": 1.0,
      "runtime.observed_request_sampling.top_k": 0,
      "runtime.observed_request_sampling.top_p": 0.95
    },
    "interpretation": "Additional observations from pinned original execution evidence. Immutable original profile unchanged; reported build identity is not an upstream release. Requested options do not establish effective kernel dispatch.",
    "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
    "sources": [
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "LAUNCH.json",
        "sha256": "7a1b2025ba36fc61df617b40882f75b6cd610ff8fbf35a7b9e744ccc2f9f116e"
      },
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "server.log",
        "sha256": "06121358544ecb3991b4efe89827237eb3bec3d60c4e10197075038ea03f96b4"
      },
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "HTTP_RESULTS.jsonl",
        "sha256": "e3d04398854f4860d2832d8e800e8281f1cbab4e965c1552ffa0c66c07829384"
      }
    ]
  }
]
```

</details>

Evidence metadata: [audit-3445736042f8404217af](../audits/audit-3445736042f8404217af.md)

## Recorded engine timings and energy denominator

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "aggregation": "Rate = sum of recorded token counts / sum of engine timing seconds for the exact task set; excludes startup/warmup. GPU J/output token uses gross case-window GPU energy including prefill. Engine prefill time is not TTFT. No unseen holdout claim.",
    "evidence_id": "measurement-4ca4bd028d86160775c711b7aee22bbc6253e91a742b36121e84fc98cf1261ff",
    "run_id": "run-0e8de51b2454162fbf22814c31d992d06c7c10a200e2aa0664b78c212099ff38",
    "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
    "sources": [
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "LAUNCH.json",
        "sha256": "7a1b2025ba36fc61df617b40882f75b6cd610ff8fbf35a7b9e744ccc2f9f116e"
      },
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "server.log",
        "sha256": "06121358544ecb3991b4efe89827237eb3bec3d60c4e10197075038ea03f96b4"
      },
      {
        "authority_audit_id": "audit-3445736042f8404217af",
        "filename": "HTTP_RESULTS.jsonl",
        "sha256": "e3d04398854f4860d2832d8e800e8281f1cbab4e965c1552ffa0c66c07829384"
      },
      {
        "authority_audit_id": "audit-d68ff6f2d825024dde4c",
        "filename": "AUDIT.json",
        "sha256": "d68ff6f2d825024dde4c54a8c05e65e7a1a98dcd21a80a00d6bbf774eee12cfe"
      }
    ],
    "task_phase_scope": "Recorded audited task phase includes input/template/token preparation between requests; completion-HTTP window sums are separate. Startup/warmup and CPU scoring are excluded from task-phase throughput.",
    "tasks": 200,
    "values": {
      "decode_engine_ms": 938054.161,
      "decode_tok_s": 68.72097868131519,
      "decode_tokens": 64464,
      "prefill_engine_ms": 99064.705,
      "prefill_tok_s": 1081.7071529158645,
      "prefill_tokens": 107159,
      "startup_s": 114.56150525,
      "successful_tasks_per_task_phase_s": 0.16178954890374264,
      "task_phase_s": 1038.385984375
    },
    "wall_sum_s": 1038.246775357
  }
]
```

</details>

## Immutable full profile and measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-6d31d250e173b4e16472a23411e50e25c87f14e9bcb89d7eae6e3baab6e87ef9",
      "audit_hash": "d9785d63f2b201f8ae1081aa86cf3ffdc921e28f4183d42065ec407f1c1f608d",
      "audit_id": "audit-d9785d63f2b201f8ae10",
      "execution_status": "INFERENCE_OBSERVED_IN_BROKER_CAMPAIGN; FULL_BENCHMARK_NOT_IMPLIED",
      "experiment_id": "R574",
      "lab_metrics": {},
      "model_family_id": "glm47_flash",
      "model_name": "GLM-4.7-Flash",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
      "scientific_status": "BOUNDED_NATIVE_EXECUTION_OBSERVED"
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
      "artifact_sha256": "21d16834f428215926466ce44862fccbd3337008b49ea4ac2f58abdd8ddd1e91",
      "family_id": "glm47_flash",
      "hf_repository": "unsloth/GLM-4.7-Flash-GGUF",
      "hf_revision": "0d32489ecb9db6d2a4fc93bd27ef01519f95474d",
      "name": "GLM-4.7-Flash",
      "quantization": "Q3_K_S",
      "tensor_precision_map": null,
      "variant": "GLM-4.7-Flash",
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-441a09dbbb92e9e490bab7e6b4e9fab4450bbc2a7bec06693c69754a43e3379d",
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
      "CPU_scoring_limit_s": 120,
      "CPU_threads": "6",
      "GPU_offload": "99",
      "GPU_wrapper_limit_s": 1440,
      "RAM_budget": null,
      "VRAM_budget_mib": 14336,
      "batch": "2048",
      "benchmark_task_limit_s": 1200,
      "chat_template_sha256": "d63ad536c3c81880043e22ec7fd08db42b4d8fb7c89c7138bc562bfa25281375",
      "context": "8192",
      "execution_deadline_s": 1200,
      "max_output": 4096,
      "microbatch": "512",
      "native_HTTP_timeout_policy": "REMAINING_TASK_TIME",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": {
        "min_p": 0.0,
        "seed": 1001,
        "temperature": 1.0,
        "top_k": 0,
        "top_p": 0.95
      },
      "startup_limit_s": 180,
      "thinking_reasoning_requested": null,
      "timing_scope": "TASK_PHASE_ONLY",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
    "schema_version": 1,
    "source_plan_sha256": "dd8b0a5a45dacb76df44d663b39716512f52d904454b8bc204c0ab51e6b516a1",
    "source_provenance": {
      "first_part_collection_audit_sha256": "d9785d63f2b201f8ae1081aa86cf3ffdc921e28f4183d42065ec407f1c1f608d",
      "first_part_contract_sha256": "1ae3cd0312ccc9f0c34fa0807d46a828907a1ed61a834a1f4bba6f75b9e2eb2d",
      "frozen_model_profile_sha256": "5f874119dc8746364a2f4dadc158066bba2c8afb3e1d4b77947765253a87883e",
      "kind": "BROKER_NATIVE_CAPTURED_CONFIGURATION"
    },
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:21d16834f428215926466ce44862fccbd3337008b49ea4ac2f58abdd8ddd1e91]",
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
        "[artifact:d63ad536c3c81880043e22ec7fd08db42b4d8fb7c89c7138bc562bfa25281375]",
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
      "environment": {
        "GGML_CUDA_GRAPH_OPT": "0",
        "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0",
        "OMP_NUM_THREADS": "6"
      },
      "exact_private_launch_sha256": "822cc397458db01aa8893a767fea63d104a7e3553cfe27d8935babfb694a2614",
      "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
      "redacted_argument_positions": [
        0,
        2,
        4,
        12,
        14,
        17
      ]
    }
  },
  "runs": [
    {
      "audit_hash": "d68ff6f2d825024dde4c54a8c05e65e7a1a98dcd21a80a00d6bbf774eee12cfe",
      "audit_ids": [
        "audit-d68ff6f2d825024dde4c",
        "audit-d9785d63f2b201f8ae10",
        "audit-e4ec23028c58a6695f7d"
      ],
      "benchmark_id": "bfcl-v4-parallel-multiple-full200",
      "benchmark_identity_id": "bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe",
      "benchmark_revision": "6ea57973c7a6097fd7c5915698c54c17c5b1b6c8",
      "causal_optimization_proof": null,
      "counter_energy": {
        "audit_id": "audit-e4ec23028c58a6695f7d",
        "complete_request_s": 1038.246775357,
        "group_window_s": 1038.385380932,
        "groups": 1,
        "included_between_request_setup_s": 0.138605575,
        "j_per_success_lower": 1053.0064285714284,
        "j_per_success_upper": 1053.7785952380952,
        "lower_j": 176905.08,
        "max_query_duration_s": 0.039997127,
        "method": "NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1",
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "solved": 168,
        "tasks": 200,
        "upper_j": 177034.804
      },
      "dataset_split_hash": "8863ea8433239f55c5f016154cf0830853c89f693c6ea270396a2fa121960579",
      "date": "2026-10-27",
      "discipline": "tools",
      "evaluated_task_ids": [
        "parallel_multiple_0",
        "parallel_multiple_1",
        "parallel_multiple_2",
        "parallel_multiple_3",
        "parallel_multiple_4",
        "parallel_multiple_5",
        "parallel_multiple_6",
        "parallel_multiple_7",
        "parallel_multiple_8",
        "parallel_multiple_9",
        "parallel_multiple_10",
        "parallel_multiple_11",
        "parallel_multiple_12",
        "parallel_multiple_13",
        "parallel_multiple_14",
        "parallel_multiple_15",
        "parallel_multiple_16",
        "parallel_multiple_17",
        "parallel_multiple_18",
        "parallel_multiple_19",
        "parallel_multiple_20",
        "parallel_multiple_21",
        "parallel_multiple_22",
        "parallel_multiple_23",
        "parallel_multiple_24",
        "parallel_multiple_25",
        "parallel_multiple_26",
        "parallel_multiple_27",
        "parallel_multiple_28",
        "parallel_multiple_29",
        "parallel_multiple_30",
        "parallel_multiple_31",
        "parallel_multiple_32",
        "parallel_multiple_33",
        "parallel_multiple_34",
        "parallel_multiple_35",
        "parallel_multiple_36",
        "parallel_multiple_37",
        "parallel_multiple_38",
        "parallel_multiple_39",
        "parallel_multiple_40",
        "parallel_multiple_41",
        "parallel_multiple_42",
        "parallel_multiple_43",
        "parallel_multiple_44",
        "parallel_multiple_45",
        "parallel_multiple_46",
        "parallel_multiple_47",
        "parallel_multiple_48",
        "parallel_multiple_49",
        "parallel_multiple_50",
        "parallel_multiple_51",
        "parallel_multiple_52",
        "parallel_multiple_53",
        "parallel_multiple_54",
        "parallel_multiple_55",
        "parallel_multiple_56",
        "parallel_multiple_57",
        "parallel_multiple_58",
        "parallel_multiple_59",
        "parallel_multiple_60",
        "parallel_multiple_61",
        "parallel_multiple_62",
        "parallel_multiple_63",
        "parallel_multiple_64",
        "parallel_multiple_65",
        "parallel_multiple_66",
        "parallel_multiple_67",
        "parallel_multiple_68",
        "parallel_multiple_69",
        "parallel_multiple_70",
        "parallel_multiple_71",
        "parallel_multiple_72",
        "parallel_multiple_73",
        "parallel_multiple_74",
        "parallel_multiple_75",
        "parallel_multiple_76",
        "parallel_multiple_77",
        "parallel_multiple_78",
        "parallel_multiple_79",
        "parallel_multiple_80",
        "parallel_multiple_81",
        "parallel_multiple_82",
        "parallel_multiple_83",
        "parallel_multiple_84",
        "parallel_multiple_85",
        "parallel_multiple_86",
        "parallel_multiple_87",
        "parallel_multiple_88",
        "parallel_multiple_89",
        "parallel_multiple_90",
        "parallel_multiple_91",
        "parallel_multiple_92",
        "parallel_multiple_93",
        "parallel_multiple_94",
        "parallel_multiple_95",
        "parallel_multiple_96",
        "parallel_multiple_97",
        "parallel_multiple_98",
        "parallel_multiple_99",
        "parallel_multiple_100",
        "parallel_multiple_101",
        "parallel_multiple_102",
        "parallel_multiple_103",
        "parallel_multiple_104",
        "parallel_multiple_105",
        "parallel_multiple_106",
        "parallel_multiple_107",
        "parallel_multiple_108",
        "parallel_multiple_109",
        "parallel_multiple_110",
        "parallel_multiple_111",
        "parallel_multiple_112",
        "parallel_multiple_113",
        "parallel_multiple_114",
        "parallel_multiple_115",
        "parallel_multiple_116",
        "parallel_multiple_117",
        "parallel_multiple_118",
        "parallel_multiple_119",
        "parallel_multiple_120",
        "parallel_multiple_121",
        "parallel_multiple_122",
        "parallel_multiple_123",
        "parallel_multiple_124",
        "parallel_multiple_125",
        "parallel_multiple_126",
        "parallel_multiple_127",
        "parallel_multiple_128",
        "parallel_multiple_129",
        "parallel_multiple_130",
        "parallel_multiple_131",
        "parallel_multiple_132",
        "parallel_multiple_133",
        "parallel_multiple_134",
        "parallel_multiple_135",
        "parallel_multiple_136",
        "parallel_multiple_137",
        "parallel_multiple_138",
        "parallel_multiple_139",
        "parallel_multiple_140",
        "parallel_multiple_141",
        "parallel_multiple_142",
        "parallel_multiple_143",
        "parallel_multiple_144",
        "parallel_multiple_145",
        "parallel_multiple_146",
        "parallel_multiple_147",
        "parallel_multiple_148",
        "parallel_multiple_149",
        "parallel_multiple_150",
        "parallel_multiple_151",
        "parallel_multiple_152",
        "parallel_multiple_153",
        "parallel_multiple_154",
        "parallel_multiple_155",
        "parallel_multiple_156",
        "parallel_multiple_157",
        "parallel_multiple_158",
        "parallel_multiple_159",
        "parallel_multiple_160",
        "parallel_multiple_161",
        "parallel_multiple_162",
        "parallel_multiple_163",
        "parallel_multiple_164",
        "parallel_multiple_165",
        "parallel_multiple_166",
        "parallel_multiple_167",
        "parallel_multiple_168",
        "parallel_multiple_169",
        "parallel_multiple_170",
        "parallel_multiple_171",
        "parallel_multiple_172",
        "parallel_multiple_173",
        "parallel_multiple_174",
        "parallel_multiple_175",
        "parallel_multiple_176",
        "parallel_multiple_177",
        "parallel_multiple_178",
        "parallel_multiple_179",
        "parallel_multiple_180",
        "parallel_multiple_181",
        "parallel_multiple_182",
        "parallel_multiple_183",
        "parallel_multiple_184",
        "parallel_multiple_185",
        "parallel_multiple_186",
        "parallel_multiple_187",
        "parallel_multiple_188",
        "parallel_multiple_189",
        "parallel_multiple_190",
        "parallel_multiple_191",
        "parallel_multiple_192",
        "parallel_multiple_193",
        "parallel_multiple_194",
        "parallel_multiple_195",
        "parallel_multiple_196",
        "parallel_multiple_197",
        "parallel_multiple_198",
        "parallel_multiple_199"
      ],
      "evaluated_task_set_hash": "8bf603cd74927e071664bcd4594c0738616480c9da7c0e86999d112a9646da59",
      "experiment_id": "R574",
      "gpu_j": null,
      "gpu_j_per_success": null,
      "measurement_conditions": {
        "cache_condition": "Native completion-HTTP intervals; startup/warmup/CPU scoring excluded; per-request native caching in exact recipe.",
        "date": "2026-10-27",
        "hardware": "Tesla V100-SXM2 16 GB HBM2",
        "output_cap": 4096,
        "power_limit_w": 300,
        "sampling": {
          "min_p": 0.0,
          "seed": 1001,
          "temperature": 1.0,
          "top_k": 0,
          "top_p": 0.95
        }
      },
      "metric": "bfcl_parallel_multiple_ast_accuracy_percent",
      "model_artifact_id": "artifact-441a09dbbb92e9e490bab7e6b4e9fab4450bbc2a7bec06693c69754a43e3379d",
      "model_family_id": "glm47_flash",
      "model_name": "GLM-4.7-Flash",
      "official_eligible": true,
      "peak_vram_mib": 13716.5,
      "practical_protocol": {
        "complete": 200,
        "solved": 168,
        "tasks": 200,
        "valid": 200
      },
      "qualification_audit": {
        "GPU_runs_in_qualification": 0,
        "all_canonical_controls_passed": true,
        "audit_hash": "d68ff6f2d825024dde4c54a8c05e65e7a1a98dcd21a80a00d6bbf774eee12cfe",
        "benchmark_identity_id": "bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe",
        "category_controls": {
          "canonical_pass": 200,
          "negative_rejected": 600,
          "schemas_passed": 200,
          "tasks": 200
        },
        "category_only": true,
        "changed_original_task_judgements": [],
        "complete_task_set": true,
        "control_audit_sha256": "0fcfeb0243c8f9aea7cf0991ec29432686ebda5df9892824a8574c8f8d881860",
        "control_stdout_sha256": "25d800384400f875caf988106b3ed6bf4f6c669b2d04543490d66f967f8aaf52",
        "dataset_split_hash": "8863ea8433239f55c5f016154cf0830853c89f693c6ea270396a2fa121960579",
        "disclosure": "First full BFCL v4 parallel_multiple200 category of unchanged R558 GLM-4.7-Flash Q3_K_S native profile. Preserve executed native template, Thinking, sampling, context8192/output4096, weights, engine, cache, batches and hardware guards. Whole-profile qualification; no optimization, automatic retry or Champion. One shared1200s TASK phase, startup180s.",
        "experiment_id": "R574",
        "immutable_scoring_plan_sha256": "1cddeb8ac818164ce7d5f554fe91c3b0c27fc8fccc6b978e211f0105bb34a44a",
        "independent_audit_verified": true,
        "independent_replay_receipts": [
          {
            "elapsed_s": 0.2265465259552002,
            "label": "r574-native-score",
            "receipt_sha256": "8e088fa7eca00ab279ca0dfbc26b58884c9ad1953c2a0faeb73dc32f76e983c5",
            "stdout_sha256": "0a480b70eba5db9d8fc0e8adf87b246a823c4609ccf8ec585989e501fc1ba4eb",
            "worker_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666"
          },
          {
            "elapsed_s": 0.2259998321533203,
            "label": "r574-native-replay",
            "receipt_sha256": "1fca529224695631b98f02aa86dc45566c85128bdd26e2dade752ca309c63c96",
            "stdout_sha256": "0a480b70eba5db9d8fc0e8adf87b246a823c4609ccf8ec585989e501fc1ba4eb",
            "worker_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666"
          }
        ],
        "metrics_verified": true,
        "model_artifact_id": "artifact-441a09dbbb92e9e490bab7e6b4e9fab4450bbc2a7bec06693c69754a43e3379d",
        "model_generation_repeats": 1,
        "model_generations_in_qualification": 0,
        "no_task_exclusions": true,
        "official_category": "parallel_multiple",
        "official_category_accuracy": 0.84,
        "official_correct_count": 168,
        "official_scorer_verified": true,
        "original_scorer_wrapper_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666",
        "prompt_protocol_verified": true,
        "qualification_kind": "FULL_OFFICIAL_BFCL_CATEGORY_LOCAL_PROTOCOL_VERIFIED",
        "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
        "scorer_execution_limits": {
          "actual_combined_CPU_wall_s": 0.5246343789622188,
          "combined_CPU_wall_limit_s": 120,
          "model_requests": 0,
          "tool_executions": 0,
          "unprivileged_OS_sandbox": true
        },
        "scorer_version": {
          "aggregation": "correct_count / len(model_result); complete200 parallel_multiple IDs required",
          "frozen_checker_adapter_sha256": "a926f83c9dd9fdba5465c3c7c6a02ec31ace9206b91f06fa27f6d7f077363710",
          "frozen_checker_bundle_sha256": "657dbc00ab40c23a53173b758d6a25e4806a18cd64c10118148b473114042236",
          "native_score_wrapper_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666",
          "official_aggregation_helper_sha256": "7c756592af53eb54733989aa03a3fa87854f1c20dd566f3f10a770e17d25a9d7",
          "official_eval_runner_sha256": "b1033684908819ccb312d4d0e2c563359d69247412f00206013b2292b0e3ce81",
          "official_native_format_sha256": "3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd",
          "official_revision": "6ea57973c7a6097fd7c5915698c54c17c5b1b6c8"
        },
        "solved": 168,
        "task_ids": [
          "parallel_multiple_0",
          "parallel_multiple_1",
          "parallel_multiple_2",
          "parallel_multiple_3",
          "parallel_multiple_4",
          "parallel_multiple_5",
          "parallel_multiple_6",
          "parallel_multiple_7",
          "parallel_multiple_8",
          "parallel_multiple_9",
          "parallel_multiple_10",
          "parallel_multiple_11",
          "parallel_multiple_12",
          "parallel_multiple_13",
          "parallel_multiple_14",
          "parallel_multiple_15",
          "parallel_multiple_16",
          "parallel_multiple_17",
          "parallel_multiple_18",
          "parallel_multiple_19",
          "parallel_multiple_20",
          "parallel_multiple_21",
          "parallel_multiple_22",
          "parallel_multiple_23",
          "parallel_multiple_24",
          "parallel_multiple_25",
          "parallel_multiple_26",
          "parallel_multiple_27",
          "parallel_multiple_28",
          "parallel_multiple_29",
          "parallel_multiple_30",
          "parallel_multiple_31",
          "parallel_multiple_32",
          "parallel_multiple_33",
          "parallel_multiple_34",
          "parallel_multiple_35",
          "parallel_multiple_36",
          "parallel_multiple_37",
          "parallel_multiple_38",
          "parallel_multiple_39",
          "parallel_multiple_40",
          "parallel_multiple_41",
          "parallel_multiple_42",
          "parallel_multiple_43",
          "parallel_multiple_44",
          "parallel_multiple_45",
          "parallel_multiple_46",
          "parallel_multiple_47",
          "parallel_multiple_48",
          "parallel_multiple_49",
          "parallel_multiple_50",
          "parallel_multiple_51",
          "parallel_multiple_52",
          "parallel_multiple_53",
          "parallel_multiple_54",
          "parallel_multiple_55",
          "parallel_multiple_56",
          "parallel_multiple_57",
          "parallel_multiple_58",
          "parallel_multiple_59",
          "parallel_multiple_60",
          "parallel_multiple_61",
          "parallel_multiple_62",
          "parallel_multiple_63",
          "parallel_multiple_64",
          "parallel_multiple_65",
          "parallel_multiple_66",
          "parallel_multiple_67",
          "parallel_multiple_68",
          "parallel_multiple_69",
          "parallel_multiple_70",
          "parallel_multiple_71",
          "parallel_multiple_72",
          "parallel_multiple_73",
          "parallel_multiple_74",
          "parallel_multiple_75",
          "parallel_multiple_76",
          "parallel_multiple_77",
          "parallel_multiple_78",
          "parallel_multiple_79",
          "parallel_multiple_80",
          "parallel_multiple_81",
          "parallel_multiple_82",
          "parallel_multiple_83",
          "parallel_multiple_84",
          "parallel_multiple_85",
          "parallel_multiple_86",
          "parallel_multiple_87",
          "parallel_multiple_88",
          "parallel_multiple_89",
          "parallel_multiple_90",
          "parallel_multiple_91",
          "parallel_multiple_92",
          "parallel_multiple_93",
          "parallel_multiple_94",
          "parallel_multiple_95",
          "parallel_multiple_96",
          "parallel_multiple_97",
          "parallel_multiple_98",
          "parallel_multiple_99",
          "parallel_multiple_100",
          "parallel_multiple_101",
          "parallel_multiple_102",
          "parallel_multiple_103",
          "parallel_multiple_104",
          "parallel_multiple_105",
          "parallel_multiple_106",
          "parallel_multiple_107",
          "parallel_multiple_108",
          "parallel_multiple_109",
          "parallel_multiple_110",
          "parallel_multiple_111",
          "parallel_multiple_112",
          "parallel_multiple_113",
          "parallel_multiple_114",
          "parallel_multiple_115",
          "parallel_multiple_116",
          "parallel_multiple_117",
          "parallel_multiple_118",
          "parallel_multiple_119",
          "parallel_multiple_120",
          "parallel_multiple_121",
          "parallel_multiple_122",
          "parallel_multiple_123",
          "parallel_multiple_124",
          "parallel_multiple_125",
          "parallel_multiple_126",
          "parallel_multiple_127",
          "parallel_multiple_128",
          "parallel_multiple_129",
          "parallel_multiple_130",
          "parallel_multiple_131",
          "parallel_multiple_132",
          "parallel_multiple_133",
          "parallel_multiple_134",
          "parallel_multiple_135",
          "parallel_multiple_136",
          "parallel_multiple_137",
          "parallel_multiple_138",
          "parallel_multiple_139",
          "parallel_multiple_140",
          "parallel_multiple_141",
          "parallel_multiple_142",
          "parallel_multiple_143",
          "parallel_multiple_144",
          "parallel_multiple_145",
          "parallel_multiple_146",
          "parallel_multiple_147",
          "parallel_multiple_148",
          "parallel_multiple_149",
          "parallel_multiple_150",
          "parallel_multiple_151",
          "parallel_multiple_152",
          "parallel_multiple_153",
          "parallel_multiple_154",
          "parallel_multiple_155",
          "parallel_multiple_156",
          "parallel_multiple_157",
          "parallel_multiple_158",
          "parallel_multiple_159",
          "parallel_multiple_160",
          "parallel_multiple_161",
          "parallel_multiple_162",
          "parallel_multiple_163",
          "parallel_multiple_164",
          "parallel_multiple_165",
          "parallel_multiple_166",
          "parallel_multiple_167",
          "parallel_multiple_168",
          "parallel_multiple_169",
          "parallel_multiple_170",
          "parallel_multiple_171",
          "parallel_multiple_172",
          "parallel_multiple_173",
          "parallel_multiple_174",
          "parallel_multiple_175",
          "parallel_multiple_176",
          "parallel_multiple_177",
          "parallel_multiple_178",
          "parallel_multiple_179",
          "parallel_multiple_180",
          "parallel_multiple_181",
          "parallel_multiple_182",
          "parallel_multiple_183",
          "parallel_multiple_184",
          "parallel_multiple_185",
          "parallel_multiple_186",
          "parallel_multiple_187",
          "parallel_multiple_188",
          "parallel_multiple_189",
          "parallel_multiple_190",
          "parallel_multiple_191",
          "parallel_multiple_192",
          "parallel_multiple_193",
          "parallel_multiple_194",
          "parallel_multiple_195",
          "parallel_multiple_196",
          "parallel_multiple_197",
          "parallel_multiple_198",
          "parallel_multiple_199"
        ],
        "task_phase_timing": {
          "clock_hashes": {
            "INITIAL.json": "c4a298bbadea8d14b460944466dda020b2f7010083ad22c3f88c50a55132982c",
            "TASK_BEGIN.json": "14a587f8f58db3a20c48da8b71699fcf9b099c5e47f2a3c9624dec2977a49387",
            "TASK_END.json": "bf6b536624949bcff3266e1c0c019bed99d822f277ae8d1ab713488a360f7e0a"
          },
          "limit_seconds": 1200,
          "seconds": 1038.385984375,
          "startup_excluded_from_task_budget": true,
          "startup_seconds": 114.56150525
        },
        "tasks": 200,
        "unique_task_ids_verified": true
      },
      "qualification_audit_id": "audit-e8db2aaaa470124b01cf",
      "record_schema_version": 1,
      "repeat_range": null,
      "run_id": "run-0e8de51b2454162fbf22814c31d992d06c7c10a200e2aa0664b78c212099ff38",
      "runtime_configuration_id": "cfg-9def619a67b02ec81dadb5ad2e8b0caebe936d6e91e92c90907b87a383fc1cde",
      "score_percent": 84.0,
      "scorer_execution_limits": {
        "actual_combined_CPU_wall_s": 0.5246343789622188,
        "combined_CPU_wall_limit_s": 120,
        "model_requests": 0,
        "tool_executions": 0,
        "unprivileged_OS_sandbox": true
      },
      "scorer_version": {
        "aggregation": "correct_count / len(model_result); complete200 parallel_multiple IDs required",
        "frozen_checker_adapter_sha256": "a926f83c9dd9fdba5465c3c7c6a02ec31ace9206b91f06fa27f6d7f077363710",
        "frozen_checker_bundle_sha256": "657dbc00ab40c23a53173b758d6a25e4806a18cd64c10118148b473114042236",
        "native_score_wrapper_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666",
        "official_aggregation_helper_sha256": "7c756592af53eb54733989aa03a3fa87854f1c20dd566f3f10a770e17d25a9d7",
        "official_eval_runner_sha256": "b1033684908819ccb312d4d0e2c563359d69247412f00206013b2292b0e3ce81",
        "official_native_format_sha256": "3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd",
        "official_revision": "6ea57973c7a6097fd7c5915698c54c17c5b1b6c8"
      },
      "solved": 168,
      "source_audit_hashes": [
        "d68ff6f2d825024dde4c54a8c05e65e7a1a98dcd21a80a00d6bbf774eee12cfe",
        "d9785d63f2b201f8ae1081aa86cf3ffdc921e28f4183d42065ec407f1c1f608d"
      ],
      "status": "FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
      "status_reason": "Full official scorer/API task set independently verified; declared local evaluation limits and any pinned upstream reference anomaly remain visible.",
      "tasks": 200,
      "wall_s": 1038.246775357,
      "warning": "One official BFCL category, not BFCL overall. Practical protocol checks are separate from official AST. No publisher equivalence, unseen holdout, model superiority, causal optimization or Champion claim. First full BFCL v4 parallel_multiple200 category of unchanged R558 GLM-4.7-Flash Q3_K_S native profile. Preserve executed native template, Thinking, sampling, context8192/output4096, weights, engine, cache, batches and hardware guards. Whole-profile qualification; no optimization, automatic retry or Champion. One shared1200s TASK phase, startup180s."
    }
  ]
}
```

</details>
