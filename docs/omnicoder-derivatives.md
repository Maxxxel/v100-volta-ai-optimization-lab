# OmniCoder derivatives: evidence and proposed tests

**Research inventory, not a model leaderboard.** Source publication, CPU weight differences, GPU compatibility and independently measured quality are separate gates. No candidate on this page has a new local GPU benchmark or qualification. [Measured configurations](configuration-comparison.md) retain their original scores and identities.

Review: `OMNICODER_DERIVATIVES_20261023` · 2026-10-23T17:39:39.466207+00:00. Bounded public HuggingFace name search, baseline relation filters, author andlinked-repository discovery; no claim to enumerate untagged/private/deleted models worldwide. Quantizations and reuploads are not new trained checkpoints.

| Inventory item | Count / meaning |
| --- | --- |
| Name-search hits | 86 |
| Distinct inventoried repositories | 105 |
| Pinned source metadata files | 542 |
| Coding proposals | 3 |
| New GPU measurements / quality qualifications | 0 / 0 |
| Counter scope | Repositories are not trained checkpoints, optimization factors, model challengers or GPU runs. The existing 162 factors and 11 challenger tracks are unchanged. |

The retained **OmniCoder 9B** baseline has byte-identical typed Q6_K payloads across all 427 tensors in the compared mradermacher V1/V2 artifacts, despite different file metadata and hashes. [Original complete comparison](weight-integrity-same-quantizer.md). This finding is specific to those quantized artifacts and does not prove training history for every source release. New derivative names and different file hashes are never sufficient evidence of a new fine-tune.

## Coding shortlist — research priority only

No quality ordering is established. Readiness, provenance, coding relevance and additional information per bounded experiment determine this order. No model should be rejected on an unmeasured quality claim or an output-format/configuration mistake.

| Priority | Pinned Q6 artifact | Why investigate | Local quality / cost |
| --- | --- | --- | --- |
| 1 | [prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF](https://huggingface.co/prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF/blob/330ab686d7784f9b21f553727635efceeb8562e7/README.md) | Merge of coding parents is directly relevant; readyQ6; changed same-dtype source values. No published target score, so this is an evidence/readiness order, not a predicted quality rank. | NOT MEASURED |
| 2 | [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | More explicit training/adapter/log evidence and an efficiency hypothesis with disclosed accuracy cost. Newer-runtime loader behavior remains an admission question. | NOT MEASURED |
| 3 | [mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF](https://huggingface.co/mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF/blob/942ac32ed196d167f90c97aa9aa2a346f4401bf9/README.md) | Changed BF16 source values and readyQ6. Teacher/dataset/training provenance is weak; test the artifact, not its name. | NOT MEASURED |

[Complete repository inventory](model-research/omnicoder-inventory.md) · [Proposed configurations and gated test plan](model-research/omnicoder-proposals.md)

## Six requested seed models

### armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill

[armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill](https://huggingface.co/armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill/blob/c009a9384d2f9792e62c71e0aedd1381151f960f/README.md) · revision `c009a9384d2f9792e62c71e0aedd1381151f960f` · DECLARED_FINETUNE · license: apache-2.0.

**Decision:** TEST_IF_APPROVED. Same-dtype source probes confirm changed values. The card is generic Unsloth metadata; teacher, dataset, loss and exact training base revision are not documented. Q6 GGUF header matches expected qwen35 layout; native tool-template differs from base.

Method evidence: `DECLARED_FINETUNE_DISTILLATION_RECIPE_UNDISCLOSED`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

### prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF

[prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF](https://huggingface.co/prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF/blob/330ab686d7784f9b21f553727635efceeb8562e7/README.md) · revision `330ab686d7784f9b21f553727635efceeb8562e7` · QUANTIZATION_OR_CONVERSION_EXPORT · license: apache-2.0.

**Decision:** TEST_IF_APPROVED. Four named coding parents and reproducible-looking merge flags are published; source probes show changes. Exact parent revisions and independent coding/tools results are absent; no additive parent capability claim.

Method evidence: `MERGE_EXPORT_WITH_PARENT_RECIPE`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

### wheattoast11/OmniCoder-9B-Zero-Phase1

[wheattoast11/OmniCoder-9B-Zero-Phase1](https://huggingface.co/wheattoast11/OmniCoder-9B-Zero-Phase1/blob/57214e22fe52dda598cd078de15f60a3f8be68a3/README.md) · revision `57214e22fe52dda598cd078de15f60a3f8be68a3` · LORA_ADAPTER · license: UNRESOLVED.

**Decision:** DEFER_PENDING_LICENSE_BASE_MAPPING. Nonzero rank64 adapter delta observed. Model card says GRPO; exact parent revision is null, keys use a text-wrapper layout, artifact license is not explicitly supplied and no official benchmark is reported.

Method evidence: `GRPO_LORA_DECLARED`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

### wheattoast11/OmniCoder-9B-Zero-Phase1-SFT

[wheattoast11/OmniCoder-9B-Zero-Phase1-SFT](https://huggingface.co/wheattoast11/OmniCoder-9B-Zero-Phase1-SFT/blob/b84da1b9904c15bc25c8e15843afa4a8d426a441/README.md) · revision `b84da1b9904c15bc25c8e15843afa4a8d426a441` · LORA_ADAPTER · license: UNRESOLVED.

**Decision:** DEFER_PENDING_LICENSE_BASE_MAPPING. Nonzero rank64 adapter delta observed. Card says SFT, but exact training base revision, complete data recipe, explicit artifact license and official benchmark evidence are missing.

Method evidence: `SFT_LORA_DECLARED`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

### wheattoast11/OmniCoder-9B-Zero-Phase2

[wheattoast11/OmniCoder-9B-Zero-Phase2](https://huggingface.co/wheattoast11/OmniCoder-9B-Zero-Phase2/blob/2fbc076a7604514bac9183ee679b8ea077f2ce58/README.md) · revision `2fbc076a7604514bac9183ee679b8ea077f2ce58` · LORA_ADAPTER · license: apache-2.0.

**Decision:** SEPARATE_GUI_FEASIBILITY_PLAN. Nonzero adapter delta observed, all inspected keys are language modules; base VLM plus processor is required. Card names an SFT substrate but adapter config names the raw base without a revision. 94.61% on167 samples is a publisher-specific GUI evaluation, not BFCL/agent qualification.

Method evidence: `VISION_GRPO_LORA_DECLARED`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

### tianrui6641/OmniCoder-HDL-9B

[tianrui6641/OmniCoder-HDL-9B](https://huggingface.co/tianrui6641/OmniCoder-HDL-9B/blob/aed9d0429b0b3658380610b5552daa3d0c208822/README.md) · revision `aed9d0429b0b3658380610b5552daa3d0c208822` · DECLARED_FINETUNE · license: apache-2.0.

**Decision:** OBSERVE_DOMAIN_SPECIALIST. Changed BF16 source values are observed. Generic card supplies no HDL task set, training recipe or standardized HDL score. Published Q5/Q4/Q8 GGUFs exist, no Q6 in this pinned own quant repo. Image-text tagging is not visual-function qualification.

Method evidence: `FINETUNE_HDL_SPECIALIZATION_UNVERIFIED`. Exact historical training/base revision: NOT RECORDED. Published base tags are not historical training provenance.

## Locally observed CPU weight evidence

**LOKAL GEMESSEN / LOCALLY MEASURED, CPU ONLY.** Matching BF16 source samples differ for Claude-distill, Nexus upstream and HDL; nonzero low-rank products are observed in three adapters. These observations disprove identity at the probed positions. A conversion or rounding round trip can also change same-dtype values: a difference alone proves neither training history nor quality. Unchanged sampled positions cannot establish full-model identity. The inspected GGUF headers are not quantized-payload comparisons or complete-file SHA verification. Small source changes can disappear under quantization.

| Source / adapter | Bounded observation | Compared scope | Limit |
| --- | --- | --- | --- |
| armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill | DIFFERENT_SAME_FORMAT_VALUES_OBSERVED | 1536 | Not a complete tensor census; no quality claim |
| tianrui6641/OmniCoder-HDL-9B | DIFFERENT_SAME_FORMAT_VALUES_OBSERVED | 1536 | Not a complete tensor census; no quality claim |
| prithivMLmods/Nexus-9B-CodeCore-Merge | DIFFERENT_SAME_FORMAT_VALUES_OBSERVED | 1536 | Not a complete tensor census; no quality claim |
| wheattoast11/OmniCoder-9B-Zero-Phase1 | NONZERO_ADAPTER_EFFECTIVE_DELTA_OBSERVED | 128 | Not a complete tensor census; no quality claim |
| wheattoast11/OmniCoder-9B-Zero-Phase1-SFT | NONZERO_ADAPTER_EFFECTIVE_DELTA_OBSERVED | 128 | Not a complete tensor census; no quality claim |
| wheattoast11/OmniCoder-9B-Zero-Phase2 | NONZERO_ADAPTER_EFFECTIVE_DELTA_OBSERVED | 128 | Not a complete tensor census; no quality claim |

The independent standard-library replay checked 62 fragment hashes, 18 source-sample pairs and 3 low-rank blocks. Numerical probes and structural summaries are available in the public benchmark register; raw weight fragments, templates and foreign code are not redistributed.

| Source | Header tensor count | Parameter count in source headers | Dtypes |
| --- | --- | --- | --- |
| Tesslate/OmniCoder-9B | 760 | 9409813744 | {'BF16': 760} |
| armand0e/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill | 760 | 9409813744 | {'BF16': 760} |
| tianrui6641/OmniCoder-HDL-9B | 760 | 9409813744 | {'BF16': 760} |
| prithivMLmods/Nexus-9B-CodeCore-Merge | 775 | 9653104368 | {'BF16': 727, 'F32': 48} |
| wheattoast11/OmniCoder-9B-Zero-Phase1 | 256 | 116391936 | {'BF16': 256} |
| wheattoast11/OmniCoder-9B-Zero-Phase1-SFT | 256 | 116391936 | {'BF16': 256} |
| wheattoast11/OmniCoder-9B-Zero-Phase2 | 256 | 116391936 | {'F32': 256} |

## V100 and deployment compatibility

| Selected GGUF | Architecture / layers | Tensor formats | MTP tensors | Actual GPU load / VRAM |
| --- | --- | --- | --- | --- |
| mradermacher/OmniCoder-9B-Claude-Opus-High-Reasoning-Distill-GGUF | qwen35 / 32 | {'F32': 177, 'Q6_K': 250} | 0 | NOT MEASURED |
| prithivMLmods/Nexus-9B-CodeCore-Merge-GGUF | qwen35 / 32 | {'F32': 177, 'Q6_K': 250} | 0 | NOT MEASURED |
| Kukedlc/Slopus-9B | qwen35 / 32 | {'F32': 177, 'Q6_K': 250} | 0 | NOT MEASURED |

```json
{
  "FP16_compute": "Supported Volta path; do not assume nativeBF16/FP8/FP4 TensorCores. Training examples on newer hardware are not local inference evidence.",
  "GPU": "TeslaV100-SXM2-16GB",
  "KV_8K_F16_analytical_bytes": 268435456,
  "KV_estimate_limit": "Architecture-derived attention KV only. Not a VRAM measurement; GDN state, checkpoint/rollback copies, CUDA/workspaces, weights and image projector are additional.",
  "MTP": "Selected3GGUFs have0MTP-named tensors. ExternalQwen head use might be possible but requires per-target tokenizer/state/quality/acceptance qualification; do not transferR179success automatically.",
  "compute_capability": "7.0",
  "device_total_MiB": 16384,
  "existing_broker_VRAM_limit_MiB": 14336,
  "max_context": "262144 declared in inspectedGGUFs, not usable capacity established on16GB. Proposed8K is a planning constraint, not measured quality.",
  "new_models_actual_VRAM": "NOT MEASURED"
}
```

All three inspected text GGUFs have 427 tensors (250 Q6_K, 177 F32), 32 layers and no MTP-named tensors. Declared 262144 context is metadata, not established usable capacity on 16GB. Selected Q6 artifacts are about 7.36GB on disk; **file size is not peak VRAM**. FP16 compute and compatible quantized weights are the intended SM70 route; no native BF16/FP8/FP4 Tensor Core assumption. External MTP needs its own tokenizer/state/acceptance/quality qualification for each target.

The GUI adapter has no vision-named adapter tensors; this does not disprove multimodality, because a frozen visual tower can be reused. It also does not demonstrate an executable screenshot path. Exact raw-base versus Vision-SFT-substrate composition, image processor, vision tower, merge/key mapping and matching projector remain unresolved. Text GGUF alone does not read screenshots. HDL remains a domain specialist without an established local HDL score.

## Published claims — external, not our benchmark results

**EXTERN BELEGT** here means the publisher statement is traceable to a pinned card; the stated training execution and benchmark quality are not independently reproduced. Missing revisions, scorers and task identities prevent direct comparison. Copied parent-model tables are not attributed as child-model measurements. No value below enters the official local leaderboard or the user-selected local average.

| Publisher model / source | Reported evaluation | Score % | Baseline % if stated | Tasks | Known limits |
| --- | --- | --- | --- | --- | --- |
| [wheattoast11/OmniCoder-9B-Zero-Phase2](https://huggingface.co/wheattoast11/OmniCoder-9B-Zero-Phase2/blob/2fbc076a7604514bac9183ee679b8ea077f2ce58/README.md) | Publisher GUI click accuracy (not established standard) | 94.61 | NOT MEASURED | 167 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | GSM8K frozen100 custom harness | 80.0 | 81.0 | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | GSM8K frozen100 custom harness | 92.0 | 97.0 | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | tinyMMLU | 76.0 | NOT MEASURED | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | tinyARC | 92.0 | NOT MEASURED | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | tinyHellaSwag | 65.0 | NOT MEASURED | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | tinyWinogrande | 76.0 | NOT MEASURED | 100 | Publisher protocol; see exact settings below |
| [Kukedlc/Slopus-9B](https://huggingface.co/Kukedlc/Slopus-9B/blob/85a138681cd780ef45a9b9c6d63363da33d08eb1/README.md) | tinyTruthfulQA MC1 | 61.0 | NOT MEASURED | 100 | Publisher protocol; see exact settings below |
| [ZelligeAI/tessera-preview-9b](https://huggingface.co/ZelligeAI/tessera-preview-9b/blob/406448148883e40a42d1592bd1b1fb3b977777b8/README.md) | LiveCodeBench release_v6 | 34.9 | 39.5 | 1055 | Publisher protocol; see exact settings below |
| [ZelligeAI/tessera-preview-9b](https://huggingface.co/ZelligeAI/tessera-preview-9b/blob/406448148883e40a42d1592bd1b1fb3b977777b8/README.md) | LiveCodeBench release_v6 | 33.7 | 45.9 | 1055 | Publisher protocol; see exact settings below |
| [ZelligeAI/tessera-preview-9b](https://huggingface.co/ZelligeAI/tessera-preview-9b/blob/406448148883e40a42d1592bd1b1fb3b977777b8/README.md) | IFEval prompt-strict | 40.9 | 59.9 | 541 | Publisher protocol; see exact settings below |
| [ZelligeAI/tessera-preview-9b](https://huggingface.co/ZelligeAI/tessera-preview-9b/blob/406448148883e40a42d1592bd1b1fb3b977777b8/README.md) | IFEval instruction-strict macro | 45.7 | 60.7 | 834 | Publisher protocol; see exact settings below |
| [Tivaphraen/Geryon-9B-v1](https://huggingface.co/Tivaphraen/Geryon-9B-v1/blob/462789d6507ffbbb6232a166731c72d995ef62cd/README.md) | GSM8K5shot flexible | 85.14 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [Tivaphraen/Geryon-9B-v1](https://huggingface.co/Tivaphraen/Geryon-9B-v1/blob/462789d6507ffbbb6232a166731c72d995ef62cd/README.md) | GSM8K5shot strict | 85.06 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | ARC | 43.1 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | ARC easy | 48.3 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | BoolQ | 62.4 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | HellaSwag | 65.6 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | OpenBookQA | 34.8 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | PIQA | 73.9 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris](https://huggingface.co/nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris/blob/26e8cf262354b32233ea6c8e43d0629b725a4ca9/README.md) | Winogrande | 64.7 | NOT MEASURED | NOT MEASURED | Publisher protocol; see exact settings below |
| [Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF](https://huggingface.co/Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF/blob/53ebc64bbacd7f0f51d01f29212831319b065f5f/README.md) | HumanEval+ copied parent claim | 78.66 | NOT MEASURED | NOT MEASURED | INHERITED_JACKRONG_V2_TEXT_NOT_VERIFIED_FOR_THIS_MERGE |
| [Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF](https://huggingface.co/Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF/blob/53ebc64bbacd7f0f51d01f29212831319b065f5f/README.md) | HumanEval+ copied parent claim | 81.7 | NOT MEASURED | NOT MEASURED | INHERITED_JACKRONG_V2_TEXT_NOT_VERIFIED_FOR_THIS_MERGE |
| [RedHatAI/OmniCoder-9B-FP8-Dynamic](https://huggingface.co/RedHatAI/OmniCoder-9B-FP8-Dynamic/blob/a1e8f2ec2ae2651c2eef923ec97a573605583880/README.md) | LiveCodeBenchv6 | 54.86 | NOT MEASURED | NOT MEASURED | Different FP8 serving stack; source subset inference-optimization/SWE-bench_Verified is declared. Completeness and protocol equivalence not independently established. |
| [RedHatAI/OmniCoder-9B-FP8-Dynamic](https://huggingface.co/RedHatAI/OmniCoder-9B-FP8-Dynamic/blob/a1e8f2ec2ae2651c2eef923ec97a573605583880/README.md) | SWE-bench Verified | 30.2 | NOT MEASURED | NOT MEASURED | Different FP8 serving stack; source subset inference-optimization/SWE-bench_Verified is declared. Completeness and protocol equivalence not independently established. |

<details><summary>Exact publisher settings and missing protocol fields</summary>

```json
[
  {
    "benchmark": "Publisher GUI click accuracy (not established standard)",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "format_compliance_percent": 100,
    "official_ranking_eligible": false,
    "repository": "wheattoast11/OmniCoder-9B-Zero-Phase2",
    "score_percent": 94.61,
    "settings": {
      "dataset_revision": null,
      "hardware": "L40S48GB training claim; evaluation hardware unspecified",
      "sampling": null,
      "scorer_version": null,
      "tasks": 167,
      "thinking": null
    }
  },
  {
    "baseline_score_percent": 81.0,
    "benchmark": "GSM8K frozen100 custom harness",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "publisher_wall_minutes": 5.5,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 80.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom Python numeric extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "temperature": 0,
      "thinking": false
    }
  },
  {
    "baseline_publisher_wall_minutes": 65.6,
    "baseline_score_percent": 97.0,
    "benchmark": "GSM8K frozen100 custom harness",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "publisher_wall_minutes": 5.5,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 92.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom Python numeric extraction",
      "presence_penalty": 1.5,
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "temperature": 1.0,
      "thinking": true,
      "top_k": 20,
      "top_p": 0.95
    }
  },
  {
    "benchmark": "tinyMMLU",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 76.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom generative answer extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "thinking": true
    }
  },
  {
    "benchmark": "tinyARC",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 92.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom generative answer extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "thinking": true
    }
  },
  {
    "benchmark": "tinyHellaSwag",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 65.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom generative answer extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "thinking": true
    }
  },
  {
    "benchmark": "tinyWinogrande",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 76.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom generative answer extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "thinking": true
    }
  },
  {
    "benchmark": "tinyTruthfulQA MC1",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Kukedlc/Slopus-9B",
    "score_percent": 61.0,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp b8292",
      "hardware": "RTX3090",
      "harness": "custom generative answer extraction",
      "quantization": "Q4_K_M",
      "scorer_version": null,
      "tasks": 100,
      "thinking": true
    }
  },
  {
    "baseline_score_percent": 39.5,
    "benchmark": "LiveCodeBench release_v6",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "ZelligeAI/tessera-preview-9b",
    "score_percent": 34.9,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM0.21.0",
      "hardware": "A10080GB",
      "harness": "evalscope1.9.0",
      "max_output": 16384,
      "scorer_version": "evalscope1.9.0 reported; exact commit unavailable",
      "tasks": 1055,
      "temperature": 0.0,
      "thinking": true
    }
  },
  {
    "baseline_score_percent": 45.9,
    "benchmark": "LiveCodeBench release_v6",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "ZelligeAI/tessera-preview-9b",
    "score_percent": 33.7,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM0.21.0",
      "hardware": "A10080GB",
      "harness": "evalscope1.9.0",
      "max_output": 16384,
      "scorer_version": "evalscope1.9.0 reported; exact commit unavailable",
      "tasks": 1055,
      "temperature": 0.6,
      "thinking": true
    }
  },
  {
    "baseline_score_percent": 59.9,
    "benchmark": "IFEval prompt-strict",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "ZelligeAI/tessera-preview-9b",
    "score_percent": 40.9,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM0.21.0",
      "hardware": "A10080GB",
      "harness": "evalscope1.9.0",
      "max_output": 16384,
      "scorer_version": "evalscope1.9.0 reported; exact commit unavailable",
      "tasks": 541,
      "temperature": 0.0,
      "thinking": true
    }
  },
  {
    "baseline_score_percent": 60.7,
    "benchmark": "IFEval instruction-strict macro",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "ZelligeAI/tessera-preview-9b",
    "score_percent": 45.7,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM0.21.0",
      "hardware": "A10080GB",
      "harness": "evalscope1.9.0",
      "max_output": 16384,
      "scorer_version": "evalscope1.9.0 reported; exact commit unavailable",
      "tasks": 834,
      "temperature": 0.0,
      "thinking": true
    }
  },
  {
    "benchmark": "GSM8K5shot flexible",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Tivaphraen/Geryon-9B-v1",
    "score_percent": 85.14,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp onWindows",
      "harness": "lm-evaluation-harness",
      "quantization": "Q8_0",
      "sampling": null,
      "scorer_version": null,
      "tasks": null
    },
    "stderr_percent": null
  },
  {
    "benchmark": "GSM8K5shot strict",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Tivaphraen/Geryon-9B-v1",
    "score_percent": 85.06,
    "settings": {
      "dataset_revision": null,
      "engine": "llama.cpp onWindows",
      "harness": "lm-evaluation-harness",
      "quantization": "Q8_0",
      "sampling": null,
      "scorer_version": null,
      "tasks": null
    },
    "stderr_percent": 0.98
  },
  {
    "benchmark": "ARC",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 43.1,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "ARC easy",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 48.3,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "BoolQ",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 62.4,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "HellaSwag",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 65.6,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "OpenBookQA",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 34.8,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "PIQA",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 73.9,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "benchmark": "Winogrande",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "nightmedia/Qwen3.5-9B-OmniCoder-Claude-Polaris",
    "score_percent": 64.7,
    "settings": {
      "dataset_revision": null,
      "engine": "MLX-format context; exact harness unavailable",
      "quantization": "mxfp8 row only",
      "sampling": null,
      "scorer_version": null,
      "tasks": null,
      "thinking": null
    }
  },
  {
    "attribution": "INHERITED_JACKRONG_V2_TEXT_NOT_VERIFIED_FOR_THIS_MERGE",
    "benchmark": "HumanEval+ copied parent claim",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF",
    "score_percent": 78.66,
    "settings": {
      "dataset_revision": null,
      "scorer_version": null,
      "tasks": null,
      "temperature": 0.2,
      "thinking": true
    }
  },
  {
    "attribution": "INHERITED_JACKRONG_V2_TEXT_NOT_VERIFIED_FOR_THIS_MERGE",
    "benchmark": "HumanEval+ copied parent claim",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "official_ranking_eligible": false,
    "repository": "Ngixdev/OmniCoder-Qwen3.5-9B-Claude-4.6-Opus-Uncensored-v2-GGUF",
    "score_percent": 81.7,
    "settings": {
      "dataset_revision": null,
      "scorer_version": null,
      "tasks": null,
      "temperature": 0.6,
      "thinking": true
    }
  },
  {
    "benchmark": "LiveCodeBenchv6",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "limit": "Different FP8 serving stack; source subset inference-optimization/SWE-bench_Verified is declared. Completeness and protocol equivalence not independently established.",
    "official_ranking_eligible": false,
    "repository": "RedHatAI/OmniCoder-9B-FP8-Dynamic",
    "score_percent": 54.86,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM",
      "harness": "lighteval/lm-eval; mini-swe-agent plusSWE-bench scorer",
      "max_output": null,
      "quantization": "FP8 Dynamic",
      "scorer_version": null,
      "tasks": null,
      "temperature": null
    }
  },
  {
    "benchmark": "SWE-bench Verified",
    "evidence_class": "PUBLISHER_REPORTED_NOT_LOCAL",
    "limit": "Different FP8 serving stack; source subset inference-optimization/SWE-bench_Verified is declared. Completeness and protocol equivalence not independently established.",
    "official_ranking_eligible": false,
    "repository": "RedHatAI/OmniCoder-9B-FP8-Dynamic",
    "score_percent": 30.2,
    "settings": {
      "dataset_revision": null,
      "engine": "vLLM",
      "harness": "lighteval/lm-eval; mini-swe-agent plusSWE-bench scorer",
      "max_output": 240000,
      "quantization": "FP8 Dynamic",
      "scorer_version": null,
      "tasks": null,
      "temperature": 0.2
    }
  }
]
```

</details>

Tessera reports less output with lower LiveCodeBench/IFEval scores; efficiency is a quality tradeoff, not a free gain. Slopus reports shorter reasoning under a small custom GSM8K protocol, with a lower thinking score than its stated baseline. These workloads, hardware and scorers do not establish superiority on this V100. Neither a merge of strong parents nor a distillation title proves additive capabilities or teacher provenance.

## Existing measured references

These unchanged records supply context, **not a controlled comparison** with the unmeasured proposals. Historical templates, sampling, output limits, MTP and weights differ. R217 also uses a derived artifact whose current availability is limited; preserve its audit and disclose reconstruction requirements.

| Model | Experiment / immutable configuration | HumanEval+ under recorded local protocol | Audit SHA256 |
| --- | --- | --- | --- |
| OmniCoder 9B | [R217](configuration-profiles/cfg-a69d0e339eeab4501399d65d30c2b6f7846566e191a7aec7cf4299fad4ee5c90.md) | 132/164 | `1f940596d115e34ae02fb770a10219149578150e431be646376f8fb223d15c0e` |
| Qwen3.5 9B | [R255](configuration-profiles/cfg-3a4e792f68b45a2e90c5792a2115936434eefcdfec54c6e5795ea0d236d9d920.md) | 132/164 | `69ed2894e20c7705ff385fc72bb70a5f0e9e353f42744449fadd8407f0c73fdb` |
| Qwen3.8 27B | [R117](configuration-profiles/cfg-06043d3a7d18c093e29a06609ddcaa375f519463c78325e89a0df1937cb66307.md) | 148/164 | `0a001d95dc6b53c43508ef53594a7cde7256e64c5089d38aa2def3b9d19f7087` |
| Qwen3.8 27B | [R118](configuration-profiles/cfg-5722b8039c1512e61e3c28558f7983b16695457fa164e45f1d3b4d0f24839b45.md) | 150/164 | `ab44bd9905753dd56faf682336ba75ef247818df7d6ba3774c7ac50fdfc4feef` |
| Ornith 1.5 9B | [R254](configuration-profiles/cfg-515700b7314a68b615da95138e8bd30da9c6011ad6762cd581468394c6cc996e.md) | 117/164 | `a898f240d6d584ddfcaaa6fdcf3b3d1a75c250ee73960005a4fe362f2551abb9` |

## Decisions for Jarvis

**Jarvis specialist:** Phase2 GUI grounding is a conditional specialist prospect; HDL only for a genuine hardware-design need. Neither is an allroundreplacement.

**best coding potential:** Nexus first for direct coding-parent merge relevance andreadyQ6; Slopus second for documented efficiency tradeoff; Claude-distill third with weak recipe provenance. Research priority only, no quality ranking.

**exclude now:** EmptyCISPOcheckpoint/no-weight repositories and incorrectformatroutes are technical exclusions only. Missinglicense/basecomposition routes deferred; no quality rejection from an absent benchmark.

**genuine weight changes:** Changed sameBF16 source values in3candidates and nonzero effectiveLoRA deltas in3adapters are locally observed; objectives, teacher provenance and quality gains are not thereby proven.

**watch:** Tessera compressed reasoning, Polaris/Geryon merges and OpenClaw-labelled adapters need more evidence; keep disclosed negative results.

**worth switching:** Not established. No new candidate has local comparable quality/latency/energy/VRAM data. Maintain current qualified baseline and larger-model references.

**NICHT VERIFIZIERT / NOT VERIFIED:** a local coding, agent, native-tool, German-conversation, memory, latency or energy advantage for any new derivative. Retain the qualified deployed baseline; assess model switching only after successful tasks and GPU-J/success are actually measured. No production changes.

## Provenance and reproduction

| Evidence | SHA256 |
| --- | --- |
| research_audit | `23843ba489791be555fbdbab2ce9997cfc4917ab91108b08869c59be1126b5e3` |
| CPU_audit | `9ef93f7cfd90800c03221b330409b81c0c712bee8548dea4046a30253eed9152` |
| GGUF_audit | `5d197e0d46269d2579f2c3d0565a874885efc6d7fcc76bd1684c01d0102a156f` |
| profiles | `f172fbbb87ac11013611fd0079d4013f5582c525952f28671a48070a1f01349b` |
| CPU_replay | `ef01843d72d7a7259dda6028a0a71d847d06cd81380fd8422f721689a15675a4` |

Original review: [audit](audits/audit-23843ba489791be555fb.md). Public metadata, source-receipt hashes, numerical summaries and proposals are under `candidate_research` in [benchmark-register.json](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json). The originals and raw fragments remain retained locally. No raw model data or model-repository program is executed or exported. Every inventory row links a revision-pinned model card; the register also pins metadata/card/config hashes.

To reproduce the bounded numerical probe, retrieve the revision-pinned safetensors headers and inclusive HTTP byte ranges in `cpu_range_receipts`, verify each SHA256, and resolve tensor offsets from the headers. Compare the first 256 row-major scalar values of each listed full-model tensor pair. Decode little-endian BF16 by shifting each unsigned16-bit word left 16 bits and interpreting it as float32; compute differences and RMSE in float64. Adapter probes multiply the first 8 rows of B by the first 16 columns of A in float64; the reported product is **unscaled**, with alpha/r supplied separately by the pinned adapter config. No model or repository code is executed. This is a bounded probe, not a complete identity test.

Unavailable originals: https://api.github.com/repos/wheattoast11/carl — HTTP404: Current original GitHub repository unavailable at review; cached web card is not a pinned current implementation. No cause inferred.

