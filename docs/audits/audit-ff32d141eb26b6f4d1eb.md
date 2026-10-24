# Public audit excerpt

Original SHA256: `ff32d141eb26b6f4d1ebb3cbc94ff906b85dba3b0e43657d9dc4e46822710c42`

Original file: `AUDIT.json`; 11832 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "GEMMA4_MBPP32_CODING_PROFILE_PROMISING_NEEDS_CONFIRMATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "32/224 fixed original-test MBPP screen, not full378 or training-exclusion proof",
    "Gemma QATQ40 fast T1/P95/K64 noMTP/cache coding profile; not an isolated model architecture/quantization effect",
    "Known native-tool/policy disqualifications retained; no allround/agent/production claim; no lossless target-token assertion",
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
  "gpu_energy_j": 30729.307379933496,
  "gpu_j_per_success": 1336.0568426058041,
  "model_starts": 1,
  "peak_device_vram_mib": 8118.5,
  "solved": 23,
  "tasks": 32,
  "wall_s": 128.351662529
}
```

</details>
