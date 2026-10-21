# Public audit excerpt

Original SHA256: `0cb596914b9fccbb3caa10511943e2acbd46e2887ab60e4251976de77ed45b49`

Original file: `RESULTS.json`; 266400 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.554098469830357,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470315008,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2663.1172298278834,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.239227078,
              "rss_peak_bytes": 7727448064,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470327296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2706.2861102167776,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.063765426,
              "rss_peak_bytes": 7726342144,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5369.403340044661,
          "raw_requests": [
            {
              "begin_ns": 290762235579253,
              "complete": true,
              "e2e_s": 0.181459446,
              "end_ns": 290762417038699,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414056448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.29473181247796,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051478177,
                "rss_peak_bytes": 1472135168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.726,
                "predicted_n": 10,
                "predicted_per_second": 77.76990477507216,
                "predicted_per_token_ms": 12.858444444444444
              },
              "ttft_s": 0.065702976,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290762469653148,
              "complete": true,
              "e2e_s": 0.23376769,
              "end_ns": 290762703420838,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414056448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 50.819918240763116,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050971024,
                "rss_peak_bytes": 1472135168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.736,
                "predicted_n": 14,
                "predicted_per_second": 78.4379977796013,
                "predicted_per_token_ms": 12.748923076923075
              },
              "ttft_s": 0.068001474,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 290762757229700,
              "complete": true,
              "e2e_s": 0.664808057,
              "end_ns": 290763422037757,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414056448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 174.6732201522666,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050794236,
                "rss_peak_bytes": 1472180224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.555,
                "predicted_n": 44,
                "predicted_per_second": 79.40098420289722,
                "predicted_per_token_ms": 12.594302325581394
              },
              "ttft_s": 0.123244798,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 290763476063551,
              "complete": true,
              "e2e_s": 0.3574598,
              "end_ns": 290763833523351,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 90.24054803133615,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050464837,
                "rss_peak_bytes": 1472184320,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.462,
                "predicted_n": 23,
                "predicted_per_second": 79.00539391371174,
                "predicted_per_token_ms": 12.657363636363636
              },
              "ttft_s": 0.079011255,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 290763885902546,
              "complete": true,
              "e2e_s": 0.294811747,
              "end_ns": 290764180714293,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414064640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 75.2010461289861,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050669458,
                "rss_peak_bytes": 1472188416,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.17,
                "predicted_n": 18,
                "predicted_per_second": 78.64180968682055,
                "predicted_per_token_ms": 12.715882352941176
              },
              "ttft_s": 0.078608685,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 290764239788831,
              "complete": true,
              "e2e_s": 0.468185333,
              "end_ns": 290764707974164,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469762048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.53352262331961,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050460234,
                "rss_peak_bytes": 1527885824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.825,
                "predicted_n": 29,
                "predicted_per_second": 79.13516568925317,
                "predicted_per_token_ms": 12.636607142857143
              },
              "ttft_s": 0.114338255,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290764763841502,
              "complete": true,
              "e2e_s": 1.07555086,
              "end_ns": 290765839392362,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470233088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 287.06048763333206,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056111228,
                "rss_peak_bytes": 1528356864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 255.901,
                "predicted_n": 21,
                "predicted_per_second": 78.15522409056628,
                "predicted_per_token_ms": 12.79505
              },
              "ttft_s": 0.819573608,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 290765892924404,
              "complete": true,
              "e2e_s": 0.201308732,
              "end_ns": 290766094233136,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.52504119317897,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054115161,
                "rss_peak_bytes": 1475686400,
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
              "ttft_s": 0.201164532
            },
            {
              "begin_ns": 290766163764787,
              "complete": true,
              "e2e_s": 1.662408816,
              "end_ns": 290767826173603,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 447.50799950274137,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050955899,
                "rss_peak_bytes": 1475686400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1596.321,
                "predicted_n": 128,
                "predicted_per_second": 79.55793352339536,
                "predicted_per_token_ms": 12.569456692913386
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.065807777
            },
            {
              "begin_ns": 290767887708116,
              "complete": true,
              "e2e_s": 0.618973019,
              "end_ns": 290768506681135,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470286336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 153.54251460806708,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056004398,
                "rss_peak_bytes": 1528401920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.013,
                "predicted_n": 34,
                "predicted_per_second": 78.94491319647953,
                "predicted_per_token_ms": 12.667060606060605
              },
              "tool_call_valid": true,
              "ttft_s": 0.317265775,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290768568845878,
              "complete": true,
              "e2e_s": 0.557690385,
              "end_ns": 290769126536263,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470315008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 142.68207388543695,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050532762,
                "rss_peak_bytes": 1528430592,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.774,
                "predicted_n": 25,
                "predicted_per_second": 78.74687473340902,
                "predicted_per_token_ms": 12.698916666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.252890224,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291218378387272,
              "complete": true,
              "e2e_s": 0.183434438,
              "end_ns": 291218561821710,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 38.597321728317596,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056984493,
                "rss_peak_bytes": 1469845504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.226,
                "predicted_n": 10,
                "predicted_per_second": 77.43534148985596,
                "predicted_per_token_ms": 12.914
              },
              "ttft_s": 0.067215261,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291218641117042,
              "complete": true,
              "e2e_s": 0.233192011,
              "end_ns": 291218874309053,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 58.42157635692884,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05022603,
                "rss_peak_bytes": 1469845504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.853,
                "predicted_n": 14,
                "predicted_per_second": 78.38266416646066,
                "predicted_per_token_ms": 12.757923076923078
              },
              "ttft_s": 0.067307219,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 291218962138735,
              "complete": true,
              "e2e_s": 0.66682185,
              "end_ns": 291219628960585,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 173.6550474454855,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051321714,
                "rss_peak_bytes": 1469890560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.87,
                "predicted_n": 44,
                "predicted_per_second": 79.20865032143975,
                "predicted_per_token_ms": 12.624883720930233
              },
              "ttft_s": 0.123948351,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 291219706236120,
              "complete": true,
              "e2e_s": 0.357740799,
              "end_ns": 291220063976919,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 86.84444949121318,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056891241,
                "rss_peak_bytes": 1469894656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.924,
                "predicted_n": 23,
                "predicted_per_second": 78.87453213061623,
                "predicted_per_token_ms": 12.678363636363635
              },
              "ttft_s": 0.078757937,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 291220142887683,
              "complete": true,
              "e2e_s": 0.295348379,
              "end_ns": 291220438236062,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.49296735528861,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051620996,
                "rss_peak_bytes": 1469894656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.455,
                "predicted_n": 18,
                "predicted_per_second": 78.53826430435888,
                "predicted_per_token_ms": 12.732647058823531
              },
              "ttft_s": 0.078840921,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 291220515080762,
              "complete": true,
              "e2e_s": 0.469681693,
              "end_ns": 291220984762455,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469770240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 113.537918634993,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052169806,
                "rss_peak_bytes": 1525587968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.11,
                "predicted_n": 29,
                "predicted_per_second": 79.07147496540622,
                "predicted_per_token_ms": 12.646785714285715
              },
              "ttft_s": 0.115507979,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291221062777848,
              "complete": true,
              "e2e_s": 1.080560577,
              "end_ns": 291222143338425,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 289.07561511419414,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055163844,
                "rss_peak_bytes": 1526059008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.765,
                "predicted_n": 21,
                "predicted_per_second": 77.8922360913676,
                "predicted_per_token_ms": 12.838249999999999
              },
              "ttft_s": 0.823696376,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 291222228902706,
              "complete": true,
              "e2e_s": 0.1977194,
              "end_ns": 291222426622106,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.585819927007705,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051014039,
                "rss_peak_bytes": 1473396736,
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
              "ttft_s": 0.197562003
            },
            {
              "begin_ns": 291222495247830,
              "complete": true,
              "e2e_s": 1.658941923,
              "end_ns": 291224154189753,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 451.17503609924097,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050183541,
                "rss_peak_bytes": 1473396736,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.066,
                "predicted_n": 128,
                "predicted_per_second": 79.62052980879787,
                "predicted_per_token_ms": 12.559574803149607
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063731293
            },
            {
              "begin_ns": 291224233240601,
              "complete": true,
              "e2e_s": 0.630418592,
              "end_ns": 291224863659193,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470298624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.70969753128406,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054195562,
                "rss_peak_bytes": 1526116352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 428.674,
                "predicted_n": 34,
                "predicted_per_second": 76.98157574287221,
                "predicted_per_token_ms": 12.990121212121212
              },
              "tool_call_valid": true,
              "ttft_s": 0.319368404,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291225005711208,
              "complete": true,
              "e2e_s": 0.560301706,
              "end_ns": 291225566012914,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 147.94001388610118,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055503816,
                "rss_peak_bytes": 1526145024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 305.084,
                "predicted_n": 25,
                "predicted_per_second": 78.66685896343303,
                "predicted_per_token_ms": 12.711833333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255191518,
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
          "gpu_j_per_correct_token": 10.226999072730408,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470261760,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2664.7996632696463,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.05407519,
              "rss_peak_bytes": 7727403008,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 369598464,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 3082.773815604843,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.096515978,
              "rss_peak_bytes": 7429197824,
              "swap_peak_bytes": 182157312
            }
          ],
          "lifecycle_gpu_j": 5747.573478874489,
          "raw_requests": [
            {
              "begin_ns": 290791127146432,
              "complete": true,
              "e2e_s": 0.182685127,
              "end_ns": 290791309831559,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414035968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 36.41974187398392,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052130434,
                "rss_peak_bytes": 1472053248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.229,
                "predicted_n": 10,
                "predicted_per_second": 77.43334279740856,
                "predicted_per_token_ms": 12.914333333333333
              },
              "ttft_s": 0.066421402,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290791370158338,
              "complete": true,
              "e2e_s": 0.233506504,
              "end_ns": 290791603664842,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414035968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 50.42475248836702,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050073025,
                "rss_peak_bytes": 1472053248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.441,
                "predicted_n": 14,
                "predicted_per_second": 78.1057551925307,
                "predicted_per_token_ms": 12.803153846153846
              },
              "ttft_s": 0.067038039,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 290791659797261,
              "complete": true,
              "e2e_s": 0.665348508,
              "end_ns": 290792325145769,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414035968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 176.35438088407267,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05080743,
                "rss_peak_bytes": 1472098304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.876,
                "predicted_n": 44,
                "predicted_per_second": 79.35394813573585,
                "predicted_per_token_ms": 12.601767441860465
              },
              "ttft_s": 0.123487452,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 290792383180461,
              "complete": true,
              "e2e_s": 0.357540246,
              "end_ns": 290792740720707,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.15847827119995,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050050533,
                "rss_peak_bytes": 1472102400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.128,
                "predicted_n": 23,
                "predicted_per_second": 78.81688687627182,
                "predicted_per_token_ms": 12.687636363636363
              },
              "ttft_s": 0.078393015,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 290792795159118,
              "complete": true,
              "e2e_s": 0.294887473,
              "end_ns": 290793090046591,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414044160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.22575124752173,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050957449,
                "rss_peak_bytes": 1472106496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.304,
                "predicted_n": 18,
                "predicted_per_second": 78.59309120497079,
                "predicted_per_token_ms": 12.723764705882353
              },
              "ttft_s": 0.078499087,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 290793146170250,
              "complete": true,
              "e2e_s": 0.46892793,
              "end_ns": 290793615098180,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469737472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.7658092224785,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050307561,
                "rss_peak_bytes": 1527799808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.228,
                "predicted_n": 29,
                "predicted_per_second": 79.04513477195479,
                "predicted_per_token_ms": 12.651
              },
              "ttft_s": 0.114678807,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290793676063970,
              "complete": true,
              "e2e_s": 1.075063339,
              "end_ns": 290794751127309,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470163456,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 286.49938844907354,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053751436,
                "rss_peak_bytes": 1528225792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.317,
                "predicted_n": 21,
                "predicted_per_second": 78.02837892141372,
                "predicted_per_token_ms": 12.815850000000001
              },
              "ttft_s": 0.818777429,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 290794816740074,
              "complete": true,
              "e2e_s": 0.197365458,
              "end_ns": 290795014105532,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417501184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.52797710676359,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053610436,
                "rss_peak_bytes": 1475563520,
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
              "ttft_s": 0.197201288
            },
            {
              "begin_ns": 290795083275295,
              "complete": true,
              "e2e_s": 1.658637193,
              "end_ns": 290796741912488,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417501184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 442.7522621840771,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050700631,
                "rss_peak_bytes": 1475563520,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.795,
                "predicted_n": 128,
                "predicted_per_second": 79.58415711291238,
                "predicted_per_token_ms": 12.565314960629921
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062762478
            },
            {
              "begin_ns": 290796797347416,
              "complete": true,
              "e2e_s": 0.619189505,
              "end_ns": 290797416536921,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470216704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 161.38426039295936,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05134684,
                "rss_peak_bytes": 1528279040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.117,
                "predicted_n": 34,
                "predicted_per_second": 78.92527689617977,
                "predicted_per_token_ms": 12.670212121212122
              },
              "tool_call_valid": true,
              "ttft_s": 0.317291797,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290797475346502,
              "complete": true,
              "e2e_s": 0.559591246,
              "end_ns": 290798034937748,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 144.12548463696533,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053899635,
                "rss_peak_bytes": 1528324096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.486,
                "predicted_n": 25,
                "predicted_per_second": 78.82135796062873,
                "predicted_per_token_ms": 12.686916666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255074785,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291188246111148,
              "complete": true,
              "e2e_s": 0.224113164,
              "end_ns": 291188470224312,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 279580672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 40.24600075997657,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051467304,
                "rss_peak_bytes": 1223860224,
                "swap_peak_bytes": 147529728
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 123.922,
                "predicted_n": 10,
                "predicted_per_second": 72.62632946530881,
                "predicted_per_token_ms": 13.76911111111111
              },
              "ttft_s": 0.093983789,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291188551212602,
              "complete": true,
              "e2e_s": 0.266239352,
              "end_ns": 291188817451954,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 267055104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 54.567402901994456,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054809092,
                "rss_peak_bytes": 1211531264,
                "swap_peak_bytes": 147009536
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 167.408,
                "predicted_n": 14,
                "predicted_per_second": 77.65459237312434,
                "predicted_per_token_ms": 12.87753846153846
              },
              "ttft_s": 0.089688727,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 291188959098181,
              "complete": true,
              "e2e_s": 0.711744906,
              "end_ns": 291189670843087,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 267960320,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 181.6454749228452,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050738471,
                "rss_peak_bytes": 1212874752,
                "swap_peak_bytes": 146497536
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 552.14,
                "predicted_n": 44,
                "predicted_per_second": 77.87879885536277,
                "predicted_per_token_ms": 12.84046511627907
              },
              "ttft_s": 0.149631703,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 291189748610796,
              "complete": true,
              "e2e_s": 0.406365153,
              "end_ns": 291190154975949,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 269045760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 97.01198662895303,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050294241,
                "rss_peak_bytes": 1209044992,
                "swap_peak_bytes": 145342464
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 284.383,
                "predicted_n": 23,
                "predicted_per_second": 77.36046106834797,
                "predicted_per_token_ms": 12.926499999999999
              },
              "ttft_s": 0.114199821,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 291190233211210,
              "complete": true,
              "e2e_s": 0.336589381,
              "end_ns": 291190569800591,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 269770752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.61389209201104,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051301958,
                "rss_peak_bytes": 1209901056,
                "swap_peak_bytes": 144306176
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 221.504,
                "predicted_n": 18,
                "predicted_per_second": 76.74804969661949,
                "predicted_per_token_ms": 13.029647058823528
              },
              "ttft_s": 0.108445191,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 291190649831507,
              "complete": true,
              "e2e_s": 0.509828234,
              "end_ns": 291191159659741,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 326160384,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 121.58933499536883,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050956801,
                "rss_peak_bytes": 1266552832,
                "swap_peak_bytes": 143720448
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 358.684,
                "predicted_n": 29,
                "predicted_per_second": 78.0631419299439,
                "predicted_per_token_ms": 12.810142857142859
              },
              "ttft_s": 0.145027251,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291191235147638,
              "complete": true,
              "e2e_s": 1.101312844,
              "end_ns": 291192336460482,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 327020544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 285.91470927515945,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058784404,
                "rss_peak_bytes": 1267412992,
                "swap_peak_bytes": 143179776
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 260.538,
                "predicted_n": 21,
                "predicted_per_second": 76.76423400809095,
                "predicted_per_token_ms": 13.026900000000001
              },
              "ttft_s": 0.835991689,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 291192417309152,
              "complete": true,
              "e2e_s": 0.198728534,
              "end_ns": 291192616037686,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 274415616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.73807612923016,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058427996,
                "rss_peak_bytes": 1214808064,
                "swap_peak_bytes": 143101952
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
              "ttft_s": 0.198587779
            },
            {
              "begin_ns": 291192683298413,
              "complete": true,
              "e2e_s": 1.659160837,
              "end_ns": 291194342459250,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 274432000,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 449.5292464913189,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050830865,
                "rss_peak_bytes": 1214824448,
                "swap_peak_bytes": 143093760
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.774,
                "predicted_n": 128,
                "predicted_per_second": 79.63510817206702,
                "predicted_per_token_ms": 12.55727559055118
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063265605
            },
            {
              "begin_ns": 291194414771538,
              "complete": true,
              "e2e_s": 0.620051723,
              "end_ns": 291195034823261,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 327147520,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 159.0646498795833,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055726538,
                "rss_peak_bytes": 1267539968,
                "swap_peak_bytes": 143081472
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.175,
                "predicted_n": 34,
                "predicted_per_second": 79.10349373764008,
                "predicted_per_token_ms": 12.641666666666667
              },
              "tool_call_valid": true,
              "ttft_s": 0.319102948,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291195118948508,
              "complete": true,
              "e2e_s": 0.559658178,
              "end_ns": 291195678606686,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 327188480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 144.87206104189588,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053499988,
                "rss_peak_bytes": 1267580928,
                "swap_peak_bytes": 143077376
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.538,
                "predicted_n": 25,
                "predicted_per_second": 78.80789917842765,
                "predicted_per_token_ms": 12.689083333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254791708,
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
          "gpu_j_per_correct_token": 9.152442224933036,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476037120,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2246.984630599701,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.076735408,
              "rss_peak_bytes": 5997289472,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 372629504,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2713.6390553140045,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.100428329,
              "rss_peak_bytes": 5419057152,
              "swap_peak_bytes": 194535424
            }
          ],
          "lifecycle_gpu_j": 4960.623685913706,
          "raw_requests": [
            {
              "begin_ns": 290840463702820,
              "complete": true,
              "e2e_s": 0.158423859,
              "end_ns": 290840622126679,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.38177054999376,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051606905,
                "rss_peak_bytes": 1216327680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.105,
                "predicted_n": 10,
                "predicted_per_second": 93.64757296706728,
                "predicted_per_token_ms": 10.678333333333335
              },
              "ttft_s": 0.06228706,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290840731756619,
              "complete": true,
              "e2e_s": 0.148950484,
              "end_ns": 290840880707103,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.60358157732636,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050748369,
                "rss_peak_bytes": 1216327680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.527,
                "predicted_n": 9,
                "predicted_per_second": 93.53771323675565,
                "predicted_per_token_ms": 10.690875
              },
              "ttft_s": 0.063413874,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 290840941680020,
              "complete": true,
              "e2e_s": 0.526307926,
              "end_ns": 290841467987946,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.6205406108758,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052127753,
                "rss_peak_bytes": 1216372736,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.153,
                "predicted_n": 39,
                "predicted_per_second": 96.4092623930301,
                "predicted_per_token_ms": 10.372447368421053
              },
              "ttft_s": 0.132112279,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 290841527574591,
              "complete": true,
              "e2e_s": 0.306433589,
              "end_ns": 290841834008180,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.97786914272217,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050963169,
                "rss_peak_bytes": 1219403776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.24,
                "predicted_n": 23,
                "predicted_per_second": 95.96928982725528,
                "predicted_per_token_ms": 10.42
              },
              "ttft_s": 0.077146594,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 290841894564090,
              "complete": true,
              "e2e_s": 0.254322142,
              "end_ns": 290842148886232,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.63956633628631,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050185761,
                "rss_peak_bytes": 1219403776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.018,
                "predicted_n": 18,
                "predicted_per_second": 95.49596108258716,
                "predicted_per_token_ms": 10.47164705882353
              },
              "ttft_s": 0.076279884,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 290842218105733,
              "complete": true,
              "e2e_s": 0.398534106,
              "end_ns": 290842616639839,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475496448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 89.66175479273488,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051037511,
                "rss_peak_bytes": 1272119296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.396,
                "predicted_n": 29,
                "predicted_per_second": 96.08917075045642,
                "predicted_per_token_ms": 10.407
              },
              "ttft_s": 0.107149532,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290842678117394,
              "complete": true,
              "e2e_s": 1.026358091,
              "end_ns": 290843704475485,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475959296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 273.00160620964294,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.076735408,
                "rss_peak_bytes": 1272582144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.146,
                "predicted_n": 16,
                "predicted_per_second": 94.25307579204002,
                "predicted_per_token_ms": 10.609733333333333
              },
              "ttft_s": 0.867179231,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 290843764151463,
              "complete": true,
              "e2e_s": 0.20411816,
              "end_ns": 290843968269623,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 48.24585892297619,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050829211,
                "rss_peak_bytes": 1219907584,
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
              "ttft_s": 0.203905974
            },
            {
              "begin_ns": 290844028924482,
              "complete": true,
              "e2e_s": 1.365796198,
              "end_ns": 290845394720680,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 345.7078891495308,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050878692,
                "rss_peak_bytes": 1219907584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.262,
                "predicted_n": 128,
                "predicted_per_second": 97.07535646529519,
                "predicted_per_token_ms": 10.30127559055118
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057374452
            },
            {
              "begin_ns": 290845458793755,
              "complete": true,
              "e2e_s": 0.548559481,
              "end_ns": 290846007353236,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476004352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 135.1654572015002,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052883222,
                "rss_peak_bytes": 1272627200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.722,
                "predicted_n": 34,
                "predicted_per_second": 96.28795350167192,
                "predicted_per_token_ms": 10.38551515151515
              },
              "tool_call_valid": true,
              "ttft_s": 0.301818152,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290846103249701,
              "complete": true,
              "e2e_s": 0.523301673,
              "end_ns": 290846626551374,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476037120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.59813200153474,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050456982,
                "rss_peak_bytes": 1272659968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 251.052,
                "predicted_n": 25,
                "predicted_per_second": 95.59772477415038,
                "predicted_per_token_ms": 10.4605
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272333479,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291120993712271,
              "complete": true,
              "e2e_s": 0.207055036,
              "end_ns": 291121200767307,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264933376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 35.509517763139826,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050446845,
                "rss_peak_bytes": 686141440,
                "swap_peak_bytes": 154910720
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 99.331,
                "predicted_n": 10,
                "predicted_per_second": 90.60615517814176,
                "predicted_per_token_ms": 11.036777777777779
              },
              "ttft_s": 0.09612838,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291121272937862,
              "complete": true,
              "e2e_s": 0.175961922,
              "end_ns": 291121448899784,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 265457664,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 34.484721415612654,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050552422,
                "rss_peak_bytes": 686936064,
                "swap_peak_bytes": 154759168
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.508,
                "predicted_n": 9,
                "predicted_per_second": 92.47699634715865,
                "predicted_per_token_ms": 10.8135
              },
              "ttft_s": 0.084948812,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 291121518298935,
              "complete": true,
              "e2e_s": 0.575390107,
              "end_ns": 291122093689042,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 266526720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.44531372678878,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050853847,
                "rss_peak_bytes": 688742400,
                "swap_peak_bytes": 154046464
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 396.384,
                "predicted_n": 39,
                "predicted_per_second": 95.86663437474772,
                "predicted_per_token_ms": 10.431157894736842
              },
              "ttft_s": 0.168465087,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 291122174064700,
              "complete": true,
              "e2e_s": 0.346545945,
              "end_ns": 291122520610645,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 270700544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 74.13816142280248,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05146817,
                "rss_peak_bytes": 693350400,
                "swap_peak_bytes": 153137152
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 232.463,
                "predicted_n": 23,
                "predicted_per_second": 94.63871669900156,
                "predicted_per_token_ms": 10.5665
              },
              "ttft_s": 0.110343496,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 291122597061021,
              "complete": true,
              "e2e_s": 0.293322272,
              "end_ns": 291122890383293,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 271507456,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 62.94642425983094,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052010419,
                "rss_peak_bytes": 694423552,
                "swap_peak_bytes": 151298048
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 179.526,
                "predicted_n": 18,
                "predicted_per_second": 94.69380479707675,
                "predicted_per_token_ms": 10.560352941176472
              },
              "ttft_s": 0.105964266,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 291122969217747,
              "complete": true,
              "e2e_s": 0.446355201,
              "end_ns": 291123415572948,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 324980736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 99.62583639873749,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056474372,
                "rss_peak_bytes": 748244992,
                "swap_peak_bytes": 151044096
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 302.74,
                "predicted_n": 29,
                "predicted_per_second": 92.48860408271123,
                "predicted_per_token_ms": 10.812142857142858
              },
              "ttft_s": 0.137617899,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291123486788482,
              "complete": true,
              "e2e_s": 1.10138488,
              "end_ns": 291124588173362,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 325918720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 278.31073402842316,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050934855,
                "rss_peak_bytes": 749240320,
                "swap_peak_bytes": 150032384
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.243,
                "predicted_n": 16,
                "predicted_per_second": 84.15477746671678,
                "predicted_per_token_ms": 11.882866666666667
              },
              "ttft_s": 0.910375439,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 291124659842400,
              "complete": true,
              "e2e_s": 0.20773623,
              "end_ns": 291124867578630,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 273289216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 50.175254278317816,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055801273,
                "rss_peak_bytes": 696610816,
                "swap_peak_bytes": 149962752
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
              "ttft_s": 0.207598053
            },
            {
              "begin_ns": 291124927307113,
              "complete": true,
              "e2e_s": 1.368998493,
              "end_ns": 291126296305606,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 273309696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 347.96500506435723,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052787546,
                "rss_peak_bytes": 696631296,
                "swap_peak_bytes": 149950464
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1310.316,
                "predicted_n": 128,
                "predicted_per_second": 96.92318494164766,
                "predicted_per_token_ms": 10.317448818897638
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057640008
            },
            {
              "begin_ns": 291126369146541,
              "complete": true,
              "e2e_s": 0.55061361,
              "end_ns": 291126919760151,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 326029312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 135.55530233570246,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055645991,
                "rss_peak_bytes": 749350912,
                "swap_peak_bytes": 149938176
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.473,
                "predicted_n": 34,
                "predicted_per_second": 96.35796106554385,
                "predicted_per_token_ms": 10.377969696969698
              },
              "tool_call_valid": true,
              "ttft_s": 0.302692558,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291126999110740,
              "complete": true,
              "e2e_s": 0.523202714,
              "end_ns": 291127522313454,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 326066176,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.878332022333,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052691604,
                "rss_peak_bytes": 749387776,
                "swap_peak_bytes": 149934080
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.548,
                "predicted_n": 25,
                "predicted_per_second": 95.79002825805833,
                "predicted_per_token_ms": 10.4395
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272555499,
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
          "gpu_j_per_correct_token": 8.421936540249318,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475959296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2253.4766744639514,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.054808998,
              "rss_peak_bytes": 5997273088,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 475979776,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2311.2129303511783,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.058011115,
              "rss_peak_bytes": 5995483136,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4564.68960481513,
          "raw_requests": [
            {
              "begin_ns": 290816387908977,
              "complete": true,
              "e2e_s": 0.156631122,
              "end_ns": 290816544540099,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 33.61859976290532,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050059338,
                "rss_peak_bytes": 1216335872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.021,
                "predicted_n": 10,
                "predicted_per_second": 93.72949667260286,
                "predicted_per_token_ms": 10.669
              },
              "ttft_s": 0.06059074,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290816600969365,
              "complete": true,
              "e2e_s": 0.148395789,
              "end_ns": 290816749365154,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.750059849592834,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050009569,
                "rss_peak_bytes": 1216335872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.419,
                "predicted_n": 9,
                "predicted_per_second": 93.65597817815708,
                "predicted_per_token_ms": 10.677375
              },
              "ttft_s": 0.062922014,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 290816806571180,
              "complete": true,
              "e2e_s": 0.528174184,
              "end_ns": 290817334745364,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.52054988642035,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05127567,
                "rss_peak_bytes": 1216380928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.769,
                "predicted_n": 39,
                "predicted_per_second": 96.2588247810745,
                "predicted_per_token_ms": 10.388657894736843
              },
              "ttft_s": 0.133385117,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 290817392119841,
              "complete": true,
              "e2e_s": 0.307870864,
              "end_ns": 290817699990705,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422760448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.38473333595289,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050096543,
                "rss_peak_bytes": 1219416064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 230.848,
                "predicted_n": 23,
                "predicted_per_second": 95.30080399223732,
                "predicted_per_token_ms": 10.49309090909091
              },
              "ttft_s": 0.07699896,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 290817756147457,
              "complete": true,
              "e2e_s": 0.253899824,
              "end_ns": 290818010047281,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422760448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 56.59589443958032,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051069121,
                "rss_peak_bytes": 1219416064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.336,
                "predicted_n": 18,
                "predicted_per_second": 95.86322010195335,
                "predicted_per_token_ms": 10.431529411764707
              },
              "ttft_s": 0.076487013,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 290818067693247,
              "complete": true,
              "e2e_s": 0.398541081,
              "end_ns": 290818466234328,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475475968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 88.96815251643885,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051113489,
                "rss_peak_bytes": 1272131584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.419,
                "predicted_n": 29,
                "predicted_per_second": 96.08158699329832,
                "predicted_per_token_ms": 10.407821428571427
              },
              "ttft_s": 0.107057991,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290818520840922,
              "complete": true,
              "e2e_s": 1.028495925,
              "end_ns": 290819549336847,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475869184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 270.52707238857556,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054808998,
                "rss_peak_bytes": 1272524800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 160.375,
                "predicted_n": 16,
                "predicted_per_second": 93.53078721745908,
                "predicted_per_token_ms": 10.691666666666666
              },
              "ttft_s": 0.868010583,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 290819608068918,
              "complete": true,
              "e2e_s": 0.204072703,
              "end_ns": 290819812141621,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423206912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.35794577855809,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050456985,
                "rss_peak_bytes": 1219862528,
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
              "ttft_s": 0.20389439
            },
            {
              "begin_ns": 290819861148385,
              "complete": true,
              "e2e_s": 1.366862093,
              "end_ns": 290821228010478,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423206912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 346.2194726180574,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050670682,
                "rss_peak_bytes": 1219862528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.235,
                "predicted_n": 128,
                "predicted_per_second": 97.00321179925683,
                "predicted_per_token_ms": 10.308937007874015
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057497773
            },
            {
              "begin_ns": 290821287118307,
              "complete": true,
              "e2e_s": 0.55022768,
              "end_ns": 290821837345987,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475918336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 139.2981036149022,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054400057,
                "rss_peak_bytes": 1272573952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.067,
                "predicted_n": 34,
                "predicted_per_second": 96.1911230167868,
                "predicted_per_token_ms": 10.395969696969697
              },
              "tool_call_valid": true,
              "ttft_s": 0.30370429,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290821905124898,
              "complete": true,
              "e2e_s": 0.523223836,
              "end_ns": 290822428348734,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475959296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.42663808270459,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050116258,
                "rss_peak_bytes": 1272614912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.492,
                "predicted_n": 25,
                "predicted_per_second": 95.81144308001852,
                "predicted_per_token_ms": 10.437166666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27268714,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291147983367252,
              "complete": true,
              "e2e_s": 0.157530718,
              "end_ns": 291148140897970,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419807232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.8427462351379,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050014566,
                "rss_peak_bytes": 1214128128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.251,
                "predicted_n": 10,
                "predicted_per_second": 93.50552202055044,
                "predicted_per_token_ms": 10.694555555555556
              },
              "ttft_s": 0.061273444,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291148212221936,
              "complete": true,
              "e2e_s": 0.148590739,
              "end_ns": 291148360812675,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419807232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.59059001767342,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051273285,
                "rss_peak_bytes": 1214128128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.67,
                "predicted_n": 9,
                "predicted_per_second": 93.38158048324968,
                "predicted_per_token_ms": 10.70875
              },
              "ttft_s": 0.062868555,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 291148435800724,
              "complete": true,
              "e2e_s": 0.525948455,
              "end_ns": 291148961749179,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419807232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.41944451026453,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052183518,
                "rss_peak_bytes": 1214173184,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.225,
                "predicted_n": 39,
                "predicted_per_second": 96.63678555534362,
                "predicted_per_token_ms": 10.348026315789474
              },
              "ttft_s": 0.13267069,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 291149036763314,
              "complete": true,
              "e2e_s": 0.306123658,
              "end_ns": 291149342886972,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422772736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 73.68032665557853,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051857284,
                "rss_peak_bytes": 1217204224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.199,
                "predicted_n": 23,
                "predicted_per_second": 95.98645718349556,
                "predicted_per_token_ms": 10.418136363636364
              },
              "ttft_s": 0.076952694,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 291149415820252,
              "complete": true,
              "e2e_s": 0.254536359,
              "end_ns": 291149670356611,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422772736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 55.79119789842645,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051600781,
                "rss_peak_bytes": 1217204224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.32,
                "predicted_n": 18,
                "predicted_per_second": 95.33423059668013,
                "predicted_per_token_ms": 10.489411764705881
              },
              "ttft_s": 0.076222593,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 291149742805613,
              "complete": true,
              "e2e_s": 0.397873084,
              "end_ns": 291150140678697,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475484160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 96.8188605358311,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0524243,
                "rss_peak_bytes": 1269915648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.833,
                "predicted_n": 29,
                "predicted_per_second": 96.27518197728592,
                "predicted_per_token_ms": 10.386892857142858
              },
              "ttft_s": 0.106985737,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291150217345461,
              "complete": true,
              "e2e_s": 1.027920069,
              "end_ns": 291151245265530,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475906048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 270.6248222162515,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051570987,
                "rss_peak_bytes": 1270337536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.338,
                "predicted_n": 16,
                "predicted_per_second": 94.13950219031241,
                "predicted_per_token_ms": 10.622533333333333
              },
              "ttft_s": 0.868533512,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 291151319830368,
              "complete": true,
              "e2e_s": 0.205462286,
              "end_ns": 291151525292654,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423223296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 50.72345193765998,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050563322,
                "rss_peak_bytes": 1217654784,
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
              "ttft_s": 0.205223854
            },
            {
              "begin_ns": 291151591107622,
              "complete": true,
              "e2e_s": 1.365224169,
              "end_ns": 291152956331791,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423223296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 349.474525939501,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052348866,
                "rss_peak_bytes": 1217654784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1307.869,
                "predicted_n": 128,
                "predicted_per_second": 97.10452652368089,
                "predicted_per_token_ms": 10.298181102362204
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057144266
            },
            {
              "begin_ns": 291153028072544,
              "complete": true,
              "e2e_s": 0.549049619,
              "end_ns": 291153577122163,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475947008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 136.45729937385894,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050640672,
                "rss_peak_bytes": 1270378496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.407,
                "predicted_n": 34,
                "predicted_per_second": 96.09588622247072,
                "predicted_per_token_ms": 10.406272727272727
              },
              "tool_call_valid": true,
              "ttft_s": 0.30115502,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291153659847658,
              "complete": true,
              "e2e_s": 0.523679544,
              "end_ns": 291154183527202,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475979776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 127.05059385048388,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050198396,
                "rss_peak_bytes": 1270411264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.34,
                "predicted_n": 25,
                "predicted_per_second": 95.86961732044419,
                "predicted_per_token_ms": 10.430833333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273339055,
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
          "gpu_j_per_correct_token": 26.326822706569125,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772698112,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7479.183351021955,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.082331732,
              "rss_peak_bytes": 11928772608,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772751360,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7158.530073830479,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.086832963,
              "rss_peak_bytes": 12140343296,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14637.713424852434,
          "raw_requests": [
            {
              "begin_ns": 290906173276435,
              "complete": true,
              "e2e_s": 0.465570601,
              "end_ns": 290906638847036,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 748576768,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.92862385245475,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051484073,
                "rss_peak_bytes": 1304555520,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.219,
                "predicted_n": 10,
                "predicted_per_second": 34.192060603527864,
                "predicted_per_token_ms": 29.246555555555556
              },
              "ttft_s": 0.202279844,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290906699157101,
              "complete": true,
              "e2e_s": 0.57371052,
              "end_ns": 290907272867621,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 142.18329212007967,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050973208,
                "rss_peak_bytes": 1169096704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.502,
                "predicted_n": 14,
                "predicted_per_second": 34.9930821368391,
                "predicted_per_token_ms": 28.577076923076923
              },
              "ttft_s": 0.202159809,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 290907336654450,
              "complete": true,
              "e2e_s": 1.762789875,
              "end_ns": 290909099444325,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 466.15393831147634,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052381907,
                "rss_peak_bytes": 1170014208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.769,
                "predicted_n": 45,
                "predicted_per_second": 35.40480974340364,
                "predicted_per_token_ms": 28.24475
              },
              "ttft_s": 0.51998039,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 290909164230095,
              "complete": true,
              "e2e_s": 0.987546959,
              "end_ns": 290910151777054,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615239680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 253.6419145444179,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050736474,
                "rss_peak_bytes": 1173729280,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.448,
                "predicted_n": 28,
                "predicted_per_second": 35.31960316463645,
                "predicted_per_token_ms": 28.31288888888889
              },
              "ttft_s": 0.223055003,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 290910212411386,
              "complete": true,
              "e2e_s": 0.845730244,
              "end_ns": 290911058141630,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615239680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 216.52358858816214,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051163442,
                "rss_peak_bytes": 1174056960,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.287,
                "predicted_n": 23,
                "predicted_per_second": 35.296741308578554,
                "predicted_per_token_ms": 28.331227272727276
              },
              "ttft_s": 0.222370689,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 290911121694156,
              "complete": true,
              "e2e_s": 1.141455348,
              "end_ns": 290912263149504,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772157440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 286.35622684585786,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052061668,
                "rss_peak_bytes": 1331564544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.221,
                "predicted_n": 29,
                "predicted_per_second": 35.388342827098874,
                "predicted_per_token_ms": 28.257892857142856
              },
              "ttft_s": 0.350179619,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290912325932754,
              "complete": true,
              "e2e_s": 3.768012379,
              "end_ns": 290916093945133,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772620288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1003.6438943726746,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.059156088,
                "rss_peak_bytes": 1332158464,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.3,
                "predicted_n": 21,
                "predicted_per_second": 34.524426031417235,
                "predicted_per_token_ms": 28.964999999999996
              },
              "ttft_s": 3.188699842,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 290916155247586,
              "complete": true,
              "e2e_s": 0.718185722,
              "end_ns": 290916873433308,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615755776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.72474528982806,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.062689072,
                "rss_peak_bytes": 1175293952,
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
              "ttft_s": 0.718024532
            },
            {
              "begin_ns": 290916933706043,
              "complete": true,
              "e2e_s": 3.772696338,
              "end_ns": 290920706402381,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615755776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1028.4141525250855,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052749045,
                "rss_peak_bytes": 1175293952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3577.999,
                "predicted_n": 128,
                "predicted_per_second": 35.49469969108432,
                "predicted_per_token_ms": 28.173220472440942
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194621196
            },
            {
              "begin_ns": 290920771574980,
              "complete": true,
              "e2e_s": 1.701205059,
              "end_ns": 290922472780039,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772673536,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 447.01275841287855,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050973782,
                "rss_peak_bytes": 1332211712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.324,
                "predicted_n": 34,
                "predicted_per_second": 35.131647865912086,
                "predicted_per_token_ms": 28.464363636363636
              },
              "tool_call_valid": true,
              "ttft_s": 1.02499654,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290922545204312,
              "complete": true,
              "e2e_s": 1.774301848,
              "end_ns": 290924319506160,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772698112,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 449.77210277829016,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053198284,
                "rss_peak_bytes": 1332236288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.494,
                "predicted_n": 25,
                "predicted_per_second": 35.165144308960954,
                "predicted_per_token_ms": 28.437250000000002
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091758494,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291069263099327,
              "complete": true,
              "e2e_s": 0.462890388,
              "end_ns": 291069725989715,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612302848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.33461272518737,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051485465,
                "rss_peak_bytes": 1256579072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.465,
                "predicted_n": 10,
                "predicted_per_second": 34.29028632389081,
                "predicted_per_token_ms": 29.162777777777777
              },
              "ttft_s": 0.200433733,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291069838081465,
              "complete": true,
              "e2e_s": 0.572749643,
              "end_ns": 291070410831108,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612302848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 139.80333312293308,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051128032,
                "rss_peak_bytes": 1256579072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.565,
                "predicted_n": 14,
                "predicted_per_second": 34.98714895105836,
                "predicted_per_token_ms": 28.581923076923076
              },
              "ttft_s": 0.201139136,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 291070521244979,
              "complete": true,
              "e2e_s": 1.764508941,
              "end_ns": 291072285753920,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612302848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 479.10813806996686,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.056726917,
                "rss_peak_bytes": 1256579072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.902,
                "predicted_n": 45,
                "predicted_per_second": 35.40102115854669,
                "predicted_per_token_ms": 28.24777272727273
              },
              "ttft_s": 0.521541375,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 291072400219671,
              "complete": true,
              "e2e_s": 0.99063269,
              "end_ns": 291073390852361,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 265.30858154920185,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052660489,
                "rss_peak_bytes": 1259876352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.099,
                "predicted_n": 28,
                "predicted_per_second": 35.38204086232585,
                "predicted_per_token_ms": 28.262925925925927
              },
              "ttft_s": 0.227462112,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 291073462136673,
              "complete": true,
              "e2e_s": 0.845254908,
              "end_ns": 291074307391581,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.04911840572657,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053859349,
                "rss_peak_bytes": 1259876352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.829,
                "predicted_n": 23,
                "predicted_per_second": 35.322696920021386,
                "predicted_per_token_ms": 28.31040909090909
              },
              "ttft_s": 0.22240151,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 291074377618388,
              "complete": true,
              "e2e_s": 1.148188525,
              "end_ns": 291075525806913,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772190208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 296.191761940874,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052024369,
                "rss_peak_bytes": 1416790016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.183,
                "predicted_n": 29,
                "predicted_per_second": 35.345368431284186,
                "predicted_per_token_ms": 28.29225
              },
              "ttft_s": 0.355782367,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291075596146426,
              "complete": true,
              "e2e_s": 3.786166692,
              "end_ns": 291079382313118,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772653056,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1016.629517463122,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.061847329,
                "rss_peak_bytes": 1417252864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.651,
                "predicted_n": 21,
                "predicted_per_second": 34.44409808990254,
                "predicted_per_token_ms": 29.032549999999997
              },
              "ttft_s": 3.205496418,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 291079454322366,
              "complete": true,
              "e2e_s": 0.722760718,
              "end_ns": 291080177083084,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615784448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 185.7792945137177,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054149404,
                "rss_peak_bytes": 1260384256,
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
              "ttft_s": 0.722594107
            },
            {
              "begin_ns": 291080236646079,
              "complete": true,
              "e2e_s": 3.77532583,
              "end_ns": 291084011971909,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615784448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1044.5437101861078,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054567074,
                "rss_peak_bytes": 1260384256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.113,
                "predicted_n": 128,
                "predicted_per_second": 35.46383484687582,
                "predicted_per_token_ms": 28.197740157480315
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194117038
            },
            {
              "begin_ns": 291084086563050,
              "complete": true,
              "e2e_s": 1.700603853,
              "end_ns": 291085787166903,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772710400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 461.9581928659605,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056225824,
                "rss_peak_bytes": 1417310208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.092,
                "predicted_n": 34,
                "predicted_per_second": 35.140327039310314,
                "predicted_per_token_ms": 28.457333333333334
              },
              "tool_call_valid": true,
              "ttft_s": 1.02469965,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291085865744397,
              "complete": true,
              "e2e_s": 1.77625137,
              "end_ns": 291087641995767,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772751360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 465.4190274477151,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054589104,
                "rss_peak_bytes": 1417351168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 685.707,
                "predicted_n": 25,
                "predicted_per_second": 35.00037187895121,
                "predicted_per_token_ms": 28.571125
              },
              "tool_facts_valid": true,
              "ttft_s": 1.090527216,
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
          "gpu_j_per_correct_token": 25.467603017080716,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772673536,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7065.4153035239415,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.082534246,
              "rss_peak_bytes": 12140400640,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772640768,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7094.5719739729375,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.07942573,
              "rss_peak_bytes": 12140404736,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14159.987277496879,
          "raw_requests": [
            {
              "begin_ns": 290960562175433,
              "complete": true,
              "e2e_s": 0.464838788,
              "end_ns": 290961027014221,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.83064344254457,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052106973,
                "rss_peak_bytes": 1256812544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.96,
                "predicted_n": 10,
                "predicted_per_second": 34.2257377547916,
                "predicted_per_token_ms": 29.217777777777776
              },
              "ttft_s": 0.201910838,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 290961089172556,
              "complete": true,
              "e2e_s": 0.572870174,
              "end_ns": 290961662042730,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 133.35841985149386,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05264833,
                "rss_peak_bytes": 1256812544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.416,
                "predicted_n": 14,
                "predicted_per_second": 35.00118465548064,
                "predicted_per_token_ms": 28.570461538461537
              },
              "ttft_s": 0.201447611,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 290961728782046,
              "complete": true,
              "e2e_s": 1.76120308,
              "end_ns": 290963489985126,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 471.65699317633704,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051177878,
                "rss_peak_bytes": 1256812544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.554,
                "predicted_n": 45,
                "predicted_per_second": 35.43945732525528,
                "predicted_per_token_ms": 28.217136363636367
              },
              "ttft_s": 0.519627607,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 290963554053998,
              "complete": true,
              "e2e_s": 0.98846534,
              "end_ns": 290964542519338,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615247872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 258.5303463730695,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052424517,
                "rss_peak_bytes": 1260118016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.629,
                "predicted_n": 28,
                "predicted_per_second": 35.265121880179564,
                "predicted_per_token_ms": 28.35662962962963
              },
              "ttft_s": 0.222781005,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 290964606151622,
              "complete": true,
              "e2e_s": 0.845301666,
              "end_ns": 290965451453288,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615247872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.41235125088792,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052141701,
                "rss_peak_bytes": 1260118016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.698,
                "predicted_n": 23,
                "predicted_per_second": 35.330127927181394,
                "predicted_per_token_ms": 28.304454545454544
              },
              "ttft_s": 0.222560452,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 290965520172128,
              "complete": true,
              "e2e_s": 1.143533108,
              "end_ns": 290966663705236,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772165632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 289.6619670677302,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050821681,
                "rss_peak_bytes": 1417035776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 790.899,
                "predicted_n": 29,
                "predicted_per_second": 35.40275054084024,
                "predicted_per_token_ms": 28.246392857142858
              },
              "ttft_s": 0.352623834,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 290966725363874,
              "complete": true,
              "e2e_s": 3.775058557,
              "end_ns": 290970500422431,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772583424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1008.8899465502637,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056703113,
                "rss_peak_bytes": 1417453568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.452,
                "predicted_n": 21,
                "predicted_per_second": 34.51536969412479,
                "predicted_per_token_ms": 28.9726
              },
              "ttft_s": 3.195522471,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 290970568197139,
              "complete": true,
              "e2e_s": 0.719070385,
              "end_ns": 290971287267524,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615710720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 189.63338808443675,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05104512,
                "rss_peak_bytes": 1260580864,
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
              "ttft_s": 0.718944971
            },
            {
              "begin_ns": 290971382792767,
              "complete": true,
              "e2e_s": 3.781551993,
              "end_ns": 290975164344760,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615710720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1035.2812382450618,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.060395549,
                "rss_peak_bytes": 1260580864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3584.905,
                "predicted_n": 128,
                "predicted_per_second": 35.42632231537517,
                "predicted_per_token_ms": 28.227598425196852
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196527398
            },
            {
              "begin_ns": 290975269903492,
              "complete": true,
              "e2e_s": 1.701600584,
              "end_ns": 290976971504076,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772632576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 449.3649713804029,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053214288,
                "rss_peak_bytes": 1417502720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.435,
                "predicted_n": 34,
                "predicted_per_second": 35.09014445442801,
                "predicted_per_token_ms": 28.4980303030303
              },
              "tool_call_valid": true,
              "ttft_s": 1.025763254,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 290977049364050,
              "complete": true,
              "e2e_s": 1.768692579,
              "end_ns": 290978818056629,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772673536,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 463.4992562401088,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053548638,
                "rss_peak_bytes": 1417543680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 679.745,
                "predicted_n": 25,
                "predicted_per_second": 35.30735790627367,
                "predicted_per_token_ms": 28.322708333333335
              },
              "tool_facts_valid": true,
              "ttft_s": 1.088910516,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 291014788295733,
              "complete": true,
              "e2e_s": 0.463251626,
              "end_ns": 291015251547359,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.04695501670426,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050280874,
                "rss_peak_bytes": 1256796160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.967,
                "predicted_n": 10,
                "predicted_per_second": 34.224826689280405,
                "predicted_per_token_ms": 29.218555555555554
              },
              "ttft_s": 0.200218335,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 291015315727822,
              "complete": true,
              "e2e_s": 0.575033874,
              "end_ns": 291015890761696,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.2719443468411,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05078298,
                "rss_peak_bytes": 1256796160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 372.925,
                "predicted_n": 14,
                "predicted_per_second": 34.85955621103439,
                "predicted_per_token_ms": 28.68653846153846
              },
              "ttft_s": 0.202071085,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 291015956190613,
              "complete": true,
              "e2e_s": 1.76076307,
              "end_ns": 291017716953683,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 473.30318063515534,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05222927,
                "rss_peak_bytes": 1256796160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.021,
                "predicted_n": 45,
                "predicted_per_second": 35.45467804332078,
                "predicted_per_token_ms": 28.205022727272727
              },
              "ttft_s": 0.519694382,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 291017788259072,
              "complete": true,
              "e2e_s": 0.992855874,
              "end_ns": 291018781114946,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 262.68328019025364,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056440584,
                "rss_peak_bytes": 1260093440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.65,
                "predicted_n": 28,
                "predicted_per_second": 35.31027267377231,
                "predicted_per_token_ms": 28.32037037037037
              },
              "ttft_s": 0.228119883,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 291018852204851,
              "complete": true,
              "e2e_s": 0.843522056,
              "end_ns": 291019695726907,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 220.68331572238307,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050529463,
                "rss_peak_bytes": 1260093440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.849,
                "predicted_n": 23,
                "predicted_per_second": 35.32156269015443,
                "predicted_per_token_ms": 28.311318181818184
              },
              "ttft_s": 0.220683886,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 291019760166587,
              "complete": true,
              "e2e_s": 1.142816452,
              "end_ns": 291020902983039,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772157440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 289.7629384369566,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055073128,
                "rss_peak_bytes": 1417007104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.673,
                "predicted_n": 29,
                "predicted_per_second": 35.36813810752672,
                "predicted_per_token_ms": 28.274035714285713
              },
              "ttft_s": 0.351121951,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 291020973252988,
              "complete": true,
              "e2e_s": 3.783141319,
              "end_ns": 291024756394307,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772575232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1009.9054070987012,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.058107216,
                "rss_peak_bytes": 1417424896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.956,
                "predicted_n": 21,
                "predicted_per_second": 34.42601505105378,
                "predicted_per_token_ms": 29.047800000000002
              },
              "ttft_s": 3.202108833,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 291024827179617,
              "complete": true,
              "e2e_s": 0.721689716,
              "end_ns": 291025548869333,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615702528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 191.25746587368812,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055390297,
                "rss_peak_bytes": 1260552192,
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
              "ttft_s": 0.72156763
            },
            {
              "begin_ns": 291025604095881,
              "complete": true,
              "e2e_s": 3.773961165,
              "end_ns": 291029378057046,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615702528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1043.749682335871,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052503649,
                "rss_peak_bytes": 1260552192,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.164,
                "predicted_n": 128,
                "predicted_per_second": 35.463329800031495,
                "predicted_per_token_ms": 28.198141732283467
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.192702004
            },
            {
              "begin_ns": 291029446183627,
              "complete": true,
              "e2e_s": 1.700981534,
              "end_ns": 291031147165161,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772612096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 456.2264012937365,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050845158,
                "rss_peak_bytes": 1417461760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.544,
                "predicted_n": 34,
                "predicted_per_second": 35.123421574721355,
                "predicted_per_token_ms": 28.471030303030304
              },
              "tool_call_valid": true,
              "ttft_s": 1.025034076,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 291031234721765,
              "complete": true,
              "e2e_s": 1.770550357,
              "end_ns": 291033005272122,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772640768,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 460.3121497851274,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053477152,
                "rss_peak_bytes": 1417490432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.111,
                "predicted_n": 25,
                "predicted_per_second": 35.23654734690821,
                "predicted_per_token_ms": 28.379625
              },
              "tool_facts_valid": true,
              "ttft_s": 1.089377659,
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
