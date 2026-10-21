# Scientific background

Volta optimization balances arithmetic intensity, HBM traffic, launch overhead and data reuse. Higher occupancy alone is not a target; register spilling can erase the benefit of a larger tile or more warps. Shared-memory banks and register banks are different mechanisms.

FP16 Tensor Core use depends on layout and instruction eligibility. Quantized GEMV, quantized GEMM, dequantized cuBLAS and recurrent GDN operations have different bottlenecks. Native FP8 Tensor Core results from newer hardware cannot be applied to SM70. W8A16 uses compressed storage plus supported arithmetic and has distinct format/loader requirements.

Hybrid models combine attention KV with recurrent states. A rollback of accepted attention tokens without equivalent recurrent-state restoration can be functionally wrong even if a primitive or synthetic throughput test passes. Token decisions, tools and policy outcomes must be checked.

The data-pattern HBM2 power paper studies separately instrumented memory. Board-level GPU energy cannot identify internal DRAM bus switching or memory-rail current. Actual DRAM-byte counters require compatible profiling, permission and an explicit hypothesis; weight bytes/time are not a traffic measurement.

See the [pinned source registry](sources.md) and [factor details](matrix.md). Published benchmarks, proven implementations and causal hypotheses are reported separately.
