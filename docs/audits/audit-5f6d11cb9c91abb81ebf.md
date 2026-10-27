# Public audit excerpt

Original SHA256: `5f6d11cb9c91abb81ebf0bf74f0e490aef96e856667718033b83c888df1969f0`

Original file: `AUDIT.json`; 34269 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Evaluate unchanged R594 candidate against fresh contemporaneous A; preserve case-level quality and safety gates. No automatic adoption or Champion.",
  "scope": "16 newly frozen task instances,32 balanced A/B requests; one resident model and shared1200s TASK. Per-arm full TASK duration NOT MEASURED. Not official or population-equivalence evidence."
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
          "complete_request_s": 18.123520126,
          "group_window_s": 18.124775901,
          "groups": 5,
          "included_between_request_setup_s": 0.001255775,
          "lower_j": 4519.558,
          "max_query_duration_s": 0.015909857,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 8,
          "upper_j": 5122.913
        },
        "GPU_j_per_success_lower": 564.94475,
        "GPU_j_per_success_upper": 640.364125,
        "completed": 8,
        "completed_request_wall_s": 18.123520126,
        "completion_tokens": 1356,
        "final_text_present": 8,
        "length_stops": 0,
        "successes": 8,
        "successful_tasks_s_completed_requests": 0.44141535112283187,
        "tokens_s_completed_requests": 74.81990201532001
      }
    },
    "B": {
      "coding": {
        "GPU_counter": {
          "complete_request_s": 16.438231608,
          "group_window_s": 16.439996063,
          "groups": 4,
          "included_between_request_setup_s": 0.001764455,
          "lower_j": 4056.72,
          "max_query_duration_s": 0.015909857,
          "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
          "tasks": 8,
          "upper_j": 4540.809
        },
        "GPU_j_per_success_lower": 579.5314285714286,
        "GPU_j_per_success_upper": 648.687,
        "completed": 8,
        "completed_request_wall_s": 16.438231608,
        "completion_tokens": 1227,
        "final_text_present": 8,
        "length_stops": 0,
        "successes": 7,
        "successful_tasks_s_completed_requests": 0.42583655997359887,
        "tokens_s_completed_requests": 74.64306558394368
      }
    }
  },
  "model_starts": 1,
  "peak_device_vram_mib": 7680.5
}
```

</details>
