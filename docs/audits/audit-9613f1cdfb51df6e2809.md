# Public audit excerpt

Original SHA256: `9613f1cdfb51df6e2809432a3be908c2f8779a930b07a8545cf804801cf0deb8`

Original file: `RESULTS.json`; 266214 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.59959197642064,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470335488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2681.4747864325113,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.219219486,
              "rss_peak_bytes": 7726145536,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470339584,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2713.4959043158883,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.079885272,
              "rss_peak_bytes": 7726129152,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5394.9706907484,
          "raw_requests": [
            {
              "begin_ns": 292044407182000,
              "complete": true,
              "e2e_s": 0.182762615,
              "end_ns": 292044589944615,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 38.45477465199708,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050321677,
                "rss_peak_bytes": 1468137472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.106,
                "predicted_n": 10,
                "predicted_per_second": 77.5153738824867,
                "predicted_per_token_ms": 12.900666666666666
              },
              "ttft_s": 0.066603622,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292044639236893,
              "complete": true,
              "e2e_s": 0.233811835,
              "end_ns": 292044873048728,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 58.250664697363426,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051470171,
                "rss_peak_bytes": 1468137472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.69,
                "predicted_n": 14,
                "predicted_per_second": 78.45977427726477,
                "predicted_per_token_ms": 12.745384615384616
              },
              "ttft_s": 0.068106514,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292044928822186,
              "complete": true,
              "e2e_s": 0.665473161,
              "end_ns": 292045594295347,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 179.05509848329572,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052459694,
                "rss_peak_bytes": 1468182528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.448,
                "predicted_n": 44,
                "predicted_per_second": 79.41667528553066,
                "predicted_per_token_ms": 12.591813953488371
              },
              "ttft_s": 0.123972185,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292045658320503,
              "complete": true,
              "e2e_s": 0.358275699,
              "end_ns": 292046016596202,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 87.98608290321076,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05133223,
                "rss_peak_bytes": 1468182528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.796,
                "predicted_n": 23,
                "predicted_per_second": 78.91074477395658,
                "predicted_per_token_ms": 12.672545454545455
              },
              "ttft_s": 0.079462913,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292046080848498,
              "complete": true,
              "e2e_s": 0.295141418,
              "end_ns": 292046375989916,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.23796972561063,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050045225,
                "rss_peak_bytes": 1468186624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 215.839,
                "predicted_n": 18,
                "predicted_per_second": 78.76241087106592,
                "predicted_per_token_ms": 12.696411764705882
              },
              "ttft_s": 0.07923968,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292046435832527,
              "complete": true,
              "e2e_s": 0.469899981,
              "end_ns": 292046905732508,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469782528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 119.4091148954864,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051234396,
                "rss_peak_bytes": 1523879936,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.249,
                "predicted_n": 29,
                "predicted_per_second": 79.04044894975003,
                "predicted_per_token_ms": 12.651750000000002
              },
              "ttft_s": 0.115624713,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292046968318629,
              "complete": true,
              "e2e_s": 1.074557832,
              "end_ns": 292048042876461,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470249472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 283.1148346558044,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053571304,
                "rss_peak_bytes": 1524346880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.535,
                "predicted_n": 21,
                "predicted_per_second": 77.96207145223848,
                "predicted_per_token_ms": 12.82675
              },
              "ttft_s": 0.817953846,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292048094865080,
              "complete": true,
              "e2e_s": 0.198459059,
              "end_ns": 292048293324139,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417587200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.93467121022992,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053796168,
                "rss_peak_bytes": 1471684608,
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
              "ttft_s": 0.198332492
            },
            {
              "begin_ns": 292048342094232,
              "complete": true,
              "e2e_s": 1.658602752,
              "end_ns": 292050000696984,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417587200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 441.8763487968904,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052342385,
                "rss_peak_bytes": 1471684608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.629,
                "predicted_n": 128,
                "predicted_per_second": 79.64234941168134,
                "predicted_per_token_ms": 12.556133858267716
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063846387
            },
            {
              "begin_ns": 292050055123917,
              "complete": true,
              "e2e_s": 0.619481182,
              "end_ns": 292050674605099,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470302720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 156.27826691141973,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051043608,
                "rss_peak_bytes": 1524400128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.873,
                "predicted_n": 34,
                "predicted_per_second": 78.97136211241214,
                "predicted_per_token_ms": 12.662818181818182
              },
              "tool_call_valid": true,
              "ttft_s": 0.317820129,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292050741135115,
              "complete": true,
              "e2e_s": 0.557993495,
              "end_ns": 292051299128610,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470335488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.3884615110656,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055263426,
                "rss_peak_bytes": 1524432896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.246,
                "predicted_n": 25,
                "predicted_per_second": 78.88353503415,
                "predicted_per_token_ms": 12.676916666666665
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253716969,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292555543158614,
              "complete": true,
              "e2e_s": 0.182434876,
              "end_ns": 292555725593490,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.76493238162364,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05051319,
                "rss_peak_bytes": 1470369792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.345,
                "predicted_n": 10,
                "predicted_per_second": 77.35613906914779,
                "predicted_per_token_ms": 12.927222222222222
              },
              "ttft_s": 0.066073524,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292555802132338,
              "complete": true,
              "e2e_s": 0.233502553,
              "end_ns": 292556035634891,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.73034094011558,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050123266,
                "rss_peak_bytes": 1470369792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.332,
                "predicted_n": 14,
                "predicted_per_second": 78.15693913378064,
                "predicted_per_token_ms": 12.79476923076923
              },
              "ttft_s": 0.067150222,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292556115935100,
              "complete": true,
              "e2e_s": 0.666503321,
              "end_ns": 292556782438421,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.56748474507694,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052839879,
                "rss_peak_bytes": 1470414848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.682,
                "predicted_n": 44,
                "predicted_per_second": 79.23609038073863,
                "predicted_per_token_ms": 12.620511627906977
              },
              "ttft_s": 0.123842209,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292556858925589,
              "complete": true,
              "e2e_s": 0.359017843,
              "end_ns": 292557217943432,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 88.4102113752961,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052654451,
                "rss_peak_bytes": 1470418944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.647,
                "predicted_n": 23,
                "predicted_per_second": 78.6706097329848,
                "predicted_per_token_ms": 12.711227272727273
              },
              "ttft_s": 0.079366655,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292557295817838,
              "complete": true,
              "e2e_s": 0.295544758,
              "end_ns": 292557591362596,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.46245078000142,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051636763,
                "rss_peak_bytes": 1470423040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.278,
                "predicted_n": 18,
                "predicted_per_second": 78.60253932438806,
                "predicted_per_token_ms": 12.722235294117647
              },
              "ttft_s": 0.079304055,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292557669102647,
              "complete": true,
              "e2e_s": 0.468671821,
              "end_ns": 292558137774468,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469790720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 114.7047116624089,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050495775,
                "rss_peak_bytes": 1526120448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.621,
                "predicted_n": 29,
                "predicted_per_second": 79.18081788129099,
                "predicted_per_token_ms": 12.629321428571428
              },
              "ttft_s": 0.115000854,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292558219214555,
              "complete": true,
              "e2e_s": 1.081767863,
              "end_ns": 292559300982418,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 286.06079061671585,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055959945,
                "rss_peak_bytes": 1526591488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.029,
                "predicted_n": 21,
                "predicted_per_second": 78.11615090478031,
                "predicted_per_token_ms": 12.801449999999999
              },
              "ttft_s": 0.825734832,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292559376928235,
              "complete": true,
              "e2e_s": 0.197946822,
              "end_ns": 292559574875057,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.01227385755487,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050310866,
                "rss_peak_bytes": 1473908736,
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
              "ttft_s": 0.197812749
            },
            {
              "begin_ns": 292559640095287,
              "complete": true,
              "e2e_s": 1.659344926,
              "end_ns": 292561299440213,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 451.71746619592517,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051267578,
                "rss_peak_bytes": 1473908736,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.828,
                "predicted_n": 128,
                "predicted_per_second": 79.63241177104992,
                "predicted_per_token_ms": 12.557700787401574
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.064382839
            },
            {
              "begin_ns": 292561377139927,
              "complete": true,
              "e2e_s": 0.619639827,
              "end_ns": 292561996779754,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 156.05069094252408,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053610368,
                "rss_peak_bytes": 1526624256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.558,
                "predicted_n": 34,
                "predicted_per_second": 78.8421198495788,
                "predicted_per_token_ms": 12.683575757575758
              },
              "tool_call_valid": true,
              "ttft_s": 0.318645682,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292562081186055,
              "complete": true,
              "e2e_s": 0.558957046,
              "end_ns": 292562640143101,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470339584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 145.96753632142807,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050336843,
                "rss_peak_bytes": 1526669312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.177,
                "predicted_n": 25,
                "predicted_per_second": 78.90142910213461,
                "predicted_per_token_ms": 12.674041666666668
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254760506,
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
          "gpu_j_per_correct_token": 13.784518474910813,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 477450240,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7611088896,
              "gpu_energy_j": 3649.5294565287822,
              "gpu_owned_peak_bytes": 7356809216,
              "max_sample_gap_s": 0.083739871,
              "rss_peak_bytes": 7726080000,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 477446144,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7611088896,
              "gpu_energy_j": 4097.369926371095,
              "gpu_owned_peak_bytes": 7356809216,
              "max_sample_gap_s": 0.081589442,
              "rss_peak_bytes": 7715917824,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 7746.899382899877,
          "raw_requests": [
            {
              "begin_ns": 292074394130165,
              "complete": true,
              "e2e_s": 0.18257872,
              "end_ns": 292074576708885,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 418000896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 41.93767132437168,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.05011847,
                "rss_peak_bytes": 1436962816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.115,
                "predicted_n": 10,
                "predicted_per_second": 77.5093657150239,
                "predicted_per_token_ms": 12.901666666666666
              },
              "ttft_s": 0.06643339,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292074636228259,
              "complete": true,
              "e2e_s": 0.234694628,
              "end_ns": 292074870922887,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 418000896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 57.7709975911978,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050432035,
                "rss_peak_bytes": 1436962816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.566,
                "predicted_n": 14,
                "predicted_per_second": 78.51853641448123,
                "predicted_per_token_ms": 12.735846153846154
              },
              "ttft_s": 0.069124642,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292074926432757,
              "complete": true,
              "e2e_s": 0.689906272,
              "end_ns": 292075616339029,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 473849856,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 178.17857044304358,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050776922,
                "rss_peak_bytes": 1493327872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.322,
                "predicted_n": 44,
                "predicted_per_second": 79.28868827006833,
                "predicted_per_token_ms": 12.61213953488372
              },
              "ttft_s": 0.147611244,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292075675643810,
              "complete": true,
              "e2e_s": 0.360097229,
              "end_ns": 292076035741039,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 421171200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 91.40405360556983,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050180951,
                "rss_peak_bytes": 1440649216,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.427,
                "predicted_n": 23,
                "predicted_per_second": 79.01532538151831,
                "predicted_per_token_ms": 12.655772727272728
              },
              "ttft_s": 0.08164078,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292076095176613,
              "complete": true,
              "e2e_s": 0.295466007,
              "end_ns": 292076390642620,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 421175296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 72.62536366060212,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050283894,
                "rss_peak_bytes": 1440653312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.226,
                "predicted_n": 18,
                "predicted_per_second": 78.62144237973231,
                "predicted_per_token_ms": 12.719176470588236
              },
              "ttft_s": 0.079204947,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292076449201019,
              "complete": true,
              "e2e_s": 0.501856856,
              "end_ns": 292076951057875,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476868608,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 121.03377893990549,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051072818,
                "rss_peak_bytes": 1496350720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 355.304,
                "predicted_n": 29,
                "predicted_per_second": 78.80575507171325,
                "predicted_per_token_ms": 12.68942857142857
              },
              "ttft_s": 0.146674337,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292077008628086,
              "complete": true,
              "e2e_s": 3.0397866,
              "end_ns": 292080048414686,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477360128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 800.6102500055113,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.052638553,
                "rss_peak_bytes": 1496842240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 255.926,
                "predicted_n": 21,
                "predicted_per_second": 78.14758953760071,
                "predicted_per_token_ms": 12.796299999999999
              },
              "ttft_s": 2.783827939,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292080143299613,
              "complete": true,
              "e2e_s": 0.648317662,
              "end_ns": 292080791617275,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477392896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 163.99392769912578,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050588953,
                "rss_peak_bytes": 1496875008,
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
              "ttft_s": 0.648193129
            },
            {
              "begin_ns": 292080839256749,
              "complete": true,
              "e2e_s": 1.659633291,
              "end_ns": 292082498890040,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 424697856,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 446.1632952013367,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.07205446,
                "rss_peak_bytes": 1444179968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1593.857,
                "predicted_n": 128,
                "predicted_per_second": 79.68092495123464,
                "predicted_per_token_ms": 12.550055118110237
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.065659327
            },
            {
              "begin_ns": 292082559760242,
              "complete": true,
              "e2e_s": 0.824749735,
              "end_ns": 292083384509977,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477413376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 205.8729443409083,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.052150953,
                "rss_peak_bytes": 1496895488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 416.74,
                "predicted_n": 34,
                "predicted_per_second": 79.1860632528675,
                "predicted_per_token_ms": 12.628484848484849
              },
              "tool_call_valid": true,
              "ttft_s": 0.524059815,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292083453808288,
              "complete": true,
              "e2e_s": 0.829481636,
              "end_ns": 292084283289924,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477450240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 206.9388141204281,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051168863,
                "rss_peak_bytes": 1496932352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.039,
                "predicted_n": 25,
                "predicted_per_second": 78.93724160387319,
                "predicted_per_token_ms": 12.668291666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.525409702,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292523019165967,
              "complete": true,
              "e2e_s": 0.18230961,
              "end_ns": 292523201475577,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 418009088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 39.6969960810087,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.05165647,
                "rss_peak_bytes": 1430634496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.896,
                "predicted_n": 10,
                "predicted_per_second": 77.65582936425761,
                "predicted_per_token_ms": 12.877333333333333
              },
              "ttft_s": 0.066419984,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292523290213059,
              "complete": true,
              "e2e_s": 0.233361437,
              "end_ns": 292523523574496,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 418009088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 58.60541256339491,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051430634,
                "rss_peak_bytes": 1430634496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.209,
                "predicted_n": 14,
                "predicted_per_second": 78.21477777978329,
                "predicted_per_token_ms": 12.785307692307693
              },
              "ttft_s": 0.067113226,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292523596793811,
              "complete": true,
              "e2e_s": 0.687839828,
              "end_ns": 292524284633639,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 473858048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 184.42020811311411,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050069245,
                "rss_peak_bytes": 1486999552,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.572,
                "predicted_n": 44,
                "predicted_per_second": 79.39849179795115,
                "predicted_per_token_ms": 12.594697674418605
              },
              "ttft_s": 0.146230976,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292524360130001,
              "complete": true,
              "e2e_s": 0.359923563,
              "end_ns": 292524720053564,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 421175296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 91.42119779679079,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051200739,
                "rss_peak_bytes": 1434316800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.109,
                "predicted_n": 23,
                "predicted_per_second": 78.82225223837283,
                "predicted_per_token_ms": 12.686772727272727
              },
              "ttft_s": 0.080790278,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292524796041437,
              "complete": true,
              "e2e_s": 0.294889848,
              "end_ns": 292525090931285,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 421179392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 73.6072795785128,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050544674,
                "rss_peak_bytes": 1434320896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.283,
                "predicted_n": 18,
                "predicted_per_second": 78.60072220192987,
                "predicted_per_token_ms": 12.722529411764706
              },
              "ttft_s": 0.078552422,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292525169714172,
              "complete": true,
              "e2e_s": 0.500192475,
              "end_ns": 292525669906647,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476876800,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 123.05471477139187,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051352222,
                "rss_peak_bytes": 1490022400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.155,
                "predicted_n": 29,
                "predicted_per_second": 79.06142790586044,
                "predicted_per_token_ms": 12.648392857142856
              },
              "ttft_s": 0.145970169,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292525763020220,
              "complete": true,
              "e2e_s": 3.041428504,
              "end_ns": 292528804448724,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477364224,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 823.5563907582439,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.053950656,
                "rss_peak_bytes": 1490391040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.233,
                "predicted_n": 21,
                "predicted_per_second": 78.05395870165044,
                "predicted_per_token_ms": 12.81165
              },
              "ttft_s": 2.785219384,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292528878047511,
              "complete": true,
              "e2e_s": 0.646795138,
              "end_ns": 292529524842649,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477396992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 166.43885416742648,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.050487053,
                "rss_peak_bytes": 1489559552,
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
              "ttft_s": 0.64667013
            },
            {
              "begin_ns": 292529611238960,
              "complete": true,
              "e2e_s": 1.659037406,
              "end_ns": 292531270276366,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 424701952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 455.4245496783615,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.052011083,
                "rss_peak_bytes": 1436864512,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.012,
                "predicted_n": 128,
                "predicted_per_second": 79.67317686441508,
                "predicted_per_token_ms": 12.55127559055118
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.064974068
            },
            {
              "begin_ns": 292531344413854,
              "complete": true,
              "e2e_s": 0.824639036,
              "end_ns": 292532169052890,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477413376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 217.292613211889,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051981125,
                "rss_peak_bytes": 1489575936,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.074,
                "predicted_n": 34,
                "predicted_per_second": 79.12264969765556,
                "predicted_per_token_ms": 12.638606060606062
              },
              "tool_call_valid": true,
              "ttft_s": 0.523696503,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292532255107345,
              "complete": true,
              "e2e_s": 0.828229888,
              "end_ns": 292533083337233,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 477446144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7611088896,
                "gpu_energy_j": 211.54177899426224,
                "gpu_owned_peak_bytes": 7356809216,
                "max_sample_gap_s": 0.051538574,
                "rss_peak_bytes": 1489608704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.119,
                "predicted_n": 25,
                "predicted_per_second": 78.91647677389443,
                "predicted_per_token_ms": 12.671625
              },
              "tool_facts_valid": true,
              "ttft_s": 0.524121721,
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
          "gpu_j_per_correct_token": 8.87987833933295,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476008448,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2256.581052787794,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.088135258,
              "rss_peak_bytes": 5995966464,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476016640,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2556.313007130665,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.056106666,
              "rss_peak_bytes": 5862264832,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4812.894059918459,
          "raw_requests": [
            {
              "begin_ns": 292133298331696,
              "complete": true,
              "e2e_s": 0.157095543,
              "end_ns": 292133455427239,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.904926338329012,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053875063,
                "rss_peak_bytes": 1206861824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.947,
                "predicted_n": 10,
                "predicted_per_second": 93.80178640290994,
                "predicted_per_token_ms": 10.660777777777778
              },
              "ttft_s": 0.061113323,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292133516866153,
              "complete": true,
              "e2e_s": 0.149499028,
              "end_ns": 292133666365181,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 28.05317786303181,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052363978,
                "rss_peak_bytes": 1206861824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.933,
                "predicted_n": 9,
                "predicted_per_second": 93.0957839246855,
                "predicted_per_token_ms": 10.741625
              },
              "ttft_s": 0.063544602,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292133724180472,
              "complete": true,
              "e2e_s": 0.526397781,
              "end_ns": 292134250578253,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.86128578752175,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052425461,
                "rss_peak_bytes": 1206906880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.132,
                "predicted_n": 39,
                "predicted_per_second": 96.41439923680392,
                "predicted_per_token_ms": 10.371894736842105
              },
              "ttft_s": 0.132201973,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292134309576165,
              "complete": true,
              "e2e_s": 0.307044506,
              "end_ns": 292134616620671,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 70.60468445402726,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050203962,
                "rss_peak_bytes": 1209937920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.48,
                "predicted_n": 23,
                "predicted_per_second": 95.8689210388705,
                "predicted_per_token_ms": 10.43090909090909
              },
              "ttft_s": 0.077610873,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292134723030649,
              "complete": true,
              "e2e_s": 0.254758606,
              "end_ns": 292134977789255,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.64807145967238,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050064257,
                "rss_peak_bytes": 1209954304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.205,
                "predicted_n": 18,
                "predicted_per_second": 95.39575208327487,
                "predicted_per_token_ms": 10.482647058823531
              },
              "ttft_s": 0.076504128,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292135038209822,
              "complete": true,
              "e2e_s": 0.398229244,
              "end_ns": 292135436439066,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475471872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.62011380588866,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051249197,
                "rss_peak_bytes": 1262669824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.861,
                "predicted_n": 29,
                "predicted_per_second": 96.26591395890134,
                "predicted_per_token_ms": 10.387892857142857
              },
              "ttft_s": 0.107350315,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292135505999427,
              "complete": true,
              "e2e_s": 1.027926399,
              "end_ns": 292136533925826,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475938816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 268.6130993426038,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051245767,
                "rss_peak_bytes": 1263136768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.704,
                "predicted_n": 16,
                "predicted_per_second": 93.92375895406502,
                "predicted_per_token_ms": 10.646933333333333
              },
              "ttft_s": 0.868172477,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292136604302093,
              "complete": true,
              "e2e_s": 0.205067726,
              "end_ns": 292136809369819,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423251968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 48.4442894704145,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052054544,
                "rss_peak_bytes": 1210449920,
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
              "ttft_s": 0.204936258
            },
            {
              "begin_ns": 292136877071393,
              "complete": true,
              "e2e_s": 1.368206957,
              "end_ns": 292138245278350,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423251968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 342.91177216557173,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.059954775,
                "rss_peak_bytes": 1210449920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1310.236,
                "predicted_n": 128,
                "predicted_per_second": 96.9291028486471,
                "predicted_per_token_ms": 10.316818897637797
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057774767
            },
            {
              "begin_ns": 292138304775978,
              "complete": true,
              "e2e_s": 0.551833875,
              "end_ns": 292138856609853,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475967488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.17991144995176,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051493037,
                "rss_peak_bytes": 1262428160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.039,
                "predicted_n": 34,
                "predicted_per_second": 96.19897446062984,
                "predicted_per_token_ms": 10.39512121212121
              },
              "tool_call_valid": true,
              "ttft_s": 0.304459796,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292138928470911,
              "complete": true,
              "e2e_s": 0.524289433,
              "end_ns": 292139452760344,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476008448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.36086978530966,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051531455,
                "rss_peak_bytes": 1262469120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.362,
                "predicted_n": 25,
                "predicted_per_second": 95.86119299254679,
                "predicted_per_token_ms": 10.43175
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273913363,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292452902152780,
              "complete": true,
              "e2e_s": 0.157011929,
              "end_ns": 292453059164709,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.547757421893266,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050256642,
                "rss_peak_bytes": 1104670720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.004,
                "predicted_n": 10,
                "predicted_per_second": 93.74609391275364,
                "predicted_per_token_ms": 10.667111111111112
              },
              "ttft_s": 0.061033506,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292453129150644,
              "complete": true,
              "e2e_s": 0.14915381,
              "end_ns": 292453278304454,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.69817100570275,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050161095,
                "rss_peak_bytes": 1104867328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.127,
                "predicted_n": 9,
                "predicted_per_second": 92.88608682526967,
                "predicted_per_token_ms": 10.765875
              },
              "ttft_s": 0.063051052,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292453351067123,
              "complete": true,
              "e2e_s": 0.526234951,
              "end_ns": 292453877302074,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 127.57651254641061,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051904063,
                "rss_peak_bytes": 1105059840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.879,
                "predicted_n": 39,
                "predicted_per_second": 96.47632902490359,
                "predicted_per_token_ms": 10.365236842105263
              },
              "ttft_s": 0.132382398,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292453947180623,
              "complete": true,
              "e2e_s": 0.306629794,
              "end_ns": 292454253810417,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.97540415273922,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052593792,
                "rss_peak_bytes": 1108221952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.111,
                "predicted_n": 23,
                "predicted_per_second": 96.0233249385669,
                "predicted_per_token_ms": 10.414136363636363
              },
              "ttft_s": 0.077461848,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292454332039084,
              "complete": true,
              "e2e_s": 0.254097498,
              "end_ns": 292454586136582,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.72396654420689,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052197149,
                "rss_peak_bytes": 1108287488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.991,
                "predicted_n": 18,
                "predicted_per_second": 95.51044715744054,
                "predicted_per_token_ms": 10.470058823529413
              },
              "ttft_s": 0.076060981,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292454662187592,
              "complete": true,
              "e2e_s": 0.398805755,
              "end_ns": 292455060993347,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475480064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 90.36358591607862,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05017213,
                "rss_peak_bytes": 1161129984,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.722,
                "predicted_n": 29,
                "predicted_per_second": 96.3119406168092,
                "predicted_per_token_ms": 10.38292857142857
              },
              "ttft_s": 0.108042232,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292455132344465,
              "complete": true,
              "e2e_s": 1.030388158,
              "end_ns": 292456162732623,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475934720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 275.0894437874387,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05346792,
                "rss_peak_bytes": 1161650176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.832,
                "predicted_n": 16,
                "predicted_per_second": 94.43940767603506,
                "predicted_per_token_ms": 10.588799999999999
              },
              "ttft_s": 0.871567308,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292456238914015,
              "complete": true,
              "e2e_s": 0.205357925,
              "end_ns": 292456444271940,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423272448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 51.449407732595525,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050076208,
                "rss_peak_bytes": 1108987904,
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
              "ttft_s": 0.205226153
            },
            {
              "begin_ns": 292456508202595,
              "complete": true,
              "e2e_s": 1.366780646,
              "end_ns": 292457874983241,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423272448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 350.544053934501,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050758176,
                "rss_peak_bytes": 1108987904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.991,
                "predicted_n": 128,
                "predicted_per_second": 97.0212935001081,
                "predicted_per_token_ms": 10.307015748031496
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057681117
            },
            {
              "begin_ns": 292457945107444,
              "complete": true,
              "e2e_s": 0.551565193,
              "end_ns": 292458496672637,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.53801660775548,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051573017,
                "rss_peak_bytes": 1161703424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.693,
                "predicted_n": 34,
                "predicted_per_second": 96.01592118547657,
                "predicted_per_token_ms": 10.414939393939393
              },
              "tool_call_valid": true,
              "ttft_s": 0.304714291,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292458579354722,
              "complete": true,
              "e2e_s": 0.523516601,
              "end_ns": 292459102871323,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476016640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.1932359430347,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056106666,
                "rss_peak_bytes": 1161732096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.205,
                "predicted_n": 25,
                "predicted_per_second": 95.92134449751202,
                "predicted_per_token_ms": 10.425208333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27326911,
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
          "gpu_j_per_correct_token": 12.652984501925875,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 483524608,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6143082496,
              "gpu_energy_j": 3424.1136555220605,
              "gpu_owned_peak_bytes": 5888802816,
              "max_sample_gap_s": 0.078779604,
              "rss_peak_bytes": 5996003328,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 483459072,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6143082496,
              "gpu_energy_j": 3433.803944521764,
              "gpu_owned_peak_bytes": 5888802816,
              "max_sample_gap_s": 0.092920538,
              "rss_peak_bytes": 5995966464,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 6857.917600043825,
          "raw_requests": [
            {
              "begin_ns": 292105761099674,
              "complete": true,
              "e2e_s": 0.157018941,
              "end_ns": 292105918118615,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423895040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 30.227263074776126,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050685714,
                "rss_peak_bytes": 1181503488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.684,
                "predicted_n": 10,
                "predicted_per_second": 94.0596128924376,
                "predicted_per_token_ms": 10.631555555555556
              },
              "ttft_s": 0.061261441,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292105976670520,
              "complete": true,
              "e2e_s": 0.148357184,
              "end_ns": 292106125027704,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423895040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 32.72602502673089,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050023443,
                "rss_peak_bytes": 1181503488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.169,
                "predicted_n": 9,
                "predicted_per_second": 93.93089034742688,
                "predicted_per_token_ms": 10.646125
              },
              "ttft_s": 0.063155974,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292106184190507,
              "complete": true,
              "e2e_s": 0.548604987,
              "end_ns": 292106732795494,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 479948800,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 132.48781337492755,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050210814,
                "rss_peak_bytes": 1238073344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.753,
                "predicted_n": 39,
                "predicted_per_second": 96.26272631240296,
                "predicted_per_token_ms": 10.388236842105263
              },
              "ttft_s": 0.153876534,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292106794406464,
              "complete": true,
              "e2e_s": 0.319809371,
              "end_ns": 292107114215835,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 427261952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 69.7981198669919,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.0538195,
                "rss_peak_bytes": 1185386496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 237.915,
                "predicted_n": 23,
                "predicted_per_second": 92.46999978984091,
                "predicted_per_token_ms": 10.814318181818182
              },
              "ttft_s": 0.081743788,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292107178162613,
              "complete": true,
              "e2e_s": 0.254012341,
              "end_ns": 292107432174954,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 427261952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 59.77645599909353,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050291574,
                "rss_peak_bytes": 1185386496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.884,
                "predicted_n": 18,
                "predicted_per_second": 95.56789818083695,
                "predicted_per_token_ms": 10.463764705882353
              },
              "ttft_s": 0.076085206,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292107487952443,
              "complete": true,
              "e2e_s": 0.429640477,
              "end_ns": 292107917592920,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 482955264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 99.41943298289824,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.051410706,
                "rss_peak_bytes": 1241079808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.61,
                "predicted_n": 29,
                "predicted_per_second": 96.34905887615705,
                "predicted_per_token_ms": 10.378928571428572
              },
              "ttft_s": 0.138975356,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292107978162034,
              "complete": true,
              "e2e_s": 3.306534392,
              "end_ns": 292111284696426,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483434496,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 860.3030211726073,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.078779604,
                "rss_peak_bytes": 1241559040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.573,
                "predicted_n": 16,
                "predicted_per_second": 94.59365717997389,
                "predicted_per_token_ms": 10.571533333333333
              },
              "ttft_s": 3.147914232,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292111341182680,
              "complete": true,
              "e2e_s": 0.719801244,
              "end_ns": 292112060983924,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483467264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 181.78871982313768,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.05073237,
                "rss_peak_bytes": 1241591808,
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
              "ttft_s": 0.719670788
            },
            {
              "begin_ns": 292112116461955,
              "complete": true,
              "e2e_s": 1.367204516,
              "end_ns": 292113483666471,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 430772224,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 347.3690044834502,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050612284,
                "rss_peak_bytes": 1188896768,
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
              "ttft_s": 0.059861763
            },
            {
              "begin_ns": 292113549205449,
              "complete": true,
              "e2e_s": 0.773836304,
              "end_ns": 292114323041753,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483487744,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 190.4780425276958,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.052551042,
                "rss_peak_bytes": 1241612288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.074,
                "predicted_n": 34,
                "predicted_per_second": 96.47035436776838,
                "predicted_per_token_ms": 10.365878787878788
              },
              "tool_call_valid": true,
              "ttft_s": 0.527465309,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292114398309116,
              "complete": true,
              "e2e_s": 0.824457719,
              "end_ns": 292115222766835,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483524608,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 201.345685342893,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050671567,
                "rss_peak_bytes": 1241649152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.052,
                "predicted_n": 25,
                "predicted_per_second": 95.9800361524803,
                "predicted_per_token_ms": 10.418833333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.574247748,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292478761327340,
              "complete": true,
              "e2e_s": 0.156199268,
              "end_ns": 292478917526608,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423849984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 32.258926364447156,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050626355,
                "rss_peak_bytes": 1181929472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.603,
                "predicted_n": 10,
                "predicted_per_second": 94.13930525192724,
                "predicted_per_token_ms": 10.622555555555556
              },
              "ttft_s": 0.060529849,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292478993429355,
              "complete": true,
              "e2e_s": 0.148540178,
              "end_ns": 292479141969533,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423849984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 32.24504672692291,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050094506,
                "rss_peak_bytes": 1181929472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.288,
                "predicted_n": 9,
                "predicted_per_second": 93.79983116030391,
                "predicted_per_token_ms": 10.661
              },
              "ttft_s": 0.063234252,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292479216632190,
              "complete": true,
              "e2e_s": 0.548979111,
              "end_ns": 292479765611301,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 479903744,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 133.02019989449522,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.051351186,
                "rss_peak_bytes": 1238503424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.173,
                "predicted_n": 39,
                "predicted_per_second": 96.4043706697313,
                "predicted_per_token_ms": 10.372973684210526
              },
              "ttft_s": 0.154814343,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292479843749843,
              "complete": true,
              "e2e_s": 0.307236012,
              "end_ns": 292480150985855,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 427220992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 71.68122061011641,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.051164264,
                "rss_peak_bytes": 1185820672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.219,
                "predicted_n": 23,
                "predicted_per_second": 95.97808209616133,
                "predicted_per_token_ms": 10.419045454545454
              },
              "ttft_s": 0.077988635,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292480227758770,
              "complete": true,
              "e2e_s": 0.254370979,
              "end_ns": 292480482129749,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 427225088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 60.56655146445371,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.052787379,
                "rss_peak_bytes": 1185824768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.257,
                "predicted_n": 18,
                "predicted_per_second": 95.36792384029799,
                "predicted_per_token_ms": 10.485705882352942
              },
              "ttft_s": 0.076061872,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292480560220686,
              "complete": true,
              "e2e_s": 0.428901801,
              "end_ns": 292480989122487,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 482914304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 98.29231843395391,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050229995,
                "rss_peak_bytes": 1241518080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 289.678,
                "predicted_n": 29,
                "predicted_per_second": 96.65904901304208,
                "predicted_per_token_ms": 10.345642857142858
              },
              "ttft_s": 0.139179517,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292481064222069,
              "complete": true,
              "e2e_s": 3.307342774,
              "end_ns": 292484371564843,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483364864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 878.7724781327549,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.05203862,
                "rss_peak_bytes": 1241968640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.765,
                "predicted_n": 16,
                "predicted_per_second": 94.47926180203446,
                "predicted_per_token_ms": 10.584333333333332
              },
              "ttft_s": 3.148550672,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292484445076789,
              "complete": true,
              "e2e_s": 0.719806125,
              "end_ns": 292485164882914,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483397632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 183.97925917403754,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.054510656,
                "rss_peak_bytes": 1242001408,
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
              "ttft_s": 0.719671856
            },
            {
              "begin_ns": 292485243117294,
              "complete": true,
              "e2e_s": 1.36906553,
              "end_ns": 292486612182824,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 430702592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 357.81791634063575,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.05259856,
                "rss_peak_bytes": 1189306368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.271,
                "predicted_n": 128,
                "predicted_per_second": 97.00054457786051,
                "predicted_per_token_ms": 10.309220472440945
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.05968545
            },
            {
              "begin_ns": 292486765756813,
              "complete": true,
              "e2e_s": 0.775639326,
              "end_ns": 292487541396139,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483426304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 191.3164166805527,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.050790778,
                "rss_peak_bytes": 1242030080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.975,
                "predicted_n": 34,
                "predicted_per_second": 95.93720473871646,
                "predicted_per_token_ms": 10.423484848484849
              },
              "tool_call_valid": true,
              "ttft_s": 0.527961977,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292487647118824,
              "complete": true,
              "e2e_s": 0.824275399,
              "end_ns": 292488471394223,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483459072,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6143082496,
                "gpu_energy_j": 204.81738247485694,
                "gpu_owned_peak_bytes": 5888802816,
                "max_sample_gap_s": 0.053431095,
                "rss_peak_bytes": 1242062848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.313,
                "predicted_n": 25,
                "predicted_per_second": 96.26453494202067,
                "predicted_per_token_ms": 10.388041666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.574931082,
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
          "gpu_j_per_correct_token": 26.555330290695743,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772427776,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7570.637680132492,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.076058985,
              "rss_peak_bytes": 11997437952,
              "swap_peak_bytes": 315392
            },
            {
              "anon_peak_bytes": 772689920,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7194.12596149434,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.081545768,
              "rss_peak_bytes": 12138999808,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14764.763641626832,
          "raw_requests": [
            {
              "begin_ns": 292199644926102,
              "complete": true,
              "e2e_s": 0.467155562,
              "end_ns": 292200112081664,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 611979264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.43933188769655,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051400092,
                "rss_peak_bytes": 1150160896,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.629,
                "predicted_n": 10,
                "predicted_per_second": 34.26887358212535,
                "predicted_per_token_ms": 29.181
              },
              "ttft_s": 0.204505452,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292200175072321,
              "complete": true,
              "e2e_s": 0.573395428,
              "end_ns": 292200748467749,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 611979264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 137.7308622090496,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050599406,
                "rss_peak_bytes": 1150226432,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.637,
                "predicted_n": 14,
                "predicted_per_second": 34.98037063048082,
                "predicted_per_token_ms": 28.58746153846154
              },
              "ttft_s": 0.201755483,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292200811110384,
              "complete": true,
              "e2e_s": 1.761473969,
              "end_ns": 292202572584353,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 611979264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 467.8997911074802,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052039422,
                "rss_peak_bytes": 1150464000,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.861,
                "predicted_n": 45,
                "predicted_per_second": 35.4306963500746,
                "predicted_per_token_ms": 28.22411363636364
              },
              "ttft_s": 0.519565258,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292202645139362,
              "complete": true,
              "e2e_s": 0.990182367,
              "end_ns": 292203635321729,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 614952960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 257.5252785044986,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051341376,
                "rss_peak_bytes": 1153916928,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.089,
                "predicted_n": 28,
                "predicted_per_second": 35.290012011674456,
                "predicted_per_token_ms": 28.33662962962963
              },
              "ttft_s": 0.225073032,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292203694188609,
              "complete": true,
              "e2e_s": 0.842691236,
              "end_ns": 292204536879845,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 614952960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 219.71093123899945,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05081029,
                "rss_peak_bytes": 1154113536,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.622,
                "predicted_n": 23,
                "predicted_per_second": 35.33444047913501,
                "predicted_per_token_ms": 28.301
              },
              "ttft_s": 0.220043373,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292204604295470,
              "complete": true,
              "e2e_s": 1.142959607,
              "end_ns": 292205747255077,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 771866624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 287.45505454283574,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050889042,
                "rss_peak_bytes": 1311260672,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 790.78,
                "predicted_n": 29,
                "predicted_per_second": 35.408078100103694,
                "predicted_per_token_ms": 28.242142857142856
              },
              "ttft_s": 0.35212688,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292205810253902,
              "complete": true,
              "e2e_s": 3.775464862,
              "end_ns": 292209585718764,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772329472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1001.0607555912482,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055815446,
                "rss_peak_bytes": 1311723520,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.99,
                "predicted_n": 21,
                "predicted_per_second": 34.4833531612614,
                "predicted_per_token_ms": 28.9995
              },
              "ttft_s": 3.195377009,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292209653201312,
              "complete": true,
              "e2e_s": 0.718675096,
              "end_ns": 292210371876408,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615464960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.99397873894122,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053160246,
                "rss_peak_bytes": 1154859008,
                "swap_peak_bytes": 249856
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
              "ttft_s": 0.71854756
            },
            {
              "begin_ns": 292210433563629,
              "complete": true,
              "e2e_s": 3.772122008,
              "end_ns": 292214205685637,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615464960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1039.2064041237459,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05219599,
                "rss_peak_bytes": 1154859008,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3578.514,
                "predicted_n": 128,
                "predicted_per_second": 35.48959148965185,
                "predicted_per_token_ms": 28.177275590551183
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193505511
            },
            {
              "begin_ns": 292214276191485,
              "complete": true,
              "e2e_s": 1.70110751,
              "end_ns": 292215977298995,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772390912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 459.47357699315546,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052541581,
                "rss_peak_bytes": 1311784960,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.473,
                "predicted_n": 34,
                "predicted_per_second": 35.126076002184206,
                "predicted_per_token_ms": 28.468878787878786
              },
              "tool_call_valid": true,
              "ttft_s": 1.025443094,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292216049106188,
              "complete": true,
              "e2e_s": 1.774817558,
              "end_ns": 292217823923746,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772427776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 454.16804479957233,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055238805,
                "rss_peak_bytes": 1311821824,
                "swap_peak_bytes": 249856
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.746,
                "predicted_n": 25,
                "predicted_per_second": 35.20372690122127,
                "predicted_per_token_ms": 28.40608333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093064001,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292403706226287,
              "complete": true,
              "e2e_s": 0.467427879,
              "end_ns": 292404173654166,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612294656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.85692525969547,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050143864,
                "rss_peak_bytes": 1255870464,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.344,
                "predicted_n": 10,
                "predicted_per_second": 34.306101911993416,
                "predicted_per_token_ms": 29.14933333333333
              },
              "ttft_s": 0.205066929,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292404242732082,
              "complete": true,
              "e2e_s": 0.574751758,
              "end_ns": 292404817483840,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612294656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 147.85980529370588,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050657093,
                "rss_peak_bytes": 1255870464,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.292,
                "predicted_n": 14,
                "predicted_per_second": 35.01287396442692,
                "predicted_per_token_ms": 28.560923076923075
              },
              "ttft_s": 0.20348934,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292404885731441,
              "complete": true,
              "e2e_s": 1.766308212,
              "end_ns": 292406652039653,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612294656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 475.3690483069332,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.054591302,
                "rss_peak_bytes": 1255907328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1243.381,
                "predicted_n": 45,
                "predicted_per_second": 35.38738327190137,
                "predicted_per_token_ms": 28.25865909090909
              },
              "ttft_s": 0.522873473,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292406726717847,
              "complete": true,
              "e2e_s": 0.993340023,
              "end_ns": 292407720057870,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 265.8046163696251,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050737108,
                "rss_peak_bytes": 1259208704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.21,
                "predicted_n": 28,
                "predicted_per_second": 35.28443172462461,
                "predicted_per_token_ms": 28.34111111111111
              },
              "ttft_s": 0.228117297,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292407789751704,
              "complete": true,
              "e2e_s": 0.846025261,
              "end_ns": 292408635776965,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 223.27971518157787,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051304593,
                "rss_peak_bytes": 1259208704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 625.338,
                "predicted_n": 23,
                "predicted_per_second": 35.180974129190936,
                "predicted_per_token_ms": 28.424454545454545
              },
              "ttft_s": 0.220701783,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292408713028741,
              "complete": true,
              "e2e_s": 1.147261061,
              "end_ns": 292409860289802,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772182016,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 293.6153679663801,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050843409,
                "rss_peak_bytes": 1416122368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.203,
                "predicted_n": 29,
                "predicted_per_second": 35.34447610019149,
                "predicted_per_token_ms": 28.292964285714284
              },
              "ttft_s": 0.355067176,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292409940706511,
              "complete": true,
              "e2e_s": 3.794414653,
              "end_ns": 292413735121164,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772612096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1015.7345687745724,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.074994174,
                "rss_peak_bytes": 1416552448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.876,
                "predicted_n": 21,
                "predicted_per_second": 34.43075630599302,
                "predicted_per_token_ms": 29.043799999999997
              },
              "ttft_s": 3.213533954,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292413807176142,
              "complete": true,
              "e2e_s": 0.725091091,
              "end_ns": 292414532267233,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615739392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 188.4545344859548,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053640627,
                "rss_peak_bytes": 1259679744,
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
              "ttft_s": 0.724942946
            },
            {
              "begin_ns": 292414636174963,
              "complete": true,
              "e2e_s": 3.777736938,
              "end_ns": 292418413911901,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615739392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1062.3798412811466,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055267767,
                "rss_peak_bytes": 1259679744,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3584.725,
                "predicted_n": 128,
                "predicted_per_second": 35.42810117930943,
                "predicted_per_token_ms": 28.226181102362204
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193019645
            },
            {
              "begin_ns": 292418481745289,
              "complete": true,
              "e2e_s": 1.705331136,
              "end_ns": 292420187076425,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772653056,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 461.9786925098092,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052930595,
                "rss_peak_bytes": 1416593408,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 941.375,
                "predicted_n": 34,
                "predicted_per_second": 35.05510556367016,
                "predicted_per_token_ms": 28.526515151515152
              },
              "tool_call_valid": true,
              "ttft_s": 1.027532192,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292420262090541,
              "complete": true,
              "e2e_s": 1.77562279,
              "end_ns": 292422037713331,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772689920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 464.73525702934916,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053349659,
                "rss_peak_bytes": 1416630272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.756,
                "predicted_n": 25,
                "predicted_per_second": 35.10024043664699,
                "predicted_per_token_ms": 28.489833333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091840331,
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
          "gpu_j_per_correct_token": 43.24622079676478,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 804134912,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12927369216,
              "gpu_energy_j": 11951.94722524291,
              "gpu_owned_peak_bytes": 12673089536,
              "max_sample_gap_s": 0.077134511,
              "rss_peak_bytes": 12139220992,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 803999744,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12927369216,
              "gpu_energy_j": 12092.95153775831,
              "gpu_owned_peak_bytes": 12673089536,
              "max_sample_gap_s": 0.071399263,
              "rss_peak_bytes": 12139028480,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 24044.89876300122,
          "raw_requests": [
            {
              "begin_ns": 292259964336993,
              "complete": true,
              "e2e_s": 0.466146439,
              "end_ns": 292260430483432,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 741806080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 107.66888111596212,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.050390555,
                "rss_peak_bytes": 1314807808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.053,
                "predicted_n": 10,
                "predicted_per_second": 34.344197547824294,
                "predicted_per_token_ms": 29.117
              },
              "ttft_s": 0.204042064,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292260500179220,
              "complete": true,
              "e2e_s": 0.574340827,
              "end_ns": 292261074520047,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640753664,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 139.33169321070426,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.052116221,
                "rss_peak_bytes": 1213755392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.375,
                "predicted_n": 14,
                "predicted_per_second": 35.0995612554843,
                "predicted_per_token_ms": 28.490384615384617
              },
              "ttft_s": 0.203855347,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292261140693881,
              "complete": true,
              "e2e_s": 1.821824684,
              "end_ns": 292262962518565,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 797650944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 477.6588171581978,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.053517046,
                "rss_peak_bytes": 1370771456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1238.605,
                "predicted_n": 45,
                "predicted_per_second": 35.523835282434675,
                "predicted_per_token_ms": 28.15011363636364
              },
              "ttft_s": 0.583137463,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292263029067238,
              "complete": true,
              "e2e_s": 0.990652057,
              "end_ns": 292264019719295,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640757760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 262.68800184452647,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.050888322,
                "rss_peak_bytes": 1213878272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 761.403,
                "predicted_n": 28,
                "predicted_per_second": 35.46085318812771,
                "predicted_per_token_ms": 28.200111111111113
              },
              "ttft_s": 0.22920572,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292264086135786,
              "complete": true,
              "e2e_s": 0.843345305,
              "end_ns": 292264929481091,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640757760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 222.11986673893438,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.050766284,
                "rss_peak_bytes": 1213878272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 621.543,
                "predicted_n": 23,
                "predicted_per_second": 35.39578114466738,
                "predicted_per_token_ms": 28.251954545454545
              },
              "ttft_s": 0.22177222,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292264997332895,
              "complete": true,
              "e2e_s": 1.27604541,
              "end_ns": 292266273378305,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 801849344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 307.77180549064235,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.052108247,
                "rss_peak_bytes": 1375703040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.933,
                "predicted_n": 29,
                "predicted_per_second": 35.35652637281184,
                "predicted_per_token_ms": 28.28332142857143
              },
              "ttft_s": 0.484040076,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292266342609263,
              "complete": true,
              "e2e_s": 14.132169221,
              "end_ns": 292280474778484,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 804057088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 3607.323577921639,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.055984079,
                "rss_peak_bytes": 1377976320,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 576.687,
                "predicted_n": 21,
                "predicted_per_second": 34.68085807379046,
                "predicted_per_token_ms": 28.83435
              },
              "ttft_s": 13.555429493,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292280540307949,
              "complete": true,
              "e2e_s": 2.991569179,
              "end_ns": 292283531877128,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 804085760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 749.8188722423741,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.054264915,
                "rss_peak_bytes": 1378004992,
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
              "ttft_s": 2.991448472
            },
            {
              "begin_ns": 292283586067364,
              "complete": true,
              "e2e_s": 3.775053078,
              "end_ns": 292287361120442,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 647188480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 1050.3737774138501,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.072911932,
                "rss_peak_bytes": 1221107712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3571.238,
                "predicted_n": 128,
                "predicted_per_second": 35.56189758285502,
                "predicted_per_token_ms": 28.119984251968503
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.203686122
            },
            {
              "begin_ns": 292287428327161,
              "complete": true,
              "e2e_s": 2.630442555,
              "end_ns": 292290058769716,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 804098048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 682.9330461295401,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.05543092,
                "rss_peak_bytes": 1378017280,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.394,
                "predicted_n": 34,
                "predicted_per_second": 35.20398039671686,
                "predicted_per_token_ms": 28.405878787878788
              },
              "tool_call_valid": true,
              "ttft_s": 1.955779873,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292290131189598,
              "complete": true,
              "e2e_s": 3.076971638,
              "end_ns": 292293208161236,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 804134912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 782.0641197027159,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.056856358,
                "rss_peak_bytes": 1374183424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.777,
                "predicted_n": 25,
                "predicted_per_second": 35.15056892660415,
                "predicted_per_token_ms": 28.44904166666667
              },
              "tool_facts_valid": true,
              "ttft_s": 2.39411271,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 292334175651530,
              "complete": true,
              "e2e_s": 0.467902087,
              "end_ns": 292334643553617,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640782336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 111.23945502125926,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.05161982,
                "rss_peak_bytes": 1239068672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.071,
                "predicted_n": 10,
                "predicted_per_second": 34.341838662041965,
                "predicted_per_token_ms": 29.119000000000003
              },
              "ttft_s": 0.205799672,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292334711032032,
              "complete": true,
              "e2e_s": 0.572782087,
              "end_ns": 292335283814119,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640782336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 142.21824810763974,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.052677474,
                "rss_peak_bytes": 1239068672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.669,
                "predicted_n": 14,
                "predicted_per_second": 35.07172167081682,
                "predicted_per_token_ms": 28.512999999999998
              },
              "ttft_s": 0.202087584,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292335351157220,
              "complete": true,
              "e2e_s": 1.82572063,
              "end_ns": 292337176877850,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 797679616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 489.6487110494775,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.055941453,
                "rss_peak_bytes": 1395965952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1246.307,
                "predicted_n": 45,
                "predicted_per_second": 35.30430303288034,
                "predicted_per_token_ms": 28.325159090909093
              },
              "ttft_s": 0.579340671,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292337249783393,
              "complete": true,
              "e2e_s": 0.995092827,
              "end_ns": 292338244876220,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640786432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 265.236482587738,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.053824493,
                "rss_peak_bytes": 1239072768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.415,
                "predicted_n": 28,
                "predicted_per_second": 35.36739519134416,
                "predicted_per_token_ms": 28.27462962962963
              },
              "ttft_s": 0.231646101,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292338311525594,
              "complete": true,
              "e2e_s": 0.846334141,
              "end_ns": 292339157859735,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 640786432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 227.18828511604224,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.050416315,
                "rss_peak_bytes": 1239072768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.611,
                "predicted_n": 23,
                "predicted_per_second": 35.33506475150616,
                "predicted_per_token_ms": 28.3005
              },
              "ttft_s": 0.223696965,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292339227795393,
              "complete": true,
              "e2e_s": 1.277748234,
              "end_ns": 292340505543627,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 801755136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 310.390293276894,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.054592702,
                "rss_peak_bytes": 1400659968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 793.132,
                "predicted_n": 29,
                "predicted_per_second": 35.30307691531801,
                "predicted_per_token_ms": 28.326142857142855
              },
              "ttft_s": 0.48457671,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292340577201892,
              "complete": true,
              "e2e_s": 14.12817127,
              "end_ns": 292354705373162,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 803930112,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 3684.786211308086,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.05496782,
                "rss_peak_bytes": 1402834944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 577.003,
                "predicted_n": 21,
                "predicted_per_second": 34.66186484299041,
                "predicted_per_token_ms": 28.850150000000003
              },
              "ttft_s": 13.551166488,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292354774533677,
              "complete": true,
              "e2e_s": 2.986946579,
              "end_ns": 292357761480256,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 803954688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 764.5224411945339,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.051959967,
                "rss_peak_bytes": 1402859520,
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
              "ttft_s": 2.986816319
            },
            {
              "begin_ns": 292357819305068,
              "complete": true,
              "e2e_s": 3.784377667,
              "end_ns": 292361603682735,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 647057408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 1061.9128736591178,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.063663603,
                "rss_peak_bytes": 1245962240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3583.405,
                "predicted_n": 128,
                "predicted_per_second": 35.44115164208343,
                "predicted_per_token_ms": 28.215787401574804
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.20088036
            },
            {
              "begin_ns": 292361674471940,
              "complete": true,
              "e2e_s": 2.637444438,
              "end_ns": 292364311916378,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 803966976,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 682.8534695866239,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.052915845,
                "rss_peak_bytes": 1402871808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.202,
                "predicted_n": 34,
                "predicted_per_second": 35.13621137944766,
                "predicted_per_token_ms": 28.46066666666667
              },
              "tool_call_valid": true,
              "ttft_s": 1.961044086,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292364388606192,
              "complete": true,
              "e2e_s": 3.025680028,
              "end_ns": 292367414286220,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 803999744,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 784.7920561702912,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.054963341,
                "rss_peak_bytes": 1402904576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 680.946,
                "predicted_n": 25,
                "predicted_per_second": 35.24508551338873,
                "predicted_per_token_ms": 28.37275
              },
              "tool_facts_valid": true,
              "ttft_s": 2.344612453,
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
