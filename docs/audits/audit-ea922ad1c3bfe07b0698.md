# Public audit excerpt

Original SHA256: `ea922ad1c3bfe07b0698d73e480f8a47efe90b797c94c26946e1fc4a50b5197e`

Original file: `AUDIT.json`; 89591 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "KEEP_VALID_WARP1_2_4_NEGATIVES_NO_RETEST_NO_DIRECT_WARP2_DECODE_GAIN",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "Read-only review of preserved realGPU evidence, not new execution or independent quality regrading.",
    "72 unique warp2 cases per process repeated across4processes, not288 unique cases; warp1/4 use16-case suite.",
    "Warp2 Q6 n1 decode uses2warps in both arms. Real changes n2/n4 and numerical IQ3 paths; no direct decode-warp speedup.",
    "C09 bounded trace does not exhaustively profile all shapes/instructions. HBM03 adds shape-specific geometry.",
    "Original QUALIFIED refers to protocol/configuration, not practical winner; quality losses remain binding.",
    "Distinct supported instruction/layout/occupancy hypothesis required; no universal exhaustion claim."
  ],
  "measurement_type": "REVIEW_EXISTING_MMVQ_WARP_EVIDENCE"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": false,
  "new_GPU_runs": 0
}
```

</details>
