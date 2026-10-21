# Public audit excerpt

Original SHA256: `be78ded0938b2be399c8896a4ebf407c11804504137c22b9635932ced7f1dfce`

Original file: `AUDIT.json`; 2640 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "H08_NO_PRACTICAL_PREFAULT_INCLUSIVE_WORKFLOW_WIN_OR_QUALITY_LOSS",
  "evidence_class": "LOKAL_GEMESSEN",
  "limitations": [
    "Onecold/prewarmcandidatepaironly;positivegainneedsindependentconfirmation",
    "Botharmssamebyteidenticalprivateinode;notaglobalcoldOS/testofproductiveOllamapagecache",
    "PrimaryrequesttofirstreplyincludesBprefaulttime;fasterprocessloadaloneisnotworkflowwin",
    "Copy/hasharecommonone-timeartifactpreparationexcludedfrombotharms;nooriginalfilecacheadvice/globalflush",
    "GPUboardenergyonly;CPU/systemenergyandpredictiveprefetchhitratemissing",
    "12originalquestionsunchangednotgeneralmodelquality,stabilityorroutingqualification"
  ]
}
```

## Selected aggregate measurements

```json
{
  "actual_generation_requests": 24,
  "metrics": {
    "A": {
      "before_process_resident_fraction": 0.0,
      "cold_resident_fraction": 0.0,
      "end_to_end_first_reply_s": 7.501458114,
      "energy_coverage": 1.0,
      "gpu_energy_to_first_reply_j": 367.66891112988844,
      "prefault_s": 5.99e-07,
      "process_to_health_s": 7.168155437
    },
    "B": {
      "before_process_resident_fraction": 1.0,
      "cold_resident_fraction": 0.0,
      "end_to_end_first_reply_s": 9.455915371,
      "energy_coverage": 1.0,
      "gpu_energy_to_first_reply_j": 399.4006486900354,
      "prefault_s": 6.807575217,
      "process_to_health_s": 2.316618251
    }
  },
  "model_starts": 2
}
```
