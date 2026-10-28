# Public audit excerpt

Original SHA256: `2c9b46a83abaf5980e1d05db6cbeff79b5f2c5aa14805365c09292c091ac9c65`

Original file: `AUDIT.json`; 11095 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "FULL164_COLLECTED_AND_SCORED_NO_CHAMPION",
  "evidence_class": "LOKAL_GEMESSEN",
  "scope": "Actual same-session Gemma4 QAT Q4_0 native configuration, q8_0 key cache, no output reuse, QA pre-exclusion, causal speedup or Champion claim. Missing tasks are not zero."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "model_starts": 1,
  "peak_device_vram_mib": 7986.5,
  "scopes": {
    "standard_full164": {
      "solved": 151,
      "tasks": 164,
      "wall_s": 793.868207806
    }
  }
}
```

</details>
