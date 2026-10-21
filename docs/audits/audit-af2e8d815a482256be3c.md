# Public audit excerpt

Original SHA256: `af2e8d815a482256be3c9607178488269091b3fde93f6016a7f2f08294b30ed6`

Original file: `AUDIT.json`; 2249 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "ROTATION_OFF_NOT_PRACTICALLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "B-onlyvsstoredR233Q8rotationON;positive requiresfreshconfirmation",
    "Onlyrotationdisabled;Q8K/Vf16/recurrentF32fixed,noMTP/cache/powercombination",
    "QuantizedoutputIDsrecordednotassumedlossless;no fullnumericaloracle",
    "Original12qualityonly;32Kfixtureissynthetic,no longdocumentsemantic/coding/agentqualification",
    "GPUboardenergyapprox,notwhole-systemenergy"
  ]
}
```

## Selected aggregate measurements

```json
{
  "long_metrics": {
    "long_decode_tps": {
      "control_change_percent": 0.7880371724740209,
      "median": 66.52533960662048
    },
    "long_e2e_s": {
      "control_change_percent": -0.24082614387841428,
      "median": 15.816817797
    },
    "long_gpu_energy_j": {
      "control_change_percent": -1.0048433584739391,
      "median": 4229.283240807421
    },
    "short_decode_tps": {
      "control_change_percent": 0.9080417995226409,
      "median": 79.30768760014936
    }
  },
  "memory_saved_mib": 230.0,
  "model_starts": 1,
  "original12_nonregression": true,
  "peak_device_vram_mib": 7924.5,
  "requests": 32
}
```
