# Open questions & research proposals

GitHub snapshot: 2026-10-26T21:57:08.216861+00:00. **10 open / 8 closed**. This is not a live issue monitor. Workflow closure, scientific disposition and optimization qualification are separate.

Current P0: owner-authorized new-family model qualification (#16); the dated Best-of-V100 decision remains a baseline. Source/kernel gates remain conditional. Harness CPU reviews (#17/#18) do not authorize new GPU ablations. No factor count or GPU coverage is increased by this registry.

| Subcase | Open GitHub issue | Research disposition | Freeze priority | Next step / evidence |
|---|---|---|---|---|
| R340-S03 | [Research: admit one SM70 vLLM source lane only after model and memory gates](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/2) | OPEN_MODEL_AND_MEMORY_ADMISSION_GATE | P2_NOVEMBER_TECHNICAL_GATE | Preserve the documented source/model/engine prerequisite and original evidence. No large new engine/kernel/adapter branch before the final freeze; reopen execution only with a distinct feasible isolated hypothesis.  |
| R340-S06 | [Research: evaluate block-FP8 W8A16 fused dequantization on SM70](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/3) | OPEN_MODEL_ARTIFACT_AND_KERNEL_GATE | P2_NOVEMBER_TECHNICAL_GATE | Preserve the documented source/model/engine prerequisite and original evidence. No large new engine/kernel/adapter branch before the final freeze; reopen execution only with a distinct feasible isolated hypothesis.  |
| R340-S07 | [Research: flash-attention V100 page/stride and causal-mask correctness](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/4) | OPEN_MODEL_ENGINE_DEPENDENT_AFTER_SOURCE_REVIEW | P2_NOVEMBER_TECHNICAL_GATE | Preserve the documented source/model/engine prerequisite and original evidence. No large new engine/kernel/adapter branch before the final freeze; reopen execution only with a distinct feasible isolated hypothesis.  |
| HBM10 | [HBM10: validate unweighted NUQ calibration and a partial-RoPE cache adapter](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/8) | OPEN_PARTIAL_ROPE_GDN_ADAPTER_PENDING | P2_NOVEMBER_TECHNICAL_GATE | Preserve the documented source/model/engine prerequisite and original evidence. No large new engine/kernel/adapter branch before the final freeze; reopen execution only with a distinct feasible isolated hypothesis.  |
| FINAL-GATE | [Final Research Gate: Qwen3.5 → OmniCoder2 Transfer, neue Optimierungen und Forschungsfragen abschließen](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/10) | CURRENT_MISSION_GATE_REVIEWED_WITH_DECLARED_LIMITS | P1_EVIDENCE_MAINTENANCE | Preserve the reviewed role decision, missing official Agents, negative results and partial history. Maintain scientific corrections and separately scoped future research; broader unchecked issue items are not automatically qualified or closed.  |
| MODEL-QUALIFICATION | [Model comparison: complete standard benchmarks before rejection or tuning](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/11) | CURRENT_MISSION_GATE_REVIEWED_WITH_DECLARED_LIMITS | P1_EVIDENCE_MAINTENANCE | Preserve the reviewed role decision, missing official Agents, negative results and partial history. Maintain scientific corrections and separately scoped future research; broader unchecked issue items are not automatically qualified or closed.  |
| LFM24-PARSER | [Investigate LFM24 one-call behavior on complete complex-tool benchmark](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/13) | DEFERRED_DISTINCT_PROFILE_HYPOTHESIS_REQUIRED | P2_NO_JUSTIFIED_RERUN | Cardinality and argument preservation checks are complete: no observed parser loss. The cause of6/200 remains unproven. Resume only for a distinct source-backed template/harness discrepancy; do not rerun merely to set parallel_tool_calls. [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/13#issuecomment-6395922011), [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/13#issuecomment-6398582411) |
| NOVEMBER-MODEL-FAMILIES | [Research: non-Qwen/Gemma models ≤30B for V100 SM70 — GLM, gpt-oss, Mistral, Nemotron; Mixtral reassessment](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/16) | ACTIVE_OWNER_AUTHORIZED_NEW_FAMILY_SCREENING | P0_NEW_MODEL_COMPARISON | Seven complete frozen32 screens (R552–R558). Full coding: Ministral8 R560 128/164, Devstral R561 122/164, Phi4 R566 134/164. Full tools: Devstral R563 175/200, Ministral8 R564 153/200. Devstral internal Agent33 R565 22/33; Ministral internal Agent33 R567: 17/33. Mistral Small3.2 coding R568: 129/164, complete and qualified. Phi4 tools R569 is in progress. A mixed-screening-to-tools broker extension passed288 CPU controls but is not activated; any later gpt-oss tool run needs its separate regular admission. Then evidence-based selection and updated Best-of-V100 review. R559 parser and R562 startup 180s blocks remain technical, not quality exclusions. Preserve references and guards; no automatic retries.  |
| NOVEMBER-HARNESS | [Research: minimal vs complex coding-agent harness — quality, tokens, latency and GPU-J/success](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17) | CPU_EVIDENCE_REVIEW_PENDING_NO_GPU_ADMISSION | P1_CPU_HARNESS_REVIEW_BEFORE_TUNING | R537 token/call reconciliation is complete and inconclusive. Pinned mini-SWE source review confirms append-only trajectories, delegated action execution and pre-query wall-clock limits; these do not replace broker deadlines or policy enforcement. Preregister matched development/holdout prose ablation; no extra GPU admission. R537 exact-token recurrence is archived below; any state-correct caching/preamble ablation remains a separate hypothesis and GPU admission. No savings measured. [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17#issuecomment-6428910994), [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/17#issuecomment-6431036526) |
| LEAN-HARNESS | [Research: Lean Jarvis harness — Caveman, mini-SWE-agent, context compaction A/B before final V100 tuning](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18) | CPU_EVIDENCE_REVIEW_PENDING_NO_GPU_ADMISSION | P1_CPU_HARNESS_REVIEW_BEFORE_TUNING | Pinned current Caveman3+ is Apache2; older release terms remain distinct. Prose compression is model-assisted rewriting, not proven lossless; documented gateway recovery does not establish local API compatibility. No proxy, MCP or compressor installed. Reuse #17; any later GPU ablation requires separate admission. R537 exact-token recurrence is archived below; any state-correct caching/preamble ablation remains a separate hypothesis and GPU admission. No savings measured. [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18#issuecomment-6428911369), [evidence](https://github.com/JuliusBrussee/caveman/blob/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4/LICENSING.md), [evidence](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/18#issuecomment-6431039573) |


<details class="lab-evidence"><summary>Harness token recurrence · R537 · 96 archived requests</summary>

| Arm | Requests | Recorded input tokens | Repeated within-case prefix tokens after first call |
|---|---|---|---|
| single | 36 | 84763 | 48287 |
| planner_worker | 27 | 51167 | 28560 |
| planner_worker_reviewer | 33 | 66888 | 29955 |


Exact token IDs and request hashes match all96 original usage records; `cache_prompt=false` throughout. Five paired development cases, not an independent harness ablation. Prefixes include task/history content; isolated system/tool preamble tokens remain **NOT MEASURED**. No prompt was shortened, cache correctness tested, or latency/energy saving measured.

Audit SHA256: `49b2dd94734d96c0c1d1b73b1a2605e8d7dcf8261abb338f25b198b75cf29bda`. [CPU reproduction script](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/scripts/harness_prefix.py), SHA256 `88d7fcb0d6fe1ced3f2b66c7caf3e6776fc3e6f66198c494320e7913242c09a3`.

</details>

??? note "Closed scoped workflow records — not additional qualified optimizations"

    | Subcase | Closed GitHub issue | Recorded scope | Priority | Evidence / boundary |
    |---|---|---|---|---|
    | R340-S01 | [Research: targeted SM70 resource/traffic profiling for a distinct kernel patch](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/1) | CLOSED_SCOPED_TECHNICAL_DEFERRAL | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | R340-S05 | [Audit: Alle DEFERRED-Optimierungen überprüfen und technisch sinnvolle Ansätze reaktivieren](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/5) | CLOSED_DEFERRED_REASSESSMENT_AUDIT_COMPLETE | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | BMT27 | [Research: head-free confidence calibration for frozen Omni after probability-acquisition gate](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/6) | CLOSED_NEGATIVE_HEAD_FREE_POLICY_SCREEN | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | GIST-V02 | [Research: one SM70 kernel L1/shared carveout admission, separate from conversion cache](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/7) | CLOSED_SCOPED_TECHNICAL_DEFERRAL | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | Q04 | [Q04: validate native MLP AWQ scaling after forward calibration](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/9) | CLOSED_NEGATIVE_Q04_DEVELOPMENT_GATE | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | OXCODER-DIAGNOSIS | [OxCoder R448: Diagnose von 104 leeren Codeantworten und 2:18 h Inferenzzeit](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/12) | CLOSED_GITHUB_SCOPED_OUTCOME | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | TASK-WRAPPER-TIMING | [Benchmark timing: review outer wrapper ending before native task allowance](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/14) | CLOSED_GITHUB_SCOPED_OUTCOME | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |
    | GEMMA-AGENT-FORMAT | [Gemma Agent18: diagnose tool and final-format failures after the 16K context fix](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/15) | CLOSED_GITHUB_SCOPED_OUTCOME | ARCHIVED_SCOPED_OUTCOME | Preserve closure evidence and original measurements. Workflow closure is not a model/optimization qualification; see the linked original issue.  |


## Retained research proposals

Hypotheses and admission prerequisites remain distinct from measured gains. Existing safety and single-factor gates still apply.

## R340-S01

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM06",
    "HBM07",
    "C09",
    "C10"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "ADMISSION_ONLY_NO_GPU_JOB",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S01",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Gezieltes Profiling zur Auswahl eines neuen Kernelpatches; Occupancy allein ist keine Zielmetrik.",
  "next_action": "Acht vorhandene Trace-Datenbanken ausgewertet; Kernelidentität und Ressourcen belegt. Nur neue konkret patchrelevante dynamische Counterfrage später zulassen, kein vollständiger Re-Trace.",
  "prerequisites": "Vorhandene Traces prüfen; tatsächlich ausgeführteQ6Kernelnamen/Shapes/Binarypins. ncu2022.4.1/nsys2022.4.2/nvprof12.0 vorhanden, CUDA12.8/SM70/driver-Kompatibilität und Counterrechte noch nicht bewiesen.",
  "priority_band": "P1",
  "risks": "Profilingreplay beeinflusst Timing/Energie/Cache; keine Counter schätzen und keine Treiber-/Berechtigungsänderung.",
  "sources": [
    "VOLTA_GUIDE",
    "VOLTA_MICROARCH",
    "VLLM_IMPLEMENTATION"
  ],
  "test_design": "Zunächst CPU/SASS-Ressourcen und alte Traces. Falls konkrete Patchentscheidung offen: höchstens120s brokerbewachte Diagnostik, identische512/2K/4K-Prefill/128Decode; verfügbare Counter abfragen, nur nötige DRAMbytes/sectors,L1/L2,localspill,occupancy/sharedconflicts sammeln. Diagnostikzeiten nicht als Servingwerte; kein automatischer Benchmarkauftrag.",
  "title": "SM70-Register/Spills und tatsächlicher Speicherverkehr"
}
```

</details>

## R340-S02

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "C14",
    "C13",
    "K05",
    "HBM05"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "CORRECTNESS_GATE_ONLY_NO_REPEAT",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S02",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Explizite aktive Masken/Barrieren bei verändertem Datenaustausch; kein Ursachenbeweis für E09.",
  "next_action": "Als Gate am nächsten passenden Patch verwenden; keine generische Wiederholung.",
  "prerequisites": "Konkreter neuer geänderter Thread-/Statepfad und unabhängiges numerisches Orakel.",
  "priority_band": "P0",
  "risks": "Keine pauschale GDN-Ursache oder Übertragung von Registerbankbefunden auf SharedMemory.",
  "sources": [
    "VOLTA_GUIDE",
    "VOLTA_MICROARCH"
  ],
  "test_design": "Quell-Diff vor GPU; Tails/Divergenz und FP16/FP32-Toleranzen, OriginalQA12 sowie State-Erhalt prüfen. Sanitizer nur nach Toolzulassung und konkretem Patch.",
  "title": "Warp-Synchronisation und numerische Zustandskorrektheit"
}
```

</details>

## R340-S03

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "E03",
    "E06",
    "E07"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "DEFERRED_EXECUTION_NO_INSTALL_MODEL_AND_SPACE_GATES",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S03",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Beide OriginalCMake-Stände erlaubenSM70 unter12.8; 0.19 auch im12.8-Zweig,0.21 dort nicht. Kein Beweis gegen bestehenden llama.cppCUDA12.8-Pfad.",
  "next_action": "E03Ausführungzurückgestellt: vollständigeinverseGDN-/Norm-/Headlayout-Konversion undQuantloader vorEngineinstallation zulassen. KeinGPU-Lauf mitbloßemAliaspatch.",
  "prerequisites": "KorrektzugelassenerOriginalGGUFLoader ODER passendesHF/FP8Gewicht; Qwen35/GDN/SM70-Tensorpfade vollständigprüfen. Namensmapping-Vorabtest R342negativ; <=14GiBPeakVRAMund10GiBfreieScratchreserve erforderlich.",
  "priority_band": "P2",
  "risks": "Torch-Wheel mussSM70 selbst enthalten; Import/Build ist keinKernel-Dispatchbeweis.",
  "sources": [
    "VLLM_REPORT",
    "VLLM_IMPLEMENTATION"
  ],
  "test_design": "Vor Installation statischeFormat/Graph/VRAM-Prüfung. Erst bei Zulassung TP1-Kernelausführung/Numerik; danach gleiche nativeQA/Tools/Coding. Enginewechsel als Gesamtkonfiguration, nicht Einzelkernelkausalität.",
  "title": "vLLM0.19/0.21 CUDA12.6-Source-Lane"
}
```

</details>

## R340-S04

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "C03",
    "C04"
  ],
  "classification": "ALREADY_COVERED",
  "counts_as_factor": false,
  "decision": "EXISTING_LLAMA_GRAPH_SCOPE_REUSED",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S04",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Replay reduziert Launch-/Hostaufwand abhängig vom konkreten Stack.",
  "next_action": "Kein erneuter Lauf gültiger Graphprofile.",
  "prerequisites": "GleicheEngine/Modell/Dtype/Tokens/Cache; Capture/Replays belegt; Graph-VRAM budgetiert.",
  "priority_band": "P2",
  "risks": "Diagnosehooks können Capture ungültig machen; externer Faktor wird nicht zum Champion addiert.",
  "sources": [
    "VLLM_REPORT",
    "VLLM_IMPLEMENTATION"
  ],
  "test_design": "llama.cppAudits wiederverwenden. Nur für später zugelassenevLLMLane Graph/Eager kontrolliert, Capturekosten und VRAM getrennt.",
  "title": "CUDA-Graphs und Eager korrekt vergleichen"
}
```

</details>

## R340-S05

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "E03",
    "C10",
    "HBM04"
  ],
  "classification": "NOT_APPLICABLE",
  "counts_as_factor": false,
  "decision": "NOT_APPLICABLE_CURRENT_DENSE_OMNI",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S05",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Upstream smallM wähltK128; Pluginheuristik ändert auchM/N/Warps/Stages. Veröffentlichter Gesamtpatch ist kein reinerK-Einzelnachweis.",
  "next_action": "Whole-model applicability remains dense-Omni NOT_APPLICABLE. A distinct isolated FP16 MoE K128/K64 component test is conditionally possible without a full vLLM install, but pinned compiler/kernel dependencies are not admitted; no GPU test or local benefit claim.",
  "prerequisites": "RoutedMoE-Modell und exakteFP16Experten/Shapes/TP; aktuellesOmni ist dense.",
  "priority_band": "P2",
  "risks": "KeinDense- oderFP8-Pfad; kein pauschaler9xGewinn;32GBTPJSONs nicht blind kopieren.",
  "sources": [
    "VLLM_REPORT",
    "VLLM_IMPLEMENTATION"
  ],
  "test_design": "Später nur bei passendemMoE: andereKernelparameter festhalten, K128vs64 samtCompilerressourcen/Spills/Numerik undE2E prüfen.",
  "title": "FP16-MoE K128→64"
}
```

</details>

## R340-S06

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "C11",
    "HBM06",
    "HBM02",
    "Q03",
    "E03"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "DEFERRED_EXECUTION_FORMAT_AND_MODEL_ADMISSION",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S06",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "E4M3-Speicher mitFP16-Rechnung; Block128/N,K-aligned TurboMinds884, sonstCUDA-CoreFallback. Anders alsGGUFQ6 und vorhandenerConversioncache.",
  "next_action": "Kein Engineinstall/Gewichtsumbau/Port; statischeAnwendbarkeit zuerst.",
  "prerequisites": "PassenderFP8Checkpoint/Scales/Loader, lokaleAlignmentprüfung, korrekterHybrid/GDNGraph,16GBPeakbudget/Scratch. Kein passendesGewicht zugelassen.",
  "priority_band": "P2",
  "risks": "Keine nativenFP8TensorCores; FP8 kann mehrGewichtsspeicher alsQ6 brauchen; FastMath/FP16 könnenToken/Toolantworten verändern; CTBlockMoE imPin nicht unterstützt.",
  "sources": [
    "VLLM_IMPLEMENTATION",
    "VLLM_REPORT"
  ],
  "test_design": "Erst statischeShape/Format-Gates; festeTensor-/Scale-/Tail-Numerik gegenReferenz. Später innerhalbgleichenFP8Modells ours/TurboMind; Q6vsFP8 ist separateGesamtkonfiguration mitQualitysuite.",
  "title": "Block-FP8 W8A16 fused Dequant/TurboMindSM70"
}
```

</details>

## R340-S07

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM18",
    "C05",
    "K05",
    "E03"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "CURRENT_LLAMA_CPP_API_NOT_DROP_IN_COMPATIBLE_WITH_PINNED_PAGED_VLLM_ADAPTER; MODEL_ENGINE_DEPENDENT",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S07",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Adapter prüftFP16KV, HeadDim128/256, Seitenlayout undQ-Contiguity; Prefill anders geroutet alsDecode. SeparateImplementierung zu llama.cppFA.",
  "next_action": "Reassess only after model/engine admission; require compatible paged KV or an explicit correct adapter, partial-RoPE and hybrid-GDN state correctness, SM70 dispatch and memory gate. No GPU timing before numerical integration passes.",
  "prerequisites": "KonkreteAttentionlayouts/Shapes, gepinnteFA-Abhängigkeit mitTilefix undCUDA12.6Softcap-Kompatibilität, kein stillerFallback.",
  "priority_band": "P1",
  "risks": "Nicht annehmen,dass llama.cpp gleicheBugs hat; GDN nicht durchAttentionShim ersetzen; schnellePrefill-Ausgabe kann falsch sein.",
  "sources": [
    "VLLM_IMPLEMENTATION",
    "VLLM_REPORT"
  ],
  "test_design": "CPU Layoutmapping. Bei später zugelassenemBackend: gemischte nichtkontiguierlicheSeiten,QKVsplit-Strides,Sq<SkPrefix/ChunkCausal,Ausgabestrides/Tails gegenNumerikreferenz; dannLangkontextsemantik/QA/E2E/VRAM/Energie.",
  "title": "FlashAttention-V100: Seiten, Strides und Causal-Masken"
}
```

</details>

## R340-S08

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM05",
    "HBM06",
    "HBM07",
    "HBM19"
  ],
  "classification": "DEFERRED",
  "counts_as_factor": false,
  "decision": "TECHNICALLY_DEFERRED_ELECTRICAL_EFFECT_NOT_IDENTIFIABLE",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S08",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "HBM-Bank-/Busstrom ist nicht dieNVML-Gesamtleistung.",
  "next_action": "PraktischeVerkehrs-/Lokalitätsarbeit in bestehendenAchsen fortführen.",
  "prerequisites": "SeparateHBMRailmessung odervalidierterCommandtrace mitkalibriertemPowerModell; interneCommand/Banksteuerung wieFPGA-Plattform fehlt.",
  "priority_band": "P3",
  "risks": "NVML erlaubt keine eindeutigeHBM-Zuordnung; keineGewichts-/Semantikänderung oderPowerVirus fürMuster.",
  "sources": [
    "HBM_POWER"
  ],
  "test_design": "Nur mit zukünftiger Instrumentierung Befehlszahlen/Timing festhalten undTogglepattern isolieren. Jetzt ausschließlichGesamtGPU-J undAufgabenerfolge ausweisen.",
  "title": "HBM2-interne Datenmusterenergie separat messen"
}
```

</details>

## R340-S09

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM01",
    "HBM02",
    "HBM03",
    "HBM04",
    "HBM05",
    "HBM06",
    "HBM07",
    "HBM19"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "KEEP_EXISTING_SCOPED_RESULTS",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S09",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Weniger redundanterVerkehr ist eine prüfbareHypothese, kein ausPapers ableitbarerGewinn.",
  "next_action": "Nur konkreteungetesteteÄnderung zulassen.",
  "prerequisites": "Eigenständiger kompatiblerQ6Kernel/Cachepatch überbisherigeVarianten hinaus.",
  "priority_band": "P1",
  "risks": "Nicht unabhängigeProzente addieren; berechneteGewichtsbytes sindkeinegemessenenTransaktionen.",
  "sources": [
    "HBM_POWER",
    "BANDWIDTH_BLOG",
    "VOLTA_GUIDE"
  ],
  "test_design": "HBM07/H03Ergebnisse nutzen; bei neuemEinzelpatch tatsächlicheDRAMBytes nur perzugelassenemCounter, Prefill/Decode getrennt, NVMLIntegral undErfolge. J/Erfolg beiNullErfolgen undefiniert.",
  "title": "Coalescing/Reuse und GPU-J pro Erfolg"
}
```

</details>

## R340-S10

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "H03",
    "H04"
  ],
  "classification": "ALREADY_COVERED",
  "counts_as_factor": false,
  "decision": "NO_NEW_CLOCK_OR_POWER_SWEEP",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S10",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Leistungsgrenze und tatsächlicherBoost getrennteFaktoren; bestehendeProfile gelten.",
  "next_action": "Keine Wiederholung ohnekonkreteUrsache.",
  "prerequisites": "NeueeigenständigeHypothese, unterstützterModus undRollback.",
  "priority_band": "P2",
  "risks": "KeineDesktopClockwerte/Undervolting/Fanänderungen übertragen.",
  "sources": [
    "ARCHWIKI",
    "BANDWIDTH_BLOG"
  ],
  "test_design": "R167 undH03 wiederverwenden; neueunabhängigeFaktoren weiteram300WBasisprofil. Angefragte1312MHz sindkein tatsächlicherLock.",
  "title": "Power-/Application-Clocks"
}
```

</details>

## R340-S11

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "H04",
    "H05"
  ],
  "classification": "NOT_APPLICABLE",
  "counts_as_factor": false,
  "decision": "NOT_APPLICABLE_CURRENT_HEADLESS_SCOPE",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S11",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Desktop-Konfiguration ist kein Inferenzkernel und betrifft geschützteHost-/Kühlungskonfiguration.",
  "next_action": "KeineXorg/Coolbits/Bootserviceänderung.",
  "prerequisites": "Andere explizit freigegebeneHardware/Desktopfragestellung.",
  "priority_band": "P3",
  "risks": "Produktiv-/Kühlungseingriff ohne eigenständigeModellhypothese.",
  "sources": [
    "ARCHWIKI"
  ],
  "test_design": "KeinVersuch in diesemScope.",
  "title": "Xorg/Coolbits/Fan- und Bootrezepte"
}
```

</details>

## R340-S12

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "H06",
    "E03"
  ],
  "classification": "NOT_APPLICABLE",
  "counts_as_factor": false,
  "decision": "NOT_APPLICABLE_SINGLE_V100",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S12",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Vier/acht32GBKarten haben andereKapazität/Kommunikation als eine16GBV100.",
  "next_action": "Nur konkreteImplementierungsideen übernehmen.",
  "prerequisites": "MehrereKarten und passendeFreigabe; nichtvorhanden.",
  "priority_band": "P3",
  "risks": "Flottengeschwindigkeit ist keinlokalerSpeedup.",
  "sources": [
    "REDDIT_LEAD",
    "VLLM_REPORT"
  ],
  "test_design": "Nicht linear herunterrechnen; nur einzelnpassendeModelle später prüfen.",
  "title": "Mehrkarten-NVLink-Headlines"
}
```

</details>

## GIST-V01

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "E06",
    "HBM01"
  ],
  "classification": "ALREADY_COVERED",
  "counts_as_factor": false,
  "decision": "CORRECT_SOURCE_SUMMARY_NO_GPU_TEST",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V01",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Full die design has84SM; localread-only driverquery exposes80activeSM,4096-bitbus,96KiBshared/SM. NVIDIA lists8x512-bitcontrollers, not gist4x512.",
  "next_action": "Retain actual80SM and existing roofline-method limits.",
  "prerequisites": "Use actual device attributes, not full-die diagram counts.",
  "priority_band": "P3",
  "risks": "900GB/s is theoretical board bandwidth; not observed model traffic.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "No benchmark for an inventory correction.",
  "title": "GV100 design limits versus installed V100"
}
```

</details>

## GIST-V02

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM07",
    "HBM04",
    "HBM18"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "DEFERRED_SELECTED_Q6_DECODE_ALREADY_MINIMUM_SHARED",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V02",
  "local_test_status": "EXISTING_SAME_BUILD_TRACE_RESOURCE_REVIEW_NO_NEW_GPU_TEST",
  "mechanism": "Combined128KiB L1/shared resource with selectable shared capacities; preferred carveout is an advisory CUDAfunctionattribute, distinct from conversioncache or MaxDynamicSharedMemorySize.",
  "next_action": "Deferred for the current practical single-factor queue: synthetic 505-token prompt is not ranking eligible and the 2K/4K/decode trace bounds are below the 3% practical screen gate. Reopen only with a frozen representative workload where this exact kernel contributes >=3% of E2E and the preference demonstrably changes its runtime configuration.",
  "prerequisites": "Reopen only for a different actual kernel/launch with demonstrably nonminimal driver-shared configuration and a useful compatible preference change. Same-build trace and CUDA12.8CUPTI field semantics are pinned.",
  "priority_band": "P2",
  "risks": "Preference may map to same physical partition or be overridden by dynamic shared needs; no assumed occupancy, cachehit, bandwidth or speedup.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "Query originalfunction resources under the broker, then at mostone preference treatment with unchanged device code/math/layout/launch. Native input/output oracle before B-only model-screen; all actualattributes, shared requirement and timing limits archived.",
  "title": "Per-kernel L1/shared-memory carveout"
}
```

</details>

## GIST-V03

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "C09",
    "C10",
    "C18",
    "HBM03",
    "HBM04"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "NO_CONCRETE_NEW_PATCH_NO_GENERIC_COUNTER_RUN",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V03",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Volta has separate FP32/INT32 issue resources; address/arithmetic scheduling can matter. Four schedulers are not a four-resident-warp limit.",
  "next_action": "Reuse current tiling/warp negatives; reopen for an independently specified scheduling patch.",
  "prerequisites": "A distinct code-generation/data-dependency change with actual source/SASS and a real hotpath, not added dummy integer work.",
  "priority_band": "P2",
  "risks": "Static instruction presence is not measured dual-issue utilization or speedup.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "Only attach profiling to a proposed kernel patch; preserve registers/precision and independent numerics.",
  "title": "FP32 and INT32 pipeline overlap"
}
```

</details>

## GIST-V04

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "C13",
    "C14",
    "K05",
    "HBM05"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "ALREADY_IN_CORRECTNESS_ADMISSION_NO_REPEAT",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V04",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Explicit active masks/barriers are correctness requirements when exchanging data. Cooperative groups express valid synchronization but are not a free cross-grid speedup.",
  "next_action": "Keep existing native negatives and test synchronization only with a concrete new patch.",
  "prerequisites": "Specific changed synchronization path; grid-wide cooperative launches additionally require supported launch/residency contract.",
  "priority_band": "P1",
  "risks": "No inference that existing E09/state failures are caused by warp synchronization; no source-only correctness certificate.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "Reuse R340-S02 correctness gate; divergent/tail/state oracle only for a changed kernel.",
  "title": "Independent thread scheduling and Cooperative Groups"
}
```

</details>

## GIST-V05

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM14",
    "H10",
    "R13",
    "K06"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "KEEP_TRANSFER_PREREQUISITES_NO_REDO_R373",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V05",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Volta page-fault-capable copy engines do not imply that pinned hostbuffers have no benefit. CUDA12.8 best-practices separately documents pinned transfer bandwidth and async-overlap conditions.",
  "next_action": "Reuse managed-memory negative and offload results; require a real transfer/overlap patch.",
  "prerequisites": "Actual transfer-dominated workload, bounded private pinned buffers and measured packing/pinning/lifetime cost.",
  "priority_band": "P2",
  "risks": "Gist no-speedup anecdote has no matching local workload; pageable copies do not prove asynchronous overlap.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "Only compare a real staging implementation with equal bytes/direction/cache state and full allocation cost; not another residency/offload flag test.",
  "title": "Pinned/pageable transfers and staging"
}
```

</details>

## GIST-V06

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "H06",
    "H10"
  ],
  "classification": "NOT_APPLICABLE",
  "counts_as_factor": false,
  "decision": "NOT_APPLICABLE_CURRENT_TOPOLOGY_ONLY",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V06",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Whitepaper describes ATS over NVLink and IBM Power platform support. CurrentsingleV100 x86_64profile does not supply that CPU-GPU topology.",
  "next_action": "Retain CUDAmanagedmemory measurements; no productive topology or IOMMU changes.",
  "prerequisites": "Different host/interconnect with verified platform capability.",
  "priority_band": "P3",
  "risks": "Do not extrapolate to generic Linux/x86 pageable-memory support or rule out all UnifiedMemory paths.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "No local ATS/NVLink flag sweep on the existing host.",
  "title": "POWER9 NVLink coherency and ATS"
}
```

</details>

## GIST-V07

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM02",
    "HBM07",
    "HBM18"
  ],
  "classification": "PARTIALLY_COVERED",
  "counts_as_factor": false,
  "decision": "HARDWARE_FEATURE_NOT_NEW_OPTIMIZATION",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V07",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Whitepaper explicitly states GV100 write caching. Store locality/cache reuse may affect memory work, but this hardware feature is already present without an enable flag.",
  "next_action": "No generic cachehint sweep without a concrete store-path hypothesis.",
  "prerequisites": "An actually redundant/store-bound target and a distinct supported store-layout/policy patch.",
  "priority_band": "P2",
  "risks": "Write-caching support does not establish storepolicy efficacy or measured HBM-energy reduction.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "Reuse current data-layout/cache evidence; independently check output bytes and physical counters only when tool access permits.",
  "title": "Write caching and global-store locality"
}
```

</details>

## GIST-V08

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "axes": [
    "HBM01",
    "HBM19"
  ],
  "classification": "ALREADY_COVERED",
  "counts_as_factor": false,
  "decision": "PRESERVE_ECC_GUARD_NO_NEW_TREATMENT",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V08",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "SECDED reliability and900GB/s theoretical HBM2 figures are hardware properties; currentguard captures ECC and board energy.",
  "next_action": "Keep ECC enabled and preserve energy-per-success methodology.",
  "prerequisites": "Existing hardware-safety and traffic-accounting contracts.",
  "priority_band": "P3",
  "risks": "HBM-internal energy and useful-task efficiency are not inferable from theoretical bandwidth/ECC bits.",
  "sources": [
    "WOLFRAM77_VOLTA_NOTES",
    "NVIDIA_VOLTA_WHITEPAPER",
    "VOLTA_GUIDE"
  ],
  "test_design": "No ECC-disable performance trial.",
  "title": "SECDED ECC and theoretical bandwidth"
}
```

</details>
