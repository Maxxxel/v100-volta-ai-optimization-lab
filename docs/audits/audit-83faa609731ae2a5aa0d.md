# Public audit excerpt

Original SHA256: `83faa609731ae2a5aa0d7d13be52a040391f90b52fada0de0cf386209a352433`

Original file: `AUDIT.json`; 96122 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "PROMISING_QWEN35_CACHE_NEEDS_TARGETED_CONFIRMATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Existing identical cache CUDA artifact, prior seeded Q6/capture/mutation controls reused; actual Qwen3.5 hits required",
    "Only warm native synthetic prefill/128decode and original12 controls; no broad model/coding/BFCL/agent superiority",
    "Native text and fixed counts checked; no exact output-token-ID/lossless claim where A0 did not expose IDs",
    "Three repetitions in one Bprocess versus stored A0, no independence CI; promising candidates need targeted fresh confirmation and later quality/stability",
    "GPU generation energy only, excludes host/CPU/loading/idle; temperature telemetry only; no automatic champion"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 34
}
```

</details>
