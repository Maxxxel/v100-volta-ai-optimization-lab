# Public audit excerpt

Original SHA256: `baefb52b9ddfc2ae03aff56c579fd5c01126cbae964783d1dd2db17be9d89f5e`

Original file: `AUDIT.json`; 7875 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

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

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 15,
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
    }
  ],
  "peak_process_vram_mib": 6392
}
```

</details>
