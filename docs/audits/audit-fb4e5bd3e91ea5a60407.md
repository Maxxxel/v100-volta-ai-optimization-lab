# Public audit excerpt

Original SHA256: `fb4e5bd3e91ea5a604077d762fdb33acc10c4e31485ac06dc795d78cda36dd81`

Original file: `AUDIT.json`; 2402 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "EFFECTIVE_SIZE_COMPRESSION_ADMITTED_FOR_ONE_OBJECT_NO_GPU_OR_FULL_BACKEND_BENEFIT",
  "evidence_class": "CPU_LOKAL_GEMESSEN_KEIN_GPU_TEST",
  "limits": [
    "6026896->1652688bytes(-72.578%) applies to oneD256deviceobject, not the completebackend or GPUVRAM.",
    "DecodednativeSM70cubinbytesidentical; decodedPTXbytesdiffer, no all-imagesbyteidentity or futureJITequivalence claim.",
    "ActualNVCC--compress-mode=size added while allothercompileflags/pinnedsource/toolchain fixed; stockCMakecache/toolkit detection unchanged.",
    "No CUDAengine load, GPUexecution, quality, startup, decode, thermal or energy measurement.",
    "Fullbackend size-compression requires additional build/repackadmission; startupreferenceR386too variable, no automaticloadbenchmark or champion."
  ],
  "measurement_type": "CPU_EFFECTIVE_NVCC_COMPRESSION_SINGLE_TU_ADMISSION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "decoded_PTX_byte_identity": false,
  "decoded_cubin_byte_identity": true,
  "explicit_NVCCflag_applied": true,
  "model_starts": 0,
  "object_size_change_percent": -72.57812313336748,
  "original_inputs_preserved": true
}
```
