# Public audit excerpt

Original SHA256: `0c0dea8f708aba6bb0df258411913bf3752b237cace1b780a979a4cae291c336`

Original file: `AUDIT.json`; 56937 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Evaluate fresh A/B against the preregistered quality, latency and energy gates before promotion.",
  "scope": "Fresh sequential A/B on identical exposed development32. One1200s clock includes both startups/warmups. No official benchmark, holdout or Champion."
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
          "complete_request_s": 47.446383002,
          "group_window_s": 47.446383002,
          "groups": 16,
          "included_between_request_setup_s": 0.0,
          "lower_j": 11535.94,
          "max_query_duration_s": 0.186473137,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 16,
          "upper_j": 13359.156
        },
        "GPU_j_per_success_lower": 823.9957142857144,
        "GPU_j_per_success_upper": 954.2254285714287,
        "completed": 16,
        "completed_request_wall_s": 47.446383002,
        "completion_tokens": 3587,
        "final_text_present": 16,
        "length_stops": 0,
        "successes": 14,
        "successful_tasks_s_completed_requests": 0.29506991079614775,
        "tokens_s_completed_requests": 75.601126430413
      }
    },
    "B": {
      "coding": {
        "GPU_counter": {
          "complete_request_s": 31.985729577,
          "group_window_s": 31.985729577,
          "groups": 16,
          "included_between_request_setup_s": 0.0,
          "lower_j": 7638.617,
          "max_query_duration_s": 0.186473137,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 16,
          "upper_j": 9377.369
        },
        "GPU_j_per_success_lower": 545.6155,
        "GPU_j_per_success_upper": 669.8120714285715,
        "completed": 16,
        "completed_request_wall_s": 31.985729577,
        "completion_tokens": 3791,
        "final_text_present": 16,
        "length_stops": 0,
        "successes": 14,
        "successful_tasks_s_completed_requests": 0.4376951904847901,
        "tokens_s_completed_requests": 118.52160479484566
      }
    }
  },
  "model_starts": 2,
  "peak_device_vram_mib": 9324.5
}
```

</details>
