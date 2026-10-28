# gemma4_12b_qat · cfg-fd11ebeae231

[Back to configuration comparison](../configuration-comparison.md)

Profile ID: `cfg-fd11ebeae2318f2ab6865462baec92c3936abc9e9a31cab64a1813cfbcc90cd8`. Null means **NOT MEASURED**, never a default setting. Hardware evidence and costs are attached to each measured run; current host settings are not retrospectively assigned to historical runs.

## Model and weights

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "architecture": null,
  "artifact_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b",
  "family_id": "gemma4_12b_qat",
  "hf_repository": null,
  "hf_revision": null,
  "name": "gemma4_12b_qat",
  "quantization": "NOT MEASURED",
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
  "binary_sha256": null,
  "build_id": null,
  "cuda_version": null,
  "driver_version": null,
  "executed_kernel_backend_path": null,
  "fork_repository": null,
  "ggml_backend_version": null,
  "git_commit": null,
  "kernel_library_file": null,
  "kernel_library_sha256": null,
  "name": null,
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
    "k": null,
    "v": null
  },
  "cuda_graphs": {
    "actual_capture_replay": null,
    "disable_knob": null,
    "optimization_knob": null
  },
  "draft_head_or_model": null,
  "draft_parameters": {},
  "draft_sha256": null,
  "flash_attention_requested": null,
  "other_explicit_knobs": {},
  "prefix_reuse": null,
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
  "CPU_threads": null,
  "GPU_offload": null,
  "RAM_budget": null,
  "VRAM_budget_mib": null,
  "batch": null,
  "chat_template_sha256": null,
  "context": null,
  "execution_deadline_s": null,
  "max_output": null,
  "microbatch": null,
  "native_template_controls": null,
  "power_limit_w": null,
  "sampling": null,
  "thinking_reasoning_requested": null,
  "tokenizer_identity": null
}
```

</details>

## Ordered startup parameters

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "argv": [],
  "environment": {},
  "exact_private_launch_sha256": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
  "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
  "redacted_argument_positions": []
}
```

</details>

## Results and original audits

| Experiment | Benchmark / scope | Success | Wall s | GPU J / success | Peak VRAM MiB | Original audits |
| --- | --- | --- | --- | --- | --- | --- |

Separate benchmark qualification audits:

| Experiment / arm | Execution evidence | Scientific decision | Original audit |
| --- | --- | --- | --- |
| R610 / 0 | INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED | HISTORICAL_CODING_REGRESSION_NO_PROMOTION | [audit-2c9b46a83abaf5980e1d](../audits/audit-2c9b46a83abaf5980e1d.md) |

## Immutable full profile and measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "attempts": [
    {
      "arm_index": 0,
      "attempt_id": "attempt-4c31dcefe4bc08882ad92762110cd4c57f9f19f419078c509aebf06f523227f5",
      "audit_hash": "2c9b46a83abaf5980e1d05db6cbeff79b5f2c5aa14805365c09292c091ac9c65",
      "audit_id": "audit-2c9b46a83abaf5980e1d",
      "execution_status": "INFERENCE_OBSERVED_IN_EXPERIMENT; PER_ARM_QUALIFICATION_NOT_IMPLIED",
      "experiment_id": "R610",
      "lab_metrics": {
        "comparison": {
          "candidate_completion_tokens": 50219,
          "candidate_peak_vram_mib": 7986.5,
          "candidate_request_wall_s": 793.868207806,
          "candidate_successes": 151,
          "counter_gpu_j_per_success_lower_candidate": 1263.797105960265,
          "counter_gpu_j_per_success_lower_reference": 1203.1023653846155,
          "counter_gpu_j_per_success_upper_candidate": 1264.436298013245,
          "counter_gpu_j_per_success_upper_reference": 1203.6756602564103,
          "paired_gains": 0,
          "paired_losses": 5,
          "reference_completion_tokens": 51322,
          "reference_peak_vram_mib": 8118.5,
          "reference_request_wall_s": 754.737726997,
          "reference_successes": 156,
          "tasks": 164
        },
        "model_starts": 1,
        "peak_device_vram_mib": 7986.5,
        "scopes": {
          "standard_full164": {
            "solved": 151,
            "tasks": 164,
            "wall_s": 793.868207806
          }
        }
      },
      "model_family_id": "gemma4_12b_qat",
      "model_name": "gemma4_12b_qat",
      "official_eligible": false,
      "runtime_configuration_id": "cfg-fd11ebeae2318f2ab6865462baec92c3936abc9e9a31cab64a1813cfbcc90cd8",
      "scientific_status": "HISTORICAL_CODING_REGRESSION_NO_PROMOTION"
    }
  ],
  "profile": {
    "engine": {
      "binary_sha256": null,
      "build_id": null,
      "cuda_version": null,
      "driver_version": null,
      "executed_kernel_backend_path": null,
      "fork_repository": null,
      "ggml_backend_version": null,
      "git_commit": null,
      "kernel_library_file": null,
      "kernel_library_sha256": null,
      "name": null,
      "patches": null,
      "version": null
    },
    "evaluation_exposure": "Historical development suites were reused; no unseen holdout or absence of overfitting is claimed.",
    "incomplete_identity_run": "R610",
    "model": {
      "architecture": null,
      "artifact_sha256": "93567e57a8fe10b23569b9d9ec38cd005deedf71e29477c421a4b83f418a538b",
      "family_id": "gemma4_12b_qat",
      "hf_repository": null,
      "hf_revision": null,
      "name": "gemma4_12b_qat",
      "quantization": "NOT MEASURED",
      "tensor_precision_map": null,
      "variant": null,
      "weight_transformations": {
        "caution": "Artifact naming is not tensor-level transformation proof; unknown provenance is not original/base weights.",
        "description": "SOURCE_GGUF_NO_LOCAL_WEIGHT_TRANSFORM_ESTABLISHED",
        "proof": null
      }
    },
    "model_artifact_id": "artifact-040742056ca1122b9c7faa7d159ec5de3fcc1452014ced4455c6738e7aadb093",
    "optimizations": {
      "GDN_state_changes": null,
      "HBM_conversion_weight_cache_limit_mib": null,
      "KV_precision": {
        "k": null,
        "v": null
      },
      "cuda_graphs": {
        "actual_capture_replay": null,
        "disable_knob": null,
        "optimization_knob": null
      },
      "draft_head_or_model": null,
      "draft_parameters": {},
      "draft_sha256": null,
      "flash_attention_requested": null,
      "other_explicit_knobs": {},
      "prefix_reuse": null,
      "quantization_calibration": null,
      "speculation_type": null
    },
    "provenance_status": "KNOWN_FIELDS_ONLY; null means NOT MEASURED",
    "runtime": {
      "CPU_budget": null,
      "CPU_threads": null,
      "GPU_offload": null,
      "RAM_budget": null,
      "VRAM_budget_mib": null,
      "batch": null,
      "chat_template_sha256": null,
      "context": null,
      "execution_deadline_s": null,
      "max_output": null,
      "microbatch": null,
      "native_template_controls": null,
      "power_limit_w": null,
      "sampling": null,
      "thinking_reasoning_requested": null,
      "tokenizer_identity": null
    },
    "runtime_configuration_id": "cfg-fd11ebeae2318f2ab6865462baec92c3936abc9e9a31cab64a1813cfbcc90cd8",
    "schema_version": 1,
    "source_plan_sha256": "417cb712a1bc10a7536d26bf5b092907680c5d33f05901e31332ab966d84bee9",
    "start_parameters": {
      "argv": [],
      "environment": {},
      "exact_private_launch_sha256": "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
      "note": "All ordered start flags retained. Private paths/addresses are redacted; their exact originals remain bound by the private launch hash.",
      "redacted_argument_positions": []
    }
  },
  "runs": []
}
```

</details>
