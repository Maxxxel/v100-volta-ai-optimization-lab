# Reproducing the results

## Export an exact measured configuration

```sh
python scripts/leaderboard.py --export-profile cfg-a4e9c9254a524b23fdc69375ec9877659abc32781e5119545b2accd73aedbc09 > profile.json
```

The JSON packet preserves the original immutable profile, ordered arguments, environment, request settings, model/quantization, weight and template hashes, engine build/binary/CUDA-library identities, recorded source/patch lineage and exact-profile benchmark audit views. Unknown fields stay `null`. Multiple views of one original measurement audit are grouped; their count is not a count of GPU jobs or independent generations. Different coding/tool configuration IDs are not silently merged.

**This is a specification, not a runnable launch or broker approval.** Replace redacted artifact/session placeholders only after verifying the corresponding assets. Requested flags do not prove an executed kernel/cache mode. No downloads, installations, model processes, broker submissions or production changes occur during export.

### Reproduction boundaries

- Obtain weights from the recorded publisher/revision under its license; no weights are distributed here.
- Exact template bytes, external draft artifacts and original engine dependencies must be supplied separately. The matched main-engine source package below supplies the archived patches and build identities; external dependencies and original build paths are not bundled. A bit-identical independent rebuild is **not established** by this packet.
- Locally retained original launch/configuration receipts remain authoritative. Redacted public bytes are not the hash of a private original launch.
- Full official tests require the exact registered dataset, task set, scorer and evaluation settings. Different templates, output limits, engines, quantization or sampling form another profile.
- Private development/Agent33 inputs are not redistributed. Exact public reproduction of those suites remains incomplete. A substitute must use a new experiment identity.
- A coding packet is not an Agent33 or tool-runtime qualification. Those original captures retain separate profile IDs/hashes and harness settings.

## Controlled Jarvis deployment proposal

**PROPOSAL ONLY — no production changes performed or implied.** [Role decisions and observed tradeoffs](configurations.md) are provisional. Official Terminal-Bench remains **NOT MEASURED**.

1. **Sandbox baseline:** retain the measured OmniCoder bartowski Q6 / MTP-OFF option for single-agent validation. Its local 28/33 result is not a safety certificate. Keep canonical OmniCoder, Nexus and Ornith as documented alternatives.
2. **Separate specialists:** Gemma4's existing nonthinking profile is a coding-quality option. OmniCoder MTP3 is a native-tool-specific option; its coding/Agent33 regression forbids promoting it to an allround profile. Qwen27 integrated MTP3 remains a larger alternative with measured VRAM/latency/energy tradeoffs.
3. **Stage exact assets and settings:** use the original matching role-specific capture. Verify weights, template, server, CUDA library and dependencies; retain measured context/output/batching/power. The packet alone does not admit a new binary or executable. Unknown or altered inputs require the existing source/build/execution review.
4. **Use the existing broker:** one GPU-heavy job; unchanged ECC, temperature, throttling, power and 14,336-MiB device-memory guards. Any research benchmark shares one 1,200-second TASK budget across all parts; startup and cleanup are separate. Existing research authorization remains valid within its policy.
5. **Shadow/simulated tools first:** enforce permissions deterministically outside the LLM. No productive Home Assistant, Proxmox or other real write actions. Record task completion, policy violations, recovery, end-to-end cost and failures. Do not retune on final official tests or repeat valid benchmarks without a distinct hypothesis.
6. **Release gate:** compare against the unchanged baseline, retain rollback artifacts, and obtain explicit production approval before changing a productive service or privileges. This proposal performs neither action.

Single-Agent remains the comparison baseline. R537's five paired cases do not justify Planner/Worker/Reviewer by default. Automatic specialist routing, real model-switch overhead and cold-start costs are **NOT QUALIFIED**; separate role recommendations do not prove that a routed system wins.

## Public documentation and data

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/validate.py
python -m unittest discover -s scripts
python scripts/render.py
mkdocs build --strict
```

The public byte manifest validates exported files; each audit separately identifies its retained original. Documentation regeneration must leave no unexplained changes. The role-comparison tests recompute the published assessment from public immutable history; no model inference is needed.

## A comparable GPU reproduction

Use one V100 SM70 with 16 GB, exact artifact and engine identities, role-specific native template/sampler/context/KV/state/batch/offload/threads, frozen tasks and scorer. Preserve warm/cold conditions and record actual power/clocks. Measure task success, response latency, prefill/decode, TTFT, memory, GPU energy and stability separately; unmeasured values remain missing.

Some historical runs lack complete public build recipes, uncertainty estimates or task-level data. Follow linked original audits and factor-specific prerequisites. No repository workflow starts GPU jobs.

## Pinned main-engine source package

**Source evidence, not a new optimization or GPU qualification.** Base commit `097cf33d9499b1eade67d51e16d7c75427e7b267`; `ea0c4c2c85fb183ec0fbd30a1af4e4275a18a064` is the separate historical comparison revision, not this build base. Original server SHA256 `08827111e1b856c38d7a3a46ef2d33b36f201d3de76afdf4ac60f061c97fce54`.

| Exact source asset | Bytes | SHA256 |
|---|---|---|
| [LICENSE.llama-cpp](assets/reproduction/LICENSE.llama-cpp) | 1078 | 94f29bbed6a22c35b992c5c6ebf0e7c92f13b836b90f36f461c9cf2f0f1d010d |
| [llama-grammar-prefill.h](assets/reproduction/llama-grammar-prefill.h) | 492 | e9b74f0ec484a3ec19bd0933099b957ce9688ce50cbcccca421ad9530c2e128d |
| [main-protocol.patch](assets/reproduction/main-protocol.patch) | 6494 | 69fd43355a882451812995e5cfb6eae8af2c01224c0c3d41ef75c73fbd6e8b45 |
| [numeric-fixtures.patch](assets/reproduction/numeric-fixtures.patch) | 893 | 479bd12d814663bc5caa4023e955ec94247b50bdf96fffa7b014ddba1a596585 |


Use a separate source checkout at the stated build-base commit, without model weights. Apply `main-protocol.patch`, place the supplied header at `include/llama-grammar-prefill.h`, and apply `numeric-fixtures.patch` for the recorded backend-test target. Verify the five resulting source hashes listed below before configuring. These steps are instructions for a new isolated tree; archived and productive trees must remain untouched.

Original upstream MIT copyright/permission notice is included. The protocol/header patch changes grammar-prefill handling; the separate numerical patch defines backend-test shapes, not a newly measured speedup. All bytes are bound to archived build/source receipts. No model weights, compiled binaries or NVIDIA libraries are redistributed.

Read-only checks match the retained patched sources. An independent fresh checkout/build and bit-identical rebuild have **not** been performed here. Compiler paths are explicitly remapped; external CUDA/system dependencies and CPU-native build conditions still matter. A rebuilt binary has a new identity and needs the existing source/build/admission review before research execution.

??? note "Recorded toolchain, configure arguments and runtime-library identities"

    Recorded compiler jobs: 1. Configure in a separate unprivileged build directory against the pinned source; do not patch a productive or archived tree. Obtain the listed toolchain separately and map compiler paths explicitly. Build targets recorded in the original recipe: `llama-server` and `test-backend-ops`. These are reproduction instructions, not commands executed by this publication.

    | Tool | Recorded version |
    |---|---|
    | c++ | c++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 |
    | cc | cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 |
    | cmake | cmake version 3.28.3 |
    | nvcc | Cuda compilation tools, release 12.8, V12.8.93 |


    ```json
    {
      "cmake_flags": [
        "-DCMAKE_BUILD_TYPE=Release",
        "-DCMAKE_CUDA_ARCHITECTURES=70",
        "-DCMAKE_CUDA_COMPILER=${CUDA_ROOT}/bin/nvcc",
        "-DCMAKE_CUDA_FLAGS=",
        "-DCMAKE_CUDA_FLAGS_RELEASE=-O3 -DNDEBUG",
        "-DCMAKE_CXX_COMPILER=c++",
        "-DCMAKE_CXX_FLAGS=",
        "-DCMAKE_CXX_FLAGS_RELEASE=-O3 -DNDEBUG",
        "-DCMAKE_C_COMPILER=cc",
        "-DCMAKE_C_FLAGS=",
        "-DCMAKE_C_FLAGS_RELEASE=-O3 -DNDEBUG",
        "-DFETCHCONTENT_FULLY_DISCONNECTED=ON",
        "-DGGML_ACCELERATE=ON",
        "-DGGML_ALL_WARNINGS_3RD_PARTY=OFF",
        "-DGGML_AMX_BF16=OFF",
        "-DGGML_AMX_INT8=OFF",
        "-DGGML_AMX_TILE=OFF",
        "-DGGML_AVX=OFF",
        "-DGGML_AVX2=OFF",
        "-DGGML_AVX512=OFF",
        "-DGGML_AVX512_BF16=OFF",
        "-DGGML_AVX512_VBMI=OFF",
        "-DGGML_AVX512_VNNI=OFF",
        "-DGGML_AVX_VNNI=OFF",
        "-DGGML_BACKEND_DL=OFF",
        "-DGGML_BLAS=OFF",
        "-DGGML_BLAS_VENDOR=Generic",
        "-DGGML_BMI2=OFF",
        "-DGGML_BUILD_EXAMPLES=OFF",
        "-DGGML_BUILD_TESTS=OFF",
        "-DGGML_CCACHE=ON",
        "-DGGML_CPU=ON",
        "-DGGML_CPU_ALL_VARIANTS=OFF",
        "-DGGML_CPU_ARM_ARCH=",
        "-DGGML_CPU_HBM=OFF",
        "-DGGML_CPU_KLEIDIAI=OFF",
        "-DGGML_CPU_POWERPC_CPUTYPE=",
        "-DGGML_CPU_REPACK=ON",
        "-DGGML_CUDA=ON",
        "-DGGML_CUDA_CCCL_VERSION=",
        "-DGGML_CUDA_COMPRESSION_MODE=size",
        "-DGGML_CUDA_FA=ON",
        "-DGGML_CUDA_FA_ALL_QUANTS=OFF",
        "-DGGML_CUDA_FA_QUANTS=f16-f16;q8_0-q8_0",
        "-DGGML_CUDA_FORCE_CUBLAS=OFF",
        "-DGGML_CUDA_FORCE_MMQ=OFF",
        "-DGGML_CUDA_GRAPHS=ON",
        "-DGGML_CUDA_NCCL=ON",
        "-DGGML_CUDA_NO_PEER_COPY=OFF",
        "-DGGML_CUDA_NO_VMM=OFF",
        "-DGGML_ET=OFF",
        "-DGGML_ET_SYSEMU=OFF",
        "-DGGML_F16C=OFF",
        "-DGGML_FMA=OFF",
        "-DGGML_GPROF=OFF",
        "-DGGML_HEXAGON=OFF",
        "-DGGML_HIP=OFF",
        "-DGGML_HIP_EXPORT_METRICS=OFF",
        "-DGGML_HIP_GRAPHS=ON",
        "-DGGML_HIP_MMQ_MFMA=ON",
        "-DGGML_HIP_NO_VMM=ON",
        "-DGGML_HIP_RCCL=OFF",
        "-DGGML_LASX=ON",
        "-DGGML_LLAMAFILE=ON",
        "-DGGML_LSX=ON",
        "-DGGML_LTO=OFF",
        "-DGGML_METAL=OFF",
        "-DGGML_METAL_EMBED_LIBRARY=OFF",
        "-DGGML_METAL_MACOSX_VERSION_MIN=",
        "-DGGML_METAL_NDEBUG=OFF",
        "-DGGML_METAL_SHADER_DEBUG=OFF",
        "-DGGML_METAL_STD=",
        "-DGGML_METAL_TARGET_OS=macos",
        "-DGGML_MUSA=OFF",
        "-DGGML_MUSA_GRAPHS=OFF",
        "-DGGML_MUSA_MUDNN_COPY=OFF",
        "-DGGML_NATIVE=ON",
        "-DGGML_OPENCL=OFF",
        "-DGGML_OPENCL_EMBED_KERNELS=ON",
        "-DGGML_OPENCL_PROFILING=OFF",
        "-DGGML_OPENCL_TARGET_VERSION=300",
        "-DGGML_OPENCL_USE_ADRENO_KERNELS=ON",
        "-DGGML_OPENMP=ON",
        "-DGGML_OPENMP_FETCH=OFF",
        "-DGGML_OPENVINO=OFF",
        "-DGGML_RPC=OFF",
        "-DGGML_RVV=ON",
        "-DGGML_RV_ZFH=ON",
        "-DGGML_RV_ZICBOP=ON",
        "-DGGML_RV_ZIHINTPAUSE=ON",
        "-DGGML_RV_ZVFBFWMA=OFF",
        "-DGGML_RV_ZVFH=ON",
        "-DGGML_SANITIZE_ADDRESS=OFF",
        "-DGGML_SANITIZE_THREAD=OFF",
        "-DGGML_SANITIZE_UNDEFINED=OFF",
        "-DGGML_SCHED_MAX_COPIES=4",
        "-DGGML_SCHED_NO_REALLOC=OFF",
        "-DGGML_SSE42=OFF",
        "-DGGML_STATIC=OFF",
        "-DGGML_SYCL=OFF",
        "-DGGML_SYCL_DEVICE_ARCH=",
        "-DGGML_SYCL_DNN=ON",
        "-DGGML_SYCL_F16=OFF",
        "-DGGML_SYCL_GRAPH=ON",
        "-DGGML_SYCL_HOST_MEM_FALLBACK=ON",
        "-DGGML_SYCL_SUPPORT_LEVEL_ZERO_API=ON",
        "-DGGML_SYCL_TARGET=INTEL",
        "-DGGML_VIRTGPU=OFF",
        "-DGGML_VIRTGPU_BACKEND=OFF",
        "-DGGML_VULKAN=OFF",
        "-DGGML_VULKAN_CHECK_RESULTS=OFF",
        "-DGGML_VULKAN_DEBUG=OFF",
        "-DGGML_VULKAN_MEMORY_DEBUG=OFF",
        "-DGGML_VULKAN_RUN_TESTS=OFF",
        "-DGGML_VULKAN_SHADER_DEBUG_INFO=OFF",
        "-DGGML_VULKAN_VALIDATE=OFF",
        "-DGGML_VXE=ON",
        "-DGGML_WEBGPU=OFF",
        "-DGGML_WEBGPU_CPU_PROFILE=OFF",
        "-DGGML_WEBGPU_DEBUG=OFF",
        "-DGGML_WEBGPU_GPU_PROFILE=OFF",
        "-DGGML_WEBGPU_JSPI=ON",
        "-DGGML_XTHEADVECTOR=OFF",
        "-DGGML_ZDNN=OFF",
        "-DGGML_ZENDNN=OFF",
        "-DLLAMA_BUILD_APP=OFF",
        "-DLLAMA_BUILD_COMMON=ON",
        "-DLLAMA_BUILD_EXAMPLES=OFF",
        "-DLLAMA_BUILD_MTMD=OFF",
        "-DLLAMA_BUILD_SERVER=ON",
        "-DLLAMA_BUILD_TESTS=ON",
        "-DLLAMA_BUILD_TOOLS=ON",
        "-DLLAMA_BUILD_UI=OFF",
        "-DLLAMA_CURL=OFF",
        "-DLLAMA_LLGUIDANCE=OFF",
        "-DLLAMA_OPENSSL=ON",
        "-DLLAMA_SUBPROCESS=ON",
        "-DLLAMA_USE_PREBUILT_UI=OFF",
        "-DLLAMA_USE_SYSTEM_GGML=OFF"
      ],
      "remapped_compiler_paths": [
        "CMAKE_CUDA_COMPILER",
        "CMAKE_CXX_COMPILER",
        "CMAKE_C_COMPILER"
      ],
      "expected_runtime_libraries_sha256": {
        "libggml-base.so.0.26.0": "cbf2ea5528c20001bc483d9e146097a314480b17afdd23c89f2e611b85d96b14",
        "libggml-cpu.so.0.26.0": "c4bf75534b706bbbfaef7c9c0463572c5dc4f0e0a6269be62c35ced515b6de34",
        "libggml-cuda.so.0.26.0": "f76ecefe4dff5bb7bacf5721159b607f008d7f23b0fc848134637b6673b0e1f5",
        "libggml.so.0.26.0": "36d444fae53a4e0fdc2781d8f8cafa445c9162b46b9b815e227f83b312b2e0c8",
        "libllama-common.so.0.6.0": "99b2d9634b9c63168c07c3a9103a0f2051302b69bbd6cf1ab7e4d1f58d406e5d",
        "libllama-server-impl.so": "eb2b6f361f604c4e5d613c63d9595890d04a293082a0f5dccd91263747a3d3e0",
        "libllama.so.0.6.0": "0175c38f4b4e345199b756365061a9f25cf9f8b575c5b83399c4608dc3f06b78",
        "libmtmd.so.0.6.0": "3a02ba5a9a59be8000d7ae589354478dd603f0f11284e29e634386093c2e1468"
      },
      "patched_sources_sha256": {
        "common/sampling.cpp": "b6a1f963fd75fd17d12bafb59351a1009d2358dd789dba7ed10943340f8e5553",
        "include/llama-grammar-prefill.h": "e9b74f0ec484a3ec19bd0933099b957ce9688ce50cbcccca421ad9530c2e128d",
        "src/llama-sampler.cpp": "7cb48cf6acf423a269adbd101132d1f611f56ebb99f0a76a58eb326ebc89c66c",
        "tests/test-backend-ops.cpp": "0394b5b42d4467b28828dc1349dae038c9ee3f43422d49f4d200ccce9d03b686",
        "tests/test-sampling.cpp": "883d3baf07684aee5c92e67fb0632f43eff62ed333eab3bc48bb418a1c447923"
      }
    }
    ```

[Original reproduction receipt](audits/audit-eb3069a8e225c07360db.md). Local library/file hashes identify the measured build; they do not assert identical output from another compiler or host.

??? note "Selected exact benchmark-profile pointers"

    | Profile | Original benchmark capture | Exact export ID |
    |---|---|---|
    | OmniCoder 9B | [R471](experiments/R471.md) | [cfg-26d5b175a8e379f00193da2b2de4bce97c7d89fdc2bacf55b6971d71cb22f28e](configuration-profiles/cfg-26d5b175a8e379f00193da2b2de4bce97c7d89fdc2bacf55b6971d71cb22f28e.md) |
    | OmniCoder-9B · bartowski Q6 | [R516](experiments/R516.md) | [cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf](configuration-profiles/cfg-9e79c90dcc636fdd0f427f39bc378a1fc3a27ae4d2408c4a75d748df003ff1cf.md) |
    | Nexus 9B CodeCore Merge | [R488](experiments/R488.md) | [cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba](configuration-profiles/cfg-7f520b1330825ae5e48219c5056194ea305e706447fcefd2ae684397e67fdfba.md) |
    | Gemma4 12B IT QAT | [R464](experiments/R464.md) | [cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625](configuration-profiles/cfg-b3afa206e961953393b5942f2b885422942f5186753d25595edce11216c0b625.md) |
    | Qwen3.5 9B | [R465](experiments/R465.md) | [cfg-9fcb6193898540f39890fcfb16525895409d6b08f8de5165231fcbc0c17d2653](configuration-profiles/cfg-9fcb6193898540f39890fcfb16525895409d6b08f8de5165231fcbc0c17d2653.md) |
    | Qwen3.8 27B | [R466](experiments/R466.md) | [cfg-1bc9cefba6ba7b1aed15ea85f4d7bd445c08f43fd9328a4f727dbd9276051cb0](configuration-profiles/cfg-1bc9cefba6ba7b1aed15ea85f4d7bd445c08f43fd9328a4f727dbd9276051cb0.md) |
    | Ornith 1.5 9B | [R495](experiments/R495.md) | [cfg-45342fe50cda5030ead55e6e8fd149cf626f59305256cd7abd1470fa695ce655](configuration-profiles/cfg-45342fe50cda5030ead55e6e8fd149cf626f59305256cd7abd1470fa695ce655.md) |
    | OmniCoder-9B bartowski Q6 · MTP3 | [R542](experiments/R542.md) | [cfg-624ae7774142d9d42df292f10804a8b704b695ebfd094ad7d9494e641a6edf97](configuration-profiles/cfg-624ae7774142d9d42df292f10804a8b704b695ebfd094ad7d9494e641a6edf97.md) |
    | Qwen3.8 27B · integrated MTP3 | [R548](experiments/R548.md) | [cfg-a4e9c9254a524b23fdc69375ec9877659abc32781e5119545b2accd73aedbc09](configuration-profiles/cfg-a4e9c9254a524b23fdc69375ec9877659abc32781e5119545b2accd73aedbc09.md) |
