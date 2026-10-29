# Public audit excerpt

Original SHA256: `d2fd87d05ffc28bc2c87091ee75360f314c808a2521b0bc4ec60674186d27c68`

Original file: `research-metadata.json`; 2042 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Predeclared 5% latency and no-new-policy-loss gates failed; retain 512 baseline. No champion promotion."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "candidate_case_wall_s": 591.593561497,
    "candidate_completion_tokens": 17903,
    "candidate_generation_requests": 186,
    "candidate_gpu_j_lower": 147737.829,
    "candidate_gpu_j_upper": 147847.571,
    "candidate_peak_vram_mib": 8098.5,
    "case_wall_change_percent": 33.17939702089223,
    "quality": {
      "policy_gate_pass": {
        "candidate_passed": 29,
        "gained": 1,
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
        "candidate_passed": 17,
        "gained": 0,
        "lost": 0,
        "reference_passed": 17
      }
    },
    "reference_case_wall_s": 444.208019206,
    "reference_completion_tokens": 14198,
    "reference_generation_requests": 177,
    "reference_gpu_j_lower": 106777.937,
    "reference_gpu_j_upper": 106859.222,
    "reference_peak_vram_mib": 8254.5,
    "sampled_vram_saved_mib": 156.0,
    "tasks": 33
  },
  "model_requests": 0
}
```

</details>
