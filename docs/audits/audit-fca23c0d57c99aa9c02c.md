# Public audit excerpt

Original SHA256: `fca23c0d57c99aa9c02cfc8440604d3bdb44931a7ff6fc2d4d0a913936de3ead`

Original file: `research-metadata.json`; 2260 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "B-only33 exposed development cases. Stored original-request control is a separate historical measurement, not a fresh paired run or official benchmark. Failed tasks remain in costs; no population equivalence or adoption."
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
        "complete_request_s": 418.846482548,
        "group_window_s": 418.854808669,
        "groups": 1,
        "included_between_request_setup_s": 0.008326121,
        "lower_j": 113599.527,
        "max_query_duration_s": 0.181676711,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 33,
        "upper_j": 113738.925
      },
      "GPU_j_per_success_lower": 4369.212576923077,
      "GPU_j_per_success_upper": 4374.574038461538,
      "case_wall_s": 418.846482548,
      "complete": true,
      "completed_cases": 33,
      "completion_tokens_reported": 23524,
      "invalid_actions": 0,
      "model_calls_attempted": 155,
      "peak_sampled_device_vram_mib": 7680.5,
      "planned_cases": 33,
      "policy_gate_passes": 27,
      "policy_violations": 6,
      "rejected_calls": 6,
      "solved": 26,
      "successful_tasks_per_s": 0.062075249723555666,
      "tool_calls": 122,
      "total_tokens_reported": 302821,
      "transform_cpu_s": 0.181019642,
      "transform_wall_s": 4.586701679
    }
  ],
  "model_requests": 0
}
```

</details>
