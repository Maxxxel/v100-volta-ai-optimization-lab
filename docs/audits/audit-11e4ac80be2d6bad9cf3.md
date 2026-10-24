# Public audit excerpt

Original SHA256: `11e4ac80be2d6bad9cf352e6f6a2f0f7f1b606613f1fd493926cf8f0eef42d6d`

Original file: `AUDIT.json`; 1319 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "STATIC_DRAFT1_NOT_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Single candidate process versus stored max3; no fresh drift control, no winner promotion",
    "Fixed length1 tests one static parameter; adaptive drafting remains unimplemented",
    "Original12 skipped after deterministic native regression or futility stop",
    "Native token identity applies only observed frozen samples, not universal losslessness"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "metrics": {
    "decode": {
      "latency_reduction_percent_vs_A0": 30.67469146230336,
      "latency_reduction_percent_vs_MTP3": -26.83928258573649,
      "latency_reduction_percent_vs_native_C": 30.831409347941573,
      "median_e2e_s": 1.162404847,
      "median_gpu_energy_j_approx": 295.10888068014617,
      "range_percent": 0.5752032105901849
    }
  },
  "model_starts": 1,
  "peak_device_vram_mib": 8908.5,
  "requests": 7
}
```

</details>
