# Public audit excerpt

Original SHA256: `c7ca0d0405f4d0cdcb9fd8090a3a17bde06a11e58c7f9ceb06c85956fde1a12a`

Original file: `AUDIT.json`; 5665 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "PROMISING_EXTERNAL_DRAFT_NATIVE_SCREEN_NEEDS_FUNCTIONAL_QUALIFICATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Published base-Qwen MTP-only head with original OmniCoder2 target; compatible geometry/tokenizer, not an OmniCoder-trained head; separate file and one GPU server",
    "Negative prefix is not a full quality/performance score; no universal lossless or model-superiority claim",
    "Observed target token/content mismatch disqualifies this configuration without isolating the numerical/root cause",
    "Synthetic decode survivor still needs fresh controls and actual coding/tool/agent qualification",
    "GPU request energy excludes CPU/system/load/idle; A0 energy absent, only C energy comparison available; temperature telemetry only"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 28,
  "peak_process_vram_mib": 8758
}
```
