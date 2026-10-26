# Public audit excerpt

Original SHA256: `f9320dd9bec8420ae433a119cbf7aeb53a6b19cea679979a49bf4adc66a5e89a`

Original file: `research-metadata.json`; 7098 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "One fresh A then B comparison on previously exposed development data, with independently replayed judgments. Both model startups/warmups are conservatively charged to one1200s clock. Response latency and complete arm wall are distinct. Same observed task successes do not establish population noninferiority or identical token decisions. Reported generation-window throughput is not end-to-end task throughput. Counter brackets are not sensor confidence intervals; CPU/system energy excluded. No official score or Champion."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "arms": {
    "A": {
      "GPU_j_per_success_lower": 1247.1690344827587,
      "GPU_j_per_success_upper": 1250.56,
      "arm_including_setup_energy": {
        "complete_request_s": 153.454412156,
        "group_window_s": 153.454412156,
        "groups": 1,
        "included_between_request_setup_s": 0.0,
        "lower_j": 39952.984,
        "max_query_duration_s": 0.0408803,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 1,
        "upper_j": 39990.756
      },
      "arm_including_setup_s": 153.454412156,
      "coding_successes": 16,
      "completion_tokens": 3649,
      "peak_device_vram_mib": 12454.5,
      "reported_generation_window_tokens_s": 35.53711906136661,
      "successes": 29,
      "tasks": 32,
      "temperature_max_c": 72,
      "temperature_min_c": 37,
      "tool_successes": 13
    },
    "B": {
      "GPU_j_per_success_lower": 771.1170344827586,
      "GPU_j_per_success_upper": 774.0019310344828,
      "arm_including_setup_energy": {
        "complete_request_s": 106.032974775,
        "group_window_s": 106.032974775,
        "groups": 1,
        "included_between_request_setup_s": 0.0,
        "lower_j": 26030.027,
        "max_query_duration_s": 0.0408803,
        "scope": "Bounds from measured cumulative counter readings before/after each selected contiguous task group. No interpolation or extrapolation. Covers counter-query timing, not undocumented NVML sensor/calibration error. GPU only; includes setup inside each group, excludes unselected tasks, load, warmup and CPU/system energy.",
        "tasks": 1,
        "upper_j": 26080.448
      },
      "arm_including_setup_s": 106.032974775,
      "coding_successes": 16,
      "completion_tokens": 3698,
      "draft_accepted": 2629,
      "draft_generated": 3135,
      "peak_device_vram_mib": 13600.5,
      "reported_generation_window_tokens_s": 72.20654915743958,
      "successes": 29,
      "tasks": 32,
      "temperature_max_c": 74,
      "temperature_min_c": 59,
      "tool_successes": 13
    }
  },
  "comparison": {
    "additional_peak_device_vram_mib": 1146.0,
    "conservative_GPU_J_per_success_reduction_percent": 37.93929213809526
  },
  "model_starts": 2,
  "quality": {
    "paired_success_gains": 0,
    "paired_success_losses": 0,
    "paired_tasks": 32
  }
}
```

</details>
