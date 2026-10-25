# Public audit excerpt

Original SHA256: `e6e53264a8e713dd6efe4f8f61e131ada059a53722fd4e556a50271ed4631dd7`

Original file: `research-metadata.json`; 4705 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "Five previously used development tasks, paired across three harness arms. All tools simulated; fixed arm order. Not Terminal-Bench, unseen validation, a population ranking or a Champion qualification."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "arms": [
    {
      "GPU_counter": {
        "complete_request_s": 68.799046771,
        "group_window_s": 68.799046771,
        "groups": 1,
        "included_between_request_setup_s": 0.0,
        "lower_j": 17999.429,
        "max_query_duration_s": 0.074714971,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 1,
        "upper_j": 18105.77
      },
      "arm_wall_s": 68.799046771,
      "complete": true,
      "completed_cases": 5,
      "completed_request_wall_s": 67.94651978899999,
      "completion_tokens_all_roles": 2775,
      "generation_requests": 36,
      "gpu_j_per_success_lower": 5999.809666666667,
      "gpu_j_per_success_upper": 6035.256666666667,
      "peak_sampled_device_vram_mib": 7356.5,
      "planned_cases": 5,
      "policy_gate_passes": 4,
      "solved": 3,
      "successful_tasks_per_s": 0.043605255316772104,
      "task_scope_passes": 5,
      "technical_preflight_cases": 0,
      "tokens_s_completed_requests": 40.84094385727833
    },
    {
      "GPU_counter": {
        "complete_request_s": 60.292242202,
        "group_window_s": 60.292242202,
        "groups": 1,
        "included_between_request_setup_s": 0.0,
        "lower_j": 16154.429,
        "max_query_duration_s": 0.074714971,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 1,
        "upper_j": 16280.849
      },
      "arm_wall_s": 60.292242202,
      "complete": true,
      "completed_cases": 5,
      "completed_request_wall_s": 59.837570834,
      "completion_tokens_all_roles": 2997,
      "generation_requests": 27,
      "gpu_j_per_success_lower": 5384.809666666667,
      "gpu_j_per_success_upper": 5426.949666666666,
      "peak_sampled_device_vram_mib": 7356.5,
      "planned_cases": 5,
      "policy_gate_passes": 4,
      "solved": 3,
      "successful_tasks_per_s": 0.049757645269667625,
      "task_scope_passes": 5,
      "technical_preflight_cases": 0,
      "tokens_s_completed_requests": 50.085589341756666
    },
    {
      "GPU_counter": {
        "complete_request_s": 84.978298829,
        "group_window_s": 84.978298829,
        "groups": 1,
        "included_between_request_setup_s": 0.0,
        "lower_j": 23356.156,
        "max_query_duration_s": 0.074714971,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 1,
        "upper_j": 23464.266
      },
      "arm_wall_s": 84.978298829,
      "complete": true,
      "completed_cases": 5,
      "completed_request_wall_s": 84.442233702,
      "completion_tokens_all_roles": 4440,
      "generation_requests": 33,
      "gpu_j_per_success_lower": 5839.039,
      "gpu_j_per_success_upper": 5866.0665,
      "peak_sampled_device_vram_mib": 7356.5,
      "planned_cases": 5,
      "policy_gate_passes": 4,
      "solved": 4,
      "successful_tasks_per_s": 0.047070841086723963,
      "task_scope_passes": 5,
      "technical_preflight_cases": 0,
      "tokens_s_completed_requests": 52.58032391313731
    }
  ],
  "model_requests": 0
}
```

</details>
