# Public audit excerpt

Original SHA256: `645b2faacd2d0de74f444b199b2b4fc1beccb5e7cee705fceb3b23c8d702b255`

Original file: `AUDIT.json`; 27121 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "E02_NATIVE_AUTO_TOOL_PILOT_DIFFERENCE_OR_TECHNICAL_STOP",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Five frozen BFCL schema cases, not full BFCL quality qualification",
    "Both sides auto tool selection; unsupported required/parallelfalse/templatekwargs excluded. Direct A is an explicit new native-auto control, not stored required-tool A0",
    "Same external buffered protocol; internal Go backend may stream",
    "Prompt order differs by frontend as part of E02 treatment; same-token speedup disallowed; sampler mismatch still prevents generation; no original12 rerun",
    "Single five-pair pilot cannot qualify a winner; >=3% needs independent confirmation"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 10,
  "model_starts": 1
}
```
