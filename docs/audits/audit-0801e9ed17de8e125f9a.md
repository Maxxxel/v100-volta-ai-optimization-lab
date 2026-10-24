# Public audit excerpt

Original SHA256: `0801e9ed17de8e125f9a018ebe0e894a9fab3dcfa89d249ec600c9a6f0ac71c7`

Original file: `AUDIT.json`; 14323 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "PRESERVE_EXISTING_DEFAULT_F32_FUSION_NO_NEW_OPTIMIZATION_OR_FULL_MTP_QUALIFICATION",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "Old native comparison explicitly disables existing defaultfusion inA and enables inB. B is not a newly invented kernel or gain over unchangedstockA0.",
    "Modeltrace proves nativefusionpath was reached; boundedmarker is not exhaustive per-token dispatch/timing.",
    "One head32/H4/T3/K3 CPUreference testcase repeated inA/B, not2unique cases or fullcurrentmodelK4fusion proof.",
    "R97/R194 validate existingGDNprimitive/chunk/snapshotsemantics without ggmlcpygraph, not C13writefusion or wholeprefix/multislot/MTPstate machinery.",
    "F16destination is explicitly rejected by old/currentF32directcachefusion matcher. R350conversionpolicy is separate and unqualified, not additive.",
    "QA24observationsare12originaltaskstwice; scoresreused, not independentregrading/fullCoding/Toolqualification.",
    "R194audit was generatedinsideGPUlease: two coordinationfiles laterfinalized. Originalprefix/reservationpre-finalization bytes reconstructed exactly;20numeric/metadata files unchanged. Oldfiles/audit leftunchanged.",
    "No newGPUexecution, calibration, referencechange, speedpromotion or combinationtest."
  ],
  "measurement_type": "REVIEW_EXISTING_F32_STATE_FUSION_SCOPE"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": false,
  "metrics": {
    "A": {
      "QA_GPU_j": 2626.5220666031782,
      "QA_unique_tasks": 12,
      "QA_wall_sum_s": 10.175231618,
      "peak_device_VRAM_mib": 7356.5
    },
    "B": {
      "QA_GPU_j": 2601.3741431780027,
      "QA_unique_tasks": 12,
      "QA_wall_sum_s": 10.122992687,
      "peak_device_VRAM_mib": 7356.5
    }
  },
  "new_GPU_runs": 0,
  "old_native_model_starts_verified": 4
}
```

</details>
