# BMT01 — Minimal tool-schema descriptions

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| TESTED_NEGATIVE | True | True | P0 |


## Theory and Volta implications

This research subcase investigates minimal tool-schema descriptions. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Function serialization and descriptions change token count and ambiguity. Faster compressed schemas can cause wrong tool selection.; Harness compression reduces context tokens but can alter tool semantics. Preserve structured data and evaluate complete tasks.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://huggingface.co/datasets/hkust-nlp/Toolathlon
- https://huggingface.co/tsinghua-sigs-robot-lab/VeriLoop-E2

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-acd0d0a644cf194577a3.md)
- [Original audit hash and public excerpt](../audits/audit-e7e6febdba552a313117.md)

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

R191 retained18/18full vs11/18compact; R195 distinctinstruction lost2prior BFCLsuccesses. No answer-specific schema tuning.

**Remaining scope:** Getestete negative Behandlung nicht wiederholen; keine pauschale Ablehnung aller Varianten.

**Reopening condition:** Eine sachlich neue selektive Kürzungsregel mit unabhängig eingefrorenen Verwechslungsfällen; bisherige Blanket-/Kurztemplate-Negative nicht nachstimmen.

**Next action:** Eine sachlich neue selektive Kürzungsregel mit unabhängig eingefrorenen Verwechslungsfällen; bisherige Blanket-/Kurztemplate-Negative nicht nachstimmen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R191](../experiments/R191.md), [R195](../experiments/R195.md)
