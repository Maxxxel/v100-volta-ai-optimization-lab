# Public audit excerpt

Original SHA256: `bba2d068363f59d27bc0b24e0da0c3334038c24906d17fa0f319c30d061e499f`

Original file: `AUDIT.json`; 4538 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "decision": "FULL200_CATEGORY_COLLECTED_AND_OFFICIAL_AST_REPLAYED_NO_CHAMPION",
  "evidence_class": "LOKAL_GEMESSEN",
  "limits": [
    "Full parallel_multiple200 category only, not BFCL overall. Official AST and practical protocol remain distinct.",
    "Nonstream complete-HTTP request windows for GPU energy and wall time; loading/warmup/CPU/system energy excluded; no TTFT measurement.",
    "Gemma4 QAT Q4_0 with K=q8_0,V=f16; stored F16 reference R472. No fresh balanced control or speedup claim.",
    "Category-aware source-reviewed scorer wrapper conservatively prints full_category_claimed=false; independent qualification requires all200 unique original IDs and unchanged original question/tool source identities."
  ]
}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "model_starts": 1
}
```

</details>
