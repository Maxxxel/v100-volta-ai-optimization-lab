# Public audit excerpt

Original SHA256: `9d1dc993ad4fb9fafdb8900cfe5b360139a325433aba63adb1d8cc2a84fc3e71`

Original file: `AUDIT.json`; 2492 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One B/A sequence; order and drift remain possible confounders.",
    "Previously exposed development tasks, not a quality equivalence or official qualification.",
    "GPU counter bounds exclude model startup, warmup, CPU energy and uncharacterized sensor error.",
    "No champion promotion."
  ],
  "scope": "Fresh sequential B/A on 32 exposed development tasks per arm; unbalanced order, no independent holdout or official benchmark."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "counter_gpu_j_per_success_lower_A": 588.8036071428571,
    "counter_gpu_j_per_success_lower_B": 488.39841379310343,
    "counter_gpu_j_per_success_upper_A": 592.1840357142856,
    "counter_gpu_j_per_success_upper_B": 491.88803448275866,
    "peak_device_vram_mib_A": 8128.5,
    "peak_device_vram_mib_B": 7988.5,
    "request_wall_reduction_percent": 8.910076972923896,
    "request_wall_s_A": 70.076521931,
    "request_wall_s_B": 63.832649887,
    "vram_reduction_mib": 140.0
  },
  "quality": {
    "candidate_successes": 29,
    "paired_regressions": 0,
    "reference_successes": 28,
    "tasks": 32
  }
}
```

</details>
