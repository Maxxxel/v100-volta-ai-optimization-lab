# HBM02 — Coalesced and vectorized accesses

| Scientific status | Experimental coverage | OmniCoder2 coverage | Priority |
|---|---|---|---|
| PARTIAL | True | True | P2 |


## Theory and Volta implications

Aligned vector loads can reduce instructions, but actual pointer alignment, tails, register pressure and fallback paths must be checked.

On SM70, require an actually dispatched compatible kernel and include conversion, workspace, launch and verification costs. The 16 GB budget includes weights, attention KV, recurrent states, graph pools and transient allocations. Quality, end-to-end latency and energy per successful task take precedence over a token-throughput screen.

## Scientific background

- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/fp8_dequant.cu
- https://raw.githubusercontent.com/KumphanartDansiri/vllm-fp8-w8a16-sm70/9e1aa6bc3398c5ea823a80027963709d20ee1974/src/fp8_w8a16_sm70/turbomind_fp8_backend.py

These are source links or general implementation background, not local speedup evidence. The source registry records pinned revisions where available. Bibliographic fields not recorded by the source review are not fabricated.

## Implementation and evidence

Relevanter OmniCoder2-/SM70-Modell- oder numerischer Komponentenpfad; kein Beweis vollständiger Achsenabdeckung.

- [Original audit hash and public excerpt](../audits/audit-0c85f6a8fd53d28ec35e.md)
- [Original audit hash and public excerpt](../audits/audit-13974d59b8cc476497a5.md)
- [Original audit hash and public excerpt](../audits/audit-c915993a806f0b95c0f6.md)

| Original variant | Signed historical state | Reviewed scoped status | Hardware coverage in this variant |
|---|---|---|---|
| reference | CONTROL_INCLUDED | PARTIAL | False |
| aligned_vector_patch | IMPLEMENTED_QUEUED | TESTED_NEGATIVE | True |


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
          "IMPLEMENTED_QUEUED"
        ],
        "signed_window_signatures": [
          "346d46a94496cc919da27bbc16243ebd0fa4da47a057ad63834b21525bca0521"
        ],
        "value": "aligned_vector_patch"
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
        "value": "aligned_vector_patch"
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
        "value": "aligned_vector_patch"
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


### Variant aligned_vector_patch

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decode": {
    "e2e_change_pct": 10.349218897638934,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 3.015319361163926,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -9.33148042493489,
    "ttft_change_pct": 11.580407457420794
  },
  "prefill": {
    "e2e_change_pct": 4.21987954080032,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 5.076844290198945,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -4.074422864850713,
    "ttft_change_pct": 4.206442793338705
  },
  "prefill2048": {
    "e2e_change_pct": 1.078757297830224,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 2.4484685370262493,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -1.0835032334954087,
    "ttft_change_pct": 1.0826750803922813
  },
  "prefill4096": {
    "e2e_change_pct": 0.7250944790446967,
    "format_pass_change": 0,
    "gpu_energy_change_pct": 0.53013147963894,
    "same_token_counts": true,
    "semantic_pass_change": 0,
    "throughput_comparison_eligible": true,
    "tokens_per_s_change_pct": -0.720887641543011,
    "ttft_change_pct": 0.7259343322720602
  }
}
```

</details>

## Decision and remaining research

HBM02:SM70Q6ql/qh ausgerichtete32-Bit-Loads mit16-Bit-Fallback wirklichgetestet. 3072Device-Loadfälle:0Fehler,B1536aligned/1536Fallback;96CPUreferenz-Matmul-FällejeA/Bbestanden. OmniDecode−9,33%,2K/4KLatenz+1,08/+0,73%,7356,5MiBbeide. KeinGewinn,keine128Bit-Vektorisierungs-/HBMBandbreitenbehauptung.

**Remaining scope:** Genaugetesteteu32/FallbackVarianteverwerfen,nichtneuauflagen. AndereLoadbreite/LayoutnurmitkonkretemabweichendemSM70-Instruction-/Alignmentpfad,Odd-Tail/Stride-NumerikundplausiblemNutzen. KeineSASS-/Register-/OccupancyursacheausQuelltextschätzen; heutigerNachbauohnealteObjektewäreeineneueBuildfrage,nichtGrundzumBenchmarkretry.

**Reopening condition:** A different load instruction/alignment treatment, actual SM70 disassembly and an unaligned/tail-safe numerical oracle are needed for any new vectorization candidate.

**Next action:** Genaugetesteteu32/FallbackVarianteverwerfen,nichtneuauflagen. AndereLoadbreite/LayoutnurmitkonkretemabweichendemSM70-Instruction-/Alignmentpfad,Odd-Tail/Stride-NumerikundplausiblemNutzen. KeineSASS-/Register-/OccupancyursacheausQuelltextschätzen; heutigerNachbauohnealteObjektewäreeineneueBuildfrage,nichtGrundzumBenchmarkretry.

These canonical rationale excerpts preserve the original language. Potential combinations require independently qualified constituents and fresh interaction controls. Transfer to another model requires compatible architecture, weights, tokenizer, state layout and engine dispatch.

## Related sprint records

[R355](../experiments/R355.md), [R391](../experiments/R391.md)
