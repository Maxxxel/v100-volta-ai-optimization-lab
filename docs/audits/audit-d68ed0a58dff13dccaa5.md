# Public audit excerpt

Original SHA256: `d68ed0a58dff13dccaa58a2c9c924346795b92ccf31613d8c28a0a0cb736da79`

Original file: `AUDIT.json`; 10903 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Q03_ATTENTION_Q8_QA12_MEMORY_SCREEN_PASSED_NOT_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Only32fullattentionprojectionmatrices copiedfromQ8 donor;allother395tensorpayloads originalQ6byteidentical",
    "No output.weight/recurrent upgrade, no combinedpreset; sourceoriginals/tokenizer/shapes/177F32anchors verified",
    "QA12firststage only;full12 no-grade-loss+<=8GiB admits deeper practicalquality screen,notchampion",
    "No lossless weights or commonBF16derivation guarantee; no speedgainclaim"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": true,
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 12,
  "model_starts": 1,
  "peak_device_vram_mib": 7464.5,
  "quality": {
    "candidate_format": 8,
    "candidate_semantic": 9,
    "reference_format_on_observed": 8,
    "reference_semantic_on_observed": 9
  }
}
```

</details>
