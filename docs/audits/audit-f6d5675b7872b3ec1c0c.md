# Public audit excerpt

Original SHA256: `f6d5675b7872b3ec1c0cf3019c3a8927bc7468885e82f0fb739f3d87540f8a5b`

Original file: `RESULTS.json`; 266344 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.981501661557568,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 370237440,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2904.799116462137,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.194987126,
              "rss_peak_bytes": 7527342080,
              "swap_peak_bytes": 177537024
            },
            {
              "anon_peak_bytes": 470315008,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2704.8048173332163,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.058869995,
              "rss_peak_bytes": 7726972928,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5609.603933795353,
          "raw_requests": [
            {
              "begin_ns": 297318984629067,
              "complete": true,
              "e2e_s": 0.216654568,
              "end_ns": 297319201283635,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 270905344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 40.47518317397676,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051810736,
                "rss_peak_bytes": 1307693056,
                "swap_peak_bytes": 143224832
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 121.018,
                "predicted_n": 10,
                "predicted_per_second": 74.36910211704044,
                "predicted_per_token_ms": 13.446444444444445
              },
              "ttft_s": 0.090587031,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297319257189671,
              "complete": true,
              "e2e_s": 0.258385623,
              "end_ns": 297319515575294,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 271343616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 57.5821506535794,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050634496,
                "rss_peak_bytes": 1308131328,
                "swap_peak_bytes": 142991360
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 169.236,
                "predicted_n": 14,
                "predicted_per_second": 76.8158075114042,
                "predicted_per_token_ms": 13.018153846153846
              },
              "ttft_s": 0.084737945,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297319567743409,
              "complete": true,
              "e2e_s": 0.707945191,
              "end_ns": 297320275688600,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 272228352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 176.8924308787231,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051548154,
                "rss_peak_bytes": 1309192192,
                "swap_peak_bytes": 141901824
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 544.717,
                "predicted_n": 44,
                "predicted_per_second": 78.94007346934279,
                "predicted_per_token_ms": 12.667837209302325
              },
              "ttft_s": 0.156857254,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297320342078403,
              "complete": true,
              "e2e_s": 0.391126668,
              "end_ns": 297320733205071,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 273154048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 90.25661435321626,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050629352,
                "rss_peak_bytes": 1310117888,
                "swap_peak_bytes": 140984320
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 283.351,
                "predicted_n": 23,
                "predicted_per_second": 77.6422176029024,
                "predicted_per_token_ms": 12.87959090909091
              },
              "ttft_s": 0.10111583,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297320789178821,
              "complete": true,
              "e2e_s": 0.322680475,
              "end_ns": 297321111859296,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 273756160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 71.3984484198886,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050444967,
                "rss_peak_bytes": 1310507008,
                "swap_peak_bytes": 140374016
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 217.421,
                "predicted_n": 18,
                "predicted_per_second": 78.1893193389783,
                "predicted_per_token_ms": 12.789470588235293
              },
              "ttft_s": 0.100564221,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297321168167935,
              "complete": true,
              "e2e_s": 0.498876556,
              "end_ns": 297321667044491,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 330006528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 119.82534958045997,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050886807,
                "rss_peak_bytes": 1366888448,
                "swap_peak_bytes": 139837440
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 356.467,
                "predicted_n": 29,
                "predicted_per_second": 78.5486454566622,
                "predicted_per_token_ms": 12.730964285714284
              },
              "ttft_s": 0.139648589,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297321732217697,
              "complete": true,
              "e2e_s": 1.091685271,
              "end_ns": 297322823902968,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 330842112,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 284.34920843573474,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054046119,
                "rss_peak_bytes": 1367724032,
                "swap_peak_bytes": 139452416
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.852,
                "predicted_n": 21,
                "predicted_per_second": 77.86585270895303,
                "predicted_per_token_ms": 12.8426
              },
              "ttft_s": 0.830984493,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297322883251296,
              "complete": true,
              "e2e_s": 0.196687865,
              "end_ns": 297323079939161,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 278228992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 47.617391995118396,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050101552,
                "rss_peak_bytes": 1315110912,
                "swap_peak_bytes": 139386880
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
              "ttft_s": 0.196529436
            },
            {
              "begin_ns": 297323134087702,
              "complete": true,
              "e2e_s": 1.657985449,
              "end_ns": 297324792073151,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 278245376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.1058515383069,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051171771,
                "rss_peak_bytes": 1315127296,
                "swap_peak_bytes": 139378688
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.19,
                "predicted_n": 128,
                "predicted_per_second": 79.6143406114632,
                "predicted_per_token_ms": 12.560551181102362
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062578467
            },
            {
              "begin_ns": 297324846893345,
              "complete": true,
              "e2e_s": 0.618554689,
              "end_ns": 297325465448034,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 330977280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 159.62667403955632,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053741961,
                "rss_peak_bytes": 1367859200,
                "swap_peak_bytes": 139366400
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.491,
                "predicted_n": 34,
                "predicted_per_second": 78.85474239589382,
                "predicted_per_token_ms": 12.681545454545454
              },
              "tool_call_valid": true,
              "ttft_s": 0.316431715,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297325527290818,
              "complete": true,
              "e2e_s": 0.557969594,
              "end_ns": 297326085260412,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331014144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 137.53042781138564,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052567049,
                "rss_peak_bytes": 1367896064,
                "swap_peak_bytes": 139362304
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.03,
                "predicted_n": 25,
                "predicted_per_second": 78.93957833108576,
                "predicted_per_token_ms": 12.667916666666665
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253946325,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297779852653741,
              "complete": true,
              "e2e_s": 0.182528992,
              "end_ns": 297780035182733,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.51120276127695,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05012223,
                "rss_peak_bytes": 1471365120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.537,
                "predicted_n": 10,
                "predicted_per_second": 77.2286913169208,
                "predicted_per_token_ms": 12.948555555555556
              },
              "ttft_s": 0.065969619,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297780113182415,
              "complete": true,
              "e2e_s": 0.233610612,
              "end_ns": 297780346793027,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.490587375508966,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050622501,
                "rss_peak_bytes": 1471365120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.464,
                "predicted_n": 14,
                "predicted_per_second": 78.09496347558631,
                "predicted_per_token_ms": 12.804923076923076
              },
              "ttft_s": 0.067121236,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297780424067393,
              "complete": true,
              "e2e_s": 0.66586125,
              "end_ns": 297781089928643,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.0857261465059,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050247156,
                "rss_peak_bytes": 1471410176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.166,
                "predicted_n": 44,
                "predicted_per_second": 79.31150238118951,
                "predicted_per_token_ms": 12.608511627906978
              },
              "ttft_s": 0.123691087,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297781165667569,
              "complete": true,
              "e2e_s": 0.358708029,
              "end_ns": 297781524375598,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414064640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 89.29397137517324,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051921594,
                "rss_peak_bytes": 1471414272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.659,
                "predicted_n": 23,
                "predicted_per_second": 78.94954047778826,
                "predicted_per_token_ms": 12.666318181818182
              },
              "ttft_s": 0.080003186,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297781601217306,
              "complete": true,
              "e2e_s": 0.294961375,
              "end_ns": 297781896178681,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 68.43242572204043,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05205332,
                "rss_peak_bytes": 1471418368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.111,
                "predicted_n": 18,
                "predicted_per_second": 78.66327951839564,
                "predicted_per_token_ms": 12.712411764705882
              },
              "ttft_s": 0.078816558,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297781974672643,
              "complete": true,
              "e2e_s": 0.469023296,
              "end_ns": 297782443695939,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469762048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.52516835449597,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052108223,
                "rss_peak_bytes": 1527111680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.314,
                "predicted_n": 29,
                "predicted_per_second": 79.02594873473811,
                "predicted_per_token_ms": 12.654071428571429
              },
              "ttft_s": 0.114688951,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297782519154685,
              "complete": true,
              "e2e_s": 1.074480434,
              "end_ns": 297783593635119,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470233088,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 286.79919351804165,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056687241,
                "rss_peak_bytes": 1527582720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 255.495,
                "predicted_n": 21,
                "predicted_per_second": 78.27941838392141,
                "predicted_per_token_ms": 12.774750000000001
              },
              "ttft_s": 0.818912787,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297783678405077,
              "complete": true,
              "e2e_s": 0.197841849,
              "end_ns": 297783876246926,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.87145836821503,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050039372,
                "rss_peak_bytes": 1474920448,
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
              "ttft_s": 0.197685465
            },
            {
              "begin_ns": 297783940642455,
              "complete": true,
              "e2e_s": 1.658050911,
              "end_ns": 297785598693366,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417570816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 448.18712472526903,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050858061,
                "rss_peak_bytes": 1474920448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.033,
                "predicted_n": 128,
                "predicted_per_second": 79.62217709602247,
                "predicted_per_token_ms": 12.559314960629921
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062842694
            },
            {
              "begin_ns": 297785678160688,
              "complete": true,
              "e2e_s": 0.618214552,
              "end_ns": 297786296375240,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470286336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 156.96576299473293,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05245433,
                "rss_peak_bytes": 1527635968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.654,
                "predicted_n": 34,
                "predicted_per_second": 79.01277133703975,
                "predicted_per_token_ms": 12.656181818181818
              },
              "tool_call_valid": true,
              "ttft_s": 0.317069483,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297786383076379,
              "complete": true,
              "e2e_s": 0.562918085,
              "end_ns": 297786945994464,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470315008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 145.5129784038997,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05317621,
                "rss_peak_bytes": 1527664640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 307.306,
                "predicted_n": 25,
                "predicted_per_second": 78.0980521044171,
                "predicted_per_token_ms": 12.804416666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255607967,
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
          "gpu_j_per_correct_token": 10.24733911288802,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470122496,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7575437312,
              "gpu_energy_j": 2657.6714006052807,
              "gpu_owned_peak_bytes": 7321157632,
              "max_sample_gap_s": 0.08813582,
              "rss_peak_bytes": 7727607808,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 367177728,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7575437312,
              "gpu_energy_j": 3101.3331808377857,
              "gpu_owned_peak_bytes": 7321157632,
              "max_sample_gap_s": 0.121821429,
              "rss_peak_bytes": 7161692160,
              "swap_peak_bytes": 188649472
            }
          ],
          "lifecycle_gpu_j": 5759.004581443067,
          "raw_requests": [
            {
              "begin_ns": 297348934304126,
              "complete": true,
              "e2e_s": 0.181704366,
              "end_ns": 297349116008492,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 413863936,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 42.31827258212607,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050096768,
                "rss_peak_bytes": 1467650048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.111,
                "predicted_n": 10,
                "predicted_per_second": 77.51203589668506,
                "predicted_per_token_ms": 12.901222222222223
              },
              "ttft_s": 0.065572708,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297349176600101,
              "complete": true,
              "e2e_s": 0.233845609,
              "end_ns": 297349410445710,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 413863936,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 55.40052185680379,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050045402,
                "rss_peak_bytes": 1467650048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.84,
                "predicted_n": 14,
                "predicted_per_second": 78.38880849011095,
                "predicted_per_token_ms": 12.756923076923076
              },
              "ttft_s": 0.067954434,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297349468110755,
              "complete": true,
              "e2e_s": 0.666256662,
              "end_ns": 297350134367417,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 413863936,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 175.49609750197365,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.051266987,
                "rss_peak_bytes": 1467695104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.893,
                "predicted_n": 44,
                "predicted_per_second": 79.35145868280269,
                "predicted_per_token_ms": 12.602162790697674
              },
              "ttft_s": 0.124378385,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297350196890460,
              "complete": true,
              "e2e_s": 0.356673192,
              "end_ns": 297350553563652,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 413872128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 89.49355200487807,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050682267,
                "rss_peak_bytes": 1467703296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.185,
                "predicted_n": 23,
                "predicted_per_second": 79.084062763988,
                "predicted_per_token_ms": 12.644772727272727
              },
              "ttft_s": 0.078430765,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297350614890000,
              "complete": true,
              "e2e_s": 0.303629021,
              "end_ns": 297350918519021,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 413872128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 72.49436080273907,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.053561975,
                "rss_peak_bytes": 1467703296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 224.94,
                "predicted_n": 18,
                "predicted_per_second": 75.57570907797636,
                "predicted_per_token_ms": 13.231764705882354
              },
              "ttft_s": 0.078519357,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297350985463423,
              "complete": true,
              "e2e_s": 0.47136218,
              "end_ns": 297351456825603,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469565440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 118.42268937351028,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.051477044,
                "rss_peak_bytes": 1523396608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.935,
                "predicted_n": 29,
                "predicted_per_second": 79.11057115006993,
                "predicted_per_token_ms": 12.640535714285715
              },
              "ttft_s": 0.117376204,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297351527012050,
              "complete": true,
              "e2e_s": 1.075023938,
              "end_ns": 297352602035988,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470036480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 285.67720290953866,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.057250221,
                "rss_peak_bytes": 1523867648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.247,
                "predicted_n": 21,
                "predicted_per_second": 78.04969424032281,
                "predicted_per_token_ms": 12.81235
              },
              "ttft_s": 0.818728404,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297352664118298,
              "complete": true,
              "e2e_s": 0.196765139,
              "end_ns": 297352860883437,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417374208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 48.52817298766781,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050372767,
                "rss_peak_bytes": 1471205376,
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
              "ttft_s": 0.196629806
            },
            {
              "begin_ns": 297352917638924,
              "complete": true,
              "e2e_s": 1.655399163,
              "end_ns": 297354573038087,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417374208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 441.1395845718806,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.052613547,
                "rss_peak_bytes": 1471205376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1592.671,
                "predicted_n": 128,
                "predicted_per_second": 79.74026022951381,
                "predicted_per_token_ms": 12.540716535433072
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062595912
            },
            {
              "begin_ns": 297354644212936,
              "complete": true,
              "e2e_s": 0.6173497,
              "end_ns": 297355261562636,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470085632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 160.65172511989138,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050848404,
                "rss_peak_bytes": 1523916800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.347,
                "predicted_n": 34,
                "predicted_per_second": 79.07089304583477,
                "predicted_per_token_ms": 12.646878787878787
              },
              "tool_call_valid": true,
              "ttft_s": 0.31610804,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297355328621558,
              "complete": true,
              "e2e_s": 0.558929193,
              "end_ns": 297355887550751,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470122496,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 138.3417595853533,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050174321,
                "rss_peak_bytes": 1523953664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.306,
                "predicted_n": 25,
                "predicted_per_second": 78.86798157118164,
                "predicted_per_token_ms": 12.679416666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254645182,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297749332168430,
              "complete": true,
              "e2e_s": 0.225056052,
              "end_ns": 297749557224482,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264249344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 39.48000247006466,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.055948186,
                "rss_peak_bytes": 911495168,
                "swap_peak_bytes": 149635072
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 121.156,
                "predicted_n": 10,
                "predicted_per_second": 74.28439367427119,
                "predicted_per_token_ms": 13.461777777777778
              },
              "ttft_s": 0.098175042,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297749632173460,
              "complete": true,
              "e2e_s": 0.263082723,
              "end_ns": 297749895256183,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264716288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 57.248309196344856,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050060182,
                "rss_peak_bytes": 912093184,
                "swap_peak_bytes": 149147648
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.995,
                "predicted_n": 14,
                "predicted_per_second": 77.84664211503338,
                "predicted_per_token_ms": 12.845769230769232
              },
              "ttft_s": 0.090306341,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297749976759433,
              "complete": true,
              "e2e_s": 0.72064031,
              "end_ns": 297750697399743,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 265691136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 182.20016006097399,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050140629,
                "rss_peak_bytes": 913702912,
                "swap_peak_bytes": 148242432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 548.638,
                "predicted_n": 44,
                "predicted_per_second": 78.37590542397719,
                "predicted_per_token_ms": 12.759023255813954
              },
              "ttft_s": 0.165538864,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 297750777170421,
              "complete": true,
              "e2e_s": 0.414232197,
              "end_ns": 297751191402618,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 266776576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 96.38693485046183,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050719663,
                "rss_peak_bytes": 915247104,
                "swap_peak_bytes": 147251200
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 280.327,
                "predicted_n": 23,
                "predicted_per_second": 78.47977540515184,
                "predicted_per_token_ms": 12.742136363636364
              },
              "ttft_s": 0.125295938,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297751267552550,
              "complete": true,
              "e2e_s": 0.321930284,
              "end_ns": 297751589482834,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 267497472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 78.48481699210205,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050085187,
                "rss_peak_bytes": 916164608,
                "swap_peak_bytes": 146989056
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 217.358,
                "predicted_n": 18,
                "predicted_per_second": 78.21198207565398,
                "predicted_per_token_ms": 12.785764705882354
              },
              "ttft_s": 0.099016119,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297751665438707,
              "complete": true,
              "e2e_s": 0.514730114,
              "end_ns": 297752180168821,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 323911680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 120.92821285231683,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.051254822,
                "rss_peak_bytes": 973103104,
                "swap_peak_bytes": 146288640
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 357.064,
                "predicted_n": 29,
                "predicted_per_second": 78.4173145430511,
                "predicted_per_token_ms": 12.752285714285716
              },
              "ttft_s": 0.15199796,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297752259942128,
              "complete": true,
              "e2e_s": 1.104339187,
              "end_ns": 297753364281315,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 324792320,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 293.6380834529209,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.06070019,
                "rss_peak_bytes": 974311424,
                "swap_peak_bytes": 145416192
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 259.144,
                "predicted_n": 21,
                "predicted_per_second": 77.1771679066465,
                "predicted_per_token_ms": 12.9572
              },
              "ttft_s": 0.838900697,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297753443344715,
              "complete": true,
              "e2e_s": 0.197400939,
              "end_ns": 297753640745654,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 272154624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 48.552281891962096,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.053068346,
                "rss_peak_bytes": 921673728,
                "swap_peak_bytes": 145149952
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
              "ttft_s": 0.197268074
            },
            {
              "begin_ns": 297753706969390,
              "complete": true,
              "e2e_s": 1.657303743,
              "end_ns": 297755364273133,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 272166912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 445.76917983103573,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.050876284,
                "rss_peak_bytes": 921686016,
                "swap_peak_bytes": 145141760
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.447,
                "predicted_n": 128,
                "predicted_per_second": 79.6514402799215,
                "predicted_per_token_ms": 12.554700787401574
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062805638
            },
            {
              "begin_ns": 297755438126212,
              "complete": true,
              "e2e_s": 0.618434789,
              "end_ns": 297756056561001,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 324890624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 163.9035795899362,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.05717441,
                "rss_peak_bytes": 974409728,
                "swap_peak_bytes": 145133568
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.199,
                "predicted_n": 34,
                "predicted_per_second": 79.09894319018022,
                "predicted_per_token_ms": 12.64239393939394
              },
              "tool_call_valid": true,
              "ttft_s": 0.31736639,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297756139900704,
              "complete": true,
              "e2e_s": 0.560721683,
              "end_ns": 297756700622387,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 324935680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7575437312,
                "gpu_energy_j": 145.96511063904592,
                "gpu_owned_peak_bytes": 7321157632,
                "max_sample_gap_s": 0.054003397,
                "rss_peak_bytes": 974454784,
                "swap_peak_bytes": 145129472
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.557,
                "predicted_n": 25,
                "predicted_per_second": 78.80298269289491,
                "predicted_per_token_ms": 12.689875
              },
              "tool_facts_valid": true,
              "ttft_s": 0.256122977,
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
          "gpu_j_per_correct_token": 8.865079123797099,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475996160,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2235.3643388335217,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.066497551,
              "rss_peak_bytes": 5997391872,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476049408,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2569.508546264505,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.161217696,
              "rss_peak_bytes": 5538942976,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4804.872885098027,
          "raw_requests": [
            {
              "begin_ns": 297400585172408,
              "complete": true,
              "e2e_s": 0.156030385,
              "end_ns": 297400741202793,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.45005350318626,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053379185,
                "rss_peak_bytes": 1216274432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.522,
                "predicted_n": 10,
                "predicted_per_second": 94.21913276522686,
                "predicted_per_token_ms": 10.613555555555557
              },
              "ttft_s": 0.060459041,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297400799165800,
              "complete": true,
              "e2e_s": 0.148281466,
              "end_ns": 297400947447266,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.874457081946424,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050075173,
                "rss_peak_bytes": 1216274432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.48,
                "predicted_n": 9,
                "predicted_per_second": 93.58914365933552,
                "predicted_per_token_ms": 10.685
              },
              "ttft_s": 0.062797266,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297401005151624,
              "complete": true,
              "e2e_s": 0.526090765,
              "end_ns": 297401531242389,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.62506173801043,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050522144,
                "rss_peak_bytes": 1216319488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.152,
                "predicted_n": 39,
                "predicted_per_second": 96.40950699222634,
                "predicted_per_token_ms": 10.372421052631578
              },
              "ttft_s": 0.131873362,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297401613211248,
              "complete": true,
              "e2e_s": 0.306417326,
              "end_ns": 297401919628574,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.34222240791877,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050869233,
                "rss_peak_bytes": 1219354624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.418,
                "predicted_n": 23,
                "predicted_per_second": 95.89482952514624,
                "predicted_per_token_ms": 10.42809090909091
              },
              "ttft_s": 0.077012542,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297401985161624,
              "complete": true,
              "e2e_s": 0.254023743,
              "end_ns": 297402239185367,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.61156979520064,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052174688,
                "rss_peak_bytes": 1219354624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.084,
                "predicted_n": 18,
                "predicted_per_second": 95.46056916960535,
                "predicted_per_token_ms": 10.475529411764706
              },
              "ttft_s": 0.075866604,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297402320161966,
              "complete": true,
              "e2e_s": 0.397198844,
              "end_ns": 297402717360810,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475496448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 92.61324461811341,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05126544,
                "rss_peak_bytes": 1272070144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.231,
                "predicted_n": 29,
                "predicted_per_second": 96.47487690839365,
                "predicted_per_token_ms": 10.365392857142856
              },
              "ttft_s": 0.106936706,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297402781199812,
              "complete": true,
              "e2e_s": 1.029229237,
              "end_ns": 297403810429049,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475926528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 270.8752157885587,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053781526,
                "rss_peak_bytes": 1272500224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.507,
                "predicted_n": 16,
                "predicted_per_second": 94.03976001053246,
                "predicted_per_token_ms": 10.6338
              },
              "ttft_s": 0.869719407,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297403873768369,
              "complete": true,
              "e2e_s": 0.204037677,
              "end_ns": 297404077806046,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.29827175774371,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050691118,
                "rss_peak_bytes": 1219817472,
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
              "ttft_s": 0.203901976
            },
            {
              "begin_ns": 297404135180387,
              "complete": true,
              "e2e_s": 1.365532412,
              "end_ns": 297405500712799,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 347.2572039590556,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054387249,
                "rss_peak_bytes": 1219817472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1307.827,
                "predicted_n": 128,
                "predicted_per_second": 97.10764497139147,
                "predicted_per_token_ms": 10.297850393700788
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057612168
            },
            {
              "begin_ns": 297405568175316,
              "complete": true,
              "e2e_s": 0.550399476,
              "end_ns": 297406118574792,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475955200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.9692435563313,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055183701,
                "rss_peak_bytes": 1272528896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.174,
                "predicted_n": 34,
                "predicted_per_second": 96.1611310880195,
                "predicted_per_token_ms": 10.39921212121212
              },
              "tool_call_valid": true,
              "ttft_s": 0.302812379,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297406181571970,
              "complete": true,
              "e2e_s": 0.522832895,
              "end_ns": 297406704404865,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475996160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.76432397011922,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052238899,
                "rss_peak_bytes": 1272569856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.161,
                "predicted_n": 25,
                "predicted_per_second": 95.93821578903186,
                "predicted_per_token_ms": 10.423375
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272651429,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297682949758616,
              "complete": true,
              "e2e_s": 0.156952375,
              "end_ns": 297683106710991,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.79341972010362,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055443099,
                "rss_peak_bytes": 804077568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.914,
                "predicted_n": 10,
                "predicted_per_second": 93.83405967846195,
                "predicted_per_token_ms": 10.657111111111112
              },
              "ttft_s": 0.061017518,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297683176511845,
              "complete": true,
              "e2e_s": 0.149518909,
              "end_ns": 297683326030754,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 33.02173426509527,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.049969696,
                "rss_peak_bytes": 804536320,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.55,
                "predicted_n": 9,
                "predicted_per_second": 93.51256575102279,
                "predicted_per_token_ms": 10.69375
              },
              "ttft_s": 0.063943255,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297683405064767,
              "complete": true,
              "e2e_s": 0.528688913,
              "end_ns": 297683933753680,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.88372131301864,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050944163,
                "rss_peak_bytes": 805892096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 396.542,
                "predicted_n": 39,
                "predicted_per_second": 95.82843683645112,
                "predicted_per_token_ms": 10.435315789473684
              },
              "ttft_s": 0.13218242,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297684046756589,
              "complete": true,
              "e2e_s": 0.307877469,
              "end_ns": 297684354634058,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.0849296528301,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052646864,
                "rss_peak_bytes": 802844672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 230.238,
                "predicted_n": 23,
                "predicted_per_second": 95.55329702308046,
                "predicted_per_token_ms": 10.465363636363636
              },
              "ttft_s": 0.077651134,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297684432136402,
              "complete": true,
              "e2e_s": 0.254407474,
              "end_ns": 297684686543876,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.982053641122256,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052102889,
                "rss_peak_bytes": 803827712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.175,
                "predicted_n": 18,
                "predicted_per_second": 95.41181422758524,
                "predicted_per_token_ms": 10.480882352941178
              },
              "ttft_s": 0.07619665,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297684757718349,
              "complete": true,
              "e2e_s": 0.398245854,
              "end_ns": 297685155964203,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475496448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 89.7896004638131,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055657824,
                "rss_peak_bytes": 857522176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.202,
                "predicted_n": 29,
                "predicted_per_second": 96.1531857610868,
                "predicted_per_token_ms": 10.400071428571428
              },
              "ttft_s": 0.107046082,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297685230436157,
              "complete": true,
              "e2e_s": 1.030203389,
              "end_ns": 297686260639546,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475959296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 275.7194655033938,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056006202,
                "rss_peak_bytes": 858312704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.724,
                "predicted_n": 16,
                "predicted_per_second": 93.91199819688964,
                "predicted_per_token_ms": 10.648266666666666
              },
              "ttft_s": 0.870496578,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297686329565427,
              "complete": true,
              "e2e_s": 0.204702554,
              "end_ns": 297686534267981,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423288832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 50.85720424006515,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055981712,
                "rss_peak_bytes": 805642240,
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
              "ttft_s": 0.204572719
            },
            {
              "begin_ns": 297686603116276,
              "complete": true,
              "e2e_s": 1.370346974,
              "end_ns": 297687973463250,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423288832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 350.06122242355593,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05213431,
                "rss_peak_bytes": 805642240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1312.55,
                "predicted_n": 128,
                "predicted_per_second": 96.7582187345244,
                "predicted_per_token_ms": 10.33503937007874
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057666868
            },
            {
              "begin_ns": 297688044124796,
              "complete": true,
              "e2e_s": 0.549683886,
              "end_ns": 297688593808682,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476004352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.84620330019268,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052229536,
                "rss_peak_bytes": 858423296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.209,
                "predicted_n": 34,
                "predicted_per_second": 96.15132470302352,
                "predicted_per_token_ms": 10.400272727272727
              },
              "tool_call_valid": true,
              "ttft_s": 0.302793258,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297688678215123,
              "complete": true,
              "e2e_s": 0.525216759,
              "end_ns": 297689203431882,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476049408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.91954699121322,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055765097,
                "rss_peak_bytes": 858468352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 251.088,
                "predicted_n": 25,
                "predicted_per_second": 95.58401835213152,
                "predicted_per_token_ms": 10.462
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27410845,
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
          "gpu_j_per_correct_token": 8.458382400903345,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475758592,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6107430912,
              "gpu_energy_j": 2278.9983028220213,
              "gpu_owned_peak_bytes": 5853151232,
              "max_sample_gap_s": 0.058594448,
              "rss_peak_bytes": 5996064768,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 475770880,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6107430912,
              "gpu_energy_j": 2305.4449584675917,
              "gpu_owned_peak_bytes": 5853151232,
              "max_sample_gap_s": 0.072110045,
              "rss_peak_bytes": 5996949504,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4584.443261289613,
          "raw_requests": [
            {
              "begin_ns": 297376399975651,
              "complete": true,
              "e2e_s": 0.155897306,
              "end_ns": 297376555872957,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419536896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 31.960737055397292,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050352939,
                "rss_peak_bytes": 1211617280,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.518,
                "predicted_n": 10,
                "predicted_per_second": 94.22307837266275,
                "predicted_per_token_ms": 10.613111111111111
              },
              "ttft_s": 0.060317306,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297376614948740,
              "complete": true,
              "e2e_s": 0.148537514,
              "end_ns": 297376763486254,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419536896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 27.380008501042212,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.049979088,
                "rss_peak_bytes": 1211617280,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.158,
                "predicted_n": 9,
                "predicted_per_second": 93.94302355621315,
                "predicted_per_token_ms": 10.64475
              },
              "ttft_s": 0.063286591,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297376829100775,
              "complete": true,
              "e2e_s": 0.526678505,
              "end_ns": 297377355779280,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419536896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 132.37182012837715,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.051678424,
                "rss_peak_bytes": 1211662336,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.998,
                "predicted_n": 39,
                "predicted_per_second": 96.44719008725933,
                "predicted_per_token_ms": 10.368368421052631
              },
              "ttft_s": 0.132635101,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297377417179838,
              "complete": true,
              "e2e_s": 0.30563204,
              "end_ns": 297377722811878,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422502400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 71.95657065698842,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050011219,
                "rss_peak_bytes": 1214038016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.685,
                "predicted_n": 23,
                "predicted_per_second": 96.20219953210749,
                "predicted_per_token_ms": 10.394772727272727
              },
              "ttft_s": 0.076906211,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297377785087702,
              "complete": true,
              "e2e_s": 0.253761324,
              "end_ns": 297378038849026,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422502400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 60.347874328428034,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050666592,
                "rss_peak_bytes": 1214038016,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.934,
                "predicted_n": 18,
                "predicted_per_second": 95.54104330819294,
                "predicted_per_token_ms": 10.46670588235294
              },
              "ttft_s": 0.075760752,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297378117400227,
              "complete": true,
              "e2e_s": 0.397899126,
              "end_ns": 297378515299353,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475213824,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 91.94235406515975,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050146597,
                "rss_peak_bytes": 1266749440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.22,
                "predicted_n": 29,
                "predicted_per_second": 96.14724263443445,
                "predicted_per_token_ms": 10.400714285714287
              },
              "ttft_s": 0.106618143,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297378580143567,
              "complete": true,
              "e2e_s": 1.02625398,
              "end_ns": 297379606397547,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475676672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 274.1995510949312,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.053269463,
                "rss_peak_bytes": 1267212288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.351,
                "predicted_n": 16,
                "predicted_per_second": 94.13182220381422,
                "predicted_per_token_ms": 10.6234
              },
              "ttft_s": 0.866864796,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297379667276585,
              "complete": true,
              "e2e_s": 0.204030552,
              "end_ns": 297379871307137,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475676672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 50.10103698664841,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.051260346,
                "rss_peak_bytes": 1267212288,
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
              "ttft_s": 0.203895882
            },
            {
              "begin_ns": 297379936436563,
              "complete": true,
              "e2e_s": 1.365411536,
              "end_ns": 297381301848099,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422993920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 347.3566043318625,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.053385079,
                "rss_peak_bytes": 1214529536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.23,
                "predicted_n": 128,
                "predicted_per_second": 97.07773098002644,
                "predicted_per_token_ms": 10.301023622047245
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057049615
            },
            {
              "begin_ns": 297381379503488,
              "complete": true,
              "e2e_s": 0.548474432,
              "end_ns": 297381927977920,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475717632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 138.50058561346432,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050646889,
                "rss_peak_bytes": 1267253248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.148,
                "predicted_n": 34,
                "predicted_per_second": 96.16841712613798,
                "predicted_per_token_ms": 10.398424242424243
              },
              "tool_call_valid": true,
              "ttft_s": 0.301662859,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297382013199449,
              "complete": true,
              "e2e_s": 0.523109333,
              "end_ns": 297382536308782,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475758592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 125.87704735462174,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050668941,
                "rss_peak_bytes": 1267294208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.822,
                "predicted_n": 25,
                "predicted_per_second": 96.06840070129931,
                "predicted_per_token_ms": 10.40925
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273274558,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297708059895051,
              "complete": true,
              "e2e_s": 0.157326291,
              "end_ns": 297708217221342,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419565568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 32.025138018548816,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050373099,
                "rss_peak_bytes": 1211441152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.343,
                "predicted_n": 10,
                "predicted_per_second": 94.39602278090683,
                "predicted_per_token_ms": 10.593666666666667
              },
              "ttft_s": 0.061984952,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297708294190537,
              "complete": true,
              "e2e_s": 0.148477599,
              "end_ns": 297708442668136,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419565568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 31.75527543602127,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050408538,
                "rss_peak_bytes": 1211441152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.092,
                "predicted_n": 9,
                "predicted_per_second": 94.0158886851878,
                "predicted_per_token_ms": 10.6365
              },
              "ttft_s": 0.063343837,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 297708517552142,
              "complete": true,
              "e2e_s": 0.526285558,
              "end_ns": 297709043837700,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419565568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 130.57380501069346,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050609094,
                "rss_peak_bytes": 1211486208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.785,
                "predicted_n": 39,
                "predicted_per_second": 96.49935878715542,
                "predicted_per_token_ms": 10.362763157894738
              },
              "ttft_s": 0.132453199,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 297709127618548,
              "complete": true,
              "e2e_s": 0.306477693,
              "end_ns": 297709434096241,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422535168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 73.19116951778047,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050215358,
                "rss_peak_bytes": 1214521344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.395,
                "predicted_n": 23,
                "predicted_per_second": 95.90444429913468,
                "predicted_per_token_ms": 10.427045454545455
              },
              "ttft_s": 0.077076229,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 297709507951857,
              "complete": true,
              "e2e_s": 0.254059573,
              "end_ns": 297709762011430,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422535168,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 55.459329489233184,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.05022527,
                "rss_peak_bytes": 1214521344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.835,
                "predicted_n": 18,
                "predicted_per_second": 95.59423060702336,
                "predicted_per_token_ms": 10.460882352941177
              },
              "ttft_s": 0.076192781,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 297709843151966,
              "complete": true,
              "e2e_s": 0.398171639,
              "end_ns": 297710241323605,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475250688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 93.70973682615912,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050675958,
                "rss_peak_bytes": 1267236864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.267,
                "predicted_n": 29,
                "predicted_per_second": 96.13172793347685,
                "predicted_per_token_ms": 10.402392857142857
              },
              "ttft_s": 0.106805909,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297710313214111,
              "complete": true,
              "e2e_s": 1.030506285,
              "end_ns": 297711343720396,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475676672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 272.51604007030846,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.057718487,
                "rss_peak_bytes": 1267662848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.998,
                "predicted_n": 16,
                "predicted_per_second": 93.75117188964863,
                "predicted_per_token_ms": 10.666533333333332
              },
              "ttft_s": 0.870483577,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 297711415196708,
              "complete": true,
              "e2e_s": 0.204533199,
              "end_ns": 297711619729907,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 436068352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 50.509504656474114,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.050542427,
                "rss_peak_bytes": 1228054528,
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
              "ttft_s": 0.204406476
            },
            {
              "begin_ns": 297711682148096,
              "complete": true,
              "e2e_s": 1.367209184,
              "end_ns": 297713049357280,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423014400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 350.2100025139349,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.05133857,
                "rss_peak_bytes": 1215000576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.402,
                "predicted_n": 128,
                "predicted_per_second": 96.99084009341668,
                "predicted_per_token_ms": 10.310251968503938
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057709469
            },
            {
              "begin_ns": 297713127864293,
              "complete": true,
              "e2e_s": 0.55264215,
              "end_ns": 297713680506443,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475729920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 139.79201685422626,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.051540843,
                "rss_peak_bytes": 1267716096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.261,
                "predicted_n": 34,
                "predicted_per_second": 96.1367589094013,
                "predicted_per_token_ms": 10.401848484848486
              },
              "tool_call_valid": true,
              "ttft_s": 0.305305887,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297713768093296,
              "complete": true,
              "e2e_s": 0.524550976,
              "end_ns": 297714292644272,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475770880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6107430912,
                "gpu_energy_j": 130.32941339255956,
                "gpu_owned_peak_bytes": 5853151232,
                "max_sample_gap_s": 0.056193143,
                "rss_peak_bytes": 1267757056,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.888,
                "predicted_n": 25,
                "predicted_per_second": 95.66021491661617,
                "predicted_per_token_ms": 10.453666666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273604346,
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
          "gpu_j_per_correct_token": 26.448326483767442,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772689920,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7590.759590218841,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.099696629,
              "rss_peak_bytes": 11714760704,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772718592,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7114.509934755857,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.080361681,
              "rss_peak_bytes": 12140077056,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14705.269524974698,
          "raw_requests": [
            {
              "begin_ns": 297469084812874,
              "complete": true,
              "e2e_s": 0.475629243,
              "end_ns": 297469560442117,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612298752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 102.93179970703991,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050574394,
                "rss_peak_bytes": 861495296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 261.982,
                "predicted_n": 10,
                "predicted_per_second": 34.353505202647504,
                "predicted_per_token_ms": 29.109111111111115
              },
              "ttft_s": 0.213617446,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297469628104787,
              "complete": true,
              "e2e_s": 0.575382934,
              "end_ns": 297470203487721,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612298752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.8244704213749,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051871815,
                "rss_peak_bytes": 861929472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.729,
                "predicted_n": 14,
                "predicted_per_second": 35.066045548095786,
                "predicted_per_token_ms": 28.517615384615382
              },
              "ttft_s": 0.204620825,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297470286210594,
              "complete": true,
              "e2e_s": 1.763768739,
              "end_ns": 297472049979333,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612298752,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 464.94429698901826,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.055852519,
                "rss_peak_bytes": 862674944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.794,
                "predicted_n": 45,
                "predicted_per_second": 35.46116438345124,
                "predicted_per_token_ms": 28.199863636363638
              },
              "ttft_s": 0.522937894,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 297472139828481,
              "complete": true,
              "e2e_s": 1.001776648,
              "end_ns": 297473141605129,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 254.55158526278746,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051206874,
                "rss_peak_bytes": 866562048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 767.766,
                "predicted_n": 28,
                "predicted_per_second": 35.166964934628524,
                "predicted_per_token_ms": 28.435777777777776
              },
              "ttft_s": 0.23395317,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 297473205747225,
              "complete": true,
              "e2e_s": 0.857106639,
              "end_ns": 297474062853864,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 221.2845034355359,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05440338,
                "rss_peak_bytes": 867364864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.994,
                "predicted_n": 23,
                "predicted_per_second": 35.256749263614715,
                "predicted_per_token_ms": 28.363363636363637
              },
              "ttft_s": 0.233046926,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 297474143492908,
              "complete": true,
              "e2e_s": 1.15601014,
              "end_ns": 297475299503048,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772190208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 288.5283351711725,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053525982,
                "rss_peak_bytes": 1024733184,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 793.606,
                "predicted_n": 29,
                "predicted_per_second": 35.28199131558985,
                "predicted_per_token_ms": 28.343071428571427
              },
              "ttft_s": 0.362375733,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297475368307350,
              "complete": true,
              "e2e_s": 3.776510441,
              "end_ns": 297479144817791,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772620288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1006.432371742254,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055683315,
                "rss_peak_bytes": 1025265664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.513,
                "predicted_n": 21,
                "predicted_per_second": 34.51173657881704,
                "predicted_per_token_ms": 28.97565
              },
              "ttft_s": 3.196887755,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297479215144482,
              "complete": true,
              "e2e_s": 0.719292727,
              "end_ns": 297479934437209,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 710107136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 191.10327836738998,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051111528,
                "rss_peak_bytes": 962752512,
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
              "ttft_s": 0.719122263
            },
            {
              "begin_ns": 297479997152496,
              "complete": true,
              "e2e_s": 3.773721818,
              "end_ns": 297483770874314,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615739392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1031.140267267835,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052476044,
                "rss_peak_bytes": 868384768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3577.105,
                "predicted_n": 128,
                "predicted_per_second": 35.50357062484886,
                "predicted_per_token_ms": 28.166181102362206
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196527257
            },
            {
              "begin_ns": 297483843150000,
              "complete": true,
              "e2e_s": 1.701401515,
              "end_ns": 297485544551515,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772661248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 441.17745991915206,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055145311,
                "rss_peak_bytes": 1025306624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.471,
                "predicted_n": 34,
                "predicted_per_second": 35.12615078059887,
                "predicted_per_token_ms": 28.468818181818182
              },
              "tool_call_valid": true,
              "ttft_s": 1.024806711,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297485634185952,
              "complete": true,
              "e2e_s": 1.774338559,
              "end_ns": 297487408524511,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772689920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 456.2650798462454,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050684803,
                "rss_peak_bytes": 1025335296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.879,
                "predicted_n": 25,
                "predicted_per_second": 35.145318570347015,
                "predicted_per_token_ms": 28.45329166666667
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091459126,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297633768154859,
              "complete": true,
              "e2e_s": 0.464842444,
              "end_ns": 297634232997303,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 107.84825404144209,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050880045,
                "rss_peak_bytes": 1257586688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.615,
                "predicted_n": 10,
                "predicted_per_second": 34.27070045503874,
                "predicted_per_token_ms": 29.179444444444446
              },
              "ttft_s": 0.202196854,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297634303112510,
              "complete": true,
              "e2e_s": 0.573195046,
              "end_ns": 297634876307556,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 138.94766798436694,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051005131,
                "rss_peak_bytes": 1257586688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.975,
                "predicted_n": 14,
                "predicted_per_second": 35.04279264101354,
                "predicted_per_token_ms": 28.536538461538463
              },
              "ttft_s": 0.202198335,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297634944074023,
              "complete": true,
              "e2e_s": 1.759882639,
              "end_ns": 297636703956662,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 473.9884210016736,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052791821,
                "rss_peak_bytes": 1257586688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.024,
                "predicted_n": 45,
                "predicted_per_second": 35.48318419643491,
                "predicted_per_token_ms": 28.182363636363633
              },
              "ttft_s": 0.519870886,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 297636796206488,
              "complete": true,
              "e2e_s": 0.989406611,
              "end_ns": 297637785613099,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 263.7169154344175,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050661022,
                "rss_peak_bytes": 1260883968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.306,
                "predicted_n": 28,
                "predicted_per_second": 35.3724456508923,
                "predicted_per_token_ms": 28.270592592592592
              },
              "ttft_s": 0.226097516,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 297637856237812,
              "complete": true,
              "e2e_s": 0.847526121,
              "end_ns": 297638703763933,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 219.19423580731484,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05072419,
                "rss_peak_bytes": 1260883968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.503,
                "predicted_n": 23,
                "predicted_per_second": 35.28451346665533,
                "predicted_per_token_ms": 28.341045454545455
              },
              "ttft_s": 0.223973106,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 297638774710028,
              "complete": true,
              "e2e_s": 1.148316186,
              "end_ns": 297639923026214,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772173824,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 292.66786781064087,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055444891,
                "rss_peak_bytes": 1417797632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 794.552,
                "predicted_n": 29,
                "predicted_per_second": 35.239984293035576,
                "predicted_per_token_ms": 28.376857142857144
              },
              "ttft_s": 0.353723567,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297639995320891,
              "complete": true,
              "e2e_s": 3.784247693,
              "end_ns": 297643779568584,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772636672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1009.52543961883,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.059313469,
                "rss_peak_bytes": 1418260480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.079,
                "predicted_n": 21,
                "predicted_per_second": 34.47806247080139,
                "predicted_per_token_ms": 29.003949999999996
              },
              "ttft_s": 3.204064144,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297643853862166,
              "complete": true,
              "e2e_s": 0.723272437,
              "end_ns": 297644577134603,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615768064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 189.93860326254526,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05041613,
                "rss_peak_bytes": 1261391872,
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
              "ttft_s": 0.723113042
            },
            {
              "begin_ns": 297644633536661,
              "complete": true,
              "e2e_s": 3.776387908,
              "end_ns": 297648409924569,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615768064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1040.8445286216634,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053407115,
                "rss_peak_bytes": 1261391872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3580.581,
                "predicted_n": 128,
                "predicted_per_second": 35.469104036467826,
                "predicted_per_token_ms": 28.193551181102364
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195752257
            },
            {
              "begin_ns": 297648517230066,
              "complete": true,
              "e2e_s": 1.70948059,
              "end_ns": 297650226710656,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772681728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 461.2744762759629,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053358013,
                "rss_peak_bytes": 1418305536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 943.283,
                "predicted_n": 34,
                "predicted_per_second": 34.9841988035404,
                "predicted_per_token_ms": 28.584333333333333
              },
              "tool_call_valid": true,
              "ttft_s": 1.033184719,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297650311664896,
              "complete": true,
              "e2e_s": 1.775919046,
              "end_ns": 297652087583942,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772718592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 459.20346510615553,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051046907,
                "rss_peak_bytes": 1418342400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.765,
                "predicted_n": 25,
                "predicted_per_second": 35.15118671870995,
                "predicted_per_token_ms": 28.448541666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093086758,
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
          "gpu_j_per_correct_token": 25.500641928977025,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772489216,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12784762880,
              "gpu_energy_j": 7052.564019413468,
              "gpu_owned_peak_bytes": 12530483200,
              "max_sample_gap_s": 0.087816798,
              "rss_peak_bytes": 12139982848,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772476928,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12784762880,
              "gpu_energy_j": 7125.792893097759,
              "gpu_owned_peak_bytes": 12530483200,
              "max_sample_gap_s": 0.066677662,
              "rss_peak_bytes": 12140146688,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14178.356912511226,
          "raw_requests": [
            {
              "begin_ns": 297525177978895,
              "complete": true,
              "e2e_s": 0.468256207,
              "end_ns": 297525646235102,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612052992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 107.78238940808541,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.050804807,
                "rss_peak_bytes": 1249251328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.637,
                "predicted_n": 10,
                "predicted_per_second": 34.267829742191694,
                "predicted_per_token_ms": 29.18188888888889
              },
              "ttft_s": 0.205620791,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297525711931076,
              "complete": true,
              "e2e_s": 0.571900506,
              "end_ns": 297526283831582,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612052992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 138.75017919546144,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.050066961,
                "rss_peak_bytes": 1249251328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.411,
                "predicted_n": 14,
                "predicted_per_second": 35.096149952350224,
                "predicted_per_token_ms": 28.493153846153845
              },
              "ttft_s": 0.201476833,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297526353039513,
              "complete": true,
              "e2e_s": 1.761472899,
              "end_ns": 297528114512412,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612052992,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 469.85634150542796,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.052283232,
                "rss_peak_bytes": 1249251328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.291,
                "predicted_n": 45,
                "predicted_per_second": 35.41843255726718,
                "predicted_per_token_ms": 28.233886363636362
              },
              "ttft_s": 0.519152212,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 297528183321656,
              "complete": true,
              "e2e_s": 0.985799065,
              "end_ns": 297529169120721,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615026688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 260.4436298960124,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.050699476,
                "rss_peak_bytes": 1205755904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 761.69,
                "predicted_n": 28,
                "predicted_per_second": 35.44749176174034,
                "predicted_per_token_ms": 28.210740740740743
              },
              "ttft_s": 0.224052203,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 297529239018448,
              "complete": true,
              "e2e_s": 0.844872706,
              "end_ns": 297530083891154,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615026688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 220.81297683924075,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.051257251,
                "rss_peak_bytes": 1205755904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.0,
                "predicted_n": 23,
                "predicted_per_second": 35.369774919614144,
                "predicted_per_token_ms": 28.272727272727273
              },
              "ttft_s": 0.222838214,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 297530153142769,
              "complete": true,
              "e2e_s": 1.147622099,
              "end_ns": 297531300764868,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 771948544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 287.4210236021593,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.053032972,
                "rss_peak_bytes": 1362677760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 789.867,
                "predicted_n": 29,
                "predicted_per_second": 35.449005971891474,
                "predicted_per_token_ms": 28.209535714285714
              },
              "ttft_s": 0.35773836,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297531378339844,
              "complete": true,
              "e2e_s": 3.774413686,
              "end_ns": 297535152753530,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772411392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 1008.5198509765928,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.059563355,
                "rss_peak_bytes": 1363140608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 582.748,
                "predicted_n": 21,
                "predicted_per_second": 34.320152106914136,
                "predicted_per_token_ms": 29.137400000000003
              },
              "ttft_s": 3.191633616,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297535232300409,
              "complete": true,
              "e2e_s": 0.722351711,
              "end_ns": 297535954652120,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615538688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 180.91891202241214,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.052717238,
                "rss_peak_bytes": 1206267904,
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
              "ttft_s": 0.722225188
            },
            {
              "begin_ns": 297536014164969,
              "complete": true,
              "e2e_s": 3.764407248,
              "end_ns": 297539778572217,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615538688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 1039.0922834076841,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.054391475,
                "rss_peak_bytes": 1206267904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3570.234,
                "predicted_n": 128,
                "predicted_per_second": 35.57189808847263,
                "predicted_per_token_ms": 28.11207874015748
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194089982
            },
            {
              "begin_ns": 297539847042678,
              "complete": true,
              "e2e_s": 1.699075728,
              "end_ns": 297541546118406,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772452352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 443.3061543890767,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.055857437,
                "rss_peak_bytes": 1363181568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.101,
                "predicted_n": 34,
                "predicted_per_second": 35.214987498679434,
                "predicted_per_token_ms": 28.397
              },
              "tool_call_valid": true,
              "ttft_s": 1.024584213,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297541624114232,
              "complete": true,
              "e2e_s": 1.771857467,
              "end_ns": 297543395971699,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772489216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 454.8509793213339,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.053400331,
                "rss_peak_bytes": 1363218432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 680.85,
                "predicted_n": 25,
                "predicted_per_second": 35.25005507821106,
                "predicted_per_token_ms": 28.368750000000002
              },
              "tool_facts_valid": true,
              "ttft_s": 1.09103535,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 297579398091390,
              "complete": true,
              "e2e_s": 0.464395776,
              "end_ns": 297579862487166,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612048896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 105.23330410125541,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.05107302,
                "rss_peak_bytes": 1253240832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.335,
                "predicted_n": 10,
                "predicted_per_second": 34.307278860998345,
                "predicted_per_token_ms": 29.14833333333333
              },
              "ttft_s": 0.202062515,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 297579930989602,
              "complete": true,
              "e2e_s": 0.578450803,
              "end_ns": 297580509440405,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612048896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 145.17379992638575,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.055153407,
                "rss_peak_bytes": 1253240832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 375.357,
                "predicted_n": 14,
                "predicted_per_second": 34.63369538865666,
                "predicted_per_token_ms": 28.873615384615388
              },
              "ttft_s": 0.20306124,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 297580580102526,
              "complete": true,
              "e2e_s": 1.759739027,
              "end_ns": 297582339841553,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612048896,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12782665728,
                "gpu_energy_j": 475.1262072082399,
                "gpu_owned_peak_bytes": 12528386048,
                "max_sample_gap_s": 0.051668523,
                "rss_peak_bytes": 1253240832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.362,
                "predicted_n": 45,
                "predicted_per_second": 35.473514989978725,
                "predicted_per_token_ms": 28.190045454545455
              },
              "ttft_s": 0.519398964,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 297582409853378,
              "complete": true,
              "e2e_s": 0.987289049,
              "end_ns": 297583397142427,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615022592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 262.77215778568996,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.055674741,
                "rss_peak_bytes": 1256538112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.726,
                "predicted_n": 28,
                "predicted_per_second": 35.35299308914453,
                "predicted_per_token_ms": 28.286148148148147
              },
              "ttft_s": 0.223567268,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 297583468283400,
              "complete": true,
              "e2e_s": 0.845430721,
              "end_ns": 297584313714121,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615022592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 224.75454732250694,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.052771971,
                "rss_peak_bytes": 1256538112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.225,
                "predicted_n": 23,
                "predicted_per_second": 35.300252717718315,
                "predicted_per_token_ms": 28.32840909090909
              },
              "ttft_s": 0.222178719,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 297584385104444,
              "complete": true,
              "e2e_s": 1.143780741,
              "end_ns": 297585528885185,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 771936256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 295.7395729566664,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.051709499,
                "rss_peak_bytes": 1413451776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 790.97,
                "predicted_n": 29,
                "predicted_per_second": 35.39957267658697,
                "predicted_per_token_ms": 28.24892857142857
              },
              "ttft_s": 0.35277138,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 297585598117433,
              "complete": true,
              "e2e_s": 3.782507609,
              "end_ns": 297589380625042,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772399104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 1016.628847605639,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.059867623,
                "rss_peak_bytes": 1413914624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.177,
                "predicted_n": 21,
                "predicted_per_second": 34.53175799453362,
                "predicted_per_token_ms": 28.95885
              },
              "ttft_s": 3.20330888,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 297589450726828,
              "complete": true,
              "e2e_s": 0.719779202,
              "end_ns": 297590170506030,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615522304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 184.7132702239477,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.052059521,
                "rss_peak_bytes": 1257037824,
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
              "ttft_s": 0.719650421
            },
            {
              "begin_ns": 297590232210449,
              "complete": true,
              "e2e_s": 3.768768203,
              "end_ns": 297594000978652,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615522304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 1038.465274179192,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.054599129,
                "rss_peak_bytes": 1257037824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3573.277,
                "predicted_n": 128,
                "predicted_per_second": 35.54160508687124,
                "predicted_per_token_ms": 28.13603937007874
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195364816
            },
            {
              "begin_ns": 297594074179638,
              "complete": true,
              "e2e_s": 1.700726679,
              "end_ns": 297595774906317,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772440064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 459.8779041574696,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.051416025,
                "rss_peak_bytes": 1413955584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.646,
                "predicted_n": 34,
                "predicted_per_second": 35.1945190402348,
                "predicted_per_token_ms": 28.41351515151515
              },
              "tool_call_valid": true,
              "ttft_s": 1.026058616,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 297595854012118,
              "complete": true,
              "e2e_s": 1.773229004,
              "end_ns": 297597627241122,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772476928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12784762880,
                "gpu_energy_j": 467.61715034835646,
                "gpu_owned_peak_bytes": 12530483200,
                "max_sample_gap_s": 0.052479407,
                "rss_peak_bytes": 1413992448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 679.507,
                "predicted_n": 25,
                "predicted_per_second": 35.31972444728311,
                "predicted_per_token_ms": 28.312791666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093667317,
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
