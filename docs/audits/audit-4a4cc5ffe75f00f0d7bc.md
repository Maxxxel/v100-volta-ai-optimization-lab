# Public audit excerpt

Original SHA256: `4a4cc5ffe75f00f0d7bc715898a90b1945ae4bb2f907d9359c010cad7f755493`

Original file: `AUDIT.json`; 2702 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "STATE_COMPONENT_FAILURE_NO_MODEL_ADMISSION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "No model loaded, no QA/coding/tool/agent quality or performance qualification.",
    "Tests existing stockGGML CUDA operators with a native graph matching the proposed storage policy; R350 libllama graph construction itself is not invoked.",
    "Independent CPU double recurrence and CPU half rounding check operator/storage semantics, not preservation of original F32 targetmodel logits or token choices.",
    "Component wall/energy includes CPUoracle work and CUDAinitialization; not inferenceperformance or per-solved-assistant-taskenergy.",
    "Generic GDN primitive and half storage/gather/copy paths only; full prefill chunk fusion, server serialization, full MTP rollback and slotisolation remain unqualified.",
    "Unwritten snapshot slots require exact untouchedbits; writtenhalfallowed1ULP due FP32reduction order; attention tolerance frozen beforeGPU."
  ],
  "measurement_type": "GPU_STATE_STORAGE_NUMERICS"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_GPU_execution": true,
  "component_wall_s": 0.386870717,
  "gpu_energy_j_approx": 16.878811563558017,
  "model_starts": 0,
  "numerical_component": {
    "wall_s": 0.386870717
  },
  "peak_device_vram_mib": 239.875
}
```

</details>
