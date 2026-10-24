# Public audit excerpt

Original SHA256: `2c2821ca804984cdab2a7ab86c5fbd039bd8cd2df81463922715af53be77e03e`

Original file: `RESULTS.json`; 266278 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.553750399160007,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470335488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2654.43694294568,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.226336806,
              "rss_peak_bytes": 7727886336,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470347776,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2714.7707813822435,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.058414313,
              "rss_peak_bytes": 7725948928,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5369.207724327924,
          "raw_requests": [
            {
              "begin_ns": 288843931307135,
              "complete": true,
              "e2e_s": 0.187750775,
              "end_ns": 288844119057910,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 43.13344661156598,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052122809,
                "rss_peak_bytes": 1473536000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.797,
                "predicted_n": 10,
                "predicted_per_second": 77.05677371850304,
                "predicted_per_token_ms": 12.977444444444444
              },
              "ttft_s": 0.071025982,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288844178852656,
              "complete": true,
              "e2e_s": 0.234077314,
              "end_ns": 288844412929970,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 57.741032705678606,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050095709,
                "rss_peak_bytes": 1473536000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.745,
                "predicted_n": 14,
                "predicted_per_second": 77.96335722210561,
                "predicted_per_token_ms": 12.826538461538462
              },
              "ttft_s": 0.067312782,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288844464310319,
              "complete": true,
              "e2e_s": 0.665813992,
              "end_ns": 288845130124311,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 174.32076272014405,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050936735,
                "rss_peak_bytes": 1473589248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.815,
                "predicted_n": 44,
                "predicted_per_second": 79.36288216457646,
                "predicted_per_token_ms": 12.600348837209303
              },
              "ttft_s": 0.123946432,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288845186127114,
              "complete": true,
              "e2e_s": 0.357763972,
              "end_ns": 288845543891086,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 84.93412334899857,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051084813,
                "rss_peak_bytes": 1473593344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.99,
                "predicted_n": 23,
                "predicted_per_second": 78.85587297035735,
                "predicted_per_token_ms": 12.681363636363637
              },
              "ttft_s": 0.078731332,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288845595034414,
              "complete": true,
              "e2e_s": 0.295113535,
              "end_ns": 288845890147949,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414081024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 68.13088537403642,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050234712,
                "rss_peak_bytes": 1473597440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.01,
                "predicted_n": 18,
                "predicted_per_second": 78.70006018239897,
                "predicted_per_token_ms": 12.706470588235293
              },
              "ttft_s": 0.07904299,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288845947131117,
              "complete": true,
              "e2e_s": 0.469437343,
              "end_ns": 288846416568460,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469774336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 116.80289584984656,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050655215,
                "rss_peak_bytes": 1529290752,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.692,
                "predicted_n": 29,
                "predicted_per_second": 78.9417297260722,
                "predicted_per_token_ms": 12.66757142857143
              },
              "ttft_s": 0.114672332,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288846470787298,
              "complete": true,
              "e2e_s": 1.075118948,
              "end_ns": 288847545906246,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470245376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 287.9282146719122,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056600794,
                "rss_peak_bytes": 1529761792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.241,
                "predicted_n": 21,
                "predicted_per_second": 78.05152180954649,
                "predicted_per_token_ms": 12.81205
              },
              "ttft_s": 0.818842326,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288847599889035,
              "complete": true,
              "e2e_s": 0.19699057,
              "end_ns": 288847796879605,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417583104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 45.80426684944115,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050220498,
                "rss_peak_bytes": 1477099520,
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
              "ttft_s": 0.196853811
            },
            {
              "begin_ns": 288847847303865,
              "complete": true,
              "e2e_s": 1.656531853,
              "end_ns": 288849503835718,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417583104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 445.0688213241297,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051278822,
                "rss_peak_bytes": 1477099520,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1593.647,
                "predicted_n": 128,
                "predicted_per_second": 79.6914247634514,
                "predicted_per_token_ms": 12.54840157480315
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062786036
            },
            {
              "begin_ns": 288849563338858,
              "complete": true,
              "e2e_s": 0.617197707,
              "end_ns": 288850180536565,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470298624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.5906863063846,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052004484,
                "rss_peak_bytes": 1529815040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.132,
                "predicted_n": 34,
                "predicted_per_second": 79.1116481113892,
                "predicted_per_token_ms": 12.640363636363636
              },
              "tool_call_valid": true,
              "ttft_s": 0.31624323,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288850243159586,
              "complete": true,
              "e2e_s": 0.558431657,
              "end_ns": 288850801591243,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470335488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 141.55455827314495,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058296448,
                "rss_peak_bytes": 1529851904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.21,
                "predicted_n": 25,
                "predicted_per_second": 78.89287005686862,
                "predicted_per_token_ms": 12.675416666666665
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254205042,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289302086170732,
              "complete": true,
              "e2e_s": 0.182127083,
              "end_ns": 289302268297815,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.22828878013645,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05080002,
                "rss_peak_bytes": 1469169664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.163,
                "predicted_n": 10,
                "predicted_per_second": 77.47733787867048,
                "predicted_per_token_ms": 12.907
              },
              "ttft_s": 0.065951507,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289302347131437,
              "complete": true,
              "e2e_s": 0.233545505,
              "end_ns": 289302580676942,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.70872838602163,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051054784,
                "rss_peak_bytes": 1469169664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.118,
                "predicted_n": 14,
                "predicted_per_second": 78.25762409853238,
                "predicted_per_token_ms": 12.778307692307692
              },
              "ttft_s": 0.067355088,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 289302661237020,
              "complete": true,
              "e2e_s": 0.666274728,
              "end_ns": 289303327511748,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.98640741065412,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053508248,
                "rss_peak_bytes": 1469214720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.627,
                "predicted_n": 44,
                "predicted_per_second": 79.24412165262694,
                "predicted_per_token_ms": 12.619232558139533
              },
              "ttft_s": 0.123620408,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 289303406035507,
              "complete": true,
              "e2e_s": 0.357611109,
              "end_ns": 289303763646616,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 89.09520916325386,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050644588,
                "rss_peak_bytes": 1469218816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.697,
                "predicted_n": 23,
                "predicted_per_second": 78.93877580311234,
                "predicted_per_token_ms": 12.668045454545455
              },
              "ttft_s": 0.078875745,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 289303842747461,
              "complete": true,
              "e2e_s": 0.295185956,
              "end_ns": 289304137933417,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 69.81542124374911,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050629462,
                "rss_peak_bytes": 1469222912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.124,
                "predicted_n": 18,
                "predicted_per_second": 78.65854787066684,
                "predicted_per_token_ms": 12.713176470588236
              },
              "ttft_s": 0.079013014,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 289304213554096,
              "complete": true,
              "e2e_s": 0.470536106,
              "end_ns": 289304684090202,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469790720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 115.75731880864306,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050478651,
                "rss_peak_bytes": 1524985856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.04,
                "predicted_n": 29,
                "predicted_per_second": 79.08710880126539,
                "predicted_per_token_ms": 12.644285714285715
              },
              "ttft_s": 0.116433743,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289304770200541,
              "complete": true,
              "e2e_s": 1.07646049,
              "end_ns": 289305846661031,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 289.528313221818,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053127275,
                "rss_peak_bytes": 1525456896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.418,
                "predicted_n": 21,
                "predicted_per_second": 77.99764447113697,
                "predicted_per_token_ms": 12.8209
              },
              "ttft_s": 0.820021434,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289305923187175,
              "complete": true,
              "e2e_s": 0.197531534,
              "end_ns": 289306120718709,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 50.568907088111835,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055829706,
                "rss_peak_bytes": 1472794624,
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
              "ttft_s": 0.197402885
            },
            {
              "begin_ns": 289306191845846,
              "complete": true,
              "e2e_s": 1.659896365,
              "end_ns": 289307851742211,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 451.5242594117719,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.058414313,
                "rss_peak_bytes": 1472794624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1597.236,
                "predicted_n": 128,
                "predicted_per_second": 79.51235759775011,
                "predicted_per_token_ms": 12.576661417322835
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062576707
            },
            {
              "begin_ns": 289307922802863,
              "complete": true,
              "e2e_s": 0.619350637,
              "end_ns": 289308542153500,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470315008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 155.4054806733208,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052646127,
                "rss_peak_bytes": 1525510144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.721,
                "predicted_n": 34,
                "predicted_per_second": 79.00009815163709,
                "predicted_per_token_ms": 12.658212121212122
              },
              "tool_call_valid": true,
              "ttft_s": 0.317987995,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289308628234783,
              "complete": true,
              "e2e_s": 0.558474294,
              "end_ns": 289309186709077,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470347776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 148.64897258978473,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056304828,
                "rss_peak_bytes": 1525542912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 303.843,
                "predicted_n": 25,
                "predicted_per_second": 78.98816164927281,
                "predicted_per_token_ms": 12.660125
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254621742,
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
          "gpu_j_per_correct_token": 10.206814489725184,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470339584,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2666.265523786607,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.055696133,
              "rss_peak_bytes": 7727869952,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470335488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 3069.9642194389467,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.09526872,
              "rss_peak_bytes": 7711776768,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5736.229743225554,
          "raw_requests": [
            {
              "begin_ns": 288872842124357,
              "complete": true,
              "e2e_s": 0.181455699,
              "end_ns": 288873023580056,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.27402777417539,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053280057,
                "rss_peak_bytes": 1473589248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.903,
                "predicted_n": 10,
                "predicted_per_second": 77.65113931477183,
                "predicted_per_token_ms": 12.878111111111112
              },
              "ttft_s": 0.065507601,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288873078945583,
              "complete": true,
              "e2e_s": 0.233817004,
              "end_ns": 288873312762587,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 57.854813003386404,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.0501546,
                "rss_peak_bytes": 1473589248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.151,
                "predicted_n": 14,
                "predicted_per_second": 78.2420809986097,
                "predicted_per_token_ms": 12.780846153846154
              },
              "ttft_s": 0.067525146,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288873377099397,
              "complete": true,
              "e2e_s": 0.665331261,
              "end_ns": 288874042430658,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.6381478499396,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052907834,
                "rss_peak_bytes": 1473642496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.073,
                "predicted_n": 44,
                "predicted_per_second": 79.32510934874085,
                "predicted_per_token_ms": 12.606348837209302
              },
              "ttft_s": 0.123234066,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288874113297565,
              "complete": true,
              "e2e_s": 0.357652474,
              "end_ns": 288874470950039,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414081024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 88.51695995498014,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050543082,
                "rss_peak_bytes": 1473646592,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.073,
                "predicted_n": 23,
                "predicted_per_second": 78.8324201911328,
                "predicted_per_token_ms": 12.685136363636362
              },
              "ttft_s": 0.07852461,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288874526907556,
              "complete": true,
              "e2e_s": 0.294736983,
              "end_ns": 288874821644539,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.01622037060102,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050651208,
                "rss_peak_bytes": 1473650688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.231,
                "predicted_n": 18,
                "predicted_per_second": 78.6196243831828,
                "predicted_per_token_ms": 12.719470588235295
              },
              "ttft_s": 0.07849642,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288874880318197,
              "complete": true,
              "e2e_s": 0.470303989,
              "end_ns": 288875350622186,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469778432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 120.71518445927066,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050334779,
                "rss_peak_bytes": 1529344000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 355.832,
                "predicted_n": 29,
                "predicted_per_second": 78.68881944288316,
                "predicted_per_token_ms": 12.708285714285713
              },
              "ttft_s": 0.114477959,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288875409169919,
              "complete": true,
              "e2e_s": 1.072392782,
              "end_ns": 288876481562701,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470249472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 285.75362859781893,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054453996,
                "rss_peak_bytes": 1529815040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.05,
                "predicted_n": 21,
                "predicted_per_second": 78.10974419058778,
                "predicted_per_token_ms": 12.8025
              },
              "ttft_s": 0.816252087,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288876553074517,
              "complete": true,
              "e2e_s": 0.196348976,
              "end_ns": 288876749423493,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417587200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.79495404418894,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055696133,
                "rss_peak_bytes": 1477152768,
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
              "ttft_s": 0.196212217
            },
            {
              "begin_ns": 288876808277960,
              "complete": true,
              "e2e_s": 1.657836666,
              "end_ns": 288878466114626,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417587200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 444.88897503070797,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050855657,
                "rss_peak_bytes": 1477152768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.297,
                "predicted_n": 128,
                "predicted_per_second": 79.60900070645152,
                "predicted_per_token_ms": 12.561393700787402
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062380149
            },
            {
              "begin_ns": 288878527993877,
              "complete": true,
              "e2e_s": 0.618013765,
              "end_ns": 288879146007642,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470306816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 154.1332680105687,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050569617,
                "rss_peak_bytes": 1529872384,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.147,
                "predicted_n": 34,
                "predicted_per_second": 79.10880337147337,
                "predicted_per_token_ms": 12.640818181818181
              },
              "tool_call_valid": true,
              "ttft_s": 0.317242375,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288879211666439,
              "complete": true,
              "e2e_s": 0.55811276,
              "end_ns": 288879769779199,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470339584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.56484518038462,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051914603,
                "rss_peak_bytes": 1529905152,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.262,
                "predicted_n": 25,
                "predicted_per_second": 78.87938684423293,
                "predicted_per_token_ms": 12.677583333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.253749291,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289272975911448,
              "complete": true,
              "e2e_s": 0.182055288,
              "end_ns": 289273157966736,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.48536100062604,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.049985702,
                "rss_peak_bytes": 1456349184,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.152,
                "predicted_n": 10,
                "predicted_per_second": 77.4846752531166,
                "predicted_per_token_ms": 12.905777777777779
              },
              "ttft_s": 0.06589848,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289273236251871,
              "complete": true,
              "e2e_s": 0.235278325,
              "end_ns": 289273471530196,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 57.48339896174505,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051831556,
                "rss_peak_bytes": 1456087040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 167.857,
                "predicted_n": 14,
                "predicted_per_second": 77.44687442287186,
                "predicted_per_token_ms": 12.912076923076922
              },
              "ttft_s": 0.067495053,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 289273542719957,
              "complete": true,
              "e2e_s": 0.666299718,
              "end_ns": 289274209019675,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 176.29296353207695,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051487488,
                "rss_peak_bytes": 1456197632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.606,
                "predicted_n": 44,
                "predicted_per_second": 79.24718856776371,
                "predicted_per_token_ms": 12.618744186046511
              },
              "ttft_s": 0.123665123,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 289274290235389,
              "complete": true,
              "e2e_s": 0.358162341,
              "end_ns": 289274648397730,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 89.30485920249498,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05192888,
                "rss_peak_bytes": 1456271360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.841,
                "predicted_n": 23,
                "predicted_per_second": 78.89800997701198,
                "predicted_per_token_ms": 12.67459090909091
              },
              "ttft_s": 0.079265205,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 289274723227209,
              "complete": true,
              "e2e_s": 0.294913969,
              "end_ns": 289275018141178,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414101504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 75.02524760488038,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052148241,
                "rss_peak_bytes": 1456275456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.098,
                "predicted_n": 18,
                "predicted_per_second": 78.66801173541633,
                "predicted_per_token_ms": 12.71164705882353
              },
              "ttft_s": 0.07875136,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 289275093791195,
              "complete": true,
              "e2e_s": 0.46926174,
              "end_ns": 289275563052935,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469794816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.16726022434771,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053399847,
                "rss_peak_bytes": 1511968768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.218,
                "predicted_n": 29,
                "predicted_per_second": 79.04736631114173,
                "predicted_per_token_ms": 12.650642857142858
              },
              "ttft_s": 0.115000836,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289275640168650,
              "complete": true,
              "e2e_s": 1.078103468,
              "end_ns": 289276718272118,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 285.17995450088176,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054638136,
                "rss_peak_bytes": 1512501248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 255.705,
                "predicted_n": 21,
                "predicted_per_second": 78.21513071703721,
                "predicted_per_token_ms": 12.785250000000001
              },
              "ttft_s": 0.822322799,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289276800519144,
              "complete": true,
              "e2e_s": 0.198189949,
              "end_ns": 289276998709093,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417595392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.35830440067111,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054362546,
                "rss_peak_bytes": 1459834880,
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
              "ttft_s": 0.198060806
            },
            {
              "begin_ns": 289277059980521,
              "complete": true,
              "e2e_s": 1.67049719,
              "end_ns": 289278730477711,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417595392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 450.54155438540397,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.057523781,
                "rss_peak_bytes": 1459834880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1607.538,
                "predicted_n": 128,
                "predicted_per_second": 79.00279806760399,
                "predicted_per_token_ms": 12.657779527559056
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062832099
            },
            {
              "begin_ns": 289278801200218,
              "complete": true,
              "e2e_s": 0.620144783,
              "end_ns": 289279421345001,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470306816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 159.33356674991148,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050862894,
                "rss_peak_bytes": 1512546304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.555,
                "predicted_n": 34,
                "predicted_per_second": 78.84268495179845,
                "predicted_per_token_ms": 12.683484848484849
              },
              "tool_call_valid": true,
              "ttft_s": 0.317791442,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289279504860533,
              "complete": true,
              "e2e_s": 0.561719179,
              "end_ns": 289280066579712,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470335488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 141.93266767740622,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.057194589,
                "rss_peak_bytes": 1512443904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.983,
                "predicted_n": 25,
                "predicted_per_second": 78.6929107524026,
                "predicted_per_token_ms": 12.707625
              },
              "tool_facts_valid": true,
              "ttft_s": 0.256710009,
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
          "gpu_j_per_correct_token": 9.181486412413014,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476020736,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2271.100698377932,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.055988402,
              "rss_peak_bytes": 5997678592,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 368394240,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2705.2649371499215,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.087297908,
              "rss_peak_bytes": 5721042944,
              "swap_peak_bytes": 206725120
            }
          ],
          "lifecycle_gpu_j": 4976.365635527854,
          "raw_requests": [
            {
              "begin_ns": 288922259225712,
              "complete": true,
              "e2e_s": 0.157876185,
              "end_ns": 288922417101897,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 432869376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.503627227790567,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051928743,
                "rss_peak_bytes": 1230880768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.645,
                "predicted_n": 10,
                "predicted_per_second": 94.09796643839196,
                "predicted_per_token_ms": 10.627222222222223
              },
              "ttft_s": 0.062233458,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288922495102572,
              "complete": true,
              "e2e_s": 0.148465865,
              "end_ns": 288922643568437,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.308790800523013,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05038175,
                "rss_peak_bytes": 1217826816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.608,
                "predicted_n": 9,
                "predicted_per_second": 93.44921035417251,
                "predicted_per_token_ms": 10.701
              },
              "ttft_s": 0.06280374,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288922738712175,
              "complete": true,
              "e2e_s": 0.526086886,
              "end_ns": 288923264799061,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419815424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 135.41189319282265,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050249884,
                "rss_peak_bytes": 1217880064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.042,
                "predicted_n": 39,
                "predicted_per_second": 96.43642048309572,
                "predicted_per_token_ms": 10.369526315789473
              },
              "ttft_s": 0.131925302,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288923340304229,
              "complete": true,
              "e2e_s": 0.30590166,
              "end_ns": 288923646205889,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.63759757115275,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050740427,
                "rss_peak_bytes": 1220907008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.926,
                "predicted_n": 23,
                "predicted_per_second": 96.10092344250981,
                "predicted_per_token_ms": 10.405727272727272
              },
              "ttft_s": 0.076992813,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288923722673203,
              "complete": true,
              "e2e_s": 0.254214419,
              "end_ns": 288923976887622,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422780928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 62.97964075575472,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050184878,
                "rss_peak_bytes": 1220907008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.003,
                "predicted_n": 18,
                "predicted_per_second": 95.50400835940968,
                "predicted_per_token_ms": 10.470764705882353
              },
              "ttft_s": 0.076187043,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288924055111009,
              "complete": true,
              "e2e_s": 0.397978128,
              "end_ns": 288924453089137,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475496448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 92.24578833058054,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05223013,
                "rss_peak_bytes": 1273622528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.584,
                "predicted_n": 29,
                "predicted_per_second": 96.35767970707265,
                "predicted_per_token_ms": 10.378
              },
              "ttft_s": 0.10732096,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288924513192179,
              "complete": true,
              "e2e_s": 1.025403335,
              "end_ns": 288925538595514,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475926528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 273.0602897240546,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055076143,
                "rss_peak_bytes": 1274052608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.74,
                "predicted_n": 16,
                "predicted_per_second": 94.49414136323547,
                "predicted_per_token_ms": 10.582666666666666
              },
              "ttft_s": 0.866639145,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288925625612474,
              "complete": true,
              "e2e_s": 0.203182492,
              "end_ns": 288925828794966,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.90377641950751,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050539667,
                "rss_peak_bytes": 1221390336,
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
              "ttft_s": 0.203055934
            },
            {
              "begin_ns": 288925896102086,
              "complete": true,
              "e2e_s": 1.366685967,
              "end_ns": 288927262788053,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 349.7886500891135,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050243142,
                "rss_peak_bytes": 1221390336,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.945,
                "predicted_n": 128,
                "predicted_per_second": 97.02470310058865,
                "predicted_per_token_ms": 10.306653543307085
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057444666
            },
            {
              "begin_ns": 288927322121118,
              "complete": true,
              "e2e_s": 0.550474697,
              "end_ns": 288927872595815,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475979776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 136.5789461606852,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051259857,
                "rss_peak_bytes": 1274105856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.145,
                "predicted_n": 34,
                "predicted_per_second": 95.88981388658851,
                "predicted_per_token_ms": 10.428636363636363
              },
              "tool_call_valid": true,
              "ttft_s": 0.302366229,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288927940622385,
              "complete": true,
              "e2e_s": 0.523663814,
              "end_ns": 288928464286199,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476020736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.30986609099168,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052243307,
                "rss_peak_bytes": 1274146816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.783,
                "predicted_n": 25,
                "predicted_per_second": 95.70026676449362,
                "predicted_per_token_ms": 10.449291666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272850469,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289206072811475,
              "complete": true,
              "e2e_s": 0.212836352,
              "end_ns": 289206285647827,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 308203520,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.750404458050795,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051484011,
                "rss_peak_bytes": 868954112,
                "swap_peak_bytes": 164298752
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 103.794,
                "predicted_n": 10,
                "predicted_per_second": 86.71021446326377,
                "predicted_per_token_ms": 11.532666666666666
              },
              "ttft_s": 0.101276504,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289206359965474,
              "complete": true,
              "e2e_s": 0.181468232,
              "end_ns": 289206541433706,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 256172032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 36.21982639455506,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050378007,
                "rss_peak_bytes": 817446912,
                "swap_peak_bytes": 164093952
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.158,
                "predicted_n": 9,
                "predicted_per_second": 92.85266603217345,
                "predicted_per_token_ms": 10.76975
              },
              "ttft_s": 0.091152163,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 289206621324672,
              "complete": true,
              "e2e_s": 0.585924718,
              "end_ns": 289207207249390,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 257302528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.28134573124882,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05084172,
                "rss_peak_bytes": 819015680,
                "swap_peak_bytes": 162807808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 395.827,
                "predicted_n": 39,
                "predicted_per_second": 96.00153602457638,
                "predicted_per_token_ms": 10.4165
              },
              "ttft_s": 0.18122403,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 289207293437660,
              "complete": true,
              "e2e_s": 0.347143746,
              "end_ns": 289207640581406,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 261550080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 77.01842465787801,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050489385,
                "rss_peak_bytes": 823889920,
                "swap_peak_bytes": 161554432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 238.621,
                "predicted_n": 23,
                "predicted_per_second": 92.19641188327935,
                "predicted_per_token_ms": 10.846409090909091
              },
              "ttft_s": 0.102403417,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 289207711690875,
              "complete": true,
              "e2e_s": 0.302317724,
              "end_ns": 289208014008599,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 262467584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 60.07987395556054,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050231686,
                "rss_peak_bytes": 825135104,
                "swap_peak_bytes": 161099776
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 179.538,
                "predicted_n": 18,
                "predicted_per_second": 94.68747563189964,
                "predicted_per_token_ms": 10.561058823529413
              },
              "ttft_s": 0.118408993,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 289208087124193,
              "complete": true,
              "e2e_s": 0.43858912,
              "end_ns": 289208525713313,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 315961344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 96.57582533033153,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052289631,
                "rss_peak_bytes": 879022080,
                "swap_peak_bytes": 159629312
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 295.853,
                "predicted_n": 29,
                "predicted_per_second": 94.64159565730279,
                "predicted_per_token_ms": 10.566178571428571
              },
              "ttft_s": 0.136115157,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289208602083864,
              "complete": true,
              "e2e_s": 1.05706521,
              "end_ns": 289209659149074,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 316956672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 277.7003911802391,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053289878,
                "rss_peak_bytes": 880148480,
                "swap_peak_bytes": 159215616
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 160.637,
                "predicted_n": 16,
                "predicted_per_second": 93.37823789039885,
                "predicted_per_token_ms": 10.709133333333334
              },
              "ttft_s": 0.891460283,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 289209729209814,
              "complete": true,
              "e2e_s": 0.205127497,
              "end_ns": 289209934337311,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264347648,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 52.494836800049974,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05080145,
                "rss_peak_bytes": 827539456,
                "swap_peak_bytes": 158949376
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
              "ttft_s": 0.204991491
            },
            {
              "begin_ns": 289210008152459,
              "complete": true,
              "e2e_s": 1.366901911,
              "end_ns": 289211375054370,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264364032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 365.93830899304777,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056196388,
                "rss_peak_bytes": 827555840,
                "swap_peak_bytes": 158937088
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.287,
                "predicted_n": 128,
                "predicted_per_second": 96.99935919320974,
                "predicted_per_token_ms": 10.309346456692914
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057527081
            },
            {
              "begin_ns": 289211485140661,
              "complete": true,
              "e2e_s": 0.552122228,
              "end_ns": 289212037262889,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 317083648,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 139.04471333122396,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054692808,
                "rss_peak_bytes": 880275456,
                "swap_peak_bytes": 158928896
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.62,
                "predicted_n": 34,
                "predicted_per_second": 96.31661899480474,
                "predicted_per_token_ms": 10.382424242424243
              },
              "tool_call_valid": true,
              "ttft_s": 0.302606359,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289212121025010,
              "complete": true,
              "e2e_s": 0.523407765,
              "end_ns": 289212644432775,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 317120512,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.64336670807518,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05191697,
                "rss_peak_bytes": 880312320,
                "swap_peak_bytes": 158920704
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.83,
                "predicted_n": 25,
                "predicted_per_second": 96.065324420606,
                "predicted_per_token_ms": 10.409583333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273534969,
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
          "gpu_j_per_correct_token": 8.372021683516097,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476020736,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2249.420865836666,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.082459977,
              "rss_peak_bytes": 5997699072,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476016640,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2288.2148866290595,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.065607671,
              "rss_peak_bytes": 5996650496,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4537.635752465725,
          "raw_requests": [
            {
              "begin_ns": 288898111720476,
              "complete": true,
              "e2e_s": 0.157356527,
              "end_ns": 288898269077003,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 472506368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 29.15668387181338,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05035982,
                "rss_peak_bytes": 1270554624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.576,
                "predicted_n": 10,
                "predicted_per_second": 94.16589938896796,
                "predicted_per_token_ms": 10.619555555555555
              },
              "ttft_s": 0.061578256,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288898324034698,
              "complete": true,
              "e2e_s": 0.148396455,
              "end_ns": 288898472431153,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.745094578039286,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.049989756,
                "rss_peak_bytes": 1217859584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.304,
                "predicted_n": 9,
                "predicted_per_second": 93.78223764419019,
                "predicted_per_token_ms": 10.663
              },
              "ttft_s": 0.063092475,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288898531755698,
              "complete": true,
              "e2e_s": 0.525927328,
              "end_ns": 288899057683026,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.46801857345625,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052146136,
                "rss_peak_bytes": 1217912832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.981,
                "predicted_n": 39,
                "predicted_per_second": 96.45135171493042,
                "predicted_per_token_ms": 10.367921052631578
              },
              "ttft_s": 0.13195481,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288899114040190,
              "complete": true,
              "e2e_s": 0.306602384,
              "end_ns": 288899420642574,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.44456382373376,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052098041,
                "rss_peak_bytes": 1220947968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.668,
                "predicted_n": 23,
                "predicted_per_second": 95.79044533848861,
                "predicted_per_token_ms": 10.439454545454545
              },
              "ttft_s": 0.076918493,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288899481209270,
              "complete": true,
              "e2e_s": 0.253991056,
              "end_ns": 288899735200326,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422785024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.13794843759296,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050656812,
                "rss_peak_bytes": 1220947968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.977,
                "predicted_n": 18,
                "predicted_per_second": 95.5179601858667,
                "predicted_per_token_ms": 10.469235294117647
              },
              "ttft_s": 0.075995774,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288899795353812,
              "complete": true,
              "e2e_s": 0.397896648,
              "end_ns": 288900193250460,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475500544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 93.03072279327678,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050653534,
                "rss_peak_bytes": 1273663488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.867,
                "predicted_n": 29,
                "predicted_per_second": 96.26392818710957,
                "predicted_per_token_ms": 10.388107142857143
              },
              "ttft_s": 0.106964631,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288900249171376,
              "complete": true,
              "e2e_s": 1.025073119,
              "end_ns": 288901274244495,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475930624,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 266.68833971632597,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.082459977,
                "rss_peak_bytes": 1274093568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.4,
                "predicted_n": 16,
                "predicted_per_second": 94.10288582183186,
                "predicted_per_token_ms": 10.626666666666667
              },
              "ttft_s": 0.865574895,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288901372765932,
              "complete": true,
              "e2e_s": 0.203845512,
              "end_ns": 288901576611444,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.507915153792375,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051064593,
                "rss_peak_bytes": 1221431296,
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
              "ttft_s": 0.203713928
            },
            {
              "begin_ns": 288901627699036,
              "complete": true,
              "e2e_s": 1.366416447,
              "end_ns": 288902994115483,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 346.38149127946537,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050637968,
                "rss_peak_bytes": 1221431296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.605,
                "predicted_n": 128,
                "predicted_per_second": 97.04991192911535,
                "predicted_per_token_ms": 10.303976377952756
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057710572
            },
            {
              "begin_ns": 288903051106790,
              "complete": true,
              "e2e_s": 0.549448099,
              "end_ns": 288903600554889,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.20681946650876,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055435379,
                "rss_peak_bytes": 1274150912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.285,
                "predicted_n": 34,
                "predicted_per_second": 96.13003772375721,
                "predicted_per_token_ms": 10.40257575757576
              },
              "tool_call_valid": true,
              "ttft_s": 0.30287219,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288903668933674,
              "complete": true,
              "e2e_s": 0.52264443,
              "end_ns": 288904191578104,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476020736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.66575373829352,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050519182,
                "rss_peak_bytes": 1274183680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.299,
                "predicted_n": 25,
                "predicted_per_second": 95.88532115589754,
                "predicted_per_token_ms": 10.429125
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272334683,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289232097437406,
              "complete": true,
              "e2e_s": 0.165373779,
              "end_ns": 289232262811185,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.53286661890961,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.065607671,
                "rss_peak_bytes": 1215229952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 98.925,
                "predicted_n": 10,
                "predicted_per_second": 90.97801364670205,
                "predicted_per_token_ms": 10.991666666666667
              },
              "ttft_s": 0.066280227,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289232342072726,
              "complete": true,
              "e2e_s": 0.148973872,
              "end_ns": 289232491046598,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.25629622926133,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050732747,
                "rss_peak_bytes": 1215229952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.53,
                "predicted_n": 9,
                "predicted_per_second": 93.53443236291359,
                "predicted_per_token_ms": 10.69125
              },
              "ttft_s": 0.063379372,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 289232563081314,
              "complete": true,
              "e2e_s": 0.527763093,
              "end_ns": 289233090844407,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419803136,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.73037015905078,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052057279,
                "rss_peak_bytes": 1215275008,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 395.314,
                "predicted_n": 39,
                "predicted_per_second": 96.12611746611555,
                "predicted_per_token_ms": 10.403
              },
              "ttft_s": 0.13242142,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 289233163080378,
              "complete": true,
              "e2e_s": 0.307170808,
              "end_ns": 289233470251186,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.46105101461526,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052733313,
                "rss_peak_bytes": 1217388544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.766,
                "predicted_n": 23,
                "predicted_per_second": 95.74958871199395,
                "predicted_per_token_ms": 10.44390909090909
              },
              "ttft_s": 0.077295794,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 289233541871496,
              "complete": true,
              "e2e_s": 0.254271541,
              "end_ns": 289233796143037,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 57.07343601472905,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051790254,
                "rss_peak_bytes": 1217388544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.786,
                "predicted_n": 18,
                "predicted_per_second": 95.6205775482884,
                "predicted_per_token_ms": 10.458
              },
              "ttft_s": 0.076392623,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 289233869090415,
              "complete": true,
              "e2e_s": 0.398396208,
              "end_ns": 289234267486623,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475484160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 93.01343098359811,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051500082,
                "rss_peak_bytes": 1270104064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.978,
                "predicted_n": 29,
                "predicted_per_second": 96.22720618053599,
                "predicted_per_token_ms": 10.392071428571429
              },
              "ttft_s": 0.107392883,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289234384183203,
              "complete": true,
              "e2e_s": 1.028461802,
              "end_ns": 289235412645005,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475947008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 272.7642987830133,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053494567,
                "rss_peak_bytes": 1270566912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.7,
                "predicted_n": 16,
                "predicted_per_second": 93.9261114589856,
                "predicted_per_token_ms": 10.646666666666667
              },
              "ttft_s": 0.868751434,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 289235491804530,
              "complete": true,
              "e2e_s": 0.204089768,
              "end_ns": 289235695894298,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.778168330391196,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053123477,
                "rss_peak_bytes": 1217884160,
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
              "ttft_s": 0.203957071
            },
            {
              "begin_ns": 289235760481938,
              "complete": true,
              "e2e_s": 1.367147528,
              "end_ns": 289237127629466,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 350.68821950193274,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05079045,
                "rss_peak_bytes": 1217884160,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.058,
                "predicted_n": 128,
                "predicted_per_second": 97.01632777157315,
                "predicted_per_token_ms": 10.307543307086615
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057992218
            },
            {
              "begin_ns": 289237200382093,
              "complete": true,
              "e2e_s": 0.549878123,
              "end_ns": 289237750260216,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475979776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.60940701670296,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053989428,
                "rss_peak_bytes": 1270599680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.743,
                "predicted_n": 34,
                "predicted_per_second": 96.28205390044435,
                "predicted_per_token_ms": 10.386151515151514
              },
              "tool_call_valid": true,
              "ttft_s": 0.302927443,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289237830784442,
              "complete": true,
              "e2e_s": 0.525371675,
              "end_ns": 289238356156117,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476016640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.46997816442695,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051852748,
                "rss_peak_bytes": 1270636544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.707,
                "predicted_n": 25,
                "predicted_per_second": 95.72927760293888,
                "predicted_per_token_ms": 10.446125
              },
              "tool_facts_valid": true,
              "ttft_s": 0.274614275,
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
          "gpu_j_per_correct_token": 26.65368934351517,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 671531008,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7699.247329471476,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.077650619,
              "rss_peak_bytes": 11667316736,
              "swap_peak_bytes": 199700480
            },
            {
              "anon_peak_bytes": 772747264,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7120.203945522957,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.07072595,
              "rss_peak_bytes": 12139905024,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14819.451274994433,
          "raw_requests": [
            {
              "begin_ns": 288990636195034,
              "complete": true,
              "e2e_s": 0.520089723,
              "end_ns": 288991156284757,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 611913728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 109.0827838685725,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053062492,
                "rss_peak_bytes": 1046200320,
                "swap_peak_bytes": 157216768
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 270.325,
                "predicted_n": 10,
                "predicted_per_second": 33.293258115231666,
                "predicted_per_token_ms": 30.03611111111111
              },
              "ttft_s": 0.243887989,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288991215008229,
              "complete": true,
              "e2e_s": 0.608249075,
              "end_ns": 288991823257304,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 456392704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 144.4980552190375,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050608187,
                "rss_peak_bytes": 890679296,
                "swap_peak_bytes": 155848704
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 372.408,
                "predicted_n": 14,
                "predicted_per_second": 34.907950419969495,
                "predicted_per_token_ms": 28.64676923076923
              },
              "ttft_s": 0.231631326,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288991885219290,
              "complete": true,
              "e2e_s": 1.825912539,
              "end_ns": 288993711131829,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 457531392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 471.5898248218872,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.076699339,
                "rss_peak_bytes": 891924480,
                "swap_peak_bytes": 155295744
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1246.846,
                "predicted_n": 45,
                "predicted_per_second": 35.28904130903095,
                "predicted_per_token_ms": 28.33740909090909
              },
              "ttft_s": 0.569455989,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 288993786585835,
              "complete": true,
              "e2e_s": 1.053703928,
              "end_ns": 288994840289763,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 461733888,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 264.1665648768067,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050909617,
                "rss_peak_bytes": 896847872,
                "swap_peak_bytes": 154050560
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 766.636,
                "predicted_n": 28,
                "predicted_per_second": 35.218800056350084,
                "predicted_per_token_ms": 28.393925925925924
              },
              "ttft_s": 0.276650837,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 288994901623875,
              "complete": true,
              "e2e_s": 0.893704144,
              "end_ns": 288995795328019,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 462565376,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 221.07484689744368,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050636895,
                "rss_peak_bytes": 897937408,
                "swap_peak_bytes": 153149440
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 629.917,
                "predicted_n": 23,
                "predicted_per_second": 34.925236181909675,
                "predicted_per_token_ms": 28.63259090909091
              },
              "ttft_s": 0.258214791,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 288995856662137,
              "complete": true,
              "e2e_s": 1.181871012,
              "end_ns": 288997038533149,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 620216320,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 294.88673681086885,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052059359,
                "rss_peak_bytes": 1055756288,
                "swap_peak_bytes": 152449024
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 795.083,
                "predicted_n": 29,
                "predicted_per_second": 35.21644910028261,
                "predicted_per_token_ms": 28.395821428571427
              },
              "ttft_s": 0.37830684,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288997103310300,
              "complete": true,
              "e2e_s": 3.799518892,
              "end_ns": 289000902829192,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621289472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1010.5156315777945,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056596077,
                "rss_peak_bytes": 1056894976,
                "swap_peak_bytes": 151683072
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 585.426,
                "predicted_n": 21,
                "predicted_per_second": 34.163156402346324,
                "predicted_per_token_ms": 29.271300000000004
              },
              "ttft_s": 3.210013932,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289000965092606,
              "complete": true,
              "e2e_s": 0.717800877,
              "end_ns": 289001682893483,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464490496,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 188.38701430337835,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054035191,
                "rss_peak_bytes": 900096000,
                "swap_peak_bytes": 151203840
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
              "ttft_s": 0.717672421
            },
            {
              "begin_ns": 289001738095778,
              "complete": true,
              "e2e_s": 3.779036799,
              "end_ns": 289005517132577,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464506880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1033.3065668189972,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054901754,
                "rss_peak_bytes": 900112384,
                "swap_peak_bytes": 151199744
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3584.077,
                "predicted_n": 128,
                "predicted_per_second": 35.434506568915786,
                "predicted_per_token_ms": 28.22107874015748
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194852022
            },
            {
              "begin_ns": 289005584641556,
              "complete": true,
              "e2e_s": 1.707464537,
              "end_ns": 289007292106093,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621432832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 444.4528225473945,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052399092,
                "rss_peak_bytes": 1057038336,
                "swap_peak_bytes": 151183360
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.383,
                "predicted_n": 34,
                "predicted_per_second": 35.129441346075026,
                "predicted_per_token_ms": 28.466151515151516
              },
              "tool_call_valid": true,
              "ttft_s": 1.031336365,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289007363548449,
              "complete": true,
              "e2e_s": 1.774216973,
              "end_ns": 289009137765422,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 621457408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 453.2784439931075,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051020775,
                "rss_peak_bytes": 1057062912,
                "swap_peak_bytes": 151175168
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.518,
                "predicted_n": 25,
                "predicted_per_second": 35.16390776506993,
                "predicted_per_token_ms": 28.43825
              },
              "tool_facts_valid": true,
              "ttft_s": 1.091683146,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289155970722997,
              "complete": true,
              "e2e_s": 0.46543274,
              "end_ns": 289156436155737,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.51570157067233,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050653798,
                "rss_peak_bytes": 1257418752,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.11,
                "predicted_n": 10,
                "predicted_per_second": 34.20622553304701,
                "predicted_per_token_ms": 29.234444444444446
              },
              "ttft_s": 0.202319778,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289156534388767,
              "complete": true,
              "e2e_s": 0.576222007,
              "end_ns": 289157110610774,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 143.41767311925173,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050937091,
                "rss_peak_bytes": 1257418752,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.353,
                "predicted_n": 14,
                "predicted_per_second": 35.00712260302192,
                "predicted_per_token_ms": 28.565615384615384
              },
              "ttft_s": 0.204844428,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 289157208740757,
              "complete": true,
              "e2e_s": 1.763812324,
              "end_ns": 289158972553081,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612290560,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 474.2888112338095,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.060578679,
                "rss_peak_bytes": 1257422848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1243.582,
                "predicted_n": 45,
                "predicted_per_second": 35.38166361365796,
                "predicted_per_token_ms": 28.263227272727274
              },
              "ttft_s": 0.520187476,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 289159089331973,
              "complete": true,
              "e2e_s": 0.988133901,
              "end_ns": 289160077465874,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615272448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 261.3367990118936,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051076175,
                "rss_peak_bytes": 1255976960,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.555,
                "predicted_n": 28,
                "predicted_per_second": 35.36091047796164,
                "predicted_per_token_ms": 28.279814814814813
              },
              "ttft_s": 0.224531666,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 289160212100720,
              "complete": true,
              "e2e_s": 0.847199676,
              "end_ns": 289161059300396,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615272448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 230.2500008697722,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052743867,
                "rss_peak_bytes": 1256108032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.048,
                "predicted_n": 23,
                "predicted_per_second": 35.310281069837316,
                "predicted_per_token_ms": 28.320363636363638
              },
              "ttft_s": 0.224083999,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 289161200127611,
              "complete": true,
              "e2e_s": 1.148508965,
              "end_ns": 289162348636576,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772198400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 289.88946797869596,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050891651,
                "rss_peak_bytes": 1413033984,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.303,
                "predicted_n": 29,
                "predicted_per_second": 35.38467565521678,
                "predicted_per_token_ms": 28.26082142857143
              },
              "ttft_s": 0.357172975,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289162464302860,
              "complete": true,
              "e2e_s": 3.787150583,
              "end_ns": 289166251453443,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772661248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1008.3529033531167,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.057097179,
                "rss_peak_bytes": 1413496832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.793,
                "predicted_n": 21,
                "predicted_per_second": 34.43567673852818,
                "predicted_per_token_ms": 29.03965
              },
              "ttft_s": 3.206315887,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289166320591529,
              "complete": true,
              "e2e_s": 0.723408313,
              "end_ns": 289167043999842,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615788544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 182.15497109136723,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051518478,
                "rss_peak_bytes": 1256689664,
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
              "ttft_s": 0.723276927
            },
            {
              "begin_ns": 289167106129157,
              "complete": true,
              "e2e_s": 3.77689128,
              "end_ns": 289170883020437,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615788544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1044.598462025516,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052990057,
                "rss_peak_bytes": 1256820736,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.8,
                "predicted_n": 128,
                "predicted_per_second": 35.45703277681613,
                "predicted_per_token_ms": 28.203149606299213
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195049591
            },
            {
              "begin_ns": 289170953838369,
              "complete": true,
              "e2e_s": 1.703619026,
              "end_ns": 289172657457395,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772702208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 452.4924721857163,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055035426,
                "rss_peak_bytes": 1414062080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.389,
                "predicted_n": 34,
                "predicted_per_second": 35.09186092138466,
                "predicted_per_token_ms": 28.496636363636362
              },
              "tool_call_valid": true,
              "ttft_s": 1.02679019,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289172737853201,
              "complete": true,
              "e2e_s": 1.77716257,
              "end_ns": 289174515015771,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772747264,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 456.16784459179144,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052840098,
                "rss_peak_bytes": 1414107136,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.407,
                "predicted_n": 25,
                "predicted_per_second": 35.169627509682634,
                "predicted_per_token_ms": 28.433625000000003
              },
              "tool_facts_valid": true,
              "ttft_s": 1.094715411,
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
          "gpu_j_per_correct_token": 25.470061468554455,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772739072,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7093.835713491655,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.08970122,
              "rss_peak_bytes": 12139732992,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772681728,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7067.518463024622,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.099950945,
              "rss_peak_bytes": 12139769856,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14161.354176516277,
          "raw_requests": [
            {
              "begin_ns": 289047210482300,
              "complete": true,
              "e2e_s": 0.468514027,
              "end_ns": 289047678996327,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 761208832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.73516513196283,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050244846,
                "rss_peak_bytes": 1403142144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.883,
                "predicted_n": 10,
                "predicted_per_second": 34.10602426075192,
                "predicted_per_token_ms": 29.32033333333333
              },
              "ttft_s": 0.204680982,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289047778474418,
              "complete": true,
              "e2e_s": 0.57876274,
              "end_ns": 289048357237158,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612311040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.56828830058313,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052866097,
                "rss_peak_bytes": 1254244352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.576,
                "predicted_n": 14,
                "predicted_per_second": 34.98611320429737,
                "predicted_per_token_ms": 28.582769230769234
              },
              "ttft_s": 0.207198629,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 289048422991028,
              "complete": true,
              "e2e_s": 1.761891693,
              "end_ns": 289050184882721,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612311040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 470.5596936295317,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052637204,
                "rss_peak_bytes": 1254244352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.025,
                "predicted_n": 45,
                "predicted_per_second": 35.42601799480687,
                "predicted_per_token_ms": 28.22784090909091
              },
              "ttft_s": 0.519865754,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 289050250112170,
              "complete": true,
              "e2e_s": 0.989901899,
              "end_ns": 289051240014069,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 257.30954284566934,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050689955,
                "rss_peak_bytes": 1257541632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.509,
                "predicted_n": 28,
                "predicted_per_second": 35.31678502149745,
                "predicted_per_token_ms": 28.31514814814815
              },
              "ttft_s": 0.225386764,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 289051307735421,
              "complete": true,
              "e2e_s": 0.846443201,
              "end_ns": 289052154178622,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615284736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 226.61274710690938,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050611876,
                "rss_peak_bytes": 1257541632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.569,
                "predicted_n": 23,
                "predicted_per_second": 35.337448539840565,
                "predicted_per_token_ms": 28.29859090909091
              },
              "ttft_s": 0.22382668,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 289052222817288,
              "complete": true,
              "e2e_s": 1.145268883,
              "end_ns": 289053368086171,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772202496,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 291.22668147357956,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051935542,
                "rss_peak_bytes": 1414459392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.485,
                "predicted_n": 29,
                "predicted_per_second": 35.331899026479995,
                "predicted_per_token_ms": 28.303035714285716
              },
              "ttft_s": 0.352773077,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289053435214188,
              "complete": true,
              "e2e_s": 3.773689571,
              "end_ns": 289057208903759,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772661248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1013.444706098339,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056727526,
                "rss_peak_bytes": 1414918144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.496,
                "predicted_n": 21,
                "predicted_per_second": 34.512749009484104,
                "predicted_per_token_ms": 28.9748
              },
              "ttft_s": 3.194155544,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289057272686796,
              "complete": true,
              "e2e_s": 0.719221407,
              "end_ns": 289057991908203,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615792640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 186.03018656683,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056018251,
                "rss_peak_bytes": 1258049536,
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
              "ttft_s": 0.719094743
            },
            {
              "begin_ns": 289058048115145,
              "complete": true,
              "e2e_s": 3.776388758,
              "end_ns": 289061824503903,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615792640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1042.2015332670683,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054283782,
                "rss_peak_bytes": 1258049536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3579.828,
                "predicted_n": 128,
                "predicted_per_second": 35.47656479585053,
                "predicted_per_token_ms": 28.187622047244094
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196281559
            },
            {
              "begin_ns": 289061889134997,
              "complete": true,
              "e2e_s": 1.701003512,
              "end_ns": 289063590138509,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772710400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 445.5390694823114,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052011702,
                "rss_peak_bytes": 1414967296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 938.452,
                "predicted_n": 34,
                "predicted_per_second": 35.16429183378585,
                "predicted_per_token_ms": 28.437939393939395
              },
              "tool_call_valid": true,
              "ttft_s": 1.025338101,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289063662875205,
              "complete": true,
              "e2e_s": 1.773584826,
              "end_ns": 289065436460031,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772739072,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 457.75668793352133,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050931388,
                "rss_peak_bytes": 1414995968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.83,
                "predicted_n": 25,
                "predicted_per_second": 35.14784060454286,
                "predicted_per_token_ms": 28.45125
              },
              "tool_facts_valid": true,
              "ttft_s": 1.090757544,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 289101573192744,
              "complete": true,
              "e2e_s": 0.46495437,
              "end_ns": 289102038147114,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 107.44930763128518,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05191979,
                "rss_peak_bytes": 1257410560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.662,
                "predicted_n": 10,
                "predicted_per_second": 34.264568152226055,
                "predicted_per_token_ms": 29.184666666666665
              },
              "ttft_s": 0.202243376,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 289102105619603,
              "complete": true,
              "e2e_s": 0.572896062,
              "end_ns": 289102678515665,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 139.64183926712403,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051701872,
                "rss_peak_bytes": 1257410560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.779,
                "predicted_n": 14,
                "predicted_per_second": 35.06131684912037,
                "predicted_per_token_ms": 28.521461538461537
              },
              "ttft_s": 0.202123866,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 289102747927263,
              "complete": true,
              "e2e_s": 1.762612077,
              "end_ns": 289104510539340,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612286464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 470.9934916187067,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052101031,
                "rss_peak_bytes": 1257410560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1243.469,
                "predicted_n": 45,
                "predicted_per_second": 35.38487891535696,
                "predicted_per_token_ms": 28.26065909090909
              },
              "ttft_s": 0.519154362,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 289104580083253,
              "complete": true,
              "e2e_s": 0.985793882,
              "end_ns": 289105565877135,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 261.80148867998975,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051960562,
                "rss_peak_bytes": 1260707840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.415,
                "predicted_n": 28,
                "predicted_per_second": 35.36739519134416,
                "predicted_per_token_ms": 28.27462962962963
              },
              "ttft_s": 0.222400386,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 289105633099023,
              "complete": true,
              "e2e_s": 0.845185418,
              "end_ns": 289106478284441,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 222.66450612463024,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05187026,
                "rss_peak_bytes": 1260707840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.611,
                "predicted_n": 23,
                "predicted_per_second": 35.27840272220984,
                "predicted_per_token_ms": 28.345954545454546
              },
              "ttft_s": 0.221566239,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 289106545747217,
              "complete": true,
              "e2e_s": 1.144918986,
              "end_ns": 289107690666203,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772177920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 289.3507167030646,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050581648,
                "rss_peak_bytes": 1417625600,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.7,
                "predicted_n": 29,
                "predicted_per_second": 35.36693191865605,
                "predicted_per_token_ms": 28.275000000000002
              },
              "ttft_s": 0.353170308,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 289107758817528,
              "complete": true,
              "e2e_s": 3.785690571,
              "end_ns": 289111544508099,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772603904,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1007.0850588600566,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056879379,
                "rss_peak_bytes": 1418051584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.447,
                "predicted_n": 21,
                "predicted_per_second": 34.39694417547945,
                "predicted_per_token_ms": 29.07235
              },
              "ttft_s": 3.204234781,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 289111611530284,
              "complete": true,
              "e2e_s": 0.722881656,
              "end_ns": 289112334411940,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772603904,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 190.532688768343,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052426435,
                "rss_peak_bytes": 1418051584,
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
              "ttft_s": 0.722750227
            },
            {
              "begin_ns": 289112396056872,
              "complete": true,
              "e2e_s": 3.773780738,
              "end_ns": 289116169837610,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615735296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1040.509771985608,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052159347,
                "rss_peak_bytes": 1261182976,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3579.123,
                "predicted_n": 128,
                "predicted_per_second": 35.48355281447438,
                "predicted_per_token_ms": 28.182070866141732
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194575398
            },
            {
              "begin_ns": 289116262794517,
              "complete": true,
              "e2e_s": 1.708812225,
              "end_ns": 289117971606742,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772648960,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 451.9245508620914,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055566223,
                "rss_peak_bytes": 1418096640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.804,
                "predicted_n": 34,
                "predicted_per_second": 35.11370455967415,
                "predicted_per_token_ms": 28.47890909090909
              },
              "tool_call_valid": true,
              "ttft_s": 1.032341731,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 289118076140853,
              "complete": true,
              "e2e_s": 1.775945524,
              "end_ns": 289119852086377,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772681728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 455.0408859455598,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051492227,
                "rss_peak_bytes": 1418129408,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.124,
                "predicted_n": 25,
                "predicted_per_second": 35.132713826479524,
                "predicted_per_token_ms": 28.4635
              },
              "tool_facts_valid": true,
              "ttft_s": 1.092728256,
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
