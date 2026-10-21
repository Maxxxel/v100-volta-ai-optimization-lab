# Public audit excerpt

Original SHA256: `47f34ac098ae5d2e1f5028f5c1e9460758a9721b053ebbf65374c36bb43cf948`

Original file: `AUDIT.json`; 3210 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "R93_R221_32K_NATIVE_PREFILL_PROFILE_INDEPENDENTLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "QualifiedONLYnative32Ksyntheticprefillprofile:twoindependentcacheBprocessesR93/R221,matchingstoredA0andfreshR222cache0control,not8K/MTP/agentprofile",
    "Original12answersandlongnativeIDsunchanged; no longdocumentsemanticqualityor newcoding/tools/agentclaim",
    "Native3reps/process are descriptive repeatability,not independentsemanticqualitytasks or24hproductionstability",
    "No newA0calibration, no productiondeployment; GPUfullrequestenergyonly, noCPU/system/load/visibleTTFT"
  ]
}
```

## Selected aggregate measurements

```json
{
  "long_metrics": {
    "long_decode_tps": {
      "A0_change_percent": 0.2775661846118105,
      "median": 71.92594459436883,
      "range_percent": 0.07184083714025795
    },
    "long_e2e_s": {
      "A0_change_percent": -0.043174138507717785,
      "median": 15.663126946,
      "range_percent": 0.2153978903211002
    },
    "long_gpu_energy_j": {
      "A0_change_percent": -0.3702934561929605,
      "median": 4186.296046159681,
      "range_percent": 1.3964724405738105
    },
    "short_decode_tps": {
      "A0_change_percent": -0.04163071667718787,
      "median": 79.8655742900768,
      "range_percent": 0.3523089564505245
    }
  },
  "model_starts": 1,
  "peak_device_vram_mib": 8154.5,
  "requests": 11
}
```
