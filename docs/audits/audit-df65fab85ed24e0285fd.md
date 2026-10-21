# Public audit excerpt

Original SHA256: `df65fab85ed24e0285fd21c9bdc901b479130319db0aa50b817e414b21689406`

Original file: `research-metadata.json`; 8159 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "IQ2_XS_QA12_QUALITY_REGRESSION_STOP",
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
  "actual_generation_requests": 5,
  "model_starts": 1,
  "peak_device_vram_mib": 3938.5,
  "quality": {
    "candidate_format": 2,
    "candidate_semantic": 3,
    "reference_format_on_observed": 3,
    "reference_semantic_on_observed": 3
  }
}
```
