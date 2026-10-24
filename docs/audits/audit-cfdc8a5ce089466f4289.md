# Public audit excerpt

Original SHA256: `cfdc8a5ce089466f4289000714608703a392e314e621f7743c382702e1a78785`

Original file: `AUDIT.json`; 5446 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "MLOCK_WARM_SCREEN_REQUIREMENTS_NOT_PASSED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Single R15 load-mode factor at original300W/defaultclocks/Q6/engine/u512/cache0, exact native prompts/tokens and12originalanswers. No new baseline or combinations.",
    "Warm-file-cache/warmGPU screen only: no RAM-pressure, swap, cold-disk, load-latency or model-switching benefit claim. Host memory binding is not GPU HBM pinning.",
    "Actual worker VmLck and hostMemAvailable retained; locks end with owned process. No productive service/config/global cache changes.",
    "Three repetitions/oneprocess only; fresh confirmation required for a meaningful survivor. GPUrequest energy excludes CPU/system/load/idle; A0energy absent, Ccomparison explicit."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 28,
  "peak_process_vram_mib": 7114
}
```

</details>
