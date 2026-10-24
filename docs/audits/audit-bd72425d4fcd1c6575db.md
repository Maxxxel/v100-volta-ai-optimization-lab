# Public audit excerpt

Original SHA256: `bd72425d4fcd1c6575db7eeba95220a7a9e2f7dba2763f07b0ff2f310d85d103`

Original file: `AUDIT.json`; 11106 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "FULL164_COLLECTED_AND_SCORED_NO_CHAMPION",
  "evidence_class": "LOKAL_GEMESSEN",
  "scope": "Actual same-session Qwen3.8 27B GSQ/RCO IQ3_S native configuration, no parameter changes, output reuse, QA pre-exclusion, causal optimization or Champion claim. Missing tasks are not zero."
}
```

## Selected aggregate measurements

```json
{
  "model_starts": 1,
  "peak_device_vram_mib": 12450.5,
  "scopes": {
    "standard_full164": {
      "solved": 149,
      "tasks": 164,
      "wall_s": 1109.486180492
    }
  }
}
```
