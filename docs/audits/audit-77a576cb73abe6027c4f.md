# Public audit excerpt

Original SHA256: `77a576cb73abe6027c4f93b96182d501f67e35744d9dd77db82701f21baf94c4`

Original file: `AUDIT.json`; 5912 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "SLOT0_ERASE_DOES_NOT_REMOVE_REPRODUCED_BAD_ENVELOPE",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Single knowncritical causalcomponent,not full18task success or unconditional statecorrectness",
    "Slot-save-path is necessary API enabling;prefix21 parity checks preserve observable pre-treatment execution",
    "No extra coldprobe, earlier reset or new output flags",
    "No specific GDN/attention/CUDA-graph root cause established by an erase effect",
    "A matching valid envelope is not global lossless/quality/performance qualification"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 26,
  "actual_history_requests": 21,
  "critical_matches_previous_bad": true,
  "critical_matches_previous_valid": false,
  "critical_output_tokens": 235,
  "critical_prompt_tokens": 2126,
  "model_starts": 1,
  "peak_device_vram_mib": 7670.5,
  "prefix_envelopes_same": 21
}
```
