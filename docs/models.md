# Model benchmarks and transfer

[View Model Comparison & Benchmarks with audited charts](benchmarks.md).

Models are compared within the same tasks using correct model-specific tokenizers/templates. A higher coding score is not general assistant superiority. Base-versus-plus joint coding scores, task success, VRAM and energy remain separate.

| Track | Candidate | Status | Evidence | Latest recorded sprint |
|---|---|---|---|---|
| BMC01 | Ornith 1.5 9B | im dokumentierten Umfang gemessen | LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED | R457 |
| BMC04 | Ternary Bonsai 2 27B PQ2_0/PTQ1_0 | im dokumentierten Umfang gemessen | LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED | R455 |
| BMC03 | MiMo V2.6 Distill Qwen 9B | im dokumentierten Umfang gemessen | LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED | R456 |
| BMC02 | OxCoder 9B | auf Nutzerwunsch gestoppt | HISTORICAL_PARTIAL_OWNER_STOP_NO_MODEL_REJECTION | R410 |
| BMC06 | LFM2.5 8B A1B | im dokumentierten Umfang gemessen | LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED | R453 |
| BMC07 | Gemma 4 12B IT QAT | im dokumentierten Umfang gemessen | LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED | R458 |
| BMC08 | Qwen3.6 27B | Gewichte und851 Tensorformen geprüft; regulärer Coding-Benchmark vorbereitet | CPU_SOURCE_AND_ARTIFACT_VERIFIED_NO_GPU_RESULT | NOT MEASURED / not recorded |
| BMC05 | LFM2.5 24B A2B QAD | Tool-Kategorie qualifiziert; Coding-Präfix85 unter Zeitlimit ausgewertet | LOKAL_GEMESSEN | NOT MEASURED / not recorded |
| BMC10 | LightOnOCR 3 4B | offen | NOT MEASURED / not recorded | NOT MEASURED / not recorded |
| BMC09 | UI-Venus 1.5 8B / Holo2 8B | offen | NOT MEASURED / not recorded | NOT MEASURED / not recorded |
| BMC11 | Qwen3.8 Flash-MTP-Derivat | offen | NOT MEASURED / not recorded | NOT MEASURED / not recorded |


## Evidence stages (not a ranking)

| Model | Local weights | GPU load | Basic quality | Coding | Tools | Agents | Own optimization | Comparable profile qualified |
|---|---|---|---|---|---|---|---|---|
| OmniCoder2 | YES | YES: R181/R183/R220 | YES: original12 | YES: R181 | YES: R183 | YES: R220 | YES: R90/R220/R226 | YES: scoped profile records |
| Qwen3.5 | YES | YES: R227/R228/R255 | YES: recorded native suite | YES: R255 | YES: R227 | YES: R228 | YES: R122–R127 | Not an allround champion |
| Qwen3.8 | YES | YES: R117/R118/R260 | YES: recorded native suite | YES: R117/R118 | See exact audits | YES: R260/R261 | YES: MTP comparison | Not an allround champion |
| Ornith 1.5 9B | YES: pinned Q6 | YES: R253 | YES: R259 | YES: R254/R258 | UNVERIFIED full100 | YES: R253 | YES: reasoning profile | UNVERIFIED / no comparable-profile qualification |
| Ternary Bonsai 2 27B PQ2_0/PTQ1_0 | YES: PQ2 track | YES: R267+ | YES: archived native suite | YES: recorded 164 | YES: recorded 100 | YES: recorded 18 | YES: kernel/recipe variants | UNVERIFIED / no comparable-profile qualification |
| MiMo V2.6 Distill Qwen 9B | YES: R287 | YES: R288 | YES: R288 | UNVERIFIED | UNVERIFIED | PARTIAL: R289 early stop | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| OxCoder 9B | YES: R290 | YES: R409 | PARTIAL: audited output-budget profile | NOT MEASURED | Control only; no100-case score | NOT MEASURED | NOT MEASURED | UNVERIFIED / no comparable-profile qualification |
| LFM2.5 8B A1B | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| Gemma 4 12B IT QAT | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| Qwen3.6 27B | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| LFM2.5 24B A2B QAD | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| LightOnOCR 3 4B | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| UI-Venus 1.5 8B / Holo2 8B | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |
| Qwen3.8 Flash-MTP-Derivat | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED / no comparable-profile qualification |


YES indicates an observed stage, not a passed quality gate. Old source-admission records are historical and may precede later GPU work. Bonsai PQ2 and the separate PTQ port must not be conflated.

## Existing OmniCoder2 / Qwen / challenger measurements

```json
{
  "model_comparison_progress": {
    "BonsaiPQ2_source_medium_coding_pilot": {
      "full164notrun": true,
      "full18": true,
      "screen_passed": true,
      "solved": 16,
      "tasks": 18
    },
    "R228_prepared_not_submitted": false,
    "current_single_factor_gate_audit": {
      "sha256": "d700f44e620df53562534cafd76eb4e53cf35c042c7a5dc04f132be40875629e"
    },
    "existing_qwen38_coding_scores_independently_checked": {
      "new_GPU_generations": 0,
      "records": {
        "R117": {
          "MTP_enabled": false,
          "audit_sha256": "0a001d95dc6b53c43508ef53594a7cde7256e64c5089d38aa2def3b9d19f7087",
          "qualification": "Retainedlocalcodingevidence,notgeneralmodel/agentwinner",
          "scopes": {
            "custom_long16": {
              "solved": 15,
              "tasks": 16
            },
            "standard_full164": {
              "solved": 148,
              "tasks": 164
            }
          },
          "score_rule": "base_pass AND plus_pass"
        },
        "R118": {
          "MTP_enabled": true,
          "audit_sha256": "ab44bd9905753dd56faf682336ba75ef247818df7d6ba3774c7ac50fdfc4feef",
          "qualification": "Retainedlocalcodingevidence,notgeneralmodel/agentwinner",
          "scopes": {
            "custom_long16": {
              "solved": 15,
              "tasks": 16
            },
            "standard_full164": {
              "solved": 150,
              "tasks": 164
            }
          },
          "score_rule": "base_pass AND plus_pass"
        }
      }
    },
    "matrix_revision": 316,
    "ornith_agents": {
      "gpu_j_per_success": 3917.593433262527,
      "original12_format": 5,
      "original12_semantic": 9,
      "screen_passed": false,
      "solved": 14,
      "tasks": 18,
      "wall_s": 201.46956243099999
    },
    "ornith_coding": {
      "custom_long_solved": 14,
      "custom_long_tasks": 16,
      "reasoning_profile_pending": true,
      "screen_passed": false,
      "standard_solved": 117,
      "standard_tasks": 164
    },
    "ornith_reasoning_coding_pilot": {
      "full18": false,
      "scopes": {
        "custom_long_pilot": {
          "solved": 0,
          "tasks": 0
        },
        "standard_pilot": {
          "solved": 6,
          "tasks": 8
        }
      },
      "screen_passed": false
    },
    "ornith_reasoning_original12": {
      "first4_reused": true,
      "format": 3,
      "full12": true,
      "semantic": 10
    },
    "ornith_reasoning_recipe": {
      "QA_cases": 4,
      "format": 2,
      "full_quality_pending": true,
      "operational": true,
      "semantic": 3
    },
    "qwen35_agents": {
      "gpu_j_per_success": 7020.5988425358355,
      "peak_device_vram_mib": 5956.5,
      "screen_passed": false,
      "solved": 8,
      "tasks": 18,
      "wall_s": 214.550275628
    },
    "qwen35_coding": {
      "custom_long_solved": 15,
      "custom_long_tasks": 16,
      "manufacturer_profile_pending": true,
      "screen_passed": false,
      "standard_solved": 132,
      "standard_tasks": 164
    },
    "qwen38_MTP_agents": {
      "coding": {
        "energy_reduction_percent_vs_R260": 14.848842521484961,
        "gpu_energy_j_approx": 63782.84098651977,
        "solved": 7,
        "tasks": 7,
        "wall_reduction_percent_vs_R260": 10.716894545598576,
        "wall_s": 246.49321105500002
      },
      "not_general_assistant_qualified": true,
      "screen_passed": false,
      "solved": 14,
      "tasks": 18,
      "wall_s": 408.702045542
    },
    "qwen38_agents": {
      "full18": true,
      "model_sha256": "58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f",
      "quality_tradeoff_candidate_not_qualified": true,
      "screen_passed": false,
      "solved": 14,
      "tasks": 18
    }
  }
}
```

## Candidate admission records


### BMC01 — Ornith 1.5 9B

```json
{
  "assessment": "Complete native BFCL simple_python400 category and explicit full/partial coding profiles are linked below. Historical profiles/negatives remain; neither whole-BFCL nor overall model qualification is claimed.",
  "current_experiment": "R457",
  "evidence_class": "LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED",
  "id": "BMC01",
  "local_scope": {
    "kind": "STANDARD_BENCHMARK_PROFILE_EVIDENCE",
    "original_profile_history_preserved": true,
    "overall_model_qualified": false,
    "selected_native_coding": [
      {
        "intended_tasks": 164,
        "official_eligible": false,
        "score_percent": 91.39784946236558,
        "solved": 85,
        "status": "PARTIAL",
        "tasks": 93
      }
    ]
  },
  "name": "Ornith 1.5 9B",
  "next_step": "Agentenqualität sowie Aufgabenlatenz, VRAM und Energie der dokumentierten Profile bewerten; bereits gültige Standardläufe und ausgeschöpfte Teilkampagnen nicht wiederholen.",
  "priority": "P0",
  "repository": "https://huggingface.co/ornith-ai/Ornith-1.5-9B",
  "source_admission": {
    "Q6_file_bytes": 7558901696,
    "Q6_remote_LFS_sha256": "b6f76e74f86245b3caee014b797c10dca931c4dfdaabfb134eab655f81e4154a",
    "actual_GPU_model_starts": 0,
    "evidence_class": "EXTERN_BELEGT_NOT_LOCAL_MODEL_MEASUREMENT",
    "interpretation": "Architecturefamilymatchesexistingqwen35SM70path;source-templateisdifferentandmustbepreserved. ConfigMTP1isnotproofGGUFcontainsusablehead. Nativeinference/VRAM/taskqualitynotlocallymeasured. No publisherleaderboardcausalityclaim.",
    "license_file_verified": false,
    "model_downloaded": false,
    "mtp_head_presence_in_GGUF_not_verified": true,
    "native_template_required": true,
    "native_thinking_toggle_implemented": true,
    "source_admission_sha256": "398784d5b1c8d0ae2cfd760b392aa0a67991f2ce3a2d4fc3b8a54ef4ad7c9f8f",
    "template_sha256": "9dd2fbd270feaa1fbef2d4f634d7887c9c506e3bde140f8e7351c8944e8fd235",
    "text_architecture_shapes": {
      "full_attention_interval": 4,
      "hidden_size": 4096,
      "linear_key_head_dim": 128,
      "linear_num_key_heads": 16,
      "linear_num_value_heads": 32,
      "linear_value_head_dim": 128,
      "mtp_num_hidden_layers": 1,
      "num_attention_heads": 16,
      "num_hidden_layers": 32,
      "num_key_value_heads": 4
    }
  },
  "status": "im dokumentierten Umfang gemessen"
}
```

### BMC04 — Ternary Bonsai 2 27B PQ2_0/PTQ1_0

```json
{
  "assessment": "Complete native BFCL simple_python400 category and explicit full/partial coding profiles are linked below. Historical profiles/negatives remain; neither whole-BFCL nor overall model qualification is claimed.",
  "current_experiment": "R455",
  "evidence_class": "LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED",
  "id": "BMC04",
  "local_scope": {
    "kind": "STANDARD_BENCHMARK_PROFILE_EVIDENCE",
    "original_profile_history_preserved": true,
    "overall_model_qualified": false
  },
  "name": "Ternary Bonsai 2 27B PQ2_0/PTQ1_0",
  "next_step": "Agentenqualität sowie Aufgabenlatenz, VRAM und Energie der dokumentierten Profile bewerten; bereits gültige Standardläufe und ausgeschöpfte Teilkampagnen nicht wiederholen.",
  "priority": "P1",
  "repository": "https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf",
  "source_admission": null,
  "status": "im dokumentierten Umfang gemessen"
}
```

### BMC03 — MiMo V2.6 Distill Qwen 9B

```json
{
  "assessment": "Complete native BFCL simple_python400 category and explicit full/partial coding profiles are linked below. Historical profiles/negatives remain; neither whole-BFCL nor overall model qualification is claimed.",
  "current_experiment": "R456",
  "evidence_class": "LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED",
  "id": "BMC03",
  "local_scope": {
    "kind": "STANDARD_BENCHMARK_PROFILE_EVIDENCE",
    "original_profile_history_preserved": true,
    "overall_model_qualified": false,
    "selected_native_coding": [
      {
        "official_eligible": true,
        "score_percent": 72.5609756097561,
        "solved": 119,
        "status": "FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
        "tasks": 164
      }
    ]
  },
  "name": "MiMo V2.6 Distill Qwen 9B",
  "next_step": "Agentenqualität sowie Aufgabenlatenz, VRAM und Energie der dokumentierten Profile bewerten; bereits gültige Standardläufe und ausgeschöpfte Teilkampagnen nicht wiederholen.",
  "priority": "P0",
  "repository": "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B",
  "source_admission": null,
  "status": "im dokumentierten Umfang gemessen"
}
```

### BMC02 — OxCoder 9B

```json
{
  "assessment": "Owner stopped further OxCoder diagnosis and inference while selecting an alternative checkpoint. Preserve R448 partial results and unresolved source-weight concern; no model-quality rejection or restart.",
  "current_experiment": "R410",
  "evidence_class": "HISTORICAL_PARTIAL_OWNER_STOP_NO_MODEL_REJECTION",
  "id": "BMC02",
  "local_scope": null,
  "name": "OxCoder 9B",
  "next_step": "Nur nach konkreter neuer Modellidentität beziehungsweise Anweisung fortsetzen.",
  "priority": "P0",
  "repository": "https://huggingface.co/OrionLLM/OxCoder-9B",
  "source_admission": null,
  "status": "auf Nutzerwunsch gestoppt"
}
```

### BMC06 — LFM2.5 8B A1B

```json
{
  "assessment": "Complete native BFCL simple_python400 category and explicit full/partial coding profiles are linked below. Historical profiles/negatives remain; neither whole-BFCL nor overall model qualification is claimed.",
  "current_experiment": "R453",
  "evidence_class": "LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED",
  "id": "BMC06",
  "local_scope": {
    "kind": "STANDARD_BENCHMARK_PROFILE_EVIDENCE",
    "original_profile_history_preserved": true,
    "overall_model_qualified": false,
    "selected_native_coding": [
      {
        "official_eligible": false,
        "score_percent": 70.73170731707317,
        "solved": 116,
        "status": "FULL_NATIVE_CODING_OFFICIAL_API_PENDING",
        "tasks": 164
      },
      {
        "official_eligible": true,
        "score_percent": 70.73170731707317,
        "solved": 116,
        "status": "FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
        "tasks": 164
      }
    ]
  },
  "name": "LFM2.5 8B A1B",
  "next_step": "Agentenqualität sowie Aufgabenlatenz, VRAM und Energie der dokumentierten Profile bewerten; bereits gültige Standardläufe und ausgeschöpfte Teilkampagnen nicht wiederholen.",
  "priority": "P0",
  "repository": "https://huggingface.co/LiquidAI/LFM2.5-8B-A1B",
  "source_admission": {
    "GPU_runs": 0,
    "sha256": "a2da6db6acd28bbce0145323499402b0edeacf11e3f5aec45c2290d1b2c7677a"
  },
  "status": "im dokumentierten Umfang gemessen"
}
```

### BMC07 — Gemma 4 12B IT QAT

```json
{
  "assessment": "Complete native BFCL simple_python400 category and explicit full/partial coding profiles are linked below. Historical profiles/negatives remain; neither whole-BFCL nor overall model qualification is claimed.",
  "current_experiment": "R458",
  "evidence_class": "LOKAL_GEMESSEN_SCOPED_BENCHMARKS_NOT_MODEL_WIDE_QUALIFIED",
  "id": "BMC07",
  "local_scope": {
    "kind": "STANDARD_BENCHMARK_PROFILE_EVIDENCE",
    "original_profile_history_preserved": true,
    "overall_model_qualified": false,
    "selected_native_coding": [
      {
        "official_eligible": true,
        "score_percent": 95.1219512195122,
        "solved": 156,
        "status": "FULL_OFFICIAL_API_LOCAL_PROTOCOL_VERIFIED",
        "tasks": 164
      }
    ]
  },
  "name": "Gemma 4 12B IT QAT",
  "next_step": "Agentenqualität sowie Aufgabenlatenz, VRAM und Energie der dokumentierten Profile bewerten; bereits gültige Standardläufe und ausgeschöpfte Teilkampagnen nicht wiederholen.",
  "priority": "P1",
  "repository": "https://huggingface.co/google/gemma-4-12B-it",
  "source_admission": {
    "GPU_runs": 0,
    "sha256": "230de81437f1f93f18388351ef795cde9470b096f93f2c2226dac94d9bfbc57f",
    "weights_available": false
  },
  "status": "im dokumentierten Umfang gemessen"
}
```

### BMC08 — Qwen3.6 27B

```json
{
  "assessment": "Technisch begründeter nächster normaler Modellvergleich, kein Qualitäts-Vorabfilter. Q3_K_S ist ein konservatives Speicherprofil; Q3_K_M ist dadurch nicht widerlegt. Exakte upstream-Konvertierungsrevision unaufgezeichnet.",
  "current_experiment": null,
  "evidence_class": "CPU_SOURCE_AND_ARTIFACT_VERIFIED_NO_GPU_RESULT",
  "id": "BMC08",
  "local_scope": {
    "GPU_runs": 0,
    "kind": "INDEPENDENT_SHA256_AND_CPU_HEADER_VERIFICATION",
    "model_sha256": "4afb4abcf0207a484b0d7e92c0421b74e8ce1c7a7250bb9d824b79288da68f20",
    "model_starts": 0,
    "parameter_count": 26895998464,
    "weights_downloaded": 1
  },
  "name": "Qwen3.6 27B",
  "next_step": "Normales HumanEval+164 mit nativem Nonthinking-Herstellerprofil über den regulären Broker;20min reine Aufgabenzeit, anschließend Tool-Kategorie. Nicht ausgeführte Aufgaben unbekannt lassen.",
  "priority": "P0",
  "repository": "https://huggingface.co/Qwen/Qwen3.6-27B",
  "source_admission": null,
  "status": "Gewichte und851 Tensorformen geprüft; regulärer Coding-Benchmark vorbereitet"
}
```

### BMC05 — LFM2.5 24B A2B QAD

```json
{
  "assessment": "R467: volle BFCL-v4-simple_python-Kategorie374/400 lokal qualifiziert. R468: HumanEval+77/85 beobachtete Aufgaben, dann1200s Aufgabenlimit; PARTIAL, keine Hochrechnung auf164. Unabhängiger CPU-Replay identisch. Coding-Zählerenergie2549,233–2550,042J je77 Erfolge nur für85 abgeschlossene Anfragen; kein BFCL-Gesamtscore, Allround-Champion oder kausaler Optimierungsgewinn.",
  "current_experiment": null,
  "evidence_class": "LOKAL_GEMESSEN",
  "id": "BMC05",
  "local_scope": {
    "GPU_runs": 2,
    "coding": {
      "HTTP_request_s": 1188.633956511,
      "evaluated": 85,
      "full_suite_tasks": 164,
      "independent_CPU_replay_changed": 0,
      "official_full_qualified": false,
      "peak_vram_mib": 13794.5,
      "solved": 77,
      "status": "PARTIAL",
      "task_limit_s": 1200
    },
    "kind": "QUALIFIED_FULL_NATIVE_TOOLS_CATEGORY_ONLY",
    "model_sha256": "d1c03f73ecaf61017d70419eec9e5dc0b05d50ae26c23d522829b934fbabf8a5",
    "model_starts": 2,
    "overall_model_or_champion_qualified": false,
    "peak_device_vram_mib": 13798.5,
    "solved": 374,
    "task_phase_s": 362.70372274,
    "tasks": 400,
    "weights_downloaded": 1
  },
  "name": "LFM2.5 24B A2B QAD",
  "next_step": "Quellprofil und beide Messbereiche erhalten. Kein Neustart desselben erschöpften Coding-Benchmarks. Andere vorhandene Modellkandidaten regulär vergleichen, später nur begründete neue Profilhypothesen.",
  "priority": "P0",
  "repository": "https://huggingface.co/LiquidAI/LFM2.5-24B-A2B",
  "source_admission": {
    "GPU_runs": 0,
    "model_starts": 0,
    "sha256": "819239f28ed8c8da96d1df75df8c8aaa87eed9136680497689c983d98d5927dc"
  },
  "status": "Tool-Kategorie qualifiziert; Coding-Präfix85 unter Zeitlimit ausgewertet"
}
```

### BMC10 — LightOnOCR 3 4B

```json
{
  "assessment": "Kein allgemeiner Agent- oder Coding-Challenger.",
  "current_experiment": null,
  "evidence_class": null,
  "id": "BMC10",
  "local_scope": null,
  "name": "LightOnOCR 3 4B",
  "next_step": "Lokale Dokumente, Tabellen und Reading Order; vollständiger multimodaler Pfad.",
  "priority": "P2",
  "repository": "https://huggingface.co/lightonai/LightOnOCR-3-4B",
  "source_admission": null,
  "status": "offen"
}
```

### BMC09 — UI-Venus 1.5 8B / Holo2 8B

```json
{
  "assessment": "Holo2 Quelle: https://huggingface.co/Hcompany/Holo2-8B",
  "current_experiment": null,
  "evidence_class": null,
  "id": "BMC09",
  "local_scope": null,
  "name": "UI-Venus 1.5 8B / Holo2 8B",
  "next_step": "Bildauflösung und normierte Koordinaten auf lokalem Screenspot; kein allgemeiner Chatwinner.",
  "priority": "P2",
  "repository": "https://huggingface.co/inclusionAI/UI-Venus-1.5-8B",
  "source_admission": null,
  "status": "offen"
}
```

### BMC11 — Qwen3.8 Flash-MTP-Derivat

```json
{
  "assessment": "MTP-Engine und geänderter Checkpoint sind jeweils zusätzliche Varianten.",
  "current_experiment": null,
  "evidence_class": null,
  "id": "BMC11",
  "local_scope": null,
  "name": "Qwen3.8 Flash-MTP-Derivat",
  "next_step": "Originalfork-SM70 und NextN-Funktionalität separat belegen, kein claim von 2x/4x.",
  "priority": "P2",
  "repository": "https://huggingface.co/SuperLogic/Qwen3.8-27B-Flash-MTP-GGUF",
  "source_admission": null,
  "status": "offen"
}
```

## Stage semantics

Researched, locally available weights, GPU-load success, measured basic quality, coding, tool calling, agents and qualified comparable profile are separate stages. Missing stage evidence is **UNVERIFIED**, not NO and not YES. A model file or source-only architecture review does not prove any downstream stage. See the linked experiments rather than infer completion from a track status.
