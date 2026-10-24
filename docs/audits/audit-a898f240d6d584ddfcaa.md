# Public audit excerpt

Original SHA256: `a898f240d6d584ddfcaaa6fdcf3b3d1a75c250ee73960005a4fe362f2551abb9`

Original file: `AUDIT.json`; 43761 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "ORNITH_CODING_SCREEN_NO_PRACTICAL_JOINT_WIN",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Same164HumanEvalPlus+16customlongdevelopmenttasks,notnewholdout;ownnativechattemplate/tokenizer",
    "HumanEval32excludedonlyfromvalidated163,full164alwaysreported;scorebaseANDplus",
    "NativeOrnithnoMTP/noCachecomparedtoqualifiedOmnigraft+cache;modelconfigtradeoffexplicit,no intrinsiccausalarchitectureclaim",
    "180freshnativeinput-IDfixturesfrozenbeforegeneration;original12reuseR253,sameconfig",
    "GPUinferencewindowenergyonly,notCPU/judge/system/startup;allgeneratedcodeexecutedonlyinisolatedCPUofficialjudge",
    "Coding screen only;R253agenttradeoff/policyfaultsremain,nomodelwinner/productionqualification"
  ],
  "score_rule": "base_pass AND plus_pass"
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "actual_generation_requests": 184,
  "model_starts": 1,
  "peak_device_vram_mib": 7356.5,
  "scopes": {
    "custom_long16": {
      "gpu_energy_j_approx": 17279.930355146305,
      "solved": 14,
      "tasks": 16,
      "wall_s": 60.700327662999996
    },
    "standard_full164": {
      "gpu_energy_j_approx": 130686.38691340903,
      "solved": 117,
      "tasks": 164,
      "wall_s": 456.935627082
    },
    "standard_validated163": {
      "gpu_energy_j_approx": 129155.5927707294,
      "solved": 117,
      "tasks": 163,
      "wall_s": 451.494141691
    }
  }
}
```

</details>
