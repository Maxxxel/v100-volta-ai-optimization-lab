# Public audit excerpt

Original SHA256: `0096de0ed9992eeb0f2a7fd9a6189f2eaa709ff98e90538e6ae1827cfd4cc012`

Original file: `AUDIT.json`; 11548 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "TEMPERATURE02_TOOL_PILOT_NO_PRACTICAL_QUALITY_GAIN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "20/100frozen toolcases,notfullBFCL or full-axis rejection",
    "One sampling seed1001;independent seeds/tasks required for quality superiority",
    "No realtools/generatedcode execution",
    "GPU inference energy only, startup/warmup/CPU/hostenergy excluded",
    "B-only quality pilot has no repeated startup warmup; archived wall/energy comparison is screening-only and cannot qualify speed."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 20,
  "gpu_energy_j_approx": 7052.593639719805,
  "gpu_j_per_success": 391.8107577622114,
  "model_starts": 1,
  "peak_device_vram_mib": 7356.5,
  "solved": 18,
  "wall_s": 26.683560394
}
```

</details>
