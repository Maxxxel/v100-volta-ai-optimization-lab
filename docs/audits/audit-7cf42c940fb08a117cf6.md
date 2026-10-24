# Public audit excerpt

Original SHA256: `7cf42c940fb08a117cf6e4bc8c02c1552e679c3592e3026ac27aa0ad91a6549c`

Original file: `research-metadata.json`; 15290 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "hypothesis": "A schema-specific stop at the closing object delimiter may avoid separateEOS generation. Receiver restores exactly the observed declared delimiter and validates the full object; no other repair or invented value. Measure both HTTP template/render and completion/framing cost.",
  "scope": "Fixed one-object enum decision schema, declared native stop delimiter and receiver framing only. Not arbitraryJSON/toolarguments or all M12 variants."
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "new_GPU_runs": 0
}
```

</details>
