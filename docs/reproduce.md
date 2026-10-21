# Reproducing the results

## Public documentation and data

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-docs.txt
python scripts/validate.py
mkdocs build --strict
```

All public pages are generated from `data/` by `python scripts/render.py`. Rerendering and validation must leave a clean worktree. `data/publication-manifest.json` verifies exported bytes; each audit receipt separately names the SHA256 of its unmodified retained original. Redacted bytes are not an original-audit hash proof.

## A comparable GPU reproduction

Use one V100 SM70 with 16 GB, the exact public weight repository and hash, pinned engine/build identities, context/KV/state/batch/offload/threads/sampler settings and frozen workload identity of the selected profile. Obtain weights from their licensed publisher; no weights are distributed here. Keep cold/warm conditions, power and actual clocks explicit. Reproduce the numerical oracle before an inference candidate and measure tasks, prefill, decode, TTFT, memory, energy and stability separately.

Use an isolated device and tool simulator. Do not apply example state or tool policies to production. No repository workflow starts a GPU job.

## Limits of this export

Private local task prompts, conversation outputs, simulator entities and infrastructure are intentionally withheld. Their retained hashes identify the original workload but do not provide its text. Thus exact independent task-level reproduction of those suites is **not yet fully public**. Public benchmark releases must be obtained under their own licenses, and any newly authored public substitute must receive a new profile identity; it cannot be passed off as the historical suite.

Some old measurements lack a complete public command/build recipe, confidence interval, numerical oracle or task-level data. Missing fields are not guessed. Follow the factor-specific prerequisites and open a Benchmark Reproduction issue when evidence is insufficient.
