# Model screening

**4/13 profiles measured** · 16 coding + 16 mock-tool development tasks.

<input id="screening-search" type="search" placeholder="Filter models or status" aria-label="Filter screening models">

<div class="screening-wrap"><table id="screening-table"><thead><tr><th>Model</th><th>Status</th><th>Coding /16</th><th>Mock tools /16</th><th>Request time s</th><th>Output tok/s¹</th><th>GPU J/success ≥²</th><th>VRAM MiB</th><th>Existing benchmarks</th><th>Details</th></tr></thead><tbody><tr><td>OmniCoder-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>13/16 · 81.2%</td><td>14/16 · 87.5%</td><td>67.2</td><td>69.6</td><td>593.8</td><td>7,356.5</td><td><a href="../results/#r471">R471 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;29208867310ffb6d01c8051d11831d1b464074f17a0dca03460c8e08c67d303c&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b&quot;,
    &quot;parent_profile_id&quot;: &quot;omni-q6-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b&quot;,
        &quot;family_id&quot;: &quot;omni&quot;,
        &quot;hf_repository&quot;: null,
        &quot;hf_revision&quot;: null,
        &quot;name&quot;: &quot;OmniCoder 9B&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;OmniCoder-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-b3c9c6dbe4a099a075a8bb6b7b5a98244616c2d014f1f94f625f1dfe5e2f943c&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;auto&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: false
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-26d5b175a8e379f00193da2b2de4bce97c7d89fdc2bacf55b6971d71cb22f28e&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;af39ac42f3d0913c6f34517990991c851cd6fdd34c904180e7df4b8ad3ad40f6&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;34f4d8b5047955f594d1397be9f0b59cfaeb8c356dc8f90930db3eec86c7e9e4&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;427207676c5cf083015dcc5a561825325b4f6d302cc58d645aad66bfdd874b69&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;dc734839d9cce8de097d89d4cb5f7eeca69515ae0ffe00990beab8f9250358e2&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;off&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--verbosity&quot;,
          &quot;4&quot;,
          &quot;--flash-attn&quot;,
          &quot;auto&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;abbaff705d4cd96710c5a0f62ced2c87d8be07ac46627ad9f777c734383720db&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          12,
          14,
          17
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: false
      },
      &quot;max_tokens&quot;: 4096,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-24T20:31:13.048854+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R497&quot;,
  &quot;independent_review_sha256&quot;: &quot;10d488e719484e00ab6804d0049d0c7efc018ea690f7f82054debc8c8de4006f&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;OmniCoder-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R471&quot;,
  &quot;peak_vram_mib&quot;: 7356.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 67.175594346,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1001.7500769230769,
      &quot;GPU_j_per_success_upper&quot;: 1136.1268461538461,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 51.728350785,
      &quot;completion_tokens&quot;: 3913,
      &quot;final_text_present&quot;: 16,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.2513128642749943,
      &quot;tokens_s_completed_requests&quot;: 75.64517214677328,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 214.9812142857143,
      &quot;GPU_j_per_success_upper&quot;: 340.1887142857143,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 15.428932838,
      &quot;completion_tokens&quot;: 761,
      &quot;final_text_present&quot;: 4,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.9073861521724514,
      &quot;tokens_s_completed_requests&quot;: 49.32291870023111,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    }
  }
}</pre></details></td></tr><tr><td>Nexus-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>14/16 · 87.5%</td><td>12/16 · 75.0%</td><td>315.2</td><td>77.5</td><td>3,359.0</td><td>7,356.5</td><td><a href="../results/#r481">R481 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;46c48438ab0b48f381a182c816dfbc1f58979f9e57238639be49a6556de9ea3b&quot;,
  &quot;conditions&quot;: &quot;Reused native A arm; interleaved ABC schedule. Same tasks/scorer and native sampler; timing is historical, not matched standalone performance evidence.&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c&quot;,
    &quot;parent_profile_id&quot;: &quot;nexus-q6-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c&quot;,
        &quot;family_id&quot;: &quot;nexus9b&quot;,
        &quot;hf_repository&quot;: &quot;prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;330ab686d7784f9b21f553727635efceeb8562e7&quot;,
        &quot;name&quot;: &quot;Nexus 9B CodeCore Merge&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Nexus CodeCore-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-bfd3858d51b6bd75120adb9782a5010423a2a5f45e955864d669598246ad3577&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.6,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-fa7673bc9bbe2719ab75ce63cc4f67d61bb1e6e4cffe230533194c4d02467853&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;db781ab34ac517868cf037b8f6943922e375528826f1ea11af3a2ceb54243d1e&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;31da6f0369fb75a61dd24d41dbd5765da594bc1e35b75ef6a1c1debdcdbf3dda&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;fa9918ef21e002a5f58f477641c71e294ae9c55e2feb229fe5c3a7b6287e7c52&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;671b81d2b8b8609ddcd63d6fc060f936c5643194457cb3f72499764d5f3a4da0&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:b994abeeffcf3f94162a91e9b3b70c4cce23e8d485d23b9874235af35753ac9c]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--verbosity&quot;,
          &quot;4&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;,
          &quot;--offline&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;a4a6459bce35cdb9061a4e17a60e54d1a36ce3c7e6362a27a56dde42d28ebe2c&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          12,
          14,
          17
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.6,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T16:22:15.043065+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R487&quot;,
  &quot;independent_review_sha256&quot;: &quot;e5f57e953d1004cfb88939c4e5b61db3da022a8a94cef583309bd9d292261628&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Nexus-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R481&quot;,
  &quot;peak_vram_mib&quot;: 7356.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: null,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 5511.0355,
      &quot;GPU_j_per_success_upper&quot;: 5642.7315,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 275.414822408,
      &quot;completion_tokens&quot;: 21716,
      &quot;final_text_present&quot;: 16,
      &quot;length_stops&quot;: 1,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.050832413003757564,
      &quot;tokens_s_completed_requests&quot;: 78.84833434211423,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 848.2989166666666,
      &quot;GPU_j_per_success_upper&quot;: 1006.6653333333334,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 39.735576887,
      &quot;completion_tokens&quot;: 2718,
      &quot;final_text_present&quot;: 5,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 12,
      &quot;successful_tasks_s_completed_requests&quot;: 0.30199637051012473,
      &quot;tokens_s_completed_requests&quot;: 68.40217792054325,
      &quot;valid_terminal_output&quot;: 12,
      &quot;wilson95&quot;: [
        0.5050168346449122,
        0.8981793250878696
      ]
    }
  }
}</pre></details></td></tr><tr><td>Slopus-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>12/16 · 75.0%</td><td>12/16 · 75.0%</td><td>177.0</td><td>76.1</td><td>1,976.1</td><td>7,356.5</td><td><a href="../results/#r483">R483 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;ef72de6b227a4bc892f701e0344fa7fa5bd951c711276bfeee819c6c0fbc79bb&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;aa4bc97efde586ce27e14fedd3fd896d78bb83b633ac8e5cd07113086b49479b&quot;,
    &quot;parent_profile_id&quot;: &quot;slopus-q6-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;aa4bc97efde586ce27e14fedd3fd896d78bb83b633ac8e5cd07113086b49479b&quot;,
        &quot;family_id&quot;: &quot;slopus9b&quot;,
        &quot;hf_repository&quot;: &quot;Kukedlc/Slopus-9B&quot;,
        &quot;hf_revision&quot;: &quot;85a138681cd780ef45a9b9c6d63363da33d08eb1&quot;,
        &quot;name&quot;: &quot;Slopus 9B&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Slopus-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-81b9e5bab3fe581ab070e34f9ff22cf3ab23ee1c2f628aeba88e1da16a5cf2b4&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.6,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-a928ba70765c1ef79611f3070d02eaa47f20e8f14e14ae25f1b2829b7bc944e2&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;b72385450f25df8a6187851b13f9b47ca404341c60398750ed42e808cdc2accc&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;93d4e34c8525736064c7c09cab8158d6df204f0e4f5d2fb8a76b025b8d9c1686&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;0e5ecffd4dbe0ac45cbe09ec2b87b80c392f49b8547a65ef65862ebc29fb6db8&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;86d03bbc69c7bc131a7df598629a392ebe8e04f5b1d5b2647e5b1248fe50b1e1&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:aa4bc97efde586ce27e14fedd3fd896d78bb83b633ac8e5cd07113086b49479b]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--verbosity&quot;,
          &quot;4&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;,
          &quot;--offline&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;b695bf066fac52a506fcd27b201cc4a40c6838a0ae9c8d902f36106fade31fc4&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          12,
          14,
          17
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.6,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T20:37:43.553309+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R498&quot;,
  &quot;independent_review_sha256&quot;: &quot;5a0316109071cfb5fbca9929e0051ca89fe91924f80fe84e77293a026980aeda&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Slopus-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R483&quot;,
  &quot;peak_vram_mib&quot;: 7356.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 176.984930613,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 3204.3186666666666,
      &quot;GPU_j_per_success_upper&quot;: 3359.38675,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 139.844509931,
      &quot;completion_tokens&quot;: 10964,
      &quot;final_text_present&quot;: 16,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 12,
      &quot;successful_tasks_s_completed_requests&quot;: 0.08580958956430153,
      &quot;tokens_s_completed_requests&quot;: 78.40136166525016,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.5050168346449122,
        0.8981793250878696
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 747.9286666666667,
      &quot;GPU_j_per_success_upper&quot;: 903.3928333333333,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 37.121657838,
      &quot;completion_tokens&quot;: 2503,
      &quot;final_text_present&quot;: 7,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 12,
      &quot;successful_tasks_s_completed_requests&quot;: 0.32326142470167557,
      &quot;tokens_s_completed_requests&quot;: 67.42694550235782,
      &quot;valid_terminal_output&quot;: 12,
      &quot;wilson95&quot;: [
        0.5050168346449122,
        0.8981793250878696
      ]
    }
  }
}</pre></details></td></tr><tr><td>Opus Distill-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>7/16 · 43.8%</td><td>10/16 · 62.5%</td><td>190.7</td><td>76.0</td><td>3,050.2</td><td>7,356.5</td><td><a href="../results/#r485">R485 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;503a80450201f424e1da7093236de909132970e6eee45b81e8d6cdf5aa0461b9&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;6a089b1b2d1fe21bbe78315a94da5b81e9dde538f9737a7f2c4a53c4eb42ae66&quot;,
    &quot;parent_profile_id&quot;: &quot;opus-distill-q6-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;6a089b1b2d1fe21bbe78315a94da5b81e9dde538f9737a7f2c4a53c4eb42ae66&quot;,
        &quot;family_id&quot;: &quot;omni_opus_distill9b&quot;,
        &quot;hf_repository&quot;: &quot;mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;942ac32ed196d167f90c97aa9aa2a346f4401bf9&quot;,
        &quot;name&quot;: &quot;OmniCoder Opus Distill 9B&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;OmniCoder Opus Distill-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-304d87156d2b6525fa8e99ec9ee326f6fe4995e7bf378bc13ee2aea5a0f4fc1d&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;e3a8a616b2fa4670edc927fe333999e709657ddf8df0fb023dd5b5d01dddd4f6&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.6,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-377170b50200a0a9f667e68998ed08155cb77536a9c39f1888d0b56f9f3cd0be&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;cfef6eaac279b653f093c506a7ff54729ac7fa5f22677bbd26eb096b38bd7d2e&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;43a5ee84de68053783fbeb7617962da7857e8e5baba7870433e9c51b79651b7c&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;364711a92a73e2d0a2f616ae6a187706c8ab1a3004319d9e4302486164235ee0&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;2d6190c732c42dbe7834cbaebc9a9fdd6ab369fe78bab33e792286107983f1ee&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:6a089b1b2d1fe21bbe78315a94da5b81e9dde538f9737a7f2c4a53c4eb42ae66]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:e3a8a616b2fa4670edc927fe333999e709657ddf8df0fb023dd5b5d01dddd4f6]&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--verbosity&quot;,
          &quot;4&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;,
          &quot;--offline&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;47d2bbd4ede50d627498bf0128815d4260d06c6e16ca15a7adb4bcff5efaebb1&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          12,
          14,
          17
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.6,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T20:43:35.436017+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R499&quot;,
  &quot;independent_review_sha256&quot;: &quot;c01e6a4e0e53258e49d5c3dc7fe493a98afd8f921a16d983eb76530dc4e7ea47&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Opus Distill-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R485&quot;,
  &quot;peak_vram_mib&quot;: 7356.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 190.698645309,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 5762.231714285715,
      &quot;GPU_j_per_success_upper&quot;: 6030.4538571428575,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 145.339624843,
      &quot;completion_tokens&quot;: 11360,
      &quot;final_text_present&quot;: 15,
      &quot;length_stops&quot;: 1,
      &quot;successes&quot;: 7,
      &quot;successful_tasks_s_completed_requests&quot;: 0.04816305262629926,
      &quot;tokens_s_completed_requests&quot;: 78.16175397639422,
      &quot;valid_terminal_output&quot;: 15,
      &quot;wilson95&quot;: [
        0.23098652405492354,
        0.6682144360118811
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1151.7738,
      &quot;GPU_j_per_success_upper&quot;: 1339.9352000000001,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 45.336913986,
      &quot;completion_tokens&quot;: 3135,
      &quot;final_text_present&quot;: 1,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 10,
      &quot;successful_tasks_s_completed_requests&quot;: 0.2205708135116561,
      &quot;tokens_s_completed_requests&quot;: 69.14895003590419,
      &quot;valid_terminal_output&quot;: 10,
      &quot;wilson95&quot;: [
        0.38641040545502714,
        0.8151876744113636
      ]
    }
  }
}</pre></details></td></tr><tr><td>Ornith-1.5-9B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r479">R479 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a&quot;,
    &quot;parent_profile_id&quot;: &quot;ornith15-q6-native-parallel200-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a&quot;,
        &quot;family_id&quot;: &quot;ornith15_9b&quot;,
        &quot;hf_repository&quot;: &quot;ornith-ai/Ornith-1.5-9B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;abdd624b12ebf020b767fff532ff44fe552b28c3&quot;,
        &quot;name&quot;: &quot;Ornith 1.5 9B&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Ornith-1.5-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-88aab23a13f70d216b990da21c365bec59e46ad6641e5b37db390b81311c1f6f&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.6,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-32d4074560ff89b4f99b63a489f28db61128bc466affc9fdc34716c2a8ffccf5&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;2739886b2b12ea0374904f207325a6c86618b86593169fbfcc44382a67212dd7&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;b7b84dd25fac11859005835193cbdc22466506fc039ee2e63b0b50c6b53a34ad&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;75265ff628efe01931af5b258fe5ad93d9b8ef66e95ba5669bf019b4465c02ef&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;b7ced761a3f5541892484b480854237cb8cfacafd17dee3df8ec676859191c13&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;f157e2c37e1720c25ada93dd957ec9cd7eda895636a85837bbd4bea32ef1410d&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.6,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Ornith-1.5-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R479&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>Qwen3.5-9B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r465">R465 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d&quot;,
    &quot;parent_profile_id&quot;: &quot;qwen35-q4-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q4_K_M&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d&quot;,
        &quot;family_id&quot;: &quot;q35&quot;,
        &quot;hf_repository&quot;: null,
        &quot;hf_revision&quot;: null,
        &quot;name&quot;: &quot;Qwen3.5 9B&quot;,
        &quot;quantization&quot;: &quot;Q4_K_M&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;qwen35-q4-native-coding-task1200-reviewed-sm70&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-beed938fd070c13bfba7993d44109e7518bc555eb0556e09671dbced1f396f74&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {},
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: null
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: false
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-9fcb6193898540f39890fcfb16525895409d6b08f8de5165231fcbc0c17d2653&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;c1e1034cc33f3d8bba738726af1bc0396b76affcef52b3ee7cf361eaed22bb77&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;4eb1556e145765cd44242083090460b4e7a0aaf2069deeac3825bc29c47abf25&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;9dfd38bb5a5c523af88f26763371e343dcc2297ed071cbf50ebca08392660eae&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;d4a1964a65c3b6855b0c08f5a43b3a9dc9568c4a602a3d5df0a04e8b3a2c51af&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:02d45dc1cf451ba2475ac33b301c2dd8f985abe4c182ce04a1f2f5bf0260278d]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;off&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:a4aee8afcf2e0711942cf848899be66016f8d14a889ff9ede07bca099c28f715]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;e453dfc9725c2c35f5a81effebac03a71ec31f8c4e317997723b3b7d27eb06c7&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: false
      },
      &quot;max_tokens&quot;: 4096,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.5-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R465&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>Qwen3.8-27B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r466">R466 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f&quot;,
    &quot;parent_profile_id&quot;: &quot;qwen38-iq3-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;GSQ/RCO IQ3_S&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f&quot;,
        &quot;family_id&quot;: &quot;q38&quot;,
        &quot;hf_repository&quot;: &quot;ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;d562806dbafae37109975e970aae91b43e73b440&quot;,
        &quot;name&quot;: &quot;Qwen3.8 27B&quot;,
        &quot;quantization&quot;: &quot;GSQ/RCO IQ3_S&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;qwen38-iq3-native-coding-task1200-reviewed-sm70&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-81368257950e68ed0a459e6e33b01ba8e9590d3d071c95b827ce3fcf85bce0de&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: false
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-1bc9cefba6ba7b1aed15ea85f4d7bd445c08f43fd9328a4f727dbd9276051cb0&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;7a21cacd939fae3227c2ceae593ade1092f241e8a59712abe498337486e37a66&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;9970f3d75788cb469468e21215f40ef32d805cc392cc157eec4ff211e8c92ba9&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;556c3adf25f8618a0d93218db3402e004446adb9197efb0732806db36f166658&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;c4b078155219cbbfe1a3534d662eb2700c70790a67c4475f2bf247316979c895&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;off&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;558f0391ff76b0c1d3eb23cde353e82f5bb93df82c6f20257dee8fa82e21270f&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: false
      },
      &quot;max_tokens&quot;: 4096,
      &quot;reasoning_effort&quot;: &quot;none&quot;,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.8-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R466&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>Gemma4-12B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r464">R464 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b&quot;,
    &quot;parent_profile_id&quot;: &quot;gemma4-qat-q4-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q4_0&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b&quot;,
        &quot;family_id&quot;: &quot;gemma4&quot;,
        &quot;hf_repository&quot;: &quot;google/gemma-4-12B-it-qat-q4_0-gguf&quot;,
        &quot;hf_revision&quot;: &quot;29d097773436b69ff9feafd636ab4cf873786537&quot;,
        &quot;name&quot;: &quot;Gemma4 12B IT QAT&quot;,
        &quot;quantization&quot;: &quot;Q4_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;gemma4-qat-q4-native-coding-task1200-reviewed-sm70&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-19f0410f08c1621397606da4afa83cbf262d3db9705dbe31926ad8df9e56d6fe&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;auto&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: false
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 1.0,
          &quot;top_k&quot;: 64,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;8799b221b845bbb9f5de79ea7bb36ca84e27531ae87dd98749002a6d9f433bef&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;303f5af22c2561933d156539249e593bdb3f0d6bd5d231d54dc66c8ac8d44392&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;9bbba0271eed8fdb3391e3eed7be4ba0b8d77d0a4e4a88c8c3863f98b38a3bd1&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;8cb7aa3284c2b17bea0d85975819f5be9958a381c4717d3867c1b00f8e9743d8&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;off&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;auto&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:ae53464bf3be25802b3a5b37def7fd89667067d7577049b3b2d74c4d8de4c6d4]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;e55ea534cb0bd6069e0705d4a7af7b8a5db9c4ecb6112fd7cf7c006fe95366d5&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: false
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 1.0,
      &quot;top_k&quot;: 64,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Gemma4-12B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R464&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>MiMo-9B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r454">R454 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;de6dae10334e088876358ef9f574835bb3b401ea2ecf5d6a9473f37894df6b73&quot;,
    &quot;parent_profile_id&quot;: &quot;mimo-q8-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q8_0&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;de6dae10334e088876358ef9f574835bb3b401ea2ecf5d6a9473f37894df6b73&quot;,
        &quot;family_id&quot;: &quot;mimo_v26_distill_qwen9b_q8&quot;,
        &quot;hf_repository&quot;: &quot;ggml-org/MiMo-V2.6-Distill-Qwen-9B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;81baddc39bc48924a88e87b8d31aceb03058e559&quot;,
        &quot;name&quot;: &quot;MiMo V2.6 Distill Qwen 9B&quot;,
        &quot;quantization&quot;: &quot;Q8_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;mimo-q8-native-coding-task1200-reviewed-sm70&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-094fe33ba6e2ef7928eab3c12b17072cfd860d9c18850a9f683130664243087e&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;d2365d1a768f61a6e46156c7dc5a7e08fe95f6bd0a9ce5cf606e908b3489a840&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.6,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-6fee55e4cd29ef463b21160ec81c870ad503865bd3fa368fefb0b64d6c8b830e&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;1cea136f756ab0a6d615cc8a6b9840653579e26e632c118eb25988b4eb20cdfd&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;e7102e9559e3ebf42829148500ecc1cb346e5fd6cb500406b1553aaf933ee1d3&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;078741e9273b13b9342a04365c50fa3a1433f2d15f9863ecfca45ccdf292f25e&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;cdaecae2f643c95d72fee2600ed6438b640f891bcc700ae75236120f070f91ae&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:de6dae10334e088876358ef9f574835bb3b401ea2ecf5d6a9473f37894df6b73]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:d2365d1a768f61a6e46156c7dc5a7e08fe95f6bd0a9ce5cf606e908b3489a840]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;df5706b689d8a877b0f32ee01b4f9847388896d25206ae6e60fe1cb8b0cea0ac&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.6,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;MiMo-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R454&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>LFM2.5-8B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r452">R452 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6&quot;,
    &quot;parent_profile_id&quot;: &quot;lfm25-q6-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6&quot;,
        &quot;family_id&quot;: &quot;lfm25_8b_a1b_q6&quot;,
        &quot;hf_repository&quot;: &quot;LiquidAI/LFM2.5-8B-A1B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;49c14831707011e64d70b2ebd8462ba08d608434&quot;,
        &quot;name&quot;: &quot;LFM2.5 8B A1B&quot;,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;native_Q6_K_T0.2_K80_output4096_noMTP_single_session&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-e72398297ed94d0b78cfd0891c8366f3b3d6e6a52f919d01741758d551b7781c&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;c5b67247c9f736f6c40eaa91ae1ef27dc67f5b041eedaadb97a1bea5030fb0ff&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_template_controls&quot;: {},
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.05,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.2,
          &quot;top_k&quot;: 80,
          &quot;top_p&quot;: 1.0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-bf94708017e31716c460eed85be81ce58b6a502ac82268cb793930118de990ae&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;2a0fcba676eab52ae6a2f1bd69ab62c7217cfec2c2f1bacbd163741d63da992c&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;5f68fa7e72e9febb72f091ec69eaa367293ee25dda0aa4c1629220fc2a2e2c89&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;88b23f3faafa315617244312d18ccd3a11b3cf861e9d9fc118efef38725d9eba&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;573c06ab6d261ecdcc75ce2dec8b91fba2d07111680cbd7ea1de9ea2cd956e96&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:c5b67247c9f736f6c40eaa91ae1ef27dc67f5b041eedaadb97a1bea5030fb0ff]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;41b7daf9f7e584b029fdfe6718df2b70dc3441b0baae52c29b4846a390d1e31b&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {},
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.05,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.2,
      &quot;top_k&quot;: 80,
      &quot;top_p&quot;: 1.0
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;LFM2.5-8B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R452&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>LFM2.5-24B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r468">R468 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;d1c03f73ecaf61017d70419eec9e5dc0b05d50ae26c23d522829b934fbabf8a5&quot;,
    &quot;parent_profile_id&quot;: &quot;lfm25-24b-qad-q4-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;QAD Q4_0&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;d1c03f73ecaf61017d70419eec9e5dc0b05d50ae26c23d522829b934fbabf8a5&quot;,
        &quot;family_id&quot;: &quot;lfm25_24b&quot;,
        &quot;hf_repository&quot;: &quot;LiquidAI/LFM2.5-24B-A2B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;0912d33141f77e10705345a6732bfd83f0252fdc&quot;,
        &quot;name&quot;: &quot;LFM2.5 24B A2B&quot;,
        &quot;quantization&quot;: &quot;QAD Q4_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;LFM2.5-24B-A2B-QAD&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-ec9ba077993eb04fbcc8772a8c8fdc8c665c44549c614679503f46b8363c4db9&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;512&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;ea663864491de7ade391839479860ca95541f892f72665c73251fbd4643b1bef&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;128&quot;,
        &quot;native_template_controls&quot;: {},
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.05,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.1,
          &quot;top_k&quot;: 50,
          &quot;top_p&quot;: 1.0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-a300301b48f44db40a601e616cb8ee7337a28054480f50650ce8d32e85116146&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;6820cd61dd44641e34171135ef138f415e2aa7119d7af725995fddad11093778&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;0d2b43a927b6ce5ca37942f03fe3716a00a1c98956ca50a7551208405162cf65&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;f0151c0e0ff5fd963e456c048c66d13159912db7fba22bd5864eed78fbcd2b3c&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;b6a27114537fde51dbd6e960b5e8c8533ea35aee989f30354a2e39d1181d7ee0&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:d1c03f73ecaf61017d70419eec9e5dc0b05d50ae26c23d522829b934fbabf8a5]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;512&quot;,
          &quot;--ubatch-size&quot;,
          &quot;128&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:ea663864491de7ade391839479860ca95541f892f72665c73251fbd4643b1bef]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;fdc375a49e0ae0fdd9ac0a3797ef04ffec17dc0e49543336b9e1e193699fca6e&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {},
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.05,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.1,
      &quot;top_k&quot;: 50,
      &quot;top_p&quot;: 1.0
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;LFM2.5-24B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R468&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>Qwen3.6-27B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r469">R469 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;4afb4abcf0207a484b0d7e92c0421b74e8ce1c7a7250bb9d824b79288da68f20&quot;,
    &quot;parent_profile_id&quot;: &quot;qwen36-27b-q3ks-native-coding-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q3_K_S&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;,
        &quot;build_id&quot;: &quot;dded13c80bc8e7d01a43ac6745d06bb22d7a15a3f5fba68729c536286e5066d4&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.26.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;4afb4abcf0207a484b0d7e92c0421b74e8ce1c7a7250bb9d824b79288da68f20&quot;,
        &quot;family_id&quot;: &quot;qwen36_27b&quot;,
        &quot;hf_repository&quot;: &quot;unsloth/Qwen3.6-27B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;82d411acf4a06cfb8d9b073a5211bf410bfc29bf&quot;,
        &quot;name&quot;: &quot;Qwen3.6 27B&quot;,
        &quot;quantization&quot;: &quot;Q3_K_S&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Qwen3.6-27B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-8eb9e2109d79535b218fe76db82c840e86d504da6c4f33147b7c020d4ea8afe7&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;512&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;55d4931433fe502b794226ee7f4d206a6bdd436ac9f80eb7d8ebb4c639f9ea0c&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;128&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: false
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 1.5,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0.7,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.8
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-24396c98c2666260c3ff74954ab4895927a8a14520fb8c1e6f059f73b5a3bcd0&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;b80456d161225ee5a38a271d46c3feb7b2d3ebaf6796b3eb63596ff4c4a32cdf&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;b8b62458b9747bde118b85ea8c4cf71786998758e7d3f552599f0f29a0292804&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;4e90c9c21fc75e1244506b628e04a56646321b6141f2fed50008357efc38fe3c&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;00e26fff944ddd52c53373f5183225dddaf80c427f827f0d31d9f531d520b5ef&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:4afb4abcf0207a484b0d7e92c0421b74e8ce1c7a7250bb9d824b79288da68f20]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;512&quot;,
          &quot;--ubatch-size&quot;,
          &quot;128&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;off&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:55d4931433fe502b794226ee7f4d206a6bdd436ac9f80eb7d8ebb4c639f9ea0c]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;aa8747f33964711c8d8c7a87cebeebfaffd8d716eeb041e4a2464c47139986ba&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: false
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;presence_penalty&quot;: 1.5,
      &quot;reasoning_effort&quot;: &quot;none&quot;,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0.7,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.8
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.6-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R469&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr><tr><td>Bonsai2-27B</td><td>SCREENING OFFEN</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td>NOT MEASURED</td><td><a href="../results/#r475">R475 archive</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: null,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.21.0&quot;: &quot;60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12&quot;,
      &quot;llama-server&quot;: &quot;94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1&quot;,
    &quot;parent_profile_id&quot;: &quot;bonsai-pq2-native-parallel200-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;PQ2_0&quot;,
    &quot;recorded_parent_profile&quot;: {
      &quot;engine&quot;: {
        &quot;binary_sha256&quot;: &quot;94c60d4646249fe067c75a56b15e6a8a9070a5e422cae16ee8dd9973389a6a27&quot;,
        &quot;build_id&quot;: &quot;bonsai-pq2-sm70-9a9394a895b9&quot;,
        &quot;cuda_version&quot;: null,
        &quot;driver_version&quot;: null,
        &quot;executed_kernel_backend_path&quot;: null,
        &quot;fork_repository&quot;: null,
        &quot;ggml_backend_version&quot;: null,
        &quot;git_commit&quot;: null,
        &quot;kernel_library_file&quot;: &quot;libggml-cuda.so.0.21.0&quot;,
        &quot;kernel_library_sha256&quot;: &quot;60c874aa652e9eb7d09ae128b79d31cbe0042f5e76476fd1d3192c47e7291d12&quot;,
        &quot;name&quot;: &quot;llama.cpp-compatible&quot;,
        &quot;patches&quot;: null,
        &quot;version&quot;: null
      },
      &quot;evaluation_exposure&quot;: &quot;Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.&quot;,
      &quot;incomplete_identity_run&quot;: null,
      &quot;model&quot;: {
        &quot;architecture&quot;: null,
        &quot;artifact_sha256&quot;: &quot;3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1&quot;,
        &quot;family_id&quot;: &quot;bonsai2_27b_pq2&quot;,
        &quot;hf_repository&quot;: &quot;prism-ml/Ternary-Bonsai-2-27B-gguf&quot;,
        &quot;hf_revision&quot;: &quot;b072e1d3b35a0a630cece372c2127528e0994386&quot;,
        &quot;name&quot;: &quot;Ternary Bonsai 2 27B&quot;,
        &quot;quantization&quot;: &quot;PQ2_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Ternary-Bonsai-2-27B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-d45c21b19c04c78375510e5c5b03ee0cd68e9cdb49b2f11e711ee162e03f3a42&quot;,
      &quot;optimizations&quot;: {
        &quot;GDN_state_changes&quot;: null,
        &quot;HBM_conversion_weight_cache_limit_mib&quot;: &quot;0&quot;,
        &quot;KV_precision&quot;: {
          &quot;k&quot;: &quot;f16&quot;,
          &quot;v&quot;: &quot;f16&quot;
        },
        &quot;cuda_graphs&quot;: {
          &quot;actual_capture_replay&quot;: null,
          &quot;disable_knob&quot;: null,
          &quot;optimization_knob&quot;: &quot;0&quot;
        },
        &quot;draft_head_or_model&quot;: null,
        &quot;draft_parameters&quot;: {
          &quot;--spec-type&quot;: &quot;none&quot;
        },
        &quot;draft_sha256&quot;: null,
        &quot;flash_attention_requested&quot;: &quot;on&quot;,
        &quot;other_explicit_knobs&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;
        },
        &quot;prefix_reuse&quot;: null,
        &quot;quantization_calibration&quot;: null,
        &quot;speculation_type&quot;: &quot;none&quot;
      },
      &quot;provenance_status&quot;: &quot;KNOWN_FIELDS_ONLY; null means NOT MEASURED&quot;,
      &quot;runtime&quot;: {
        &quot;CPU_budget&quot;: null,
        &quot;CPU_scoring_limit_s&quot;: 120,
        &quot;CPU_threads&quot;: &quot;6&quot;,
        &quot;GPU_offload&quot;: &quot;99&quot;,
        &quot;GPU_wrapper_limit_s&quot;: 1440,
        &quot;RAM_budget&quot;: null,
        &quot;VRAM_budget_mib&quot;: 14336,
        &quot;batch&quot;: &quot;2048&quot;,
        &quot;benchmark_task_limit_s&quot;: 1200,
        &quot;chat_template_sha256&quot;: &quot;c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: {
          &quot;enable_thinking&quot;: true,
          &quot;reasoning_effort&quot;: &quot;medium&quot;
        },
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.05,
          &quot;presence_penalty&quot;: 0.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 1.0,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 0.95
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;on&quot;,
        &quot;timing_scope&quot;: &quot;TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-734052029303654fd54d5b42bdc0dec93f3c5ced66ed981857ee5dc7f524c0dc&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;11ef05d11141f16e75188f7c1a84d826bc9fc50b9eb0823a299b37d87bc9cde6&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;989b072d9411fb845cec3251ebec402fb2a173d426fd70e0e5b249b73c40aa1e&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;e71aa9e403277c8cc0f45761e7aacae858454444511b6076c227fafd7d365dc5&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;758bf4436a0414d0a8d3456c49ff07a1a96d54216a4c05e0ac0878bd5d8fcc80&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1]&quot;,
          &quot;--alias&quot;,
          &quot;[session-local value]&quot;,
          &quot;--host&quot;,
          &quot;[session-local value]&quot;,
          &quot;--port&quot;,
          &quot;[session-local value]&quot;,
          &quot;--no-webui&quot;,
          &quot;--offline&quot;,
          &quot;--ctx-size&quot;,
          &quot;8192&quot;,
          &quot;--parallel&quot;,
          &quot;1&quot;,
          &quot;--n-gpu-layers&quot;,
          &quot;99&quot;,
          &quot;--threads&quot;,
          &quot;6&quot;,
          &quot;--threads-batch&quot;,
          &quot;6&quot;,
          &quot;--batch-size&quot;,
          &quot;2048&quot;,
          &quot;--ubatch-size&quot;,
          &quot;512&quot;,
          &quot;--seed&quot;,
          &quot;1001&quot;,
          &quot;--ctx-checkpoints&quot;,
          &quot;2&quot;,
          &quot;--cache-ram&quot;,
          &quot;0&quot;,
          &quot;--cache-reuse&quot;,
          &quot;0&quot;,
          &quot;--no-cache-idle-slots&quot;,
          &quot;--reasoning&quot;,
          &quot;on&quot;,
          &quot;--no-reasoning-preserve&quot;,
          &quot;--load-mode&quot;,
          &quot;mmap&quot;,
          &quot;--flash-attn&quot;,
          &quot;on&quot;,
          &quot;--cache-type-k&quot;,
          &quot;f16&quot;,
          &quot;--cache-type-v&quot;,
          &quot;f16&quot;,
          &quot;--jinja&quot;,
          &quot;--chat-template-file&quot;,
          &quot;[artifact:c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041]&quot;,
          &quot;--log-verbosity&quot;,
          &quot;4&quot;,
          &quot;--no-log-prefix&quot;,
          &quot;--no-log-timestamps&quot;,
          &quot;--spec-type&quot;,
          &quot;none&quot;,
          &quot;--reasoning-format&quot;,
          &quot;deepseek&quot;
        ],
        &quot;environment&quot;: {
          &quot;GGML_CUDA_GRAPH_OPT&quot;: &quot;0&quot;,
          &quot;GGML_CUDA_O2_WEIGHT_CACHE_MIB&quot;: &quot;0&quot;,
          &quot;OMP_NUM_THREADS&quot;: &quot;6&quot;
        },
        &quot;exact_private_launch_sha256&quot;: &quot;028d7633279a2c613eb8297711cb0ab67d24327953b5fd95348d55ca2d63a0cd&quot;,
        &quot;note&quot;: &quot;All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.&quot;,
        &quot;redacted_argument_positions&quot;: [
          0,
          2,
          4,
          6,
          8,
          47
        ]
      }
    },
    &quot;request_options&quot;: {
      &quot;cache_prompt&quot;: false,
      &quot;chat_template_kwargs&quot;: {
        &quot;enable_thinking&quot;: true,
        &quot;reasoning_effort&quot;: &quot;medium&quot;
      },
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.05,
      &quot;presence_penalty&quot;: 0.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 1.0,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 0.95
    },
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: null,
  &quot;independent_review_sha256&quot;: null,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Bonsai2-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R475&quot;,
  &quot;status&quot;: &quot;SCREENING OFFEN&quot;,
  &quot;category_results&quot;: null
}</pre></details></td></tr></tbody></table></div>

Development evidence, not an official benchmark or unseen validation set. These tasks were previously used for Nexus A/B/C tuning. No automatic exclusion from small score differences. Wilson intervals, native sampling, hashes, missing answers and audit references are in **Details**. A separate8coding+8mock-tool validation set is frozen and reserved; no model has answered it. Native templates and settings remain unchanged.

¹ Completion tokens / completed-request wall time, including reasoning when reported; not pure decode speed. ² Counter-bracketed lower bound; upper bounds remain in Details. Failed completed requests count toward costs. Historical Nexus A timings used an interleaved ABC schedule. Missing values stay unknown.


<details><summary>Other local artifacts pending standalone-profile review</summary>

- **Qwen3.5-0.8B-Q8_0.gguf** — TECHNISCH BLOCKIERT: Local draft/small model artifact has no registered executed standalone native screening parent. Requires existing technical/native admission, not quality exclusion.
- **Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf** — SCREENING OFFEN: Additional nongrafted artifact; established native baseline uses the separately identified MTP-bearing artifact with speculation disabled. No weight equivalence is assumed.
- **Tesslate_OmniCoder-9B-Q6_K.gguf** — SCREENING OFFEN: Historical alternate quantizer artifact; main canonical Omni checkpoint selected for first baseline pass. Existing weight-integrity evidence retained; no new equality claim.

</details>
