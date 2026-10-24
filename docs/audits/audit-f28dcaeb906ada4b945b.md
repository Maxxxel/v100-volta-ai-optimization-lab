# Public audit excerpt

Original SHA256: `f28dcaeb906ada4b945bc3119e9b899ad457d918608d8e4cb7c360d896f38e91`

Original file: `AUDIT.json`; 13053 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MTP_MICROBATCH_CONTROL_DRIFT_OR_FRESH_PAIR_FAILED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "One timely matchingMTP512control at original300W against existingR184microbatch2048B and storedR172MTP512. Exact same native28request work/outputs; no newB or A0calibration.",
    "OriginalR184stored-reference512energy failure remains unchanged. Frozen5%control drift and all fresh-pair performance/energy bounds are mandatory; no threshold relaxation.",
    "Any confirmed synthetic tradeoff still needs practical quality/cost qualification against functionalC. No additive gain, universal output-identity/model-superiority claim or production deployment."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 28,
  "peak_process_vram_mib": 8758
}
```

</details>
