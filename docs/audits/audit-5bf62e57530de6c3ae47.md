# Public audit excerpt

Original SHA256: `5bf62e57530de6c3ae47821cde6b0949c1e97f46c621b93d673585f0622c6b8a`

Original file: `AUDIT.json`; 3063 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "FRACTIONAL_QUEUE_SCREEN_REJECTED_PRIMARY_MEMORY_GATE",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "New0.25x/0.5x values only; existing1x/2x/4xnegatives preserved, no repeatedA0calibration.",
    "Originalstockbackend andCUDA/cuBLAS used; no privateSASS-only/compression/prefetch/MMQ/MTP/power combination.",
    "Environmentvalue verifiedinactualownedGPUchild; not a measurement of effectivephysicalqueuecapacity or proof of whichmemoryallocationchanged.",
    "NVMLdevice/processmemoryobservations only. No occupancy, HBMtransaction or commandbufferhardwarecounter claimed.",
    "Earlymemoryfutility means no completeoriginal12/nativeperformance/agentquality claim. Warmuptimings are not winnerqualification.",
    "TotalvariantNVMLboardJincludesprocessload/warmups/teardown, not matchedagenttaskenergy or energyper success.",
    "Anypromisingscreen needs independentfreshconfirmation/quality/stability; no directChampionpromotion."
  ],
  "measurement_type": "GPU_C16_FRACTIONAL_QUEUE_MEMORY_SCREEN"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": true,
  "model_starts": 2,
  "peak_device_vram_mib": 7354.5,
  "queue_memory_variants": [
    {
      "capacity_setting": "0.25x",
      "measurement_valid": true,
      "memory_saved_vs_A0_mib": 2.0,
      "minimum_memory_saving_mib": 64,
      "model_starts": 1,
      "peak_device_vram_mib": 7354.5,
      "primary_memory_gate_passed": false,
      "quality_cases": 0,
      "requests": 4,
      "scope": "EARLY_MEMORY_SCREEN_ONLY",
      "screen_passed": false,
      "warmup_requests": 4
    },
    {
      "capacity_setting": "0.5x",
      "measurement_valid": true,
      "memory_saved_vs_A0_mib": 2.0,
      "minimum_memory_saving_mib": 64,
      "model_starts": 1,
      "peak_device_vram_mib": 7354.5,
      "primary_memory_gate_passed": false,
      "quality_cases": 0,
      "requests": 4,
      "scope": "EARLY_MEMORY_SCREEN_ONLY",
      "screen_passed": false,
      "warmup_requests": 4
    }
  ],
  "requests": 8
}
```

</details>
