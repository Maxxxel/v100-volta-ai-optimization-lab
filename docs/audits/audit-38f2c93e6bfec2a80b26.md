# Public audit excerpt

Original SHA256: `38f2c93e6bfec2a80b264350b7f2d3c1909be3798c0ccdbee1306311050007a6`

Original file: `AUDIT.json`; 11490 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MBPP32_MTP_SCREEN_QUALITY_OR_PRACTICAL_GAIN_GATE_NOT_MET",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "32/224 fixed original-test MBPP screen, not full378 or training-exclusion proof",
    "Existing independently qualified R181 singleMTP profile transferred to new benchmark; no weight cache/new combination",
    "MTP target decisions may differ; exact task success is scored; no lossless claim",
    "GPU-board generation intervals only; loading/warmup/CPU judge excluded; positive screen not Champion qualification"
  ],
  "score_rule": "base_pass AND plus_pass"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 36,
  "gpu_energy_j": 13302.363587449874,
  "gpu_j_per_success": 700.124399339467,
  "model_starts": 1,
  "peak_device_vram_mib": 8998.5,
  "solved": 19,
  "tasks": 32,
  "wall_s": 49.011552342
}
```

</details>
