# Public audit excerpt

Original SHA256: `33a9f3ecdd2c4c1b8a61c2c01739f7ff093bb8b077b67ebde3463d8c741c681b`

Original file: `AUDIT.json`; 10162 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "IQ3_S_QA12_QUALITY_REGRESSION_STOP",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Original12 development tasks, no HumanEvalPlus/agent/tool winner",
    "Pinned i1 repository, same published OmniCoder2 identity/shapes/tokenizer/F32 anchors; parent common BF16 derivation and imatrix causal effect not proven",
    "No claimed lossless output IDs across weight quantization",
    "No general decode/coding speed claim from a QA screen"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 11,
  "model_starts": 1,
  "peak_device_vram_mib": 4884.5,
  "quality": {
    "candidate_format": 7,
    "candidate_semantic": 7,
    "reference_format_on_observed": 7,
    "reference_semantic_on_observed": 8
  }
}
```
