# Ministral-3-14B-Instruct-2512 · cfg-ee3bb53965a3

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "architecture": null,
  "artifact_sha256": "f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000",
  "family_id": "ministral3_14b",
  "hf_repository": "mistralai/Ministral-3-14B-Instruct-2512-GGUF",
  "hf_revision": "74fac473c43357d7fb2671713608183cc72496d0",
  "name": "Ministral-3-14B-Instruct-2512",
  "quantization": "Q5_K_M",
  "tensor_precision_map": null,
  "variant": "ministral3-14b-native-coding-task1200-reviewed-sm70",
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
  "chat_template_sha256": "6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b",
  "context": "8192",
  "execution_deadline_s": 1200,
  "max_output": 4096,
  "microbatch": "512",
  "native_template_controls": null,
  "power_limit_w": 300,
  "sampling": {
    "seed": 1001,
    "temperature": 0
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
    "[artifact:f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000]",
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
    "[artifact:6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b]",
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
  "exact_private_launch_sha256": "8b98b0e66df2b15e0a16b5eec43c39de58f34388beadc38c3bacd288a1416db9",
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
| R575 | humanevalplus-v0.1.10 / FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED | 135/164 | 530.844694893 | NOT MEASURED | 10948.5 | [audit-b3c10beebc5bc04afd4f](../audits/audit-b3c10beebc5bc04afd4f.md), [audit-467ab04c8189449e95e1](../audits/audit-467ab04c8189449e95e1.md), [audit-46b9c08a8b4bd6e8a4bd](../audits/audit-46b9c08a8b4bd6e8a4bd.md), [audit-9cf0781941aca005cbad](../audits/audit-9cf0781941aca005cbad.md) |

Separate benchmark qualification audits: [audit-4823e3da93d7bc875b78](../audits/audit-4823e3da93d7bc875b78.md)

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R575 / 0 | INFERENCE_OBSERVED_IN_BROKER_CAMPAIGN; FULL_BENCHMARK_NOT_IMPLIED | BOUNDED_NATIVE_EXECUTION_OBSERVED | [audit-467ab04c8189449e95e1](../audits/audit-467ab04c8189449e95e1.md) |

## Additional hash-bound execution evidence

These observations supplement the original immutable profile; they do not assign a release version to an unidentified historical build. Declared plan controls, observed request settings and executed sampler settings remain separate.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "evidence_id": "evidence-8171a93d0b3f08d76ec9b7d1fa75023e90338c4caeb0916a9ab87ab077875947",
    "fields": {
      "engine.reported_build_number": 0,
      "engine.reported_compiled_CUDA_archs": "700",
      "engine.version_provenance_note": "Pinned historical server log reports build 0 (unknown); no identifiable upstream version or commit. Binary and CUDA-library hashes remain authoritative.",
      "model.architecture": "mistral3",
      "runtime.observed_generation_settings.backend_sampling": false,
      "runtime.observed_generation_settings.frequency_penalty": 0.0,
      "runtime.observed_generation_settings.ignore_eos": false,
      "runtime.observed_generation_settings.min_p": 0.05000000074505806,
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
      "runtime.observed_generation_settings.temperature": 0.0,
      "runtime.observed_generation_settings.top_k": 40,
      "runtime.observed_generation_settings.top_p": 0.949999988079071,
      "runtime.observed_generation_settings.typical_p": 1.0,
      "runtime.observed_request_sampling.seed": 1001,
      "runtime.observed_request_sampling.temperature": 0
    },
    "interpretation": "Additional observations from pinned original execution evidence. Immutable original profile unchanged; reported build identity is not an upstream release. Requested options do not establish effective kernel dispatch.",
    "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
    "sources": [
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "LAUNCH.json",
        "sha256": "170d36950aabac0a48a83b4453b80c14183efd13732f91faa192e1959765931f"
      },
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "server.log",
        "sha256": "72fcc73ce7ecb142bfb1b5ed2e326a37b11a205a5397bf2e0b1bfad5add387b7"
      },
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "HTTP_RESULTS.jsonl",
        "sha256": "56f0c9e1d962baeaecd91adeb1af5c61d15043c472594556f8e7cda5b217ade5"
      }
    ]
  }
]
```

</details>

Evidence metadata: [audit-7514d15dbb4b8a12f870](../audits/audit-7514d15dbb4b8a12f870.md)

## Recorded engine timings and energy denominator

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "aggregation": "Rate = sum of recorded token counts / sum of engine timing seconds for the exact task set; excludes startup/warmup. GPU J/output token uses gross case-window GPU energy including prefill. Engine prefill time is not TTFT. No unseen holdout claim.",
    "evidence_id": "measurement-3a11fcdd079e5792aec7f81bfe6568c906263b4cee265cc979f9418973b90b27",
    "run_id": "run-a1cffb7c0da0257cfd2cb4bf0dc3b5bbf753db2fed9d91256700aab2d5e5bad1",
    "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
    "sources": [
      {
        "authority_audit_id": "audit-b3c10beebc5bc04afd4f",
        "filename": "AUDIT.json",
        "sha256": "b3c10beebc5bc04afd4f8cc81e4ed1798c5bf7f73d541a5b4d101ade72023260"
      },
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "LAUNCH.json",
        "sha256": "170d36950aabac0a48a83b4453b80c14183efd13732f91faa192e1959765931f"
      },
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "server.log",
        "sha256": "72fcc73ce7ecb142bfb1b5ed2e326a37b11a205a5397bf2e0b1bfad5add387b7"
      },
      {
        "authority_audit_id": "audit-7514d15dbb4b8a12f870",
        "filename": "HTTP_RESULTS.jsonl",
        "sha256": "56f0c9e1d962baeaecd91adeb1af5c61d15043c472594556f8e7cda5b217ade5"
      }
    ],
    "task_phase_scope": "Recorded audited task phase includes input/template/token preparation between requests; completion-HTTP window sums are separate. Startup/warmup and CPU scoring are excluded from task-phase throughput.",
    "tasks": 164,
    "values": {
      "decode_engine_ms": 458171.842,
      "decode_tok_s": 64.5652946956963,
      "decode_tokens": 29582,
      "prefill_engine_ms": 71992.073,
      "prefill_tok_s": 1615.8862379195552,
      "prefill_tokens": 116331,
      "startup_s": 84.398056226,
      "successful_tasks_per_task_phase_s": 0.2542684249121962,
      "task_phase_s": 530.934975692
    },
    "wall_sum_s": 530.844694893
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
      "attempt_id": "attempt-6590c9e4f17451d4c13f08dcd8da19226f7c57a5232bef48763428c53402c011",
      "audit_hash": "467ab04c8189449e95e1879e76c5848a87fb7aa7efd395521e35cfa378336ad6",
      "audit_id": "audit-467ab04c8189449e95e1",
      "execution_status": "INFERENCE_OBSERVED_IN_BROKER_CAMPAIGN; FULL_BENCHMARK_NOT_IMPLIED",
      "experiment_id": "R575",
      "lab_metrics": {},
      "model_family_id": "ministral3_14b",
      "model_name": "Ministral-3-14B-Instruct-2512",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
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
      "artifact_sha256": "f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000",
      "family_id": "ministral3_14b",
      "hf_repository": "mistralai/Ministral-3-14B-Instruct-2512-GGUF",
      "hf_revision": "74fac473c43357d7fb2671713608183cc72496d0",
      "name": "Ministral-3-14B-Instruct-2512",
      "quantization": "Q5_K_M",
      "tensor_precision_map": null,
      "variant": "ministral3-14b-native-coding-task1200-reviewed-sm70",
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-b676e54cbff84cdb910e1f08c83d1512cfd1bbf717a4e46044ede929afb9a13a",
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
      "chat_template_sha256": "6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b",
      "context": "8192",
      "execution_deadline_s": 1200,
      "max_output": 4096,
      "microbatch": "512",
      "native_template_controls": null,
      "power_limit_w": 300,
      "sampling": {
        "seed": 1001,
        "temperature": 0
      },
      "startup_limit_s": 180,
      "thinking_reasoning_requested": null,
      "timing_scope": "TASK_PHASE_ONLY",
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
    "schema_version": 1,
    "source_plan_sha256": "b789813cbce53d4d792467d7bf44e8cbf3ef305e3df42dd3657d074084075aa4",
    "source_provenance": {
      "first_part_collection_audit_sha256": "467ab04c8189449e95e1879e76c5848a87fb7aa7efd395521e35cfa378336ad6",
      "first_part_contract_sha256": "9a38f20fff2670a485289a325feb0fe3d038435c59d2b7b9f74a0d4eaf41d6b4",
      "frozen_model_profile_sha256": "b3401d57799963a06831e660c49f976b347a6cd7118f9aee374a9bc3bb84f563",
      "kind": "BROKER_NATIVE_CAPTURED_CONFIGURATION"
    },
    "start_parameters": {
      "argv": [
        "llama-server",
        "--model",
        "[artifact:f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000]",
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
        "[artifact:6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b]",
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
      "exact_private_launch_sha256": "8b98b0e66df2b15e0a16b5eec43c39de58f34388beadc38c3bacd288a1416db9",
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
      "audit_hash": "b3c10beebc5bc04afd4f8cc81e4ed1798c5bf7f73d541a5b4d101ade72023260",
      "audit_ids": [
        "audit-b3c10beebc5bc04afd4f",
        "audit-467ab04c8189449e95e1",
        "audit-46b9c08a8b4bd6e8a4bd",
        "audit-9cf0781941aca005cbad"
      ],
      "benchmark_id": "humanevalplus-v0.1.10",
      "benchmark_identity_id": "bench-343ddfa996f79239e54edb7a1ddd23732c676d7d21d5d83cb22efddfc23e8f9c",
      "benchmark_revision": "release:v0.1.10",
      "causal_optimization_proof": null,
      "counter_energy": {
        "audit_id": "audit-9cf0781941aca005cbad",
        "complete_request_s": 530.844694893,
        "group_window_s": 530.934436057,
        "groups": 1,
        "included_between_request_setup_s": 0.089741164,
        "j_per_success_lower": 1124.5918074074075,
        "j_per_success_upper": 1125.5629037037038,
        "lower_j": 151819.894,
        "max_query_duration_s": 0.035766499,
        "method": "NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1",
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "solved": 135,
        "tasks": 164,
        "upper_j": 151950.992
      },
      "dataset_split_hash": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
      "date": "2026-10-27",
      "discipline": "coding",
      "evaluated_task_set_hash": "cc7377147a38ea139e77745d18fcc35c267dd192d4b99c89d8a4e653ef4d39d5",
      "experiment_id": "R575",
      "gpu_j": null,
      "gpu_j_per_success": null,
      "measurement_conditions": {
        "cache_condition": "Completion HTTP intervals; startup, warmups and CPU evaluation excluded; see original per-request cache setting.",
        "date": "2026-10-27",
        "hardware": "Tesla V100-SXM2 16 GB HBM2",
        "output_cap": 4096,
        "power_limit_w": 300,
        "sampling": {
          "seed": 1001,
          "temperature": 0
        }
      },
      "metric": "pass_at_1_percent",
      "model_artifact_id": "artifact-b676e54cbff84cdb910e1f08c83d1512cfd1bbf717a4e46044ede929afb9a13a",
      "model_family_id": "ministral3_14b",
      "model_name": "Ministral-3-14B-Instruct-2512",
      "official_eligible": true,
      "peak_vram_mib": 10948.5,
      "qualification_audit": {
        "GPU_runs": 0,
        "all_canonical_controls_passed": false,
        "audit_hash": "b3c10beebc5bc04afd4f8cc81e4ed1798c5bf7f73d541a5b4d101ade72023260",
        "benchmark_identity_id": "bench-343ddfa996f79239e54edb7a1ddd23732c676d7d21d5d83cb22efddfc23e8f9c",
        "canonical_reference_exception": {
          "all_negative_controls_rejected": true,
          "calibration_sha256": "8d3ae0ee4baa41c101ef10724388725fb708e5a21ae1f5757956cc50f7e9d1c8",
          "control_task_count": 164,
          "full_task_set_independently_replayed": true,
          "official_oracle_source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
          "other_canonical_tasks_passed": 163,
          "source_review_sha256": "c7bd0ccf2a32a11dd8fa524c495b71cd1f18bd1003335cbacbcfc085292b62d0",
          "task_ids": [
            "HumanEval/32"
          ],
          "unchanged_official_oracle_and_dataset": true
        },
        "changed_original_task_judgements": [],
        "complete_task_set": true,
        "dataset_split_hash": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
        "disclosure": "Full original164 HumanEval+ qualification of unchanged R552 Ministral-3-14B-Instruct-2512 Q5_K_M native profile. Exact executed template, sampler, engine and4096-output/8192-context retained. Whole-profile comparison, no causal optimization or Champion claim. Shared HumanEval/32 canonical-reference anomaly disclosed; all164 tasks retained.",
        "experiment_id": "R575",
        "immutable_replay_plan_sha256": "b044a59397bd812b341d85748d6e0d31c4d02e193941e645c6f14c772460b94f",
        "independent_audit_verified": true,
        "metrics_verified": true,
        "model_artifact_id": "artifact-b676e54cbff84cdb910e1f08c83d1512cfd1bbf717a4e46044ede929afb9a13a",
        "model_generations": 0,
        "no_task_exclusions": true,
        "official_pass_at_1": 0.823170731707317,
        "official_scorer_verified": true,
        "prompt_protocol_verified": true,
        "qualification_kind": "FULL_NATIVE164_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
        "raw_replay_sha256": "a4b979c3c6668cd34e1f9f84226f07a7fe6200348996a5c9c9f3225e6b0b6298",
        "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
        "sandbox_receipt_sha256": "c63b767505146cdd294da5a721100f7c96796a39a002cddb472ba12929e10f2a",
        "scorer_execution_limits": {
          "CPU_quota_percent": 100,
          "adapter": "streaming pinned official check_correctness + untrusted_check + estimate_pass_at_k; not optional full CLI",
          "cgroup_memory_max_bytes": 1073741824,
          "complete_actual_evaluation_elapsed_s": 17.11196780204773,
          "groundtruth": "Reused SHA-verified official canonical outputs/timings; decoded only inside isolation",
          "groundtruth_time_limit_factor": 4.0,
          "mini": false,
          "minimum_case_time_limit_s": 1.0,
          "noextreme": false,
          "parallel_evaluation_workers": 1,
          "per_model_runtime_cap_s": 120,
          "samples_per_task": 1,
          "scorer_memory_limit_bytes": 805306368
        },
        "scorer_version": {
          "git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e",
          "package": "evalplus",
          "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
          "version": "0.3.1 + official find_zero progress fix"
        },
        "shared_reference_calibration": {
          "identical_pinned_inputs": {
            "dataset.jsonl": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
            "evaluator.txt": "47f766df2dbb2280f7dd2c1040bfff0396c2b414a8d44b639424aa941bee7eab",
            "gt0.jsonl": "850f85ff685b06394a70f164380d7a365929c76cdb3e8453e0b87dae7bac6fc0",
            "gt1.jsonl": "fec568034557cc62d6f3532ac01990831de278cb9787af6cd545aa4266229942",
            "official_eval.txt": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf"
          },
          "qualification_sha256": "846227489c7ca68147fe1eeba8a742ae659e8096a19cdfcaab1737fe6a296964",
          "replay_plan_sha256": "56fd77e31bc4ad0bbfe05c91c4ca25d8a8b9296bb08beb278eaf7c6f19867c5f",
          "worker_sha256": "a9d167ece30b454f29512b8fee945a47b72c0bd79abc652d0683a22efb40232b"
        },
        "solved": 135,
        "source_replay_audit_sha256": "350a2de07c475a9b2129511140cef9731b01273b73d30b623ba4fae85ad2c0ab",
        "task_ids": [
          "HumanEval/0",
          "HumanEval/1",
          "HumanEval/10",
          "HumanEval/100",
          "HumanEval/101",
          "HumanEval/102",
          "HumanEval/103",
          "HumanEval/104",
          "HumanEval/105",
          "HumanEval/106",
          "HumanEval/107",
          "HumanEval/108",
          "HumanEval/109",
          "HumanEval/11",
          "HumanEval/110",
          "HumanEval/111",
          "HumanEval/112",
          "HumanEval/113",
          "HumanEval/114",
          "HumanEval/115",
          "HumanEval/116",
          "HumanEval/117",
          "HumanEval/118",
          "HumanEval/119",
          "HumanEval/12",
          "HumanEval/120",
          "HumanEval/121",
          "HumanEval/122",
          "HumanEval/123",
          "HumanEval/124",
          "HumanEval/125",
          "HumanEval/126",
          "HumanEval/127",
          "HumanEval/128",
          "HumanEval/129",
          "HumanEval/13",
          "HumanEval/130",
          "HumanEval/131",
          "HumanEval/132",
          "HumanEval/133",
          "HumanEval/134",
          "HumanEval/135",
          "HumanEval/136",
          "HumanEval/137",
          "HumanEval/138",
          "HumanEval/139",
          "HumanEval/14",
          "HumanEval/140",
          "HumanEval/141",
          "HumanEval/142",
          "HumanEval/143",
          "HumanEval/144",
          "HumanEval/145",
          "HumanEval/146",
          "HumanEval/147",
          "HumanEval/148",
          "HumanEval/149",
          "HumanEval/15",
          "HumanEval/150",
          "HumanEval/151",
          "HumanEval/152",
          "HumanEval/153",
          "HumanEval/154",
          "HumanEval/155",
          "HumanEval/156",
          "HumanEval/157",
          "HumanEval/158",
          "HumanEval/159",
          "HumanEval/16",
          "HumanEval/160",
          "HumanEval/161",
          "HumanEval/162",
          "HumanEval/163",
          "HumanEval/17",
          "HumanEval/18",
          "HumanEval/19",
          "HumanEval/2",
          "HumanEval/20",
          "HumanEval/21",
          "HumanEval/22",
          "HumanEval/23",
          "HumanEval/24",
          "HumanEval/25",
          "HumanEval/26",
          "HumanEval/27",
          "HumanEval/28",
          "HumanEval/29",
          "HumanEval/3",
          "HumanEval/30",
          "HumanEval/31",
          "HumanEval/32",
          "HumanEval/33",
          "HumanEval/34",
          "HumanEval/35",
          "HumanEval/36",
          "HumanEval/37",
          "HumanEval/38",
          "HumanEval/39",
          "HumanEval/4",
          "HumanEval/40",
          "HumanEval/41",
          "HumanEval/42",
          "HumanEval/43",
          "HumanEval/44",
          "HumanEval/45",
          "HumanEval/46",
          "HumanEval/47",
          "HumanEval/48",
          "HumanEval/49",
          "HumanEval/5",
          "HumanEval/50",
          "HumanEval/51",
          "HumanEval/52",
          "HumanEval/53",
          "HumanEval/54",
          "HumanEval/55",
          "HumanEval/56",
          "HumanEval/57",
          "HumanEval/58",
          "HumanEval/59",
          "HumanEval/6",
          "HumanEval/60",
          "HumanEval/61",
          "HumanEval/62",
          "HumanEval/63",
          "HumanEval/64",
          "HumanEval/65",
          "HumanEval/66",
          "HumanEval/67",
          "HumanEval/68",
          "HumanEval/69",
          "HumanEval/7",
          "HumanEval/70",
          "HumanEval/71",
          "HumanEval/72",
          "HumanEval/73",
          "HumanEval/74",
          "HumanEval/75",
          "HumanEval/76",
          "HumanEval/77",
          "HumanEval/78",
          "HumanEval/79",
          "HumanEval/8",
          "HumanEval/80",
          "HumanEval/81",
          "HumanEval/82",
          "HumanEval/83",
          "HumanEval/84",
          "HumanEval/85",
          "HumanEval/86",
          "HumanEval/87",
          "HumanEval/88",
          "HumanEval/89",
          "HumanEval/9",
          "HumanEval/90",
          "HumanEval/91",
          "HumanEval/92",
          "HumanEval/93",
          "HumanEval/94",
          "HumanEval/95",
          "HumanEval/96",
          "HumanEval/97",
          "HumanEval/98",
          "HumanEval/99"
        ],
        "task_phase_timing": {
          "CPU_scoring_separately_bounded": true,
          "clock_hashes": {
            "INITIAL.json": "e16dfde23c982d05860e5b38d0e27ded23ca37239eaf8f1b0c2e17332bfcb09c",
            "TASK_BEGIN.json": "a8baf7e35863d071865f89d382bff4dc18e41c6c12ea415ee8667ad117c20508",
            "TASK_END.json": "201217210b03a039a2d1f348cb0319e78a256fc0897a873439b56af92292c2e8"
          },
          "limit_seconds": 1200,
          "seconds": 530.934975692,
          "startup_excluded_from_task_budget": true,
          "startup_seconds": 84.398056226
        },
        "tasks": 164,
        "unique_task_ids_verified": true
      },
      "qualification_audit_id": "audit-4823e3da93d7bc875b78",
      "record_schema_version": 1,
      "repeat_range": null,
      "run_id": "run-a1cffb7c0da0257cfd2cb4bf0dc3b5bbf753db2fed9d91256700aab2d5e5bad1",
      "runtime_configuration_id": "cfg-ee3bb53965a3c29d8ad9ee42fdc77360bdde5295c02fbc0ce1c29cbb7e56c57b",
      "score_percent": 82.3170731707317,
      "scorer_execution_limits": {
        "CPU_quota_percent": 100,
        "adapter": "streaming pinned official check_correctness + untrusted_check + estimate_pass_at_k; not optional full CLI",
        "cgroup_memory_max_bytes": 1073741824,
        "complete_actual_evaluation_elapsed_s": 17.11196780204773,
        "groundtruth": "Reused SHA-verified official canonical outputs/timings; decoded only inside isolation",
        "groundtruth_time_limit_factor": 4.0,
        "mini": false,
        "minimum_case_time_limit_s": 1.0,
        "noextreme": false,
        "parallel_evaluation_workers": 1,
        "per_model_runtime_cap_s": 120,
        "samples_per_task": 1,
        "scorer_memory_limit_bytes": 805306368
      },
      "scorer_version": {
        "git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e",
        "package": "evalplus",
        "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
        "version": "0.3.1 + official find_zero progress fix"
      },
      "solved": 135,
      "source_audit_hashes": [
        "b3c10beebc5bc04afd4f8cc81e4ed1798c5bf7f73d541a5b4d101ade72023260",
        "467ab04c8189449e95e1879e76c5848a87fb7aa7efd395521e35cfa378336ad6",
        "46b9c08a8b4bd6e8a4bd111949755238dad759983f266cea61b01dfc1ce348d5"
      ],
      "status": "FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
      "status_reason": "Full official scorer/API task set independently verified; declared local evaluation limits and any pinned upstream reference anomaly remain visible.",
      "tasks": 164,
      "wall_s": 530.844694893,
      "warning": "Declared native template/sampling and local output/context limits apply. No publisher-protocol equivalence, model superiority or causal optimization benefit is implied. Monitoring corrections and data recovery remain in original audit lineage. Full original164 HumanEval+ qualification of unchanged R552 Ministral-3-14B-Instruct-2512 Q5_K_M native profile. Exact executed template, sampler, engine and4096-output/8192-context retained. Whole-profile comparison, no causal optimization or Champion claim. Shared HumanEval/32 canonical-reference anomaly disclosed; all164 tasks retained."
    }
  ]
}
```

</details>
