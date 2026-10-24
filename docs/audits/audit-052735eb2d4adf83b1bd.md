# Public audit excerpt

Original SHA256: `052735eb2d4adf83b1bdf4e57d2422c101e7074a77457880ea598d0d2ffe0403`

Original file: `AUDIT.json`; 2211 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "Q8_KEY_32K_NOT_PRACTICALLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "B-onlyscreenvsstoredrecentmatching32KF16control;positive requiresfreshconfirmation",
    "OnlyattentionKcachechanged;Vf16/recurrentF32, noMTP/cache/powercombination",
    "QuantizedoutputIDsrecordednotassumedlossless;no fullnumericaloracle",
    "Original12qualityonly;32Kfixtureissynthetic,no longdocumentsemantic/coding/agentqualification",
    "GPUboardenergyapprox,notwhole-systemenergy"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "long_metrics": {
    "long_decode_tps": {
      "control_change_percent": -8.2317312434807,
      "median": 66.00519414102556
    },
    "long_e2e_s": {
      "control_change_percent": 1.2250034023314926,
      "median": 15.855000784
    },
    "long_gpu_energy_j": {
      "control_change_percent": 2.0523210751900223,
      "median": 4272.212282184863
    },
    "short_decode_tps": {
      "control_change_percent": -1.5921168340347847,
      "median": 78.59402103720592
    }
  },
  "memory_saved_mib": 222.0,
  "model_starts": 1,
  "original12_nonregression": true,
  "peak_device_vram_mib": 7932.5,
  "requests": 32
}
```

</details>
