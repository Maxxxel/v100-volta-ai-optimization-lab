# Public audit excerpt

Original SHA256: `3282effcb0cfa011c3fa3df749c6a84d28051aaebad9d1b286031a3190c7df83`

Original file: `AUDIT.json`; 1698 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "QWEN35_NATIVE_TOOL_MODEL_SCREEN_NO_PRACTICAL_WIN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Same100balancedBFCLpilot/developmenttasks,notfullBFCLornewholdout",
    "ModelnativeQwentemplate/tokenizerandactualtokenIDs; sharedtaskbodies/scorer/outputbudget/greedyseed; noTok/s-onlyrank",
    "SingleBscreenagainstvalidstoredcomparators;independentconfirmationneededforwinner",
    "NoMTP/cachebaselineforthisQwen35model;doesnotruleoutownoptimizedprofile",
    "GPUboardinferenceenergyonly,notCPU/system/load;no actualtoolsproductiondispatch"
  ]
}
```

## Selected aggregate measurements

```json
{
  "gpu_energy_j_approx": 32539.26549423958,
  "gpu_j_per_success": 374.01454591079977,
  "model_starts": 1,
  "peak_device_vram_mib": 5956.5,
  "wall_s": 123.929553805
}
```
