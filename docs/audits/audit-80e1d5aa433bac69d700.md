# Public audit excerpt

Original SHA256: `80e1d5aa433bac69d7009586f011ecde54d4ec6e80a4de09e87bbff7bdfed51d`

Original file: `AUDIT.json`; 244549 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "MATCHED_NATIVE_BFCL_MTP_OFF_A0_CALIBRATED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Balanced100single-turn native pilot,20percategory; not full BFCL leaderboard or agent qualification",
    "Official positive Python AST checker unchanged; strict local irrelevance score separate, no parse-error credit",
    "One greedy seed/process; generation+server-preprocessing wall/GPUenergy only; untimed template preparation, model-load, CPU/system/idle energy excluded",
    "MTPoff profile only",
    "No model superiority or automatic champion"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 116,
  "scopes": {
    "irrelevance": {
      "complete": 20,
      "gpu_energy_j": 20413.622808793232,
      "gpu_j_per_success": 2916.2318298276045,
      "protocol_valid": 20,
      "solved": 7,
      "successes_per_second": 0.09525493535293234,
      "tasks": 20,
      "wall_s": 73.487005939
    },
    "multiple": {
      "complete": 20,
      "gpu_energy_j": 14709.542131918544,
      "gpu_j_per_success": 774.1864279957128,
      "protocol_valid": 20,
      "solved": 19,
      "successes_per_second": 0.34728186167506325,
      "tasks": 20,
      "wall_s": 54.710602818
    },
    "overall": {
      "complete": 100,
      "gpu_energy_j": 99960.8953697791,
      "gpu_j_per_success": 1298.1934463607674,
      "protocol_valid": 100,
      "solved": 77,
      "successes_per_second": 0.21213106087957764,
      "tasks": 100,
      "wall_s": 362.983146743
    },
    "parallel": {
      "complete": 20,
      "gpu_energy_j": 26863.062811916665,
      "gpu_j_per_success": 1790.8708541277776,
      "protocol_valid": 20,
      "solved": 15,
      "successes_per_second": 0.155542309792978,
      "tasks": 20,
      "wall_s": 96.43678314900001
    },
    "parallel_multiple": {
      "complete": 20,
      "gpu_energy_j": 24785.340880036463,
      "gpu_j_per_success": 1457.961228237439,
      "protocol_valid": 20,
      "solved": 17,
      "successes_per_second": 0.18902980515407122,
      "tasks": 20,
      "wall_s": 89.932907597
    },
    "simple_python": {
      "complete": 20,
      "gpu_energy_j": 13189.326737114186,
      "gpu_j_per_success": 694.1750914270624,
      "protocol_valid": 20,
      "solved": 19,
      "successes_per_second": 0.3924334919890168,
      "tasks": 20,
      "wall_s": 48.41584724
    }
  }
}
```
