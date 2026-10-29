# Public audit excerpt

Original SHA256: `9ebc7de1ef58210b7e27d6b7fca5c8d48b3011362677395c92a77c1f2aaa9d07`

Original file: `research-metadata.json`; 2106 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "candidate_cache": {
      "cache_hit_turns": 122,
      "cached_tokens": 214113,
      "completion_tokens": 16777,
      "turns": 155
    },
    "candidate_case_wall_s": 255.4077487,
    "candidate_gpu_j_lower": 69685.207,
    "candidate_gpu_j_upper": 69786.33,
    "candidate_peak_vram_mib": 7356.5,
    "case_wall_reduction_percent": 20.176389965779627,
    "quality": {
      "policy_gate_pass": {
        "candidate_passed": 28,
        "gained": 0,
        "lost": 1,
        "reference_passed": 29
      },
      "task_scope_pass": {
        "candidate_passed": 33,
        "gained": 0,
        "lost": 0,
        "reference_passed": 33
      },
      "task_success": {
        "candidate_passed": 25,
        "gained": 0,
        "lost": 0,
        "reference_passed": 25
      }
    },
    "reference_cache": {
      "cache_hit_turns": 0,
      "cached_tokens": 0,
      "completion_tokens": 16392,
      "turns": 153
    },
    "reference_case_wall_s": 319.96516894,
    "reference_gpu_j_lower": 87162.708,
    "reference_gpu_j_upper": 87236.676,
    "reference_peak_vram_mib": 7356.5,
    "tasks": 33
  },
  "model_requests": 0
}
```

</details>
