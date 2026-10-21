# Public audit excerpt

Original SHA256: `058f7fb472328b4ccdeeae69c9146073534f1a449071686094bae5f0b41babd0`

Original file: `AUDIT.json`; 52206 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GRAFT_CODING_QUALITY_MEMORY_SCREEN_PASSED_NOT_GENERAL_SPEED_CHAMPION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Exact existing164HumanEvalPlus+16customlongtasks; no newbenchmarkholdout",
    "HumanEval/32 remains excluded only from validated163, full164also reported",
    "Quality/memoryscreen only vs qualifiedR181externalMTP C; no freshcodingcontrol or generalcodingspeedwin",
    "GPUenergy approximate inferencewindows, not system/startup energy; no productiondeployment"
  ]
}
```

## Selected aggregate measurements

```json
{
  "model_starts": 1,
  "peak_device_vram_mib": 7966.5,
  "scopes": {
    "custom_long16": {
      "gpu_energy_j_approx": 11437.451257796934,
      "solved": 16,
      "tasks": 16,
      "wall_s": 42.245476014
    },
    "standard_full164": {
      "gpu_energy_j_approx": 74797.31763950948,
      "solved": 132,
      "tasks": 164,
      "wall_s": 270.633297554
    },
    "standard_validated163": {
      "gpu_energy_j_approx": 72579.2518467272,
      "solved": 132,
      "tasks": 163,
      "wall_s": 262.802572938
    }
  }
}
```
