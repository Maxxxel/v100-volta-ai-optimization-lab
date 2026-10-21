# Public audit excerpt

Original SHA256: `4e5c4e18df8e19bfef6af51dd2eb65c24960292285d402b9fe9896a35f1d6ad1`

Original file: `AUDIT.json`; 1374 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Synthetic HA/PVE read-only tools, no real external execution",
    "Single GPU model start, AB/BA order; not independent startup stability or speed qualification",
    "No model/kernel/weight change. Only streaming transport/parser compatibility measured, not throughput speed gain"
  ],
  "scope": "16 fresh native tool routing cases: OpenAI buffered JSON vs SSE, one server and same tokenized prompts"
}
```

## Selected aggregate measurements

NOT MEASURED / not included in the approved public schema.
