# Public audit excerpt

Original SHA256: `3d43ffa876d47a33c8dfca7a08fd5f50da78c0d4c0758599449a00a98bb67f2d`

Original file: `AUDIT.json`; 2245 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "ROTATION_OFF_NOT_PRACTICALLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "B-onlyvsstoredR234Q8valueRotationON;positive requiresfreshconfirmation",
    "Onlyrotationdisabled;KF16/VQ8/recurrentF32fixed,noMTP/cache/powercombination",
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
      "control_change_percent": 0.5223694443221572,
      "median": 66.55389188294062
    },
    "long_e2e_s": {
      "control_change_percent": -0.23199133230337177,
      "median": 15.862241306
    },
    "long_gpu_energy_j": {
      "control_change_percent": -1.1453701623867607,
      "median": 4218.307784252388
    },
    "short_decode_tps": {
      "control_change_percent": 0.32091037271375633,
      "median": 79.19863454070716
    }
  },
  "memory_saved_mib": 230.0,
  "model_starts": 1,
  "original12_nonregression": true,
  "peak_device_vram_mib": 7924.5,
  "requests": 32
}
```

</details>
