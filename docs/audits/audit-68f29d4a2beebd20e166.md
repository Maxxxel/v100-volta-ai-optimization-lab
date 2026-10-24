# Public audit excerpt

Original SHA256: `68f29d4a2beebd20e166625829db2b8c980e59e011bbc7f4b725a98012851bac`

Original file: `AUDIT.json`; 77816 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "REUSE_EXACT_FUSION_AND_TWO_Q6_PORT_NEGATIVES_RETAIN_R81_NO_RETEST",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "Read-only evidence review; no new GPU experiment or independent task regrading.",
    "C11 A is artificially forced dequant+cublas and disables existing quantized vector fusion; B forces fused MMVQ/MMQ. Standard also dispatches to cuBLAS on suitable shapes, so global B is not simply the stock engine. No 4x/5x A0 improvement inferred.",
    "C18 Q6 MMQ Pascal configuration changes host AND device configurations under common forced MMQ; not a stock A0 routing comparison.",
    "C18 four-row MMVQ applies only SM70 Q6, four output columns, no IDs/fusion, rows divisible by four. Original 4-slot/concurrency workload is not a current E09 parallel-profile safety qualification.",
    "Old QUALIFICATION speed_gain_qualified field uses historical protocol meaning, explicitly disclaims improved speed; it is not a current Champion qualification.",
    "HBM06 reuses C11 evidence; do not double count a new GPU run. HBM05 reuses reviewed R81; do not use one-token prefill fake decode TPS. R81 independent kernel numeric oracle absent; byte-identical outputs alone are limited-scope evidence.",
    "QA24 observations mean12unique frozen tasks repeated twice; no HumanEval/BFCL/full-agent comparison or statistical significance inferred.",
    "No new A0/C promotion, historical audit changes, original cell mutations, production change or global axis completion."
  ],
  "measurement_type": "REVIEW_EXISTING_FUSION_PORTED_Q6_AND_VOLTA_SCOPE"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": false,
  "new_GPU_runs": 0,
  "old_native_model_starts_verified": 12,
  "primary_archives_checked": 3
}
```

</details>
