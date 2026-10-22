# Public audit excerpt

Original SHA256: `0f4239ca198c9619efaaf678fb0ff52e30866f33eb2d336128a4322ebcda3c4b`

Original file: `INDEPENDENT_REVIEW.json`; 4476 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "PREREGISTERED_EXACT_ENVELOPE_PARITY_NOT_MET; STATE_SERIALIZATION_OBSERVER_PASSED; TASK_QUALITY_AND_CAUSAL_ROLLBACK_UNRESOLVED",
  "evidence_class": "LOKAL GEMESSEN",
  "interpretation": "The preregistered exact-response parity gate failed. Observed differences do not establish incorrect tool behavior: the two history tool calls use different replacement-span widths but target the same return-line change, and the critical tool call is identical. This experiment did not execute or score the edits. It therefore does not prove a quality regression, lossless speculative decoding, or a GDN rollback defect.",
  "scope": "Replayed immutable A0/MTP envelopes and raw hash manifest; no prompt or model-output payload copied into this review."
}
```

## Selected aggregate measurements

```json
{
  "comparison": {
    "critical_envelope_equal": false,
    "critical_tool_calls_equal": true,
    "history_cases": 21,
    "history_differences": [
      {
        "ordinal_zero_based": 3,
        "text_equal": false,
        "tool_calls_equal": false
      },
      {
        "ordinal_zero_based": 12,
        "text_equal": false,
        "tool_calls_equal": false
      }
    ],
    "history_envelopes_equal": false
  }
}
```
