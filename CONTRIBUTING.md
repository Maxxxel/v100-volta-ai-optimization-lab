# Contributing

Use a research issue template. State architecture, GPU memory, engine/build,
weight/tokenizer hashes, context, KV/state formats and cache conditions. Separate
published evidence, a hypothesis, measured screening and independent qualification.

For a result, include an isolated intervention, baseline identity, task count,
quality, latency, memory, energy, uncertainty, numerical checks and failures.
Do not upload private prompts, infrastructure, credentials or unlicensed test data.
Do not alter historical negative results silently. Submit a scientific correction
with the original audit ID, old interpretation and new evidence.

Run `python scripts/render.py`, `python -m unittest discover -s scripts`,
`python scripts/validate.py --write-manifest` and `mkdocs build --strict`.
Review the actual diff before proposing publication. No CI job runs a GPU test.
