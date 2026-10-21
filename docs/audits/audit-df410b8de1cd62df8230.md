# Public audit excerpt

Original SHA256: `df410b8de1cd62df8230e0b77ac800545a6954a745224a5ac24918637ca60a8f`

Original file: `AUDIT.json`; 7135 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "STOP_QUANT_ORIGINAL12_QUALITY_LOSS",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Same published Omni family/tokenizer/shapes; only weights Q6 to Q5_K_M, original JSON requests/engine/template/runtime unchanged",
    "Changed output tokens are expected for changed quantized weights; no lossless/numerical-equivalence or common upstream BF16 claim",
    "Original12 exploratory pilot only; no full coding/tool/agent qualification or final model ranking",
    "Stored A0 lacks energy; extra GPU-energy comparison uses two existing uncached R90 controls, never fabricated A0 energy",
    "Negative prefix is not a full12 or full native score; no automatic new baseline/champion/deployment",
    "Q05 causal outlier-retention ablation not exercised; GPU request energy excludes CPU/system/load/idle"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 11,
  "original12": [
    {
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": false
      }
    },
    {
      "grades": {
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    },
    {
      "grades": {
        "format_pass": false,
        "raw_preserved": true,
        "semantic_pass": true
      }
    }
  ],
  "peak_process_vram_mib": 6392
}
```
