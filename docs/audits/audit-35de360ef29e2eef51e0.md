# Public audit excerpt

Original SHA256: `35de360ef29e2eef51e019ccf8cfbf79608a888bcc00bfe20cb6b73efd76f13c`

Original file: `AUDIT.json`; 7418 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "TESTED_NEGATIVE_QUALITY_REGRESSION_EARLY_STOP",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Screen stopped at the first B irrelevance tool call; only the first 51 paired tasks were generated.",
    "No model-response BFCL AST score, full-suite quality score, tasks-per-success, or joules-per-success is available.",
    "Partial request timings, prompt tokens and GPU energy are descriptive only and are not a performance result.",
    "No independent confirmation, Champion promotion, or deployment is warranted."
  ]
}
```

## Selected aggregate measurements

```json
{
  "model_starts": 1
}
```
