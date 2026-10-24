# Benchmark register and publisher evidence

**EXTERNAL PUBLISHER SELF-REPORTS are not local measurements.** A mention on a model card does not establish the dataset version, scorer, scaffold or hardware equivalence. HumanEval is distinct from HumanEval+; BFCL v3 is distinct from v4.

## HumanEval+ v0.1.10

| Field | Pinned definition |
| --- | --- |
| benchmark_id | humanevalplus-v0.1.10 |
| benchmark_revision | release:v0.1.10 |
| canonical_reference_exceptions | ["HumanEval/32"] |
| category | coding |
| dataset_split | test |
| dataset_split_hash | 42526ec0e7d5f3ee0b06d6ced98f8c8bae3d76519151bfb3d36f79010645bd7f |
| expected_task_ids_hash | 8c4a9413be6b6b793de94b702ab733ca734db2f5d6bca361605f1d7f71dd9ebe |
| hf_dataset_id | evalplus/humanevalplus |
| hf_latest_observed_revision | d32357cf319e50e9c8d8dab5ea876c72b0fd321b |
| hf_revision_is_not_release_equivalence_proof | True |
| license | Apache-2.0 |
| local_complete_conformant_results | 7 independently replayed full official API records under the declared local evaluation protocol; not publisher-protocol or production qualifications. |
| metric | pass_at_1_percent |
| name | HumanEval+ v0.1.10 |
| official_definition_verified | True |
| provider_repository | https://github.com/evalplus/evalplus |
| required_evaluation_settings | Full164 v0.1.10 IDs; one frozen answer per task; official base AND plus checker and pass@1 estimator; model-native prompt/sampler disclosed. All canonical controls accounted for, including the pinned unchanged upstream HumanEval/32 residual anomaly. No task exclusions or tolerance changes. Local scorer limits: 1GiB cgroup,805306368-byte EVALPLUS memory limit,one CPU,minimum1s/case,GT factor4. Publisher protocol equivalence is NOT VERIFIED. |
| required_task_count | 164 |
| scorer_version | {"git_commit": "26d6d00bb1fd0fa37f39c99d5290da67891d1c5e", "package": "evalplus", "source_sha256": "3c833c39b842e33f251c83db4347e0a95191909f23b390c12d73ab29a28a4daf", "version": "0.3.1 + official find_zero progress fix"} |
| status | DEFINITION_PINNED |
| version | v0.1.10 |

Model-card sources: [prism-ml/Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/b072e1d3b35a0a630cece372c2127528e0994386/README.md)

## MBPP+ v0.2.0

| Field | Pinned definition |
| --- | --- |
| benchmark_id | mbppplus-v0.2.0 |
| benchmark_revision | 64fc4195b858a17cdfdb3324f0baf37939144e14 |
| category | coding |
| dataset_split | test |
| dataset_split_hash | b54e762755248ca411b523c917fa9f93c07b5ff2966bf60b3917b853926a3dad |
| hf_dataset_id | evalplus/mbppplus |
| hf_latest_observed_revision | b2d74c91837c3f2a20c1299ae98133cbe7cfa077 |
| hf_revision_is_not_release_equivalence_proof | True |
| license | Apache-2.0 |
| local_complete_conformant_results | NOT MEASURED |
| metric | pass_at_1_percent |
| name | MBPP+ v0.2.0 |
| official_definition_verified | True |
| provider_repository | https://github.com/evalplus/mbppplus_release |
| required_evaluation_settings | All378 official release problems, official deserializer and special oracles, base AND plus; no original-test-ID filter or resource exclusion. |
| required_task_count | 378 |
| scorer_version | {"package": "evalplus", "version": "0.3.1; exact adapter identity required"} |
| status | DEFINITION_PINNED |
| version | v0.2.0 |

Model-card sources: [prism-ml/Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/b072e1d3b35a0a630cece372c2127528e0994386/README.md)

## BFCL v4 full official evaluator

| Field | Pinned definition |
| --- | --- |
| benchmark_id | bfcl-v4-full |
| benchmark_revision | 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8 |
| category | tool-calling |
| dataset_split | test |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | gorilla-llm/Berkeley-Function-Calling-Leaderboard |
| license | Apache-2.0 |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | BFCL v4 full official evaluator |
| official_definition_verified | False |
| provider_repository | https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard |
| required_evaluation_settings | Freeze the official v4 category manifest and category aggregation. Local100 static subset is not the full leaderboard. The currently fetched HF snapshot documents v3 and is NOT a verified v4 replacement. |
| required_task_count | NOT MEASURED |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | v4 |

Model-card sources: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md), [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md)

## SWE-bench Verified

| Field | Pinned definition |
| --- | --- |
| benchmark_id | swe-bench-verified |
| benchmark_revision | c104f840cc67f8b6eec6f759ebc8b2693d585d4a |
| category | agents |
| dataset_split | test |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | princeton-nlp/SWE-bench_Verified |
| license | NOT MEASURED |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | SWE-bench Verified |
| official_definition_verified | False |
| provider_repository | https://github.com/SWE-bench/SWE-bench |
| required_evaluation_settings | Official500 test instances, pinned Docker/image and evaluator, declared agent scaffold, trials, timeouts and environment; no production tools. |
| required_task_count | 500 |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | Verified |

Model-card sources: [ornith-ai/Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md), [OrionLLM/OxCoder-9B](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md)

## Terminal-Bench 2.1

| Field | Pinned definition |
| --- | --- |
| benchmark_id | terminal-bench-2.1 |
| benchmark_revision | 7131e4375048a0e408a8fb404b5f499d726b695b |
| category | agents |
| dataset_split | test |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | NOT MEASURED |
| license | Apache-2.0 |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | Terminal-Bench 2.1 |
| official_definition_verified | False |
| provider_repository | https://github.com/harbor-framework/terminal-bench-2-1 |
| required_evaluation_settings | Official complete89-task dataset and pinned Harbor evaluator; fix scaffold/parser/context/resources/repetitions and metric. Model-card128K/32CPU/48GB recipes are not assumed locally available. |
| required_task_count | 89 |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | 2.1 |

Model-card sources: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md), [ornith-ai/Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md), [OrionLLM/OxCoder-9B](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md), [XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B/blob/2367e865d009c13ac81713a2878291d33ab28177/README.md)

## BFCL v3 full

| Field | Pinned definition |
| --- | --- |
| benchmark_id | bfcl-v3-full |
| benchmark_revision | NOT MEASURED |
| category | tool-calling |
| dataset_split | NOT MEASURED |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | gorilla-llm/Berkeley-Function-Calling-Leaderboard |
| license | NOT MEASURED |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | BFCL v3 full |
| official_definition_verified | False |
| provider_repository | https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard |
| required_evaluation_settings | Freeze exact release/date window, split, evaluator, agent/scaffold and sampling before admission. No mixed model-card versions. |
| required_task_count | NOT MEASURED |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | NOT MEASURED |

Model-card sources: [prism-ml/Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/b072e1d3b35a0a630cece372c2127528e0994386/README.md), [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md)

## SWE-bench Pro

| Field | Pinned definition |
| --- | --- |
| benchmark_id | swe-bench-pro |
| benchmark_revision | NOT MEASURED |
| category | agents |
| dataset_split | NOT MEASURED |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | ScaleAI/SWE-bench_Pro |
| license | NOT MEASURED |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | SWE-bench Pro |
| official_definition_verified | False |
| provider_repository | https://github.com/scaleapi/SWE-bench_Pro-os |
| required_evaluation_settings | Freeze exact release/date window, split, evaluator, agent/scaffold and sampling before admission. No mixed model-card versions. |
| required_task_count | NOT MEASURED |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | NOT MEASURED |

Model-card sources: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md), [ornith-ai/Ornith-1.5-9B](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md), [OrionLLM/OxCoder-9B](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md)

## LiveCodeBench

| Field | Pinned definition |
| --- | --- |
| benchmark_id | livecodebench |
| benchmark_revision | NOT MEASURED |
| category | coding |
| dataset_split | NOT MEASURED |
| dataset_split_hash | NOT MEASURED |
| hf_dataset_id | livecodebench/code_generation_lite |
| license | NOT MEASURED |
| local_complete_conformant_results | NOT MEASURED |
| metric | official_evaluator_report |
| name | LiveCodeBench |
| official_definition_verified | False |
| provider_repository | https://github.com/LiveCodeBench/LiveCodeBench |
| required_evaluation_settings | Freeze exact release/date window, split, evaluator, agent/scaffold and sampling before admission. No mixed model-card versions. |
| required_task_count | NOT MEASURED |
| scorer_version | NOT MEASURED |
| status | DEFINITION_REQUIRES_ADMISSION |
| version | NOT MEASURED |

Model-card sources: [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md), [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md), [prism-ml/Ternary-Bonsai-2-27B-gguf](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/b072e1d3b35a0a630cece372c2127528e0994386/README.md), [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it/blob/707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7/README.md)

## BFCL v4 Simple Python — complete400 category

| Field | Pinned definition |
| --- | --- |
| benchmark_id | bfcl-v4-simple-python-full400 |
| benchmark_revision | 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8 |
| category | native_tools |
| dataset_split | official simple_python entire category |
| dataset_split_hash | 82dd63ba502eb2520c6b5d1d9a5c4b590e03ff261565175561f6228a367d1991 |
| existing_CPU_controls_reused | {"negative_controls": 1200, "positive_controls": 400, "simple_python_schemas": 400} |
| expected_task_ids_hash | 284fd37e027916e261462b977d9ff61dd129fcade6566a94c709c3430ac1e836 |
| hf_dataset_id | NOT MEASURED |
| hf_snapshot_equivalence | NOT VERIFIED: the current HF dataset snapshot is v3; no substitute for this Git-pinned v4 category. |
| license | Apache-2.0 |
| local_complete_conformant_results | NOT MEASURED |
| metric | bfcl_simple_python_ast_accuracy_percent |
| model_card_relation | BFCLv4 family mentions only; no same-category publisher result assumed. |
| name | BFCL v4 Simple Python — complete400 category |
| official_definition_verified | True |
| original100_pilot_overlap | 20 |
| per_model_progress_scope | Model-specific coverage is tracked in experiment/campaign evidence, not a global remaining count. |
| preparation_audit_sha256 | b05f0509061815926a201c9b6217a00019356d6ea6cd20129a4dd299301aa3fc |
| prerequisites | ["Collect or exactly reuse all400 unique category task answers under one declared per-model configuration.", "Independently verify input/schema/score/configuration identities and complete original official AST aggregation; preserve separate practical protocol scores.", "No whole-BFCL, publisher-protocol equivalence or assistant qualification claim from this one category."] |
| provider_repository | https://github.com/ShishirPatil/gorilla/tree/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard |
| reference_answers_sha256 | 90cd5bc653690ee8e459b5b3f3fc9458606f7f3fcbf795bb51b7dc581f8c86dc |
| required_evaluation_settings | All400 official category IDs and official AST category aggregation, declared native template/sampler and unchanged task/function schemas. The old20 answers may be reused only for identical verified configuration/input/answer identities. This category is not the complete BFCLv4 overall leaderboard. |
| required_task_count | 400 |
| scorer_version | {"aggregation": "correct_count / len(model_result); complete400 IDs required", "frozen_checker_adapter_sha256": "a926f83c9dd9fdba5465c3c7c6a02ec31ace9206b91f06fa27f6d7f077363710", "frozen_checker_bundle_sha256": "657dbc00ab40c23a53173b758d6a25e4806a18cd64c10118148b473114042236", "native_score_wrapper_sha256": "585f63055c4abc62057cdb2c51764b3147f2621f9ca4bb1594d2227a5302bfd1", "official_aggregation_helper_sha256": "7c756592af53eb54733989aa03a3fa87854f1c20dd566f3f10a770e17d25a9d7", "official_eval_runner_sha256": "b1033684908819ccb312d4d0e2c563359d69247412f00206013b2292b0e3ce81", "official_native_format_sha256": "3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd", "official_revision": "6ea57973c7a6097fd7c5915698c54c17c5b1b6c8"} |
| status | OFFICIAL_CATEGORY_DEFINITION_AND_NATIVE_ADAPTER_REVIEWED_FULL_MODEL_RESULT_PENDING |
| version | v4, entire simple_python category only |

Model-card sources: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md), [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md)

## BFCL v4 Parallel Multiple — complete200 category

| Field | Pinned definition |
| --- | --- |
| benchmark_id | bfcl-v4-parallel-multiple-full200 |
| benchmark_revision | 6ea57973c7a6097fd7c5915698c54c17c5b1b6c8 |
| category | native_tools |
| dataset_split | official parallel_multiple entire category |
| dataset_split_hash | 8863ea8433239f55c5f016154cf0830853c89f693c6ea270396a2fa121960579 |
| existing_CPU_controls_reused | {"negative_controls": 600, "parallel_multiple_schemas": 200, "positive_controls": 200} |
| expected_task_ids_hash | 8bf603cd74927e071664bcd4594c0738616480c9da7c0e86999d112a9646da59 |
| hf_dataset_id | NOT MEASURED |
| hf_snapshot_equivalence | NOT VERIFIED: the current HF dataset snapshot is v3; no substitute for this Git-pinned v4 category. |
| license | Apache-2.0 |
| local_complete_conformant_results | NOT MEASURED |
| metric | bfcl_parallel_multiple_ast_accuracy_percent |
| model_card_relation | BFCLv4 family mentions only; no same-category publisher result assumed. |
| name | BFCL v4 Parallel Multiple — complete200 category |
| official_definition_verified | True |
| per_model_progress_scope | Model-specific coverage is tracked in experiment/campaign evidence, not a global remaining count. |
| preparation_audit_sha256 | 2e28c35d1726e9c9b45ec343616ab10a26326bfa7c9c8bc9ed99a5b61ca0056b |
| provider_repository | https://github.com/ShishirPatil/gorilla/tree/6ea57973c7a6097fd7c5915698c54c17c5b1b6c8/berkeley-function-call-leaderboard |
| reference_answers_sha256 | 5ebf24f458c1f16300c05505d83d6f0a1b68b79be273a033febd0d4f840507e3 |
| required_evaluation_settings | All200 original official parallel_multiple IDs, unchanged native function schemas and official AST category aggregation. Declared model-native template/sampler/output/context. Technical context preflight is not a quality filter. Complete category only, not full BFCL leaderboard or equivalent publisher harness. |
| required_task_count | 200 |
| scorer_version | {"aggregation": "correct_count / len(model_result); complete200 parallel_multiple IDs required", "frozen_checker_adapter_sha256": "a926f83c9dd9fdba5465c3c7c6a02ec31ace9206b91f06fa27f6d7f077363710", "frozen_checker_bundle_sha256": "657dbc00ab40c23a53173b758d6a25e4806a18cd64c10118148b473114042236", "native_score_wrapper_sha256": "3478606c296e65ef9088c96a7f1c79e99b49bc7016a44c77b3719d14e4dd6666", "official_aggregation_helper_sha256": "7c756592af53eb54733989aa03a3fa87854f1c20dd566f3f10a770e17d25a9d7", "official_eval_runner_sha256": "b1033684908819ccb312d4d0e2c563359d69247412f00206013b2292b0e3ce81", "official_native_format_sha256": "3703b9bb63f83581c60b8e0b82aac74c360c9ca781e99e7d4eb28b0cce2285dd", "official_revision": "6ea57973c7a6097fd7c5915698c54c17c5b1b6c8"} |
| status | OFFICIAL_CATEGORY_DEFINITION_VERIFIED_MODEL_RESULTS_PENDING |
| version | v4, entire parallel_multiple category only |

Model-card sources: [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md), [LiquidAI/LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md)

## Verified cached model cards

| Model | Revision / source SHA256 | Reported benchmark families | Architecture declared by source | Card |
| --- | --- | --- | --- | --- |
| Qwen/Qwen3.8-27B | 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0 / 57e4bdb258ee1a7d2635c5174ebd4e56abe392505cdb5f8bbb356b0dc4293641 | swe-bench-pro, terminal-bench-2.1, terminal-bench-unspecified, livecodebench | ["Qwen3_5ForConditionalGeneration"] | [source](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) |
| ornith-ai/Ornith-1.5-9B | 489cb97981b8654bcfcf30ce1f94ed1b62e07b53 / 7a03f9b2b2d7e12e740df3bb5af43c82837aad9dd9b945de7c0a67ac4ee5998f | swe-bench-verified, swe-bench-pro, terminal-bench-2.1, terminal-bench-unspecified | ["Qwen3_5ForConditionalGeneration"] | [source](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md) |
| Qwen/Qwen3.5-9B | c202236235762e1c871ad0ccb60c8ee5ba337b9a / c5f5a8c2dddab69cfbf05279235aa5fddb137939a06539c4c7637aa900fef6d0 | bfcl-v4, bfcl-unspecified, livecodebench | ["Qwen3_5ForConditionalGeneration"] | [source](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md) |
| OrionLLM/OxCoder-9B | 07ba04e2149bace1b43c66448471a70378a7a708 / c26991b9b7b6efcda0d067f75c7ebb4322384b66745b936a3808b8bebddc6246 | swe-bench-verified, swe-bench-pro, terminal-bench-2.1, terminal-bench-unspecified | ["Qwen3_5ForConditionalGeneration"] | [source](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md) |
| XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B | 2367e865d009c13ac81713a2878291d33ab28177 / 09f915ac8116db54ca78586cfdf9ddb14209cba1ca23561a202f38039eac95ca | terminal-bench-2.1, terminal-bench-unspecified | ["Qwen3_5ForConditionalGeneration"] | [source](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B/blob/2367e865d009c13ac81713a2878291d33ab28177/README.md) |
| prism-ml/Ternary-Bonsai-2-27B-gguf | b072e1d3b35a0a630cece372c2127528e0994386 / 98f4a6c74b5e88a4039cad9a343269bc458b303accd21ed95bbdac42b387d2c9 | humanevalplus, mbppplus, bfcl-v3, bfcl-unspecified, livecodebench | null | [source](https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf/blob/b072e1d3b35a0a630cece372c2127528e0994386/README.md) |
| google/gemma-4-12B-it | 707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7 / 04a06469e3d83b941eaa776a3647b8690b5a7cc5c833af2381e5345bb1bb45c0 | livecodebench | ["Gemma4UnifiedForConditionalGeneration"] | [source](https://huggingface.co/google/gemma-4-12B-it/blob/707f0a3b8a3c7ad586ed01e27eafbad8a27dd0f7/README.md) |
| LiquidAI/LFM2.5-8B-A1B | 5dd22602c2e9f6a097b1de4c4efe0658b605015c / eb40f5396ef5200a14240f8c0523b269bcc114f40b153ac2fa9017dad391e59b | bfcl-v4, bfcl-v3 | ["Lfm2MoeForCausalLM"] | [source](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md) |

## Publisher numeric claims — never local highscores

Reported numeric cells retain the publisher’s scale. Protocol matching and local reproducibility remain unverified; no conversion to local percentage or cross-model ranking is performed.

| Model / publisher column | Reported label | Reported value | Scale / comparability | Source |
| --- | --- | --- | --- | --- |
| Qwen/Qwen3.8-27B / Qwen3.8-27B | Agentic terminal codingTerminal Bench 2.1 (Terminus) | 73.0 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) |
| Qwen/Qwen3.8-27B / Qwen3.8-27B | Agentic codingSWE-bench Pro | 61.7 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) |
| Qwen/Qwen3.8-27B / Qwen3.8-27B | Competitive codingLiveCodeBench v6 | 90.3 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) |
| ornith-ai/Ornith-1.5-9B / Ornith-1.5-9B | Terminal-Bench 2.1 (Terminus-2) | 46.2 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md) |
| ornith-ai/Ornith-1.5-9B / Ornith-1.5-9B | Terminal-Bench 2.1 (Claude Code) | 47.0 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md) |
| ornith-ai/Ornith-1.5-9B / Ornith-1.5-9B | SWE-bench Verified | 70.6 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md) |
| ornith-ai/Ornith-1.5-9B / Ornith-1.5-9B | SWE-bench Pro | 47.5 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/ornith-ai/Ornith-1.5-9B/blob/489cb97981b8654bcfcf30ce1f94ed1b62e07b53/README.md) |
| Qwen/Qwen3.5-9B / Qwen3.5-9B | LiveCodeBench v6 82.7 | 65.6 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md) |
| Qwen/Qwen3.5-9B / Qwen3.5-9B | BFCL-V4 -- | 66.1 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md) |
| OrionLLM/OxCoder-9B / OxCoder-9B | Agentic terminal codingTerminal-Bench 2.1 (Terminus-2) | 49.6 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md) |
| OrionLLM/OxCoder-9B / OxCoder-9B | Agentic terminal codingTerminal-Bench 2.1 (Claude Code) | 50.8 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md) |
| OrionLLM/OxCoder-9B / OxCoder-9B | Agentic codingSWE-bench Verified | 73.5 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md) |
| OrionLLM/OxCoder-9B / OxCoder-9B | Real-world software engineeringSWE-bench Pro | 49.1 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/OrionLLM/OxCoder-9B/blob/07ba04e2149bace1b43c66448471a70378a7a708/README.md) |
| XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B / MiMo-V2.6-Distill-Qwen-9B (SFT) | General Terminal Bench 2.1 | 37.1 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B/blob/2367e865d009c13ac81713a2878291d33ab28177/README.md) |
| LiquidAI/LFM2.5-8B-A1B / LFM2.5-8B-A1B | BFCLv3 45.07 | 64.36 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md) |
| LiquidAI/LFM2.5-8B-A1B / LFM2.5-8B-A1B | BFCLv4 25.52 | 48.5 | PUBLISHER_REPORTED_UNCONFIRMED_SCALE / NOT VERIFIED | [card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/5dd22602c2e9f6a097b1de4c4efe0658b605015c/README.md) |

## Independent CPU replay of archived model answers

These are verification events for existing measurements, **not new GPU runs**. Official scoring functions and pass@1 aggregation were replayed through a streaming API adapter, preserving all164 tasks and the known upstream canonical-reference exception. The full optional CLI was not used; evaluation memory limits remain explicitly local. This verifies archived judgments without implying publisher-protocol equivalence or automatic official highscore qualification.

| Original experiment | Full task coverage | Confirmed successes | Changed judgments | Verification audit |
| --- | --- | --- | --- | --- |
| R217 | 164 | 132 | 0 | [audit-d308fd8d22dee385af6d](audits/audit-d308fd8d22dee385af6d.md) |
| R255 | 164 | 132 | 0 | [audit-d308fd8d22dee385af6d](audits/audit-d308fd8d22dee385af6d.md) |
| R425 | 164 | 149 | 0 | [audit-d308fd8d22dee385af6d](audits/audit-d308fd8d22dee385af6d.md) |
| R117 | 164 | 148 | 0 | [audit-d308fd8d22dee385af6d](audits/audit-d308fd8d22dee385af6d.md) |
| R118 | 164 | 150 | 0 | [audit-d308fd8d22dee385af6d](audits/audit-d308fd8d22dee385af6d.md) |
| R254 | 164 | 117 | 0 | [audit-58f7f002ffc04c7f34a7](audits/audit-58f7f002ffc04c7f34a7.md) |
| R279 | 164 | 151 | 0 | [audit-58f7f002ffc04c7f34a7](audits/audit-58f7f002ffc04c7f34a7.md) |

## Unreachable / unresolved model-card identities

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "model_repository": "Tesslate/OmniCoder-2-9B",
    "note": "Do not substitute OmniCoder-9B or a quantizer card as the same model/version.",
    "source_check": "omni_api",
    "status": "UNREACHABLE_AT_REVIEW"
  }
]
```

</details>

## Source retrieval receipts

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "bfcl_hf": {
    "bytes": 3668,
    "license": "apache-2.0",
    "repository": "gorilla-llm/Berkeley-Function-Calling-Leaderboard",
    "revision": "61fc0608cfd831fcfbbaa676ebdfef0ed963eeda",
    "sha256": "48328df2f68d22dcc29a2022e4c6031889daf669611ddb1142ffa1ce00eacf55",
    "status": "FETCHED",
    "url": "https://huggingface.co/api/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard"
  },
  "humaneval_hf": {
    "bytes": 1257,
    "license": "apache-2.0",
    "repository": "evalplus/humanevalplus",
    "revision": "d32357cf319e50e9c8d8dab5ea876c72b0fd321b",
    "sha256": "619cbedbfefefd1c58b7b859573f0a9d3ba7c4c839385e876fc033855f9910ea",
    "status": "FETCHED",
    "url": "https://huggingface.co/api/datasets/evalplus/humanevalplus"
  },
  "mbpp_hf": {
    "bytes": 1148,
    "license": "apache-2.0",
    "repository": "evalplus/mbppplus",
    "revision": "b2d74c91837c3f2a20c1299ae98133cbe7cfa077",
    "sha256": "caf68384a2bf6ab3218ddcc9723c524b8539ce795c96bf465c2a0cc1f7b52c53",
    "status": "FETCHED",
    "url": "https://huggingface.co/api/datasets/evalplus/mbppplus"
  },
  "omni_api": {
    "error": "HTTPError: HTTP Error 401: Unauthorized",
    "status": "UNREACHABLE",
    "url": "https://huggingface.co/api/models/Tesslate/OmniCoder-2-9B"
  },
  "omni_card": {
    "error": "HTTPError: HTTP Error 401: Unauthorized",
    "status": "UNREACHABLE",
    "url": "https://huggingface.co/Tesslate/OmniCoder-2-9B/raw/main/README.md"
  },
  "swe_hf": {
    "bytes": 1994,
    "license": null,
    "repository": "princeton-nlp/SWE-bench_Verified",
    "revision": "c104f840cc67f8b6eec6f759ebc8b2693d585d4a",
    "sha256": "87d6e7d0a2402c4eba9b438cd5bcbdc71bada8518df3edbde35250c2dde94394",
    "status": "FETCHED",
    "url": "https://huggingface.co/api/datasets/princeton-nlp/SWE-bench_Verified"
  },
  "terminal_license": {
    "bytes": 11357,
    "sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "status": "FETCHED",
    "url": "https://raw.githubusercontent.com/harbor-framework/terminal-bench-2-1/main/LICENSE"
  },
  "terminal_readme": {
    "bytes": 4624,
    "sha256": "70de9a9a5f040c4e5f39a411d8e925611e37650562959a031e1202bd7f4af321",
    "status": "FETCHED",
    "url": "https://raw.githubusercontent.com/harbor-framework/terminal-bench-2-1/main/README.md"
  },
  "terminal_repo": {
    "bytes": 7186,
    "revision": "7131e4375048a0e408a8fb404b5f499d726b695b",
    "sha256": "197957c3fb032567fbf5bec2456319eadd9b23cde836e0a3da1c248e518831b4",
    "status": "FETCHED",
    "url": "https://api.github.com/repos/harbor-framework/terminal-bench-2-1/commits/main"
  }
}
```

</details>

## Transparent admission-policy corrections

| Previous definition identity | Correction / preserved boundaries |
| --- | --- |
| bench-cd00cbe0bd8dc4e4024ca32e47d28496abf2400f18f5e476d1f91c3b609b616f | The initial project admission wording required every canonical reference to pass. Source/API replay proves the documented HumanEval/32 residual anomaly also occurs under the exact official oracle. Permit that explicitly pinned upstream anomaly without dropping any task, changing tolerance or changing the official scorer. This is a transparent admission-policy correction, not a changed score or dataset. |
| bench-e4fd06b46fd684c2f281978d02c31df1f37ec3f4934f2194e07ca341ab1fc672 | Pinned category scorer/aggregation and reviewed native adapter admitted; no model result admitted. |

## Source and definition checks — no model results

| Verification | Date | New GPU runs | Model results admitted | Source audit |
| --- | --- | --- | --- | --- |
| BFCL_FULL400_CATEGORY_DEFINITION_ADMISSION | 2026-10-23T12:06:36.040369+00:00 | 0 | 0 | [audit-c4fd1b463dd5f4e884bb](audits/audit-c4fd1b463dd5f4e884bb.md) |

