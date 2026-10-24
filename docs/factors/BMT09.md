# BMT09 — KV rotation and mean centering

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| TESTED_NEGATIVE | True | True | P1 |


## Theory and Volta implications

This research subcase investigates kv rotation and mean centering. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Quantizing attention keys reduces KV storage but adds conversion and changes attention scores. It does not quantize the separate GDN recurrent state.; Quantizing attention values reduces KV storage but changes the attention value product. Its error behavior differs from key quantization.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://arxiv.org/abs/2402.02750
- https://github.com/PrismML-Eng/Bonsai-demo/blob/db871ea96bffff5ce5609873c412b75d7cd5ba3c/community-benchmarks/bonsai2/cuda-tesla-v100-windows.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-a2270317169dec422f24.md)
- [Original audit hash and public excerpt](../audits/audit-fae4b1903a527efdd0b8.md)

### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Existingrotationpreviouslyalreadyactivecorrected;K/VrotationOFF<3%gain. ExistingforkQ4centeringpathadmitted/actual8layerOmniGPUcalibrationandload,butindependentfrozengradershowssortinglossafter8cases. Noperformanceclaim/noR269time-restorationclaim. CorpusretuningonfailedQAforbidden;otherstudiesP2deferredabsentpracticalKVcapacityneed.

**Remaining scope:** AndereKalibrierkorpora/volleKLD-/KontextstudienP2zurückgestellt: aktuelleVarianteverliertungeänderteQualität;keinNachkalibrierenaufbekannteFehler/keinbelegterKV-KapazitätsengpassimZielprofil.

**Reopening condition:** Andere vorab begründete Kalibration plus unabhängige Aufgaben; keine Nachkalibration auf R269/R270-Fehler. Bestehende KV-Rotations-/Centering-Screens nicht wiederholen.

**Next action:** Andere vorab begründete Kalibration plus unabhängige Aufgaben; keine Nachkalibration auf R269/R270-Fehler. Bestehende KV-Rotations-/Centering-Screens nicht wiederholen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R270](../experiments/R270.md)
