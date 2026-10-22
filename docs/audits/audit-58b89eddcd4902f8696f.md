# Public audit excerpt

Original SHA256: `58b89eddcd4902f8696fb88d53b4a165ade1bc1252a9189ef76d8c96dcf2e693`

Original file: `AUDIT.json`; 10978 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GEMMA4_NATIVE_ADMISSION_GATE_NOT_PASSED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "NativeGemma4operational/QA12admissiononly;notfullBFCL/coding/agent/modelwinner",
    "PublishedT1/P.95/K64/nativeGemma4fasttemplate/2048;notexternal benchmark reproduction",
    "ExistingstockSM70engine/CUDA12.8runtime;no kernelbuild or borrowedBonsaiPQ2paths",
    "BoardGPUenergyonlynotwhole-system;referenceA0/Cunchanged",
    "No actualtools/model-codeexecution/visionprojector"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 17,
  "actual_sampler_control_passed": true,
  "diagnostic_format_passes": 1,
  "diagnostic_semantic_passes": 10,
  "gpu_j_per_semantic_success": 156.71466031393987,
  "model_starts": 1,
  "observed_original_QA_cases": 12,
  "original12_full_score_claimed": true,
  "peak_device_vram_mib": 8118.5,
  "quality_gpu_energy_j": 1567.1466031393986,
  "quality_wall_s": 6.876421839,
  "semantic_successes_per_s": 1.4542446979160668
}
```
