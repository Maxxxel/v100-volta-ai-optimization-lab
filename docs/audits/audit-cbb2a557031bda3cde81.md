# Public audit excerpt

Original SHA256: `cbb2a557031bda3cde81491d757806835345b15f0aa0bf5a29d77558717f48f1`

Original file: `AUDIT.json`; 2177 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "Q2_K_QA12_QUALITY_REGRESSION_STOP",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Original12 development tasks, no HumanEvalPlus/agent/tool winner",
    "Quantizer same pinned repository/identical shape/tokenizer/F32 anchors; identical upstream BF16 derivation not cryptographically established",
    "No claimed lossless output IDs across weight quantization",
    "No general decode/coding speed claim from a QA screen"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 1,
  "model_starts": 1,
  "peak_device_vram_mib": 4346.5,
  "quality": {
    "candidate_format": 0,
    "candidate_semantic": 0,
    "reference_format_on_observed": 1,
    "reference_semantic_on_observed": 1
  }
}
```
