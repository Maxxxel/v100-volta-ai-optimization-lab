# Public audit excerpt

Original SHA256: `b939abaa6c68ac7fbb46989896ffda9bac86f3021dee8d2b91d1e7c19d7a3d42`

Original file: `AUDIT.json`; 2820 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "NATIVE_Q8KV_COMPONENT_PASS_MODEL_SCREEN_PENDING",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Component random inputs compare CUDA against CPU on the same tensors; separate process repeats are not identical-input timing A/B.",
    "No whole-model quality, throughput, task-energy or champion claim.",
    "Existing A0/C profiles and historical mixed-KV negatives preserved.",
    "Guard applies only when native can_use_vector_kernel permits it; padding/prefill cases also test preserved fallback."
  ],
  "measurement_type": "GPU_Q8KV_ROUTING_NUMERICAL_ADMISSION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "gpu_energy_j_approx": 74.54588275865231,
  "model_starts": 0,
  "peak_device_vram_mib": 630.5
}
```
