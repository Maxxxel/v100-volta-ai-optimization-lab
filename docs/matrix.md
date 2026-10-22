# Optimization matrix

130 original factors plus 32 additional technique subcases; model candidates, research sources and signed test windows are separate inventories. Each row links to theory, evidence, variants, decisions and reopening conditions.

| ID | Technique | Status | Experimentally covered | Priority |
|---|---|---|---|---|
| [R01](factors/R01.md) | CPU Threads | PARTIAL | YES | P2 |
| [R02](factors/R02.md) | Threads Batch | PARTIAL | YES | P2 |
| [R03](factors/R03.md) | Logical Batch | PARTIAL | YES | P2 |
| [R04](factors/R04.md) | Microbatch | QUALIFIED | YES | P0 |
| [R05](factors/R05.md) | Parallel Slots | PARTIAL | YES | P2 |
| [R06](factors/R06.md) | FlashAttention | PARTIAL | YES | P2 |
| [R07](factors/R07.md) | Cache RAM MiB | PARTIAL | YES | P2 |
| [R08](factors/R08.md) | Cache Reuse | PARTIAL | NO | P2 |
| [R09](factors/R09.md) | Context Shift | PARTIAL | NO | P2 |
| [R10](factors/R10.md) | KV unified | PARTIAL | YES | P2 |
| [R11](factors/R11.md) | KV unified per slot | PARTIAL | YES | P1 |
| [R12](factors/R12.md) | Prompt caching | PARTIAL | YES | P2 |
| [R13](factors/R13.md) | GPU Residency | PARTIAL | YES | P2 |
| [R14](factors/R14.md) | mmap | PARTIAL | YES | P2 |
| [R15](factors/R15.md) | mlock | PARTIAL | YES | P1 |
| [R16](factors/R16.md) | NUMA policy | NOT_APPLICABLE | NO | P3 |
| [R17](factors/R17.md) | CPU Affinity | PARTIAL | YES | P2 |
| [R18](factors/R18.md) | Streaming | PARTIAL | YES | P2 |
| [R19](factors/R19.md) | Context Size | PARTIAL | YES | P1 |
| [R20](factors/R20.md) | Prompt Length | PARTIAL | YES | P2 |
| [R21](factors/R21.md) | Decode Length | PARTIAL | YES | P2 |
| [R22](factors/R22.md) | Warm State | PARTIAL | YES | P0 |
| [K01](factors/K01.md) | KV Type K | PARTIAL | YES | P1 |
| [K02](factors/K02.md) | KV Type V | PARTIAL | YES | P1 |
| [K03](factors/K03.md) | KV Type Paired | PARTIAL | YES | P2 |
| [K04](factors/K04.md) | FA Quant Kernel Coverage | PARTIAL | YES | P2 |
| [K05](factors/K05.md) | Recurrent State Sequence | PARTIAL | YES | P1 |
| [K06](factors/K06.md) | KV Offload | PARTIAL | YES | P2 |
| [K07](factors/K07.md) | Cache Compaction | PARTIAL | YES | P1 |
| [C01](factors/C01.md) | FORCE_MMQ | TESTED_NEGATIVE | YES | P3 |
| [C02](factors/C02.md) | FORCE_CUBLAS | PARTIAL | YES | P2 |
| [C03](factors/C03.md) | CUDA GRAPHS Compile | PARTIAL | YES | P2 |
| [C04](factors/C04.md) | GRAPH OPT C6C | PARTIAL | YES | P2 |
| [C05](factors/C05.md) | FlashAttention Compile | PARTIAL | YES | P2 |
| [C06](factors/C06.md) | CUDA NO VMM | PARTIAL | YES | P2 |
| [C07](factors/C07.md) | FA_QUANTS coverage | PARTIAL | YES | P2 |
| [C08](factors/C08.md) | cuBLAS compute type | PARTIAL | YES | P2 |
| [C09](factors/C09.md) | SM70 MMVQ warp dispatch | PARTIAL | YES | P2 |
| [C10](factors/C10.md) | SM70 MMQ tile width | PARTIAL | YES | P2 |
| [C11](factors/C11.md) | Dequant GEMM fusion | PARTIAL | YES | P2 |
| [C12](factors/C12.md) | RMSNorm RoPE Fusion | PARTIAL | YES | P2 |
| [C13](factors/C13.md) | Delta State Fusion | PARTIAL | YES | P2 |
| [C14](factors/C14.md) | FP16 / FP32 accumulation | PARTIAL | YES | P2 |
| [C15](factors/C15.md) | Binary Compression Mode | OPEN | NO | P2 |
| [C16](factors/C16.md) | CUDA Launch Queues | PARTIAL | YES | P2 |
| [C17](factors/C17.md) | CUDA Max Connections | PARTIAL | YES | P2 |
| [C18](factors/C18.md) | CUDA upstream patches | PARTIAL | YES | P2 |
| [H01](factors/H01.md) | Host CPU Pinning | PARTIAL | YES | P2 |
| [H02](factors/H02.md) | Host CPU Isolation | DEFERRED | NO | P3 |
| [H03](factors/H03.md) | V100 Power Limit | QUALIFIED | YES | P0 |
| [H04](factors/H04.md) | V100 Application Clocks | PARTIAL | YES | P0 |
| [H05](factors/H05.md) | Airflow Fan Cooling | DEFERRED | NO | P3 |
| [H06](factors/H06.md) | PCIe and Topology | DEFERRED | NO | P3 |
| [H07](factors/H07.md) | Swap Hugepages | DEFERRED | NO | P3 |
| [H08](factors/H08.md) | Model Page Cache | PARTIAL | YES | P1 |
| [H09](factors/H09.md) | CUDA MPS | DEFERRED | NO | P3 |
| [H10](factors/H10.md) | Unified GPU Memory | TESTED_NEGATIVE | YES | P3 |
| [Q01](factors/Q01.md) | GGUF Weight Family | PARTIAL | YES | P1 |
| [Q02](factors/Q02.md) | Importance Matrix | PARTIAL | YES | P2 |
| [Q03](factors/Q03.md) | Mixed Tensor Quant | PARTIAL | YES | P0 |
| [Q04](factors/Q04.md) | AWQ Calibration | OPEN | NO | P3 |
| [Q05](factors/Q05.md) | Outlier Tensor Retention | PARTIAL | YES | P1 |
| [Q06](factors/Q06.md) | Quant Format Kernel Compatibility | PARTIAL | YES | P0 |
| [Q07](factors/Q07.md) | QAT Checkpoint | OPEN | NO | P3 |
| [Q08](factors/Q08.md) | Selective Hybrid State Precision | PARTIAL | YES | P2 |
| [M01](factors/M01.md) | Native Thinking Budget | PARTIAL | YES | P2 |
| [M02](factors/M02.md) | Temperature | PARTIAL | YES | P2 |
| [M03](factors/M03.md) | TopK | PARTIAL | YES | P2 |
| [M04](factors/M04.md) | TopP | PARTIAL | YES | P2 |
| [M05](factors/M05.md) | MinP | PARTIAL | YES | P2 |
| [M06](factors/M06.md) | Repetition DRY | PARTIAL | YES | P2 |
| [M07](factors/M07.md) | Template variants | PARTIAL | YES | P2 |
| [M08](factors/M08.md) | Output Grammar | PARTIAL | YES | P0 |
| [M09](factors/M09.md) | Function Serialization | PARTIAL | YES | P2 |
| [M10](factors/M10.md) | Model Context Scaling | OPEN | NO | P2 |
| [M11](factors/M11.md) | System Prompt Placement | PARTIAL | YES | P2 |
| [M12](factors/M12.md) | Stop Tokens | OPEN | NO | P2 |
| [M13](factors/M13.md) | Tool Completion | PARTIAL | YES | P2 |
| [S01](factors/S01.md) | Ngram backend | PARTIAL | YES | P1 |
| [S02](factors/S02.md) | Ngram Max Draft Tokens | PARTIAL | YES | P1 |
| [S03](factors/S03.md) | Self Speculative MTP | QUALIFIED | YES | P0 |
| [S04](factors/S04.md) | Secondary Draft Model | PARTIAL | YES | P1 |
| [E01](factors/E01.md) | llama.cpp Revision | PARTIAL | YES | P2 |
| [E02](factors/E02.md) | Ollama Lab Runtime | PARTIAL | YES | P2 |
| [E03](factors/E03.md) | vLLM Compatibility | OPEN | NO | P3 |
| [E04](factors/E04.md) | TensorRT-LLM Compatibility | OPEN | NO | P3 |
| [E05](factors/E05.md) | ExLlama Compatibility | OPEN | NO | P3 |
| [E06](factors/E06.md) | SM70 Build Target | OPEN | NO | P2 |
| [E07](factors/E07.md) | CUDA Library Version | TESTED_NEGATIVE | YES | P2 |
| [E08](factors/E08.md) | Grammar Parser | PARTIAL | YES | P2 |
| [E09](factors/E09.md) | Scheduler Strategy | PARTIAL | YES | P1 |
| [A01](factors/A01.md) | Prefix and Schema Cache | PARTIAL | YES | P0 |
| [A02](factors/A02.md) | History Retrieval | PARTIAL | YES | P1 |
| [A03](factors/A03.md) | Harness Token Compression | PARTIAL | YES | P1 |
| [A04](factors/A04.md) | Tool Security Gate | PARTIAL | YES | P0 |
| [A05](factors/A05.md) | Planning Loop | PARTIAL | YES | P2 |
| [A06](factors/A06.md) | Code Test Harness | PARTIAL | YES | P0 |
| [A07](factors/A07.md) | Idempotency | PARTIAL | NO | P1 |
| [A08](factors/A08.md) | Context Compression | PARTIAL | YES | P1 |
| [T01](factors/T01.md) | LoRA QLoRA | OPEN | NO | P3 |
| [T02](factors/T02.md) | Domain Fine Tuning | OPEN | NO | P3 |
| [T03](factors/T03.md) | SVD Low Rank | OPEN | NO | P3 |
| [T04](factors/T04.md) | Pruning | OPEN | NO | P3 |
| [T05](factors/T05.md) | Distillation | OPEN | NO | P3 |
| [T06](factors/T06.md) | QAT Retraining | OPEN | NO | P3 |
| [T07](factors/T07.md) | Tensor Smoothing | OPEN | NO | P3 |
| [HBM01](factors/HBM01.md) | Effective bandwidth and roofline | PARTIAL | YES | P2 |
| [HBM02](factors/HBM02.md) | Coalesced and vectorized accesses | PARTIAL | YES | P2 |
| [HBM03](factors/HBM03.md) | SM70 MMVQ warp mapping | PARTIAL | YES | P2 |
| [HBM04](factors/HBM04.md) | SM70 MMQ tiles and warps | PARTIAL | YES | P2 |
| [HBM05](factors/HBM05.md) | Volta FP16 Tensor Core kernel | TESTED_NEGATIVE | YES | P3 |
| [HBM06](factors/HBM06.md) | Dequantization and GEMV/GEMM fusion | PARTIAL | YES | P2 |
| [HBM07](factors/HBM07.md) | L1/L2/shared-memory reuse | QUALIFIED | YES | P0 |
| [HBM08](factors/HBM08.md) | F16/Q8/Q4 attention KV cache | PARTIAL | YES | P1 |
| [HBM09](factors/HBM09.md) | KIVI asymmetric KV quantization | OPEN | NO | P3 |
| [HBM10](factors/HBM10.md) | KVQuant calibrated KV quantization | OPEN | NO | P3 |
| [HBM11](factors/HBM11.md) | Paged attention and KV blocks | OPEN | NO | P3 |
| [HBM12](factors/HBM12.md) | Asynchronous KV prefetch to L2 | PARTIAL | YES | P2 |
| [HBM13](factors/HBM13.md) | OasisKV sparse lookahead prefetch | OPEN | NO | P3 |
| [HBM14](factors/HBM14.md) | Host/PCIe/HBM staging | PARTIAL | YES | P2 |
| [HBM15](factors/HBM15.md) | VMM and allocator fragmentation | PARTIAL | YES | P2 |
| [HBM16](factors/HBM16.md) | Attention and recurrent-state memory | PARTIAL | YES | P2 |
| [HBM17](factors/HBM17.md) | Speculative decoding memory traffic | PARTIAL | YES | P2 |
| [HBM18](factors/HBM18.md) | Volta-specific flash attention | PARTIAL | YES | P2 |
| [HBM19](factors/HBM19.md) | Energy per correct task/token | PARTIAL | YES | P0 |
| [HBM20](factors/HBM20.md) | StreamDQ custom HBM | NOT_APPLICABLE | NO | P3 |
| [HBM21](factors/HBM21.md) | FlashAccel high-bandwidth flash | NOT_APPLICABLE | NO | P3 |
| [HBM22](factors/HBM22.md) | QServe W4A8KV4 | OPEN | NO | P3 |
| [HBM23](factors/HBM23.md) | FlashInfer attention engine | OPEN | NO | P3 |
| [HBM24](factors/HBM24.md) | Fork-specific experimental attention | NOT_APPLICABLE | NO | P3 |
| [BMT01](factors/BMT01.md) | Minimal tool-schema descriptions | TESTED_NEGATIVE | YES | P0 |
| [BMT02](factors/BMT02.md) | GDN/MTP rejection, prefix and slot-state correctness | PARTIAL | YES | P0 |
| [BMT03](factors/BMT03.md) | Adaptive MTP draft length | TESTED_NEGATIVE | YES | P1 |
| [BMT04](factors/BMT04.md) | Independent Q4/Q5/Q6 draft precision | TESTED_NEGATIVE | YES | P0 |
| [BMT05](factors/BMT05.md) | MTP-head GGUF graft packaging | QUALIFIED | YES | P1 |
| [BMT06](factors/BMT06.md) | Agent harness and bounded recovery | PARTIAL | YES | P1 |
| [BMT07](factors/BMT07.md) | Source-grounded retrieval | PARTIAL | YES | P0 |
| [BMT08](factors/BMT08.md) | Hybrid attention KV precision | PARTIAL | YES | P1 |
| [BMT09](factors/BMT09.md) | KV rotation and mean centering | TESTED_NEGATIVE | YES | P1 |
| [BMT10](factors/BMT10.md) | DP4A/ternary inference kernels | DEFERRED | YES | P2 |
| [BMT11](factors/BMT11.md) | Deployment-compatible QAD/QAT checkpoints | DEFERRED | NO | P2 |
| [BMT12](factors/BMT12.md) | MoE residency and expert prefetch | NOT_APPLICABLE | NO | P2 |
| [BMT13](factors/BMT13.md) | DFlash/DSpark drafting | DEFERRED | NO | P3 |
| [BMT14](factors/BMT14.md) | Verified trajectory distillation | DEFERRED | NO | P3 |
| [BMT15](factors/BMT15.md) | Sensitivity-guided rank/pruning | DEFERRED | NO | P3 |
| [BMT16](factors/BMT16.md) | Cold-load and specialist routing | DEFERRED | NO | P1 |
| [BMT17](factors/BMT17.md) | SM70 graphs and GDN fusion | PARTIAL | YES | P2 |
| [BMT18](factors/BMT18.md) | Independent tool authorization gates | PARTIAL | YES | P0 |
| [BMT19](factors/BMT19.md) | Looped transformer weight sharing | DEFERRED | NO | P3 |
| [BMT20](factors/BMT20.md) | LoopSplit, hyperconnections and depth attention | DEFERRED | NO | P3 |
| [BMT21](factors/BMT21.md) | Task/scaffold/rollout co-evolution | DEFERRED | NO | P3 |
| [BMT22](factors/BMT22.md) | Trajectory-level DPPO | DEFERRED | NO | P3 |
| [BMT23](factors/BMT23.md) | Weakness-directed cross-model training data | DEFERRED | NO | P2 |
| [BMT24](factors/BMT24.md) | Geometry-grounded OCR | DEFERRED | NO | P3 |
| [BMT25](factors/BMT25.md) | Action-grounded GUI policies | DEFERRED | NO | P3 |
| [BMT26](factors/BMT26.md) | Streaming cache-aware RNNT ASR | DEFERRED | NO | P3 |
| [BMT27](factors/BMT27.md) | Confidence calibration and selective tool use | PARTIAL | YES | P1 |
| [BMT28](factors/BMT28.md) | Stochastic recurrent-state rounding | DEFERRED | NO | P3 |
| [BMT29](factors/BMT29.md) | Adaptive reasoning budgets | PARTIAL | YES | P1 |
| [BMT30](factors/BMT30.md) | Learned ngram embeddings | DEFERRED | NO | P3 |
| [BMT31](factors/BMT31.md) | Q4/Q6 conversion-cache transfer | QUALIFIED | YES | P0 |
| [BMT32](factors/BMT32.md) | GQA/MQA/MLA and sparse/local attention | DEFERRED | NO | P2 |
