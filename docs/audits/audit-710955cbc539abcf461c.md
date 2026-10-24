# Public audit excerpt

Original SHA256: `710955cbc539abcf461cf4fa218a20f6825cc9e437c12aa1243e83420a235ae0`

Original file: `RESULTS.json`; 266309 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.603196235425694,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470327296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2654.900390238516,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.211805536,
              "rss_peak_bytes": 7727697920,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470331392,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2742.0958940707237,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.05629887,
              "rss_peak_bytes": 7726755840,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5396.99628430924,
          "raw_requests": [
            {
              "begin_ns": 296643472676439,
              "complete": true,
              "e2e_s": 0.182086543,
              "end_ns": 296643654762982,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.92193146062355,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050162845,
                "rss_peak_bytes": 1473441792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.41,
                "predicted_n": 10,
                "predicted_per_second": 77.31294562322825,
                "predicted_per_token_ms": 12.934444444444445
              },
              "ttft_s": 0.065605913,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296643708147001,
              "complete": true,
              "e2e_s": 0.233097119,
              "end_ns": 296643941244120,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.969191777227444,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050202962,
                "rss_peak_bytes": 1473441792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.827,
                "predicted_n": 14,
                "predicted_per_second": 78.39495377712917,
                "predicted_per_token_ms": 12.755923076923077
              },
              "ttft_s": 0.06721023,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296643996792553,
              "complete": true,
              "e2e_s": 0.667042493,
              "end_ns": 296644663835046,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.65129890820276,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051993318,
                "rss_peak_bytes": 1473507328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 543.127,
                "predicted_n": 44,
                "predicted_per_second": 79.17116991053659,
                "predicted_per_token_ms": 12.630860465116278
              },
              "ttft_s": 0.123766985,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 296644718149484,
              "complete": true,
              "e2e_s": 0.357313669,
              "end_ns": 296645075463153,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.44131183500186,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050151289,
                "rss_peak_bytes": 1473511424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.651,
                "predicted_n": 23,
                "predicted_per_second": 78.95180709920294,
                "predicted_per_token_ms": 12.665954545454547
              },
              "ttft_s": 0.078600064,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 296645130280716,
              "complete": true,
              "e2e_s": 0.29531316,
              "end_ns": 296645425593876,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 67.47346004833119,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050555949,
                "rss_peak_bytes": 1473515520,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 215.78,
                "predicted_n": 18,
                "predicted_per_second": 78.7839466122903,
                "predicted_per_token_ms": 12.692941176470589
              },
              "ttft_s": 0.079504047,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 296645484137748,
              "complete": true,
              "e2e_s": 0.46834895,
              "end_ns": 296645952486698,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469770240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 117.53658745419048,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050370804,
                "rss_peak_bytes": 1529208832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.892,
                "predicted_n": 29,
                "predicted_per_second": 79.12018355882586,
                "predicted_per_token_ms": 12.639
              },
              "ttft_s": 0.114382635,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296646008146393,
              "complete": true,
              "e2e_s": 1.073976151,
              "end_ns": 296647082122544,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 285.29234693519436,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051206359,
                "rss_peak_bytes": 1529679872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.901,
                "predicted_n": 21,
                "predicted_per_second": 77.85100096924496,
                "predicted_per_token_ms": 12.84505
              },
              "ttft_s": 0.816961818,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296647138116421,
              "complete": true,
              "e2e_s": 0.198309762,
              "end_ns": 296647336426183,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.51936216702331,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052687825,
                "rss_peak_bytes": 1477017600,
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
              "ttft_s": 0.198179085
            },
            {
              "begin_ns": 296647388735866,
              "complete": true,
              "e2e_s": 1.657042755,
              "end_ns": 296649045778621,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 442.21523721527666,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052310644,
                "rss_peak_bytes": 1477017600,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.262,
                "predicted_n": 128,
                "predicted_per_second": 79.66068312485652,
                "predicted_per_token_ms": 12.55324409448819
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062609666
            },
            {
              "begin_ns": 296649112159600,
              "complete": true,
              "e2e_s": 0.6178535,
              "end_ns": 296649730013100,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 152.46539141835422,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050307895,
                "rss_peak_bytes": 1529733120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.643,
                "predicted_n": 34,
                "predicted_per_second": 79.01485239786135,
                "predicted_per_token_ms": 12.655848484848484
              },
              "tool_call_valid": true,
              "ttft_s": 0.316567929,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296649793829854,
              "complete": true,
              "e2e_s": 0.559779502,
              "end_ns": 296650353609356,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 144.18044723184263,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052544726,
                "rss_peak_bytes": 1529765888,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 306.077,
                "predicted_n": 25,
                "predicted_per_second": 78.41164151504361,
                "predicted_per_token_ms": 12.753208333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253648134,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297103526164449,
              "complete": true,
              "e2e_s": 0.18205795,
              "end_ns": 297103708222399,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.171385184231696,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051507484,
                "rss_peak_bytes": 1471311872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.237,
                "predicted_n": 10,
                "predicted_per_second": 77.42801345526811,
                "predicted_per_token_ms": 12.915222222222221
              },
              "ttft_s": 0.065784722,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297103785169892,
              "complete": true,
              "e2e_s": 0.233187065,
              "end_ns": 297104018356957,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 54.38891623498034,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054322697,
                "rss_peak_bytes": 1471311872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.021,
                "predicted_n": 14,
                "predicted_per_second": 78.30334716692467,
                "predicted_per_token_ms": 12.770846153846152
              },
              "ttft_s": 0.067134977,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297104109070256,
              "complete": true,
              "e2e_s": 0.667264455,
              "end_ns": 297104776334711,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.21453892943427,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050891843,
                "rss_peak_bytes": 1471356928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.725,
                "predicted_n": 44,
                "predicted_per_second": 79.37606719276386,
                "predicted_per_token_ms": 12.59825581395349
              },
              "ttft_s": 0.125489327,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297104858223595,
              "complete": true,
              "e2e_s": 0.357951648,
              "end_ns": 297105216175243,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.22674459464368,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050273483,
                "rss_peak_bytes": 1471365120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.313,
                "predicted_n": 23,
                "predicted_per_second": 78.76468334807188,
                "predicted_per_token_ms": 12.696045454545454
              },
              "ttft_s": 0.078557943,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297105299250000,
              "complete": true,
              "e2e_s": 0.295301947,
              "end_ns": 297105594551947,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.21652757054463,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050597019,
                "rss_peak_bytes": 1471369216,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.653,
                "predicted_n": 18,
                "predicted_per_second": 78.46648788615897,
                "predicted_per_token_ms": 12.744294117647058
              },
              "ttft_s": 0.07863635,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297105695200390,
              "complete": true,
              "e2e_s": 0.470105339,
              "end_ns": 297106165305729,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469770240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 113.05581851211055,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055565718,
                "rss_peak_bytes": 1527066624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.72,
                "predicted_n": 29,
                "predicted_per_second": 78.93549842129002,
                "predicted_per_token_ms": 12.668571428571429
              },
              "ttft_s": 0.115256285,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297106264161162,
              "complete": true,
              "e2e_s": 1.079081431,
              "end_ns": 297107343242593,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 287.7321781396225,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052501536,
                "rss_peak_bytes": 1527537664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.579,
                "predicted_n": 21,
                "predicted_per_second": 77.94870195924062,
                "predicted_per_token_ms": 12.82895
              },
              "ttft_s": 0.822428519,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297107447699246,
              "complete": true,
              "e2e_s": 0.198077961,
              "end_ns": 297107645777207,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.80615940942973,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05629887,
                "rss_peak_bytes": 1474875392,
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
              "ttft_s": 0.19791145
            },
            {
              "begin_ns": 297107734198537,
              "complete": true,
              "e2e_s": 1.659113364,
              "end_ns": 297109393311901,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 447.9669756142149,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052200881,
                "rss_peak_bytes": 1474875392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.751,
                "predicted_n": 128,
                "predicted_per_second": 79.6362566946188,
                "predicted_per_token_ms": 12.557094488188977
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.064211329
            },
            {
              "begin_ns": 297109472305415,
              "complete": true,
              "e2e_s": 0.618480786,
              "end_ns": 297110090786201,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 163.05069705093877,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050991995,
                "rss_peak_bytes": 1527590912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.566,
                "predicted_n": 34,
                "predicted_per_second": 79.0294228936264,
                "predicted_per_token_ms": 12.653515151515151
              },
              "tool_call_valid": true,
              "ttft_s": 0.317441948,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297110186340123,
              "complete": true,
              "e2e_s": 0.559586533,
              "end_ns": 297110745926656,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470331392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.8549903194684,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051334424,
                "rss_peak_bytes": 1527627776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.206,
                "predicted_n": 25,
                "predicted_per_second": 78.89390741799963,
                "predicted_per_token_ms": 12.67525
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255426014,
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
          "gpu_j_per_correct_token": 9.935649949529111,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470302720,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2678.6409229604124,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.073210786,
              "rss_peak_bytes": 1529794560,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470249472,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2905.194348674948,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.113899972,
              "rss_peak_bytes": 1526755328,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5583.83527163536,
          "raw_requests": [
            {
              "begin_ns": 296672543155134,
              "complete": true,
              "e2e_s": 0.181762344,
              "end_ns": 296672724917478,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414048256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 36.76410374416799,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050565491,
                "rss_peak_bytes": 1473474560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.108,
                "predicted_n": 10,
                "predicted_per_second": 77.51403865366727,
                "predicted_per_token_ms": 12.90088888888889
              },
              "ttft_s": 0.065624846,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296672782248528,
              "complete": true,
              "e2e_s": 0.233414349,
              "end_ns": 296673015662877,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414048256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.13011959361646,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050689993,
                "rss_peak_bytes": 1473474560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.269,
                "predicted_n": 14,
                "predicted_per_second": 78.18655311573414,
                "predicted_per_token_ms": 12.789923076923078
              },
              "ttft_s": 0.067077767,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296673069563728,
              "complete": true,
              "e2e_s": 0.666125092,
              "end_ns": 296673735688820,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414048256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 176.72412193652988,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05075778,
                "rss_peak_bytes": 1473540096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.026,
                "predicted_n": 44,
                "predicted_per_second": 79.3319877644246,
                "predicted_per_token_ms": 12.605255813953487
              },
              "ttft_s": 0.124088311,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 296673791196501,
              "complete": true,
              "e2e_s": 0.357596914,
              "end_ns": 296674148793415,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414056448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 88.4101988373533,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050718696,
                "rss_peak_bytes": 1473548288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.944,
                "predicted_n": 23,
                "predicted_per_second": 78.86887690719284,
                "predicted_per_token_ms": 12.679272727272728
              },
              "ttft_s": 0.078547528,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 296674206329994,
              "complete": true,
              "e2e_s": 0.294682788,
              "end_ns": 296674501012782,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414056448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.28745847475713,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050306928,
                "rss_peak_bytes": 1473548288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.274,
                "predicted_n": 18,
                "predicted_per_second": 78.6039930828486,
                "predicted_per_token_ms": 12.722
              },
              "ttft_s": 0.078340337,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 296674557180924,
              "complete": true,
              "e2e_s": 0.468771646,
              "end_ns": 296675025952570,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469753856,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.40561062704099,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050702744,
                "rss_peak_bytes": 1529245696,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.868,
                "predicted_n": 29,
                "predicted_per_second": 79.12554963997876,
                "predicted_per_token_ms": 12.638142857142856
              },
              "ttft_s": 0.114879591,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296675086791630,
              "complete": true,
              "e2e_s": 1.075985187,
              "end_ns": 296676162776817,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470220800,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 288.24730782543656,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053530806,
                "rss_peak_bytes": 1529712640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.554,
                "predicted_n": 21,
                "predicted_per_second": 77.95629769950966,
                "predicted_per_token_ms": 12.827699999999998
              },
              "ttft_s": 0.819385034,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296676218096432,
              "complete": true,
              "e2e_s": 0.198221042,
              "end_ns": 296676416317474,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417558528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.08779831780971,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050479036,
                "rss_peak_bytes": 1477050368,
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
              "ttft_s": 0.198086025
            },
            {
              "begin_ns": 296676464877559,
              "complete": true,
              "e2e_s": 1.662073488,
              "end_ns": 296678126951047,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417558528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.947059784751,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051859342,
                "rss_peak_bytes": 1477050368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1599.265,
                "predicted_n": 128,
                "predicted_per_second": 79.4114796484635,
                "predicted_per_token_ms": 12.592637795275591
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.06271192
            },
            {
              "begin_ns": 296678187075058,
              "complete": true,
              "e2e_s": 0.61824187,
              "end_ns": 296678805316928,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470269952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.13200103879407,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054552107,
                "rss_peak_bytes": 1529761792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.311,
                "predicted_n": 34,
                "predicted_per_second": 79.07771422272597,
                "predicted_per_token_ms": 12.645787878787878
              },
              "tool_call_valid": true,
              "ttft_s": 0.316995006,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296678872216604,
              "complete": true,
              "e2e_s": 0.558498572,
              "end_ns": 296679430715176,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470302720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 137.668115926826,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054813372,
                "rss_peak_bytes": 1529794560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.536,
                "predicted_n": 25,
                "predicted_per_second": 78.80841673890772,
                "predicted_per_token_ms": 12.689
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253974529,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297073613007297,
              "complete": true,
              "e2e_s": 0.181819385,
              "end_ns": 297073794826682,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.358441715482336,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052045945,
                "rss_peak_bytes": 1470500864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.122,
                "predicted_n": 10,
                "predicted_per_second": 77.50469333976335,
                "predicted_per_token_ms": 12.902444444444445
              },
              "ttft_s": 0.065680913,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297073871112179,
              "complete": true,
              "e2e_s": 0.23350198,
              "end_ns": 297074104614159,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 54.075075350721846,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050598281,
                "rss_peak_bytes": 1470500864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.239,
                "predicted_n": 14,
                "predicted_per_second": 78.20066290100397,
                "predicted_per_token_ms": 12.787615384615385
              },
              "ttft_s": 0.067241417,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297074183115524,
              "complete": true,
              "e2e_s": 0.665519845,
              "end_ns": 297074848635369,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 176.91594984122042,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05027614,
                "rss_peak_bytes": 1470545920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.994,
                "predicted_n": 44,
                "predicted_per_second": 79.33667162367111,
                "predicted_per_token_ms": 12.604511627906977
              },
              "ttft_s": 0.123462556,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297074929115145,
              "complete": true,
              "e2e_s": 0.358112237,
              "end_ns": 297075287227382,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414044160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 88.73175826155898,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058460517,
                "rss_peak_bytes": 1470550016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.682,
                "predicted_n": 23,
                "predicted_per_second": 78.6607647256527,
                "predicted_per_token_ms": 12.712818181818182
              },
              "ttft_s": 0.078406856,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297075364554194,
              "complete": true,
              "e2e_s": 0.294778875,
              "end_ns": 297075659333069,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414048256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 76.29347658081645,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050173656,
                "rss_peak_bytes": 1470554112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.009,
                "predicted_n": 18,
                "predicted_per_second": 78.70042451934874,
                "predicted_per_token_ms": 12.706411764705882
              },
              "ttft_s": 0.078697936,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297075736109451,
              "complete": true,
              "e2e_s": 0.468311253,
              "end_ns": 297076204420704,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469737472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 117.36812425101327,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051468651,
                "rss_peak_bytes": 1526243328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.761,
                "predicted_n": 29,
                "predicted_per_second": 79.14948227758288,
                "predicted_per_token_ms": 12.634321428571429
              },
              "ttft_s": 0.114510287,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297076279231171,
              "complete": true,
              "e2e_s": 1.076195899,
              "end_ns": 297077355427070,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470167552,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 288.24996286230527,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.057655501,
                "rss_peak_bytes": 1526673408,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.18,
                "predicted_n": 21,
                "predicted_per_second": 78.07010695604653,
                "predicted_per_token_ms": 12.809000000000001
              },
              "ttft_s": 0.819996489,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297077434376595,
              "complete": true,
              "e2e_s": 0.197449286,
              "end_ns": 297077631825881,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417505280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.11182140301653,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051711914,
                "rss_peak_bytes": 1474011136,
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
              "ttft_s": 0.197317747
            },
            {
              "begin_ns": 297077696945905,
              "complete": true,
              "e2e_s": 1.669512836,
              "end_ns": 297079366458741,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417505280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.5253245586601,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053145947,
                "rss_peak_bytes": 1474011136,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1606.828,
                "predicted_n": 128,
                "predicted_per_second": 79.03770658713938,
                "predicted_per_token_ms": 12.652188976377953
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062597973
            },
            {
              "begin_ns": 297079440889542,
              "complete": true,
              "e2e_s": 0.620211672,
              "end_ns": 297080061101214,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470220800,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.54989358553706,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050677782,
                "rss_peak_bytes": 1526726656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.12,
                "predicted_n": 34,
                "predicted_per_second": 78.92471060939442,
                "predicted_per_token_ms": 12.67030303030303
              },
              "tool_call_valid": true,
              "ttft_s": 0.319348639,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297080149500469,
              "complete": true,
              "e2e_s": 0.559671414,
              "end_ns": 297080709171883,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470249472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.42716422307436,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050593167,
                "rss_peak_bytes": 1526755328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.392,
                "predicted_n": 25,
                "predicted_per_second": 78.84569896712134,
                "predicted_per_token_ms": 12.683
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255246954,
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
          "gpu_j_per_correct_token": 9.03640979056846,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476004352,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2243.1623999959397,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.068192306,
              "rss_peak_bytes": 5997551616,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 384008192,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2654.571706492165,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.079255839,
              "rss_peak_bytes": 5744099328,
              "swap_peak_bytes": 177496064
            }
          ],
          "lifecycle_gpu_j": 4897.734106488105,
          "raw_requests": [
            {
              "begin_ns": 296723867735469,
              "complete": true,
              "e2e_s": 0.157510054,
              "end_ns": 296724025245523,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.38575969974783,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050066049,
                "rss_peak_bytes": 1216712704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.08,
                "predicted_n": 10,
                "predicted_per_second": 93.67194004995838,
                "predicted_per_token_ms": 10.675555555555555
              },
              "ttft_s": 0.061505566,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296724083177649,
              "complete": true,
              "e2e_s": 0.149139408,
              "end_ns": 296724232317057,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.87210545239619,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050115744,
                "rss_peak_bytes": 1216712704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.393,
                "predicted_n": 9,
                "predicted_per_second": 92.60009491509729,
                "predicted_per_token_ms": 10.799125
              },
              "ttft_s": 0.062739206,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 296724289076419,
              "complete": true,
              "e2e_s": 0.525666087,
              "end_ns": 296724814742506,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.33285472497587,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050584686,
                "rss_peak_bytes": 1216757760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.81,
                "predicted_n": 39,
                "predicted_per_second": 96.49323277722759,
                "predicted_per_token_ms": 10.36342105263158
              },
              "ttft_s": 0.131813691,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 296724877585582,
              "complete": true,
              "e2e_s": 0.307161392,
              "end_ns": 296725184746974,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 70.31593000937254,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051738436,
                "rss_peak_bytes": 1219784704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 230.438,
                "predicted_n": 23,
                "predicted_per_second": 95.470365130751,
                "predicted_per_token_ms": 10.474454545454545
              },
              "ttft_s": 0.076685962,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 296725245323234,
              "complete": true,
              "e2e_s": 0.254010116,
              "end_ns": 296725499333350,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.431512300913056,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052821606,
                "rss_peak_bytes": 1219784704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.009,
                "predicted_n": 18,
                "predicted_per_second": 95.50078928593499,
                "predicted_per_token_ms": 10.471117647058822
              },
              "ttft_s": 0.07590185,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 296725558141076,
              "complete": true,
              "e2e_s": 0.39787366,
              "end_ns": 296725956014736,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475500544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.24883801929289,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050886168,
                "rss_peak_bytes": 1272500224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.795,
                "predicted_n": 29,
                "predicted_per_second": 96.28776285699547,
                "predicted_per_token_ms": 10.385535714285714
              },
              "ttft_s": 0.107084005,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296726016921202,
              "complete": true,
              "e2e_s": 1.024459633,
              "end_ns": 296727041380835,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475934720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 270.650034133777,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.068192306,
                "rss_peak_bytes": 1272934400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.185,
                "predicted_n": 16,
                "predicted_per_second": 94.22998398090273,
                "predicted_per_token_ms": 10.612333333333334
              },
              "ttft_s": 0.865246125,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 296727101113178,
              "complete": true,
              "e2e_s": 0.203599528,
              "end_ns": 296727304712706,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.52079700687964,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050794161,
                "rss_peak_bytes": 1220259840,
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
              "ttft_s": 0.203399096
            },
            {
              "begin_ns": 296727364560441,
              "complete": true,
              "e2e_s": 1.38212472,
              "end_ns": 296728746685161,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 350.2373868537462,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055249645,
                "rss_peak_bytes": 1220259840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1324.135,
                "predicted_n": 128,
                "predicted_per_second": 95.9116706378126,
                "predicted_per_token_ms": 10.426259842519684
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057829555
            },
            {
              "begin_ns": 296728809564939,
              "complete": true,
              "e2e_s": 0.549807713,
              "end_ns": 296729359372652,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475979776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.5861504452337,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053441775,
                "rss_peak_bytes": 1272979456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.096,
                "predicted_n": 34,
                "predicted_per_second": 96.18299251521441,
                "predicted_per_token_ms": 10.396848484848485
              },
              "tool_call_valid": true,
              "ttft_s": 0.302554472,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296729430128442,
              "complete": true,
              "e2e_s": 0.522519297,
              "end_ns": 296729952647739,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476004352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 127.82548976830518,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050079845,
                "rss_peak_bytes": 1273004032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.753,
                "predicted_n": 25,
                "predicted_per_second": 96.09494180250087,
                "predicted_per_token_ms": 10.406374999999999
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272770265,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297010446844086,
              "complete": true,
              "e2e_s": 0.206346273,
              "end_ns": 297010653190359,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331591680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 37.22434442490899,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050735826,
                "rss_peak_bytes": 1062793216,
                "swap_peak_bytes": 140918784
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 100.256,
                "predicted_n": 10,
                "predicted_per_second": 89.77018831790616,
                "predicted_per_token_ms": 11.139555555555555
              },
              "ttft_s": 0.100129129,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297010728707937,
              "complete": true,
              "e2e_s": 0.173707874,
              "end_ns": 297010902415811,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 280031232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.500117284956826,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051352937,
                "rss_peak_bytes": 1011560448,
                "swap_peak_bytes": 139837440
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.439,
                "predicted_n": 9,
                "predicted_per_second": 92.55081618251022,
                "predicted_per_token_ms": 10.804875
              },
              "ttft_s": 0.083006872,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297010978918144,
              "complete": true,
              "e2e_s": 0.572796293,
              "end_ns": 297011551714437,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 281071616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 135.06435368550558,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054514151,
                "rss_peak_bytes": 1013235712,
                "swap_peak_bytes": 139149312
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 395.66,
                "predicted_n": 39,
                "predicted_per_second": 96.04205631097406,
                "predicted_per_token_ms": 10.412105263157896
              },
              "ttft_s": 0.171012115,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297011640036220,
              "complete": true,
              "e2e_s": 0.349279892,
              "end_ns": 297011989316112,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 285069312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 76.2846233400286,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.058707752,
                "rss_peak_bytes": 1017597952,
                "swap_peak_bytes": 138502144
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 232.487,
                "predicted_n": 23,
                "predicted_per_second": 94.62894699488575,
                "predicted_per_token_ms": 10.567590909090908
              },
              "ttft_s": 0.1113563,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297012058185612,
              "complete": true,
              "e2e_s": 0.295622206,
              "end_ns": 297012353807818,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 285831168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 60.92085372156968,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050863796,
                "rss_peak_bytes": 1018621952,
                "swap_peak_bytes": 136962048
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 181.465,
                "predicted_n": 18,
                "predicted_per_second": 93.68197724079023,
                "predicted_per_token_ms": 10.674411764705882
              },
              "ttft_s": 0.109030921,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297012423197251,
              "complete": true,
              "e2e_s": 0.439915403,
              "end_ns": 297012863112654,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 339255296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.96150252690602,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052242123,
                "rss_peak_bytes": 1072046080,
                "swap_peak_bytes": 136417280
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 295.498,
                "predicted_n": 29,
                "predicted_per_second": 94.75529445207751,
                "predicted_per_token_ms": 10.5535
              },
              "ttft_s": 0.138748007,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297012940727031,
              "complete": true,
              "e2e_s": 1.054693613,
              "end_ns": 297013995420644,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 340185088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 278.315033284219,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053029505,
                "rss_peak_bytes": 1073106944,
                "swap_peak_bytes": 136044544
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.994,
                "predicted_n": 16,
                "predicted_per_second": 93.75351575684088,
                "predicted_per_token_ms": 10.666266666666667
              },
              "ttft_s": 0.889358131,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297014072106132,
              "complete": true,
              "e2e_s": 0.205827876,
              "end_ns": 297014277934008,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 287571968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 51.701125529865095,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053172895,
                "rss_peak_bytes": 1020493824,
                "swap_peak_bytes": 135720960
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
              "ttft_s": 0.205692327
            },
            {
              "begin_ns": 297014343694582,
              "complete": true,
              "e2e_s": 1.3673832,
              "end_ns": 297015711077782,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 287592448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 349.48668621780314,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05396604,
                "rss_peak_bytes": 1020514304,
                "swap_peak_bytes": 135708672
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.297,
                "predicted_n": 128,
                "predicted_per_second": 96.9986183425151,
                "predicted_per_token_ms": 10.309425196850395
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057981311
            },
            {
              "begin_ns": 297015784898001,
              "complete": true,
              "e2e_s": 0.552491628,
              "end_ns": 297016337389629,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 340312064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.64951078714446,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05465827,
                "rss_peak_bytes": 1073233920,
                "swap_peak_bytes": 135696384
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.641,
                "predicted_n": 34,
                "predicted_per_second": 96.03045038281229,
                "predicted_per_token_ms": 10.413363636363638
              },
              "tool_call_valid": true,
              "ttft_s": 0.304369951,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297016431730360,
              "complete": true,
              "e2e_s": 0.523881681,
              "end_ns": 297016955612041,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 340361216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 127.74717179072474,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05054144,
                "rss_peak_bytes": 1073283072,
                "swap_peak_bytes": 135692288
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.343,
                "predicted_n": 25,
                "predicted_per_second": 95.86846846127114,
                "predicted_per_token_ms": 10.430958333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273478985,
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
          "gpu_j_per_correct_token": 8.398689684014828,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475996160,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2274.303195258542,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.084849629,
              "rss_peak_bytes": 1273110528,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476016640,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2277.7866134774945,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.061489354,
              "rss_peak_bytes": 1271787520,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4552.0898087360365,
          "raw_requests": [
            {
              "begin_ns": 296699479264649,
              "complete": true,
              "e2e_s": 0.156460058,
              "end_ns": 296699635724707,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419770368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.79723718102748,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.04998435,
                "rss_peak_bytes": 1216774144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.932,
                "predicted_n": 10,
                "predicted_per_second": 93.81645332110244,
                "predicted_per_token_ms": 10.65911111111111
              },
              "ttft_s": 0.060516636,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296699699690180,
              "complete": true,
              "e2e_s": 0.148242067,
              "end_ns": 296699847932247,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419770368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 28.896490783229154,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050775471,
                "rss_peak_bytes": 1216774144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.137,
                "predicted_n": 9,
                "predicted_per_second": 93.96619566111092,
                "predicted_per_token_ms": 10.642125
              },
              "ttft_s": 0.063053432,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 296699907109119,
              "complete": true,
              "e2e_s": 0.525598172,
              "end_ns": 296700432707291,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419770368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.2344925145091,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050431683,
                "rss_peak_bytes": 1216819200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.839,
                "predicted_n": 39,
                "predicted_per_second": 96.48612758005174,
                "predicted_per_token_ms": 10.364184210526316
              },
              "ttft_s": 0.131730781,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 296700494096660,
              "complete": true,
              "e2e_s": 0.306213658,
              "end_ns": 296700800310318,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422735872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.90297055354169,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050814287,
                "rss_peak_bytes": 1219850240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.079,
                "predicted_n": 23,
                "predicted_per_second": 96.03673841775108,
                "predicted_per_token_ms": 10.412681818181818
              },
              "ttft_s": 0.077081816,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 296700860115610,
              "complete": true,
              "e2e_s": 0.254093521,
              "end_ns": 296701114209131,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422735872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.45934264316651,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050011436,
                "rss_peak_bytes": 1219850240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.567,
                "predicted_n": 18,
                "predicted_per_second": 95.73850997088422,
                "predicted_per_token_ms": 10.445117647058824
              },
              "ttft_s": 0.076438556,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 296701175205485,
              "complete": true,
              "e2e_s": 0.397721648,
              "end_ns": 296701572927133,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475447296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 93.23835412055301,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051210105,
                "rss_peak_bytes": 1272561664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.538,
                "predicted_n": 29,
                "predicted_per_second": 96.37293572613564,
                "predicted_per_token_ms": 10.376357142857144
              },
              "ttft_s": 0.107133106,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296701635858891,
              "complete": true,
              "e2e_s": 1.02538465,
              "end_ns": 296702661243541,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475910144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 264.7863017636087,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.084849629,
                "rss_peak_bytes": 1273024512,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.241,
                "predicted_n": 16,
                "predicted_per_second": 94.19684628958622,
                "predicted_per_token_ms": 10.616066666666667
              },
              "ttft_s": 0.866088181,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 296702719203988,
              "complete": true,
              "e2e_s": 0.203652078,
              "end_ns": 296702922856066,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423235584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 51.72605364850043,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051490137,
                "rss_peak_bytes": 1220349952,
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
              "ttft_s": 0.203513263
            },
            {
              "begin_ns": 296702982128404,
              "complete": true,
              "e2e_s": 1.368744306,
              "end_ns": 296704350872710,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423235584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 345.1773793105352,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052324665,
                "rss_peak_bytes": 1220349952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1311.133,
                "predicted_n": 128,
                "predicted_per_second": 96.86278966359629,
                "predicted_per_token_ms": 10.32388188976378
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.05752376
            },
            {
              "begin_ns": 296704410730642,
              "complete": true,
              "e2e_s": 0.55043439,
              "end_ns": 296704961165032,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475959296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 136.9572194027207,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050197716,
                "rss_peak_bytes": 1273073664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.455,
                "predicted_n": 34,
                "predicted_per_second": 96.08245621697165,
                "predicted_per_token_ms": 10.407727272727271
              },
              "tool_call_valid": true,
              "ttft_s": 0.303672253,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296705027619197,
              "complete": true,
              "e2e_s": 0.530094755,
              "end_ns": 296705557713952,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475996160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 125.89383409612968,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05577417,
                "rss_peak_bytes": 1273110528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 254.808,
                "predicted_n": 25,
                "predicted_per_second": 94.1885655081473,
                "predicted_per_token_ms": 10.616999999999999
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27522675,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297036279835201,
              "complete": true,
              "e2e_s": 0.156972639,
              "end_ns": 297036436807840,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.77302848999332,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051427126,
                "rss_peak_bytes": 1215520768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.76,
                "predicted_n": 10,
                "predicted_per_second": 93.98496240601503,
                "predicted_per_token_ms": 10.64
              },
              "ttft_s": 0.061178205,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297036515672679,
              "complete": true,
              "e2e_s": 0.148920091,
              "end_ns": 297036664592770,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.61151275832232,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050574168,
                "rss_peak_bytes": 1215520768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.758,
                "predicted_n": 9,
                "predicted_per_second": 93.28575759695889,
                "predicted_per_token_ms": 10.71975
              },
              "ttft_s": 0.063044861,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297036738069296,
              "complete": true,
              "e2e_s": 0.529847046,
              "end_ns": 297037267916342,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.84085559496899,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051221752,
                "rss_peak_bytes": 1215565824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 397.529,
                "predicted_n": 39,
                "predicted_per_second": 95.59051037785923,
                "predicted_per_token_ms": 10.46128947368421
              },
              "ttft_s": 0.132293278,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297037342909591,
              "complete": true,
              "e2e_s": 0.307413707,
              "end_ns": 297037650323298,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.88829596823513,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050444384,
                "rss_peak_bytes": 1218527232,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.058,
                "predicted_n": 23,
                "predicted_per_second": 96.04554305023183,
                "predicted_per_token_ms": 10.411727272727273
              },
              "ttft_s": 0.078312042,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297037725128643,
              "complete": true,
              "e2e_s": 0.256741486,
              "end_ns": 297037981870129,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.19725454493715,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052322382,
                "rss_peak_bytes": 1218527232,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 180.371,
                "predicted_n": 18,
                "predicted_per_second": 94.25018434227232,
                "predicted_per_token_ms": 10.610058823529412
              },
              "ttft_s": 0.076373765,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297038056099652,
              "complete": true,
              "e2e_s": 0.397796814,
              "end_ns": 297038453896466,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475467776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 92.38932867586486,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05227646,
                "rss_peak_bytes": 1271238656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.928,
                "predicted_n": 29,
                "predicted_per_second": 96.24374415662982,
                "predicted_per_token_ms": 10.390285714285714
              },
              "ttft_s": 0.106844561,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297038529328162,
              "complete": true,
              "e2e_s": 1.027491918,
              "end_ns": 297039556820080,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475930624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 266.71416502839213,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050393581,
                "rss_peak_bytes": 1271701504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.119,
                "predicted_n": 16,
                "predicted_per_second": 94.26906906152,
                "predicted_per_token_ms": 10.607933333333333
              },
              "ttft_s": 0.868245465,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297039635105973,
              "complete": true,
              "e2e_s": 0.204516049,
              "end_ns": 297039839622022,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 47.09800554586824,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050518727,
                "rss_peak_bytes": 1219026944,
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
              "ttft_s": 0.204351978
            },
            {
              "begin_ns": 297039905471838,
              "complete": true,
              "e2e_s": 1.365980601,
              "end_ns": 297041271452439,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 351.93644835696506,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051048517,
                "rss_peak_bytes": 1219026944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.612,
                "predicted_n": 128,
                "predicted_per_second": 97.04939279175187,
                "predicted_per_token_ms": 10.304031496062994
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057277108
            },
            {
              "begin_ns": 297041345799012,
              "complete": true,
              "e2e_s": 0.549811143,
              "end_ns": 297041895610155,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475975680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.4993147484889,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050736265,
                "rss_peak_bytes": 1271746560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.615,
                "predicted_n": 34,
                "predicted_per_second": 96.3180246048772,
                "predicted_per_token_ms": 10.382272727272728
              },
              "tool_call_valid": true,
              "ttft_s": 0.303161119,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297041982739610,
              "complete": true,
              "e2e_s": 0.524259212,
              "end_ns": 297042506998822,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476016640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 126.8747001280642,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053423157,
                "rss_peak_bytes": 1271787520,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.481,
                "predicted_n": 25,
                "predicted_per_second": 96.19971059920394,
                "predicted_per_token_ms": 10.395041666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.274763658,
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
          "gpu_j_per_correct_token": 26.793961172247815,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 665341952,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7772.1878707965825,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.086083624,
              "rss_peak_bytes": 11004628992,
              "swap_peak_bytes": 207069184
            },
            {
              "anon_peak_bytes": 772702208,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7125.254540973203,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.08957206,
              "rss_peak_bytes": 12139773952,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14897.442411769785,
          "raw_requests": [
            {
              "begin_ns": 296794142844196,
              "complete": true,
              "e2e_s": 0.522085863,
              "end_ns": 296794664930059,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605548544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 109.22994133207264,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050718072,
                "rss_peak_bytes": 829079552,
                "swap_peak_bytes": 163631104
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 276.484,
                "predicted_n": 10,
                "predicted_per_second": 32.551612389867046,
                "predicted_per_token_ms": 30.720444444444443
              },
              "ttft_s": 0.23892789,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296794726043652,
              "complete": true,
              "e2e_s": 0.607114768,
              "end_ns": 296795333158420,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 450412544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 139.71106779964114,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051412327,
                "rss_peak_bytes": 675467264,
                "swap_peak_bytes": 161959936
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 374.418,
                "predicted_n": 14,
                "predicted_per_second": 34.72055296486814,
                "predicted_per_token_ms": 28.801384615384617
              },
              "ttft_s": 0.228261471,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296795395848160,
              "complete": true,
              "e2e_s": 1.827340096,
              "end_ns": 296797223188256,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 451530752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 477.867973259455,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05192609,
                "rss_peak_bytes": 678182912,
                "swap_peak_bytes": 161783808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1245.757,
                "predicted_n": 45,
                "predicted_per_second": 35.3198898340527,
                "predicted_per_token_ms": 28.312659090909094
              },
              "ttft_s": 0.574975001,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 296797310828871,
              "complete": true,
              "e2e_s": 1.0582789,
              "end_ns": 296798369107771,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 455782400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 255.13551012457134,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051826829,
                "rss_peak_bytes": 684081152,
                "swap_peak_bytes": 159817728
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 770.892,
                "predicted_n": 28,
                "predicted_per_second": 35.024361389144005,
                "predicted_per_token_ms": 28.551555555555556
              },
              "ttft_s": 0.278841954,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 296798433189604,
              "complete": true,
              "e2e_s": 0.886538,
              "end_ns": 296799319727604,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 456638464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 219.0363887700736,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051439822,
                "rss_peak_bytes": 686211072,
                "swap_peak_bytes": 159039488
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 627.961,
                "predicted_n": 23,
                "predicted_per_second": 35.034022813518675,
                "predicted_per_token_ms": 28.54368181818182
              },
              "ttft_s": 0.253492618,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 296799386072379,
              "complete": true,
              "e2e_s": 1.195769358,
              "end_ns": 296800581841737,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 614395904,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 294.37337153538044,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052714684,
                "rss_peak_bytes": 845160448,
                "swap_peak_bytes": 158318592
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 795.292,
                "predicted_n": 29,
                "predicted_per_second": 35.20719433868315,
                "predicted_per_token_ms": 28.403285714285715
              },
              "ttft_s": 0.393529393,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296800647708202,
              "complete": true,
              "e2e_s": 3.812699603,
              "end_ns": 296804460407805,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615542784,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1015.886511879293,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055324294,
                "rss_peak_bytes": 846831616,
                "swap_peak_bytes": 157671424
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 591.597,
                "predicted_n": 21,
                "predicted_per_second": 33.80679753277992,
                "predicted_per_token_ms": 29.57985
              },
              "ttft_s": 3.215889338,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296804523103789,
              "complete": true,
              "e2e_s": 0.72182206,
              "end_ns": 296805244925849,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 458739712,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 182.14342589889162,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052389989,
                "rss_peak_bytes": 690028544,
                "swap_peak_bytes": 157028352
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
              "ttft_s": 0.721674108
            },
            {
              "begin_ns": 296805301742947,
              "complete": true,
              "e2e_s": 3.776344831,
              "end_ns": 296809078087778,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 458756096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1030.7745252672094,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051896737,
                "rss_peak_bytes": 690044928,
                "swap_peak_bytes": 157024256
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3579.275,
                "predicted_n": 128,
                "predicted_per_second": 35.48204594505871,
                "predicted_per_token_ms": 28.183267716535433
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196947835
            },
            {
              "begin_ns": 296809144162691,
              "complete": true,
              "e2e_s": 1.701828943,
              "end_ns": 296810845991634,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615686144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 447.91689451567197,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054320942,
                "rss_peak_bytes": 846974976,
                "swap_peak_bytes": 157007872
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.027,
                "predicted_n": 34,
                "predicted_per_second": 35.10537463285629,
                "predicted_per_token_ms": 28.485666666666667
              },
              "tool_call_valid": true,
              "ttft_s": 1.025175497,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296810919757679,
              "complete": true,
              "e2e_s": 1.774088043,
              "end_ns": 296812693845722,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615718912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 453.8891018886427,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051947839,
                "rss_peak_bytes": 847007744,
                "swap_peak_bytes": 156999680
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.723,
                "predicted_n": 25,
                "predicted_per_second": 35.15334916210527,
                "predicted_per_token_ms": 28.446791666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091333144,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 296960666697552,
              "complete": true,
              "e2e_s": 0.465333786,
              "end_ns": 296961132031338,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 108.54145312680471,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050776653,
                "rss_peak_bytes": 1257422848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.941,
                "predicted_n": 10,
                "predicted_per_second": 34.22821089141671,
                "predicted_per_token_ms": 29.215666666666664
              },
              "ttft_s": 0.202407602,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296961199677214,
              "complete": true,
              "e2e_s": 0.575708201,
              "end_ns": 296961775385415,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.31905481622772,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050154587,
                "rss_peak_bytes": 1257422848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.348,
                "predicted_n": 14,
                "predicted_per_second": 35.00759395499639,
                "predicted_per_token_ms": 28.56523076923077
              },
              "ttft_s": 0.204366918,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296961850998675,
              "complete": true,
              "e2e_s": 1.764565962,
              "end_ns": 296963615564637,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 477.3659457114662,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.08957206,
                "rss_peak_bytes": 1257422848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.904,
                "predicted_n": 45,
                "predicted_per_second": 35.40096419353385,
                "predicted_per_token_ms": 28.247818181818182
              },
              "ttft_s": 0.521628476,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 296963695448201,
              "complete": true,
              "e2e_s": 0.997407775,
              "end_ns": 296964692855976,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 266.0435317167228,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.057785421,
                "rss_peak_bytes": 1260720128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 766.607,
                "predicted_n": 28,
                "predicted_per_second": 35.22013234943068,
                "predicted_per_token_ms": 28.39285185185185
              },
              "ttft_s": 0.230797796,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 296964763730564,
              "complete": true,
              "e2e_s": 0.847399495,
              "end_ns": 296965611130059,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 221.40488206007012,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051332577,
                "rss_peak_bytes": 1260720128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.684,
                "predicted_n": 23,
                "predicted_per_second": 35.21780612277568,
                "predicted_per_token_ms": 28.39472727272727
              },
              "ttft_s": 0.222651304,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 296965680271016,
              "complete": true,
              "e2e_s": 1.144513483,
              "end_ns": 296966824784499,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772157440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 291.3580923346963,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052374157,
                "rss_peak_bytes": 1417633792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.493,
                "predicted_n": 29,
                "predicted_per_second": 35.376181469703454,
                "predicted_per_token_ms": 28.267607142857145
              },
              "ttft_s": 0.352987825,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296966892431367,
              "complete": true,
              "e2e_s": 3.783894286,
              "end_ns": 296970676325653,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772620288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1013.7845447406007,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056062089,
                "rss_peak_bytes": 1418096640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.47,
                "predicted_n": 21,
                "predicted_per_second": 34.39558360706485,
                "predicted_per_token_ms": 29.073500000000003
              },
              "ttft_s": 3.202345654,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296970747041811,
              "complete": true,
              "e2e_s": 0.720105454,
              "end_ns": 296971467147265,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772620288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 191.68433615676554,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053258134,
                "rss_peak_bytes": 1418096640,
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
              "ttft_s": 0.719937287
            },
            {
              "begin_ns": 296971534169815,
              "complete": true,
              "e2e_s": 3.775483499,
              "end_ns": 296975309653314,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615743488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1049.9853833414734,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054241796,
                "rss_peak_bytes": 1261219840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.531,
                "predicted_n": 128,
                "predicted_per_second": 35.45969586749354,
                "predicted_per_token_ms": 28.201031496062992
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193899092
            },
            {
              "begin_ns": 296975382975583,
              "complete": true,
              "e2e_s": 1.705305442,
              "end_ns": 296977088281025,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772665344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 450.2508020557218,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054790883,
                "rss_peak_bytes": 1418141696,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 941.169,
                "predicted_n": 34,
                "predicted_per_second": 35.06277831080284,
                "predicted_per_token_ms": 28.520272727272726
              },
              "tool_call_valid": true,
              "ttft_s": 1.028947346,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296977165693609,
              "complete": true,
              "e2e_s": 1.777132155,
              "end_ns": 296978942825764,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772702208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 457.02121096884014,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05207935,
                "rss_peak_bytes": 1418178560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.084,
                "predicted_n": 25,
                "predicted_per_second": 35.13477112624509,
                "predicted_per_token_ms": 28.46183333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.09394236,
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
          "gpu_j_per_correct_token": 25.56585458526683,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772673536,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7085.522489302741,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.062247828,
              "rss_peak_bytes": 1417048064,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772669440,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7129.092660105617,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.076180753,
              "rss_peak_bytes": 1418137600,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14214.615149408357,
          "raw_requests": [
            {
              "begin_ns": 296852141198176,
              "complete": true,
              "e2e_s": 0.465913954,
              "end_ns": 296852607112130,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 639475712,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 107.37800818681323,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051636062,
                "rss_peak_bytes": 1283526656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.077,
                "predicted_n": 10,
                "predicted_per_second": 34.341052438787074,
                "predicted_per_token_ms": 29.119666666666667
              },
              "ttft_s": 0.203782549,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296852671236276,
              "complete": true,
              "e2e_s": 0.571806858,
              "end_ns": 296853243043134,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612216832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 143.44825953751308,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052166588,
                "rss_peak_bytes": 1256267776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.983,
                "predicted_n": 14,
                "predicted_per_second": 35.04203696665346,
                "predicted_per_token_ms": 28.537153846153846
              },
              "ttft_s": 0.200844639,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296853309098085,
              "complete": true,
              "e2e_s": 1.758663999,
              "end_ns": 296855067762084,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612216832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 473.3183014829686,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051157516,
                "rss_peak_bytes": 1256267776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1239.231,
                "predicted_n": 45,
                "predicted_per_second": 35.50589034651328,
                "predicted_per_token_ms": 28.16434090909091
              },
              "ttft_s": 0.519397502,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 296855133100729,
              "complete": true,
              "e2e_s": 0.987808362,
              "end_ns": 296856120909091,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615202816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 258.3506113208627,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051400476,
                "rss_peak_bytes": 1259577344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 762.824,
                "predicted_n": 28,
                "predicted_per_second": 35.39479617841074,
                "predicted_per_token_ms": 28.252740740740737
              },
              "ttft_s": 0.224922777,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 296856188055299,
              "complete": true,
              "e2e_s": 0.847062027,
              "end_ns": 296857035117326,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615202816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 217.6333461224362,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051702526,
                "rss_peak_bytes": 1259577344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.596,
                "predicted_n": 23,
                "predicted_per_second": 35.27925131014311,
                "predicted_per_token_ms": 28.34527272727273
              },
              "ttft_s": 0.223399842,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 296857098729574,
              "complete": true,
              "e2e_s": 1.145830252,
              "end_ns": 296858244559826,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772120576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 288.5416389282199,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.0530588,
                "rss_peak_bytes": 1416495104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.341,
                "predicted_n": 29,
                "predicted_per_second": 35.338320243430545,
                "predicted_per_token_ms": 28.29789285714286
              },
              "ttft_s": 0.353480801,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296858338748216,
              "complete": true,
              "e2e_s": 3.77717771,
              "end_ns": 296862115925926,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772583424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1008.1092562112683,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.061824024,
                "rss_peak_bytes": 1416957952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.34,
                "predicted_n": 21,
                "predicted_per_second": 34.46255643243616,
                "predicted_per_token_ms": 29.017000000000003
              },
              "ttft_s": 3.196798572,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296862178612542,
              "complete": true,
              "e2e_s": 0.721986814,
              "end_ns": 296862900599356,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615714816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.53595570622065,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051682556,
                "rss_peak_bytes": 1260089344,
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
              "ttft_s": 0.721862318
            },
            {
              "begin_ns": 296862956140724,
              "complete": true,
              "e2e_s": 3.766343287,
              "end_ns": 296866722484011,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615714816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1046.3211837780277,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052468687,
                "rss_peak_bytes": 1260089344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3573.2,
                "predicted_n": 128,
                "predicted_per_second": 35.54237098399194,
                "predicted_per_token_ms": 28.13543307086614
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193065828
            },
            {
              "begin_ns": 296866787131372,
              "complete": true,
              "e2e_s": 1.700900455,
              "end_ns": 296868488031827,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772636672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 446.2540238262827,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052551073,
                "rss_peak_bytes": 1417011200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.373,
                "predicted_n": 34,
                "predicted_per_second": 35.12981531298004,
                "predicted_per_token_ms": 28.465848484848486
              },
              "tool_call_valid": true,
              "ttft_s": 1.024913963,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296868559909871,
              "complete": true,
              "e2e_s": 1.773004836,
              "end_ns": 296870332914707,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772673536,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 452.32593273916416,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053670978,
                "rss_peak_bytes": 1417048064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.908,
                "predicted_n": 25,
                "predicted_per_second": 35.19536359743543,
                "predicted_per_token_ms": 28.412833333333335
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091038909,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 296906318105392,
              "complete": true,
              "e2e_s": 0.465698537,
              "end_ns": 296906783803929,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612249600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 109.23356726979837,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053601396,
                "rss_peak_bytes": 1257394176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.119,
                "predicted_n": 10,
                "predicted_per_second": 34.20505550720396,
                "predicted_per_token_ms": 29.235444444444447
              },
              "ttft_s": 0.202536462,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 296906845192674,
              "complete": true,
              "e2e_s": 0.575175113,
              "end_ns": 296907420367787,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612249600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 141.27796941087516,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050663014,
                "rss_peak_bytes": 1257394176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.429,
                "predicted_n": 14,
                "predicted_per_second": 34.999959615431216,
                "predicted_per_token_ms": 28.571461538461538
              },
              "ttft_s": 0.203692639,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 296907486100190,
              "complete": true,
              "e2e_s": 1.760276404,
              "end_ns": 296909246376594,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612253696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 477.65155457575037,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050717359,
                "rss_peak_bytes": 1257398272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.428,
                "predicted_n": 45,
                "predicted_per_second": 35.471627535012104,
                "predicted_per_token_ms": 28.19154545454546
              },
              "ttft_s": 0.519823857,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 296909312606658,
              "complete": true,
              "e2e_s": 1.019510318,
              "end_ns": 296910332116976,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615227392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 269.59393422966787,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052068726,
                "rss_peak_bytes": 1260695552,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 766.521,
                "predicted_n": 28,
                "predicted_per_second": 35.22408388028508,
                "predicted_per_token_ms": 28.389666666666667
              },
              "ttft_s": 0.252999619,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 296910395218559,
              "complete": true,
              "e2e_s": 0.8472203,
              "end_ns": 296911242438859,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615227392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 227.14407579385485,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050740833,
                "rss_peak_bytes": 1260695552,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.613,
                "predicted_n": 23,
                "predicted_per_second": 35.278289580236454,
                "predicted_per_token_ms": 28.346045454545457
              },
              "ttft_s": 0.223619729,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 296911311638756,
              "complete": true,
              "e2e_s": 1.147757942,
              "end_ns": 296912459396698,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772149248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 296.3316658239683,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053407826,
                "rss_peak_bytes": 1417617408,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 793.684,
                "predicted_n": 29,
                "predicted_per_second": 35.278523946558074,
                "predicted_per_token_ms": 28.34585714285714
              },
              "ttft_s": 0.35404388,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 296912528205525,
              "complete": true,
              "e2e_s": 3.783570394,
              "end_ns": 296916311775919,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772575232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1012.0971431245979,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054477241,
                "rss_peak_bytes": 1418043392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.309,
                "predicted_n": 21,
                "predicted_per_second": 34.40510984691446,
                "predicted_per_token_ms": 29.06545
              },
              "ttft_s": 3.20226898,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 296916377193239,
              "complete": true,
              "e2e_s": 0.723324443,
              "end_ns": 296917100517682,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615702528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 186.1188331676948,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.057226423,
                "rss_peak_bytes": 1261170688,
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
              "ttft_s": 0.723198316
            },
            {
              "begin_ns": 296917162291993,
              "complete": true,
              "e2e_s": 3.776221187,
              "end_ns": 296920938513180,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615702528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1050.1017127899452,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054894238,
                "rss_peak_bytes": 1261170688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3576.69,
                "predicted_n": 128,
                "predicted_per_second": 35.50769007098742,
                "predicted_per_token_ms": 28.162913385826773
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.19939833
            },
            {
              "begin_ns": 296921008183880,
              "complete": true,
              "e2e_s": 1.704325911,
              "end_ns": 296922712509791,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772628480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 459.2146093412224,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050698394,
                "rss_peak_bytes": 1418096640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.458,
                "predicted_n": 34,
                "predicted_per_second": 35.089286283916984,
                "predicted_per_token_ms": 28.498727272727272
              },
              "tool_call_valid": true,
              "ttft_s": 1.027364635,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 296922789211368,
              "complete": true,
              "e2e_s": 1.77603343,
              "end_ns": 296924565244798,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772669440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 461.75982762734765,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053113065,
                "rss_peak_bytes": 1418137600,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.358,
                "predicted_n": 25,
                "predicted_per_second": 35.172153034037855,
                "predicted_per_token_ms": 28.431583333333332
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093588838,
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
