# Public audit excerpt

Original SHA256: `fe9d4937f9a1adf5117683c1d291bc9164a14188dfcaab9801df4c10c6dcce1f`

Original file: `AUDIT.json`; 12909 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "NATIVE_TOOL_OUTPUT_INJECTION_GATE_SCOPE_PASSED_NOT_DEPLOYED",
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
  "actual_generation_requests": 24
}
```
