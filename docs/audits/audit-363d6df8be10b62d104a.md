# Public audit excerpt

Original SHA256: `363d6df8be10b62d104a478683a7bf40f58522409623c661a0de4479881bf2b6`

Original file: `INDEPENDENT_REVIEW.json`; 3306 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "PARTIAL_STARTUP_FAILURE; exact inner worker cause remains NOT_DETERMINED. The failure is bounded to after the llama-server reports model ready/listening and before INPUT_PREFLIGHT_COMPLETE/TASK_PHASE_BEGIN; no generation or draft-token execution occurred.",
  "interpretation": "Original GPU_ATTEMPT field launch_log_confirms_mtp=false conflicts with the hash-pinned LAUNCH.json (--spec-type draft-mtp and draft path) and server.log (draft-mtp implementation registered, draft model loaded, speculative context initialized). This addendum corrects that field only; it does not change the original report or claim MTP generation/acceptance.",
  "limitations": [
    "R602 CT_STDOUT.log is empty; CT_COMPLETION.json and ACTUAL_MAPS.txt were unavailable.",
    "LXC transient unit exited status 120; its journal contains no inner Python exception.",
    "Server readiness is logged; endpoint health response and prompt preflight completion are not separately recorded.",
    "No quality, decode speed, accepted draft-token, task latency, task energy, or champion result. Lease energy includes model load and teardown only.",
    "Do not retry the consumed single-use R602 contract. Any new test needs its own reviewed admission."
  ],
  "qualification": "MTP_INITIALIZATION_CONFIRMED_FROM_PINNED_LAUNCH_AND_SERVER_LOG; NO_TOKEN_LEVEL_MTP_EXECUTION"
}
```

</details>

## Selected aggregate measurements

NOT MEASURED / not included in the approved public schema.
