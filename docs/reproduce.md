# Reproducing the results

## Export an exact measured configuration

```sh
python scripts/leaderboard.py --export-profile cfg-a4e9c9254a524b23fdc69375ec9877659abc32781e5119545b2accd73aedbc09 > profile.json
```

The JSON packet preserves the original immutable profile, ordered arguments, environment, request settings, model/quantization, weight and template hashes, engine build/binary/CUDA-library identities, recorded source/patch lineage and exact-profile benchmark audit views. Unknown fields stay `null`. Multiple views of one original measurement audit are grouped; their count is not a count of GPU jobs or independent generations. Different coding/tool configuration IDs are not silently merged.

**This is a specification, not a runnable launch or broker approval.** Replace redacted artifact/session placeholders only after verifying the corresponding assets. Requested flags do not prove an executed kernel/cache mode. No downloads, installations, model processes, broker submissions or production changes occur during export.

### Reproduction boundaries

- Obtain weights from the recorded publisher/revision under its license; no weights are distributed here.
- Exact template bytes, external draft artifacts and original engine dependencies must be supplied separately. Source/patch hashes identify retained inputs; patch bytes and the complete build dependency recipe are not fully public. A bit-identical independent rebuild is **not established** by this packet.
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
