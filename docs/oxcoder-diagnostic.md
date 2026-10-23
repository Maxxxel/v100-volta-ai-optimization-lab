# OxCoder R448: archived response diagnosis

Read-only investigation of [issue12](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/12). **No new GPU runs, model requests or changes to original benchmark results.**

## Confirmed observations

All104 empty final responses reached4096 completion tokens with `finish_reason=length`. Their archived reasoning equals the complete raw text, with no closing thinking tag. All60 nonempty final responses contain the closing tag and their final-channel text matches the text after that tag. This establishes an exhausted output budget before final-answer emission in the recorded profile; it does not prove why the model reasons for so long.

| Group | Tasks | Passed | Wall sum s | Median s | P90 s | Completion tokens | Recorded decode tok/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| All | 164 | 53 | 8303.198969689 | 59.9503553765 | 60.2242152373 | 566326 | 68.3965110398731 |
| Empty final | 104 | 0 | 6247.526179799 | 59.9991166155 | 60.308621765000005 | 425984 | 68.3448612162287 |
| Final present | 60 | 53 | 2055.67278989 | 39.113010691 | 57.4451959663 | 140342 | 68.55376439148269 |

Original success remains 53/164. Empty-final requests consumed 75.24% of summed request latency. Median and linearly interpolated P90 at position(n-1)*0.9; request wall sums exclude startup/warmup/scoring. Reasoning characters are not token counts. Exact reasoning-token counts were not supplied by the API: **NOT RECORDED**. Completion-token counts are measured; they are not silently relabelled reasoning-token counts.

## Parser, template and scoring checks

```json
{
  "assistant_history_requests": 0,
  "context_truncated_requests": 0,
  "empty_alternative_closing_markers": 0,
  "empty_reasoning_equals_raw_trimmed": 104,
  "explicit_reasoning_token_counts_available": 0,
  "nonempty_final_equals_raw_post_close_trimmed": 60,
  "prompt_opens_think": 164
}
```

The frozen template preopens thinking. The `deepseek` response mode separates reasoning into its own field. No unrecognised closing-tag variant or missing post-close final text is observed. The source meaning of `--no-reasoning-preserve` concerns retained assistant history; none of these requests contains prior assistant messages. This is not evidence that toggling that flag would fix the failures. The scorer correctly used final content under its declared answer contract; reasoning-only fenced code is not retroactively promoted to a valid answer.

## Historical profiles: comparison limits

| Experiment | Profile | Endpoint / protocol | Output cap | MTP | Solved | Median s | P90 s | Completion tokens | Empty final |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R217 | OmniCoder2 9B Q6_K grafted | /completion; historical non-thinking task profile, not the R448 chat protocol | 1024 | True | 132/164 | 1.313699555 | 2.5980146812000013 | 36785 | 0 |
| R255 | Qwen3.5 9B Q4_K_M | /completion; historical non-thinking task profile, not the R448 chat protocol | 1024 | False | 132/164 | 2.2581174534999997 | 4.305586797600004 | 41845 | 0 |

OmniCoder2 and Qwen3.5 used preclosed thinking prompts, greedy temperature0 and a1024-token limit through the historical completion endpoint. OxCoder used native chat, thinking enabled, temperature1 and4096 tokens. Quantization, weights and MTP also differ. These are **whole-profile historical observations**, not causal proof of intrinsic model speed or superiority.

## Weight identity: higher-priority hold on further OxCoder GPU work

A [reported upstream tensor-identity concern](https://huggingface.co/OrionLLM/OxCoder-9B/discussions/3) was acknowledged by the maintainer as a possible export/checkpoint problem. That report is external evidence, not our completed independent tensor census. Our retrieved HF metadata shows that the currently published safetensors LFS object equals the original upload. No corrected weight payload is established by that history. The tested Q6 artifact matches its pinned quantizer identity, but exact conversion lineage to an upstream checkpoint is not supplied.

The independent header inspection finds760 shared tensors and15 additional Qwen MTP tensors;48 shared tensors have different stored dtypes. Headers alone do not prove equal values. The source tensor-payload census is tracked separately and must not be prematurely labelled complete. All further OxCoder optimization proposals below are **on hold pending weight-identity review**, in addition to their separate GPU-approval and900-second requirements.

```json
{
  "at_utc": "2026-10-23T15:54:46.056325+00:00",
  "external_claim": {
    "maintainer_response": "Acknowledged tensor comparison and said the export/checkpoint path would be investigated; acknowledgment is not a corrected-weight release.",
    "status": "EXTERNALLY REPORTED; independent payload census in progress",
    "url": "https://huggingface.co/OrionLLM/OxCoder-9B/discussions/3"
  },
  "independent_header_inventory": {
    "Qwen_only_tensors": [
      "mtp.fc.weight",
      "mtp.layers.0.input_layernorm.weight",
      "mtp.layers.0.mlp.down_proj.weight",
      "mtp.layers.0.mlp.gate_proj.weight",
      "mtp.layers.0.mlp.up_proj.weight",
      "mtp.layers.0.post_attention_layernorm.weight",
      "mtp.layers.0.self_attn.k_norm.weight",
      "mtp.layers.0.self_attn.k_proj.weight",
      "mtp.layers.0.self_attn.o_proj.weight",
      "mtp.layers.0.self_attn.q_norm.weight",
      "mtp.layers.0.self_attn.q_proj.weight",
      "mtp.layers.0.self_attn.v_proj.weight",
      "mtp.norm.weight",
      "mtp.pre_fc_norm_embedding.weight",
      "mtp.pre_fc_norm_hidden.weight"
    ],
    "common_tensors": 760,
    "dtype_mismatches": 48,
    "header_comparison_is_payload_comparison": false,
    "ox_tensors": 760,
    "qwen_tensors": 775,
    "shape_mismatches": 0
  },
  "local_R448_artifact": {
    "bytes": 7359268288,
    "current_published_LFS_matches": true,
    "fresh_redundant_full_local_hash": false,
    "full_weight_hash_was_already_verified_by_original_artifact_admission_and_per_job_broker": true,
    "original_R290_audit_sha256": "e1c1453a8a998cb3545fb54ec2a9808c93bfd8b63cdddcd909c4d2da7049bab8",
    "quantizer_repository": "mradermacher/OxCoder-9B-GGUF",
    "quantizer_revision": "525d7144604d67d86d138cde41e93c7bb545f82a",
    "sha256": "468e7c0d6806033050271a8f29d4fefb38f7d376e2f91ce5d442669244b3d82f"
  },
  "next_decision": "Hold all OxCoder GPU optimization follow-ups pending the independent tensor census and resolution of source-to-Q6 lineage. Existing53/164 remains an observed score of the pinned tested artifact, not evidence of advertised fine-tuning superiority or inferiority.",
  "source_lineage": {
    "exact_quantizer_to_upstream_checkpoint_derivation": "NOT VERIFIED",
    "implication": "A Q6 artifact identity is proven, its exact upstream trained-checkpoint provenance is not. Do not claim the advertised fine-tuning quality from the R448 score.",
    "original_R290_provenance_warning": "QuantizerdeclaresOrionLLM/OxCoder-9B;doesnotpublishcryptographicupstreamcommitderivation. Originalmodelpin07ba04e...andquantizerpin525d714...recordedseparately."
  },
  "sources": {
    "SAFETENSORS_HEADERS.json": "4128473faab475ea7eb5921c3f2e091a82bb3a3307d29a72ac11dcb8e94ff0ec",
    "discussion-3.json": "b478e9a3410a6b95d1d035156ae0a62530da161dfe48b23cef4d5039592db47c",
    "oxcoder-commits.json": "e8c810034f8f98b71690e89579bc5893f9e1a062ff11429fb7571fe4029acb6a",
    "oxcoder-current.json": "6e29b7efcbfb148d24f6e2b824c962d37915b653b3527f1130394c64bf5b591d",
    "oxcoder-gguf-current.json": "382e30b6f9c73c1d40e79569533ef33224ba788f69b67fde349cc12937b72d77",
    "oxcoder-original-upload.json": "67ded87262a61eac799e856930239fcceb154a13cb6ba0fc3964f1159b36bff1",
    "qwen35-current.json": "78b92ec8a24e68cea1aa24dfb935511b959d9fb8472d43bd66fe64652c9974cf"
  },
  "upstream_safetensors": {
    "current_equals_original_upload_LFS": true,
    "current_file_SHA256_reported_by_HF": "d4fca6821fe35b46e684ab88217ec25cdbfcdf9fa208c01110be95a200fcc33b",
    "current_revision": "07ba04e2149bace1b43c66448471a70378a7a708",
    "limitation": "HF commit/file metadata was independently retrieved; full safetensors file SHA was not independently streamed yet.",
    "original_upload_revision": "301439404fbf6d483b303c172e90591627483caf",
    "post_discussion_corrected_weight_payload_evidence_found": false,
    "repository": "OrionLLM/OxCoder-9B"
  }
}
```

[audit-7469da0fdc13596f8c53](audits/audit-7469da0fdc13596f8c53.md)

## Frozen R448 profile

```json
{
  "MTP": false,
  "binary_sha256": "08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54",
  "context": 8192,
  "model_sha256": "468e7c0d6806033050271a8f29d4fefb38f7d376e2f91ce5d442669244b3d82f",
  "output_cap": 4096,
  "reasoning_format": "deepseek",
  "reasoning_preserve": false,
  "temperature": 1.0,
  "template_sha256": "d203f3342d8a7f8474dd55563eece3a26e71b21c6f667c9db9c93b762b3bf997",
  "thinking": true,
  "top_k": 0,
  "top_p": 0.95
}
```

## Proposed isolated follow-up — not executed

**Separate GPU approval is required by issue12, as is trusted enforcement of the900-second budget for the entire paired trial.** No GPU experiment is authorized or started by this report. P0 changes only explicit thinking true versus false; P1 separately tests a genuine1024-token reasoning budget inside an unchanged4096 total output budget. Native-template switching and actual reasoning-budget support must be verified before execution. Four frozen development cases are proposed; no official HumanEval failures are selected for tuning. This screen cannot qualify a general benchmark winner.

```json
{
  "common_constraints": {
    "applies_to_all_parts_and_both_arms_combined": true,
    "cache_prompt": false,
    "max_generation_requests": 8,
    "model_loads": 2,
    "no_productive_changes": true,
    "observed_prompt_template_must_confirm_switch": true,
    "parallel_GPU_jobs": 0,
    "same_task_order": true,
    "sampler": "temperature1.0/top_p0.95/top_k0/min_p0/repeat_penalty1/presence0",
    "seed": 1001,
    "whole_benchmark_seconds": 900
  },
  "development_inputs": {
    "case_ids": [
      "code",
      "sorting",
      "filtering",
      "log_injection"
    ],
    "prompts": "Original frozen questions unchanged; development screen only. No official test tasks selected by failure outcome.",
    "scoring": "Existing deterministic QA semantic/format/safety gates; code evaluated only inside original CPU sandbox. Source task per-case output limits overridden uniformly to4096 for both arms; do not conflate this diagnostic with the original QA12 score.",
    "sha256": "6a901906898710ff9d319771c5ce33f4322b2cee27a098ecafdbf4d4da9c346b"
  },
  "early_stop": [
    "Hard900s for entire paired trial; retain partial raw data and do not report a full score.",
    "Hardware/ECC/VRAM/power/temperature/broker lease failure.",
    "Any source/weight/template hash mismatch or unverifiable thinking-mode switch."
  ],
  "not_justified": [
    "Re-scoring reasoning text as final code would change answer-selection semantics and is not an admissible correction.",
    "Changing only --no-reasoning-preserve is not a remedy established by these single-turn tasks; no previous assistant trace exists.",
    "Do not simultaneously change thinking, sampler, engine, context and output cap and call it an isolated optimization.",
    "Do not replay all164 HumanEval tasks for tuning; independent validation must disclose prior test exposure."
  ],
  "practical_minimum": "At least20% lower paired task latency or removal of observed empty-final failures, with all previously successful development tasks still passing; one screen is not independent winner qualification.",
  "primary_metric": "Successful development tasks per total paired-arm inference second; zero quality/safety regression required. No general benchmark qualification from n4.",
  "proposals": [
    {
      "A": {
        "chat_template_kwargs.enable_thinking": true
      },
      "B": {
        "chat_template_kwargs.enable_thinking": false
      },
      "admission_prerequisites": [
        "Pin original native recipe and template to the recorded binary/model hashes.",
        "Validate the non-thinking native template path and captured prompt suffix without model generation.",
        "Register a closed dev-dataset adapter/profile; an existing profile must not be mutated.",
        "Enforce trusted whole-trial900s deadline including both arms, preflight/load/warmup/collection.",
        "Obtain the separate GPU approval required by issue12."
      ],
      "all_other_parameters_fixed": true,
      "factor": "Thinking template switch, single factor",
      "hypothesis": "Suppressing the open thinking prefix may make final output available within the4096-token cap and reduce latency; quality benefit unverified.",
      "priority": "P0"
    },
    {
      "A": {
        "reasoning_budget": "unrestricted, actual baseline must be captured",
        "thinking": true
      },
      "B": {
        "reasoning_budget": 1024,
        "thinking": true
      },
      "admission_prerequisites": [
        "Local source exposes --reasoning-budget; verify the actual tokenizer/parser and generated closing-marker path before admitting the trial.",
        "Same independent approval and900s whole-trial gate as P0."
      ],
      "all_other_parameters_fixed": true,
      "factor": "Reasoning-token budget, separate single-factor trial",
      "hypothesis": "A true reasoning-token cap may leave capacity for final code inside the unchanged4096 total output budget. No claim that this is already supported correctly by the actual parser/sampler path.",
      "priority": "P1"
    }
  ],
  "secondary_metrics": [
    "empty_final_content",
    "finish_reason",
    "completion_tokens",
    "reasoning_tokens_only_if_explicitly_recorded",
    "prefill_decode_timings",
    "request_wall_s",
    "GPU_joules_per_success",
    "peak_VRAM"
  ],
  "source_review": {
    "engine_argument_source_file": "common/arg.cpp",
    "engine_argument_source_sha256": "449cd9be39dd477c751a8575e99b4deee737ae85a698e1c8bac7c22f28a9d151",
    "interpretation": "Pinned local source review supports flag meanings; runtime behavior is established separately by the recorded native responses. The snapshot reports no upstream commit.",
    "preserve_reasoning_source_lines": [
      3755,
      3767
    ],
    "reasoning_budget_source_lines": [
      3739,
      3746
    ],
    "reasoning_format_source_lines": [
      3699,
      3705
    ],
    "template_sha256": "d203f3342d8a7f8474dd55563eece3a26e71b21c6f667c9db9c93b762b3bf997"
  },
  "status": "PROPOSED_REQUIRES_SEPARATE_GPU_APPROVAL_AND_HARD_WHOLE_BENCHMARK_900S_ADMISSION"
}
```

## Evidence and remaining hypotheses

Source experiment SHA256: `bb7e7ca493d0666a21c6b74d231f0c3ecb6144b140ce9477ca25eb92cb0ae4f5`. Diagnostic SHA256: `d9eefff3d6c2342adfb07fbe83ae63493e9d29bf7eb4ff628852b001c5d9b4fa`. Follow-up plan SHA256: `0e97dd72c90af4703b6fcf52363877460104c46359b10cbcba5c9327cdc10558`. [audit-d9eefff3d6c2342adfb0](audits/audit-d9eefff3d6c2342adfb0.md), [audit-0e97dd72c90af4703b6f](audits/audit-0e97dd72c90af4703b6f.md)

**LOCALLY MEASURED:** the original outputs, finish reasons, counters, timing and unchanged score. **LOCAL SOURCE REVIEW:** template and flag meanings, with source hashes in the plan. **NOT VERIFIED:** benefit or quality of thinking-off/budgeted thinking, larger-output profiles, parser alternatives and cross-model causal effects. Original inputs, answers and judgments remain unchanged.

