# Public audit excerpt

Original SHA256: `13697d6c2db1e7cf8ca9b8da7d086f1e2069d7a1d354b506ebc1abd92a1c5fcb`

Original file: `AUDIT.json`; 5297 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GEMMA16K_LONG_INPUT_BASELINE_ADMITTED_FOR32K_CONTROL_SCREEN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "SameR338text/tools/oracles;Gemma own native template/tokenizer andT1P95K64, not identical cross-modelsampling.",
    "12development longinventory tasks, not fullBFCL or independentmodelwinner; actualGemmatokenlengths retained.",
    "No GDN/MTP/cache/grammar optimization;16Knewprofile only;32Knot yet tested.",
    "Original12knownnativeJSONformatweakness retained; sourceprevioussuccess loss stops thisprofile.",
    "GPUboardlongtask inferencewindow only; noCPU/system/load/warmupenergy; no productiontools."
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "actual_generation_requests": 28,
  "context_tokens": 16384,
  "full_12_semantic_score_claimed": true,
  "gpu_energy_j_approx": 33429.067342198075,
  "gpu_j_per_success": 2785.7556118498396,
  "model_starts": 1,
  "observed_cases": 12,
  "original12": {
    "format": 1,
    "observed": 12,
    "semantic": 10
  },
  "peak_device_vram_mib": 8254.5,
  "planned_cases": 12,
  "solved": 12,
  "wall_s": 124.101119805
}
```
