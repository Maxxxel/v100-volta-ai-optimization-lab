# Public audit excerpt

Original SHA256: `42ee9099f72f7b3df9cd8a6297b5f6f3028b1193c8c8eeaf5ebda52d9c78c49c`

Original file: `AUDIT.json`; 56755 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Assess the fixed R592 prompt variant with contemporaneous controls and preregistered quality/latency/energy gates. No adoption without new unseen confirmation.",
  "scope": "Fresh balanced AB/BA for32 exposed tasks,64 requests, one unchanged resident model and one1200s TASK clock. Startup/warmup separate. Not official, holdout, independent population qualification or Champion."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "arms": {
    "A": {
      "coding": {
        "GPU_counter": {
          "complete_request_s": 47.484726995,
          "group_window_s": 47.484726995,
          "groups": 16,
          "included_between_request_setup_s": 0.0,
          "lower_j": 11868.3,
          "max_query_duration_s": 0.054395889,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 16,
          "upper_j": 13803.835
        },
        "GPU_j_per_success_lower": 847.7357142857143,
        "GPU_j_per_success_upper": 985.9882142857142,
        "completed": 16,
        "completed_request_wall_s": 47.484726995,
        "completion_tokens": 3587,
        "final_text_present": 16,
        "length_stops": 0,
        "successes": 14,
        "successful_tasks_s_completed_requests": 0.29483164137121726,
        "tokens_s_completed_requests": 75.54007839989688
      }
    },
    "B": {
      "coding": {
        "GPU_counter": {
          "complete_request_s": 43.519155076,
          "group_window_s": 43.519155076,
          "groups": 16,
          "included_between_request_setup_s": 0.0,
          "lower_j": 10439.895,
          "max_query_duration_s": 0.054395889,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 16,
          "upper_j": 12420.282
        },
        "GPU_j_per_success_lower": 745.7067857142857,
        "GPU_j_per_success_upper": 887.1629999999999,
        "completed": 16,
        "completed_request_wall_s": 43.519155076,
        "completion_tokens": 3279,
        "final_text_present": 16,
        "length_stops": 0,
        "successes": 14,
        "successful_tasks_s_completed_requests": 0.3216974221018537,
        "tokens_s_completed_requests": 75.34613193371274
      }
    }
  },
  "model_starts": 1,
  "peak_device_vram_mib": 7680.5
}
```

</details>
