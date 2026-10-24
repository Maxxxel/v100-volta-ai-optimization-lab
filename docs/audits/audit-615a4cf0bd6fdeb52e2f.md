# Public audit excerpt

Original SHA256: `615a4cf0bd6fdeb52e2fd72b6ce1ff4d2614cd8528449e93cc3a24c76ba8b7e6`

Original file: `RESULTS.json`; 266289 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{}
```

</details>

## Selected aggregate measurements

<details class="lab-evidence"><summary>Structured evidence</summary>

```json
{
  "models": {
    "omnicoder2": {
      "metrics": {
        "A": {
          "correct_tokens": 562,
          "gpu_j_per_correct_token": 9.62730233848368,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470364160,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2691.2472876617953,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.216111653,
              "rss_peak_bytes": 7726669824,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470327296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2719.296626566033,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.087667603,
              "rss_peak_bytes": 7725207552,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5410.543914227828,
          "raw_requests": [
            {
              "begin_ns": 294087040189932,
              "complete": true,
              "e2e_s": 0.181803926,
              "end_ns": 294087221993858,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 43.25141800957551,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050824977,
                "rss_peak_bytes": 1471590400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.298,
                "predicted_n": 10,
                "predicted_per_second": 77.3874013310633,
                "predicted_per_token_ms": 12.922
              },
              "ttft_s": 0.065492802,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294087281632958,
              "complete": true,
              "e2e_s": 0.234588356,
              "end_ns": 294087516221314,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.26300018348343,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052602019,
                "rss_peak_bytes": 1471590400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 167.476,
                "predicted_n": 14,
                "predicted_per_second": 77.62306240894218,
                "predicted_per_token_ms": 12.882769230769231
              },
              "ttft_s": 0.067058103,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294087568083270,
              "complete": true,
              "e2e_s": 0.66577581,
              "end_ns": 294088233859080,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 173.36165448446823,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054074256,
                "rss_peak_bytes": 1471635456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.17,
                "predicted_n": 44,
                "predicted_per_second": 79.31091723998009,
                "predicted_per_token_ms": 12.60860465116279
              },
              "ttft_s": 0.123553857,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294088304159192,
              "complete": true,
              "e2e_s": 0.357225059,
              "end_ns": 294088661384251,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414101504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 85.24557785871772,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050959489,
                "rss_peak_bytes": 1471639552,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.862,
                "predicted_n": 23,
                "predicted_per_second": 78.89206847831544,
                "predicted_per_token_ms": 12.675545454545455
              },
              "ttft_s": 0.078300319,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294088736160322,
              "complete": true,
              "e2e_s": 0.295369196,
              "end_ns": 294089031529518,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414105600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.04281737391425,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051799755,
                "rss_peak_bytes": 1471643648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.536,
                "predicted_n": 18,
                "predicted_per_second": 78.50888535855469,
                "predicted_per_token_ms": 12.737411764705882
              },
              "ttft_s": 0.078789329,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294089105153577,
              "complete": true,
              "e2e_s": 0.468818723,
              "end_ns": 294089573972300,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469803008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 116.10419643377105,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050589098,
                "rss_peak_bytes": 1527341056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.341,
                "predicted_n": 29,
                "predicted_per_second": 79.01992713233862,
                "predicted_per_token_ms": 12.655035714285715
              },
              "ttft_s": 0.114452537,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294089647360388,
              "complete": true,
              "e2e_s": 1.075175587,
              "end_ns": 294090722535975,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470274048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 283.92835581576844,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054280981,
                "rss_peak_bytes": 1527812096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.882,
                "predicted_n": 21,
                "predicted_per_second": 77.85675913454426,
                "predicted_per_token_ms": 12.844100000000001
              },
              "ttft_s": 0.818264896,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294090794862072,
              "complete": true,
              "e2e_s": 0.197820957,
              "end_ns": 294090992683029,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417611776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.000687132718696,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053512406,
                "rss_peak_bytes": 1475149824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.197685998
            },
            {
              "begin_ns": 294091058126671,
              "complete": true,
              "e2e_s": 1.657678039,
              "end_ns": 294092715804710,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417611776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 442.21378272632745,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052181642,
                "rss_peak_bytes": 1475149824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.538,
                "predicted_n": 128,
                "predicted_per_second": 79.6468945863943,
                "predicted_per_token_ms": 12.555417322834646
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.06303449
            },
            {
              "begin_ns": 294092773580801,
              "complete": true,
              "e2e_s": 0.617042093,
              "end_ns": 294093390622894,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470331392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.47233100166108,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052164819,
                "rss_peak_bytes": 1527869440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.305,
                "predicted_n": 34,
                "predicted_per_second": 79.07885119996166,
                "predicted_per_token_ms": 12.645606060606061
              },
              "tool_call_valid": true,
              "ttft_s": 0.316059154,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294093448787496,
              "complete": true,
              "e2e_s": 0.558334532,
              "end_ns": 294094007122028,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470364160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 141.78334720328294,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052415223,
                "rss_peak_bytes": 1527902208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.945,
                "predicted_n": 25,
                "predicted_per_second": 78.70271688337242,
                "predicted_per_token_ms": 12.706041666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253370251,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294541266319817,
              "complete": true,
              "e2e_s": 0.182280894,
              "end_ns": 294541448600711,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 35.9918043401927,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050601759,
                "rss_peak_bytes": 1469190144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.261,
                "predicted_n": 10,
                "predicted_per_second": 77.4120298294355,
                "predicted_per_token_ms": 12.91788888888889
              },
              "ttft_s": 0.065993336,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294541527171980,
              "complete": true,
              "e2e_s": 0.23365044,
              "end_ns": 294541760822420,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 54.72249857164934,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.057065906,
                "rss_peak_bytes": 1469190144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.194,
                "predicted_n": 14,
                "predicted_per_second": 78.22183713010097,
                "predicted_per_token_ms": 12.784153846153846
              },
              "ttft_s": 0.067435319,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294541835049081,
              "complete": true,
              "e2e_s": 0.66665612,
              "end_ns": 294542501705201,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.54090487040983,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051513202,
                "rss_peak_bytes": 1469235200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.024,
                "predicted_n": 44,
                "predicted_per_second": 79.33228048942482,
                "predicted_per_token_ms": 12.605209302325582
              },
              "ttft_s": 0.124621267,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294542581170009,
              "complete": true,
              "e2e_s": 0.358055947,
              "end_ns": 294542939225956,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414081024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.93351205682298,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051464951,
                "rss_peak_bytes": 1469239296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.401,
                "predicted_n": 23,
                "predicted_per_second": 78.73987566257816,
                "predicted_per_token_ms": 12.700045454545455
              },
              "ttft_s": 0.07857934,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294543017216938,
              "complete": true,
              "e2e_s": 0.295222136,
              "end_ns": 294543312439074,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.45963037687412,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058267768,
                "rss_peak_bytes": 1469243392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.309,
                "predicted_n": 18,
                "predicted_per_second": 78.5912745193219,
                "predicted_per_token_ms": 12.724058823529411
              },
              "ttft_s": 0.078865985,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294543388203140,
              "complete": true,
              "e2e_s": 0.468725055,
              "end_ns": 294543856928195,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469782528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 117.06952747932785,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055208933,
                "rss_peak_bytes": 1524940800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.983,
                "predicted_n": 29,
                "predicted_per_second": 79.09984377780853,
                "predicted_per_token_ms": 12.64225
              },
              "ttft_s": 0.114689469,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294543934833142,
              "complete": true,
              "e2e_s": 1.079436871,
              "end_ns": 294545014270013,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470253568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 289.4823844663526,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054107436,
                "rss_peak_bytes": 1525411840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 257.846,
                "predicted_n": 21,
                "predicted_per_second": 77.5656787384718,
                "predicted_per_token_ms": 12.8923
              },
              "ttft_s": 0.821588966,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294545093189314,
              "complete": true,
              "e2e_s": 0.197697946,
              "end_ns": 294545290887260,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.22140253798155,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051311895,
                "rss_peak_bytes": 1472729088,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.197568818
            },
            {
              "begin_ns": 294545356296855,
              "complete": true,
              "e2e_s": 1.659513809,
              "end_ns": 294547015810664,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 450.8980987407531,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051911789,
                "rss_peak_bytes": 1472729088,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1597.002,
                "predicted_n": 128,
                "predicted_per_second": 79.52400811019648,
                "predicted_per_token_ms": 12.574818897637796
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062424244
            },
            {
              "begin_ns": 294547092645351,
              "complete": true,
              "e2e_s": 0.620379169,
              "end_ns": 294547713024520,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470290432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 163.08242073388314,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055758087,
                "rss_peak_bytes": 1525448704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.342,
                "predicted_n": 34,
                "predicted_per_second": 78.88282792547724,
                "predicted_per_token_ms": 12.677030303030303
              },
              "tool_call_valid": true,
              "ttft_s": 0.319460122,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294547830807131,
              "complete": true,
              "e2e_s": 0.558774572,
              "end_ns": 294548389581703,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 135.5794989139778,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05127435,
                "rss_peak_bytes": 1525485568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.188,
                "predicted_n": 25,
                "predicted_per_second": 78.89857588070535,
                "predicted_per_token_ms": 12.6745
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254527713,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        },
        "B": {
          "correct_tokens": 562,
          "gpu_j_per_correct_token": 10.051945542171993,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 495935488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7843872768,
              "gpu_energy_j": 2648.9553022163905,
              "gpu_owned_peak_bytes": 7589593088,
              "max_sample_gap_s": 0.078394182,
              "rss_peak_bytes": 7726653440,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 495665152,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7843872768,
              "gpu_energy_j": 3000.2380924842696,
              "gpu_owned_peak_bytes": 7589593088,
              "max_sample_gap_s": 0.094032371,
              "rss_peak_bytes": 7621308416,
              "swap_peak_bytes": 389120
            }
          ],
          "lifecycle_gpu_j": 5649.19339470066,
          "raw_requests": [
            {
              "begin_ns": 294116496793304,
              "complete": true,
              "e2e_s": 0.182479405,
              "end_ns": 294116679272709,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439701504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 42.9154309128209,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050079922,
                "rss_peak_bytes": 1539190784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.805,
                "predicted_n": 10,
                "predicted_per_second": 77.05149608321561,
                "predicted_per_token_ms": 12.978333333333333
              },
              "ttft_s": 0.065516128,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294116733776607,
              "complete": true,
              "e2e_s": 0.233433917,
              "end_ns": 294116967210524,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439701504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 55.836536772206664,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050094819,
                "rss_peak_bytes": 1539190784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.346,
                "predicted_n": 14,
                "predicted_per_second": 78.15036129513183,
                "predicted_per_token_ms": 12.795846153846155
              },
              "ttft_s": 0.067090847,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294117021105730,
              "complete": true,
              "e2e_s": 0.66540317,
              "end_ns": 294117686508900,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439701504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 176.06790499717246,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050659562,
                "rss_peak_bytes": 1539235840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.617,
                "predicted_n": 44,
                "predicted_per_second": 79.39189501068098,
                "predicted_per_token_ms": 12.595744186046511
              },
              "ttft_s": 0.123751486,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294117742098180,
              "complete": true,
              "e2e_s": 0.358680862,
              "end_ns": 294118100779042,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439705600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 90.72279021187747,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050209606,
                "rss_peak_bytes": 1539239936,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 280.186,
                "predicted_n": 23,
                "predicted_per_second": 78.5192693425082,
                "predicted_per_token_ms": 12.735727272727273
              },
              "ttft_s": 0.078443552,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294118156102747,
              "complete": true,
              "e2e_s": 0.294788146,
              "end_ns": 294118450890893,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439709696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 71.27070348834746,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.051263772,
                "rss_peak_bytes": 1539244032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 215.744,
                "predicted_n": 18,
                "predicted_per_second": 78.79709285078613,
                "predicted_per_token_ms": 12.690823529411764
              },
              "ttft_s": 0.079034857,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294118504329117,
              "complete": true,
              "e2e_s": 0.468552398,
              "end_ns": 294118972881515,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495403008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 116.08629444407005,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050095735,
                "rss_peak_bytes": 1594937344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.207,
                "predicted_n": 29,
                "predicted_per_second": 79.04982114977965,
                "predicted_per_token_ms": 12.65025
              },
              "ttft_s": 0.114352009,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294119031501190,
              "complete": true,
              "e2e_s": 0.988338256,
              "end_ns": 294120019839446,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495853568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 256.03125766879054,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.060142952,
                "rss_peak_bytes": 1595387904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.535,
                "predicted_n": 21,
                "predicted_per_second": 75.89124784184263,
                "predicted_per_token_ms": 13.176750000000002
              },
              "ttft_s": 0.724775151,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294120074109686,
              "complete": true,
              "e2e_s": 0.197018205,
              "end_ns": 294120271127891,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443191296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 50.10564692011278,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.052818554,
                "rss_peak_bytes": 1542725632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.196750283
            },
            {
              "begin_ns": 294120319153776,
              "complete": true,
              "e2e_s": 1.658151561,
              "end_ns": 294121977305337,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443191296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 443.06746247568697,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.050866816,
                "rss_peak_bytes": 1542725632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.205,
                "predicted_n": 128,
                "predicted_per_second": 79.61359198347549,
                "predicted_per_token_ms": 12.560669291338582
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062889205
            },
            {
              "begin_ns": 294122037852743,
              "complete": true,
              "e2e_s": 0.61793752,
              "end_ns": 294122655790263,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495902720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 154.960193056694,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.052477801,
                "rss_peak_bytes": 1595437056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.742,
                "predicted_n": 34,
                "predicted_per_second": 78.99612679596497,
                "predicted_per_token_ms": 12.658848484848486
              },
              "tool_call_valid": true,
              "ttft_s": 0.316631461,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294122724009675,
              "complete": true,
              "e2e_s": 0.559878217,
              "end_ns": 294123283887892,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495935488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 139.5063007240319,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.05529345,
                "rss_peak_bytes": 1595469824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.38,
                "predicted_n": 25,
                "predicted_per_second": 78.8488074117879,
                "predicted_per_token_ms": 12.6825
              },
              "tool_facts_valid": true,
              "ttft_s": 0.25544662,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294511379645846,
              "complete": true,
              "e2e_s": 0.182497934,
              "end_ns": 294511562143780,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439431168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 41.726662148032815,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.056744462,
                "rss_peak_bytes": 1447538688,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.98,
                "predicted_n": 10,
                "predicted_per_second": 77.5995861355406,
                "predicted_per_token_ms": 12.886666666666667
              },
              "ttft_s": 0.066417946,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294511637187491,
              "complete": true,
              "e2e_s": 0.234409187,
              "end_ns": 294511871596678,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439431168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 57.82269767013754,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.05129592,
                "rss_peak_bytes": 1447538688,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.435,
                "predicted_n": 14,
                "predicted_per_second": 78.10857091356986,
                "predicted_per_token_ms": 12.802692307692308
              },
              "ttft_s": 0.068013479,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294511947065179,
              "complete": true,
              "e2e_s": 0.666245375,
              "end_ns": 294512613310554,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439431168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 177.4333329524331,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.056118937,
                "rss_peak_bytes": 1447583744,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.178,
                "predicted_n": 44,
                "predicted_per_second": 79.309746983463,
                "predicted_per_token_ms": 12.608790697674419
              },
              "ttft_s": 0.12406231,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294512688795574,
              "complete": true,
              "e2e_s": 0.358006839,
              "end_ns": 294513046802413,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439431168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 90.5435607753888,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050900136,
                "rss_peak_bytes": 1447714816,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.145,
                "predicted_n": 23,
                "predicted_per_second": 78.81208690823766,
                "predicted_per_token_ms": 12.68840909090909
              },
              "ttft_s": 0.078860638,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294513121246523,
              "complete": true,
              "e2e_s": 0.295648006,
              "end_ns": 294513416894529,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 439435264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 71.87459455931334,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.050980772,
                "rss_peak_bytes": 1447718912,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.415,
                "predicted_n": 18,
                "predicted_per_second": 78.55278053739345,
                "predicted_per_token_ms": 12.730294117647059
              },
              "ttft_s": 0.079220262,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294513495205647,
              "complete": true,
              "e2e_s": 0.4698762,
              "end_ns": 294513965081847,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495132672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7831289856,
                "gpu_energy_j": 117.26435410204559,
                "gpu_owned_peak_bytes": 7577010176,
                "max_sample_gap_s": 0.057943601,
                "rss_peak_bytes": 1503416320,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.907,
                "predicted_n": 29,
                "predicted_per_second": 78.89390741799964,
                "predicted_per_token_ms": 12.67525
              },
              "ttft_s": 0.114917404,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294514040132650,
              "complete": true,
              "e2e_s": 0.9865595,
              "end_ns": 294515026692150,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495583232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 257.78944630948405,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.051865549,
                "rss_peak_bytes": 1503866880,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.864,
                "predicted_n": 21,
                "predicted_per_second": 77.86221502429302,
                "predicted_per_token_ms": 12.8432
              },
              "ttft_s": 0.729666095,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294515104908603,
              "complete": true,
              "e2e_s": 0.198623217,
              "end_ns": 294515303531820,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 442920960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 46.19152278116595,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.052456159,
                "rss_peak_bytes": 1451204608,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.198486563
            },
            {
              "begin_ns": 294515387093732,
              "complete": true,
              "e2e_s": 1.659440682,
              "end_ns": 294517046534414,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 442920960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 448.05592972756125,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.05354102,
                "rss_peak_bytes": 1451204608,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1596.32,
                "predicted_n": 128,
                "predicted_per_second": 79.55798336173198,
                "predicted_per_token_ms": 12.569448818897637
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063044917
            },
            {
              "begin_ns": 294517123373434,
              "complete": true,
              "e2e_s": 0.619200834,
              "end_ns": 294517742574268,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495632384,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 158.06243480284033,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.050662634,
                "rss_peak_bytes": 1503916032,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.527,
                "predicted_n": 34,
                "predicted_per_second": 79.03680480543773,
                "predicted_per_token_ms": 12.652333333333333
              },
              "tool_call_valid": true,
              "ttft_s": 0.317861447,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294517830100304,
              "complete": true,
              "e2e_s": 0.559423333,
              "end_ns": 294518389523637,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 495665152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7843872768,
                "gpu_energy_j": 139.751476821819,
                "gpu_owned_peak_bytes": 7589593088,
                "max_sample_gap_s": 0.050593434,
                "rss_peak_bytes": 1503948800,
                "swap_peak_bytes": 274432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.04,
                "predicted_n": 25,
                "predicted_per_second": 78.93698197605578,
                "predicted_per_token_ms": 12.668333333333335
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255322368,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        }
      },
      "quality_gate": false,
      "status": "NEGATIVE"
    },
    "qwen35": {
      "metrics": {
        "A": {
          "correct_tokens": 542,
          "gpu_j_per_correct_token": 8.840362851959433,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475979776,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2248.022567058399,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.072148782,
              "rss_peak_bytes": 5996539904,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476053504,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2543.4540987036135,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.058207983,
              "rss_peak_bytes": 5961478144,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4791.476665762013,
          "raw_requests": [
            {
              "begin_ns": 294166382163364,
              "complete": true,
              "e2e_s": 0.156086755,
              "end_ns": 294166538250119,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 35.34582384515695,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050035462,
                "rss_peak_bytes": 1216061440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.517,
                "predicted_n": 10,
                "predicted_per_second": 94.2240648261566,
                "predicted_per_token_ms": 10.613
              },
              "ttft_s": 0.060517047,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294166598657895,
              "complete": true,
              "e2e_s": 0.14808727,
              "end_ns": 294166746745165,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.43099969658651,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0500971,
                "rss_peak_bytes": 1216061440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.168,
                "predicted_n": 9,
                "predicted_per_second": 93.93199323689647,
                "predicted_per_token_ms": 10.646
              },
              "ttft_s": 0.062882192,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294166803206016,
              "complete": true,
              "e2e_s": 0.526256481,
              "end_ns": 294167329462497,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.6186932088292,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051462383,
                "rss_peak_bytes": 1216106496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.199,
                "predicted_n": 39,
                "predicted_per_second": 96.39801217151742,
                "predicted_per_token_ms": 10.373657894736843
              },
              "ttft_s": 0.132004143,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294167391984598,
              "complete": true,
              "e2e_s": 0.307236674,
              "end_ns": 294167699221272,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 74.5204674682591,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05286547,
                "rss_peak_bytes": 1219117056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.531,
                "predicted_n": 23,
                "predicted_per_second": 95.84761971149867,
                "predicted_per_token_ms": 10.433227272727272
              },
              "ttft_s": 0.077757413,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294167799758526,
              "complete": true,
              "e2e_s": 0.254095591,
              "end_ns": 294168053854117,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.43019240398373,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052563121,
                "rss_peak_bytes": 1219117056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.971,
                "predicted_n": 18,
                "predicted_per_second": 95.52118041703424,
                "predicted_per_token_ms": 10.468882352941177
              },
              "ttft_s": 0.076046577,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294168113306009,
              "complete": true,
              "e2e_s": 0.397345657,
              "end_ns": 294168510651666,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475467776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 91.59260736275918,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052407621,
                "rss_peak_bytes": 1271828480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.649,
                "predicted_n": 29,
                "predicted_per_second": 96.33613052169454,
                "predicted_per_token_ms": 10.38032142857143
              },
              "ttft_s": 0.106632251,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294168569771858,
              "complete": true,
              "e2e_s": 1.025726137,
              "end_ns": 294169595497995,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475901952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 272.2124467297819,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.072148782,
                "rss_peak_bytes": 1272262656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.774,
                "predicted_n": 16,
                "predicted_per_second": 94.47390630707798,
                "predicted_per_token_ms": 10.584933333333334
              },
              "ttft_s": 0.866861738,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294169652563388,
              "complete": true,
              "e2e_s": 0.203764922,
              "end_ns": 294169856328310,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423227392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.26657793490148,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05654124,
                "rss_peak_bytes": 1219588096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.20360823
            },
            {
              "begin_ns": 294169921702251,
              "complete": true,
              "e2e_s": 1.365419277,
              "end_ns": 294171287121528,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423227392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 344.8237990519365,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050784982,
                "rss_peak_bytes": 1219588096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1307.765,
                "predicted_n": 128,
                "predicted_per_second": 97.11224876028949,
                "predicted_per_token_ms": 10.29736220472441
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057501979
            },
            {
              "begin_ns": 294171348168710,
              "complete": true,
              "e2e_s": 0.550014712,
              "end_ns": 294171898183422,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475947008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 135.78627846926116,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053640246,
                "rss_peak_bytes": 1272307712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.959,
                "predicted_n": 34,
                "predicted_per_second": 95.94166746618056,
                "predicted_per_token_ms": 10.423
              },
              "tool_call_valid": true,
              "ttft_s": 0.30231206,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294171965191207,
              "complete": true,
              "e2e_s": 0.523201011,
              "end_ns": 294172488392218,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475979776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 122.6544366248294,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053305111,
                "rss_peak_bytes": 1272340480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.383,
                "predicted_n": 25,
                "predicted_per_second": 95.8531529696505,
                "predicted_per_token_ms": 10.432625
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272771815,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294447186025628,
              "complete": true,
              "e2e_s": 0.156315516,
              "end_ns": 294447342341144,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 34.41035191365606,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051310403,
                "rss_peak_bytes": 1137475584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.654,
                "predicted_n": 10,
                "predicted_per_second": 94.08911284420935,
                "predicted_per_token_ms": 10.628222222222222
              },
              "ttft_s": 0.060615892,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294447415156019,
              "complete": true,
              "e2e_s": 0.148974504,
              "end_ns": 294447564130523,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 28.185496411377898,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055234364,
                "rss_peak_bytes": 1137475584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.633,
                "predicted_n": 9,
                "predicted_per_second": 93.42192846215829,
                "predicted_per_token_ms": 10.704125
              },
              "ttft_s": 0.06324396,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294447633213813,
              "complete": true,
              "e2e_s": 0.527030439,
              "end_ns": 294448160244252,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.63730057778977,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054824257,
                "rss_peak_bytes": 1137586176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.56,
                "predicted_n": 39,
                "predicted_per_second": 96.30981346309814,
                "predicted_per_token_ms": 10.383157894736842
              },
              "ttft_s": 0.132362357,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294448232150785,
              "complete": true,
              "e2e_s": 0.306251059,
              "end_ns": 294448538401844,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 73.77522526538453,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05081253,
                "rss_peak_bytes": 1140723712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.303,
                "predicted_n": 23,
                "predicted_per_second": 95.94292268308745,
                "predicted_per_token_ms": 10.422863636363637
              },
              "ttft_s": 0.076947099,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294448606648969,
              "complete": true,
              "e2e_s": 0.254085964,
              "end_ns": 294448860734933,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 54.14560752466612,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055669219,
                "rss_peak_bytes": 1140854784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.022,
                "predicted_n": 18,
                "predicted_per_second": 95.4938153711339,
                "predicted_per_token_ms": 10.471882352941176
              },
              "ttft_s": 0.076002237,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294448935559606,
              "complete": true,
              "e2e_s": 0.398063372,
              "end_ns": 294449333622978,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475504640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 95.66347519029141,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050854409,
                "rss_peak_bytes": 1193750528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.119,
                "predicted_n": 29,
                "predicted_per_second": 96.18059968603903,
                "predicted_per_token_ms": 10.397107142857143
              },
              "ttft_s": 0.106943296,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294449404888826,
              "complete": true,
              "e2e_s": 1.033556114,
              "end_ns": 294450438444940,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475967488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 271.76294517710716,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05174332,
                "rss_peak_bytes": 1194278912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.978,
                "predicted_n": 16,
                "predicted_per_second": 94.35267772899394,
                "predicted_per_token_ms": 10.598533333333334
              },
              "ttft_s": 0.874527783,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294450508748143,
              "complete": true,
              "e2e_s": 0.204151055,
              "end_ns": 294450712899198,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423297024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 48.12895837181683,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.058207983,
                "rss_peak_bytes": 1141608448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.204018274
            },
            {
              "begin_ns": 294450778926954,
              "complete": true,
              "e2e_s": 1.365941047,
              "end_ns": 294452144868001,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423297024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 347.14050714924826,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050686879,
                "rss_peak_bytes": 1141608448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.017,
                "predicted_n": 128,
                "predicted_per_second": 97.09353930415277,
                "predicted_per_token_ms": 10.299346456692914
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057801429
            },
            {
              "begin_ns": 294452214238822,
              "complete": true,
              "e2e_s": 0.550813636,
              "end_ns": 294452765052458,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476008448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 134.85940984775576,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051363191,
                "rss_peak_bytes": 1193795584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.493,
                "predicted_n": 34,
                "predicted_per_second": 96.35233420829039,
                "predicted_per_token_ms": 10.378575757575758
              },
              "tool_call_valid": true,
              "ttft_s": 0.304208521,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294452847158086,
              "complete": true,
              "e2e_s": 0.52530898,
              "end_ns": 294453372467066,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476053504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.10189721250484,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052241958,
                "rss_peak_bytes": 1193840640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.406,
                "predicted_n": 25,
                "predicted_per_second": 95.8443487775852,
                "predicted_per_token_ms": 10.433583333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.274834382,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        },
        "B": {
          "correct_tokens": 542,
          "gpu_j_per_correct_token": 8.227788642940753,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 501587968,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6375866368,
              "gpu_energy_j": 2199.688241177253,
              "gpu_owned_peak_bytes": 6121586688,
              "max_sample_gap_s": 0.078545222,
              "rss_peak_bytes": 5996449792,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 501583872,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6375866368,
              "gpu_energy_j": 2259.773203296635,
              "gpu_owned_peak_bytes": 6121586688,
              "max_sample_gap_s": 0.082452823,
              "rss_peak_bytes": 5994491904,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4459.461444473888,
          "raw_requests": [
            {
              "begin_ns": 294142358164786,
              "complete": true,
              "e2e_s": 0.156653259,
              "end_ns": 294142514818045,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 31.418218369172482,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.052150772,
                "rss_peak_bytes": 1283284992,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.881,
                "predicted_n": 10,
                "predicted_per_second": 93.86635516942877,
                "predicted_per_token_ms": 10.653444444444444
              },
              "ttft_s": 0.060711453,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294142584764435,
              "complete": true,
              "e2e_s": 0.154291805,
              "end_ns": 294142739056240,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 31.47046134585132,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.052430476,
                "rss_peak_bytes": 1283284992,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 90.268,
                "predicted_n": 9,
                "predicted_per_second": 88.62498338281561,
                "predicted_per_token_ms": 11.2835
              },
              "ttft_s": 0.063990919,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294142799831497,
              "complete": true,
              "e2e_s": 0.525776909,
              "end_ns": 294143325608406,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 127.32585192191273,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050934703,
                "rss_peak_bytes": 1283330048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.682,
                "predicted_n": 39,
                "predicted_per_second": 96.52460615420567,
                "predicted_per_token_ms": 10.360052631578947
              },
              "ttft_s": 0.132039943,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294143385021189,
              "complete": true,
              "e2e_s": 0.306668937,
              "end_ns": 294143691690126,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448348160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 70.81459128670649,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050780489,
                "rss_peak_bytes": 1286377472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.297,
                "predicted_n": 23,
                "predicted_per_second": 95.94543321543676,
                "predicted_per_token_ms": 10.422590909090909
              },
              "ttft_s": 0.077336214,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294143758169835,
              "complete": true,
              "e2e_s": 0.25434207,
              "end_ns": 294144012511905,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448348160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 52.80646222652949,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050374753,
                "rss_peak_bytes": 1286377472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.239,
                "predicted_n": 18,
                "predicted_per_second": 95.37755485612016,
                "predicted_per_token_ms": 10.48464705882353
              },
              "ttft_s": 0.076044325,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294144077592776,
              "complete": true,
              "e2e_s": 0.398204771,
              "end_ns": 294144475797547,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501063680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 91.36311275510504,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.05047101,
                "rss_peak_bytes": 1339092992,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.105,
                "predicted_n": 29,
                "predicted_per_second": 96.18522526236237,
                "predicted_per_token_ms": 10.396607142857144
              },
              "ttft_s": 0.107041982,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294144534293372,
              "complete": true,
              "e2e_s": 0.906572356,
              "end_ns": 294145440865728,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501510144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 230.4844922868217,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.078545222,
                "rss_peak_bytes": 1339539456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 160.89,
                "predicted_n": 16,
                "predicted_per_second": 93.23140033563305,
                "predicted_per_token_ms": 10.725999999999999
              },
              "ttft_s": 0.745629576,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294145502015728,
              "complete": true,
              "e2e_s": 0.204135386,
              "end_ns": 294145706151114,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448835584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 49.666075917406445,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.050405813,
                "rss_peak_bytes": 1286864896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.203967424
            },
            {
              "begin_ns": 294145759177800,
              "complete": true,
              "e2e_s": 1.368159904,
              "end_ns": 294147127337704,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448835584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 347.1744826725292,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.050747845,
                "rss_peak_bytes": 1286864896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1310.657,
                "predicted_n": 128,
                "predicted_per_second": 96.8979679656844,
                "predicted_per_token_ms": 10.320133858267717
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057457391
            },
            {
              "begin_ns": 294147187885150,
              "complete": true,
              "e2e_s": 0.551226937,
              "end_ns": 294147739112087,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501551104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 136.5087577303662,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.051800309,
                "rss_peak_bytes": 1339580416,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.512,
                "predicted_n": 34,
                "predicted_per_second": 96.06651296024592,
                "predicted_per_token_ms": 10.409454545454546
              },
              "tool_call_valid": true,
              "ttft_s": 0.303563181,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294147804096754,
              "complete": true,
              "e2e_s": 0.52202329,
              "end_ns": 294148326120044,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501587968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 128.52952682644639,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.051890536,
                "rss_peak_bytes": 1339617280,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.532,
                "predicted_n": 25,
                "predicted_per_second": 95.7961458017339,
                "predicted_per_token_ms": 10.438833333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.271486563,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294471559217617,
              "complete": true,
              "e2e_s": 0.156403428,
              "end_ns": 294471715621045,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 32.57779431974782,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050134811,
                "rss_peak_bytes": 1281093632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.638,
                "predicted_n": 10,
                "predicted_per_second": 94.10485371923293,
                "predicted_per_token_ms": 10.626444444444445
              },
              "ttft_s": 0.060724485,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294471786192119,
              "complete": true,
              "e2e_s": 0.149279534,
              "end_ns": 294471935471653,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 32.11985074682575,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050137929,
                "rss_peak_bytes": 1281093632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.097,
                "predicted_n": 9,
                "predicted_per_second": 92.91845244317456,
                "predicted_per_token_ms": 10.762125
              },
              "ttft_s": 0.063146469,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294472008623116,
              "complete": true,
              "e2e_s": 0.527102495,
              "end_ns": 294472535725611,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 445382656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 131.88469733175734,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.05268216,
                "rss_peak_bytes": 1281138688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.575,
                "predicted_n": 39,
                "predicted_per_second": 96.30615218906418,
                "predicted_per_token_ms": 10.383552631578947
              },
              "ttft_s": 0.132544622,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294472614075002,
              "complete": true,
              "e2e_s": 0.307705852,
              "end_ns": 294472921780854,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448344064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 70.03693194512915,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.052129818,
                "rss_peak_bytes": 1284141056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 230.32,
                "predicted_n": 23,
                "predicted_per_second": 95.51927752691908,
                "predicted_per_token_ms": 10.469090909090909
              },
              "ttft_s": 0.077367292,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294473000973847,
              "complete": true,
              "e2e_s": 0.254918817,
              "end_ns": 294473255892664,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448344064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 57.75196245834451,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050638918,
                "rss_peak_bytes": 1284141056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.162,
                "predicted_n": 18,
                "predicted_per_second": 95.41877617000259,
                "predicted_per_token_ms": 10.480117647058824
              },
              "ttft_s": 0.076677583,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294473340393080,
              "complete": true,
              "e2e_s": 0.398628958,
              "end_ns": 294473739022038,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501059584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6363283456,
                "gpu_energy_j": 96.50871098867353,
                "gpu_owned_peak_bytes": 6109003776,
                "max_sample_gap_s": 0.050128895,
                "rss_peak_bytes": 1336856576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.263,
                "predicted_n": 29,
                "predicted_per_second": 96.13304813862386,
                "predicted_per_token_ms": 10.402249999999999
              },
              "ttft_s": 0.107315193,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294473818109511,
              "complete": true,
              "e2e_s": 0.912007344,
              "end_ns": 294474730116855,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501506048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 240.59218670239008,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.059034279,
                "rss_peak_bytes": 1337303040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 160.743,
                "predicted_n": 16,
                "predicted_per_second": 93.31666075661148,
                "predicted_per_token_ms": 10.716199999999999
              },
              "ttft_s": 0.75120086,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294474809142571,
              "complete": true,
              "e2e_s": 0.204176546,
              "end_ns": 294475013319117,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448831488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 48.41019796560024,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.058597229,
                "rss_peak_bytes": 1284628480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.20403822
            },
            {
              "begin_ns": 294475078273261,
              "complete": true,
              "e2e_s": 1.370651594,
              "end_ns": 294476448924855,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 448831488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 346.9069531655008,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.054544684,
                "rss_peak_bytes": 1284628480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1312.694,
                "predicted_n": 128,
                "predicted_per_second": 96.74760454454733,
                "predicted_per_token_ms": 10.336173228346457
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057871627
            },
            {
              "begin_ns": 294476528096459,
              "complete": true,
              "e2e_s": 0.551534498,
              "end_ns": 294477079630957,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501542912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 137.57793394104863,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.05097791,
                "rss_peak_bytes": 1337339904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.65,
                "predicted_n": 34,
                "predicted_per_second": 95.749310895111,
                "predicted_per_token_ms": 10.443939393939393
              },
              "tool_call_valid": true,
              "ttft_s": 0.303202693,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294477182810272,
              "complete": true,
              "e2e_s": 0.525119004,
              "end_ns": 294477707929276,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 501583872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6375866368,
                "gpu_energy_j": 134.5727249099199,
                "gpu_owned_peak_bytes": 6121586688,
                "max_sample_gap_s": 0.051687485,
                "rss_peak_bytes": 1337380864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 251.323,
                "predicted_n": 25,
                "predicted_per_second": 95.49464235266967,
                "predicted_per_token_ms": 10.471791666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273836302,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        }
      },
      "quality_gate": false,
      "status": "NEGATIVE"
    },
    "qwen38": {
      "metrics": {
        "A": {
          "correct_tokens": 556,
          "gpu_j_per_correct_token": 26.726341141556425,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 673239040,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7712.111487228389,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.056510653,
              "rss_peak_bytes": 11904954368,
              "swap_peak_bytes": 189898752
            },
            {
              "anon_peak_bytes": 772685824,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7147.734187476982,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.074976635,
              "rss_peak_bytes": 12139343872,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14859.845674705371,
          "raw_requests": [
            {
              "begin_ns": 294234039941428,
              "complete": true,
              "e2e_s": 0.512734627,
              "end_ns": 294234552676055,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 619765760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.34162407109942,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052333034,
                "rss_peak_bytes": 1230602240,
                "swap_peak_bytes": 149409792
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 270.071,
                "predicted_n": 10,
                "predicted_per_second": 33.324570205612595,
                "predicted_per_token_ms": 30.007888888888893
              },
              "ttft_s": 0.237695318,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294234620478812,
              "complete": true,
              "e2e_s": 0.610575775,
              "end_ns": 294235231054587,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 463986688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 145.0899858092728,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.054091298,
                "rss_peak_bytes": 1074823168,
                "swap_peak_bytes": 148717568
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 377.006,
                "predicted_n": 14,
                "predicted_per_second": 34.48220983220427,
                "predicted_per_token_ms": 29.000461538461536
              },
              "ttft_s": 0.231795581,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294235295450869,
              "complete": true,
              "e2e_s": 1.821770049,
              "end_ns": 294237117220918,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464973824,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 471.87734209729797,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050571591,
                "rss_peak_bytes": 1075916800,
                "swap_peak_bytes": 147800064
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1245.765,
                "predicted_n": 45,
                "predicted_per_second": 35.31966301830602,
                "predicted_per_token_ms": 28.312840909090912
              },
              "ttft_s": 0.566547964,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294237195038075,
              "complete": true,
              "e2e_s": 1.044452863,
              "end_ns": 294238239490938,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469098496,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 263.5238032736339,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052330639,
                "rss_peak_bytes": 1080455168,
                "swap_peak_bytes": 146690048
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.886,
                "predicted_n": 28,
                "predicted_per_second": 35.253288348396495,
                "predicted_per_token_ms": 28.366148148148145
              },
              "ttft_s": 0.272149675,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294238301161085,
              "complete": true,
              "e2e_s": 0.881699173,
              "end_ns": 294239182860258,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469848064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 227.31802893043175,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051411469,
                "rss_peak_bytes": 1081204736,
                "swap_peak_bytes": 145596416
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.933,
                "predicted_n": 23,
                "predicted_per_second": 35.20377384455614,
                "predicted_per_token_ms": 28.406045454545453
              },
              "ttft_s": 0.251950786,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294239246058133,
              "complete": true,
              "e2e_s": 1.18947014,
              "end_ns": 294240435528273,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 627470336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 295.361946830159,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05074357,
                "rss_peak_bytes": 1238863872,
                "swap_peak_bytes": 144928768
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 795.798,
                "predicted_n": 29,
                "predicted_per_second": 35.184808205097276,
                "predicted_per_token_ms": 28.421357142857143
              },
              "ttft_s": 0.383971462,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294240497212937,
              "complete": true,
              "e2e_s": 3.803614759,
              "end_ns": 294244300827696,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628494336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1006.3741757588256,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054662264,
                "rss_peak_bytes": 1239887872,
                "swap_peak_bytes": 144273408
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 586.589,
                "predicted_n": 21,
                "predicted_per_second": 34.09542285995816,
                "predicted_per_token_ms": 29.32945
              },
              "ttft_s": 3.214671472,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294244364204859,
              "complete": true,
              "e2e_s": 0.719238597,
              "end_ns": 294245083443456,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 471687168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 189.88412665940118,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05077539,
                "rss_peak_bytes": 1083080704,
                "swap_peak_bytes": 144052224
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.719113829
            },
            {
              "begin_ns": 294245142199365,
              "complete": true,
              "e2e_s": 3.772188595,
              "end_ns": 294248914387960,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 471703552,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1031.4247719677257,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051952834,
                "rss_peak_bytes": 1083097088,
                "swap_peak_bytes": 144048128
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3578.511,
                "predicted_n": 128,
                "predicted_per_second": 35.4896212419076,
                "predicted_per_token_ms": 28.17725196850394
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193585347
            },
            {
              "begin_ns": 294248983046547,
              "complete": true,
              "e2e_s": 1.699843387,
              "end_ns": 294250682889934,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628625408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 463.0204061534213,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051226079,
                "rss_peak_bytes": 1240018944,
                "swap_peak_bytes": 144031744
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 938.884,
                "predicted_n": 34,
                "predicted_per_second": 35.148112013837704,
                "predicted_per_token_ms": 28.451030303030304
              },
              "tool_call_valid": true,
              "ttft_s": 1.024355896,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294250754203541,
              "complete": true,
              "e2e_s": 1.772519312,
              "end_ns": 294252526722853,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628645888,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 454.43244698860025,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054306115,
                "rss_peak_bytes": 1240039424,
                "swap_peak_bytes": 144027648
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.315,
                "predicted_n": 25,
                "predicted_per_second": 35.17436960934465,
                "predicted_per_token_ms": 28.42979166666667
              },
              "tool_facts_valid": true,
              "ttft_s": 1.090215852,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294397444815824,
              "complete": true,
              "e2e_s": 0.466689435,
              "end_ns": 294397911505259,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.79787108794547,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.054385623,
                "rss_peak_bytes": 1256505344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.816,
                "predicted_n": 10,
                "predicted_per_second": 34.24449044198222,
                "predicted_per_token_ms": 29.201777777777775
              },
              "ttft_s": 0.203810106,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294397980727676,
              "complete": true,
              "e2e_s": 0.5727899,
              "end_ns": 294398553517576,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 141.71914494091368,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050645117,
                "rss_peak_bytes": 1256505344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.288,
                "predicted_n": 14,
                "predicted_per_second": 35.01325116890392,
                "predicted_per_token_ms": 28.560615384615385
              },
              "ttft_s": 0.201462905,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294398619859610,
              "complete": true,
              "e2e_s": 1.759642776,
              "end_ns": 294400379502386,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 486.05608502522557,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.071361977,
                "rss_peak_bytes": 1256505344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.236,
                "predicted_n": 45,
                "predicted_per_second": 35.47711887092456,
                "predicted_per_token_ms": 28.18718181818182
              },
              "ttft_s": 0.519416674,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294400449217355,
              "complete": true,
              "e2e_s": 0.986495569,
              "end_ns": 294401435712924,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 262.67364574773177,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050996537,
                "rss_peak_bytes": 1259806720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.525,
                "predicted_n": 28,
                "predicted_per_second": 35.362299859205656,
                "predicted_per_token_ms": 28.2787037037037
              },
              "ttft_s": 0.222906934,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294401504635259,
              "complete": true,
              "e2e_s": 0.843832278,
              "end_ns": 294402348467537,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.72496247598963,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052969523,
                "rss_peak_bytes": 1259806720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.976,
                "predicted_n": 23,
                "predicted_per_second": 35.314362029997945,
                "predicted_per_token_ms": 28.317090909090908
              },
              "ttft_s": 0.220816341,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294402420747563,
              "complete": true,
              "e2e_s": 1.143361937,
              "end_ns": 294403564109500,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772165632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 293.33528149508953,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055451818,
                "rss_peak_bytes": 1416728576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.801,
                "predicted_n": 29,
                "predicted_per_second": 35.362420608208375,
                "predicted_per_token_ms": 28.278607142857144
              },
              "ttft_s": 0.351483043,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294403632269013,
              "complete": true,
              "e2e_s": 3.787195613,
              "end_ns": 294407419464626,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772595712,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1015.5524278992791,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055698825,
                "rss_peak_bytes": 1417158656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.638,
                "predicted_n": 21,
                "predicted_per_second": 34.38564880561449,
                "predicted_per_token_ms": 29.0819
              },
              "ttft_s": 3.205461599,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294407489807928,
              "complete": true,
              "e2e_s": 0.721430992,
              "end_ns": 294408211238920,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615727104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 183.5235141762035,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055423426,
                "rss_peak_bytes": 1260290048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.721300085
            },
            {
              "begin_ns": 294408268149235,
              "complete": true,
              "e2e_s": 3.769145415,
              "end_ns": 294412037294650,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615727104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1061.7843806558476,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052727169,
                "rss_peak_bytes": 1260290048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3574.564,
                "predicted_n": 128,
                "predicted_per_second": 35.52880854839919,
                "predicted_per_token_ms": 28.146173228346456
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194444511
            },
            {
              "begin_ns": 294412108317012,
              "complete": true,
              "e2e_s": 1.703601076,
              "end_ns": 294413811918088,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772644864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 454.6186416949284,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052168534,
                "rss_peak_bytes": 1417207808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.859,
                "predicted_n": 34,
                "predicted_per_second": 35.11164972618233,
                "predicted_per_token_ms": 28.48057575757576
              },
              "tool_call_valid": true,
              "ttft_s": 1.028504311,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294413894429396,
              "complete": true,
              "e2e_s": 1.774838376,
              "end_ns": 294415669267772,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772685824,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 464.0685256940418,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051338508,
                "rss_peak_bytes": 1417248768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.38,
                "predicted_n": 25,
                "predicted_per_second": 35.22263641433561,
                "predicted_per_token_ms": 28.390833333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093430164,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        },
        "B": {
          "correct_tokens": 556,
          "gpu_j_per_correct_token": 25.07209126211255,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 782327808,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13231456256,
              "gpu_energy_j": 6949.7879410966425,
              "gpu_owned_peak_bytes": 12977176576,
              "max_sample_gap_s": 0.07783235,
              "rss_peak_bytes": 12139245568,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 782315520,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13231456256,
              "gpu_energy_j": 6990.294800637937,
              "gpu_owned_peak_bytes": 12977176576,
              "max_sample_gap_s": 0.085704299,
              "rss_peak_bytes": 12139343872,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 13940.082741734579,
          "raw_requests": [
            {
              "begin_ns": 294289684573867,
              "complete": true,
              "e2e_s": 0.46825557,
              "end_ns": 294290152829437,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621903872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 109.10694181590135,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.052486398,
                "rss_peak_bytes": 1315962880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.553,
                "predicted_n": 10,
                "predicted_per_second": 34.148729098132065,
                "predicted_per_token_ms": 29.283666666666665
              },
              "ttft_s": 0.204734979,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294290227877734,
              "complete": true,
              "e2e_s": 0.572676789,
              "end_ns": 294290800554523,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621903872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 140.46348765013443,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.052601279,
                "rss_peak_bytes": 1315962880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.526,
                "predicted_n": 14,
                "predicted_per_second": 35.085257174935094,
                "predicted_per_token_ms": 28.502000000000002
              },
              "ttft_s": 0.202147552,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294290882543882,
              "complete": true,
              "e2e_s": 1.760780142,
              "end_ns": 294292643324024,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621907968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 473.4071366458693,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.050896233,
                "rss_peak_bytes": 1315966976,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1239.721,
                "predicted_n": 45,
                "predicted_per_second": 35.49185663548492,
                "predicted_per_token_ms": 28.175477272727274
              },
              "ttft_s": 0.521014072,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294292738199840,
              "complete": true,
              "e2e_s": 0.988563527,
              "end_ns": 294293726763367,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 624881664,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 260.9350010197005,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.051370899,
                "rss_peak_bytes": 1319264256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 762.598,
                "predicted_n": 28,
                "predicted_per_second": 35.40528561575037,
                "predicted_per_token_ms": 28.24437037037037
              },
              "ttft_s": 0.225927101,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294293794109590,
              "complete": true,
              "e2e_s": 0.846898989,
              "end_ns": 294294641008579,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 624881664,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 218.37246185884177,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.051131582,
                "rss_peak_bytes": 1319264256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.598,
                "predicted_n": 23,
                "predicted_per_second": 35.3358025563847,
                "predicted_per_token_ms": 28.29990909090909
              },
              "ttft_s": 0.224286252,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294294705906706,
              "complete": true,
              "e2e_s": 1.144253316,
              "end_ns": 294295850160022,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 781795328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 287.7503417949208,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.051109611,
                "rss_peak_bytes": 1476177920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 789.493,
                "predicted_n": 29,
                "predicted_per_second": 35.46579893678601,
                "predicted_per_token_ms": 28.19617857142857
              },
              "ttft_s": 0.354713408,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294295916425802,
              "complete": true,
              "e2e_s": 3.234003758,
              "end_ns": 294299150429560,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782233600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 863.5376094483851,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.05839038,
                "rss_peak_bytes": 1476616192,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.139,
                "predicted_n": 21,
                "predicted_per_second": 34.474496629256095,
                "predicted_per_token_ms": 29.00695
              },
              "ttft_s": 2.653851524,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294299215163437,
              "complete": true,
              "e2e_s": 0.722833042,
              "end_ns": 294299937996479,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 663334912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 192.07629879451537,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.051320754,
                "rss_peak_bytes": 1357717504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.722702517
            },
            {
              "begin_ns": 294299998160482,
              "complete": true,
              "e2e_s": 3.763058773,
              "end_ns": 294303761219255,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 625360896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 1048.9621484519275,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.07783235,
                "rss_peak_bytes": 1319743488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3567.454,
                "predicted_n": 128,
                "predicted_per_second": 35.599618102994455,
                "predicted_per_token_ms": 28.090188976377956
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195509582
            },
            {
              "begin_ns": 294303830619416,
              "complete": true,
              "e2e_s": 1.702158808,
              "end_ns": 294305532778224,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782286848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 459.65696251548235,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.056860488,
                "rss_peak_bytes": 1476669440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.215,
                "predicted_n": 34,
                "predicted_per_second": 35.210704054032426,
                "predicted_per_token_ms": 28.400454545454547
              },
              "tool_call_valid": true,
              "ttft_s": 1.02756236,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294305638896601,
              "complete": true,
              "e2e_s": 1.770431613,
              "end_ns": 294307409328214,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782327808,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 454.81990126480986,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.053167374,
                "rss_peak_bytes": 1476710400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.015,
                "predicted_n": 25,
                "predicted_per_second": 35.24151450408581,
                "predicted_per_token_ms": 28.375625
              },
              "tool_facts_valid": true,
              "ttft_s": 1.089332831,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294343697714413,
              "complete": true,
              "e2e_s": 0.468714335,
              "end_ns": 294344166428748,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621895680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 105.97732326905685,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.050321057,
                "rss_peak_bytes": 1316495360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.676,
                "predicted_n": 10,
                "predicted_per_second": 34.26274193302776,
                "predicted_per_token_ms": 29.18622222222222
              },
              "ttft_s": 0.205971983,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294344233114676,
              "complete": true,
              "e2e_s": 0.573401116,
              "end_ns": 294344806515792,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621895680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 143.0423030131997,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.051765308,
                "rss_peak_bytes": 1316495360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.557,
                "predicted_n": 14,
                "predicted_per_second": 35.08232201793516,
                "predicted_per_token_ms": 28.504384615384616
              },
              "ttft_s": 0.202799352,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294344877159367,
              "complete": true,
              "e2e_s": 1.760973376,
              "end_ns": 294346638132743,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621895680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13212581888,
                "gpu_energy_j": 478.2965873278091,
                "gpu_owned_peak_bytes": 12958302208,
                "max_sample_gap_s": 0.052169171,
                "rss_peak_bytes": 1316495360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1239.741,
                "predicted_n": 45,
                "predicted_per_second": 35.49128406659133,
                "predicted_per_token_ms": 28.17593181818182
              },
              "ttft_s": 0.521202268,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294346707148510,
              "complete": true,
              "e2e_s": 0.992976586,
              "end_ns": 294347700125096,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 624865280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 261.45941925493634,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.07522126,
                "rss_peak_bytes": 1319788544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 762.306,
                "predicted_n": 28,
                "predicted_per_second": 35.41884754940929,
                "predicted_per_token_ms": 28.233555555555558
              },
              "ttft_s": 0.230569496,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294347766174927,
              "complete": true,
              "e2e_s": 0.852491396,
              "end_ns": 294348618666323,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 624865280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 225.1523257438357,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.051325282,
                "rss_peak_bytes": 1319788544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.397,
                "predicted_n": 23,
                "predicted_per_second": 35.29051310801945,
                "predicted_per_token_ms": 28.336227272727275
              },
              "ttft_s": 0.229058034,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294348682135551,
              "complete": true,
              "e2e_s": 1.146494315,
              "end_ns": 294349828629866,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 781783040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13214679040,
                "gpu_energy_j": 297.1273384622126,
                "gpu_owned_peak_bytes": 12960399360,
                "max_sample_gap_s": 0.08295188,
                "rss_peak_bytes": 1476706304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 790.315,
                "predicted_n": 29,
                "predicted_per_second": 35.42891125690389,
                "predicted_per_token_ms": 28.225535714285716
              },
              "ttft_s": 0.356143539,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294349899945525,
              "complete": true,
              "e2e_s": 3.244081958,
              "end_ns": 294353144027483,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782225408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 865.9876987788439,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.085704299,
                "rss_peak_bytes": 1477148672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.563,
                "predicted_n": 21,
                "predicted_per_second": 34.390083275586655,
                "predicted_per_token_ms": 29.07815
              },
              "ttft_s": 2.662473769,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294353218210650,
              "complete": true,
              "e2e_s": 0.726406678,
              "end_ns": 294353944617328,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 635842560,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 192.60019818558254,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.05118561,
                "rss_peak_bytes": 1330765824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 0.001,
                "predicted_n": 1,
                "predicted_per_second": 0.0,
                "predicted_per_token_ms": 0.0
              },
              "tokens_evaluated": 505,
              "tokens_predicted": 1,
              "ttft_s": 0.726282152
            },
            {
              "begin_ns": 294354005144955,
              "complete": true,
              "e2e_s": 3.770416032,
              "end_ns": 294357775560987,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 625360896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 1046.678420903972,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.05195295,
                "rss_peak_bytes": 1320284160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3574.727,
                "predicted_n": 128,
                "predicted_per_second": 35.52718850977991,
                "predicted_per_token_ms": 28.147456692913384
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195541215
            },
            {
              "begin_ns": 294357844114885,
              "complete": true,
              "e2e_s": 1.700859019,
              "end_ns": 294359544973904,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782282752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 448.6941110016803,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.05211913,
                "rss_peak_bytes": 1477206016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.397,
                "predicted_n": 34,
                "predicted_per_second": 35.20386773160144,
                "predicted_per_token_ms": 28.4059696969697
              },
              "tool_call_valid": true,
              "ttft_s": 1.026206763,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294359622101738,
              "complete": true,
              "e2e_s": 1.773379829,
              "end_ns": 294361395481567,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 782315520,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13231456256,
                "gpu_energy_j": 459.5989507266527,
                "gpu_owned_peak_bytes": 12977176576,
                "max_sample_gap_s": 0.052123186,
                "rss_peak_bytes": 1477238784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.089,
                "predicted_n": 25,
                "predicted_per_second": 35.2376855300849,
                "predicted_per_token_ms": 28.378708333333336
              },
              "tool_facts_valid": true,
              "ttft_s": 1.09226063,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        }
      },
      "quality_gate": false,
      "status": "NEGATIVE"
    }
  }
}
```

</details>
