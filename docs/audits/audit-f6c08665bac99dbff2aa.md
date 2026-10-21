# Public audit excerpt

Original SHA256: `f6c08665bac99dbff2aa5cc30313b106981ecce7ca24e740f025e9dd36ec56de`

Original file: `AUDIT.json`; 65461 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "MATCHED_QWEN35_ORIGINAL_NATIVE_A0_CALIBRATED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One original-engine native A0 with cacheoff; no cache B measurement or speedup inferred",
    "Original12 controls only; no standardized coding/BFCL/German/agent superiority qualification",
    "3native repeats in one process, all observations retained; no independent-session CI",
    "GPUgeneration energy only; CPU/system/model load/idle excluded; temperature telemetry only",
    "Historical qwen35 timings not imported because engine/CUDA library hashes differ"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 34
}
```
