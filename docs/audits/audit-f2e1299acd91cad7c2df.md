# Public audit excerpt

Original SHA256: `f2e1299acd91cad7c2df0db7960a108bf922bad775535ed649e926e57ad8bc9d`

Original file: `RESULTS.json`; 266274 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.627586159831301,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470355968,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2658.3193061188304,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.215877052,
              "rss_peak_bytes": 7726292992,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470335488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2752.3841157063607,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.05556369,
              "rss_peak_bytes": 7725977600,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5410.703421825191,
          "raw_requests": [
            {
              "begin_ns": 294727485093754,
              "complete": true,
              "e2e_s": 0.183094969,
              "end_ns": 294727668188723,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 466788352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 35.89273132620987,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050579477,
                "rss_peak_bytes": 1521389568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.449,
                "predicted_n": 10,
                "predicted_per_second": 77.2870527011825,
                "predicted_per_token_ms": 12.938777777777778
              },
              "ttft_s": 0.066470878,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294727716104380,
              "complete": true,
              "e2e_s": 0.234247727,
              "end_ns": 294727950352107,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.75825025983319,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051244546,
                "rss_peak_bytes": 1468694528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.946,
                "predicted_n": 14,
                "predicted_per_second": 77.8694907335306,
                "predicted_per_token_ms": 12.842
              },
              "ttft_s": 0.067183094,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294728006098702,
              "complete": true,
              "e2e_s": 0.665997074,
              "end_ns": 294728672095776,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 172.86211497778393,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05164399,
                "rss_peak_bytes": 1468739584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.323,
                "predicted_n": 44,
                "predicted_per_second": 79.28854206810334,
                "predicted_per_token_ms": 12.612162790697674
              },
              "ttft_s": 0.123616108,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294728727109280,
              "complete": true,
              "e2e_s": 0.358255241,
              "end_ns": 294729085364521,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 85.59783257155439,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05173744,
                "rss_peak_bytes": 1468743680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.296,
                "predicted_n": 23,
                "predicted_per_second": 78.76947754353804,
                "predicted_per_token_ms": 12.695272727272727
              },
              "ttft_s": 0.078976886,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294729154153798,
              "complete": true,
              "e2e_s": 0.295009917,
              "end_ns": 294729449163715,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414097408,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.80941325602234,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052062728,
                "rss_peak_bytes": 1468743680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 215.965,
                "predicted_n": 18,
                "predicted_per_second": 78.71645868543514,
                "predicted_per_token_ms": 12.703823529411764
              },
              "ttft_s": 0.078959087,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294729511112187,
              "complete": true,
              "e2e_s": 0.469334735,
              "end_ns": 294729980446922,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469790720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 111.59186824720342,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051442714,
                "rss_peak_bytes": 1524436992,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.616,
                "predicted_n": 29,
                "predicted_per_second": 78.95864822794233,
                "predicted_per_token_ms": 12.664857142857143
              },
              "ttft_s": 0.114699435,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294730045264535,
              "complete": true,
              "e2e_s": 1.073415434,
              "end_ns": 294731118679969,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 284.85906338684305,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050674936,
                "rss_peak_bytes": 1524908032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.751,
                "predicted_n": 21,
                "predicted_per_second": 77.89648336325857,
                "predicted_per_token_ms": 12.837549999999998
              },
              "ttft_s": 0.816690088,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294731171831965,
              "complete": true,
              "e2e_s": 0.197919195,
              "end_ns": 294731369751160,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 45.51156357277394,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052484628,
                "rss_peak_bytes": 1472245760,
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
              "ttft_s": 0.197794195
            },
            {
              "begin_ns": 294731418233991,
              "complete": true,
              "e2e_s": 1.658147524,
              "end_ns": 294733076381515,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 447.4130737242892,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053396984,
                "rss_peak_bytes": 1472245760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.259,
                "predicted_n": 128,
                "predicted_per_second": 79.61089703928955,
                "predicted_per_token_ms": 12.561094488188976
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062818065
            },
            {
              "begin_ns": 294733132288017,
              "complete": true,
              "e2e_s": 0.618032673,
              "end_ns": 294733750320690,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470319104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 158.3025731086857,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050601784,
                "rss_peak_bytes": 1524965376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.47,
                "predicted_n": 34,
                "predicted_per_second": 79.04759623445995,
                "predicted_per_token_ms": 12.650606060606062
              },
              "tool_call_valid": true,
              "ttft_s": 0.316661533,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294733811729923,
              "complete": true,
              "e2e_s": 0.560046597,
              "end_ns": 294734371776520,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470355968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 142.36158841742557,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050715932,
                "rss_peak_bytes": 1525002240,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.149,
                "predicted_n": 25,
                "predicted_per_second": 78.90869277886824,
                "predicted_per_token_ms": 12.672875
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255840017,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295184675101784,
              "complete": true,
              "e2e_s": 0.182424134,
              "end_ns": 295184857525918,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 39.405859279574344,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050128975,
                "rss_peak_bytes": 1470488576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.411,
                "predicted_n": 10,
                "predicted_per_second": 77.31228148542662,
                "predicted_per_token_ms": 12.934555555555555
              },
              "ttft_s": 0.066053067,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295184935762548,
              "complete": true,
              "e2e_s": 0.23552667,
              "end_ns": 295185171289218,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 51.1015448518203,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050889809,
                "rss_peak_bytes": 1470488576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.202,
                "predicted_n": 14,
                "predicted_per_second": 78.21807198469332,
                "predicted_per_token_ms": 12.78476923076923
              },
              "ttft_s": 0.069435772,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295185250664412,
              "complete": true,
              "e2e_s": 0.667020481,
              "end_ns": 295185917684893,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 178.93875812100367,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050934166,
                "rss_peak_bytes": 1470533632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 543.397,
                "predicted_n": 44,
                "predicted_per_second": 79.13183179148946,
                "predicted_per_token_ms": 12.637139534883723
              },
              "ttft_s": 0.123642484,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295185997130712,
              "complete": true,
              "e2e_s": 0.357941214,
              "end_ns": 295186355071926,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 90.83143009181241,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050631888,
                "rss_peak_bytes": 1470533632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.976,
                "predicted_n": 23,
                "predicted_per_second": 78.85983023629272,
                "predicted_per_token_ms": 12.680727272727273
              },
              "ttft_s": 0.078926218,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295186433674584,
              "complete": true,
              "e2e_s": 0.295493674,
              "end_ns": 295186729168258,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 72.32310891232346,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050996023,
                "rss_peak_bytes": 1470537728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.38,
                "predicted_n": 18,
                "predicted_per_second": 78.56548664386727,
                "predicted_per_token_ms": 12.728235294117647
              },
              "ttft_s": 0.07908741,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295186810444149,
              "complete": true,
              "e2e_s": 0.469491437,
              "end_ns": 295187279935586,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469770240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 119.9405783378325,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052411431,
                "rss_peak_bytes": 1526235136,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.96,
                "predicted_n": 29,
                "predicted_per_second": 78.88212756366916,
                "predicted_per_token_ms": 12.677142857142856
              },
              "ttft_s": 0.114521091,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295187377046231,
              "complete": true,
              "e2e_s": 1.08094412,
              "end_ns": 295188457990351,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 283.2175665889141,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050718307,
                "rss_peak_bytes": 1526706176,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.988,
                "predicted_n": 21,
                "predicted_per_second": 77.8246455087397,
                "predicted_per_token_ms": 12.8494
              },
              "ttft_s": 0.82388519,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295188538024476,
              "complete": true,
              "e2e_s": 0.20010601,
              "end_ns": 295188738130486,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 50.26580451759523,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054057859,
                "rss_peak_bytes": 1474043904,
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
              "ttft_s": 0.199870281
            },
            {
              "begin_ns": 295188805211305,
              "complete": true,
              "e2e_s": 1.659628633,
              "end_ns": 295190464839938,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 452.2210548017823,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052371877,
                "rss_peak_bytes": 1474043904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1596.651,
                "predicted_n": 128,
                "predicted_per_second": 79.5414902818462,
                "predicted_per_token_ms": 12.572055118110237
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062860355
            },
            {
              "begin_ns": 295190563116078,
              "complete": true,
              "e2e_s": 0.619657757,
              "end_ns": 295191182773835,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 162.30171138420272,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051904975,
                "rss_peak_bytes": 1526759424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.203,
                "predicted_n": 34,
                "predicted_per_second": 78.90904656351103,
                "predicted_per_token_ms": 12.672818181818181
              },
              "tool_call_valid": true,
              "ttft_s": 0.317999131,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295191274136862,
              "complete": true,
              "e2e_s": 0.560271842,
              "end_ns": 295191834408704,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470335488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 141.31071839247312,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050633096,
                "rss_peak_bytes": 1526800384,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.139,
                "predicted_n": 25,
                "predicted_per_second": 78.91128727325335,
                "predicted_per_token_ms": 12.672458333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.256121299,
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
          "gpu_j_per_correct_token": 10.052427472660995,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 490618880,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7936147456,
              "gpu_energy_j": 2681.6363566592804,
              "gpu_owned_peak_bytes": 7681867776,
              "max_sample_gap_s": 0.070955371,
              "rss_peak_bytes": 7726415872,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 490676224,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7936147456,
              "gpu_energy_j": 2967.827882976199,
              "gpu_owned_peak_bytes": 7681867776,
              "max_sample_gap_s": 0.093893857,
              "rss_peak_bytes": 7532457984,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5649.464239635479,
          "raw_requests": [
            {
              "begin_ns": 294756407163934,
              "complete": true,
              "e2e_s": 0.182113436,
              "end_ns": 294756589277370,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431730688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 43.0907139884395,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.051209872,
                "rss_peak_bytes": 1501814784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.414,
                "predicted_n": 10,
                "predicted_per_second": 77.31028914048139,
                "predicted_per_token_ms": 12.934888888888889
              },
              "ttft_s": 0.065673388,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294756648168860,
              "complete": true,
              "e2e_s": 0.232964833,
              "end_ns": 294756881133693,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431730688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 55.11295196180552,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.053330428,
                "rss_peak_bytes": 1501814784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.063,
                "predicted_n": 14,
                "predicted_per_second": 78.28354299271963,
                "predicted_per_token_ms": 12.774076923076922
              },
              "ttft_s": 0.066913554,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294756936810685,
              "complete": true,
              "e2e_s": 0.667353137,
              "end_ns": 294757604163822,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431730688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 176.82738804528225,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.050716213,
                "rss_peak_bytes": 1501859840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.192,
                "predicted_n": 44,
                "predicted_per_second": 79.30769911765574,
                "predicted_per_token_ms": 12.609116279069768
              },
              "ttft_s": 0.125123395,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 294757660813299,
              "complete": true,
              "e2e_s": 0.358363365,
              "end_ns": 294758019176664,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431742976,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 89.90125860166278,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.050088359,
                "rss_peak_bytes": 1501872128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.694,
                "predicted_n": 23,
                "predicted_per_second": 78.65738986177752,
                "predicted_per_token_ms": 12.713363636363637
              },
              "ttft_s": 0.078542745,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294758074330324,
              "complete": true,
              "e2e_s": 0.294993368,
              "end_ns": 294758369323692,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431747072,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 67.4484285353069,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.050374187,
                "rss_peak_bytes": 1501876224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 215.737,
                "predicted_n": 18,
                "predicted_per_second": 78.79964957332307,
                "predicted_per_token_ms": 12.690411764705882
              },
              "ttft_s": 0.079200868,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294758422865643,
              "complete": true,
              "e2e_s": 0.468370022,
              "end_ns": 294758891235665,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 487436288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 114.66224047971669,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.051217412,
                "rss_peak_bytes": 1557565440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.429,
                "predicted_n": 29,
                "predicted_per_second": 79.22383279244205,
                "predicted_per_token_ms": 12.622464285714285
              },
              "ttft_s": 0.114869031,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294758947802307,
              "complete": true,
              "e2e_s": 1.097204603,
              "end_ns": 294760045006910,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490545152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 287.28016939689644,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.053660073,
                "rss_peak_bytes": 1560858624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.283,
                "predicted_n": 21,
                "predicted_per_second": 76.25351242741618,
                "predicted_per_token_ms": 13.11415
              },
              "ttft_s": 0.834942143,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294760099109583,
              "complete": true,
              "e2e_s": 0.198560424,
              "end_ns": 294760297670007,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437862400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 49.31920136353812,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.056483548,
                "rss_peak_bytes": 1508175872,
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
              "ttft_s": 0.198432146
            },
            {
              "begin_ns": 294760346863923,
              "complete": true,
              "e2e_s": 1.670191994,
              "end_ns": 294762017055917,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437862400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 448.1068204502167,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.058978168,
                "rss_peak_bytes": 1508175872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1606.995,
                "predicted_n": 128,
                "predicted_per_second": 79.0294929355723,
                "predicted_per_token_ms": 12.653503937007873
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063094918
            },
            {
              "begin_ns": 294762118644637,
              "complete": true,
              "e2e_s": 0.621436556,
              "end_ns": 294762740081193,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490586112,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 162.81378482617336,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.053297365,
                "rss_peak_bytes": 1560899584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 419.605,
                "predicted_n": 34,
                "predicted_per_second": 78.64539269074487,
                "predicted_per_token_ms": 12.715303030303032
              },
              "tool_call_valid": true,
              "ttft_s": 0.31886487,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294762807075779,
              "complete": true,
              "e2e_s": 0.562820287,
              "end_ns": 294763369896066,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490618880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 146.71566070717984,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.053390276,
                "rss_peak_bytes": 1560932352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 306.296,
                "predicted_n": 25,
                "predicted_per_second": 78.35557761119962,
                "predicted_per_token_ms": 12.762333333333332
              },
              "tool_facts_valid": true,
              "ttft_s": 0.256465455,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295154048157972,
              "complete": true,
              "e2e_s": 0.182862889,
              "end_ns": 295154231020861,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431779840,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 41.50783928057655,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.051088237,
                "rss_peak_bytes": 1202884608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.787,
                "predicted_n": 10,
                "predicted_per_second": 77.72893329993867,
                "predicted_per_token_ms": 12.865222222222222
              },
              "ttft_s": 0.067042691,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295154311650576,
              "complete": true,
              "e2e_s": 0.233300434,
              "end_ns": 295154544951010,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431779840,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 57.97428677935618,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.052671147,
                "rss_peak_bytes": 1202950144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.088,
                "predicted_n": 14,
                "predicted_per_second": 78.27175954915467,
                "predicted_per_token_ms": 12.776
              },
              "ttft_s": 0.067219306,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295154706719796,
              "complete": true,
              "e2e_s": 0.666250293,
              "end_ns": 295155372970089,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431779840,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 178.8019308345719,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.054791389,
                "rss_peak_bytes": 1203191808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 541.994,
                "predicted_n": 44,
                "predicted_per_second": 79.33667162367111,
                "predicted_per_token_ms": 12.604511627906977
              },
              "ttft_s": 0.124227371,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 295155452165588,
              "complete": true,
              "e2e_s": 0.357584539,
              "end_ns": 295155809750127,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431788032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 91.56112425348897,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.051027576,
                "rss_peak_bytes": 1203724288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.878,
                "predicted_n": 23,
                "predicted_per_second": 78.88754222276408,
                "predicted_per_token_ms": 12.676272727272726
              },
              "ttft_s": 0.078673999,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295155887743538,
              "complete": true,
              "e2e_s": 0.295142554,
              "end_ns": 295156182886092,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 431792128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7934050304,
                "gpu_energy_j": 72.69208106635219,
                "gpu_owned_peak_bytes": 7679770624,
                "max_sample_gap_s": 0.050614474,
                "rss_peak_bytes": 1204187136,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.513,
                "predicted_n": 18,
                "predicted_per_second": 78.51722529363133,
                "predicted_per_token_ms": 12.736058823529412
              },
              "ttft_s": 0.07857718,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295156260284203,
              "complete": true,
              "e2e_s": 0.468697179,
              "end_ns": 295156728981382,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 487485440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 120.22585780915361,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.050635431,
                "rss_peak_bytes": 1260142592,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.91,
                "predicted_n": 29,
                "predicted_per_second": 79.11615947557289,
                "predicted_per_token_ms": 12.639642857142858
              },
              "ttft_s": 0.114775617,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295156812049211,
              "complete": true,
              "e2e_s": 1.102283853,
              "end_ns": 295157914333064,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490598400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 291.83789224916427,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.056420096,
                "rss_peak_bytes": 1263636480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.829,
                "predicted_n": 21,
                "predicted_per_second": 75.8066778102483,
                "predicted_per_token_ms": 13.19145
              },
              "ttft_s": 0.838332694,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295157996823476,
              "complete": true,
              "e2e_s": 0.199474548,
              "end_ns": 295158196298024,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437932032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 48.82956863485004,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.050069087,
                "rss_peak_bytes": 1210970112,
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
              "ttft_s": 0.199338412
            },
            {
              "begin_ns": 295158262162763,
              "complete": true,
              "e2e_s": 1.655395902,
              "end_ns": 295159917558665,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437932032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 453.5076355788221,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.050660787,
                "rss_peak_bytes": 1210970112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1592.315,
                "predicted_n": 128,
                "predicted_per_second": 79.75808806674559,
                "predicted_per_token_ms": 12.537913385826773
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.062970788
            },
            {
              "begin_ns": 295159995124214,
              "complete": true,
              "e2e_s": 0.623167477,
              "end_ns": 295160618291691,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490643456,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 158.4686447923597,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.054223383,
                "rss_peak_bytes": 1263681536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 419.44,
                "predicted_n": 34,
                "predicted_per_second": 78.67633034522221,
                "predicted_per_token_ms": 12.71030303030303
              },
              "tool_call_valid": true,
              "ttft_s": 0.320682476,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295160707724951,
              "complete": true,
              "e2e_s": 0.564041418,
              "end_ns": 295161271766369,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490676224,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7936147456,
                "gpu_energy_j": 147.4030563207197,
                "gpu_owned_peak_bytes": 7681867776,
                "max_sample_gap_s": 0.056298543,
                "rss_peak_bytes": 1263714304,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 306.921,
                "predicted_n": 25,
                "predicted_per_second": 78.19601786779009,
                "predicted_per_token_ms": 12.788375
              },
              "tool_facts_valid": true,
              "ttft_s": 0.257105426,
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
          "gpu_j_per_correct_token": 8.799144967818,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476061696,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2251.4901463595584,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.056356119,
              "rss_peak_bytes": 5996343296,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476024832,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2517.646426197797,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.076018255,
              "rss_peak_bytes": 5989277696,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4769.136572557356,
          "raw_requests": [
            {
              "begin_ns": 294806708516928,
              "complete": true,
              "e2e_s": 0.156146117,
              "end_ns": 294806864663045,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.96591005974409,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050866744,
                "rss_peak_bytes": 1215746048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.716,
                "predicted_n": 10,
                "predicted_per_second": 94.02816665970161,
                "predicted_per_token_ms": 10.63511111111111
              },
              "ttft_s": 0.060383106,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294806922175465,
              "complete": true,
              "e2e_s": 0.149237878,
              "end_ns": 294807071413343,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.49750406721123,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050230608,
                "rss_peak_bytes": 1215746048,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.467,
                "predicted_n": 9,
                "predicted_per_second": 93.60337908198485,
                "predicted_per_token_ms": 10.683375
              },
              "ttft_s": 0.06373655,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294807129138486,
              "complete": true,
              "e2e_s": 0.525611902,
              "end_ns": 294807654750388,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.47617130750746,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050689742,
                "rss_peak_bytes": 1215791104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.525,
                "predicted_n": 39,
                "predicted_per_second": 96.56311543103996,
                "predicted_per_token_ms": 10.355921052631578
              },
              "ttft_s": 0.132036941,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294807713421794,
              "complete": true,
              "e2e_s": 0.306607569,
              "end_ns": 294808020029363,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 69.36807783102677,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052281664,
                "rss_peak_bytes": 1218822144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.367,
                "predicted_n": 23,
                "predicted_per_second": 95.91615184398802,
                "predicted_per_token_ms": 10.425772727272728
              },
              "ttft_s": 0.077219004,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294808088218966,
              "complete": true,
              "e2e_s": 0.253903357,
              "end_ns": 294808342122323,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.42744527686127,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050582664,
                "rss_peak_bytes": 1218822144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.759,
                "predicted_n": 18,
                "predicted_per_second": 95.63510145759146,
                "predicted_per_token_ms": 10.456411764705882
              },
              "ttft_s": 0.076037459,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294808404307490,
              "complete": true,
              "e2e_s": 0.398004831,
              "end_ns": 294808802312321,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475504640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 95.31433116260341,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050593048,
                "rss_peak_bytes": 1271537664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.137,
                "predicted_n": 29,
                "predicted_per_second": 96.174653170157,
                "predicted_per_token_ms": 10.39775
              },
              "ttft_s": 0.106880783,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294808863804682,
              "complete": true,
              "e2e_s": 1.026408474,
              "end_ns": 294809890213156,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475971584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 268.3085647504696,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056356119,
                "rss_peak_bytes": 1272004608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.132,
                "predicted_n": 16,
                "predicted_per_second": 94.26136792097127,
                "predicted_per_token_ms": 10.6088
              },
              "ttft_s": 0.867240145,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294809959599286,
              "complete": true,
              "e2e_s": 0.204703217,
              "end_ns": 294810164302503,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423309312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 51.262958569700096,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050364775,
                "rss_peak_bytes": 1219342336,
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
              "ttft_s": 0.204440376
            },
            {
              "begin_ns": 294810216305179,
              "complete": true,
              "e2e_s": 1.365887788,
              "end_ns": 294811582192967,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423309312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 359.57504673713873,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050709997,
                "rss_peak_bytes": 1219342336,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.734,
                "predicted_n": 128,
                "predicted_per_second": 97.04034586096182,
                "predicted_per_token_ms": 10.304992125984251
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057011623
            },
            {
              "begin_ns": 294811647176660,
              "complete": true,
              "e2e_s": 0.549126843,
              "end_ns": 294812196303503,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476020736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.69635004891595,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051557443,
                "rss_peak_bytes": 1272053760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.086,
                "predicted_n": 34,
                "predicted_per_second": 96.18579598118257,
                "predicted_per_token_ms": 10.396545454545455
              },
              "tool_call_valid": true,
              "ttft_s": 0.302356834,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294812267032100,
              "complete": true,
              "e2e_s": 0.523311862,
              "end_ns": 294812790343962,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476061696,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.05159837968586,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055635364,
                "rss_peak_bytes": 1272094720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.638,
                "predicted_n": 25,
                "predicted_per_second": 95.75563162808513,
                "predicted_per_token_ms": 10.44325
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272652599,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295090132793905,
              "complete": true,
              "e2e_s": 0.156646359,
              "end_ns": 295090289440264,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 29.444320299397226,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052616392,
                "rss_peak_bytes": 960307200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.747,
                "predicted_n": 10,
                "predicted_per_second": 93.99772316626108,
                "predicted_per_token_ms": 10.638555555555556
              },
              "ttft_s": 0.060832205,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295090367845428,
              "complete": true,
              "e2e_s": 0.148511069,
              "end_ns": 295090516356497,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.27056701343985,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0500737,
                "rss_peak_bytes": 960438272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.258,
                "predicted_n": 9,
                "predicted_per_second": 93.8328368012386,
                "predicted_per_token_ms": 10.65725
              },
              "ttft_s": 0.063234315,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295090586772144,
              "complete": true,
              "e2e_s": 0.526290553,
              "end_ns": 295091113062697,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.17132620560932,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050652512,
                "rss_peak_bytes": 961204224,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.141,
                "predicted_n": 39,
                "predicted_per_second": 96.4121976653025,
                "predicted_per_token_ms": 10.37213157894737
              },
              "ttft_s": 0.13215488,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295091187964965,
              "complete": true,
              "e2e_s": 0.306545347,
              "end_ns": 295091494510312,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422764544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.71541143215589,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050530773,
                "rss_peak_bytes": 964612096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.959,
                "predicted_n": 23,
                "predicted_per_second": 96.08707235793308,
                "predicted_per_token_ms": 10.407227272727273
              },
              "ttft_s": 0.077534082,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295091565794718,
              "complete": true,
              "e2e_s": 0.254631138,
              "end_ns": 295091820425856,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422764544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 57.8010181915452,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053744372,
                "rss_peak_bytes": 965005312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.431,
                "predicted_n": 18,
                "predicted_per_second": 95.27492420039118,
                "predicted_per_token_ms": 10.49594117647059
              },
              "ttft_s": 0.076171113,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295091897698916,
              "complete": true,
              "e2e_s": 0.399583064,
              "end_ns": 295092297281980,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475475968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 95.18730719643237,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052158887,
                "rss_peak_bytes": 1018175488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.174,
                "predicted_n": 29,
                "predicted_per_second": 96.4938278412263,
                "predicted_per_token_ms": 10.363357142857142
              },
              "ttft_s": 0.109469863,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295092367091647,
              "complete": true,
              "e2e_s": 1.027376598,
              "end_ns": 295093394468245,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475947008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 269.4060944557466,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0516503,
                "rss_peak_bytes": 1018712064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.542,
                "predicted_n": 16,
                "predicted_per_second": 94.01912975893495,
                "predicted_per_token_ms": 10.636133333333333
              },
              "ttft_s": 0.86774509,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295093468114251,
              "complete": true,
              "e2e_s": 0.204186158,
              "end_ns": 295093672300409,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.58650653965864,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05026969,
                "rss_peak_bytes": 966041600,
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
              "ttft_s": 0.203996289
            },
            {
              "begin_ns": 295093731089473,
              "complete": true,
              "e2e_s": 1.366106362,
              "end_ns": 295095097195835,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423276544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 348.5595789409681,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051228049,
                "rss_peak_bytes": 966041600,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.319,
                "predicted_n": 128,
                "predicted_per_second": 97.07112714865411,
                "predicted_per_token_ms": 10.301724409448818
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057667455
            },
            {
              "begin_ns": 295095167730821,
              "complete": true,
              "e2e_s": 0.550052541,
              "end_ns": 295095717783362,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475992064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.52708495525533,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053456936,
                "rss_peak_bytes": 1018757120,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.089,
                "predicted_n": 34,
                "predicted_per_second": 96.1849549242325,
                "predicted_per_token_ms": 10.396636363636363
              },
              "tool_call_valid": true,
              "ttft_s": 0.303324848,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295095802224854,
              "complete": true,
              "e2e_s": 0.523704202,
              "end_ns": 295096325929056,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476024832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.96033970093572,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055434217,
                "rss_peak_bytes": 1018789888,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 249.97,
                "predicted_n": 25,
                "predicted_per_second": 96.0115213825659,
                "predicted_per_token_ms": 10.415416666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27372477,
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
          "gpu_j_per_correct_token": 8.488359090256438,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 496631808,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6468141056,
              "gpu_energy_j": 2286.593457426755,
              "gpu_owned_peak_bytes": 6213861376,
              "max_sample_gap_s": 0.091183627,
              "rss_peak_bytes": 5996331008,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 496685056,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6468141056,
              "gpu_energy_j": 2314.097169492235,
              "gpu_owned_peak_bytes": 6213861376,
              "max_sample_gap_s": 0.056519113,
              "rss_peak_bytes": 5996756992,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4600.690626918989,
          "raw_requests": [
            {
              "begin_ns": 294782382669355,
              "complete": true,
              "e2e_s": 0.156577508,
              "end_ns": 294782539246863,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437493760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 31.488393240033222,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.050585647,
                "rss_peak_bytes": 1246302208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.393,
                "predicted_n": 10,
                "predicted_per_second": 94.34654534399799,
                "predicted_per_token_ms": 10.599222222222222
              },
              "ttft_s": 0.06110553,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294782595178918,
              "complete": true,
              "e2e_s": 0.14776559,
              "end_ns": 294782742944508,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437493760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 32.6285755814868,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.049980931,
                "rss_peak_bytes": 1246302208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 84.987,
                "predicted_n": 9,
                "predicted_per_second": 94.13204372433431,
                "predicted_per_token_ms": 10.623375
              },
              "ttft_s": 0.062740094,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 294782798750842,
              "complete": true,
              "e2e_s": 0.533587958,
              "end_ns": 294783332338800,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437493760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 135.07714763369316,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.058149817,
                "rss_peak_bytes": 1246347264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 401.888,
                "predicted_n": 39,
                "predicted_per_second": 94.55370650529501,
                "predicted_per_token_ms": 10.575999999999999
              },
              "ttft_s": 0.131720353,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 294783430118767,
              "complete": true,
              "e2e_s": 0.305801989,
              "end_ns": 294783735920756,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 440463360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 71.1975249711999,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.050709255,
                "rss_peak_bytes": 1249382400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.776,
                "predicted_n": 23,
                "predicted_per_second": 96.16393327971466,
                "predicted_per_token_ms": 10.398909090909092
              },
              "ttft_s": 0.077044462,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 294783807220189,
              "complete": true,
              "e2e_s": 0.253978681,
              "end_ns": 294784061198870,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 440463360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 58.694278552713975,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.051448367,
                "rss_peak_bytes": 1249382400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.918,
                "predicted_n": 18,
                "predicted_per_second": 95.54963522521611,
                "predicted_per_token_ms": 10.465764705882354
              },
              "ttft_s": 0.076072009,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 294784132330532,
              "complete": true,
              "e2e_s": 0.396929548,
              "end_ns": 294784529260080,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 493178880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 89.9514190713917,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.051045581,
                "rss_peak_bytes": 1302097920,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.001,
                "predicted_n": 29,
                "predicted_per_second": 96.55139120209931,
                "predicted_per_token_ms": 10.357178571428571
              },
              "ttft_s": 0.10689854,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294784624181463,
              "complete": true,
              "e2e_s": 1.046514506,
              "end_ns": 294785670695969,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496562176,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 279.0242713839508,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.091183627,
                "rss_peak_bytes": 1305665536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 161.945,
                "predicted_n": 16,
                "predicted_per_second": 92.62403902559512,
                "predicted_per_token_ms": 10.796333333333333
              },
              "ttft_s": 0.884501544,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 294785726700049,
              "complete": true,
              "e2e_s": 0.205731027,
              "end_ns": 294785932431076,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443879424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 49.16631251723152,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.051491715,
                "rss_peak_bytes": 1252982784,
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
              "ttft_s": 0.205597625
            },
            {
              "begin_ns": 294785982110351,
              "complete": true,
              "e2e_s": 1.362217464,
              "end_ns": 294787344327815,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443879424,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 347.721092555158,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.053339123,
                "rss_peak_bytes": 1252982784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1304.365,
                "predicted_n": 128,
                "predicted_per_second": 97.36538468910159,
                "predicted_per_token_ms": 10.270590551181103
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057737957
            },
            {
              "begin_ns": 294787403370879,
              "complete": true,
              "e2e_s": 0.551804464,
              "end_ns": 294787955175343,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496599040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 138.87754948808572,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.050550612,
                "rss_peak_bytes": 1305702400,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.433,
                "predicted_n": 34,
                "predicted_per_second": 95.80963496529078,
                "predicted_per_token_ms": 10.437363636363637
              },
              "tool_call_valid": true,
              "ttft_s": 0.30379213,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294788022292939,
              "complete": true,
              "e2e_s": 0.526876306,
              "end_ns": 294788549169245,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496631808,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 130.24844910585279,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.052403917,
                "rss_peak_bytes": 1305735168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 252.022,
                "predicted_n": 25,
                "predicted_per_second": 95.22978152700955,
                "predicted_per_token_ms": 10.500916666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.274914082,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295114429822487,
              "complete": true,
              "e2e_s": 0.159278182,
              "end_ns": 295114589100669,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437526528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 31.9340177927927,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.050012507,
                "rss_peak_bytes": 1169100800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 97.166,
                "predicted_n": 10,
                "predicted_per_second": 92.62499228125064,
                "predicted_per_token_ms": 10.796222222222221
              },
              "ttft_s": 0.062079526,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295114664668347,
              "complete": true,
              "e2e_s": 0.148603725,
              "end_ns": 295114813272072,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437526528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 31.872577857535408,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.055160207,
                "rss_peak_bytes": 1169231872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.465,
                "predicted_n": 9,
                "predicted_per_second": 93.60556953138712,
                "predicted_per_token_ms": 10.683125
              },
              "ttft_s": 0.063131928,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 295114897626984,
              "complete": true,
              "e2e_s": 0.524291527,
              "end_ns": 295115421918511,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 437526528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 133.84544760306022,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.051066645,
                "rss_peak_bytes": 1169539072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 391.951,
                "predicted_n": 39,
                "predicted_per_second": 96.95089437200058,
                "predicted_per_token_ms": 10.3145
              },
              "ttft_s": 0.132291893,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 295115496135876,
              "complete": true,
              "e2e_s": 0.306173344,
              "end_ns": 295115802309220,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 440500224,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 74.26502372097609,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.050030716,
                "rss_peak_bytes": 1173012480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.08,
                "predicted_n": 23,
                "predicted_per_second": 96.03631918980268,
                "predicted_per_token_ms": 10.412727272727274
              },
              "ttft_s": 0.077030993,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 295115873814001,
              "complete": true,
              "e2e_s": 0.253396787,
              "end_ns": 295116127210788,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 440500224,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 54.82323765922216,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.056038017,
                "rss_peak_bytes": 1173209088,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.514,
                "predicted_n": 18,
                "predicted_per_second": 95.7670944263551,
                "predicted_per_token_ms": 10.442
              },
              "ttft_s": 0.075856428,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 295116200117165,
              "complete": true,
              "e2e_s": 0.398231455,
              "end_ns": 295116598348620,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 493215744,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 96.67170185935196,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.051143823,
                "rss_peak_bytes": 1225924608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.426,
                "predicted_n": 29,
                "predicted_per_second": 96.07927913089429,
                "predicted_per_token_ms": 10.408071428571429
              },
              "ttft_s": 0.106795319,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295116673207690,
              "complete": true,
              "e2e_s": 1.045213641,
              "end_ns": 295117718421331,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496590848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 279.0151067541552,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.05646579,
                "rss_peak_bytes": 1229615104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 161.998,
                "predicted_n": 16,
                "predicted_per_second": 92.59373572513242,
                "predicted_per_token_ms": 10.799866666666667
              },
              "ttft_s": 0.883145195,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 295117799140389,
              "complete": true,
              "e2e_s": 0.208087211,
              "end_ns": 295118007227600,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443928576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 52.89499848053078,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.054245433,
                "rss_peak_bytes": 1176952832,
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
              "ttft_s": 0.207953204
            },
            {
              "begin_ns": 295118068152794,
              "complete": true,
              "e2e_s": 1.362140284,
              "end_ns": 295119430293078,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 443928576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 350.831007914695,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.052761936,
                "rss_peak_bytes": 1177018368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1304.77,
                "predicted_n": 128,
                "predicted_per_second": 97.33516251906467,
                "predicted_per_token_ms": 10.273779527559055
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057261101
            },
            {
              "begin_ns": 295119504103903,
              "complete": true,
              "e2e_s": 0.552800482,
              "end_ns": 295120056904385,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496648192,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 141.90000447794216,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.054151252,
                "rss_peak_bytes": 1229737984,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 345.472,
                "predicted_n": 34,
                "predicted_per_second": 95.52148944053354,
                "predicted_per_token_ms": 10.468848484848484
              },
              "tool_call_valid": true,
              "ttft_s": 0.304083254,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295120146059202,
              "complete": true,
              "e2e_s": 0.526681213,
              "end_ns": 295120672740415,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 496685056,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6468141056,
                "gpu_energy_j": 132.46927477322836,
                "gpu_owned_peak_bytes": 6213861376,
                "max_sample_gap_s": 0.05324248,
                "rss_peak_bytes": 1229774848,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 251.94,
                "predicted_n": 25,
                "predicted_per_second": 95.26077637532747,
                "predicted_per_token_ms": 10.4975
              },
              "tool_facts_valid": true,
              "ttft_s": 0.27472404,
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
          "gpu_j_per_correct_token": 26.64223074146484,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 685707264,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7694.427086118194,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.070160062,
              "rss_peak_bytes": 11821092864,
              "swap_peak_bytes": 164061184
            },
            {
              "anon_peak_bytes": 772694016,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7118.653206136257,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.08468596,
              "rss_peak_bytes": 12139851776,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14813.08029225445,
          "raw_requests": [
            {
              "begin_ns": 294875494179961,
              "complete": true,
              "e2e_s": 0.545496376,
              "end_ns": 294876039676337,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483364864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 111.79492051467426,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.0509435,
                "rss_peak_bytes": 1034567680,
                "swap_peak_bytes": 129368064
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 309.301,
                "predicted_n": 10,
                "predicted_per_second": 29.097869066055395,
                "predicted_per_token_ms": 34.36677777777778
              },
              "ttft_s": 0.232683987,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294876108993123,
              "complete": true,
              "e2e_s": 0.612946891,
              "end_ns": 294876721940014,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 483725312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.6541561830862,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050674157,
                "rss_peak_bytes": 1034993664,
                "swap_peak_bytes": 128540672
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 378.08,
                "predicted_n": 14,
                "predicted_per_second": 34.38425730004232,
                "predicted_per_token_ms": 29.083076923076923
              },
              "ttft_s": 0.227114014,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294876784099063,
              "complete": true,
              "e2e_s": 1.797233905,
              "end_ns": 294878581332968,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 484577280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 467.94576181875243,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052655535,
                "rss_peak_bytes": 1036017664,
                "swap_peak_bytes": 128483328
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1242.849,
                "predicted_n": 45,
                "predicted_per_second": 35.402530798190284,
                "predicted_per_token_ms": 28.24656818181818
              },
              "ttft_s": 0.544129525,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294878655591655,
              "complete": true,
              "e2e_s": 1.028294901,
              "end_ns": 294879683886556,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 488513536,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 267.6680669393736,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050675749,
                "rss_peak_bytes": 1040433152,
                "swap_peak_bytes": 126799872
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 766.02,
                "predicted_n": 28,
                "predicted_per_second": 35.24712148507872,
                "predicted_per_token_ms": 28.37111111111111
              },
              "ttft_s": 0.258258437,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294879748174935,
              "complete": true,
              "e2e_s": 0.884862679,
              "end_ns": 294880633037614,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 489136128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 221.41700938125348,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05070355,
                "rss_peak_bytes": 1041186816,
                "swap_peak_bytes": 126111744
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 626.745,
                "predicted_n": 23,
                "predicted_per_second": 35.10199522931974,
                "predicted_per_token_ms": 28.48840909090909
              },
              "ttft_s": 0.252499354,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294880698174648,
              "complete": true,
              "e2e_s": 1.1785891,
              "end_ns": 294881876763748,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 646664192,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 287.16602453330455,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053078576,
                "rss_peak_bytes": 1198882816,
                "swap_peak_bytes": 125542400
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.243,
                "predicted_n": 29,
                "predicted_per_second": 35.34269157316631,
                "predicted_per_token_ms": 28.29439285714286
              },
              "ttft_s": 0.383212486,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294881936957125,
              "complete": true,
              "e2e_s": 3.792268569,
              "end_ns": 294885729225694,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 647647232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1002.5946721110155,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053403545,
                "rss_peak_bytes": 1199865856,
                "swap_peak_bytes": 125104128
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 585.49,
                "predicted_n": 21,
                "predicted_per_second": 34.15942202257938,
                "predicted_per_token_ms": 29.2745
              },
              "ttft_s": 3.20029829,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 294885793183341,
              "complete": true,
              "e2e_s": 0.718208284,
              "end_ns": 294886511391625,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490835968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 189.41206114284688,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055817013,
                "rss_peak_bytes": 1043054592,
                "swap_peak_bytes": 124923904
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
              "ttft_s": 0.718085586
            },
            {
              "begin_ns": 294886567269366,
              "complete": true,
              "e2e_s": 3.774627352,
              "end_ns": 294890341896718,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 490852352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1033.125454367583,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053237505,
                "rss_peak_bytes": 1043070976,
                "swap_peak_bytes": 124919808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3580.198,
                "predicted_n": 128,
                "predicted_per_second": 35.47289842628816,
                "predicted_per_token_ms": 28.190535433070867
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.19434397
            },
            {
              "begin_ns": 294890410077226,
              "complete": true,
              "e2e_s": 1.705994384,
              "end_ns": 294892116071610,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 647782400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 445.2461202016781,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052028867,
                "rss_peak_bytes": 1200001024,
                "swap_peak_bytes": 124903424
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.519,
                "predicted_n": 34,
                "predicted_per_second": 35.08701046975128,
                "predicted_per_token_ms": 28.500575757575756
              },
              "tool_call_valid": true,
              "ttft_s": 1.02951812,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294892189754658,
              "complete": true,
              "e2e_s": 1.770051177,
              "end_ns": 294893959805835,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 647806976,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.62407224921697,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052692974,
                "rss_peak_bytes": 1200025600,
                "swap_peak_bytes": 124899328
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 680.589,
                "predicted_n": 25,
                "predicted_per_second": 35.26357316971035,
                "predicted_per_token_ms": 28.357875000000003
              },
              "tool_facts_valid": true,
              "ttft_s": 1.089392251,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 295041234994038,
              "complete": true,
              "e2e_s": 0.464876347,
              "end_ns": 295041699870385,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 761159680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 109.17537357839896,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050244036,
                "rss_peak_bytes": 1406476288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.618,
                "predicted_n": 10,
                "predicted_per_second": 34.27030896587439,
                "predicted_per_token_ms": 29.179777777777776
              },
              "ttft_s": 0.202237742,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 295041763931925,
              "complete": true,
              "e2e_s": 0.576938355,
              "end_ns": 295042340870280,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612261888,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 142.0251655353744,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050678355,
                "rss_peak_bytes": 1257578496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.409,
                "predicted_n": 14,
                "predicted_per_second": 35.001844327951126,
                "predicted_per_token_ms": 28.569923076923075
              },
              "ttft_s": 0.205510308,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 295042412614769,
              "complete": true,
              "e2e_s": 1.763738413,
              "end_ns": 295044176353182,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612261888,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 470.1215018782702,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.055360986,
                "rss_peak_bytes": 1257578496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1243.488,
                "predicted_n": 45,
                "predicted_per_second": 35.38433824853959,
                "predicted_per_token_ms": 28.26109090909091
              },
              "ttft_s": 0.520244904,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 295044247576460,
              "complete": true,
              "e2e_s": 0.988213193,
              "end_ns": 295045235789653,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615235584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 264.5336661576611,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050624946,
                "rss_peak_bytes": 1260875776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.549,
                "predicted_n": 28,
                "predicted_per_second": 35.314937302906685,
                "predicted_per_token_ms": 28.316629629629627
              },
              "ttft_s": 0.22371096,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 295045312678520,
              "complete": true,
              "e2e_s": 0.846646873,
              "end_ns": 295046159325393,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615235584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 219.46948440407832,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050718135,
                "rss_peak_bytes": 1260875776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.209,
                "predicted_n": 23,
                "predicted_per_second": 35.24460557281296,
                "predicted_per_token_ms": 28.373136363636362
              },
              "ttft_s": 0.222371464,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 295046228674790,
              "complete": true,
              "e2e_s": 1.145401217,
              "end_ns": 295047374076007,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772149248,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 286.90832110385224,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051544079,
                "rss_peak_bytes": 1417789440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 793.331,
                "predicted_n": 29,
                "predicted_per_second": 35.29422145359251,
                "predicted_per_token_ms": 28.33325
              },
              "ttft_s": 0.352037547,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 295047447228216,
              "complete": true,
              "e2e_s": 3.78480119,
              "end_ns": 295051232029406,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772612096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1016.638333992919,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056789896,
                "rss_peak_bytes": 1418252288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.105,
                "predicted_n": 21,
                "predicted_per_second": 34.41718794365906,
                "predicted_per_token_ms": 29.05525
              },
              "ttft_s": 3.203688243,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 295051305970779,
              "complete": true,
              "e2e_s": 0.72515976,
              "end_ns": 295052031130539,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615735296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.76773605218304,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054596168,
                "rss_peak_bytes": 1261375488,
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
              "ttft_s": 0.725014747
            },
            {
              "begin_ns": 295052094910653,
              "complete": true,
              "e2e_s": 3.780174085,
              "end_ns": 295055875084738,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615735296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1053.096078471075,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.080636956,
                "rss_peak_bytes": 1261375488,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3583.399,
                "predicted_n": 128,
                "predicted_per_second": 35.44121098431964,
                "predicted_per_token_ms": 28.215740157480315
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196718834
            },
            {
              "begin_ns": 295055943130986,
              "complete": true,
              "e2e_s": 1.7043472,
              "end_ns": 295057647478186,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772657152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.9994398417838,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052185456,
                "rss_peak_bytes": 1418297344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 940.102,
                "predicted_n": 34,
                "predicted_per_second": 35.10257397601537,
                "predicted_per_token_ms": 28.487939393939392
              },
              "tool_call_valid": true,
              "ttft_s": 1.027985106,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295057727118229,
              "complete": true,
              "e2e_s": 1.774297321,
              "end_ns": 295059501415550,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772694016,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.6832574983618,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.059488823,
                "rss_peak_bytes": 1418334208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.275,
                "predicted_n": 25,
                "predicted_per_second": 35.228065025136694,
                "predicted_per_token_ms": 28.386458333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 1.092988295,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            }
          ],
          "requests": 22
        },
        "B": {
          "correct_tokens": 514,
          "gpu_j_per_correct_token": 27.950006731800986,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 767504384,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13403422720,
              "gpu_energy_j": 7186.178730848167,
              "gpu_owned_peak_bytes": 13149143040,
              "max_sample_gap_s": 0.086835078,
              "rss_peak_bytes": 12139737088,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 767418368,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13403422720,
              "gpu_energy_j": 7180.12472929754,
              "gpu_owned_peak_bytes": 13149143040,
              "max_sample_gap_s": 0.089230413,
              "rss_peak_bytes": 12139798528,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14366.303460145708,
          "raw_requests": [
            {
              "begin_ns": 294931815864052,
              "complete": true,
              "e2e_s": 0.467957747,
              "end_ns": 294932283821799,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602603520,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 102.74419528511798,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.052175868,
                "rss_peak_bytes": 1259036672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 259.929,
                "predicted_n": 10,
                "predicted_per_second": 34.62483986011565,
                "predicted_per_token_ms": 28.880999999999997
              },
              "ttft_s": 0.207969519,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294932345934259,
              "complete": true,
              "e2e_s": 0.590829855,
              "end_ns": 294932936764114,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602603520,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 144.9763283234094,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.052768178,
                "rss_peak_bytes": 1259036672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 376.031,
                "predicted_n": 14,
                "predicted_per_second": 34.57161776555657,
                "predicted_per_token_ms": 28.92546153846154
              },
              "ttft_s": 0.214826083,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294933001126079,
              "complete": true,
              "e2e_s": 1.766664243,
              "end_ns": 294934767790322,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602615808,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 471.58416284974845,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.05061417,
                "rss_peak_bytes": 1258655744,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1245.603,
                "predicted_n": 45,
                "predicted_per_second": 35.32425660503387,
                "predicted_per_token_ms": 28.30915909090909
              },
              "ttft_s": 0.52107825,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294934849152826,
              "complete": true,
              "e2e_s": 0.99341914,
              "end_ns": 294935842571966,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605601792,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 261.30103178466305,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.050702129,
                "rss_peak_bytes": 1261965312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.184,
                "predicted_n": 28,
                "predicted_per_second": 35.285630645700905,
                "predicted_per_token_ms": 28.340148148148145
              },
              "ttft_s": 0.228199984,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294935911744267,
              "complete": true,
              "e2e_s": 0.850170787,
              "end_ns": 294936761915054,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605601792,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 223.85815033473668,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.052012902,
                "rss_peak_bytes": 1261965312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.972,
                "predicted_n": 23,
                "predicted_per_second": 35.201577030650974,
                "predicted_per_token_ms": 28.407818181818183
              },
              "ttft_s": 0.225119641,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294936830853900,
              "complete": true,
              "e2e_s": 1.152036283,
              "end_ns": 294937982890183,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 762515456,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 293.8306217232518,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.051088752,
                "rss_peak_bytes": 1418878976,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 793.57,
                "predicted_n": 29,
                "predicted_per_second": 35.28359186965233,
                "predicted_per_token_ms": 28.341785714285717
              },
              "ttft_s": 0.358405999,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294938048826751,
              "complete": true,
              "e2e_s": 3.962302658,
              "end_ns": 294942011129409,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767422464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 1057.9284810341508,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.056873969,
                "rss_peak_bytes": 1424035840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 726.923,
                "predicted_n": 26,
                "predicted_per_second": 34.39153803085058,
                "predicted_per_token_ms": 29.07692
              },
              "ttft_s": 3.235368655,
              "usage": {
                "completion_tokens": 26,
                "total_tokens": 2228
              }
            },
            {
              "begin_ns": 294942083416849,
              "complete": true,
              "e2e_s": 0.725060237,
              "end_ns": 294942808477086,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 688156672,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 193.57418424097403,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.059287838,
                "rss_peak_bytes": 1344770048,
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
              "ttft_s": 0.724927777
            },
            {
              "begin_ns": 294942876778009,
              "complete": true,
              "e2e_s": 3.783813814,
              "end_ns": 294946660591823,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 610541568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 1045.5001839128117,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.053364483,
                "rss_peak_bytes": 1267154944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3584.435,
                "predicted_n": 128,
                "predicted_per_second": 35.430967502549215,
                "predicted_per_token_ms": 28.223897637795275
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.199196388
            },
            {
              "begin_ns": 294946754757888,
              "complete": true,
              "e2e_s": 1.710162043,
              "end_ns": 294948464919931,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767455232,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 456.0140648902754,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.055215241,
                "rss_peak_bytes": 1424068608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 945.262,
                "predicted_n": 34,
                "predicted_per_second": 34.910955904288976,
                "predicted_per_token_ms": 28.64430303030303
              },
              "tool_call_valid": true,
              "ttft_s": 1.027976614,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 294948569166678,
              "complete": true,
              "e2e_s": 1.780452271,
              "end_ns": 294950349618949,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767504384,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 461.48845325937543,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.05083812,
                "rss_peak_bytes": 1424117760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 688.092,
                "predicted_n": 25,
                "predicted_per_second": 34.87905687030223,
                "predicted_per_token_ms": 28.6705
              },
              "tool_facts_valid": true,
              "ttft_s": 1.092308516,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 294986704174589,
              "complete": true,
              "e2e_s": 0.467781629,
              "end_ns": 294987171956218,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602558464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 108.56283875895122,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.050722728,
                "rss_peak_bytes": 1259368448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 260.826,
                "predicted_n": 10,
                "predicted_per_second": 34.505762462331205,
                "predicted_per_token_ms": 28.980666666666668
              },
              "ttft_s": 0.206913098,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 294987234077296,
              "complete": true,
              "e2e_s": 0.576958319,
              "end_ns": 294987811035615,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602558464,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 140.1426861382777,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.050675113,
                "rss_peak_bytes": 1259368448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 373.061,
                "predicted_n": 14,
                "predicted_per_second": 34.84684810258912,
                "predicted_per_token_ms": 28.697
              },
              "ttft_s": 0.203852757,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 294987877162506,
              "complete": true,
              "e2e_s": 1.76591292,
              "end_ns": 294989643075426,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 602566656,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13401325568,
                "gpu_energy_j": 475.497654043323,
                "gpu_owned_peak_bytes": 13147045888,
                "max_sample_gap_s": 0.054827637,
                "rss_peak_bytes": 1259376640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1244.918,
                "predicted_n": 45,
                "predicted_per_second": 35.34369331956,
                "predicted_per_token_ms": 28.293590909090906
              },
              "ttft_s": 0.521022725,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 294989711307780,
              "complete": true,
              "e2e_s": 0.992402931,
              "end_ns": 294990703710711,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605548544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 259.4082899487962,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.050715951,
                "rss_peak_bytes": 1262682112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 767.189,
                "predicted_n": 28,
                "predicted_per_second": 35.19341387845759,
                "predicted_per_token_ms": 28.414407407407406
              },
              "ttft_s": 0.225127211,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 294990772718409,
              "complete": true,
              "e2e_s": 0.849571443,
              "end_ns": 294991622289852,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605548544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 218.36298907564228,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.050730213,
                "rss_peak_bytes": 1262682112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.304,
                "predicted_n": 23,
                "predicted_per_second": 35.23924242035932,
                "predicted_per_token_ms": 28.377454545454544
              },
              "ttft_s": 0.22522288,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 294991687617373,
              "complete": true,
              "e2e_s": 1.153832,
              "end_ns": 294992841449373,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 762462208,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 295.31125822871945,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.053423979,
                "rss_peak_bytes": 1419595776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 794.361,
                "predicted_n": 29,
                "predicted_per_second": 35.24845756526315,
                "predicted_per_token_ms": 28.370035714285713
              },
              "ttft_s": 0.359401093,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 294992910968551,
              "complete": true,
              "e2e_s": 3.961787781,
              "end_ns": 294996872756332,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767344640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 1066.0291945086408,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.058068065,
                "rss_peak_bytes": 1424728064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 726.373,
                "predicted_n": 26,
                "predicted_per_second": 34.417578847231376,
                "predicted_per_token_ms": 29.054920000000003
              },
              "ttft_s": 3.235387457,
              "usage": {
                "completion_tokens": 26,
                "total_tokens": 2228
              }
            },
            {
              "begin_ns": 294996943657185,
              "complete": true,
              "e2e_s": 0.72500076,
              "end_ns": 294997668657945,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 610471936,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 189.9983758092487,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.050717642,
                "rss_peak_bytes": 1267855360,
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
              "ttft_s": 0.724873045
            },
            {
              "begin_ns": 294997724295072,
              "complete": true,
              "e2e_s": 3.778332016,
              "end_ns": 295001502627088,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 610471936,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 1046.2302435729905,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.05196227,
                "rss_peak_bytes": 1267855360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3582.813,
                "predicted_n": 128,
                "predicted_per_second": 35.44700770037398,
                "predicted_per_token_ms": 28.211125984251968
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.19540032
            },
            {
              "begin_ns": 295001575158593,
              "complete": true,
              "e2e_s": 1.709074638,
              "end_ns": 295003284233231,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767385600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 455.8605978661175,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.051844235,
                "rss_peak_bytes": 1424769024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 943.789,
                "predicted_n": 34,
                "predicted_per_second": 34.965442487674686,
                "predicted_per_token_ms": 28.599666666666668
              },
              "tool_call_valid": true,
              "ttft_s": 1.027512959,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 295003360297779,
              "complete": true,
              "e2e_s": 1.781397177,
              "end_ns": 295005141694956,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 767418368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13403422720,
                "gpu_energy_j": 461.74584415480234,
                "gpu_owned_peak_bytes": 13149143040,
                "max_sample_gap_s": 0.053405929,
                "rss_peak_bytes": 1424801792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 687.899,
                "predicted_n": 25,
                "predicted_per_second": 34.8888426934768,
                "predicted_per_token_ms": 28.662458333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093456904,
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
