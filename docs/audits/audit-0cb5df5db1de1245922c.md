# Public audit excerpt

Original SHA256: `0cb5df5db1de1245922cfcd5ffadeb1842d7ac96d0f65bd025311830655c3c09`

Original file: `research-metadata.json`; 14161 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "limits": [
    "These are reported cumulative GPU-counter bounds, not interpolation, extrapolation or guessed counters.",
    "Bounds account for unknown counter-read time within each recorded query interval. Undocumented NVML sensor/calibration error is not bounded.",
    "Selected contiguous groups include setup between selected requests; unselected tasks, startup/warmup and CPU/system energy are excluded.",
    "Stored LFM and fresh Bonsai profiles were measured at different times. This is not balanced A/B, a causal kernel effect or general model superiority.",
    "Original per-case power integration remains NOT MEASURED because its sampling-gap gate failed. No historical audit or scorer result is replaced."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "model_requests": 0
}
```

</details>
