# Open questions & research proposals

These are hypotheses or admission plans, never claimed local improvements. They extend existing axes and do not increase the factor count. GPU execution remains behind the single-factor and safety gates.

| Subcase | Public research issue | Status |
|---|---|---|
| R340-S01 | [Research: targeted SM70 resource/traffic profiling for a distinct kernel patch](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/1) | OPEN_HYPOTHESIS_NOT_GPU_ADMISSION |
| R340-S03 | [Research: admit one SM70 vLLM source lane only after model and memory gates](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/2) | OPEN_HYPOTHESIS_NOT_GPU_ADMISSION |
| R340-S06 | [Research: evaluate block-FP8 W8A16 fused dequantization on SM70](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/3) | OPEN_HYPOTHESIS_NOT_GPU_ADMISSION |
| R340-S07 | [Research: flash-attention V100 page/stride and causal-mask correctness](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/issues/4) | OPEN_HYPOTHESIS_NOT_GPU_ADMISSION |


## R340-S01

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

## R340-S02

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

## R340-S03

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

## R340-S04

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

## R340-S05

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

## R340-S06

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

## R340-S07

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
  "decision": "NEW_CORRECTNESS_SUBCASE_NOT_ADMITTED_PORT",
  "expected_knowledge_gain": "Unterschied zum bisherigen Pfad, Engpass oder Kompatibilität prüfen; zusätzlicher lokaler Nutzen NICHT VERIFIZIERT.",
  "id": "R340-S07",
  "local_test_status": "NO_NEW_GPU_TEST",
  "mechanism": "Adapter prüftFP16KV, HeadDim128/256, Seitenlayout undQ-Contiguity; Prefill anders geroutet alsDecode. SeparateImplementierung zu llama.cppFA.",
  "next_action": "Invarianten am passenden zukünftigenBackend prüfen; vorhandenenFA-Pfad erhalten.",
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

## R340-S08

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

## R340-S09

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

## R340-S10

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

## R340-S11

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

## R340-S12

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

## GIST-V01

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

## GIST-V02

```json
{
  "axes": [
    "HBM07",
    "HBM04",
    "HBM18"
  ],
  "classification": "NEW_SUBCASE",
  "counts_as_factor": false,
  "decision": "ADMIT_BOUNDED_SOURCE_RESOURCE_FEASIBILITY_NOT_GPU_RUN",
  "expected_knowledge_gain": "Identify a distinct compatible treatment, not a source-derived speedup.",
  "id": "GIST-V02",
  "local_test_status": "SOURCE_ADMISSION_ONLY_NO_NEW_GPU_TEST",
  "mechanism": "Combined128KiB L1/shared resource with selectable shared capacities; preferred carveout is an advisory CUDAfunctionattribute, distinct from conversioncache or MaxDynamicSharedMemorySize.",
  "next_action": "Inspect one dominant originalkernel resource/launch contract. No partitiongrid, no retest of HBM07 conversioncache.",
  "prerequisites": "Choose one executed SM70 kernel/shape; identify actual static/dynamic shared usage and resident-block limits before selecting a meaningfully different compatible preference.",
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

## GIST-V03

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

## GIST-V04

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

## GIST-V05

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

## GIST-V06

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

## GIST-V07

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

## GIST-V08

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
