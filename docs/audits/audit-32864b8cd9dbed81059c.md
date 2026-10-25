# Public audit excerpt

Original SHA256: `32864b8cd9dbed81059c5ec13f58b4667b284253faee11c3e9cde40ccba3d31a`

Original file: `research-metadata.json`; 1254 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "scope": "GPU executed captured selected_task_inputs fixtures (JSON-sorted mapping keys); scorer initialized from semantically equal archive fixtures with different insertion order. Simulated observation JSON strings then differed in key order, changing subsequent exact request bytes. Replay now initializes from the exact captured profile fixture after verifying equality with the frozen archive. No request normalization, prompt/oracle/answer/weight/score-rule changes. Original failed replay and raw GPU capture remain intact."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "solved": 26
}
```

</details>
