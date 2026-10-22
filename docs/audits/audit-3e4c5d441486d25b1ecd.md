# Public audit excerpt

Original SHA256: `3e4c5d441486d25b1ecd73f77476a064c92c49440a55d060381b3b6a955b6a9a`

Original file: `AUDIT.json`; 10207 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "R192_A04_SIMULATED_GATE_SCOPE_PASSED_NOT_DEPLOYED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Deterministic deny-by-default simulated harness gate only, no production tooling or enforcement deployment",
    "No causal inference acceleration: identical GPU proposals are evaluated twice logically, GPU executed once",
    "Gate preserves only exact fixture-authorized calls; false positives outside these fixtures not established",
    "Unparsed/malformed native envelope is blocked by default. Recovery/error messaging and multistep agent quality unqualified",
    "Read-only synthetic HA/PVE case IDs; no actual privileged operations"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 24,
  "source_cases": 24
}
```
