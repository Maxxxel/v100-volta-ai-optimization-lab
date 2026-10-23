# Proposed OmniCoder derivative test profiles

[Research decisions](../omnicoder-derivatives.md). **PROPOSED, NOT EXECUTED OR GPU-ADMITTED.** No profile here is inserted into the measured configuration history. Separate user approval is mandatory before new derivative GPU trials.

After any future pinned download, verify the complete file SHA256 and compare quantized tensor payloads against the retained baseline before attributing a result to changed weights. A source BF16 difference is not proof that the selected quantized export retains that difference. Identical weights with a different template are a template/profile comparison, not a newly trained-model result.

The 900-second budget covers the whole benchmark, all parts, startup, retries, evaluation phases and cleanup. The trusted broker migration is still required; the old per-job contract must not be bypassed or reset. A full benchmark score requires every official task and evaluator to finish. An interrupted run is PARTIAL, not a zero score, a complete benchmark or grounds to reject the model. No task-selected output/sampling tuning on official tests.

At most three coding candidates are proposed. Use pinned native templates and explicit thinking controls; requested FA, graph, MTP and cache controls do not prove the executed paths. Actual VRAM, quality and energy remain unmeasured. Historical reference settings differ and cannot support a causal improvement claim. Standard full benchmarks are the target; no small private quality pre-screen is used to discard a candidate.

## Priority 1 — prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF

```json
{
  "benchmark": {
    "benchmark_id": "humanevalplus-v0.1.10",
    "benchmark_revision": "release:v0.1.10",
    "dataset_split_hash": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
    "expected_task_ids_hash": "8c4a9413be6b6b793de94b702ab733ca734db2f5d6bca361605f1d7f71dd9ebe",
    "required_task_count": 164,
    "scorer_version": {
      "git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e",
      "package": "evalplus",
      "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
      "version": "0.3.1 + official find_zero progress fix"
    }
  },
  "budget_covers": "startup, all generation parts, retries, verification phases and cleanup; no reset between parts",
  "bytes": 7359260416,
  "comparison_limit": "Historical references use differing sampling, templates, MTP and output budgets. No controlled model-superiority or optimization delta until exact comparable fresh/stored profiles are available.",
  "declared_upstream": "prithivMLmods/Nexus-9B-CodeCore-Merge",
  "engine": {
    "CUDA_compiler_record": "12.8 compiler path recorded in CMakeCache; loaded CUDA runtime version not newly measured",
    "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
    "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
    "build_receipt_sha256": "b23f17f03e34ae0d68f5ea11fa58b4a22ef19e3a74a5e933d20f2818a1f4eaa9",
    "driver_observed": "580.178.04",
    "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
    "name": "llama.cpp-compatible reviewed local build",
    "patch_receipts": {
      "numeric_test_diff_sha256": "479bd12d814663bc5caa4023e955ec94247b50bdf96fffa7b014ddba1a596585"
    },
    "repository": "https://github.com/ggml-org/llama.cpp",
    "source_attested_commit": "097cf33d9499b1eade67d51e16d7c75427e7b267",
    "source_inputs_sha256": "9e3f8d55281b16afdd88a51c1e51f2c658ae1958caf88fdf1537601b35245213",
    "source_proof_sha256": "e457c83f82afcad8fb054d0ce032d15a3daa5aa1817cc49c084688362aa3bb85",
    "upstream_contract_commit": "ea0c4c2c85fb183ec0fbd30a1af4e4275a18a064",
    "version": null
  },
  "filename": "Nexus-9B-CodeCore-Merge.Q6_K.gguf",
  "metrics": {
    "GPU_J_per_success": "NOT MEASURED",
    "TTFT": "NOT MEASURED",
    "decode": "NOT MEASURED",
    "peak_VRAM": "NOT MEASURED",
    "prefill": "NOT MEASURED",
    "success": "NOT MEASURED",
    "wall_s": "NOT MEASURED"
  },
  "model_sha256": "b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c",
  "new_GPU_execution_authorized": false,
  "planned_argv": [
    "llama-server",
    "--model",
    "[artifact:b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c]",
    "--alias",
    "admission",
    "--host",
    "[session-local]",
    "--port",
    "[session-local]",
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
    "[template:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
    "--spec-type",
    "none",
    "--reasoning-format",
    "deepseek"
  ],
  "prerequisites": [
    "Separate user approval forPhaseC.",
    "Whole900s trusted broker migration must be active and independently checked.",
    "Verify complete modelSHA after approved storage-checked download; header validation is not full-file verification.",
    "Model/template execution admission with unchanged ECC/VRAM/power/temperature/lease checks.",
    "Native benchmark adapter currently caps8tasks/job; review a one-model-session full-suite adapter or accept honest deadline-truncated evidence. Never silently bypass a contract.",
    "No per-test prompt/budget tuning. Full164 result only if all original tasks and official evaluator complete; otherwise PARTIAL and no full highscore."
  ],
  "profile_id": "omni-derivative-proposal-1",
  "quality_rank": null,
  "quantization": "Q6_K",
  "quantizer": "prithivMLmods",
  "reason": "Merge of coding parents is directly relevant; readyQ6; changed same-dtype source values. No published target score, so this is an evidence/readiness order, not a predicted quality rank.",
  "repository": "prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF",
  "request_options": {
    "cache_prompt": false,
    "chat_template_kwargs": {
      "enable_thinking": true
    },
    "max_tokens": 4096,
    "min_p": 0.0,
    "model": "admission",
    "presence_penalty": 0.0,
    "repeat_penalty": 1.0,
    "return_tokens": true,
    "seed": 1001,
    "stream": false,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95,
    "verbose": true
  },
  "research_priority_rank": 1,
  "revision": "330ab686d7784f9b21f553727635efceeb8562e7",
  "runtime": {
    "CPU_threads": 6,
    "GPU_offload_layers": 99,
    "KV_K": "f16",
    "KV_V": "f16",
    "MTP_requested": false,
    "actual_graph_capture": null,
    "batch": 2048,
    "cache_prompt": false,
    "context_tokens": 8192,
    "environment": {
      "GGML_CUDA_GRAPH_OPT": "0",
      "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
    },
    "external_draft": null,
    "flash_attention_effective": null,
    "flash_attention_requested": "on",
    "max_output_tokens": 4096,
    "microbatch": 512,
    "power_limit_w": 300,
    "prefix_reuse_requested": false,
    "sampling": {
      "min_p": 0.0,
      "presence_penalty": 0.0,
      "repeat_penalty": 1.0,
      "seed": 1001,
      "temperature": 0.6,
      "top_k": 20,
      "top_p": 0.95
    },
    "spec_type": "none",
    "thinking_effective": null,
    "thinking_requested": true
  },
  "runtime_identity_note": "Build attests source commit097cf33...; retained adapter contract names ea0c4c2... separately. Neither is silently substituted for a release version. Requested FA/graph settings are not proof of executed kernels.",
  "status": "PROPOSED_NOT_GPU_ADMITTED_NOT_DOWNLOADED",
  "template_sha256": "a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715",
  "whole_benchmark_wall_budget_s": 900
}
```

## Priority 2 — Kukedlc/Slopus-9B

```json
{
  "benchmark": {
    "benchmark_id": "humanevalplus-v0.1.10",
    "benchmark_revision": "release:v0.1.10",
    "dataset_split_hash": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
    "expected_task_ids_hash": "8c4a9413be6b6b793de94b702ab733ca734db2f5d6bca361605f1d7f71dd9ebe",
    "required_task_count": 164,
    "scorer_version": {
      "git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e",
      "package": "evalplus",
      "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
      "version": "0.3.1 + official find_zero progress fix"
    }
  },
  "budget_covers": "startup, all generation parts, retries, verification phases and cleanup; no reset between parts",
  "bytes": 7359258944,
  "comparison_limit": "Historical references use differing sampling, templates, MTP and output budgets. No controlled model-superiority or optimization delta until exact comparable fresh/stored profiles are available.",
  "declared_upstream": "Kukedlc/Slopus-9B",
  "engine": {
    "CUDA_compiler_record": "12.8 compiler path recorded in CMakeCache; loaded CUDA runtime version not newly measured",
    "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
    "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
    "build_receipt_sha256": "b23f17f03e34ae0d68f5ea11fa58b4a22ef19e3a74a5e933d20f2818a1f4eaa9",
    "driver_observed": "580.178.04",
    "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
    "name": "llama.cpp-compatible reviewed local build",
    "patch_receipts": {
      "numeric_test_diff_sha256": "479bd12d814663bc5caa4023e955ec94247b50bdf96fffa7b014ddba1a596585"
    },
    "repository": "https://github.com/ggml-org/llama.cpp",
    "source_attested_commit": "097cf33d9499b1eade67d51e16d7c75427e7b267",
    "source_inputs_sha256": "9e3f8d55281b16afdd88a51c1e51f2c658ae1958caf88fdf1537601b35245213",
    "source_proof_sha256": "e457c83f82afcad8fb054d0ce032d15a3daa5aa1817cc49c084688362aa3bb85",
    "upstream_contract_commit": "ea0c4c2c85fb183ec0fbd30a1af4e4275a18a064",
    "version": null
  },
  "filename": "Slopus-9B-Q6_K.gguf",
  "metrics": {
    "GPU_J_per_success": "NOT MEASURED",
    "TTFT": "NOT MEASURED",
    "decode": "NOT MEASURED",
    "peak_VRAM": "NOT MEASURED",
    "prefill": "NOT MEASURED",
    "success": "NOT MEASURED",
    "wall_s": "NOT MEASURED"
  },
  "model_sha256": "aa4bc97efde586ce27e14fedd3fd896d78bb83b633ac8e5cd07113086b49479b",
  "new_GPU_execution_authorized": false,
  "planned_argv": [
    "llama-server",
    "--model",
    "[artifact:aa4bc97efde586ce27e14fedd3fd896d78bb83b633ac8e5cd07113086b49479b]",
    "--alias",
    "admission",
    "--host",
    "[session-local]",
    "--port",
    "[session-local]",
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
    "[template:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]",
    "--spec-type",
    "none",
    "--reasoning-format",
    "deepseek"
  ],
  "prerequisites": [
    "Separate user approval forPhaseC.",
    "Whole900s trusted broker migration must be active and independently checked.",
    "Verify complete modelSHA after approved storage-checked download; header validation is not full-file verification.",
    "Model/template execution admission with unchanged ECC/VRAM/power/temperature/lease checks.",
    "Native benchmark adapter currently caps8tasks/job; review a one-model-session full-suite adapter or accept honest deadline-truncated evidence. Never silently bypass a contract.",
    "No per-test prompt/budget tuning. Full164 result only if all original tasks and official evaluator complete; otherwise PARTIAL and no full highscore."
  ],
  "profile_id": "omni-derivative-proposal-2",
  "quality_rank": null,
  "quantization": "Q6_K",
  "quantizer": "Kukedlc",
  "reason": "More explicit training/adapter/log evidence and an efficiency hypothesis with disclosed accuracy cost. Newer-runtime loader behavior remains an admission question.",
  "repository": "Kukedlc/Slopus-9B",
  "request_options": {
    "cache_prompt": false,
    "chat_template_kwargs": {
      "enable_thinking": true
    },
    "max_tokens": 4096,
    "min_p": 0.0,
    "model": "admission",
    "presence_penalty": 0.0,
    "repeat_penalty": 1.0,
    "return_tokens": true,
    "seed": 1001,
    "stream": false,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95,
    "verbose": true
  },
  "research_priority_rank": 2,
  "revision": "85a138681cd780ef45a9b9c6d63363da33d08eb1",
  "runtime": {
    "CPU_threads": 6,
    "GPU_offload_layers": 99,
    "KV_K": "f16",
    "KV_V": "f16",
    "MTP_requested": false,
    "actual_graph_capture": null,
    "batch": 2048,
    "cache_prompt": false,
    "context_tokens": 8192,
    "environment": {
      "GGML_CUDA_GRAPH_OPT": "0",
      "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
    },
    "external_draft": null,
    "flash_attention_effective": null,
    "flash_attention_requested": "on",
    "max_output_tokens": 4096,
    "microbatch": 512,
    "power_limit_w": 300,
    "prefix_reuse_requested": false,
    "sampling": {
      "min_p": 0.0,
      "presence_penalty": 0.0,
      "repeat_penalty": 1.0,
      "seed": 1001,
      "temperature": 0.6,
      "top_k": 20,
      "top_p": 0.95
    },
    "spec_type": "none",
    "thinking_effective": null,
    "thinking_requested": true
  },
  "runtime_identity_note": "Build attests source commit097cf33...; retained adapter contract names ea0c4c2... separately. Neither is silently substituted for a release version. Requested FA/graph settings are not proof of executed kernels.",
  "status": "PROPOSED_NOT_GPU_ADMITTED_NOT_DOWNLOADED",
  "template_sha256": "a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715",
  "whole_benchmark_wall_budget_s": 900
}
```

## Priority 3 — mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF

```json
{
  "benchmark": {
    "benchmark_id": "humanevalplus-v0.1.10",
    "benchmark_revision": "release:v0.1.10",
    "dataset_split_hash": "42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f",
    "expected_task_ids_hash": "8c4a9413be6b6b793de94b702ab733ca734db2f5d6bca361605f1d7f71dd9ebe",
    "required_task_count": 164,
    "scorer_version": {
      "git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e",
      "package": "evalplus",
      "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf",
      "version": "0.3.1 + official find_zero progress fix"
    }
  },
  "budget_covers": "startup, all generation parts, retries, verification phases and cleanup; no reset between parts",
  "bytes": 7359260128,
  "comparison_limit": "Historical references use differing sampling, templates, MTP and output budgets. No controlled model-superiority or optimization delta until exact comparable fresh/stored profiles are available.",
  "declared_upstream": "armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill",
  "engine": {
    "CUDA_compiler_record": "12.8 compiler path recorded in CMakeCache; loaded CUDA runtime version not newly measured",
    "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
    "build_id": "dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4",
    "build_receipt_sha256": "b23f17f03e34ae0d68f5ea11fa58b4a22ef19e3a74a5e933d20f2818a1f4eaa9",
    "driver_observed": "580.178.04",
    "kernel_library_sha256": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
    "name": "llama.cpp-compatible reviewed local build",
    "patch_receipts": {
      "numeric_test_diff_sha256": "479bd12d814663bc5caa4023e955ec94247b50bdf96fffa7b014ddba1a596585"
    },
    "repository": "https://github.com/ggml-org/llama.cpp",
    "source_attested_commit": "097cf33d9499b1eade67d51e16d7c75427e7b267",
    "source_inputs_sha256": "9e3f8d55281b16afdd88a51c1e51f2c658ae1958caf88fdf1537601b35245213",
    "source_proof_sha256": "e457c83f82afcad8fb054d0ce032d15a3daa5aa1817cc49c084688362aa3bb85",
    "upstream_contract_commit": "ea0c4c2c85fb183ec0fbd30a1af4e4275a18a064",
    "version": null
  },
  "filename": "OmniCoder-9B-Claude-Opus-High-Reasoning-Distill.Q6_K.gguf",
  "metrics": {
    "GPU_J_per_success": "NOT MEASURED",
    "TTFT": "NOT MEASURED",
    "decode": "NOT MEASURED",
    "peak_VRAM": "NOT MEASURED",
    "prefill": "NOT MEASURED",
    "success": "NOT MEASURED",
    "wall_s": "NOT MEASURED"
  },
  "model_sha256": "6a089b1b2d1fe21bbe78315a94da5b81e9dde538f9737a7f2c4a53c4eb42ae66",
  "new_GPU_execution_authorized": false,
  "planned_argv": [
    "llama-server",
    "--model",
    "[artifact:6a089b1b2d1fe21bbe78315a94da5b81e9dde538f9737a7f2c4a53c4eb42ae66]",
    "--alias",
    "admission",
    "--host",
    "[session-local]",
    "--port",
    "[session-local]",
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
    "[template:e3a8a616b2fa4670edc927fe333999e709657ddf8df0fb023dd5b5d01dddd4f6]",
    "--spec-type",
    "none",
    "--reasoning-format",
    "deepseek"
  ],
  "prerequisites": [
    "Separate user approval forPhaseC.",
    "Whole900s trusted broker migration must be active and independently checked.",
    "Verify complete modelSHA after approved storage-checked download; header validation is not full-file verification.",
    "Model/template execution admission with unchanged ECC/VRAM/power/temperature/lease checks.",
    "Native benchmark adapter currently caps8tasks/job; review a one-model-session full-suite adapter or accept honest deadline-truncated evidence. Never silently bypass a contract.",
    "No per-test prompt/budget tuning. Full164 result only if all original tasks and official evaluator complete; otherwise PARTIAL and no full highscore."
  ],
  "profile_id": "omni-derivative-proposal-3",
  "quality_rank": null,
  "quantization": "Q6_K",
  "quantizer": "mradermacher",
  "reason": "Changed BF16 source values and readyQ6. Teacher/dataset/training provenance is weak; test the artifact, not its name.",
  "repository": "mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF",
  "request_options": {
    "cache_prompt": false,
    "chat_template_kwargs": {
      "enable_thinking": true
    },
    "max_tokens": 4096,
    "min_p": 0.0,
    "model": "admission",
    "presence_penalty": 0.0,
    "repeat_penalty": 1.0,
    "return_tokens": true,
    "seed": 1001,
    "stream": false,
    "temperature": 0.6,
    "top_k": 20,
    "top_p": 0.95,
    "verbose": true
  },
  "research_priority_rank": 3,
  "revision": "942ac32ed196d167f90c97aa9aa2a346f4401bf9",
  "runtime": {
    "CPU_threads": 6,
    "GPU_offload_layers": 99,
    "KV_K": "f16",
    "KV_V": "f16",
    "MTP_requested": false,
    "actual_graph_capture": null,
    "batch": 2048,
    "cache_prompt": false,
    "context_tokens": 8192,
    "environment": {
      "GGML_CUDA_GRAPH_OPT": "0",
      "GGML_CUDA_O2_WEIGHT_CACHE_MIB": "0"
    },
    "external_draft": null,
    "flash_attention_effective": null,
    "flash_attention_requested": "on",
    "max_output_tokens": 4096,
    "microbatch": 512,
    "power_limit_w": 300,
    "prefix_reuse_requested": false,
    "sampling": {
      "min_p": 0.0,
      "presence_penalty": 0.0,
      "repeat_penalty": 1.0,
      "seed": 1001,
      "temperature": 0.6,
      "top_k": 20,
      "top_p": 0.95
    },
    "spec_type": "none",
    "thinking_effective": null,
    "thinking_requested": true
  },
  "runtime_identity_note": "Build attests source commit097cf33...; retained adapter contract names ea0c4c2... separately. Neither is silently substituted for a release version. Requested FA/graph settings are not proof of executed kernels.",
  "status": "PROPOSED_NOT_GPU_ADMITTED_NOT_DOWNLOADED",
  "template_sha256": "e3a8a616b2fa4670edc927fe333999e709657ddf8df0fb023dd5b5d01dddd4f6",
  "whole_benchmark_wall_budget_s": 900
}
```

## GUI specialist — separate feasibility gate

```json
{
  "GPU_allowed": false,
  "quality": "NOT MEASURED",
  "repository": "wheattoast11/OmniCoder-9B-Zero-Phase2",
  "requirements": [
    "Resolve whetherPhase2 LoRA is incremental on the namedVisionSFT substrate or standalone on the raw base. Pin exact base, substrate and adapter revisions.",
    "Confirm compatible complete vision tower, processor and matching mmproj after merge; textGGUF alone does not read screenshots.",
    "Review actual llama.cpp LoRA key mapping for text-only versusconditional-generation wrappers. No code execution from model repositories.",
    "BF16 full model alone exceeds16GB; defineFP16 compute + admitted weight quantization, bounded image resolution, KV/workspace budget and measure true VRAM only after approval.",
    "Use frozen offline screenshots andclick oracles; no live desktop/production/HomeAssistant actions."
  ],
  "status": "SEPARATE_GUI_FEASIBILITY_ONLY"
}
```

## Storage snapshot, not a reservation

```json
{
  "download_executed": false,
  "fits_at_observed_time": true,
  "free_bytes": 87955591168,
  "minimum_free_reserve_bytes": 8589934592,
  "observed_at_utc": "2026-10-23T17:41:16.676255+00:00",
  "rule": "Recheck immediately before any future single-file pinned download; reuse exact locally verified artifacts; never replace/delete existing models.",
  "shortlist_weights_published_bytes": 22077779488
}
```

