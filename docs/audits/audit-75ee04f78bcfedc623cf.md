# Public audit excerpt

Original SHA256: `75ee04f78bcfedc623cf848d0d31f7cf3d9dc040fbdc9b669720e441c41d42de`

Original file: `INDEPENDENT_REVIEW.json`; 5842 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "limits": [
    "Only resident originalQ6/8K/1slot profile; no out-of-core, host-RAM savings, migration counter, agent or coldstart claim.",
    "CUDA allocation observation preserves original ABI/pointers/results and adds no CUDA operations; positive qualification needs fresh matching instrumentation control.",
    "Measured B GPU energy only; unavailable stored A0 energy is not invented."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "native_metrics": {
    "decode": {
      "A0_E2E_reduction_percent": 0.7328111396422421,
      "median_E2E_s": 1.664452188,
      "median_GPU_j": 450.5469009783743,
      "range_percent": 0.0785466839735899
    },
    "prefill": {
      "A0_E2E_reduction_percent": 7.39091253583365,
      "median_E2E_s": 0.198385009,
      "median_GPU_j": 55.708618184189675,
      "range_percent": 0.6981797702264936
    },
    "prefill2048": {
      "A0_E2E_reduction_percent": 1.4754366720500234,
      "median_E2E_s": 0.719863442,
      "median_GPU_j": 182.8426280544353,
      "range_percent": 0.29188938865435465
    },
    "prefill4096": {
      "A0_E2E_reduction_percent": 0.26594286924276345,
      "median_E2E_s": 1.420817335,
      "median_GPU_j": 370.4789116824757,
      "range_percent": 0.1667670390578367
    }
  },
  "original12": [
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    },
    {
      "prior_grade_loss": false
    }
  ],
  "peak_device_vram_mib": 7452.5
}
```
