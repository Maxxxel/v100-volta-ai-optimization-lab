# Public audit excerpt

Original SHA256: `b8a83b89fd187aadf424abdadf22cd8e206081adc69ace53c53bfbad6468109b`

Original file: `RESULTS.json`; 266301 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "omnicoder2": {
      "metrics": {
        "A": {
          "correct_tokens": 562,
          "gpu_j_per_correct_token": 9.671853285568735,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470355968,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2677.016463078122,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.212261553,
              "rss_peak_bytes": 7726915584,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470343680,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2758.565083411508,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.056218733,
              "rss_peak_bytes": 7724113920,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5435.5815464896295,
          "raw_requests": [
            {
              "begin_ns": 295365817684788,
              "complete": true,
              "e2e_s": 0.182866831,
              "end_ns": 295366000551619,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414101504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.08646101910525,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050232509,
                "rss_peak_bytes": 1469779968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.743,
                "predicted_n": 10,
                "predicted_per_second": 77.09241667594631,
                "predicted_per_token_ms": 12.971444444444444
              },
              "ttft_s": 0.066044976,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295366059172504,
              "complete": true,
              "e2e_s": 0.234566198,
              "end_ns": 295366293738702,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414101504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 56.28322979429205,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051060658,
                "rss_peak_bytes": 1469779968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 167.001,
                "predicted_n": 14,
                "predicted_per_second": 77.84384524643565,
                "predicted_per_token_ms": 12.84623076923077
              },
              "ttft_s": 0.067555077,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295366381265881,
              "complete": true,
              "e2e_s": 0.666194886,
              "end_ns": 295367047460767,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414101504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 174.14617887394806,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050708024,
                "rss_peak_bytes": 1469825024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.112,
                "predicted_n": 44,
                "predicted_per_second": 79.31940263266632,
                "predicted_per_token_ms": 12.607255813953488
              },
              "ttft_s": 0.124091627,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295367128904535,
              "complete": true,
              "e2e_s": 0.357684901,
              "end_ns": 295367486589436,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414105600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 88.85119237576804,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05158813,
                "rss_peak_bytes": 1469829120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.764,
                "predicted_n": 23,
                "predicted_per_second": 78.91980313096383,
                "predicted_per_token_ms": 12.671090909090909
              },
              "ttft_s": 0.078871141,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295367586389656,
              "complete": true,
              "e2e_s": 0.295209305,
              "end_ns": 295367881598961,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414109696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.89740235405277,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050610772,
                "rss_peak_bytes": 1469833216,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.213,
                "predicted_n": 18,
                "predicted_per_second": 78.62616956427226,
                "predicted_per_token_ms": 12.718411764705882
              },
              "ttft_s": 0.078978479,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295367935202649,
              "complete": true,
              "e2e_s": 0.470153925,
              "end_ns": 295368405356574,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469807104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 113.23515409270647,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05189596,
                "rss_peak_bytes": 1525530624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.775,
                "predicted_n": 29,
                "predicted_per_second": 79.14635008126635,
                "predicted_per_token_ms": 12.634821428571428
              },
              "ttft_s": 0.116344111,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295368465745150,
              "complete": true,
              "e2e_s": 1.076278653,
              "end_ns": 295369542023803,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470274048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 285.3212901292101,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056521421,
                "rss_peak_bytes": 1525997568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.741,
                "predicted_n": 21,
                "predicted_per_second": 77.89951741248964,
                "predicted_per_token_ms": 12.83705
              },
              "ttft_s": 0.819532314,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295369597112586,
              "complete": true,
              "e2e_s": 0.198090718,
              "end_ns": 295369795203304,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417611776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.77792148251503,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050222263,
                "rss_peak_bytes": 1473335296,
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
              "ttft_s": 0.197960898
            },
            {
              "begin_ns": 295369843097233,
              "complete": true,
              "e2e_s": 1.657103153,
              "end_ns": 295371500200386,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417611776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.1806911969253,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052813813,
                "rss_peak_bytes": 1473335296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.198,
                "predicted_n": 128,
                "predicted_per_second": 79.66388114901662,
                "predicted_per_token_ms": 12.552740157480315
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062762717
            },
            {
              "begin_ns": 295371567595299,
              "complete": true,
              "e2e_s": 0.618611969,
              "end_ns": 295372186207268,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 159.38478740611492,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051018536,
                "rss_peak_bytes": 1526050816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.553,
                "predicted_n": 34,
                "predicted_per_second": 79.031883377679,
                "predicted_per_token_ms": 12.653121212121212
              },
              "tool_call_valid": true,
              "ttft_s": 0.317244623,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295372250164873,
              "complete": true,
              "e2e_s": 0.558481547,
              "end_ns": 295372808646420,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470355968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 146.98106096564982,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052141787,
                "rss_peak_bytes": 1526079488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.081,
                "predicted_n": 25,
                "predicted_per_second": 78.92633870580536,
                "predicted_per_token_ms": 12.670041666666668
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254382222,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295818655134972,
              "complete": true,
              "e2e_s": 0.182044034,
              "end_ns": 295818837179006,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.656202645373334,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051577448,
                "rss_peak_bytes": 1468510208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.12,
                "predicted_n": 10,
                "predicted_per_second": 77.50602824664139,
                "predicted_per_token_ms": 12.902222222222223
              },
              "ttft_s": 0.065909832,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295818931147167,
              "complete": true,
              "e2e_s": 0.234388526,
              "end_ns": 295819165535693,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.87849649071842,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050896504,
                "rss_peak_bytes": 1468510208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.726,
                "predicted_n": 14,
                "predicted_per_second": 77.97224188189004,
                "predicted_per_token_ms": 12.825076923076923
              },
              "ttft_s": 0.06767055,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295819244110950,
              "complete": true,
              "e2e_s": 0.667018174,
              "end_ns": 295819911129124,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.82803554833043,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050561391,
                "rss_peak_bytes": 1468555264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 543.357,
                "predicted_n": 44,
                "predicted_per_second": 79.13765719407314,
                "predicted_per_token_ms": 12.63620930232558
              },
              "ttft_s": 0.123603494,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295819987119123,
              "complete": true,
              "e2e_s": 0.359113502,
              "end_ns": 295820346232625,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.84664777857064,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052262849,
                "rss_peak_bytes": 1468559360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 280.14,
                "predicted_n": 23,
                "predicted_per_second": 78.53216249018348,
                "predicted_per_token_ms": 12.733636363636363
              },
              "ttft_s": 0.079338881,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295820443743774,
              "complete": true,
              "e2e_s": 0.295220635,
              "end_ns": 295820738964409,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.58044442101551,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050489484,
                "rss_peak_bytes": 1468563456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.437,
                "predicted_n": 18,
                "predicted_per_second": 78.54479594524041,
                "predicted_per_token_ms": 12.731588235294119
              },
              "ttft_s": 0.078790598,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295820844054039,
              "complete": true,
              "e2e_s": 0.468808665,
              "end_ns": 295821312862704,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469786624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 117.67337272507905,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051215538,
                "rss_peak_bytes": 1524256768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.921,
                "predicted_n": 29,
                "predicted_per_second": 79.1137005150867,
                "predicted_per_token_ms": 12.640035714285714
              },
              "ttft_s": 0.114910685,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295821421367490,
              "complete": true,
              "e2e_s": 1.075106245,
              "end_ns": 295822496473735,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470253568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 288.52409083446787,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05400227,
                "rss_peak_bytes": 1524723712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.14,
                "predicted_n": 21,
                "predicted_per_second": 78.082298742875,
                "predicted_per_token_ms": 12.806999999999999
              },
              "ttft_s": 0.81892523,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295822609145037,
              "complete": true,
              "e2e_s": 0.197312214,
              "end_ns": 295822806457251,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417591296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.390153565685374,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051627575,
                "rss_peak_bytes": 1472061440,
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
              "ttft_s": 0.197151614
            },
            {
              "begin_ns": 295822903138945,
              "complete": true,
              "e2e_s": 1.659127675,
              "end_ns": 295824562266620,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417591296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 448.68818240514133,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05205267,
                "rss_peak_bytes": 1472061440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.835,
                "predicted_n": 128,
                "predicted_per_second": 79.58216231627956,
                "predicted_per_token_ms": 12.565629921259843
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063115552
            },
            {
              "begin_ns": 295824671052471,
              "complete": true,
              "e2e_s": 0.619070178,
              "end_ns": 295825290122649,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470306816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.62023617720314,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050629346,
                "rss_peak_bytes": 1524776960,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.78,
                "predicted_n": 34,
                "predicted_per_second": 78.98894154818325,
                "predicted_per_token_ms": 12.659999999999998
              },
              "tool_call_valid": true,
              "ttft_s": 0.317489248,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295825417179880,
              "complete": true,
              "e2e_s": 0.560073191,
              "end_ns": 295825977253071,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470343680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.60319694026828,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05096602,
                "rss_peak_bytes": 1524813824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 305.081,
                "predicted_n": 25,
                "predicted_per_second": 78.66763253037718,
                "predicted_per_token_ms": 12.711708333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254931322,
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
          "gpu_j_per_correct_token": 10.063910023205718,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470327296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2668.6539742274313,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.06368195,
              "rss_peak_bytes": 7726952448,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470294528,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2987.2634588141827,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.120330905,
              "rss_peak_bytes": 7570771968,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5655.917433041614,
          "raw_requests": [
            {
              "begin_ns": 295394864284247,
              "complete": true,
              "e2e_s": 0.182737959,
              "end_ns": 295395047022206,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.38641517196775,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050008415,
                "rss_peak_bytes": 1471426560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.498,
                "predicted_n": 10,
                "predicted_per_second": 77.25454514240587,
                "predicted_per_token_ms": 12.944222222222223
              },
              "ttft_s": 0.066222219,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295395101766730,
              "complete": true,
              "e2e_s": 0.233242198,
              "end_ns": 295395335008928,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 58.24087531247648,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050042344,
                "rss_peak_bytes": 1471426560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.033,
                "predicted_n": 14,
                "predicted_per_second": 78.29768780905002,
                "predicted_per_token_ms": 12.77176923076923
              },
              "ttft_s": 0.06717424,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295395394188779,
              "complete": true,
              "e2e_s": 0.666176891,
              "end_ns": 295396060365670,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.9535203574873,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051700199,
                "rss_peak_bytes": 1471471616,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.839,
                "predicted_n": 44,
                "predicted_per_second": 79.21317370343692,
                "predicted_per_token_ms": 12.624162790697676
              },
              "ttft_s": 0.123340975,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295396118880513,
              "complete": true,
              "e2e_s": 0.357717296,
              "end_ns": 295396476597809,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 84.11965200999691,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051022836,
                "rss_peak_bytes": 1471471616,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.352,
                "predicted_n": 23,
                "predicted_per_second": 78.75368710444172,
                "predicted_per_token_ms": 12.69781818181818
              },
              "ttft_s": 0.078338659,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295396531656369,
              "complete": true,
              "e2e_s": 0.294899813,
              "end_ns": 295396826556182,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.2815401438614,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050738086,
                "rss_peak_bytes": 1471475712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.063,
                "predicted_n": 18,
                "predicted_per_second": 78.68075515011824,
                "predicted_per_token_ms": 12.709588235294117
              },
              "ttft_s": 0.078783717,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295396882244431,
              "complete": true,
              "e2e_s": 0.495460314,
              "end_ns": 295397377704745,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469766144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 116.03697329131074,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052804479,
                "rss_peak_bytes": 1527074816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 355.37,
                "predicted_n": 29,
                "predicted_per_second": 78.7911191152883,
                "predicted_per_token_ms": 12.691785714285714
              },
              "ttft_s": 0.140101303,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295397435233954,
              "complete": true,
              "e2e_s": 1.075860102,
              "end_ns": 295398511094056,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470237184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 284.16504285538184,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050797458,
                "rss_peak_bytes": 1526226944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.093,
                "predicted_n": 21,
                "predicted_per_second": 78.09662895901097,
                "predicted_per_token_ms": 12.80465
              },
              "ttft_s": 0.819644472,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295398567176432,
              "complete": true,
              "e2e_s": 0.197099377,
              "end_ns": 295398764275809,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417574912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.297603143466766,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050406748,
                "rss_peak_bytes": 1473564672,
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
              "ttft_s": 0.196938933
            },
            {
              "begin_ns": 295398818737359,
              "complete": true,
              "e2e_s": 1.666901668,
              "end_ns": 295400485639027,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417574912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 449.03974865624417,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056275672,
                "rss_peak_bytes": 1473564672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1604.146,
                "predicted_n": 128,
                "predicted_per_second": 79.16985112327681,
                "predicted_per_token_ms": 12.631070866141732
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062628974
            },
            {
              "begin_ns": 295400548216490,
              "complete": true,
              "e2e_s": 0.618452342,
              "end_ns": 295401166668832,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 154.30731529391622,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050675237,
                "rss_peak_bytes": 1526284288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.875,
                "predicted_n": 34,
                "predicted_per_second": 78.97098414597667,
                "predicted_per_token_ms": 12.662878787878787
              },
              "tool_call_valid": true,
              "ttft_s": 0.317254234,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295401228788904,
              "complete": true,
              "e2e_s": 0.559136583,
              "end_ns": 295401787925487,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 142.17840463695003,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051011538,
                "rss_peak_bytes": 1526317056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.369,
                "predicted_n": 25,
                "predicted_per_second": 78.85165703471772,
                "predicted_per_token_ms": 12.682041666666668
              },
              "tool_facts_valid": true,
              "ttft_s": 0.25473091,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295787862559457,
              "complete": true,
              "e2e_s": 0.182130568,
              "end_ns": 295788044690025,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 39.75463444106559,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05072868,
                "rss_peak_bytes": 1337663488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.089,
                "predicted_n": 10,
                "predicted_per_second": 77.52672518498738,
                "predicted_per_token_ms": 12.898777777777777
              },
              "ttft_s": 0.06602626,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295788125307975,
              "complete": true,
              "e2e_s": 0.233822999,
              "end_ns": 295788359130974,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 51.939900205235375,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053095907,
                "rss_peak_bytes": 1337663488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.097,
                "predicted_n": 14,
                "predicted_per_second": 78.26751837781538,
                "predicted_per_token_ms": 12.776692307692308
              },
              "ttft_s": 0.06762587,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295788434037088,
              "complete": true,
              "e2e_s": 0.678754252,
              "end_ns": 295789112791340,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.8538627779209,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056047702,
                "rss_peak_bytes": 1337774080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 555.047,
                "predicted_n": 44,
                "predicted_per_second": 77.47091687730949,
                "predicted_per_token_ms": 12.90806976744186
              },
              "ttft_s": 0.123647844,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295789193290888,
              "complete": true,
              "e2e_s": 0.357960399,
              "end_ns": 295789551251287,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 92.19046789995858,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050070671,
                "rss_peak_bytes": 1337905152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.763,
                "predicted_n": 23,
                "predicted_per_second": 78.92008623813061,
                "predicted_per_token_ms": 12.671045454545453
              },
              "ttft_s": 0.079125033,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295789629130422,
              "complete": true,
              "e2e_s": 0.295260174,
              "end_ns": 295789924390596,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.66403302451477,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05064466,
                "rss_peak_bytes": 1337905152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.444,
                "predicted_n": 18,
                "predicted_per_second": 78.54225573358468,
                "predicted_per_token_ms": 12.732
              },
              "ttft_s": 0.078782691,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295790049993891,
              "complete": true,
              "e2e_s": 0.470575402,
              "end_ns": 295790520569293,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469786624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 119.38801030202836,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056101732,
                "rss_peak_bytes": 1392422912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.9,
                "predicted_n": 29,
                "predicted_per_second": 79.11839502684374,
                "predicted_per_token_ms": 12.639285714285714
              },
              "ttft_s": 0.116618681,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295790595879958,
              "complete": true,
              "e2e_s": 1.079026273,
              "end_ns": 295791674906231,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470216704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 287.8960118674675,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055606483,
                "rss_peak_bytes": 1392918528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.622,
                "predicted_n": 21,
                "predicted_per_second": 77.93564074787041,
                "predicted_per_token_ms": 12.831100000000001
              },
              "ttft_s": 0.82239164,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295791752592557,
              "complete": true,
              "e2e_s": 0.198187386,
              "end_ns": 295791950779943,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417554432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.91799881825813,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050122711,
                "rss_peak_bytes": 1340256256,
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
              "ttft_s": 0.198060033
            },
            {
              "begin_ns": 295792022197407,
              "complete": true,
              "e2e_s": 1.660651926,
              "end_ns": 295793682849333,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417554432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.5245275740549,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052051877,
                "rss_peak_bytes": 1340256256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.511,
                "predicted_n": 128,
                "predicted_per_second": 79.5983230450934,
                "predicted_per_token_ms": 12.56307874015748
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.065003945
            },
            {
              "begin_ns": 295793756145494,
              "complete": true,
              "e2e_s": 0.619510179,
              "end_ns": 295794375655673,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470265856,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 163.7935570825412,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.0565927,
                "rss_peak_bytes": 1392967680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.609,
                "predicted_n": 34,
                "predicted_per_second": 79.02128546080185,
                "predicted_per_token_ms": 12.65481818181818
              },
              "tool_call_valid": true,
              "ttft_s": 0.318671563,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295794458123411,
              "complete": true,
              "e2e_s": 0.560002233,
              "end_ns": 295795018125644,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 144.99954991806567,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052459029,
                "rss_peak_bytes": 1392996352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.666,
                "predicted_n": 25,
                "predicted_per_second": 78.7747894415524,
                "predicted_per_token_ms": 12.694416666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255315626,
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
          "gpu_j_per_correct_token": 8.90794815028374,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475996160,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2266.1416154232443,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.085479666,
              "rss_peak_bytes": 5996777472,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476041216,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2561.9662820305425,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.090989077,
              "rss_peak_bytes": 5814968320,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4828.107897453787,
          "raw_requests": [
            {
              "begin_ns": 295444979822007,
              "complete": true,
              "e2e_s": 0.158149113,
              "end_ns": 295445137971120,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419786752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 29.227533654626363,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050573012,
                "rss_peak_bytes": 1215766528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.715,
                "predicted_n": 10,
                "predicted_per_second": 94.02914903620122,
                "predicted_per_token_ms": 10.635
              },
              "ttft_s": 0.062459113,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295445195668741,
              "complete": true,
              "e2e_s": 0.148111645,
              "end_ns": 295445343780386,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419786752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.37760472419664,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050056931,
                "rss_peak_bytes": 1215766528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.138,
                "predicted_n": 9,
                "predicted_per_second": 93.96509196833375,
                "predicted_per_token_ms": 10.64225
              },
              "ttft_s": 0.062940545,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295445404178098,
              "complete": true,
              "e2e_s": 0.540692977,
              "end_ns": 295445944871075,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419786752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 134.60677197808286,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.057085964,
                "rss_peak_bytes": 1215811584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 408.33,
                "predicted_n": 39,
                "predicted_per_second": 93.0619841794627,
                "predicted_per_token_ms": 10.745526315789473
              },
              "ttft_s": 0.132306461,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295446005445255,
              "complete": true,
              "e2e_s": 0.306994445,
              "end_ns": 295446312439700,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422752256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.68225861471137,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050600263,
                "rss_peak_bytes": 1218842624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.768,
                "predicted_n": 23,
                "predicted_per_second": 96.16729612533221,
                "predicted_per_token_ms": 10.398545454545454
              },
              "ttft_s": 0.078163897,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295446373066931,
              "complete": true,
              "e2e_s": 0.253715054,
              "end_ns": 295446626781985,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422752256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 53.95768757525805,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050638397,
                "rss_peak_bytes": 1218842624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.55,
                "predicted_n": 18,
                "predicted_per_second": 95.7476767107857,
                "predicted_per_token_ms": 10.444117647058825
              },
              "ttft_s": 0.076123614,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295446693706290,
              "complete": true,
              "e2e_s": 0.400506346,
              "end_ns": 295447094212636,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475467776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.72395894559757,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050575634,
                "rss_peak_bytes": 1271558144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.708,
                "predicted_n": 29,
                "predicted_per_second": 95.98639735626037,
                "predicted_per_token_ms": 10.418142857142858
              },
              "ttft_s": 0.108740671,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295447155110715,
              "complete": true,
              "e2e_s": 1.025324978,
              "end_ns": 295448180435693,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475930624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 271.9548841909493,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053339472,
                "rss_peak_bytes": 1272020992,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.426,
                "predicted_n": 16,
                "predicted_per_second": 94.08753904632871,
                "predicted_per_token_ms": 10.6284
              },
              "ttft_s": 0.865907222,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295448241268812,
              "complete": true,
              "e2e_s": 0.204858641,
              "end_ns": 295448446127453,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.08332351479686,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051539689,
                "rss_peak_bytes": 1219346432,
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
              "ttft_s": 0.204694231
            },
            {
              "begin_ns": 295448498216572,
              "complete": true,
              "e2e_s": 1.366388711,
              "end_ns": 295449864605283,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 345.47334269476414,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05103109,
                "rss_peak_bytes": 1219346432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.919,
                "predicted_n": 128,
                "predicted_per_second": 97.02663037208566,
                "predicted_per_token_ms": 10.306448818897639
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057353612
            },
            {
              "begin_ns": 295449924861405,
              "complete": true,
              "e2e_s": 0.548808126,
              "end_ns": 295450473669531,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475971584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.67583057599697,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053750805,
                "rss_peak_bytes": 1272061952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.557,
                "predicted_n": 34,
                "predicted_per_second": 96.33433268040064,
                "predicted_per_token_ms": 10.380515151515151
              },
              "tool_call_valid": true,
              "ttft_s": 0.301935245,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295450542745737,
              "complete": true,
              "e2e_s": 0.523866281,
              "end_ns": 295451066612018,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475996160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.1775505923168,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051266344,
                "rss_peak_bytes": 1272086528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.923,
                "predicted_n": 25,
                "predicted_per_second": 95.64687174950085,
                "predicted_per_token_ms": 10.455125
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272966729,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295723568100959,
              "complete": true,
              "e2e_s": 0.156182686,
              "end_ns": 295723724283645,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.22261832665838,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050791053,
                "rss_peak_bytes": 1035853824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.404,
                "predicted_n": 10,
                "predicted_per_second": 94.33566726761981,
                "predicted_per_token_ms": 10.600444444444443
              },
              "ttft_s": 0.060726314,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295723802436306,
              "complete": true,
              "e2e_s": 0.148707342,
              "end_ns": 295723951143648,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.85743720198155,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050149244,
                "rss_peak_bytes": 1035984896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.274,
                "predicted_n": 9,
                "predicted_per_second": 93.81523090273706,
                "predicted_per_token_ms": 10.65925
              },
              "ttft_s": 0.06341597,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295724028152061,
              "complete": true,
              "e2e_s": 0.526232171,
              "end_ns": 295724554384232,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.97614628303884,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050559897,
                "rss_peak_bytes": 1036554240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.69,
                "predicted_n": 39,
                "predicted_per_second": 96.52264472046534,
                "predicted_per_token_ms": 10.360263157894737
              },
              "ttft_s": 0.132485814,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295724629877857,
              "complete": true,
              "e2e_s": 0.306692485,
              "end_ns": 295724936570342,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422772736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.83593845234763,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051134346,
                "rss_peak_bytes": 1039749120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.442,
                "predicted_n": 23,
                "predicted_per_second": 95.88479877267459,
                "predicted_per_token_ms": 10.429181818181819
              },
              "ttft_s": 0.077206893,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295725010255365,
              "complete": true,
              "e2e_s": 0.255424442,
              "end_ns": 295725265679807,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422772736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.193839934092246,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051566787,
                "rss_peak_bytes": 1040142336,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.801,
                "predicted_n": 18,
                "predicted_per_second": 95.61251061580083,
                "predicted_per_token_ms": 10.458882352941176
              },
              "ttft_s": 0.077541609,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295725340754533,
              "complete": true,
              "e2e_s": 0.3979352,
              "end_ns": 295725738689733,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475484160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 92.88095697726052,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052093779,
                "rss_peak_bytes": 1093312512,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.846,
                "predicted_n": 29,
                "predicted_per_second": 96.27087874682822,
                "predicted_per_token_ms": 10.387357142857143
              },
              "ttft_s": 0.107079274,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295725809321463,
              "complete": true,
              "e2e_s": 1.03112639,
              "end_ns": 295726840447853,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475947008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 269.10206645330135,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053887065,
                "rss_peak_bytes": 1093971968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.949,
                "predicted_n": 16,
                "predicted_per_second": 93.77989234068359,
                "predicted_per_token_ms": 10.663266666666667
              },
              "ttft_s": 0.871136822,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295726914968609,
              "complete": true,
              "e2e_s": 0.204453367,
              "end_ns": 295727119421976,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.40233450542548,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05184431,
                "rss_peak_bytes": 1041301504,
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
              "ttft_s": 0.204314881
            },
            {
              "begin_ns": 295727179089708,
              "complete": true,
              "e2e_s": 1.367950734,
              "end_ns": 295728547040442,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 349.4762495664062,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051894781,
                "rss_peak_bytes": 1041301504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.483,
                "predicted_n": 128,
                "predicted_per_second": 96.98484058212287,
                "predicted_per_token_ms": 10.310889763779526
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.058328555
            },
            {
              "begin_ns": 295728616185521,
              "complete": true,
              "e2e_s": 0.550240527,
              "end_ns": 295729166426048,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475992064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.8051134738466,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054093427,
                "rss_peak_bytes": 1094017024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.431,
                "predicted_n": 34,
                "predicted_per_second": 96.08917075045643,
                "predicted_per_token_ms": 10.407
              },
              "tool_call_valid": true,
              "ttft_s": 0.302799433,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295729246203008,
              "complete": true,
              "e2e_s": 0.523770907,
              "end_ns": 295729769973915,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476041216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 134.0703029663668,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054930887,
                "rss_peak_bytes": 1094066176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.429,
                "predicted_n": 25,
                "predicted_per_second": 95.83554620271613,
                "predicted_per_token_ms": 10.434541666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273331966,
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
          "gpu_j_per_correct_token": 8.41854722109679,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476033024,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2266.42162522563,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.091200208,
              "rss_peak_bytes": 5996785664,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476037120,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2296.4309686088313,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.080663988,
              "rss_peak_bytes": 5993095168,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4562.852593834461,
          "raw_requests": [
            {
              "begin_ns": 295420493141569,
              "complete": true,
              "e2e_s": 0.156251086,
              "end_ns": 295420649392655,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 33.20437239123315,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050106208,
                "rss_peak_bytes": 1215229952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.576,
                "predicted_n": 10,
                "predicted_per_second": 94.16589938896796,
                "predicted_per_token_ms": 10.619555555555555
              },
              "ttft_s": 0.060629636,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295420706250852,
              "complete": true,
              "e2e_s": 0.148409571,
              "end_ns": 295420854660423,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.673754957079208,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050288859,
                "rss_peak_bytes": 1215229952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.327,
                "predicted_n": 9,
                "predicted_per_second": 93.75695852426547,
                "predicted_per_token_ms": 10.665875
              },
              "ttft_s": 0.063037637,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295420912187755,
              "complete": true,
              "e2e_s": 0.527075225,
              "end_ns": 295421439262980,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.5276019286141,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051734595,
                "rss_peak_bytes": 1215275008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.003,
                "predicted_n": 39,
                "predicted_per_second": 96.69137385719702,
                "predicted_per_token_ms": 10.342184210526316
              },
              "ttft_s": 0.134046626,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295421504995864,
              "complete": true,
              "e2e_s": 0.305787615,
              "end_ns": 295421810783479,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.05357379888119,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053573751,
                "rss_peak_bytes": 1218342912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.795,
                "predicted_n": 23,
                "predicted_per_second": 96.15594746388689,
                "predicted_per_token_ms": 10.399772727272726
              },
              "ttft_s": 0.077003504,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295421871748541,
              "complete": true,
              "e2e_s": 0.254918267,
              "end_ns": 295422126666808,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 55.088887567047884,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050506204,
                "rss_peak_bytes": 1218342912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.36,
                "predicted_n": 18,
                "predicted_per_second": 95.31285041489122,
                "predicted_per_token_ms": 10.491764705882353
              },
              "ttft_s": 0.076542575,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295422191036121,
              "complete": true,
              "e2e_s": 0.39708576,
              "end_ns": 295422588121881,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475496448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.05980630709529,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050114415,
                "rss_peak_bytes": 1271058432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.427,
                "predicted_n": 29,
                "predicted_per_second": 96.40976906417103,
                "predicted_per_token_ms": 10.372392857142858
              },
              "ttft_s": 0.106557926,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295422652183297,
              "complete": true,
              "e2e_s": 1.026979336,
              "end_ns": 295423679162633,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475963392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 269.92709592483436,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.091200208,
                "rss_peak_bytes": 1271525376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.325,
                "predicted_n": 16,
                "predicted_per_second": 94.14718343009572,
                "predicted_per_token_ms": 10.621666666666666
              },
              "ttft_s": 0.867690347,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295423735808991,
              "complete": true,
              "e2e_s": 0.20409787,
              "end_ns": 295423939906861,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.14780140622798,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052437631,
                "rss_peak_bytes": 1218846720,
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
              "ttft_s": 0.203969131
            },
            {
              "begin_ns": 295423995055547,
              "complete": true,
              "e2e_s": 1.365371644,
              "end_ns": 295425360427191,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 348.2924955350731,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052654397,
                "rss_peak_bytes": 1218846720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1307.243,
                "predicted_n": 128,
                "predicted_per_second": 97.15102700875049,
                "predicted_per_token_ms": 10.293251968503936
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057986085
            },
            {
              "begin_ns": 295425424169309,
              "complete": true,
              "e2e_s": 0.549014449,
              "end_ns": 295425973183758,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476000256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.738984674744,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05410738,
                "rss_peak_bytes": 1271562240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.104,
                "predicted_n": 34,
                "predicted_per_second": 96.18074986010073,
                "predicted_per_token_ms": 10.397090909090908
              },
              "tool_call_valid": true,
              "ttft_s": 0.301701908,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295426043160023,
              "complete": true,
              "e2e_s": 0.523437774,
              "end_ns": 295426566597797,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476033024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.44738185244637,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053210944,
                "rss_peak_bytes": 1271595008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.775,
                "predicted_n": 25,
                "predicted_per_second": 95.7033197089024,
                "predicted_per_token_ms": 10.448958333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272649477,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295748093677988,
              "complete": true,
              "e2e_s": 0.156883224,
              "end_ns": 295748250561212,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 34.34176531351079,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050079994,
                "rss_peak_bytes": 1211965440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.61,
                "predicted_n": 10,
                "predicted_per_second": 94.13241292751803,
                "predicted_per_token_ms": 10.623333333333333
              },
              "ttft_s": 0.061225997,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295748328275009,
              "complete": true,
              "e2e_s": 0.148668932,
              "end_ns": 295748476943941,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 27.46322812075703,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055912649,
                "rss_peak_bytes": 1211965440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.465,
                "predicted_n": 9,
                "predicted_per_second": 93.60556953138712,
                "predicted_per_token_ms": 10.683125
              },
              "ttft_s": 0.06316525,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295748548028035,
              "complete": true,
              "e2e_s": 0.526594437,
              "end_ns": 295749074622472,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419794944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.89877257153194,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055965114,
                "rss_peak_bytes": 1212010496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.462,
                "predicted_n": 39,
                "predicted_per_second": 96.33374063914901,
                "predicted_per_token_ms": 10.38057894736842
              },
              "ttft_s": 0.132132664,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295749149649201,
              "complete": true,
              "e2e_s": 0.306651408,
              "end_ns": 295749456300609,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422760448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 73.17561723440839,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050223029,
                "rss_peak_bytes": 1215041536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.484,
                "predicted_n": 23,
                "predicted_per_second": 95.8672500043576,
                "predicted_per_token_ms": 10.43109090909091
              },
              "ttft_s": 0.077155157,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295749531733275,
              "complete": true,
              "e2e_s": 0.254052549,
              "end_ns": 295749785785824,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422760448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.54414073982311,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050417806,
                "rss_peak_bytes": 1215041536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.981,
                "predicted_n": 18,
                "predicted_per_second": 95.51581348570916,
                "predicted_per_token_ms": 10.469470588235295
              },
              "ttft_s": 0.076058287,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295749863092403,
              "complete": true,
              "e2e_s": 0.398119747,
              "end_ns": 295750261212150,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475475968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.05037272938024,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051414875,
                "rss_peak_bytes": 1267757056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.031,
                "predicted_n": 29,
                "predicted_per_second": 96.20968213008236,
                "predicted_per_token_ms": 10.393964285714286
              },
              "ttft_s": 0.107113755,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295750340187678,
              "complete": true,
              "e2e_s": 1.027074377,
              "end_ns": 295751367262055,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475942912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 275.4334778885775,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053172868,
                "rss_peak_bytes": 1268224000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.301,
                "predicted_n": 16,
                "predicted_per_second": 94.16136747415271,
                "predicted_per_token_ms": 10.620066666666666
              },
              "ttft_s": 0.867765713,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295751442150526,
              "complete": true,
              "e2e_s": 0.204361256,
              "end_ns": 295751646511782,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423280640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 47.23071733779369,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050653429,
                "rss_peak_bytes": 1215561728,
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
              "ttft_s": 0.204237343
            },
            {
              "begin_ns": 295751707045295,
              "complete": true,
              "e2e_s": 1.366609341,
              "end_ns": 295753073654636,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423280640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 349.8212601084708,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054893158,
                "rss_peak_bytes": 1215561728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.917,
                "predicted_n": 128,
                "predicted_per_second": 97.02677862691066,
                "predicted_per_token_ms": 10.306433070866142
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057590143
            },
            {
              "begin_ns": 295753145167950,
              "complete": true,
              "e2e_s": 0.550692435,
              "end_ns": 295753695860385,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476000256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 139.37118185274602,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050636246,
                "rss_peak_bytes": 1268281344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.385,
                "predicted_n": 34,
                "predicted_per_second": 96.10204289645733,
                "predicted_per_token_ms": 10.405606060606061
              },
              "tool_call_valid": true,
              "ttft_s": 0.303687805,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295753780208768,
              "complete": true,
              "e2e_s": 0.524573786,
              "end_ns": 295754304782554,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476037120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 128.13174665739422,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05063274,
                "rss_peak_bytes": 1268318208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.573,
                "predicted_n": 25,
                "predicted_per_second": 95.78047116010104,
                "predicted_per_token_ms": 10.440541666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273983587,
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
          "gpu_j_per_correct_token": 26.629114236121566,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 670109696,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7625.710602858931,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.062398472,
              "rss_peak_bytes": 11901853696,
              "swap_peak_bytes": 189534208
            },
            {
              "anon_peak_bytes": 772743168,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7180.076912424661,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.08200338,
              "rss_peak_bytes": 12139950080,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14805.787515283591,
          "raw_requests": [
            {
              "begin_ns": 295510955231671,
              "complete": true,
              "e2e_s": 0.516981229,
              "end_ns": 295511472212900,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 619847680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 112.88749362063564,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052927355,
                "rss_peak_bytes": 1218052096,
                "swap_peak_bytes": 149315584
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 271.914,
                "predicted_n": 10,
                "predicted_per_second": 33.098700324367265,
                "predicted_per_token_ms": 30.212666666666664
              },
              "ttft_s": 0.239309698,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295511535190214,
              "complete": true,
              "e2e_s": 0.600511193,
              "end_ns": 295512135701407,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464199680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 147.5258209226498,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053453611,
                "rss_peak_bytes": 1062535168,
                "swap_peak_bytes": 148123648
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 373.145,
                "predicted_n": 14,
                "predicted_per_second": 34.83900360449692,
                "predicted_per_token_ms": 28.703461538461536
              },
              "ttft_s": 0.225171961,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295512204876470,
              "complete": true,
              "e2e_s": 1.813798211,
              "end_ns": 295514018674681,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 465096704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 475.12549434091505,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.056076998,
                "rss_peak_bytes": 1063604224,
                "swap_peak_bytes": 147361792
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1254.841,
                "predicted_n": 45,
                "predicted_per_second": 35.064203353253525,
                "predicted_per_token_ms": 28.519113636363635
              },
              "ttft_s": 0.553891674,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 295514086084142,
              "complete": true,
              "e2e_s": 1.036705369,
              "end_ns": 295515122789511,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469192704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 262.5715353956071,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052678505,
                "rss_peak_bytes": 1068208128,
                "swap_peak_bytes": 146092032
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 770.162,
                "predicted_n": 28,
                "predicted_per_second": 35.05755931868879,
                "predicted_per_token_ms": 28.52451851851852
              },
              "ttft_s": 0.262294521,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 295515190611556,
              "complete": true,
              "e2e_s": 0.881820745,
              "end_ns": 295516072432301,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469917696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.79728970340258,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052184665,
                "rss_peak_bytes": 1068998656,
                "swap_peak_bytes": 145342464
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 626.35,
                "predicted_n": 23,
                "predicted_per_second": 35.12413187514967,
                "predicted_per_token_ms": 28.470454545454547
              },
              "ttft_s": 0.249852708,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 295516134303659,
              "complete": true,
              "e2e_s": 1.183953211,
              "end_ns": 295517318256870,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 627580928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 293.55900438947,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053462171,
                "rss_peak_bytes": 1226727424,
                "swap_peak_bytes": 144605184
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.907,
                "predicted_n": 29,
                "predicted_per_second": 35.313094726115416,
                "predicted_per_token_ms": 28.318107142857144
              },
              "ttft_s": 0.383996873,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295517380184315,
              "complete": true,
              "e2e_s": 3.794631326,
              "end_ns": 295521174815641,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628678656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1013.2276608888805,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056223654,
                "rss_peak_bytes": 1227825152,
                "swap_peak_bytes": 144498688
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 589.029,
                "predicted_n": 21,
                "predicted_per_second": 33.95418561734652,
                "predicted_per_token_ms": 29.45145
              },
              "ttft_s": 3.202258953,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295521235556099,
              "complete": true,
              "e2e_s": 0.718703204,
              "end_ns": 295521954259303,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 471875584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 191.22736007427912,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055339521,
                "rss_peak_bytes": 1071022080,
                "swap_peak_bytes": 143896576
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
              "ttft_s": 0.718571547
            },
            {
              "begin_ns": 295522008538837,
              "complete": true,
              "e2e_s": 3.777156553,
              "end_ns": 295525785695390,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 471887872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1032.7026774966453,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053207554,
                "rss_peak_bytes": 1071034368,
                "swap_peak_bytes": 143892480
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.734,
                "predicted_n": 128,
                "predicted_per_second": 35.45768613749654,
                "predicted_per_token_ms": 28.20262992125984
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195319899
            },
            {
              "begin_ns": 295525854090822,
              "complete": true,
              "e2e_s": 1.706133364,
              "end_ns": 295527560224186,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628817920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 452.20409498256913,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054113299,
                "rss_peak_bytes": 1227964416,
                "swap_peak_bytes": 143880192
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 942.067,
                "predicted_n": 34,
                "predicted_per_second": 35.029355661539995,
                "predicted_per_token_ms": 28.54748484848485
              },
              "tool_call_valid": true,
              "ttft_s": 1.028414228,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295527630760640,
              "complete": true,
              "e2e_s": 1.776275518,
              "end_ns": 295529407036158,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 628846592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 455.36044261621083,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052504326,
                "rss_peak_bytes": 1227993088,
                "swap_peak_bytes": 143872000
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.196,
                "predicted_n": 25,
                "predicted_per_second": 35.12901129397713,
                "predicted_per_token_ms": 28.4665
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093031669,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295675061874736,
              "complete": true,
              "e2e_s": 0.467341763,
              "end_ns": 295675529216499,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612290560,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.49910664426555,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052124435,
                "rss_peak_bytes": 1257115648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.739,
                "predicted_n": 10,
                "predicted_per_second": 34.25452635505198,
                "predicted_per_token_ms": 29.193222222222218
              },
              "ttft_s": 0.204599813,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295675602162448,
              "complete": true,
              "e2e_s": 0.574452079,
              "end_ns": 295676176614527,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612290560,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 148.5998023639688,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053470912,
                "rss_peak_bytes": 1257115648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 372.388,
                "predicted_n": 14,
                "predicted_per_second": 34.90982523604413,
                "predicted_per_token_ms": 28.645230769230768
              },
              "ttft_s": 0.202089185,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295676256054680,
              "complete": true,
              "e2e_s": 1.761462126,
              "end_ns": 295678017516806,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612290560,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 474.0352621882316,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.08200338,
                "rss_peak_bytes": 1257115648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.529,
                "predicted_n": 45,
                "predicted_per_second": 35.44017095049733,
                "predicted_per_token_ms": 28.216568181818182
              },
              "ttft_s": 0.519920178,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 295678089307033,
              "complete": true,
              "e2e_s": 0.987723209,
              "end_ns": 295679077030242,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 264.2103186721006,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05219013,
                "rss_peak_bytes": 1260417024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.011,
                "predicted_n": 28,
                "predicted_per_second": 35.339805316939156,
                "predicted_per_token_ms": 28.296703703703702
              },
              "ttft_s": 0.223636308,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 295679145057338,
              "complete": true,
              "e2e_s": 0.844560097,
              "end_ns": 295679989617435,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 226.27967526465036,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053375741,
                "rss_peak_bytes": 1260417024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.133,
                "predicted_n": 23,
                "predicted_per_second": 35.305464483505126,
                "predicted_per_token_ms": 28.324227272727274
              },
              "ttft_s": 0.221397736,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 295680060335485,
              "complete": true,
              "e2e_s": 1.144263994,
              "end_ns": 295681204599479,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772198400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 295.34197516818267,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050881568,
                "rss_peak_bytes": 1417347072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.385,
                "predicted_n": 29,
                "predicted_per_second": 35.336357957306106,
                "predicted_per_token_ms": 28.299464285714286
              },
              "ttft_s": 0.351897856,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295681276358521,
              "complete": true,
              "e2e_s": 3.782269903,
              "end_ns": 295685058628424,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772657152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1017.6505190760764,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056117727,
                "rss_peak_bytes": 1417805824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.718,
                "predicted_n": 21,
                "predicted_per_second": 34.44012412220734,
                "predicted_per_token_ms": 29.035899999999998
              },
              "ttft_s": 3.201452874,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295685127027371,
              "complete": true,
              "e2e_s": 0.722378856,
              "end_ns": 295685849406227,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 653533184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 192.40966394546098,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051391006,
                "rss_peak_bytes": 1298681856,
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
              "ttft_s": 0.722245119
            },
            {
              "begin_ns": 295685909208925,
              "complete": true,
              "e2e_s": 3.777768813,
              "end_ns": 295689686977738,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615784448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1060.7749420575885,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053185311,
                "rss_peak_bytes": 1260933120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.145,
                "predicted_n": 128,
                "predicted_per_second": 35.463517953056915,
                "predicted_per_token_ms": 28.197992125984253
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196564164
            },
            {
              "begin_ns": 295689756330663,
              "complete": true,
              "e2e_s": 1.700323958,
              "end_ns": 295691456654621,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772706304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 459.1492462420445,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054015173,
                "rss_peak_bytes": 1417854976,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.81,
                "predicted_n": 34,
                "predicted_per_second": 35.18836438084474,
                "predicted_per_token_ms": 28.418484848484848
              },
              "tool_call_valid": true,
              "ttft_s": 1.025405034,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295691534962113,
              "complete": true,
              "e2e_s": 1.773032366,
              "end_ns": 295693307994479,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772743168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 463.4596781800773,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052657535,
                "rss_peak_bytes": 1417891840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.691,
                "predicted_n": 25,
                "predicted_per_second": 35.206567198334724,
                "predicted_per_token_ms": 28.403791666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 1.09130815,
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
          "gpu_j_per_correct_token": 25.579341338916926,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772710400,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7081.126990506355,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.07810118,
              "rss_peak_bytes": 12139950080,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772698112,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7140.986793931456,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.083929844,
              "rss_peak_bytes": 12139864064,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14222.11378443781,
          "raw_requests": [
            {
              "begin_ns": 295566231503369,
              "complete": true,
              "e2e_s": 0.465481248,
              "end_ns": 295566696984617,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 769175552,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 108.39040921743718,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050964133,
                "rss_peak_bytes": 1413996544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 264.094,
                "predicted_n": 10,
                "predicted_per_second": 34.07877498163533,
                "predicted_per_token_ms": 29.343777777777778
              },
              "ttft_s": 0.201342513,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295566762303412,
              "complete": true,
              "e2e_s": 0.574132171,
              "end_ns": 295567336435583,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612278272,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 141.48549511362964,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051952139,
                "rss_peak_bytes": 1257099264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 372.401,
                "predicted_n": 14,
                "predicted_per_second": 34.90860658268909,
                "predicted_per_token_ms": 28.64623076923077
              },
              "ttft_s": 0.201628524,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295567405099484,
              "complete": true,
              "e2e_s": 1.762240128,
              "end_ns": 295569167339612,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612278272,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 467.84399189429786,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050978883,
                "rss_peak_bytes": 1257099264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.456,
                "predicted_n": 45,
                "predicted_per_second": 35.41372893687986,
                "predicted_per_token_ms": 28.237636363636362
              },
              "ttft_s": 0.519795055,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 295569244120694,
              "complete": true,
              "e2e_s": 0.988595873,
              "end_ns": 295570232716567,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 260.08927927493403,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050599742,
                "rss_peak_bytes": 1260400640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.959,
                "predicted_n": 28,
                "predicted_per_second": 35.29600932860454,
                "predicted_per_token_ms": 28.331814814814813
              },
              "ttft_s": 0.223640997,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 295570308108606,
              "complete": true,
              "e2e_s": 0.844201747,
              "end_ns": 295571152310353,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615256064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.290116503546,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052514287,
                "rss_peak_bytes": 1260400640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.291,
                "predicted_n": 23,
                "predicted_per_second": 35.29651479004189,
                "predicted_per_token_ms": 28.331409090909094
              },
              "ttft_s": 0.220924073,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 295571228060586,
              "complete": true,
              "e2e_s": 1.144964238,
              "end_ns": 295572373024824,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772169728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 285.55944243180045,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052224108,
                "rss_peak_bytes": 1417314304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.534,
                "predicted_n": 29,
                "predicted_per_second": 35.329714561141856,
                "predicted_per_token_ms": 28.304785714285714
              },
              "ttft_s": 0.352407217,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295572463700623,
              "complete": true,
              "e2e_s": 3.777894826,
              "end_ns": 295576241595449,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772628480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1009.7979669345053,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055232331,
                "rss_peak_bytes": 1417773056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.767,
                "predicted_n": 21,
                "predicted_per_second": 34.43721836812353,
                "predicted_per_token_ms": 29.03835
              },
              "ttft_s": 3.197021777,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295576330961661,
              "complete": true,
              "e2e_s": 0.71962499,
              "end_ns": 295577050586651,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 726908928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 188.11737279491274,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055419912,
                "rss_peak_bytes": 1372053504,
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
              "ttft_s": 0.719499146
            },
            {
              "begin_ns": 295577147798998,
              "complete": true,
              "e2e_s": 3.770085886,
              "end_ns": 295580917884884,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615759872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1047.1767174056718,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.061597704,
                "rss_peak_bytes": 1260904448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3576.138,
                "predicted_n": 128,
                "predicted_per_second": 35.5131709123082,
                "predicted_per_token_ms": 28.15856692913386
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.19386793
            },
            {
              "begin_ns": 295581025333655,
              "complete": true,
              "e2e_s": 1.70952885,
              "end_ns": 295582734862505,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772669440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 451.3247464623035,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055401887,
                "rss_peak_bytes": 1417814016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 946.054,
                "predicted_n": 34,
                "predicted_per_second": 34.88172979555078,
                "predicted_per_token_ms": 28.66830303030303
              },
              "tool_call_valid": true,
              "ttft_s": 1.027654801,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295582856559603,
              "complete": true,
              "e2e_s": 1.776596632,
              "end_ns": 295584633156235,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772710400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 456.6975242093379,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053456218,
                "rss_peak_bytes": 1417854976,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.153,
                "predicted_n": 25,
                "predicted_per_second": 35.131222434798644,
                "predicted_per_token_ms": 28.464708333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093468331,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295620799870217,
              "complete": true,
              "e2e_s": 0.464579305,
              "end_ns": 295621264449522,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612253696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 108.48257554914693,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050765588,
                "rss_peak_bytes": 1257013248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.771,
                "predicted_n": 10,
                "predicted_per_second": 34.12050604501632,
                "predicted_per_token_ms": 29.30788888888889
              },
              "ttft_s": 0.200702277,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295621331498052,
              "complete": true,
              "e2e_s": 0.573874356,
              "end_ns": 295621905372408,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612253696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.07327846542847,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050670759,
                "rss_peak_bytes": 1257013248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.465,
                "predicted_n": 14,
                "predicted_per_second": 34.99656764432719,
                "predicted_per_token_ms": 28.574230769230766
              },
              "ttft_s": 0.202329308,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295621974601252,
              "complete": true,
              "e2e_s": 1.76138322,
              "end_ns": 295623735984472,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612253696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 474.54716655280566,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.056579898,
                "rss_peak_bytes": 1257013248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.334,
                "predicted_n": 45,
                "predicted_per_second": 35.44573821388925,
                "predicted_per_token_ms": 28.212136363636365
              },
              "ttft_s": 0.520028462,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 295623808789794,
              "complete": true,
              "e2e_s": 0.988225328,
              "end_ns": 295624797015122,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615231488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 258.590048755902,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050759074,
                "rss_peak_bytes": 1260314624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.487,
                "predicted_n": 28,
                "predicted_per_second": 35.271663659866206,
                "predicted_per_token_ms": 28.35137037037037
              },
              "ttft_s": 0.222713469,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 295624867127535,
              "complete": true,
              "e2e_s": 0.848044208,
              "end_ns": 295625715171743,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615231488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 218.68653353972425,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053807417,
                "rss_peak_bytes": 1260314624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.251,
                "predicted_n": 23,
                "predicted_per_second": 35.29878010624933,
                "predicted_per_token_ms": 28.329590909090907
              },
              "ttft_s": 0.224756887,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 295625793286441,
              "complete": true,
              "e2e_s": 1.146029951,
              "end_ns": 295626939316392,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772145152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 294.80335728209224,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052303436,
                "rss_peak_bytes": 1417228288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 790.702,
                "predicted_n": 29,
                "predicted_per_second": 35.411570983758736,
                "predicted_per_token_ms": 28.23935714285714
              },
              "ttft_s": 0.35527643,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295627005273488,
              "complete": true,
              "e2e_s": 3.780962566,
              "end_ns": 295630786236054,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772612096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1019.235567539057,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.066160903,
                "rss_peak_bytes": 1417695232,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.519,
                "predicted_n": 21,
                "predicted_per_second": 34.511379264527996,
                "predicted_per_token_ms": 28.97595
              },
              "ttft_s": 3.201373598,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295630877877094,
              "complete": true,
              "e2e_s": 0.720373277,
              "end_ns": 295631598250371,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 653721600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 190.46795982384918,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05156938,
                "rss_peak_bytes": 1298804736,
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
              "ttft_s": 0.720165983
            },
            {
              "begin_ns": 295631655651230,
              "complete": true,
              "e2e_s": 3.772368795,
              "end_ns": 295635428020025,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615747584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1056.8603781659772,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054185815,
                "rss_peak_bytes": 1260830720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3577.393,
                "predicted_n": 128,
                "predicted_per_second": 35.50071239027974,
                "predicted_per_token_ms": 28.168448818897637
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194869444
            },
            {
              "begin_ns": 295635495316616,
              "complete": true,
              "e2e_s": 1.704513535,
              "end_ns": 295637199830151,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772661248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.85916420828505,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053430932,
                "rss_peak_bytes": 1417744384,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.309,
                "predicted_n": 34,
                "predicted_per_second": 35.09484648131625,
                "predicted_per_token_ms": 28.49421212121212
              },
              "tool_call_valid": true,
              "ttft_s": 1.027938898,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295637277071084,
              "complete": true,
              "e2e_s": 1.771788124,
              "end_ns": 295639048859208,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772698112,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 464.86595755655395,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052430808,
                "rss_peak_bytes": 1417781248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.455,
                "predicted_n": 25,
                "predicted_per_second": 35.21875985941845,
                "predicted_per_token_ms": 28.393958333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 1.090270353,
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
