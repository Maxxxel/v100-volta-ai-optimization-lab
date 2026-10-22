# Public audit excerpt

Original SHA256: `82f3d7c217bf9fc6f74c9ba4f448a3442f07367b55093719f6ce6a29080a6b99`

Original file: `AUDIT.json`; 1613 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "NATIVE_KV_PREFETCH_COMPONENT_GATE_FAILED_NO_MODEL_ADMISSION",
  "evidence_class": "NICHT_VERIFIZIERT",
  "limits": [
    "New KV prefetch treatment only; R242 weight-prefetch and R381 Q8 route remain separate.",
    "Static prefetch instruction presence plus an eligible actual CUDA launch is recorded; no hardware counter or memory-transaction claim.",
    "Native component correctness does not establish model quality, speed, energy per task or champion qualification.",
    "GQA4 is exercised with eight KV heads in available native fixtures; exact whole Omni model uses four KV heads and requires separate model screen.",
    "No fresh reference recalibration, no model starts, no optimization combinations."
  ],
  "measurement_type": "GPU_F16_KV_PREFETCH_NUMERICAL_ADMISSION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "component_wall_s": 0.669182031,
  "gpu_energy_j_approx": 29.16096797237627,
  "model_starts": 0,
  "numerical_component": {
    "NMSE_limit": 0.0005,
    "cases_count": 0,
    "model_starts": 0,
    "numerical_gate_passed": false,
    "passed_cases": 0,
    "private_library_mapping_verified": true,
    "wall_s": 0.669182031
  },
  "peak_device_vram_mib": 550.5
}
```
