# BMT17 — SM70 graphs and GDN fusion

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

This research subcase investigates sm70 graphs and gdn fusion. It is a distinct technique hypothesis, not proof that any source model uses it or that it improves Volta inference. Related mechanisms: Compiling CUDA Graph support can reduce repeated launch overhead. Correct capture, replay and state lifecycle must be distinguished from graph optimization settings.; Graph optimization policy is distinct from enabling CUDA Graphs. A flag value alone does not prove optimized nodes or a replay-time improvement.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-dc8a8b9d5095ace488a2.md)

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

ExistingC03/C04/C11/C12/C13/HBM18 andR81 evidence retained. No new specific semantically equivalent SM70 graph/fusionpatch or causal profile bottleneck admitted; do not rebuild/rename tested kernels.

**Remaining scope:** Offenen Rest auf einen konkreten sinnvollen Einzelversuch prüfen; bestehende Messungen erhalten.

**Reopening condition:** Konkreter noch nicht getesteter semantisch äquivalenter Graph-/Fusion-Patch mit ausgeführtem Pfad und Profilinghypothese; C03/C04/C11/C12/C13 nicht umbenennen.

**Next action:** Konkreter noch nicht getesteter semantisch äquivalenter Graph-/Fusion-Patch mit ausgeführtem Pfad und Profilinghypothese; C03/C04/C11/C12/C13 nicht umbenennen.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R194](../experiments/R194.md)
