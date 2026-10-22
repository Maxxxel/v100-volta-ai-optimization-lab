# Public audit excerpt

Original SHA256: `abe7f577bc3edbec058e8a1b6f6b7d7471908eb62f44ef86dd23488b47021343`

Original file: `AUDIT.json`; 10261 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "QWEN38_NO_MTP32K_EXTENDED_CAPACITY_SCREEN_PROMISING_NEEDS_CONFIRMATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Common14KsameinputIDs compared only tostoredR43216K; extended doubledcatalog separateworkload, no causal speedup fromdifferentlengths.",
    "Extendedactualtokenlengthverified>16Kandfit32K; fixedgenerator/oracles,12developmentcases notmodeltrainingholdout.",
    "Original12nativeJSONweaknessandCoding/Tools/Agentnegativefindingsretained; no overallmodel or productionqualification.",
    "OnlyGPUboardcaseinferenceenergy; startup,warmup,CPU/systemenergyexcluded; no repeated-run variance or visibleTTFT."
  ]
}
```

## Selected aggregate measurements

```json
{
  "VRAM_increase_MiB_vs16K": 1040.0,
  "actual_GPU_execution": true,
  "actual_generation_requests": 40,
  "common_GPU_J_per_success_change_percent_vs16K": 0.036432478909764754,
  "common_control_passed": true,
  "common_wall_change_percent_vs16K": 0.0762440460144509,
  "context_profile_token_ranges": {
    "common": {
      "maximum_tokens": 14066,
      "minimum_tokens": 14003
    },
    "extended": {
      "maximum_tokens": 27729,
      "minimum_tokens": 27562
    }
  },
  "context_tokens": 32768,
  "model_starts": 1,
  "original12": {
    "format": 6,
    "observed": 12,
    "semantic": 10
  },
  "peak_device_vram_mib": 14014.5,
  "scopes": {
    "common": {
      "full12": true,
      "gpu_energy_j_approx": 73402.4561531012,
      "gpu_j_per_success": 6116.871346091767,
      "observed": 12,
      "planned": 12,
      "solved": 12,
      "wall_s": 269.612280729
    },
    "extended": {
      "full12": true,
      "gpu_energy_j_approx": 148646.22863598037,
      "gpu_j_per_success": 12387.18571966503,
      "observed": 12,
      "planned": 12,
      "solved": 12,
      "wall_s": 551.395513527
    }
  }
}
```
