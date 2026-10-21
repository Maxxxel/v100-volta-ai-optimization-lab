# Public audit excerpt

Original SHA256: `2da70f9a1f9f3bf94e45e80377f5c80da0434637f2e50349227cf150e5a8f8f9`

Original file: `AUDIT.json`; 4445 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "SEMANTIC_DISK_RESTORE_QA12_SCREEN_PASSED_NOT_INDEPENDENTLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Two unchanged QA12 subcases only: multi-turn memory and native~2K context",
    "No MTP, cache conversion, multi-slot, or full scheduler state proof",
    "Roundtrip SHA equality alone is not numerical state correctness",
    "No speedup/champion from this bounded correctness screen"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 4,
  "model_starts": 1,
  "peak_device_vram_mib": 7354.5,
  "quality": {
    "cold_format": 1,
    "cold_semantic": 2,
    "warm_format": 1,
    "warm_semantic": 2
  }
}
```
