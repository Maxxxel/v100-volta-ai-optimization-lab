# Public audit excerpt

Original SHA256: `56e975702f6bb38cac5a7c253b6c7bb51cd095e50b8e659c4a4e99c9e53c329c`

Original file: `AUDIT.json`; 3883 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "Q3_K_M_QA12_QUALITY_REGRESSION_STOP",
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
  "actual_generation_requests": 3,
  "model_starts": 1,
  "peak_device_vram_mib": 5116.5,
  "quality": {
    "candidate_format": 1,
    "candidate_semantic": 2,
    "reference_format_on_observed": 2,
    "reference_semantic_on_observed": 2
  }
}
```
