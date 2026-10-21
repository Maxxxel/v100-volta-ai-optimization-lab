# HBM07 — L1/L2/shared-memory reuse

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| QUALIFIED | True | True | P0 |


## Theory and Volta implications

Persistent conversion or shared/cache reuse can reduce redundant reads and dequantization. It consumes capacity and can change the workload that fits.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-01288096354b4d254f2a.md)
- [Original audit hash and public excerpt](../audits/audit-056d794ebc3542e436de.md)
- [Original audit hash and public excerpt](../audits/audit-14791a89af65ec81443c.md)
- [Original audit hash and public excerpt](../audits/audit-1bcbaa3ce104e67fe6d6.md)
- [Original audit hash and public excerpt](../audits/audit-1f940596d115e34ae02f.md)
- [Original audit hash and public excerpt](../audits/audit-22786f761eb0e7bce306.md)
- [Original audit hash and public excerpt](../audits/audit-22d741ba21637e69bc9a.md)
- [Original audit hash and public excerpt](../audits/audit-2680061ad08d56e324f6.md)
- [Original audit hash and public excerpt](../audits/audit-273b2160c856596f102f.md)
- [Original audit hash and public excerpt](../audits/audit-34aef30f35e398a2b566.md)
- [Original audit hash and public excerpt](../audits/audit-3c1799daa595eea43052.md)
- [Original audit hash and public excerpt](../audits/audit-72561777b6d13a0a47fe.md)
- [Original audit hash and public excerpt](../audits/audit-74211c6727a78a62efe6.md)
- [Original audit hash and public excerpt](../audits/audit-7a9b64a68a7800dd100d.md)
- [Original audit hash and public excerpt](../audits/audit-7be4a096b60529fdd3d1.md)
- [Original audit hash and public excerpt](../audits/audit-7c91d45dc1aa187fe880.md)
- [Original audit hash and public excerpt](../audits/audit-81a482bba6bcc81336a6.md)
- [Original audit hash and public excerpt](../audits/audit-90c23d1af2a59b1df673.md)
- [Original audit hash and public excerpt](../audits/audit-97b2bd9c2d3316dd4eab.md)
- [Original audit hash and public excerpt](../audits/audit-9a720eae0135df096db9.md)
- [Original audit hash and public excerpt](../audits/audit-b4e2008571fcb429d31e.md)
- [Original audit hash and public excerpt](../audits/audit-cad113d219a201e0f5e0.md)
- [Original audit hash and public excerpt](../audits/audit-cc4a0b8610c091844255.md)
- [Original audit hash and public excerpt](../audits/audit-d3d48f461ddbab44a526.md)
- [Original audit hash and public excerpt](../audits/audit-dc120944347a4f5cf410.md)
- [Original audit hash and public excerpt](../audits/audit-e5c8f2e9455ada3d921a.md)
- [Original audit hash and public excerpt](../audits/audit-ec82b4c9401ad086f524.md)
- [Original audit hash and public excerpt](../audits/audit-ef37383ee044d72312b7.md)
- [Original audit hash and public excerpt](../audits/audit-f01e69f875f6c1042276.md)
- [Original audit hash and public excerpt](../audits/audit-fe2e5fbb2e31d1cf8f9f.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | See linked original evidence | Not separately reconciled |
| shared_reuse_patch | BLOCKED | See linked original evidence | Not separately reconciled |


### Recorded model-specific variant coverage

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
      }
    ],
    "model": "omnicoder2"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
      }
    ],
    "model": "qwen35"
  },
  {
    "levels": [
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "shared_reuse_patch"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


## Decision and remaining research

ReuseR219/R220qualifiedagentthroughputgraftxHBM07profile andR207graftmemoryalternative; separateR90prefill/CodingR181/ToolsR183/Energyprofiles retained. Extra6GiBvsqualifiedgraft memoryalternative. No additive speedup or universal quality/state proof. R93native32K independentlyqualifiedbyR221/R222;semanticlongdocumentqualityremainsunverified.

**Remaining scope:** None identified beyond already reviewed evidence; do not automatically repeat.

**Reopening condition:** Nur bei konkret anderer zulässiger Hypothese/technischer Voraussetzung; kein Wiederholen gültiger Belege.

**Next action:** Qualifizierter workloadgebundener Prefill-Cachegewinn bleibt gültig, hoher VRAM und nahezu unverändertes Decode explizit. Kein neu etikettierter Cachetest.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R100](../experiments/R100.md), [R107](../experiments/R107.md), [R108](../experiments/R108.md), [R109](../experiments/R109.md), [R122](../experiments/R122.md), [R123](../experiments/R123.md), [R124](../experiments/R124.md), [R125](../experiments/R125.md), [R126](../experiments/R126.md), [R127](../experiments/R127.md), [R132](../experiments/R132.md), [R133](../experiments/R133.md), [R134](../experiments/R134.md), [R136](../experiments/R136.md), [R141](../experiments/R141.md), [R149](../experiments/R149.md), [R165](../experiments/R165.md), [R166](../experiments/R166.md), [R186](../experiments/R186.md), [R213](../experiments/R213.md), [R214](../experiments/R214.md), [R215](../experiments/R215.md), [R216](../experiments/R216.md), [R217](../experiments/R217.md), [R218](../experiments/R218.md), [R219](../experiments/R219.md), [R220](../experiments/R220.md), [R221](../experiments/R221.md), [R222](../experiments/R222.md), [R251](../experiments/R251.md), [R88](../experiments/R88.md), [R89](../experiments/R89.md), [R90](../experiments/R90.md), [R91](../experiments/R91.md), [R92](../experiments/R92.md), [R93](../experiments/R93.md), [R94](../experiments/R94.md), [R95](../experiments/R95.md)
