# Public audit excerpt

Original SHA256: `42d5d51be97f1a10cc296bfca08a113ce846dbce2be595a6fd75d2b6ddb8060a`

Original file: `AUDIT.json`; 5600 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

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

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 0,
  "model_starts": 1
}
```

</details>
