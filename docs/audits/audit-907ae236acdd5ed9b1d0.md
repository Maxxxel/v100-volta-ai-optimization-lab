# Public audit excerpt

Original SHA256: `907ae236acdd5ed9b1d044abbf39d5fd0114186cd372e3276ddc283f4fa226d7`

Original file: `research-metadata.json`; 8530 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "Complete original164 tasks, same weights, engine, native template and T1/seed1001 sampling. Intended engine change: K-cache F16 to Q8_0, V remains F16. Controller preflight/HTTP-timeout policy also differs and is reported explicitly; stored-control configuration comparison, not a clean causal kernel/cache gain or fresh A/B repetition. Single stochastic seed is not equivalence. GPU-counter bounds include all failures, exclude load/warmup/CPU/system energy, and are not calibration confidence intervals. No task-driven tuning, model exclusion or Champion."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "model_requests": 0
}
```

</details>
