# HBM03 — SM70 MMVQ warp mapping

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

MMVQ warp configuration changes work distribution and register pressure. Shape-specific decode paths require actual dispatch evidence.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://docs.nvidia.com/cuda/volta-tuning-guide/index.html
- https://github.com/ggml-org/llama.cpp

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-2e1860757e2916d6fcff.md)
- [Original audit hash and public excerpt](../audits/audit-2e4467cc7d157b5b6514.md)
- [Original audit hash and public excerpt](../audits/audit-39ab6c81075e07c1190b.md)
- [Original audit hash and public excerpt](../audits/audit-b0f72f931a0f006c7f1e.md)
- [Original audit hash and public excerpt](../audits/audit-c915993a806f0b95c0f6.md)
- [Original audit hash and public excerpt](../audits/audit-d9756453b1f9bd997a38.md)
- [Original audit hash and public excerpt](../audits/audit-e2238f64473e0e4d2c93.md)
- [Original audit hash and public excerpt](../audits/audit-ea922ad1c3bfe07b0698.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | CONTROL_INCLUDED | PARTIAL | False |
| warp1 | BLOCKED | TESTED_NEGATIVE | True |
| warp2 | IMPLEMENTED_QUEUED | TESTED_NEGATIVE | True |
| warp4 | BLOCKED | TESTED_NEGATIVE | True |


### Recorded model-specific variant coverage

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
[
  {
    "levels": [
      {
        "historical_states": [
          "CONTROL_INCLUDED"
        ],
        "signed_window_signatures": [],
        "value": "reference"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp1"
      },
      {
        "historical_states": [
          "IMPLEMENTED_QUEUED"
        ],
        "signed_window_signatures": [
          "2b20fc55f5616293f2a4c1359774f71c69c63b8660f884d0e86f96cd232cd27e",
          "5fceca83fc2c6ec81a29513972dc4ef19b63aa8e6ce72a68b8b34b9a87e03c29"
        ],
        "value": "warp2"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp4"
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
        "value": "warp1"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp2"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp4"
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
        "value": "warp1"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp2"
      },
      {
        "historical_states": [
          "BLOCKED"
        ],
        "signed_window_signatures": [],
        "value": "warp4"
      }
    ],
    "model": "qwen38"
  }
]
```

</details>

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant warp1

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decode": {
    "e2e_change_pct": 4.011154970840436,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 0.5671935413597007,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -3.98005576518925,
    "ttft_change_pct": 0.5067566834503934
  },
  "prefill": {
    "e2e_change_pct": 0.6712073243178018,
    "format_pass_change": 0,
    "gpu_energy_change_pct": -0.39585008794362775,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -0.6590941202216483,
    "ttft_change_pct": 0.6625956877915673
  },
  "prefill2048": {
    "e2e_change_pct": 0.1613661487274154,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 0.3359760807019496,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -0.1731717171239877,
    "ttft_change_pct": 0.1753732156551724
  },
  "prefill4096": {
    "e2e_change_pct": 0.08912499355095971,
    "format_pass_change": 0,
    "gpu_energy_change_pct": -0.5112492110042166,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -0.08917245636325122,
    "ttft_change_pct": 0.09202792048879083
  }
}
```

</details>

### Variant warp2

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decode": {
    "e2e_change_pct": 0.12128009397174289,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 1.6071863069079262,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -0.1302360969994476,
    "ttft_change_pct": -0.634261882101117
  },
  "prefill": {
    "e2e_change_pct": -0.1028304560187987,
    "format_pass_change": 0,
    "gpu_energy_change_pct": -3.200843258841246,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": 0.14021576239127143,
    "ttft_change_pct": -0.10369394218420203
  },
  "prefill2048": {
    "e2e_change_pct": -0.1618869813767687,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 0.5962917743690177,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": 0.1542811927474519,
    "ttft_change_pct": -0.1636402453026209
  },
  "prefill4096": {
    "e2e_change_pct": 0.06022565746530706,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 1.383535442937811,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -0.05750158858087717,
    "ttft_change_pct": 0.06042396967467223
  }
}
```

</details>

### Variant warp4

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decode": {
    "e2e_change_pct": -0.29965942091372266,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 1.4204841824257963,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": 0.3321649455577447,
    "ttft_change_pct": 0.5196611430222209
  },
  "prefill": {
    "e2e_change_pct": -0.2758656793980796,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 1.1530259428972123,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": 0.2828346705833873,
    "ttft_change_pct": -0.27469332417936476
  },
  "prefill2048": {
    "e2e_change_pct": -0.2573099566567594,
    "format_pass_change": 0,
    "gpu_energy_change_pct": -0.10513028887507714,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": 0.2571840160999761,
    "ttft_change_pct": -0.2555561320758182
  },
  "prefill4096": {
    "e2e_change_pct": -0.49032272272990785,
    "format_pass_change": 0,
    "gpu_energy_change_pct": -0.24810571889886113,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": 0.491929689520787,
    "ttft_change_pct": -0.49101868840329965
  }
}
```

</details>

## Decision and remaining research

Warp1: Decode -3,98%; Warp4: +0,33%, kein praktischer Vorteil. Warp2 ändert Q6-Spalten2/4 von4 auf2Warps; Q6-Decode(n1) bleibt2/2. Original-QA Warp2 verliert Zeit-Aufgabe in beiden B-Starts (18→16/24 semantisch,16→14/24 Format). Kein Gewinner.

**Remaining scope:** Nur eine tatsächlich neue Form-/Register-/Layout- oder Dispatchhypothese mit unveränderter Qualität rechtfertigt erneuten MMVQ-Test; Warp1/2/4 nicht erneut messen. Fehlende dynamische Spilling-/Occupancycounter nicht aus Launchtraces schätzen.

**Reopening condition:** A distinct MMVQ design must address register/occupancy or dispatch cost and pass numerical plus unchanged-quality checks; no renamed warp2 retry.

**Next action:** Vorhandene Warp-Negativbefunde nutzen; neuer Kernel benötigt eigenständigen Quelldiff und Numerikorakel.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R348](../experiments/R348.md), [R391](../experiments/R391.md)
