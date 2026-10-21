# Public audit excerpt

Original SHA256: `577b1f3693e2c89cecab48dc643bf226b17a346dffad9984fa5f87fba4dc3afc`

Original file: `AUDIT.json`; 17349 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{
  "decision": "REUSE_CALIBRATION_DISTINGUISH_NATIVE_EXPERIMENTAL_TRAINER_FROM_QAT_LORA_READINESS_NO_BLANKET_16GB_EXCLUSION",
  "evidence_class": "LOKAL_STATISCH_GEPRUEFT",
  "limits": [
    "No newcalibration/modelgeneration/optimizerstep, no modeldownload, no originalweight/historicalaudit/queuechange.",
    "Nativeexperimentaltrainingexists; do notclaim GGUF categorically cannottrain. MissingGDNbackward and F32parameterselection describe this source, not allotherframeworks or frozenheadstrategies.",
    "SystemPythonmoduleprobe is scoped; missing modules there do not prove allprivatevenvs absent. A lowparameter frozenbackbone strategy mayfit16GB but is unverified untilactualgraph/step/memoryproof.",
    "Alltraining/quantization variants remain individually conditional and scientificallyOPEN in parentmatrix; this sourceadmission is not a GPUexperiment or winnerqualification."
  ],
  "measurement_type": "SOURCE_CALIBRATION_AND_TRAINING_QUANTIZATION_ADMISSION"
}
```

## Selected aggregate measurements

```json
{
  "actual_GPU_execution": false,
  "new_GPU_runs": 0
}
```
