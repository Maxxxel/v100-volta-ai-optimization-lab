# Public audit excerpt

Original SHA256: `5c12c2ecf298df008b8b238d1958e71fec1e4ee18a61c87ec7bff397577193af`

Original file: `AUDIT.json`; 3972 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "WEIGHTEDV_FP32_NUMERICAL_SCREEN_FAILED_NO_MODEL_ADMISSION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Operatorcomponent only, randomnativefixtures with exactuploadedbytes verified; no wholeOmniweightload or original12/taskqualityresult.",
    "This is a precisionvariant of the existingtileoperator; newentryname onlyavoidsCUDAregistrationcollision, not a novelkernelalgorithmclaim.",
    "OnlyweightedVcompute/rescale precision changed; Q/K/KQrepresentationandprefillguardbypasses preserved. No R384prefetch/Q8routing/MTP/cache/power combination.",
    "Seededbaseline mayfail32Ktolerance; retainedasvalidcorrective-treatmentcontrol, not a32Kmodelqualitychampion.",
    "Instrumentedcomponentwall/Joule totals includeCPUinitialization/hashing/referencecompute and are not inference speed or GPUJ/success.",
    "A numericalpass requires subsequent realmodelquality/latency/memory/energy/stability checks beforeanychampion."
  ],
  "measurement_type": "GPU_WEIGHTEDV_FP32_EXACT_INPUT_NUMERICAL_SCREEN"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": true,
  "model_starts": 0,
  "peak_device_vram_mib": 812.5,
  "weighted_V_precision_component": {
    "NMSE_comparisons": [
      {
        "A_NMSE": 2.9314524719616203e-06,
        "B_NMSE": 2.9314524719616203e-06,
        "change_percent": 0.0
      },
      {
        "A_NMSE": 0.00036829741005028356,
        "B_NMSE": 0.00036302013180500206,
        "change_percent": -1.4328849731962578
      },
      {
        "A_NMSE": 0.0006796596455055297,
        "B_NMSE": 0.0006718347742246566,
        "change_percent": -1.1512926113265043
      },
      {
        "A_NMSE": 0.0007395845164017028,
        "B_NMSE": 0.0007307560497686112,
        "change_percent": -1.1937062549720157
      },
      {
        "A_NMSE": 2.2232163018119267e-05,
        "B_NMSE": 2.2232163018119267e-05,
        "change_percent": 0.0
      },
      {
        "A_NMSE": 2.4111667347203536e-05,
        "B_NMSE": 2.4111667347203536e-05,
        "change_percent": 0.0
      }
    ],
    "NMSE_limit": 0.0005,
    "actual_precision_dispatch_verified": true,
    "baseline_passed_cases": 4,
    "candidate_numerical_gate_passed": false,
    "candidate_passed_cases": 4,
    "identical_tensor_upload_bytes_SHA_verified": true,
    "model_starts": 0,
    "native_cases_per_arm": 6,
    "operator_processes": 2,
    "peak_device_vram_mib": 812.5,
    "tensor_upload_records": 86
  }
}
```

</details>
