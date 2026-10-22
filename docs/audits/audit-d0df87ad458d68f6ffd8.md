# Public audit excerpt

Original SHA256: `d0df87ad458d68f6ffd8598ba023a7ac349453f3245ccadd058a6c176333700d`

Original file: `AUDIT.json`; 7274 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "INSTRUCT_QA_SCREEN_PROMISING_NEEDS_CODING_TOOLS_AGENTS",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "PublishedwholeInstructprofile:modeANDsamplerchange,notisolatedkernel/quantizationspeedup",
    "B-onlycachedR263comparison,notindependentprofilewinnerqualification",
    "Original12diagnosticonly;Coding/Tools/isolatedAgentsandGermanqualityneeded",
    "GPUinferenceenergyonly;noCPU/system/loadenergy",
    "AllpriorA0/Candweightsunchanged;R273fixedPQ2numericsreused"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 17,
  "actual_sampler_control_passed": true,
  "diagnostic_format_passes": 8,
  "diagnostic_semantic_passes": 9,
  "model_starts": 1,
  "observed_original_QA_cases": 12,
  "original12_full_score_claimed": true,
  "peak_device_vram_mib": 8158.5,
  "quality_wall_s": 11.957781277
}
```
