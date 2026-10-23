# All Results & Configurations

## All measured results

One row per measured configuration. Tuning parameters are on the left; HumanEval+, BFCL and MBPP+ results are on the right. **Asterisk: subset. Dagger: historical scorer protocol.** Unmarked values passed the declared local official-benchmark admission. Click a model for full parameters, metrics and audits. Additional tuning columns are optional. No combined score. Unknown values remain **NOT MEASURED**.

<div id="all-measured-results" aria-live="polite"></div>

## Compare selected configurations

Select two or more **measured result profiles**, including weaker configurations. Differences describe complete tested profiles. A causal claim about MTP, quantization or another factor requires a dedicated isolated experiment.

<div id="configuration-comparison" aria-live="polite"></div>

## Full configuration history

The searchable history also contains failed or declared attempts, clearly distinguished from observed inference. An attempt without benchmark output is not a scored run. Missing fields remain **NOT MEASURED**.

<div id="configuration-history"></div>

Machine-readable [configuration history](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/configuration-history.json) is append-only. Changed metadata require a new profile identity; old results and original audit hashes remain retained.

## Provenance gaps — excluded from reconstructed profiles

| Experiment | Reason | Original audit |
| --- | --- | --- |
| R408 | Current historical plan differs from its original precheck pin; configuration not reconstructed from mismatched bytes. Original audit remains preserved. | [audit-74e8e58e72e5b8769e71](audits/audit-74e8e58e72e5b8769e71.md) |

