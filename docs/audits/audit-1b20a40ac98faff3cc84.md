# Public audit excerpt

Original SHA256: `1b20a40ac98faff3cc848e16904dd8312c4973f73a1a4a763a0a09a7a80c1cee`

Original file: `AUDIT.json`; 2070 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "SAME_FORK_F16_REFERENCE_VALID",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Newruntimebaseline;oldengineR222descriptiveonly,noCpromotion",
    "OriginalOmniQ6/newfork/F16KV/recurrentF32;noMTP/cache/powercombination",
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
      "control_change_percent": 3.701091275143331,
      "median": 74.58798945431545
    },
    "long_e2e_s": {
      "control_change_percent": 3.693987675607513,
      "median": 16.241720925
    },
    "long_gpu_energy_j": {
      "control_change_percent": 5.547375082264194,
      "median": 4418.525589894155
    },
    "short_decode_tps": {
      "control_change_percent": 4.216715863869669,
      "median": 83.23327863093708
    }
  },
  "memory_saved_mib": 22.0,
  "model_starts": 1,
  "original12_nonregression": true,
  "peak_device_vram_mib": 8132.5,
  "requests": 32
}
```
