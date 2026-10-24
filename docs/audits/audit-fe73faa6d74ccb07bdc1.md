# Public audit excerpt

Original SHA256: `fe73faa6d74ccb07bdc1a61062744f6df9a2f9f082215e7a291ac85f925f4387`

Original file: `AUDIT.json`; 170715 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "BIND_EXISTING_TRACES_TRANSPORT_ALLOCATOR_AND_F32_SCOPE_KEEP_ATTENTION_NUMERICS_SEPARATE_FROM_SPEED_QUALIFICATION",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "Eight preserved traces read immutable/read-only and hash-checked before/after. No newGPUwork, no newHWcounter collection or calibration. Kernel/copy durations are summed events, not necessarily non-overlapping wall time.",
    "CUDA memcpy byte counts are copy-API activity, not physical DRAM/HBM transactions. Register/shared/local resource metadata do not measure achieved occupancy, spilling instructions, cache hit rates or roofline bandwidth.",
    "Six old attention windows contain24earlier modelstarts. Initial patch dispatch was real but numericinstrumentation recorded0cases. Later48cases/armpassed, but paired whole-engine scope and change_exercisedFalse prevent an isolated performancewin claim. Do not erase validnumerics or rerun old failedinstrumentation.",
    "Native flash-attn on/off/build-disable/quant-format availability and a D256Volta port are distinct variants; no modern Ampere-only kernel port inferred.",
    "R13fourCPUlayers and K06attentionKVplusrecurrentRS onCPU are measured capacity/latency tradeoffs, not newoverlappedstaging or isolatedKV-only gains.",
    "C06noVMM is an existingallocator toggle, not fragmentation defragmentation or entireVMM architecture. F32GDNcachefusion is stockdefault in the tested matcher, not a newkernel; F16statetrajectory/rollback/multislot remain separately unqualified.",
    "A new trace/profiler run requires an eligible missingmetric for a concrete patch. No replay/metadata review is counted as a newGPUtest, champion or fullaxiscompletion."
  ],
  "measurement_type": "REVIEW_EXISTING_HBM_TRACES_ALLOCATOR_RESIDENCY_AND_ATTENTION_SCOPE"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": false,
  "new_GPU_runs": 0
}
```

</details>
