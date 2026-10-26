# Model screening

**19/19 profiles measured** · 16 coding + 16 mock-tool development tasks.

Screening → full qualification → targeted optimization → independent confirmation.

[Current Jarvis qualification shortlist](pipeline-methods.md#jarvis-qualification) · screening complete; no repeat planned.

<input id="screening-search" type="search" placeholder="Filter models or status" aria-label="Filter screening models">

<div class="screening-wrap"><table id="screening-table"><thead><tr><th>Model</th><th>Status</th><th>Coding /16</th><th>Mock tools /16</th><th>Request time s</th><th>Output tok/s¹</th><th>GPU J/success ≥²</th><th>VRAM MiB</th><th>Existing benchmarks</th><th>Details</th></tr></thead><tbody><tr><td>OmniCoder-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>13/16 · 81.2%</td><td>14/16 · 87.5%</td><td>67.2</td><td>69.6</td><td>593.8</td><td>7,356.5</td><td><a href="../experiments/R471/">R471</a> · <a href="../experiments/R471/">R471</a> · <a href="../experiments/R478/">R478</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R497/">Screening R497</a> · <details><summary>Profile & evidence</summary><pre>{
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-c98ecea3a0e41008f904fc0102cfcf18d5601d145c731403748690d5946ae759&quot;,
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
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;0725b527fc77fa0b1bc3129d4f9b0b1a9c290df3b375236659c864b6fde90958&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-343ddfa996f79239e54edb7a1ddd23732c676d7d21d5d83cb22efddfc23e8f9c&quot;,
      &quot;experiment_id&quot;: &quot;R471&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-26d5b175a8e379f00193da2b2de4bce97c7d89fdc2bacf55b6971d71cb22f28e&quot;
    },
    {
      &quot;audit_hash&quot;: &quot;0725b527fc77fa0b1bc3129d4f9b0b1a9c290df3b375236659c864b6fde90958&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-343ddfa996f79239e54edb7a1ddd23732c676d7d21d5d83cb22efddfc23e8f9c&quot;,
      &quot;experiment_id&quot;: &quot;R471&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-26d5b175a8e379f00193da2b2de4bce97c7d89fdc2bacf55b6971d71cb22f28e&quot;
    },
    {
      &quot;audit_hash&quot;: &quot;9facd2474e8be80aa0fa2c617e617ec16cd9b11b38d2b6b2d8630435fc6edb42&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R478&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-21e92fd73d60a2aea4381051b00148063e4e562f95a71a0c1c558ea7b511cb1a&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
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
      &quot;gpu_energy_j_lower&quot;: 13022.751,
      &quot;gpu_energy_j_upper&quot;: 14769.649,
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
      &quot;gpu_energy_j_lower&quot;: 3009.737,
      &quot;gpu_energy_j_upper&quot;: 4762.642,
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
}</pre></details></td></tr><tr><td>Nexus-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>14/16 · 87.5%</td><td>12/16 · 75.0%</td><td>315.2</td><td>77.5</td><td>3,359.0</td><td>7,356.5</td><td><a href="../experiments/R482/">R482</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R487/">Screening R487</a> · <details><summary>Profile & evidence</summary><pre>{
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-55c39c010a375967005d3e9ef85275af15a398f50c6eb3e8332cf55a94b9ce2c&quot;,
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
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;a7f63146ef37d27560d5f765ac76875bb196a335b851beeb32a24d985fbb3b6f&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R482&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-256a4259cced4012a6f1d2aca480672d7937d939e945b91ea2e5ad81269fe190&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
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
      &quot;gpu_energy_j_lower&quot;: 77154.497,
      &quot;gpu_energy_j_upper&quot;: 78998.241,
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
      &quot;gpu_energy_j_lower&quot;: 10179.587,
      &quot;gpu_energy_j_upper&quot;: 12079.984,
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
}</pre></details></td></tr><tr><td>Slopus-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>12/16 · 75.0%</td><td>12/16 · 75.0%</td><td>177.0</td><td>76.1</td><td>1,976.1</td><td>7,356.5</td><td><a href="../experiments/R484/">R484</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R498/">Screening R498</a> · <details><summary>Profile & evidence</summary><pre>{
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-895f851c9a05ebf887ff2720c76e32206bbc44f99e31b601e4a2139fdc99fee3&quot;,
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
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;b0dcae0da912bdcab55d93e932040c51218876d9af67748ffbb636d48c3c44bf&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R484&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-a655247266cf1392456339334bac37e034964d6fd64d478ddae1ee3da97015bb&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
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
      &quot;gpu_energy_j_lower&quot;: 38451.824,
      &quot;gpu_energy_j_upper&quot;: 40312.641,
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
      &quot;gpu_energy_j_lower&quot;: 8975.144,
      &quot;gpu_energy_j_upper&quot;: 10840.714,
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
}</pre></details></td></tr><tr><td>Opus Distill-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>7/16 · 43.8%</td><td>10/16 · 62.5%</td><td>190.7</td><td>76.0</td><td>3,050.2</td><td>7,356.5</td><td><a href="../experiments/R486/">R486</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R499/">Screening R499</a> · <details><summary>Profile & evidence</summary><pre>{
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-a9f7e66a82f6202d535f7491384767a14b7db12e6c787786df994de75142da92&quot;,
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
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;82fa3745132d538d00df05cdb34302a999897fc9febae953809b2fd601be9691&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R486&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-1bfa20f10018719df37b9b8e2315529dade0e317da207d333bd337e551021d84&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
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
      &quot;gpu_energy_j_lower&quot;: 40335.622,
      &quot;gpu_energy_j_upper&quot;: 42213.177,
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
      &quot;gpu_energy_j_lower&quot;: 11517.738,
      &quot;gpu_energy_j_upper&quot;: 13399.352,
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
}</pre></details></td></tr><tr><td>Ornith-1.5-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>13/16 · 81.2%</td><td>11/16 · 68.8%</td><td>361.5</td><td>77.5</td><td>4,207.4</td><td>7,356.5</td><td><a href="../experiments/R479/">R479</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R500/">Screening R500</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;f5efcab1dbcdfb77af2b3344ab79755e9c792618d05b1687d69e89cfdc2d5d06&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-e0d1af3e684f133fde9c9df0ff310d3bcece321dfdaf9dcfe4df1e9522ec8c5e&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;date&quot;: &quot;2026-10-24T20:54:46.305815+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R500&quot;,
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;ae71481c7169f4a37b5281bc61f2b96f940172d7bd41e126468d8a16729ae6b1&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R479&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-32d4074560ff89b4f99b63a489f28db61128bc466affc9fdc34716c2a8ffccf5&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
  &quot;independent_review_sha256&quot;: &quot;24b20a9e63e5c5c5d77efb2b0e0039261d09c310d524e14570a20992951249ef&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Ornith-1.5-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R479&quot;,
  &quot;peak_vram_mib&quot;: 7356.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 361.511117741,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 7119.365,
      &quot;GPU_j_per_success_upper&quot;: 7277.29876923077,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 327.578638926,
      &quot;completion_tokens&quot;: 25779,
      &quot;final_text_present&quot;: 14,
      &quot;gpu_energy_j_lower&quot;: 92551.745,
      &quot;gpu_energy_j_upper&quot;: 94604.884,
      &quot;length_stops&quot;: 2,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.03968512734109229,
      &quot;tokens_s_completed_requests&quot;: 78.69560751738601,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 766.053,
      &quot;GPU_j_per_success_upper&quot;: 950.7,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 33.91245192,
      &quot;completion_tokens&quot;: 2242,
      &quot;final_text_present&quot;: 7,
      &quot;gpu_energy_j_lower&quot;: 8426.583,
      &quot;gpu_energy_j_upper&quot;: 10457.7,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.3243646323760125,
      &quot;tokens_s_completed_requests&quot;: 66.11140961700183,
      &quot;valid_terminal_output&quot;: 11,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    }
  }
}</pre></details></td></tr><tr><td>Qwen3.5-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>15/16 · 93.8%</td><td>12/16 · 75.0%</td><td>79.6</td><td>87.2</td><td>699.7</td><td>5,956.5</td><td><a href="../experiments/R474/">R474</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R501/">Screening R501</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;9e9b0f0375c964838fb98cac1be993c2b7bb88c3299d8e7e0759f9d3f95deca7&quot;,
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
    &quot;parent_profile_id&quot;: &quot;qwen35-q4-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;variant&quot;: &quot;Qwen3.5-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-ddd6ec28478225f72a667b27a60a88676313261cd6901581f8854784127a33b6&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-aae586a5fa23e08f528cfec90a0d3e1817a681b815a4b5329c4326467b848a55&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;924f251221d4929978f976f6f90df4640e27b716f1bb6a658222b6b5d4ecc759&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;dc535e060e2756a5f575511f2d9eaafe961c1a25a9caf69975ebffba1e1f1927&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;16af9a0ea14cf79f0bb3609eeebf78f266cb908bcaa1c73336ad8134ed5505a1&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;73f83d92df3630237f20d3fe49a7f351af86652d8ee1294b00247ad38fdca5e8&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;71326d5b93b4150a1f942c752b7053ded68b6e5ab6d408e8f320b7b81d121a5f&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-eec00db88dcfa3e17fa958de15a41465ed1601e5a26d4a54ad4501fe842d6655&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-24T21:00:51.448625+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R501&quot;,
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;89329075d5e77e4cc223859b7afb31a4f03e8810875b017a7a3e9cb48427e3f0&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R474&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-aae586a5fa23e08f528cfec90a0d3e1817a681b815a4b5329c4326467b848a55&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
  &quot;independent_review_sha256&quot;: &quot;7d2a537289937e394ddec616d533689fb94c88c496d72c6889e4fe87e9a5b438&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.5-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R474&quot;,
  &quot;peak_vram_mib&quot;: 5956.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 79.578397402,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1072.4802666666667,
      &quot;GPU_j_per_success_upper&quot;: 1189.4296666666667,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 64.93725960900001,
      &quot;completion_tokens&quot;: 6098,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 16087.204,
      &quot;gpu_energy_j_upper&quot;: 17841.445,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 15,
      &quot;successful_tasks_s_completed_requests&quot;: 0.23099219293080653,
      &quot;tokens_s_completed_requests&quot;: 93.90602616613721,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.7167126242970107,
        0.9888806552353576
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 233.80058333333332,
      &quot;GPU_j_per_success_upper&quot;: 377.6571666666667,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 14.623752884,
      &quot;completion_tokens&quot;: 838,
      &quot;final_text_present&quot;: 3,
      &quot;gpu_energy_j_lower&quot;: 2805.607,
      &quot;gpu_energy_j_upper&quot;: 4531.886,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 12,
      &quot;successful_tasks_s_completed_requests&quot;: 0.8205827939782355,
      &quot;tokens_s_completed_requests&quot;: 57.30403177948012,
      &quot;valid_terminal_output&quot;: 12,
      &quot;wilson95&quot;: [
        0.5050168346449122,
        0.8981793250878696
      ]
    }
  }
}</pre></details></td></tr><tr><td>Qwen3.8-27B</td><td>SCREENING VOLLSTÄNDIG</td><td>16/16 · 100.0%</td><td>13/16 · 81.2%</td><td>132.5</td><td>27.5</td><td>1,187.4</td><td>12,454.5</td><td>NOT MEASURED</td><td><a href="../experiments/R502/">Screening R502</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;6559318406c61ee8c2e1032f4eb4bfb544a25b53b3a40fe40a99a9ce77dec93c&quot;,
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
    &quot;parent_profile_id&quot;: &quot;qwen38-iq3-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;variant&quot;: &quot;Qwen3.8-27B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-caf2bd548235bbc543cf0a388956ebc2e4724badd60bbb95a8b5e543f886a4d0&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-8f78ed6d25af1f692013432f586b4f86710b67f7e2c3f08af4cb3989b6ca2ca5&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;56fa8b24518b215ec5eff2ac8dbeb75e654f968836f26b282eb738337960a657&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;fe87419649ed3e438fd6759b727e3d14fe2929bcb7383110f4159d5bf6279d9d&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;c438a5a29296e3ecd24879a4284f1de988bd0ae411e0e5bf9f2e81ad6f5a25c0&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;a3467f360dbad23eeaf796ff430ad523186d76951984e000e5df2466fe4bb966&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;f10ce72b41d42ad8ca35496f4690682c22d868ad6f7fe6657cc08709f2c33c99&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-1d42865a4b3685127bcbd09b6dc8c0a6e72600aee8bf1204cb243b17c54f5794&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;date&quot;: &quot;2026-10-24T21:08:34.997295+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R502&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;de9061d3cf9d5b1542bed68e54c4f12a2b4ca69b040e255330a26a49d40a05d4&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.8-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R473&quot;,
  &quot;peak_vram_mib&quot;: 12454.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 132.500644243,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1492.73025,
      &quot;GPU_j_per_success_upper&quot;: 1605.1528125,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 89.031972242,
      &quot;completion_tokens&quot;: 2885,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 23883.684,
      &quot;gpu_energy_j_upper&quot;: 25682.445,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 16,
      &quot;successful_tasks_s_completed_requests&quot;: 0.1797107218574245,
      &quot;tokens_s_completed_requests&quot;: 32.40408953491686,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.8063923194655637,
        1
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 811.7017692307692,
      &quot;GPU_j_per_success_upper&quot;: 949.1646923076922,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 43.450667561,
      &quot;completion_tokens&quot;: 764,
      &quot;final_text_present&quot;: 3,
      &quot;gpu_energy_j_lower&quot;: 10552.123,
      &quot;gpu_energy_j_upper&quot;: 12339.141,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.29918987968940675,
      &quot;tokens_s_completed_requests&quot;: 17.583159083285135,
      &quot;valid_terminal_output&quot;: 13,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    }
  }
}</pre></details></td></tr><tr><td>Gemma4-12B</td><td>SCREENING VOLLSTÄNDIG</td><td>14/16 · 87.5%</td><td>14/16 · 87.5%</td><td>70.1</td><td>62.8</td><td>522.4</td><td>8,128.5</td><td><a href="../experiments/R472/">R472</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R503/">Screening R503</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;c1a7d873cd05b2925811e4ef06efde1c1056e5fa7d7c1c2037ef9d34659707ef&quot;,
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
    &quot;parent_profile_id&quot;: &quot;gemma4-qat-q4-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;variant&quot;: &quot;Gemma4-12B-IT-QAT&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-1ec9fa790255e20ba7009e7654a609b907bdf0da29d1fb3fef77f730e0592a6e&quot;,
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
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-aebfa2c88282523db04a6e6e6b802fcb8eb8912f4c2715d30c53e52ed40096e7&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;f6138859b29e191883e0acf88644b036e5dcee08622ff45ba8a7ee97336ac1ea&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;649fe42a4411f7135b8c1b1dd12d4a31ce7a42a96dd787a2504c7d9583a2b42f&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;0af23c90de165cfa20a59cabbc5a6ac8007b63c6a7efe34dea9877b5a91654bf&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;d7c0787185abcc04ec22ae198e061e2198e7170373c5958fb7045961ce9ee5a3&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;a5b36a29dd7394bed8656479342f82a08388a67a548ffd22591a4b2f400df776&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-1304a92162789caaac5ada03c62c855e213b1293e3c3d2b68d37524500f2a45c&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-24T21:12:00.666621+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R503&quot;,
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;7bfd00d2fcca7e4c767d6a197c3b1f9cc2bb1a146d794d2977f54d28cf21b1aa&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R472&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-aebfa2c88282523db04a6e6e6b802fcb8eb8912f4c2715d30c53e52ed40096e7&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
  &quot;independent_review_sha256&quot;: &quot;2e826b4289beb3b8fd38a91724688c55729249e3e59c557dd695ce02dfbcc66c&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Gemma4-12B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R472&quot;,
  &quot;peak_vram_mib&quot;: 8128.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 70.120594692,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 907.9131428571428,
      &quot;GPU_j_per_success_upper&quot;: 1029.0434285714286,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 57.288395713,
      &quot;completion_tokens&quot;: 3935,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 12710.784,
      &quot;gpu_energy_j_upper&quot;: 14406.608,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.24437758861561368,
      &quot;tokens_s_completed_requests&quot;: 68.68755794303142,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 136.9222142857143,
      &quot;GPU_j_per_success_upper&quot;: 255.97607142857143,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 12.815634876,
      &quot;completion_tokens&quot;: 466,
      &quot;final_text_present&quot;: 5,
      &quot;gpu_energy_j_lower&quot;: 1916.911,
      &quot;gpu_energy_j_upper&quot;: 3583.665,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 1.092415641945135,
      &quot;tokens_s_completed_requests&quot;: 36.36183493903092,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    }
  }
}</pre></details></td></tr><tr><td>MiMo-9B</td><td>SCREENING VOLLSTÄNDIG</td><td>11/16 · 68.8%</td><td>11/16 · 68.8%</td><td>105.3</td><td>68.7</td><td>1,047.7</td><td>9,188.5</td><td>NOT MEASURED</td><td><a href="../experiments/R504/">Screening R504</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;e0bc7965bf9b4193b4d6a47c934663faea44c1dcb07500937da8c5f0e3dfa9fe&quot;,
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
    &quot;parent_profile_id&quot;: &quot;mimo-q8-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;variant&quot;: &quot;MiMo-V2.6-Distill-Qwen-9B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-2224e59ff4350ffe912658c5054cac69f6269e0c915a56cbb906f5e5191dc758&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-146fc8bdf55eefbb6d995e664f5c6ef1f86c8b8d5c5a2f4093859df6decc9a17&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;09c7d299580ad564304c5a634c9bfae96f9fb4dbe19e1083f0b2af3a389f0ec6&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;988fce72427535a9ec716e81207026763894b608cb556ca80b112ed43e5d38d4&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;6ba5c5672f6abef6edc20f6841a68b6afdd981f3c13e5f8fb098242254af76fe&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;b460a336eb9f08c7b4154b2a6d70bc1fb2d23fae3a425e6c0fece9d3b781db44&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;313f669d7e3894a05ec451d60c07e2ffb564b31d2058f210fd9001a8c671445f&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-89d46f4a13813c0c26c4122e45c4fa367a47e586b10f8394d00b40d347214e8a&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;date&quot;: &quot;2026-10-24T21:16:45.099593+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R504&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;1d7c418edeba12b15e5ad7af3fde77c9fa4d083d9e04ebea8bf010d5fb25fbae&quot;,
  &quot;local_artifact_available&quot;: false,
  &quot;model&quot;: &quot;MiMo-9B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R480&quot;,
  &quot;peak_vram_mib&quot;: 9188.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 105.363514769,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1619.263,
      &quot;GPU_j_per_success_upper&quot;: 1772.794,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 79.16284308200001,
      &quot;completion_tokens&quot;: 5657,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 17811.893,
      &quot;gpu_energy_j_upper&quot;: 19500.734,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.1389540796129033,
      &quot;tokens_s_completed_requests&quot;: 71.46029348819945,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 476.1469090909091,
      &quot;GPU_j_per_success_upper&quot;: 627.3834545454546,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 26.183561683,
      &quot;completion_tokens&quot;: 1585,
      &quot;final_text_present&quot;: 6,
      &quot;gpu_energy_j_lower&quot;: 5237.616,
      &quot;gpu_energy_j_upper&quot;: 6901.218,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.42011091283818297,
      &quot;tokens_s_completed_requests&quot;: 60.53416334986545,
      &quot;valid_terminal_output&quot;: 11,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    }
  }
}</pre></details></td></tr><tr><td>LFM2.5-8B</td><td>SCREENING VOLLSTÄNDIG</td><td>11/16 · 68.8%</td><td>11/16 · 68.8%</td><td>86.8</td><td>189.2</td><td>684.8</td><td>7,448.5</td><td>NOT MEASURED</td><td><a href="../experiments/R505/">Screening R505</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;15b1f86cbdc561077496b659a92808bbc811386bedae2246932068c506288c6f&quot;,
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
    &quot;parent_profile_id&quot;: &quot;lfm25-q6-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;variant&quot;: &quot;LFM2.5-8B-A1B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-2702a7fc9eace54d1410594cda39f3596ce11ad6cd49fc8c4f59136917460c9d&quot;,
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
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-3336324962cd5565abc86e4a6440d7b5a982511204e848fe30f92f1d524f0813&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;bd5e403bc5b530b50ed6fe893280c8fd42315ebcc5b2f2593cb4fb6500980aee&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;640003a17661439eb3bd232d4e1cbcf2723cac351caf17cd45723402c37c6c3a&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;102642c5fac98ffd1db3a725e51e61eb34cc4c375a452f9c27e99ee096afbc84&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;f5442e8be08c017d87f79c71e583615b42195824ef129d4c60003eb7a0121230&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;9bf2b4f08bae7a81688998d19c72d6ee637603ea2af3e527e96bcb1a9e48071a&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-c95787a399c9fd317e7552ef984e726fcc770b566e086d94cc020fc38d9ebb61&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T21:21:58.513563+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R505&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;d08c18ec7b417a8186d2524d707372c17610fc10a0da48c66c414e4b3379ecd5&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;LFM2.5-8B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R476&quot;,
  &quot;peak_vram_mib&quot;: 7448.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 86.852830793,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 925.9827272727272,
      &quot;GPU_j_per_success_upper&quot;: 1060.9189090909092,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 57.410959971,
      &quot;completion_tokens&quot;: 11245,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 10185.81,
      &quot;gpu_energy_j_upper&quot;: 11670.108,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.19160104630816888,
      &quot;tokens_s_completed_requests&quot;: 195.8685241577599,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 443.61790909090905,
      &quot;GPU_j_per_success_upper&quot;: 574.0803636363636,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 29.420594416,
      &quot;completion_tokens&quot;: 5185,
      &quot;final_text_present&quot;: 7,
      &quot;gpu_energy_j_lower&quot;: 4879.797,
      &quot;gpu_energy_j_upper&quot;: 6314.884,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.3738877551032006,
      &quot;tokens_s_completed_requests&quot;: 176.23709183728138,
      &quot;valid_terminal_output&quot;: 11,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    }
  }
}</pre></details></td></tr><tr><td>LFM2.5-24B</td><td>SCREENING VOLLSTÄNDIG</td><td>13/16 · 81.2%</td><td>10/16 · 62.5%</td><td>241.4</td><td>155.5</td><td>1,633.9</td><td>13,796.5</td><td>NOT MEASURED</td><td><a href="../experiments/R506/">Screening R506</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;c5a2970677678b185f3adf53e9be41cb4a5d5e5e508948ee688e93eb5931de8d&quot;,
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
    &quot;parent_profile_id&quot;: &quot;lfm25-24b-qad-q4-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-7afa9f9f465d059ff54d9b6fef6762dded717f96ac2772dd651304a689955bd3&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;b54c574811d852cc329956c1f9ccfe7316227f5a536ef8963124ef1bb684aba3&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;2ccbecd53844ebc8e6b60e6448d4e0245c88fd877567c40dcb10f68023a9b6c7&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;d1e4e6e099fbca4c0abd429bf910eeb5d43c3a9a27538d31dd1cf8fa832bb393&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;b4dc711ea350619cdb04e552b60afce10e56c9a3e1e5afdc30088edc098490ca&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;3fa2b2bb6252b9e917e2134b29b2c03ca3bac1e1740b48b3b59e9b6f148092f4&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-478fffcf2e7f388f83f2f791dbbaa798a1060e1fe8b6ebd1f0fd14a6439b24a5&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T21:30:52.902537+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R506&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;7b92769344562f7dcef7803b4d2ddd1bdadb886b407a2179505e2680a0cf16f7&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;LFM2.5-24B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R477&quot;,
  &quot;peak_vram_mib&quot;: 13796.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 241.464198521,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 2240.3563846153847,
      &quot;GPU_j_per_success_upper&quot;: 2331.211307692308,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 185.709724326,
      &quot;completion_tokens&quot;: 29953,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 29124.633,
      &quot;gpu_energy_j_upper&quot;: 30305.747,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.07000171933473683,
      &quot;tokens_s_completed_requests&quot;: 161.28934609487476,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 845.5285,
      &quot;GPU_j_per_success_upper&quot;: 963.4309,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 55.726972467,
      &quot;completion_tokens&quot;: 7582,
      &quot;final_text_present&quot;: 5,
      &quot;gpu_energy_j_lower&quot;: 8455.285,
      &quot;gpu_energy_j_upper&quot;: 9634.309,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 10,
      &quot;successful_tasks_s_completed_requests&quot;: 0.17944631759641577,
      &quot;tokens_s_completed_requests&quot;: 136.05619800160244,
      &quot;valid_terminal_output&quot;: 10,
      &quot;wilson95&quot;: [
        0.38641040545502714,
        0.8151876744113636
      ]
    }
  }
}</pre></details></td></tr><tr><td>Qwen3.6-27B</td><td>SCREENING VOLLSTÄNDIG</td><td>14/16 · 87.5%</td><td>14/16 · 87.5%</td><td>208.5</td><td>22.3</td><td>1,982.9</td><td>12,766.5</td><td>NOT MEASURED</td><td><a href="../experiments/R507/">Screening R507</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;fded363bc68976cb8b1d97d16d52c1dec3bb8bb42a1b485d91ff4dec49b8ac8d&quot;,
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
    &quot;parent_profile_id&quot;: &quot;qwen36-27b-q3ks-native-parallel200-task1200-reviewed-sm70&quot;,
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
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
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
      &quot;runtime_configuration_id&quot;: &quot;cfg-22ddad19e7c5ae6c80fc0c4116156b827125813bdf4fd91f2b04dd13a56f68f1&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;e30f672384e09df13e6c64a0a9d9e55bea0e20baf702205b099cbf211f9afb11&quot;,
      &quot;source_provenance&quot;: {
        &quot;first_part_collection_audit_sha256&quot;: &quot;a778c6835cd770378e2f848f952ea40bee39586e7f128496c60f27c0f19bd13c&quot;,
        &quot;first_part_contract_sha256&quot;: &quot;042f09a6e140c4da0fdad52553758176e77dfcf0624f044a146c025f3a3f6689&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;4e374684f8fb355a8596b7e526efe0897d9a22b2ff15ea1216f83908457883f8&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;8e7a14894889dcfab9aa8b14766246149f74bdb19c96d4c9ed158c1c269a938e&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-154d3f063690166ef43fa2d9b475de65391faf61d8616a63d2b84d760b0477af&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 1
  },
  &quot;date&quot;: &quot;2026-10-24T21:38:42.195001+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R507&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;21d5129f9437d6035eac4b26ae90e594d658630c6166d6f0a47c6ed94cd57e34&quot;,
  &quot;local_artifact_available&quot;: false,
  &quot;model&quot;: &quot;Qwen3.6-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R492&quot;,
  &quot;peak_vram_mib&quot;: 12766.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 208.575632234,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 2821.360857142857,
      &quot;GPU_j_per_success_upper&quot;: 2951.427714285714,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 147.500644822,
      &quot;completion_tokens&quot;: 3964,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 39499.052,
      &quot;gpu_energy_j_upper&quot;: 41319.988,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.09491483930049825,
      &quot;tokens_s_completed_requests&quot;: 26.87445878479822,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1144.5365714285715,
      &quot;GPU_j_per_success_upper&quot;: 1278.3473571428572,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 61.048389781,
      &quot;completion_tokens&quot;: 694,
      &quot;final_text_present&quot;: 7,
      &quot;gpu_energy_j_lower&quot;: 16023.512,
      &quot;gpu_energy_j_upper&quot;: 17896.863,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.22932627789565713,
      &quot;tokens_s_completed_requests&quot;: 11.368031204256146,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    }
  }
}</pre></details></td></tr><tr><td>Bonsai2-27B</td><td>SCREENING VOLLSTÄNDIG</td><td>12/16 · 75.0%</td><td>13/16 · 81.2%</td><td>452.9</td><td>51.8</td><td>4,887.9</td><td>8,158.5</td><td>NOT MEASURED</td><td><a href="../experiments/R508/">Screening R508</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;da2e0b26bdb5cce3032b048b13bf8a4c6bbd1fe5120ccf6b7447df243c024f30&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-0b7dc4a06e1e28010bf89952b3c3be5d7e7ba098c070578d5135526e44648987&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 4
  },
  &quot;date&quot;: &quot;2026-10-24T21:48:51.017314+00:00&quot;,
  &quot;decision&quot;: &quot;No quality exclusion from16 tasks; retain for review.&quot;,
  &quot;experiment_id&quot;: &quot;R508&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;5ce96cdc8da904ffc67a244d8b460d4567ffe886b6cab0f987dd76b65fc295d6&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Bonsai2-27B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R475&quot;,
  &quot;peak_vram_mib&quot;: 8158.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 452.966795712,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 8961.988166666666,
      &quot;GPU_j_per_success_upper&quot;: 9119.1265,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 393.30735144700003,
      &quot;completion_tokens&quot;: 21332,
      &quot;final_text_present&quot;: 14,
      &quot;gpu_energy_j_lower&quot;: 107543.858,
      &quot;gpu_energy_j_upper&quot;: 109429.518,
      &quot;length_stops&quot;: 2,
      &quot;successes&quot;: 12,
      &quot;successful_tasks_s_completed_requests&quot;: 0.030510489966310877,
      &quot;tokens_s_completed_requests&quot;: 54.237480996778636,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.5050168346449122,
        0.8981793250878696
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1127.285076923077,
      &quot;GPU_j_per_success_upper&quot;: 1269.985846153846,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 59.639571464999996,
      &quot;completion_tokens&quot;: 2135,
      &quot;final_text_present&quot;: 4,
      &quot;gpu_energy_j_lower&quot;: 14654.706,
      &quot;gpu_energy_j_upper&quot;: 16509.816,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.2179760799862414,
      &quot;tokens_s_completed_requests&quot;: 35.79837929004811,
      &quot;valid_terminal_output&quot;: 13,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    }
  }
}</pre></details></td></tr><tr><td>Qwen3.5-0.8B</td><td>SCREENING VOLLSTÄNDIG · WEITERE DIAGNOSE</td><td>0/16 · 0.0%</td><td>7/16 · 43.8%</td><td>76.7</td><td>150.4</td><td>1,083.0</td><td>1,546.5</td><td>NOT MEASURED</td><td><a href="../experiments/R514/">Screening R514</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;c33850fc274f506ed87d214a3e9c6f02465cfd04ea82c3bb7c0b28b560d421e1&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;0ad885ffd4bb022fc4f0d33a3308fa108ef8613159d3b3a67e23abca056b7a6c&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;Qwen/Qwen3.5-0.8B&quot;,
      &quot;base_revision&quot;: &quot;2fc06364715b967f1860aea9cf38778875588b17&quot;,
      &quot;hf_repository&quot;: &quot;unsloth/Qwen3.5-0.8B-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;6ab461498e2023f6e3c1baea90a8f0fe38ab64d0&quot;,
      &quot;license&quot;: &quot;apache-2.0&quot;,
      &quot;parameters_in_GGUF&quot;: 752393024,
      &quot;quantizer&quot;: &quot;Unsloth&quot;
    },
    &quot;parent_profile_id&quot;: &quot;qwen35-08b-q8-native-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q8_0&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;qwen35&quot;,
        &quot;artifact_sha256&quot;: &quot;0ad885ffd4bb022fc4f0d33a3308fa108ef8613159d3b3a67e23abca056b7a6c&quot;,
        &quot;family_id&quot;: &quot;qwen35_08b&quot;,
        &quot;hf_repository&quot;: &quot;unsloth/Qwen3.5-0.8B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;6ab461498e2023f6e3c1baea90a8f0fe38ab64d0&quot;,
        &quot;name&quot;: &quot;Qwen3.5-0.8B&quot;,
        &quot;parameters_in_GGUF&quot;: 752393024,
        &quot;quantization&quot;: &quot;Q8_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Qwen3.5-0.8B&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-0d3fc86251b2e81f00ebb221eccc013a26819f1f6220fb0c6f0404763572331c&quot;,
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
        &quot;chat_template_sha256&quot;: &quot;7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67&quot;,
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
          &quot;min_p&quot;: 0.0,
          &quot;presence_penalty&quot;: 2.0,
          &quot;repeat_penalty&quot;: 1.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 1.0,
          &quot;top_k&quot;: 20,
          &quot;top_p&quot;: 1.0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: &quot;off&quot;,
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-e5ddc1799699bf24d07b923cfc8e7802ed0e1ff12d71abce1914d4feb4aecbb4&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;4ab87b8b5f8adad05c94d31d1ee0cef8f2521f2d827948516c71dd4d27c4fcd3&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;6a1ac65b988d3843616c95e9df012fccffd15e75a1010b161d8ff23ff6cf8380&quot;,
        &quot;actual_profile_sha256&quot;: &quot;8f04e95e1a04ccac68e3b2843c8863423b6074e225e264a6208a9704efb57bd6&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;a8978b17f9a0fcc2812687aa2ab0f7050fa8bd649dde06fd998c5e325572625a&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;33ff41443a2a7d93c9a49ae8dada6699bb2b8962839f035c8ff024a9b0c022b6&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:0ad885ffd4bb022fc4f0d33a3308fa108ef8613159d3b3a67e23abca056b7a6c]&quot;,
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
          &quot;[artifact:7f0e529032c25183bcd66c7f238da2d377f43be754a94e2725a58c4e16d2ed67]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;a0b0b87dbbefd7c7c05f5260d2a05922142cc722b41cfedb0071dcc80bb37d94&quot;,
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
      &quot;presence_penalty&quot;: 2.0,
      &quot;repeat_penalty&quot;: 1.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 1.0,
      &quot;top_k&quot;: 20,
      &quot;top_p&quot;: 1.0
    },
    &quot;screening_configuration_id&quot;: &quot;screening-config-291e4f2b2bd4d58552ace22af81769c1ebdaee8314bfc216baec1b408361ba79&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-24T23:49:04.539920+00:00&quot;,
  &quot;decision&quot;: &quot;WEITERE_DIAGNOSE_NO_AUTOMATIC_QUALITY_EXCLUSION&quot;,
  &quot;diagnostic_audit_sha256&quot;: &quot;e567dbbbda11abd7d32325255f6a0a103ea4fdbd1059777aeee59d30f6605545&quot;,
  &quot;diagnostic_summary&quot;: {
    &quot;functional_cases_passed&quot;: 16,
    &quot;functional_cases_total&quot;: 69,
    &quot;sandbox_failure_classes&quot;: {
      &quot;IndentationError&quot;: 1,
      &quot;LOADED_BUT_FUNCTIONAL_CASE_FAILURE&quot;: 11,
      &quot;SyntaxError&quot;: 4
    },
    &quot;task_successes&quot;: 0,
    &quot;tasks&quot;: 16
  },
  &quot;experiment_id&quot;: &quot;R514&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;151004c63549d85a4d6f3cacb9454637c69a6de218885238cd24802ec8e20f5a&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Qwen3.5-0.8B&quot;,
  &quot;parent_experiment_id&quot;: &quot;R514&quot;,
  &quot;peak_vram_mib&quot;: 1546.5,
  &quot;selection_status&quot;: &quot;WEITERE DIAGNOSE&quot;,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 76.76757358,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: null,
      &quot;GPU_j_per_success_upper&quot;: null,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 70.826671294,
      &quot;completion_tokens&quot;: 10843,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 7300.057,
      &quot;gpu_energy_j_upper&quot;: 8145.608,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 0,
      &quot;successful_tasks_s_completed_requests&quot;: 0.0,
      &quot;tokens_s_completed_requests&quot;: 153.09204572089715,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0,
        0.1936076805344365
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 40.137571428571434,
      &quot;GPU_j_per_success_upper&quot;: 156.82171428571428,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 5.922701359,
      &quot;completion_tokens&quot;: 699,
      &quot;final_text_present&quot;: 1,
      &quot;gpu_energy_j_lower&quot;: 280.963,
      &quot;gpu_energy_j_upper&quot;: 1097.752,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 7,
      &quot;successful_tasks_s_completed_requests&quot;: 1.1818931220232742,
      &quot;tokens_s_completed_requests&quot;: 118.02047032775268,
      &quot;valid_terminal_output&quot;: 7,
      &quot;wilson95&quot;: [
        0.23098652405492354,
        0.6682144360118811
      ]
    }
  }
}</pre></details></td></tr><tr><td>OmniCoder-9B · bartowski Q6</td><td>SCREENING VOLLSTÄNDIG · VERTIEFUNG EMPFOHLEN</td><td>14/16 · 87.5%</td><td>14/16 · 87.5%</td><td>62.6</td><td>69.4</td><td>518.2</td><td>7,680.5</td><td><a href="../experiments/R516/">R516</a> · <a href="../experiments/R517/">R517</a> · <a href="../configuration-comparison/">Official comparison</a></td><td><a href="../experiments/R515/">Screening R515</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;3cd7716f53c300fc23a043c0f8c939244a7033084caec34253a29d358697b403&quot;,
  &quot;comparison_audit_sha256&quot;: &quot;c60c95f9ca764628d88b2d00ff90f3ee102cd4304c60f22760545393a4a52b48&quot;,
  &quot;comparison_summary&quot;: {
    &quot;additional_peak_vram_mib&quot;: 324.0,
    &quot;baseline&quot;: {
      &quot;coding_successes&quot;: 13,
      &quot;complete_request_wall_s&quot;: 67.157283623,
      &quot;completion_tokens&quot;: 4674,
      &quot;mock_tool_successes&quot;: 14,
      &quot;peak_device_vram_mib&quot;: 7356.5,
      &quot;task_phase_s&quot;: 67.175594346,
      &quot;tasks_per_category&quot;: 16
    },
    &quot;candidate&quot;: {
      &quot;coding_successes&quot;: 14,
      &quot;complete_request_wall_s&quot;: 62.648162967,
      &quot;completion_tokens&quot;: 4348,
      &quot;mock_tool_successes&quot;: 14,
      &quot;peak_device_vram_mib&quot;: 7680.5,
      &quot;task_phase_s&quot;: 62.664775063,
      &quot;tasks_per_category&quot;: 16
    }
  },
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;Tesslate/OmniCoder-9B&quot;,
      &quot;base_revision&quot;: &quot;9edd36a30fc7b95b6fd81b7ea16a73cbaf205734&quot;,
      &quot;hf_repository&quot;: &quot;bartowski/Tesslate_OmniCoder-9B-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;f0fbc2243f49ab2dbdf91fe5930dd73e6bce767c&quot;,
      &quot;license&quot;: &quot;apache-2.0&quot;,
      &quot;parameters_in_GGUF&quot;: 8953803264,
      &quot;quantizer&quot;: &quot;bartowski&quot;
    },
    &quot;parent_profile_id&quot;: &quot;omni-bartowski-q6-native-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;qwen35&quot;,
        &quot;artifact_sha256&quot;: &quot;a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052&quot;,
        &quot;family_id&quot;: &quot;omni&quot;,
        &quot;hf_repository&quot;: &quot;bartowski/Tesslate_OmniCoder-9B-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;f0fbc2243f49ab2dbdf91fe5930dd73e6bce767c&quot;,
        &quot;name&quot;: &quot;OmniCoder-9B \u00b7 bartowski Q6&quot;,
        &quot;parameters_in_GGUF&quot;: 8953803264,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;OmniCoder-9B \u00b7 bartowski Q6&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-1b4802fd05fca260d7101aad04f04e6693e505e633c99caabd04117ebf39e34b&quot;,
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
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-e9e2f024338f647f3f3c71c5f468d7377f04be185bdceb1bcf4c6e5ac2a54bc3&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;b551ff90b51d15eb805c61649d8c6713284974a022ecf9d8ff411cd9f168ba01&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;061b33cb94ddebde7d0cfb507a87da81cb96ebb0cf8ef1793157f26497ce9b9a&quot;,
        &quot;actual_profile_sha256&quot;: &quot;a0f758bd36c8d005fe3e149ee07373f7164ac565cdea1a52dfa9b406f8295fea&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;5b755feb0d56c735bcf1bcc202f3e50e1a452a4139d5cb1d9196068a732ab7a2&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;142bc12a54f3cc773104140541a5decdcb32a9438d4fffda68d428310a0f4fe6&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:a73cc3136da753063e667edef95bec3bbf47829e34a2a31bf0f5a29c970f9052]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;07a85ed4fcadbc70d2e3437a9d4e907c08425385fe74d9b553ea22a5cf86e47d&quot;,
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
    &quot;screening_configuration_id&quot;: &quot;screening-config-4d900edb2f0df287b0592176fc9b2e1e87c9a49dd2e1f2dcd81f72f1927e5018&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-25T00:23:58.566844+00:00&quot;,
  &quot;decision&quot;: &quot;PROMISING_ALTERNATE_ARTIFACT_PROCEED_TO_FULL_QUALIFICATION&quot;,
  &quot;experiment_id&quot;: &quot;R515&quot;,
  &quot;full_benchmark_runs&quot;: [
    {
      &quot;audit_hash&quot;: &quot;518b6f38c0768b23386ee218e6c86a77d672e6631fc246ff685e53db6b50f4dd&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-343ddfa996f79239e54edb7a1ddd23732c676d7d21d5d83cb22efddfc23e8f9c&quot;,
      &quot;experiment_id&quot;: &quot;R516&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf&quot;
    },
    {
      &quot;audit_hash&quot;: &quot;d995531168d22041ed7c3157c30cf3bc05afcc806c0f3b470514f812ecb59f69&quot;,
      &quot;benchmark_identity_id&quot;: &quot;bench-5d4b86368f32863a23b3a9a2c99c8077c3e5d9b9731a76b1d6db15573d6c6fbe&quot;,
      &quot;experiment_id&quot;: &quot;R517&quot;,
      &quot;official_eligible&quot;: true,
      &quot;runtime_configuration_id&quot;: &quot;cfg-ef44057a9355a2b971bac6e5dcf6f018050b972a796a26c03d68c09af2e52049&quot;
    }
  ],
  &quot;full_benchmark_status&quot;: &quot;MATCHED_FULL_LOCAL_RESULTS&quot;,
  &quot;independent_review_sha256&quot;: &quot;9d10929dde759251e65ee9869bb5a4c27f228ba0b3ba69b3dbbfc4ec8055605e&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;OmniCoder-9B \u00b7 bartowski Q6&quot;,
  &quot;parent_experiment_id&quot;: &quot;R515&quot;,
  &quot;peak_vram_mib&quot;: 7680.5,
  &quot;selection_status&quot;: &quot;VERTIEFUNG EMPFOHLEN&quot;,
  &quot;source_provenance_limits&quot;: &quot;The inspected upstream model-card/config revision is not a verified exact quantization-parent weight revision. Different quantization recipes and possibly checkpoint ancestry remain confounded. This compares whole existing artifacts, not a proven fine-tune or isolated tensor-precision intervention.&quot;,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 62.664775063,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 820.0747142857143,
      &quot;GPU_j_per_success_upper&quot;: 951.4265714285714,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 47.434242018,
      &quot;completion_tokens&quot;: 3587,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 11481.046,
      &quot;gpu_energy_j_upper&quot;: 13319.972,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.2951454351202109,
      &quot;tokens_s_completed_requests&quot;: 75.62047684115689,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 216.24792857142856,
      &quot;GPU_j_per_success_upper&quot;: 345.40621428571427,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 15.213920949,
      &quot;completion_tokens&quot;: 761,
      &quot;final_text_present&quot;: 4,
      &quot;gpu_energy_j_lower&quot;: 3027.471,
      &quot;gpu_energy_j_upper&quot;: 4835.687,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 14,
      &quot;successful_tasks_s_completed_requests&quot;: 0.9202098556270079,
      &quot;tokens_s_completed_requests&quot;: 50.01997858086807,
      &quot;valid_terminal_output&quot;: 14,
      &quot;wilson95&quot;: [
        0.639771727342413,
        0.9650225122567595
      ]
    }
  }
}</pre></details></td></tr><tr><td>Ministral-3-14B-Instruct-2512</td><td>SCREENING VOLLSTÄNDIG</td><td>11/16 · 68.8%</td><td>9/16 · 56.2%</td><td>36.7</td><td>53.1</td><td>412.1</td><td>10,950.5</td><td>NOT MEASURED</td><td><a href="../experiments/R552/">Screening R552</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;0727b3219022724c5926db58337c36ce98d1a44e73ebbf1742f8a3ec9728d928&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;mistralai/Ministral-3-14B-Instruct-2512&quot;,
      &quot;base_revision&quot;: &quot;29439f81c2be264d8d393273f99e7db9c0961120&quot;,
      &quot;hf_repository&quot;: &quot;mistralai/Ministral-3-14B-Instruct-2512-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;74fac473c43357d7fb2671713608183cc72496d0&quot;,
      &quot;license&quot;: &quot;apache-2.0&quot;,
      &quot;parameters_in_GGUF&quot;: 13506073600,
      &quot;quantizer&quot;: &quot;mistralai&quot;
    },
    &quot;parent_profile_id&quot;: &quot;ministral3-14b-instruct-q5km-native-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q5_K_M&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;mistral3&quot;,
        &quot;artifact_sha256&quot;: &quot;f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000&quot;,
        &quot;family_id&quot;: &quot;ministral3_14b&quot;,
        &quot;hf_repository&quot;: &quot;mistralai/Ministral-3-14B-Instruct-2512-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;74fac473c43357d7fb2671713608183cc72496d0&quot;,
        &quot;name&quot;: &quot;Ministral-3-14B-Instruct-2512&quot;,
        &quot;parameters_in_GGUF&quot;: 13506073600,
        &quot;quantization&quot;: &quot;Q5_K_M&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Ministral-3-14B-Instruct-2512&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-5b10e1392554e863d5388135a4c31616c93bc504b637ecdce3bd44d13b4e4475&quot;,
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
        &quot;chat_template_sha256&quot;: &quot;6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: null,
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: null,
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-2e50f43337cb3d364e5043c8981f54dd572817a681199f0475443170250875d3&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;d63eb9b24ce6e6b591b5b3d4c2ee90485c7b66d80041460cd35a4b95782517bd&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;95dfa3c9a3d7ce0d308ec4486264bf721b21374255977047ef22cce26699b401&quot;,
        &quot;actual_profile_sha256&quot;: &quot;f97a39fa2db1d7ef399448973fc5fd819535119e437b5097145406346bdfbb5c&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;239fe4040540cb2f5cf62e8870321a62ccbb495bdc13b9fbe08b47c014f03b62&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;9bfe7d70ac76920e4e963d79357ba734c25cf0db5dd0d7a5c32b6b03c0f5dfeb&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:f16fef77021df0d4c22e69140a2038478370492f51867b6237699918ae711000]&quot;,
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
          &quot;[artifact:6cc0f8c0cfbafcfd8b146d60e947a1b2511ace4db907b0a73f6a474d04bdca9b]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;39452ae5abdcc955a7a6fcde2c09cce5ec92c3438ee0c11a82d28fb69df458d7&quot;,
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
      &quot;max_tokens&quot;: 4096,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;screening_configuration_id&quot;: &quot;screening-config-8c9591cad6eec1ca04bec9707a46954cbdeb463adc95209d44c64e90505ebacf&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-26T21:01:01.149911+00:00&quot;,
  &quot;decision&quot;: &quot;First native source-reviewed screening only. No full result inherited from the engine reference; retain without small-sample quality rejection.&quot;,
  &quot;experiment_id&quot;: &quot;R552&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;7c6fb2c22d7a16acfcdfba85bbb5b94f4e21248fc45303965d21ecc45fb49478&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Ministral-3-14B-Instruct-2512&quot;,
  &quot;parent_experiment_id&quot;: &quot;R552&quot;,
  &quot;peak_vram_mib&quot;: 10950.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 36.75011769,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 571.0773636363637,
      &quot;GPU_j_per_success_upper&quot;: 760.8093636363636,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 25.697165944,
      &quot;completion_tokens&quot;: 1535,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 6281.851,
      &quot;gpu_energy_j_upper&quot;: 8368.903,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.42806276863259995,
      &quot;tokens_s_completed_requests&quot;: 59.734213622821905,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 217.72455555555555,
      &quot;GPU_j_per_success_upper&quot;: 447.018,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 11.037618547,
      &quot;completion_tokens&quot;: 417,
      &quot;final_text_present&quot;: 7,
      &quot;gpu_energy_j_lower&quot;: 1959.521,
      &quot;gpu_energy_j_upper&quot;: 4023.162,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 9,
      &quot;successful_tasks_s_completed_requests&quot;: 0.8153932808672918,
      &quot;tokens_s_completed_requests&quot;: 37.77988868018452,
      &quot;valid_terminal_output&quot;: 9,
      &quot;wilson95&quot;: [
        0.331785563988119,
        0.7690134759450765
      ]
    }
  }
}</pre></details></td></tr><tr><td>gpt-oss-20b</td><td>SCREENING VOLLSTÄNDIG</td><td>15/16 · 93.8%</td><td>11/16 · 68.8%</td><td>149.2</td><td>119.4</td><td>1,127.4</td><td>11,934.5</td><td>NOT MEASURED</td><td><a href="../experiments/R553/">Screening R553</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;61a32aaf587adfe87bd8487ae90ce9fbc07e34defdbeaf7d558457086dd24be1&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;27cd6c432c7672cb812a92f611cf3ba7bbc35928262bb1e1253ff4ee6ae35901&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;openai/gpt-oss-20b&quot;,
      &quot;base_revision&quot;: &quot;6cee5e81ee83917806bbde320786a8fb61efebee&quot;,
      &quot;hf_repository&quot;: &quot;ggml-org/gpt-oss-20b-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;15dcfc7e7c608c6161507211ed43c5b590801b4b&quot;,
      &quot;license&quot;: &quot;apache-2.0&quot;,
      &quot;parameters_in_GGUF&quot;: 20914757184,
      &quot;quantizer&quot;: &quot;ggml-org&quot;
    },
    &quot;parent_profile_id&quot;: &quot;gpt-oss-20b-mxfp4-native-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;MXFP4&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;gpt-oss&quot;,
        &quot;artifact_sha256&quot;: &quot;27cd6c432c7672cb812a92f611cf3ba7bbc35928262bb1e1253ff4ee6ae35901&quot;,
        &quot;family_id&quot;: &quot;gpt_oss_20b&quot;,
        &quot;hf_repository&quot;: &quot;ggml-org/gpt-oss-20b-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;15dcfc7e7c608c6161507211ed43c5b590801b4b&quot;,
        &quot;name&quot;: &quot;gpt-oss-20b&quot;,
        &quot;parameters_in_GGUF&quot;: 20914757184,
        &quot;quantization&quot;: &quot;MXFP4&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;gpt-oss-20b&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-c5a1bbf0bdc560fdcd257d1257ef97281119475d6a365f5207d23dc30958838f&quot;,
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
        &quot;chat_template_sha256&quot;: &quot;a4c9919cbbd4acdd51ccffe22da049264b1b73e59055fa58811a99efbd7c8146&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: null,
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;min_p&quot;: 0.0,
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 1.0,
          &quot;top_k&quot;: 0,
          &quot;top_p&quot;: 1.0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: null,
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-2b24de433d1d73d9fb8eada5478d075be38b4d90dc729968c091b0130754a74a&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;789c4973dab2c8907f2b0132611edf117253dcfe23304ded6385a312b60120ec&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;cf16c49c911128b4ddae01292d448d0cc5bcfb883aaa075a14b83589caac8d8e&quot;,
        &quot;actual_profile_sha256&quot;: &quot;e0b53b6c5d087b26195a2b58ff5d3a7b5c4a6ffa2e64809e6ae16188599a9b7b&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;a1ec580ccd0c4a3530788a9d80cef297a786e1d58e02454f7842ca340faeb7a4&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;2d9053220e19c6ace0dcc35c461427b5e76a8d3fed145d35ab661fef41f7e0eb&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:27cd6c432c7672cb812a92f611cf3ba7bbc35928262bb1e1253ff4ee6ae35901]&quot;,
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
          &quot;[artifact:a4c9919cbbd4acdd51ccffe22da049264b1b73e59055fa58811a99efbd7c8146]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;d5e89262c07cf69d11f379d3bf4fd1abe686e4b7631fd050afc66a330d1e211e&quot;,
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
      &quot;max_tokens&quot;: 4096,
      &quot;min_p&quot;: 0.0,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 1.0,
      &quot;top_k&quot;: 0,
      &quot;top_p&quot;: 1.0
    },
    &quot;screening_configuration_id&quot;: &quot;screening-config-7be9ebc4cab5e5d282fe62dff3160c4d9b8bb8003257b6889b453312964305b0&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-26T21:36:34.059286+00:00&quot;,
  &quot;decision&quot;: &quot;First native source-reviewed screening only. No full result inherited from the engine reference; retain without small-sample quality rejection.&quot;,
  &quot;experiment_id&quot;: &quot;R553&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;25585b1cb3f86adca9e4426f60c82a31518953f40ee49d964d1966890ac7db9e&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;gpt-oss-20b&quot;,
  &quot;parent_experiment_id&quot;: &quot;R553&quot;,
  &quot;peak_vram_mib&quot;: 11934.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 149.234217539,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1611.4779999999998,
      &quot;GPU_j_per_success_upper&quot;: 1714.4197333333332,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 120.69507172,
      &quot;completion_tokens&quot;: 14747,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 24172.17,
      &quot;gpu_energy_j_upper&quot;: 25716.296,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 15,
      &quot;successful_tasks_s_completed_requests&quot;: 0.12428013659744483,
      &quot;tokens_s_completed_requests&quot;: 122.18394496016792,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.7167126242970107,
        0.9888806552353576
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 467.31045454545455,
      &quot;GPU_j_per_success_upper&quot;: 610.9025454545455,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 28.514090262,
      &quot;completion_tokens&quot;: 3073,
      &quot;final_text_present&quot;: 6,
      &quot;gpu_energy_j_lower&quot;: 5140.415,
      &quot;gpu_energy_j_upper&quot;: 6719.928,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.38577418739041514,
      &quot;tokens_s_completed_requests&quot;: 107.77127980461326,
      &quot;valid_terminal_output&quot;: 11,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    }
  }
}</pre></details></td></tr><tr><td>Ministral-3-8B-Instruct-2512</td><td>SCREENING VOLLSTÄNDIG</td><td>13/16 · 81.2%</td><td>10/16 · 62.5%</td><td>33.6</td><td>63.3</td><td>253.3</td><td>10,014.5</td><td>NOT MEASURED</td><td><a href="../experiments/R554/">Screening R554</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;17e2267cff8b807c9dc3d7c3973a52143683f4426366b679ef5910cfa733c277&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;bd0ca58473b64618df4d08c1410cc25c910ca84e647833ebaf099e0fc0523b45&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;mistralai/Ministral-3-8B-Instruct-2512&quot;,
      &quot;base_revision&quot;: &quot;5b26027e7b19eeb4b7352e1fed3926375dd2cb4d&quot;,
      &quot;hf_repository&quot;: &quot;mistralai/Ministral-3-8B-Instruct-2512-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;0102285ad796bd99af90f58de616092e5630e970&quot;,
      &quot;license&quot;: &quot;apache-2.0&quot;,
      &quot;parameters_in_GGUF&quot;: 8489553920,
      &quot;quantizer&quot;: &quot;mistralai&quot;
    },
    &quot;parent_profile_id&quot;: &quot;ministral3-8b-instruct-q8-native-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q8_0&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;mistral3&quot;,
        &quot;artifact_sha256&quot;: &quot;bd0ca58473b64618df4d08c1410cc25c910ca84e647833ebaf099e0fc0523b45&quot;,
        &quot;family_id&quot;: &quot;ministral3_8b&quot;,
        &quot;hf_repository&quot;: &quot;mistralai/Ministral-3-8B-Instruct-2512-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;0102285ad796bd99af90f58de616092e5630e970&quot;,
        &quot;name&quot;: &quot;Ministral-3-8B-Instruct-2512&quot;,
        &quot;parameters_in_GGUF&quot;: 8489553920,
        &quot;quantization&quot;: &quot;Q8_0&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Ministral-3-8B-Instruct-2512&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-f15644ade257de4692a193cfe1e41cb02879f2e5d4e44287d9d979119e533276&quot;,
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
        &quot;chat_template_sha256&quot;: &quot;749c9389522945c616d66276cda637639fe83ed4c865eb5bb6dcff7bc7fa34c1&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: null,
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: null,
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-f6563829a5d2de7d163afc74c15f4d4b51a7bd1a616a92217fb52f92b154b1e3&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;57c6a22d0abffe3286e84b03d2668bcf198aa934d20fa96316ba720929162dfa&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;66350c7d2432c8f63e09c76ab37d31411ffd5622a55d472615bdd28290e02619&quot;,
        &quot;actual_profile_sha256&quot;: &quot;0026bb6b7b028a698e1d909d5592f0b55e384ab2c0e4544c08f5af4fa831e460&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;cae4e0ee01463ada1d6bd830baed62a39a10f4112e3ef40b00059cdb33d90e36&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;9c71b2e499f884c6e103165bbaff300fca1247d4e5a4557f0b20188991c35803&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:bd0ca58473b64618df4d08c1410cc25c910ca84e647833ebaf099e0fc0523b45]&quot;,
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
          &quot;[artifact:749c9389522945c616d66276cda637639fe83ed4c865eb5bb6dcff7bc7fa34c1]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;63ef3b53bd8b9615e2ba87f6d5eda5b5d5f80422eaa6f1744e618f7ca746cf24&quot;,
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
      &quot;max_tokens&quot;: 4096,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;screening_configuration_id&quot;: &quot;screening-config-3110ac6cba4af1a74a0919270dd0d5ac5306a55ef9c545a645ee8f7ea613d946&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-26T21:46:10.011396+00:00&quot;,
  &quot;decision&quot;: &quot;First native source-reviewed screening only. No full result inherited from the engine reference; retain without small-sample quality rejection.&quot;,
  &quot;experiment_id&quot;: &quot;R554&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;0aae0f7784ca06be3c7b2d37deceb90d415401e20fb6a680ddb29c53a0e82747&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Ministral-3-8B-Instruct-2512&quot;,
  &quot;parent_experiment_id&quot;: &quot;R554&quot;,
  &quot;peak_vram_mib&quot;: 10014.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 33.639376769,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 359.64084615384616,
      &quot;GPU_j_per_success_upper&quot;: 497.2534615384615,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 24.917414863,
      &quot;completion_tokens&quot;: 1710,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 4675.331,
      &quot;gpu_energy_j_upper&quot;: 6464.295,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 13,
      &quot;successful_tasks_s_completed_requests&quot;: 0.5217234641505194,
      &quot;tokens_s_completed_requests&quot;: 68.62670182287602,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.5699111903802586,
        0.9340840092857187
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 115.1274,
      &quot;GPU_j_per_success_upper&quot;: 291.1835,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 8.690347331,
      &quot;completion_tokens&quot;: 416,
      &quot;final_text_present&quot;: 6,
      &quot;gpu_energy_j_lower&quot;: 1151.274,
      &quot;gpu_energy_j_upper&quot;: 2911.835,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 10,
      &quot;successful_tasks_s_completed_requests&quot;: 1.1507019937313943,
      &quot;tokens_s_completed_requests&quot;: 47.869202939226,
      &quot;valid_terminal_output&quot;: 10,
      &quot;wilson95&quot;: [
        0.38641040545502714,
        0.8151876744113636
      ]
    }
  }
}</pre></details></td></tr><tr><td>Phi-4 <small title="Explicit generic tool-wire adapter; no native tool-training claim">· tool bridge</small></td><td>SCREENING VOLLSTÄNDIG</td><td>11/16 · 68.8%</td><td>9/16 · 56.2%</td><td>72.0</td><td>48.9</td><td>929.8</td><td>13,792.5</td><td>NOT MEASURED</td><td><a href="../experiments/R555/">Screening R555</a> · <details><summary>Profile & evidence</summary><pre>{
  &quot;audit_sha256&quot;: &quot;701163dc62d5fc6a02e9ff5a39fe063d95e2505e8e230ed131758953b49d5c58&quot;,
  &quot;conditions&quot;: &quot;Single native-profile session; frozen base-task order; explicit generic tool-wire adapter, not native tool-training evidence&quot;,
  &quot;configuration&quot;: {
    &quot;binary_identities&quot;: {
      &quot;libggml-cuda.so.0.26.0&quot;: &quot;f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5&quot;,
      &quot;llama-server&quot;: &quot;08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54&quot;
    },
    &quot;context&quot;: 8192,
    &quot;engine&quot;: &quot;llama.cpp native&quot;,
    &quot;engine_version&quot;: null,
    &quot;hardware&quot;: &quot;Tesla V100 SXM2 16 GB&quot;,
    &quot;model_sha256&quot;: &quot;537248da5492a9a34b1d811307c6b9226d9539a81653aa9bb0d7ec6104169320&quot;,
    &quot;model_source&quot;: {
      &quot;base_repository&quot;: &quot;microsoft/phi-4&quot;,
      &quot;base_revision&quot;: &quot;2db69c1c3e91a05d2c64a3185acfbaf36f744e25&quot;,
      &quot;hf_repository&quot;: &quot;bartowski/phi-4-GGUF&quot;,
      &quot;hf_revision&quot;: &quot;19cd65f97c2f1712a81c506611d3f9c94b16a1e1&quot;,
      &quot;license&quot;: &quot;mit&quot;,
      &quot;parameters_in_GGUF&quot;: 14659507200,
      &quot;quantizer&quot;: &quot;bartowski&quot;
    },
    &quot;native_template_sha256&quot;: &quot;fe4120415a3858b873955c92ce3a103a95bc97c2cb00b72e62659aaf0f891ee5&quot;,
    &quot;parent_profile_id&quot;: &quot;phi4-q6-toolbridge-screening32-task1200-reviewed-sm70&quot;,
    &quot;power_w&quot;: 300,
    &quot;quantization&quot;: &quot;Q6_K&quot;,
    &quot;recorded_native_profile&quot;: {
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
        &quot;architecture&quot;: &quot;phi3&quot;,
        &quot;artifact_sha256&quot;: &quot;537248da5492a9a34b1d811307c6b9226d9539a81653aa9bb0d7ec6104169320&quot;,
        &quot;family_id&quot;: &quot;phi4&quot;,
        &quot;hf_repository&quot;: &quot;bartowski/phi-4-GGUF&quot;,
        &quot;hf_revision&quot;: &quot;19cd65f97c2f1712a81c506611d3f9c94b16a1e1&quot;,
        &quot;name&quot;: &quot;Phi-4&quot;,
        &quot;parameters_in_GGUF&quot;: 14659507200,
        &quot;quantization&quot;: &quot;Q6_K&quot;,
        &quot;tensor_precision_map&quot;: null,
        &quot;variant&quot;: &quot;Phi-4&quot;,
        &quot;weight_transformations&quot;: {
          &quot;caution&quot;: &quot;Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.&quot;,
          &quot;description&quot;: &quot;SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED&quot;,
          &quot;proof&quot;: null
        }
      },
      &quot;model_artifact_id&quot;: &quot;artifact-6712cd1f2ac9b7b5b79709b54e60efc642ee9fec6075e09e4de84b2a0ef00da1&quot;,
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
        &quot;chat_template_sha256&quot;: &quot;4e5e30f37831a4c1a458d1bdc90199d66ed862684f605875ba9b3ed3bb88d895&quot;,
        &quot;context&quot;: &quot;8192&quot;,
        &quot;execution_deadline_s&quot;: 1200,
        &quot;max_output&quot;: 4096,
        &quot;microbatch&quot;: &quot;512&quot;,
        &quot;native_HTTP_timeout_policy&quot;: &quot;REMAINING_TASK_TIME&quot;,
        &quot;native_template_controls&quot;: null,
        &quot;power_limit_w&quot;: 300,
        &quot;sampling&quot;: {
          &quot;seed&quot;: 1001,
          &quot;temperature&quot;: 0
        },
        &quot;startup_limit_s&quot;: 180,
        &quot;thinking_reasoning_requested&quot;: null,
        &quot;timing_scope&quot;: &quot;DEVELOPMENT_SCREEN_TASK_PHASE_ONLY&quot;,
        &quot;tokenizer_identity&quot;: null
      },
      &quot;runtime_configuration_id&quot;: &quot;cfg-6c502e1d89dc38cec5a6404aafdb6576f6035ac506883562177d10544525484d&quot;,
      &quot;schema_version&quot;: 1,
      &quot;source_plan_sha256&quot;: &quot;65c391aeb1cc04e44d8353895f2980d0e237afee927542f9ea3c225f1b0194a4&quot;,
      &quot;source_provenance&quot;: {
        &quot;actual_launch_sha256&quot;: &quot;5e2fa6d1f512a157a1d3a7b686bb627c8cb6b9eff0c619045dbfd5952c168f0a&quot;,
        &quot;actual_profile_sha256&quot;: &quot;1398ad784538c12704e226a5119ef5568ab7921abc32ea72dddf7d4de4cc446b&quot;,
        &quot;evidence_scope&quot;: &quot;FIRST_SOURCE_REVIEWED_DEVELOPMENT_SCREEN_ONLY&quot;,
        &quot;frozen_model_profile_sha256&quot;: &quot;275ea4c66c0c85e743384ba255e413a0f4b784f27d6e2c281a8136467b3ab046&quot;,
        &quot;kind&quot;: &quot;BROKER_NATIVE_CAPTURED_CONFIGURATION&quot;,
        &quot;model_source_package_sha256&quot;: &quot;c4ee540f75666fd9db4092a3e3a84db5493bdd9c413cbec366bc35a456036770&quot;
      },
      &quot;start_parameters&quot;: {
        &quot;argv&quot;: [
          &quot;llama-server&quot;,
          &quot;--model&quot;,
          &quot;[artifact:537248da5492a9a34b1d811307c6b9226d9539a81653aa9bb0d7ec6104169320]&quot;,
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
          &quot;[artifact:4e5e30f37831a4c1a458d1bdc90199d66ed862684f605875ba9b3ed3bb88d895]&quot;,
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
        &quot;exact_private_launch_sha256&quot;: &quot;2bd3f264b976c5a62d00135426838df880bd6794ecdf1a5b7745b836f6ea5825&quot;,
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
      &quot;max_tokens&quot;: 4096,
      &quot;seed&quot;: 1001,
      &quot;temperature&quot;: 0
    },
    &quot;runtime_template_sha256&quot;: &quot;4e5e30f37831a4c1a458d1bdc90199d66ed862684f605875ba9b3ed3bb88d895&quot;,
    &quot;screening_configuration_id&quot;: &quot;screening-config-b9547b5be700e0762b1fae802fa5410d2c8177feda00f7318e7369be72715c79&quot;,
    &quot;task_time_policy&quot;: {
      &quot;cleanup_seconds&quot;: 60,
      &quot;startup_seconds&quot;: 180,
      &quot;task_seconds&quot;: 1200,
      &quot;wall_seconds&quot;: 1440
    },
    &quot;tool_transport&quot;: &quot;EXPLICIT_GENERIC_XML_JSON_BRIDGE_PHI_ROLE_DELIMITERS_NOT_NATIVE_TRAINING&quot;,
    &quot;warmup_requests&quot;: 2
  },
  &quot;date&quot;: &quot;2026-10-26T21:59:30.395271+00:00&quot;,
  &quot;decision&quot;: &quot;First native source-reviewed screening only. No full result inherited from the engine reference; retain without small-sample quality rejection.&quot;,
  &quot;experiment_id&quot;: &quot;R555&quot;,
  &quot;full_benchmark_runs&quot;: [],
  &quot;full_benchmark_status&quot;: &quot;NOT MEASURED&quot;,
  &quot;independent_review_sha256&quot;: &quot;198e92eea5e081373228b0ad47482ee93b4da944ee8237d7d88ee5c4f54e72fd&quot;,
  &quot;local_artifact_available&quot;: true,
  &quot;model&quot;: &quot;Phi-4&quot;,
  &quot;parent_experiment_id&quot;: &quot;R555&quot;,
  &quot;peak_vram_mib&quot;: 13792.5,
  &quot;status&quot;: &quot;SCREENING VOLLST\u00c4NDIG&quot;,
  &quot;task_phase_s&quot;: 72.004129515,
  &quot;timeouts&quot;: 0,
  &quot;category_results&quot;: {
    &quot;coding&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 1121.010909090909,
      &quot;GPU_j_per_success_upper&quot;: 1311.6644545454544,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 45.808151238,
      &quot;completion_tokens&quot;: 2427,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 12331.12,
      &quot;gpu_energy_j_upper&quot;: 14428.309,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 11,
      &quot;successful_tasks_s_completed_requests&quot;: 0.240131935097066,
      &quot;tokens_s_completed_requests&quot;: 52.98183695277993,
      &quot;valid_terminal_output&quot;: 16,
      &quot;wilson95&quot;: [
        0.44404355834740666,
        0.8583535614521796
      ]
    },
    &quot;tools&quot;: {
      &quot;GPU_j_per_success_lower&quot;: 696.0805555555556,
      &quot;GPU_j_per_success_upper&quot;: 927.8326666666667,
      &quot;completed&quot;: 16,
      &quot;completed_request_wall_s&quot;: 26.17929219,
      &quot;completion_tokens&quot;: 1096,
      &quot;final_text_present&quot;: 16,
      &quot;gpu_energy_j_lower&quot;: 6264.725,
      &quot;gpu_energy_j_upper&quot;: 8350.494,
      &quot;length_stops&quot;: 0,
      &quot;successes&quot;: 9,
      &quot;successful_tasks_s_completed_requests&quot;: 0.3437831678061117,
      &quot;tokens_s_completed_requests&quot;: 41.86515021283316,
      &quot;valid_terminal_output&quot;: 9,
      &quot;wilson95&quot;: [
        0.331785563988119,
        0.7690134759450765
      ]
    }
  }
}</pre></details></td></tr></tbody></table></div>

Development evidence, not an official benchmark or unseen validation set. These tasks were previously used for Nexus A/B/C tuning. No automatic exclusion from small score differences. Wilson intervals, native sampling, hashes, missing answers and audit references are in **Details**. Native templates and settings remain unchanged. Reserved8+8 validation status and evidence are recorded separately in the methods archive.

¹ Completion tokens / completed-request wall time, including reasoning when reported; not pure decode speed. ² Counter-bracketed lower bound; upper bounds remain in Details. Failed completed requests count toward costs. Historical Nexus A timings used an interleaved ABC schedule. Missing values stay unknown.


<details><summary>Other local artifacts: technical disposition</summary><ul><li><strong>Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf</strong> — DEFERRED: No new GPU screen:851 common payloads are bound by verified assembly; the R502 no-speculation engine already skips15 MTP tensors and caches only64 trunk layers. Separate base-file performance is NOT MEASURED. Reopen for changed loader/weights/MTP loading or material cold-start/storage hypothesis. <a href="../audits/audit-a6d64223c65f59269a00/">CPU review</a> · GPU screen: NOT MEASURED</li></ul></details>

<details><summary>Conservative qualification shortlist & next decisions</summary><ul><li><strong>P0 · OmniCoder-9B, Qwen3.5-9B, Gemma4-12B, MiMo-9B, LFM2.5-8B</strong>: Reuse existing complete native coding/tools results; no repeated GPU benchmarks.</li><li><strong>P0 · Qwen3.8-27B</strong>: Reuse complete native coding; inspect the incomplete tools campaign and its shared budget before any justified full200 qualification. No silent reset.</li><li><strong>P1 · Qwen3.6-27B, Bonsai2-27B</strong>: Assess missing matched native full benchmarks after screening. Preserve partials and historical valid Bonsai coding under its original profile; no transfer of scores between configurations.</li><li><strong>P1 · Nexus-9B, Slopus-9B, Opus Distill-9B, Ornith-1.5-9B</strong>: Retain. Existing full OFF/T0 profiles are separate valid configurations; native ON screening does not inherit their scores. Reuse them; fill native-profile gaps only with a concrete practical reason.</li><li><strong>DIAGNOSIS · LFM2.5-24B</strong>: Retain coding/specialist candidacy. Existing complete native tools6/200 is a profile-specific negative result and must not be blindly repeated. Investigate only a concrete configuration hypothesis after qualification decisions.</li></ul><p>Terminal-Bench2.1 remains NOT MEASURED and technically unadmitted. Mock tools are not agent-trajectory qualification.</p></details>

[Reserved independent validation: status and evidence](pipeline-methods.md#independent-native-profile-validation).
