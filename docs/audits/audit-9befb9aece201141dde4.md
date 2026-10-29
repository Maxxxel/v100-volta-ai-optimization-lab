# Public audit excerpt

Original SHA256: `9befb9aece201141dde494721eebf4ae53e887754759d2d0c20f9769d7d4a954`

Original file: `AUDIT.json`; 4392 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "Three exposed fixed historical requests; two sequential model starts, ABBA then BAAB, identical actual input token IDs, same sampler and seed, no tool calls executed. Shared task time includes both startups and warmups; capped at 1100 seconds after conservatively reserving 100 seconds for the earlier failed R619 attempt. Not a full task quality or safety qualification; logits NOT MEASURED."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "peak_device_vram_mib": 7680.5
}
```

</details>
