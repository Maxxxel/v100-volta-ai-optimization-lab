# HBM17 — Speculative decoding memory traffic

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

MTP proposes tokens with model-compatible prediction heads. State rollback and target verification must be tested; do not assume identical decisions.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-005e431f9699e2f9139e.md)
- [Original audit hash and public excerpt](../audits/audit-058f7fb472328b4ccdee.md)
- [Original audit hash and public excerpt](../audits/audit-0f287160bf817b3ca016.md)
- [Original audit hash and public excerpt](../audits/audit-0ff1930c5d4878017f54.md)
- [Original audit hash and public excerpt](../audits/audit-126955c25fb6d48bafda.md)
- [Original audit hash and public excerpt](../audits/audit-14791a89af65ec81443c.md)
- [Original audit hash and public excerpt](../audits/audit-1e481b9ad01b4b62af21.md)
- [Original audit hash and public excerpt](../audits/audit-1f940596d115e34ae02f.md)
- [Original audit hash and public excerpt](../audits/audit-21267142b49cd147290a.md)
- [Original audit hash and public excerpt](../audits/audit-22d741ba21637e69bc9a.md)
- [Original audit hash and public excerpt](../audits/audit-29320e8e583d52eb5f20.md)
- [Original audit hash and public excerpt](../audits/audit-2cc154e4c127f0906ae0.md)
- [Original audit hash and public excerpt](../audits/audit-3bbcbd54e7cb734a5ce0.md)
- [Original audit hash and public excerpt](../audits/audit-4074703750eba42f8b7f.md)
- [Original audit hash and public excerpt](../audits/audit-429e93ed0d4b5e650ef5.md)
- [Original audit hash and public excerpt](../audits/audit-4376616d031747b32c87.md)
- [Original audit hash and public excerpt](../audits/audit-483d9caa91ea1c956079.md)
- [Original audit hash and public excerpt](../audits/audit-4af664a242392bba07e2.md)
- [Original audit hash and public excerpt](../audits/audit-4ed8d00dfd5d86541176.md)
- [Original audit hash and public excerpt](../audits/audit-4f9c259520d274f056b6.md)
- [Original audit hash and public excerpt](../audits/audit-5a6acf8414af5ba4fef9.md)
- [Original audit hash and public excerpt](../audits/audit-5cd1753822f1c6a3c06d.md)
- [Original audit hash and public excerpt](../audits/audit-62ba042a766f67beec9f.md)
- [Original audit hash and public excerpt](../audits/audit-642fa8e7d42cda1f1762.md)
- [Original audit hash and public excerpt](../audits/audit-683c5d2a873df7e2c3ce.md)
- [Original audit hash and public excerpt](../audits/audit-74d034ef6a5873b4a5e9.md)
- [Original audit hash and public excerpt](../audits/audit-7ac0039875dbca1d0b67.md)
- [Original audit hash and public excerpt](../audits/audit-7c91d45dc1aa187fe880.md)
- [Original audit hash and public excerpt](../audits/audit-81a482bba6bcc81336a6.md)
- [Original audit hash and public excerpt](../audits/audit-8788e59c2be22318680e.md)
- [Original audit hash and public excerpt](../audits/audit-8b0a5f586ab7c4916cc8.md)
- [Original audit hash and public excerpt](../audits/audit-90c23d1af2a59b1df673.md)
- [Original audit hash and public excerpt](../audits/audit-943484dd7722dbde7820.md)
- [Original audit hash and public excerpt](../audits/audit-9570ac8fc6dfdcbfd5ed.md)
- [Original audit hash and public excerpt](../audits/audit-9a720eae0135df096db9.md)
- [Original audit hash and public excerpt](../audits/audit-9dda8d7330e18ec39f99.md)
- [Original audit hash and public excerpt](../audits/audit-b27b25417f2e056a1b90.md)
- [Original audit hash and public excerpt](../audits/audit-b43d241215ca8c84c3c2.md)
- [Original audit hash and public excerpt](../audits/audit-c70de178e95e5c46203d.md)
- [Original audit hash and public excerpt](../audits/audit-c7ca0d0405f4d0cdcb9f.md)
- [Original audit hash and public excerpt](../audits/audit-c7cd773e3f897f934e45.md)
- [Original audit hash and public excerpt](../audits/audit-cad113d219a201e0f5e0.md)
- [Original audit hash and public excerpt](../audits/audit-cf094fc512d83c5c3636.md)
- [Original audit hash and public excerpt](../audits/audit-d409fb639593d5c459a5.md)
- [Original audit hash and public excerpt](../audits/audit-d87732dab7205ef6b52e.md)
- [Original audit hash and public excerpt](../audits/audit-dffb404b82747d32d666.md)
- [Original audit hash and public excerpt](../audits/audit-e5c8f2e9455ada3d921a.md)
- [Original audit hash and public excerpt](../audits/audit-f28dcaeb906ada4b945b.md)
- [Original audit hash and public excerpt](../audits/audit-f342d89e541599ff11aa.md)
- [Original audit hash and public excerpt](../audits/audit-f681d1b3ad53e12ab335.md)
- [Original audit hash and public excerpt](../audits/audit-f6ede40a69a9cd5a74b3.md)
- [Original audit hash and public excerpt](../audits/audit-f966ff96cd7e62ab7c38.md)
- [Original audit hash and public excerpt](../audits/audit-fb076ec1a01a891d9edb.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| off | BLOCKED | See linked original evidence | Not separately reconciled |
| ngram_simple | BLOCKED | See linked original evidence | Not separately reconciled |
| ngram_mod | BLOCKED | See linked original evidence | Not separately reconciled |


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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
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
        "value": "off"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_simple"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "ngram_mod"
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

Speculation acceptance and GPU energy are observed, but accepted-token counts do not measure physical HBM traffic.

**Remaining scope:** A new traffic optimization needs actual reused/avoided tensor reads plus equivalent verification and rollback; hardware-counter metrics must be eligible on SM70.

**Reopening condition:** A new traffic optimization needs actual reused/avoided tensor reads plus equivalent verification and rollback; hardware-counter metrics must be eligible on SM70.

**Next action:** Retain S01/S02/S03 measured scopes; do not add an independent HBM speedup for the same MTP treatment.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R159](../experiments/R159.md), [R171](../experiments/R171.md), [R172](../experiments/R172.md), [R173](../experiments/R173.md), [R174](../experiments/R174.md), [R175](../experiments/R175.md), [R176](../experiments/R176.md), [R177](../experiments/R177.md), [R178](../experiments/R178.md), [R179](../experiments/R179.md), [R180](../experiments/R180.md), [R181](../experiments/R181.md), [R182](../experiments/R182.md), [R183](../experiments/R183.md), [R184](../experiments/R184.md), [R185](../experiments/R185.md), [R186](../experiments/R186.md), [R200](../experiments/R200.md), [R201](../experiments/R201.md), [R202](../experiments/R202.md), [R203](../experiments/R203.md), [R204](../experiments/R204.md), [R205](../experiments/R205.md), [R206](../experiments/R206.md), [R207](../experiments/R207.md), [R208](../experiments/R208.md), [R209](../experiments/R209.md), [R210](../experiments/R210.md), [R211](../experiments/R211.md), [R212](../experiments/R212.md), [R213](../experiments/R213.md), [R214](../experiments/R214.md), [R215](../experiments/R215.md), [R216](../experiments/R216.md), [R217](../experiments/R217.md), [R218](../experiments/R218.md), [R219](../experiments/R219.md), [R220](../experiments/R220.md), [R235](../experiments/R235.md), [R236](../experiments/R236.md), [R244](../experiments/R244.md), [R245](../experiments/R245.md), [R246](../experiments/R246.md)
