# Public audit excerpt

Original SHA256: `d2d5c935e9e86b3fca2e8d31cae55e9aeffe6a8505ef59ead099ae144940006e`

Original file: `INDEPENDENT_REVIEW.json`; 7711 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "CONVERSION_AND_COPY_MATCH_EXACTLY_IN_TESTED_SCOPE_RECURRENT_TRAJECTORY_GATE_STILL_FAILS",
  "interpretation": "Storedhalf values are correct nearesthalf conversions of each testedGPUF32snapshot. Tiny localCPUdouble/GPUF32arithmetic differences coexist with larger halfULP distances in independently evolved rounded trajectories. No conversion/copy defect demonstrated; no proof of fullmodelquality preservation.",
  "limits": [
    "Case3only,H2/QH1,T1,B1,K4,16calls. No head32/fullmodel/serverstatefile/MTPagent qualification.",
    "Exact localconversion does not make F16state equivalent to originalF32state, and does not release the failedoriginaltrajectorygate.",
    "No new tolerance, modelquality claim, practicalmemorygain or speedup inferred."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "model_starts": 0
}
```

</details>
