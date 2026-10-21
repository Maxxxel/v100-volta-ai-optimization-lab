# Public audit excerpt

Original SHA256: `b5edd428483c7038becdd10ace30c4e01f8066c427c473dcb7f49424c42a0b00`

Original file: `research-metadata.json`; 7170 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "limitations": [
    "Five pre-frozen developmentcases,notfull100BFCL/agents/independentqualification",
    "All5nativeinputtokenIDs differ;same-tokenengine/kernelgain notcomparable",
    "OneAparallelcase has102additional explanatorytokens withsamevalidcalls; wall/Jdifference notattributedsolelytofrontendperformance",
    "Buffered external E2E;internalGostream differs, noTTFTclaim",
    "GPU-J excludeshost/CPU/load/idle;onepairedpilot, no statisticalgainclaim",
    "Original literalparitygateFalse preserved; independentfunctionalASTscore separately5/5both"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": true,
  "metrics": {
    "A": {
      "GPU_J_per_success": 446.58912680971827,
      "GPU_energy_j": 2232.9456340485913,
      "correct": 5,
      "energy_intervals": [
        {
          "GPU_energy_j": 203.31490859752452,
          "max_sample_gap_s": 0.038438989
        },
        {
          "GPU_energy_j": 235.84070673699938,
          "max_sample_gap_s": 0.04588939
        },
        {
          "GPU_energy_j": 761.2614713899447,
          "max_sample_gap_s": 0.040445785
        },
        {
          "GPU_energy_j": 437.3559519151792,
          "max_sample_gap_s": 0.016123847
        },
        {
          "GPU_energy_j": 595.1725954089433,
          "max_sample_gap_s": 0.019087032
        }
      ],
      "tasks": 5,
      "wall_s": 8.651852568
    },
    "B": {
      "GPU_J_per_success": 380.3124933329003,
      "GPU_energy_j": 1901.5624666645017,
      "correct": 5,
      "energy_intervals": [
        {
          "GPU_energy_j": 208.80663925659923,
          "max_sample_gap_s": 0.01853863
        },
        {
          "GPU_energy_j": 243.94038290256788,
          "max_sample_gap_s": 0.018550711
        },
        {
          "GPU_energy_j": 415.27172203812165,
          "max_sample_gap_s": 0.016255095
        },
        {
          "GPU_energy_j": 438.3621608741462,
          "max_sample_gap_s": 0.020401749
        },
        {
          "GPU_energy_j": 595.1815615930668,
          "max_sample_gap_s": 0.017872098
        }
      ],
      "tasks": 5,
      "wall_s": 7.436568606
    }
  },
  "peak_device_vram_mib": 7356.5
}
```
