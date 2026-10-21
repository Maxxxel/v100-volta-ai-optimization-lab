# Public audit excerpt

Original SHA256: `307acb7d054d5e3795cc93dffa76411d464ff02920892bfb042490623adc63ca`

Original file: `AUDIT.json`; 7894 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "STOP_QUANT_ORIGINAL12_QUALITY_LOSS",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Published Q8_0 versus original Q6, same tokenizer/shapes/engine/template/requests; no claimed common upstream BF16 payload identity or Q05 ablation",
    "Original12 exploratory quality-only gate; no native speed/energy efficiency, BFCL/coding/agent or final model-superiority claim",
    "No automatic A0/champion update or production deployment; temperature telemetry only; peak from observed screen"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 16,
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
        "format_pass": true,
        "raw_preserved": true,
        "semantic_pass": true
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
    }
  ],
  "peak_process_vram_mib": 8944
}
```
