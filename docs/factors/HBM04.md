# HBM04 — SM70 MMQ tiles and warps

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

MMQ tile width changes reuse, occupancy and resource pressure. Comparisons with common forced routing do not represent stock routing.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://raw.githubusercontent.com/KumphanartDansiri/v100-vllm-2026/295b5bd547edb07c9de0b58b7c98aaacfac8ec30/docs/02_fp16_moe_fix.md
- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/vllm_serve.py

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-13974d59b8cc476497a5.md)
- [Original audit hash and public excerpt](../audits/audit-76529acdcbe759e8bcab.md)
- [Original audit hash and public excerpt](../audits/audit-f96908ff12c1e106761e.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | BLOCKED | PARTIAL | False |
| tile_patch | BLOCKED | TESTED_NEGATIVE | True |


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
        "value": "tile_patch"
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
        "value": "tile_patch"
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
        "value": "tile_patch"
      }
    ],
    "model": "qwen38"
  }
]
```

Historical states and window signatures are evidence links, not qualification of every model/variant.

## Available results

Values, baseline/candidate comparisons, model/engine identity and limits are in the linked audit excerpts and profile records. Missing measurements are **NOT MEASURED**. Existing native screens are not HumanEval, BFCL or full-agent qualifications.


### Variant tile_patch

```json
{
  "decode": {
    "e2e_change_pct": -0.05160119064760993,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 0.3005812727121082,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": 0.005428694014275592,
    "ttft_change_pct": -0.3540009960232626
  },
  "prefill": {
    "e2e_change_pct": 13.23198876518985,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 14.307923681761858,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -11.731084239527046,
    "ttft_change_pct": 13.255340934061666
  },
  "prefill2048": {
    "e2e_change_pct": 14.256760368387344,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 15.247297579111919,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -12.487223841314233,
    "ttft_change_pct": 14.25746229077185
  },
  "prefill4096": {
    "e2e_change_pct": 14.58417710236155,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 14.756058205133682,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "tokens_per_s_change_pct": -12.737309300765798,
    "ttft_change_pct": 14.58766020600728
  }
}
```

## Decision and remaining research

HBM04teiltC10-BelegefürJ-Caps64/32untergemeinsamForced-MMQRounting; beidePrefilllangsamer. KeinseparaterWarp-/TileI-/SharedMemory-TestdurchdieseZuordnung. KeineweitereMessungoderzweiterSpeedup.

**Remaining scope:** R353/C10gültigeJ-Cap-Negativbefundewiederverwenden. WirklichanderesWarp-/TilemappingbenötigtSource-/Register-/SharedMemory-Zulassung,SM70DispatchundNumerik/Tails. KeineumbenannteCap64/32-Wiederholung.

**Reopening condition:** A different SM70 tile/warp mapping needs register/shared-memory feasibility, actual dispatch and numerical tails before B-screen.

**Next action:** R353/C10gültigeJ-Cap-Negativbefundewiederverwenden. WirklichanderesWarp-/TilemappingbenötigtSource-/Register-/SharedMemory-Zulassung,SM70DispatchundNumerik/Tails. KeineumbenannteCap64/32-Wiederholung.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R355](../experiments/R355.md)
