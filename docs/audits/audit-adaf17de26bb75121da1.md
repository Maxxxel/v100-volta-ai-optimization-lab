# Public audit excerpt

Original SHA256: `adaf17de26bb75121da159b04123bacbf5498d6b4b63d5a6cbaa95bfebe40753`

Original file: `AUDIT.json`; 12529 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "SAMPLED_Q6_PROJECTION_NUMERICALLY_QUALIFIED",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "CPUdoublechecks16of2048 predeterminedcolumns acrossall4096rows; fulltwoGPUmatrices compared, notallCPUreferencecolumnscomputed",
    "ExactretainedR85 Q6matrix, extendedsyntheticF32activations; notrealmodelweights orcapturedmodelactivations",
    "GPUallocation/graphs/profiler apply tooperatoronly; no performance ranking or fullmodel causalproof",
    "R95 remainsunqualified; no retroactive relaxation or championpromotion"
  ]
}
```

</details>

## Selected aggregate measurements

NOT MEASURED / not included in the approved public schema.
