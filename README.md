# V100 Volta AI Optimization Lab

<p class="lab-eyebrow">Independent research · NVIDIA Volta / SM70</p>
<p class="lab-lead">Better local AI on one Tesla V100-SXM2 with 16 GB HBM2. We measure model quality, useful speed and GPU energy — with reproducible configurations and retained negative results.</p>

<div class="lab-actions"><a class="lab-button lab-primary" href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configuration-comparison/">Compare models</a><a class="lab-button" href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/archive/">Explore the research</a></div>

<div class="lab-kpis"><div><strong>162</strong><span>Research factors</span><small>130 original + 32 techniques</small></div><div><strong>113</strong><span>Experimentally covered</span><small>Factors, not GPU run count</small></div><div><strong>6</strong><span>Qualified factor scopes</span><small>Workload-specific evidence</small></div><div><strong>16 GB</strong><span>HBM2 on one V100</span><small>One GPU benchmark at a time</small></div></div>

## Research pipeline

**Model selection frozen through R585:** [OmniCoder allround · Gemma coding · Nexus worker](docs/final-selection.md). [All candidate decisions](docs/final-qualification.md). Next: separately scoped lean-harness research (#17/#18); no production deployment or exhaustive inference-tuning campaign.

[Best-of-V100 research decision](docs/best-of-v100-2026.md) · [Screening](docs/screening.md) → [Official qualification](docs/configuration-comparison.md) → [Targeted optimization](docs/configurations.md). Development screens stay outside official scores.

## Model comparison

<div class="lab-results"><a class="lab-result" href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configuration-profiles/cfg-3ba6be2510c3ae429ea93b13373010a1ff233d72b36d5c1b40ad0472efb6f5ff/"><span>Coding</span><strong>17/164</strong><b>Qwen3.5-0.8B</b><small>Latest complete result · R585</small></a><a class="lab-result" href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configuration-profiles/cfg-bf342cf0c82599f597854631d5a966963f80eee7c85a05ee0d2b69e4d91e7c15/"><span>Tools</span><strong>79/200</strong><b>Qwen3.5-0.8B</b><small>Latest complete result · R584</small></a><a class="lab-result" href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configuration-comparison/"><span>Agents</span><strong>Not measured</strong><b>Evaluator admission pending</b><small>No local score claimed</small></a></div>

Latest complete category measurements, not a ranking. [All configurations, costs and audits](docs/configuration-comparison.md).

## Optimization findings

<div class="lab-links"><a href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configurations/"><strong>Prefix reuse</strong><span>Lower latency with repeated context; not a universal decode gain.</span></a><a href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configurations/"><strong>HBM conversion cache</strong><span>Qualified prefill profiles with additional VRAM cost.</span></a><a href="https://maxxxel.github.io/v100-volta-ai-optimization-lab/configurations/"><strong>Energy profiles</strong><span>Measured trade-offs between task latency, memory and GPU joules.</span></a></div>

## Research progress

<div class="lab-status"><span><strong>6</strong> Qualified</span><span><strong>8</strong> Negative</span><span><strong>105</strong> Partial</span><span><strong>10</strong> Open</span><span><strong>28</strong> Deferred</span><span><strong>5</strong> Not applicable</span></div>

Reviewed, experimentally covered and qualified are separate stages. [Matrix and evidence](docs/matrix.md) · [Open questions](docs/questions.md).

<details><summary>Snapshot and methodology</summary>

Revision **435** · 2026-10-24. 511 sprint records, 61 immutable references and 12 scoped Champion pointers are separate inventories, not a count of independent GPU runs.

Benchmark task phase: **1,200 seconds total**, shared across all parts. Startup, wrapper and CPU evaluation limits are separate. Historical measurements retain their original conditions. [Methods](docs/methodology.md) · [Hardware](docs/hardware.md) · [Reproduce](docs/reproduce.md).

</details>

Independent community project; no affiliation with NVIDIA, Ollama or model publishers. Local measurements, external evidence and unverified hypotheses remain distinct. No universal winner is claimed.

## Documentation and collaboration

Build with `pip install -r requirements-docs.txt` and `mkdocs build --strict`. [Contribute](CONTRIBUTING.md) · [Reproduce](docs/reproduce.md) · [German overview](docs/de.md). Publishing never launches a GPU job.
