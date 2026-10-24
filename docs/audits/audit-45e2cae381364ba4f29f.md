# Public audit excerpt

Original SHA256: `45e2cae381364ba4f29f2c96e7d010d2eb28b3bc53eb87de4b5f31a2910c2011`

Original file: `AUDIT.json`; 2613 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "GEMMA4_NATIVE_TOOL_MODEL_SCREEN_NO_PRACTICAL_WIN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Same100balancedBFCLpilot/developmenttasks,notfullBFCLornewholdout",
    "Gemma native template/tokenizer and publisher T1/P.95/K64; same task messages/tools/scorer/1024 cap, different source sampling; noTok/s-onlyrank",
    "SingleBscreenagainstvalidstoredcomparators;independentconfirmationneededforwinner",
    "Official QAT Q4_0 fast/noMTP/cache Gemma profile; JSON-object not applied to native function framing",
    "GPUboardinferenceenergyonly,notCPU/system/load;no actualtoolsproductiondispatch"
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_full_GPU_offload": true,
  "gpu_energy_j_approx": 34637.24230076317,
  "gpu_j_per_success": 412.348122628133,
  "model_starts": 1,
  "peak_device_vram_mib": 8118.5,
  "wall_s": 144.725644477
}
```

</details>
