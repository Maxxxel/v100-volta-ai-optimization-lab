# BMT06 — Agent harness and bounded recovery

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P1 |


## Theory and Volta implications

This research subcase investigates agent harness and bounded recovery. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Harness compression reduces context tokens but can alter tool semantics. Preserve structured data and evaluate complete tasks.; Planning/reflection loops trade extra generation for recovery. Evaluate additional successful tasks per second and joule, including failures.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B
- https://huggingface.co/datasets/benchflow/skillsbench
- https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2
- https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2/blob/44b6f230347f9ccf2a5ce96a44bcd74ecaaaa51f/README.md

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-4912e9ed03c1c3a64139.md)
- [Original audit hash and public excerpt](../audits/audit-b8f8679e9ce0cb9301a6.md)
- [Original audit hash and public excerpt](../audits/audit-fb4096705054d7be1534.md)

### Recorded model-specific variant coverage

```json
[]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

Gültigen Negativbefund übernehmen; weder dieselben5 Fälle nachoptimieren noch einen vollen Kontrolllauf starten. Andere History-/Skill-Verfahren brauchen eine neue, semantisch und funktional begründete Behandlung. Privates VeriLoop-Rezept nicht verfügbar; keine Kausalbehauptung zu dessen Benchmarkrang.

**Remaining scope:** Gültigen Negativbefund übernehmen; weder dieselben5 Fälle nachoptimieren noch einen vollen Kontrolllauf starten. Andere History-/Skill-Verfahren brauchen eine neue, semantisch und funktional begründete Behandlung.

**Reopening condition:** Neue Recovery-/Skill-Policy mit unabhängigem Aufgaben-/Effektvertrag; CPU-Retry-Komponente und negativer GPU-History-Test sind verschiedene Belege.

**Next action:** Neue Recovery-/Skill-Policy mit unabhängigem Aufgaben-/Effektvertrag; CPU-Retry-Komponente und negativer GPU-History-Test sind verschiedene Belege.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R240](../experiments/R240.md), [R243](../experiments/R243.md)
