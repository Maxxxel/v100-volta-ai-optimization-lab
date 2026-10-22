# Public audit excerpt

Original SHA256: `23d38cbb14bfd9a5f424fa93c3220c2481e59e4d49706aa8ee6f35b34000dafe`

Original file: `AUDIT.json`; 43959 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "GEMMA4_CODING_MODEL_SCREEN_PROMISING_NEEDS_BROADER_CONFIRMATION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Same164HumanEvalPlus+16customlongdevelopmenttasks,notnewholdout;ownnativechattemplate/tokenizer",
    "HumanEval32excludedonlyfromvalidated163,full164alwaysreported;scorebaseANDplus",
    "NativeGemmaQATQ40T1noMTP/noCachecomparedtoqualifiedOmnigraft+cache;modelconfigtradeoffexplicit,no intrinsiccausalarchitectureclaim",
    "180freshnativeinput-IDfixturesfrozenbeforegeneration;original12reuseR421andformatR422R423,scopeexplicit",
    "GPUinferencewindowenergyonly,notCPU/judge/system/startup;allgeneratedcodeexecutedonlyinisolatedCPUofficialjudge",
    "Coding screen only;R424nativeTool84/100negative remains,nomodelwinner/productionqualification"
  ],
  "score_rule": "base_pass AND plus_pass"
}
```

## Selected aggregate measurements

```json
{
  "actual_full_GPU_offload": true,
  "actual_generation_requests": 184,
  "model_starts": 1,
  "peak_device_vram_mib": 8118.5,
  "scopes": {
    "custom_long16": {
      "gpu_energy_j_approx": 24089.84561229056,
      "solved": 16,
      "tasks": 16,
      "wall_s": 95.65515782
    },
    "standard_full164": {
      "gpu_energy_j_approx": 183962.58556396523,
      "solved": 149,
      "tasks": 164,
      "wall_s": 741.044285822
    },
    "standard_validated163": {
      "gpu_energy_j_approx": 182195.5005183773,
      "solved": 149,
      "tasks": 163,
      "wall_s": 733.838468562
    }
  }
}
```
