# V100 Volta AI Optimization Lab

<p class="lab-eyebrow">Independent research · NVIDIA Volta / SM70</p>
<p class="lab-lead">Better local AI on one Tesla V100-SXM2 with 16 GB HBM2. We measure model quality, useful speed and GPU energy — with reproducible configurations and retained negative results.</p>

<div class="lab-actions"><a class="lab-button lab-primary" href="configuration-comparison/">Compare models</a><a class="lab-button" href="archive/">Explore the research</a></div>

<div class="lab-kpis"><div><strong>162</strong><span>Research factors</span><small>130 original + 32 techniques</small></div><div><strong>113</strong><span>Experimentally covered</span><small>Factors, not GPU run count</small></div><div><strong>6</strong><span>Qualified factor scopes</span><small>Workload-specific evidence</small></div><div><strong>16 GB</strong><span>HBM2 on one V100</span><small>One GPU benchmark at a time</small></div></div>

## Research pipeline

[Screening](screening.md) → [Official qualification](configuration-comparison.md) → [Targeted optimization](configurations.md). Development screens stay outside official scores.

## Model comparison

<div class="lab-results"><a class="lab-result" href="configuration-profiles/cfg-0826b77042cf7a110898c986ab209eeed23a2c3b3e6c3f22b914fc489ff601ad/"><span>Coding</span><strong>131/164</strong><b>OmniCoder-9B bartowski Q6 · MTP3</b><small>Latest complete result · R541</small></a><a class="lab-result" href="configuration-profiles/cfg-ef44057a9355a2b971bac6e5dcf6f018050b972a796a26c03d68c09af2e52049/"><span>Tools</span><strong>178/200</strong><b>OmniCoder-9B · bartowski Q6</b><small>Latest complete result · R517</small></a><a class="lab-result" href="configuration-comparison/"><span>Agents</span><strong>Not measured</strong><b>Evaluator admission pending</b><small>No local score claimed</small></a></div>

Latest complete category measurements, not a ranking. [All configurations, costs and audits](configuration-comparison.md).

## Optimization findings

<div class="lab-links"><a href="configurations/"><strong>Prefix reuse</strong><span>Lower latency with repeated context; not a universal decode gain.</span></a><a href="configurations/"><strong>HBM conversion cache</strong><span>Qualified prefill profiles with additional VRAM cost.</span></a><a href="configurations/"><strong>Energy profiles</strong><span>Measured trade-offs between task latency, memory and GPU joules.</span></a></div>

## Research progress

<div class="lab-status"><span><strong>6</strong> Qualified</span><span><strong>8</strong> Negative</span><span><strong>105</strong> Partial</span><span><strong>10</strong> Open</span><span><strong>28</strong> Deferred</span><span><strong>5</strong> Not applicable</span></div>

Reviewed, experimentally covered and qualified are separate stages. [Matrix and evidence](matrix.md) · [Open questions](questions.md).

<details><summary>Snapshot and methodology</summary>

Revision **435** · 2026-10-24. 460 sprint records, 60 immutable references and 12 scoped Champion pointers are separate inventories, not a count of independent GPU runs.

Benchmark task phase: **1,200 seconds total**, shared across all parts. Startup, wrapper and CPU evaluation limits are separate. Historical measurements retain their original conditions. [Methods](methodology.md) · [Hardware](hardware.md) · [Reproduce](reproduce.md).

</details>

Independent community project; no affiliation with NVIDIA, Ollama or model publishers. Local measurements, external evidence and unverified hypotheses remain distinct. No universal winner is claimed.
