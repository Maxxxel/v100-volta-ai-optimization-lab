# Public audit excerpt

Original SHA256: `1cb6bc76806bd1de7c63a02007e4c4745adb1036a9c98452f1a553e12b293eb0`

Original file: `research-metadata.json`; 5769 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "DEFERRED_NO_ADMITTED_BEYOND_NATIVE_SCALING_WORKLOAD_AND_CURRENT_F16_2X_EXCEEDS_BUDGET",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "Analytical budget is not an observed OOM, allocator result or measuredVRAMsaving.",
    "Only oneF16doubling example is ruledout; no universal maximumcontext bound or Q8/Q4/offload exclusion.",
    "Metadata262K is not training-data verification or a local quality guarantee.",
    "Previously failedquality gates are preserved without assigning a new causal explanation."
  ],
  "measurement_type": "SOURCE_ONLY_CONTEXT_SCALING_RESOURCE_ADMISSION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "model_starts": 0,
  "new_GPU_runs": 0
}
```
