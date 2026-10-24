# Public audit excerpt

Original SHA256: `fae4b1903a527efdd0b8cce27be9692f2edd11e7f361057382e33d0d2109758d`

Original file: `AUDIT.json`; 1555 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MEAN_CENTERED_Q4_SCREEN_FAILED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "B-onlyvsjustcalibratedR268sameforkF16;nonewA0/C",
    "OnlyprecalibratedbiasloadedatfixedQ4K/VF16/recurrentF32;noMTP/cache/powercombination",
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
  "memory_saved_mib": 396.0,
  "model_starts": 1,
  "original12_nonregression": false,
  "peak_device_vram_mib": 7736.5,
  "requests": 12
}
```

</details>
