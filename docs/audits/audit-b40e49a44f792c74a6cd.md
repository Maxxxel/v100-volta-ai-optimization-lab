# Public audit excerpt

Original SHA256: `b40e49a44f792c74a6cda5b7c3ac6e8df7e3da9032b10bf9200796f8c33a0ccf`

Original file: `AUDIT.json`; 1611 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "NO_PRACTICAL_GAIN_IN_SINGLE_SCREEN",
  "evidence_class": "LOKAL_GEMESSEN",
  "scope": "Previously exposed Agent33 development tasks, fixed A then B order, same engine/model/profile, 0 versus 4096 MiB conversion cache. No independent holdout or champion qualification. Arm energy includes startup and idle; sample boundaries omitted. Per-case energy not measured."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "comparison": {
    "arm_gpu_energy_j_A": 110514.19,
    "arm_gpu_energy_j_B": 110185.522,
    "arm_gpu_j_per_success_A": 3946.9353571428574,
    "arm_gpu_j_per_success_B": 3935.1972142857144,
    "paired_gained": 0,
    "paired_lost": 0,
    "peak_device_vram_mib_A": 7680.5,
    "peak_device_vram_mib_B": 11776.5,
    "request_wall_reduction_percent": 1.4167890053129018,
    "request_wall_s_A": 400.845347522,
    "request_wall_s_B": 395.16621471,
    "successes_A": 28,
    "successes_B": 28,
    "tasks_per_arm": 33
  },
  "model_starts": 2
}
```

</details>
