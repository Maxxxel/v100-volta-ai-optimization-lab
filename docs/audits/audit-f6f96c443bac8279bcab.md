# Public audit excerpt

Original SHA256: `f6f96c443bac8279bcab67ee55efbe7381c60457e0adc825864d5259758f7abf`

Original file: `RESULTS.json`; 266255 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.665281775371431,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470310912,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2691.7805292765297,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.241659513,
              "rss_peak_bytes": 7729143808,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470310912,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2740.107828482214,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.073697059,
              "rss_peak_bytes": 7726166016,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5431.888357758744,
          "raw_requests": [
            {
              "begin_ns": 292752834758907,
              "complete": true,
              "e2e_s": 0.181550827,
              "end_ns": 292753016309734,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 42.44115863141239,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050063765,
                "rss_peak_bytes": 1475584000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.791,
                "predicted_n": 10,
                "predicted_per_second": 77.72624815400161,
                "predicted_per_token_ms": 12.865666666666666
              },
              "ttft_s": 0.065681975,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292753072180230,
              "complete": true,
              "e2e_s": 0.234126141,
              "end_ns": 292753306306371,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 58.8929853768905,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050023634,
                "rss_peak_bytes": 1475584000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 167.123,
                "predicted_n": 14,
                "predicted_per_second": 77.78701914159033,
                "predicted_per_token_ms": 12.855615384615383
              },
              "ttft_s": 0.066966193,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292753358151161,
              "complete": true,
              "e2e_s": 0.665675487,
              "end_ns": 292754023826648,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414040064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.15335418299932,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05107316,
                "rss_peak_bytes": 1475649536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.221,
                "predicted_n": 44,
                "predicted_per_second": 79.30345744631802,
                "predicted_per_token_ms": 12.609790697674418
              },
              "ttft_s": 0.123447594,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292754078723768,
              "complete": true,
              "e2e_s": 0.357787912,
              "end_ns": 292754436511680,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414044160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 91.12129574370341,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050665501,
                "rss_peak_bytes": 1475653632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.529,
                "predicted_n": 23,
                "predicted_per_second": 78.70381963946495,
                "predicted_per_token_ms": 12.705863636363636
              },
              "ttft_s": 0.0782039,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292754489739215,
              "complete": true,
              "e2e_s": 0.295206927,
              "end_ns": 292754784946142,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414044160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 68.25812554726684,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05018822,
                "rss_peak_bytes": 1475653632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.804,
                "predicted_n": 18,
                "predicted_per_second": 78.4118374199738,
                "predicted_per_token_ms": 12.753176470588235
              },
              "ttft_s": 0.078427981,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292754839879479,
              "complete": true,
              "e2e_s": 0.468247333,
              "end_ns": 292755308126812,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469741568,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 118.37301014098485,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050613123,
                "rss_peak_bytes": 1531351040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.578,
                "predicted_n": 29,
                "predicted_per_second": 79.19044736946303,
                "predicted_per_token_ms": 12.627785714285713
              },
              "ttft_s": 0.114582269,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292755364815302,
              "complete": true,
              "e2e_s": 1.071780547,
              "end_ns": 292756436595849,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470212608,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 287.78611336651176,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055601734,
                "rss_peak_bytes": 1531822080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.804,
                "predicted_n": 21,
                "predicted_per_second": 77.88040684724538,
                "predicted_per_token_ms": 12.8402
              },
              "ttft_s": 0.814996128,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292756490781231,
              "complete": true,
              "e2e_s": 0.196637045,
              "end_ns": 292756687418276,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417550336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 45.536701765941174,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050390222,
                "rss_peak_bytes": 1479159808,
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
              "ttft_s": 0.196506162
            },
            {
              "begin_ns": 292756735685554,
              "complete": true,
              "e2e_s": 1.657786535,
              "end_ns": 292758393472089,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417550336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 446.44987211188254,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050884098,
                "rss_peak_bytes": 1479159808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.638,
                "predicted_n": 128,
                "predicted_per_second": 79.64189991709718,
                "predicted_per_token_ms": 12.556204724409449
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063018486
            },
            {
              "begin_ns": 292758452101223,
              "complete": true,
              "e2e_s": 0.618969914,
              "end_ns": 292759071071137,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470269952,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 159.33061362871214,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.054951117,
                "rss_peak_bytes": 1531879424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.137,
                "predicted_n": 34,
                "predicted_per_second": 78.92150180443252,
                "predicted_per_token_ms": 12.670818181818182
              },
              "tool_call_valid": true,
              "ttft_s": 0.31803613,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292759133738912,
              "complete": true,
              "e2e_s": 0.557217218,
              "end_ns": 292759690956130,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470310912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.1362366660097,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050424279,
                "rss_peak_bytes": 1531920384,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.23,
                "predicted_n": 25,
                "predicted_per_second": 78.88768366038852,
                "predicted_per_token_ms": 12.676250000000001
              },
              "tool_facts_valid": true,
              "ttft_s": 0.25300632,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293239006798553,
              "complete": true,
              "e2e_s": 0.182729753,
              "end_ns": 293239189528306,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 37.20487895231241,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056691114,
                "rss_peak_bytes": 1470582784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.554,
                "predicted_n": 10,
                "predicted_per_second": 77.2174271153285,
                "predicted_per_token_ms": 12.950444444444445
              },
              "ttft_s": 0.066141702,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293239273076055,
              "complete": true,
              "e2e_s": 0.233325704,
              "end_ns": 293239506401759,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 58.50862504824396,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050007046,
                "rss_peak_bytes": 1470582784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.174,
                "predicted_n": 14,
                "predicted_per_second": 78.2312515796695,
                "predicted_per_token_ms": 12.782615384615385
              },
              "ttft_s": 0.067117798,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 293239587247628,
              "complete": true,
              "e2e_s": 0.666354243,
              "end_ns": 293240253601871,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414060544,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 172.63222041170727,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051393488,
                "rss_peak_bytes": 1470627840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.525,
                "predicted_n": 44,
                "predicted_per_second": 79.25902032164417,
                "predicted_per_token_ms": 12.616860465116279
              },
              "ttft_s": 0.123830481,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 293240332081778,
              "complete": true,
              "e2e_s": 0.358061196,
              "end_ns": 293240690142974,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 87.79883834481575,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052401037,
                "rss_peak_bytes": 1470636032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.207,
                "predicted_n": 23,
                "predicted_per_second": 78.79458609562082,
                "predicted_per_token_ms": 12.691227272727273
              },
              "ttft_s": 0.078806508,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 293240765307167,
              "complete": true,
              "e2e_s": 0.295517209,
              "end_ns": 293241060824376,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 74.35073853914922,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050060227,
                "rss_peak_bytes": 1470640128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.395,
                "predicted_n": 18,
                "predicted_per_second": 78.560040666374,
                "predicted_per_token_ms": 12.729117647058825
              },
              "ttft_s": 0.079107419,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 293241141322208,
              "complete": true,
              "e2e_s": 0.46895941,
              "end_ns": 293241610281618,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469766144,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 116.51166186453779,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050351392,
                "rss_peak_bytes": 1526333440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.158,
                "predicted_n": 29,
                "predicted_per_second": 79.06075819267107,
                "predicted_per_token_ms": 12.6485
              },
              "ttft_s": 0.114726165,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293241688082529,
              "complete": true,
              "e2e_s": 1.081732165,
              "end_ns": 293242769814694,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470237184,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 286.4199005931313,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056063846,
                "rss_peak_bytes": 1526804480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 257.487,
                "predicted_n": 21,
                "predicted_per_second": 77.67382430957679,
                "predicted_per_token_ms": 12.874350000000002
              },
              "ttft_s": 0.824153731,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 293242849302595,
              "complete": true,
              "e2e_s": 0.197993599,
              "end_ns": 293243047296194,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417554432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.01319446680072,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.057654907,
                "rss_peak_bytes": 1474121728,
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
              "ttft_s": 0.197863843
            },
            {
              "begin_ns": 293243115214278,
              "complete": true,
              "e2e_s": 1.659257443,
              "end_ns": 293244774471721,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417554432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 449.50187725333967,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050509136,
                "rss_peak_bytes": 1474121728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.843,
                "predicted_n": 128,
                "predicted_per_second": 79.58176336895295,
                "predicted_per_token_ms": 12.565692913385828
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063233104
            },
            {
              "begin_ns": 293244853412515,
              "complete": true,
              "e2e_s": 0.618522129,
              "end_ns": 293245471934644,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470274048,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 160.83539738383385,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052414128,
                "rss_peak_bytes": 1526841344,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.53,
                "predicted_n": 34,
                "predicted_per_second": 79.03623691710776,
                "predicted_per_token_ms": 12.652424242424242
              },
              "tool_call_valid": true,
              "ttft_s": 0.317497746,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293245561318405,
              "complete": true,
              "e2e_s": 0.558747919,
              "end_ns": 293246120066324,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470310912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 140.28584223813755,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052758502,
                "rss_peak_bytes": 1526878208,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 303.803,
                "predicted_n": 25,
                "predicted_per_second": 78.99856156785812,
                "predicted_per_token_ms": 12.658458333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254946194,
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
          "gpu_j_per_correct_token": 11.991514661283246,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 469696512,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7625768960,
              "gpu_energy_j": 3133.7593738240885,
              "gpu_owned_peak_bytes": 7371489280,
              "max_sample_gap_s": 0.054744106,
              "rss_peak_bytes": 7729287168,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 374202368,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7625768960,
              "gpu_energy_j": 3605.471865817096,
              "gpu_owned_peak_bytes": 7371489280,
              "max_sample_gap_s": 0.119021731,
              "rss_peak_bytes": 7364407296,
              "swap_peak_bytes": 177676288
            }
          ],
          "lifecycle_gpu_j": 6739.231239641184,
          "raw_requests": [
            {
              "begin_ns": 292782231345318,
              "complete": true,
              "e2e_s": 0.181898139,
              "end_ns": 292782413243457,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 406048768,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 44.52178498091721,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050617514,
                "rss_peak_bytes": 1436409856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 115.724,
                "predicted_n": 10,
                "predicted_per_second": 77.77124883343126,
                "predicted_per_token_ms": 12.858222222222222
              },
              "ttft_s": 0.066111802,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292782466940924,
              "complete": true,
              "e2e_s": 0.233043951,
              "end_ns": 292782699984875,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 406048768,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 59.2263124992449,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050610371,
                "rss_peak_bytes": 1436409856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.075,
                "predicted_n": 14,
                "predicted_per_second": 78.27788649706459,
                "predicted_per_token_ms": 12.774999999999999
              },
              "ttft_s": 0.066940853,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292782761139939,
              "complete": true,
              "e2e_s": 0.665829668,
              "end_ns": 292783426969607,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 406048768,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 182.4359146462027,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050579185,
                "rss_peak_bytes": 1436409856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.167,
                "predicted_n": 44,
                "predicted_per_second": 79.31135609507771,
                "predicted_per_token_ms": 12.608534883720932
              },
              "ttft_s": 0.12360463,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 292783482291533,
              "complete": true,
              "e2e_s": 0.358042853,
              "end_ns": 292783840334386,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 406052864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 92.77330737873355,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050684649,
                "rss_peak_bytes": 1436413952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.368,
                "predicted_n": 23,
                "predicted_per_second": 78.74917671315254,
                "predicted_per_token_ms": 12.698545454545455
              },
              "ttft_s": 0.078644435,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292783892136299,
              "complete": true,
              "e2e_s": 0.295192085,
              "end_ns": 292784187328384,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 406052864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 70.4308082947022,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.051655395,
                "rss_peak_bytes": 1436413952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.529,
                "predicted_n": 18,
                "predicted_per_second": 78.51142341210647,
                "predicted_per_token_ms": 12.737
              },
              "ttft_s": 0.078612612,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292784244187079,
              "complete": true,
              "e2e_s": 0.469487639,
              "end_ns": 292784713674718,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 458764288,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 112.02558934458784,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.053164793,
                "rss_peak_bytes": 1489125376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.98,
                "predicted_n": 29,
                "predicted_per_second": 78.87768324976055,
                "predicted_per_token_ms": 12.677857142857144
              },
              "ttft_s": 0.114452236,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292784773787446,
              "complete": true,
              "e2e_s": 1.867065265,
              "end_ns": 292786640852711,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469614592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 506.3605852125214,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.054744106,
                "rss_peak_bytes": 1499975680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.33,
                "predicted_n": 21,
                "predicted_per_second": 78.02442164397456,
                "predicted_per_token_ms": 12.8165
              },
              "ttft_s": 1.610743066,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292786694225122,
              "complete": true,
              "e2e_s": 0.393374232,
              "end_ns": 292787087599354,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469626880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 99.85518046937203,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.051934525,
                "rss_peak_bytes": 1499987968,
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
              "ttft_s": 0.393245465
            },
            {
              "begin_ns": 292787136892294,
              "complete": true,
              "e2e_s": 1.662243821,
              "end_ns": 292788799136115,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 416931840,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 448.78125861953686,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.053324264,
                "rss_peak_bytes": 1447292928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1597.671,
                "predicted_n": 128,
                "predicted_per_second": 79.49070866279729,
                "predicted_per_token_ms": 12.58008661417323
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.064479571
            },
            {
              "begin_ns": 292788862108968,
              "complete": true,
              "e2e_s": 0.735275565,
              "end_ns": 292789597384533,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469655552,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 192.86023983296906,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.053915957,
                "rss_peak_bytes": 1500016640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.146,
                "predicted_n": 34,
                "predicted_per_second": 79.10899301443618,
                "predicted_per_token_ms": 12.64078787878788
              },
              "tool_call_valid": true,
              "ttft_s": 0.433904908,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292789663734496,
              "complete": true,
              "e2e_s": 0.670211994,
              "end_ns": 292790333946490,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469696512,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 179.76366354324418,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.053754871,
                "rss_peak_bytes": 1500057600,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.105,
                "predicted_n": 25,
                "predicted_per_second": 78.92010983048617,
                "predicted_per_token_ms": 12.671041666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.366089558,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293206104045898,
              "complete": true,
              "e2e_s": 0.228688754,
              "end_ns": 293206332734652,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 315744256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 44.9515821324228,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.051316119,
                "rss_peak_bytes": 1180389376,
                "swap_peak_bytes": 142991360
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 122.009,
                "predicted_n": 10,
                "predicted_per_second": 73.7650501192535,
                "predicted_per_token_ms": 13.556555555555555
              },
              "ttft_s": 0.103681972,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293206404062088,
              "complete": true,
              "e2e_s": 0.255742875,
              "end_ns": 293206659804963,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 264175616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 59.36069465649773,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.053935254,
                "rss_peak_bytes": 1129541632,
                "swap_peak_bytes": 142282752
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 171.317,
                "predicted_n": 14,
                "predicted_per_second": 75.88272033715276,
                "predicted_per_token_ms": 13.178230769230769
              },
              "ttft_s": 0.082067389,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 293206794045810,
              "complete": true,
              "e2e_s": 0.702737015,
              "end_ns": 293207496782825,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 265048064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 179.06013465290167,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.05177099,
                "rss_peak_bytes": 1131003904,
                "swap_peak_bytes": 141352960
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 548.487,
                "predicted_n": 44,
                "predicted_per_second": 78.39748252921218,
                "predicted_per_token_ms": 12.755511627906976
              },
              "ttft_s": 0.14599437,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 293207589117740,
              "complete": true,
              "e2e_s": 0.39930439,
              "end_ns": 293207988422130,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 266084352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 95.47373215764279,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050790926,
                "rss_peak_bytes": 1132367872,
                "swap_peak_bytes": 140550144
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 281.746,
                "predicted_n": 23,
                "predicted_per_second": 78.08451584050883,
                "predicted_per_token_ms": 12.806636363636363
              },
              "ttft_s": 0.113812536,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 293208070759145,
              "complete": true,
              "e2e_s": 0.329134091,
              "end_ns": 293208399893236,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 266825728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 73.82593281916188,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050192744,
                "rss_peak_bytes": 1133568000,
                "swap_peak_bytes": 139227136
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.827,
                "predicted_n": 18,
                "predicted_per_second": 78.4035198568444,
                "predicted_per_token_ms": 12.754529411764706
              },
              "ttft_s": 0.108020319,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 293208489597738,
              "complete": true,
              "e2e_s": 0.503909898,
              "end_ns": 293208993507636,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 320176128,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7617380352,
                "gpu_energy_j": 121.29900565332593,
                "gpu_owned_peak_bytes": 7363100672,
                "max_sample_gap_s": 0.050771663,
                "rss_peak_bytes": 1187246080,
                "swap_peak_bytes": 138866688
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 357.196,
                "predicted_n": 29,
                "predicted_per_second": 78.38833581563063,
                "predicted_per_token_ms": 12.757000000000001
              },
              "ttft_s": 0.141904094,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293209082809829,
              "complete": true,
              "e2e_s": 1.89906964,
              "end_ns": 293210981879469,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331812864,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 509.4983592266252,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.05361718,
                "rss_peak_bytes": 1199144960,
                "swap_peak_bytes": 138186752
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.67,
                "predicted_n": 21,
                "predicted_per_second": 77.92106596018233,
                "predicted_per_token_ms": 12.8335
              },
              "ttft_s": 1.638714315,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 293211056126373,
              "complete": true,
              "e2e_s": 0.39992971,
              "end_ns": 293211456056083,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331894784,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 103.74299149168156,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.057590446,
                "rss_peak_bytes": 1148370944,
                "swap_peak_bytes": 137744384
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
              "ttft_s": 0.399784986
            },
            {
              "begin_ns": 293211560786812,
              "complete": true,
              "e2e_s": 1.663923017,
              "end_ns": 293213224709829,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 279212032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 476.7794329780995,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.054582048,
                "rss_peak_bytes": 987086848,
                "swap_peak_bytes": 137732096
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1595.414,
                "predicted_n": 128,
                "predicted_per_second": 79.60316256470108,
                "predicted_per_token_ms": 12.562314960629921
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.068415388
            },
            {
              "begin_ns": 293213300035492,
              "complete": true,
              "e2e_s": 0.735156207,
              "end_ns": 293214035191699,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331931648,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 191.0101312161594,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.051503799,
                "rss_peak_bytes": 1039405056,
                "swap_peak_bytes": 137719808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.346,
                "predicted_n": 34,
                "predicted_per_second": 79.07108250708045,
                "predicted_per_token_ms": 12.646848484848485
              },
              "tool_call_valid": true,
              "ttft_s": 0.433678312,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293214124258648,
              "complete": true,
              "e2e_s": 0.673098546,
              "end_ns": 293214797357194,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 331980800,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7625768960,
                "gpu_energy_j": 181.8553632184833,
                "gpu_owned_peak_bytes": 7371489280,
                "max_sample_gap_s": 0.052627919,
                "rss_peak_bytes": 1039519744,
                "swap_peak_bytes": 137719808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 306.09,
                "predicted_n": 25,
                "predicted_per_second": 78.40831128099579,
                "predicted_per_token_ms": 12.753749999999998
              },
              "tool_facts_valid": true,
              "ttft_s": 0.366016679,
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
          "gpu_j_per_correct_token": 8.782279462589216,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476020736,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2264.8564356292122,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.082345856,
              "rss_peak_bytes": 5998923776,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476016640,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2495.139033094143,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.05956109,
              "rss_peak_bytes": 5992058880,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4759.995468723355,
          "raw_requests": [
            {
              "begin_ns": 292840478706795,
              "complete": true,
              "e2e_s": 0.161871947,
              "end_ns": 292840640578742,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.66652339962819,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054327875,
                "rss_peak_bytes": 1219792896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 98.876,
                "predicted_n": 10,
                "predicted_per_second": 91.02309963995307,
                "predicted_per_token_ms": 10.986222222222223
              },
              "ttft_s": 0.063028097,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292840720496764,
              "complete": true,
              "e2e_s": 0.152526971,
              "end_ns": 292840873023735,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.122487493370514,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051809465,
                "rss_peak_bytes": 1219792896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 86.512,
                "predicted_n": 9,
                "predicted_per_second": 92.4727205474385,
                "predicted_per_token_ms": 10.814
              },
              "ttft_s": 0.066063099,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292840929696956,
              "complete": true,
              "e2e_s": 0.525676724,
              "end_ns": 292841455373680,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419823616,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 129.98817147750862,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050542754,
                "rss_peak_bytes": 1219858432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.437,
                "predicted_n": 39,
                "predicted_per_second": 96.58471368986648,
                "predicted_per_token_ms": 10.353605263157895
              },
              "ttft_s": 0.132086852,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292841528107306,
              "complete": true,
              "e2e_s": 0.307155167,
              "end_ns": 292841835262473,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.40920822678149,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050137287,
                "rss_peak_bytes": 1222889472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.963,
                "predicted_n": 23,
                "predicted_per_second": 95.66756391245548,
                "predicted_per_token_ms": 10.452863636363636
              },
              "ttft_s": 0.077248773,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292841894111853,
              "complete": true,
              "e2e_s": 0.254221197,
              "end_ns": 292842148333050,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422789120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 53.92987326274057,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050154229,
                "rss_peak_bytes": 1222889472,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.937,
                "predicted_n": 18,
                "predicted_per_second": 95.53943249577097,
                "predicted_per_token_ms": 10.466882352941177
              },
              "ttft_s": 0.076226906,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292842212594651,
              "complete": true,
              "e2e_s": 0.398268728,
              "end_ns": 292842610863379,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475508736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 93.18260009128521,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050649974,
                "rss_peak_bytes": 1275609088,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.822,
                "predicted_n": 29,
                "predicted_per_second": 96.27882347277716,
                "predicted_per_token_ms": 10.3865
              },
              "ttft_s": 0.107395689,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292842673671322,
              "complete": true,
              "e2e_s": 1.028251299,
              "end_ns": 292843701922621,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475942912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 275.28412664063484,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.082345856,
                "rss_peak_bytes": 1276043264,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.677,
                "predicted_n": 16,
                "predicted_per_second": 93.93964064956131,
                "predicted_per_token_ms": 10.645133333333332
              },
              "ttft_s": 0.868650632,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292843766586450,
              "complete": true,
              "e2e_s": 0.205107891,
              "end_ns": 292843971694341,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 50.362217779221226,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051049059,
                "rss_peak_bytes": 1223368704,
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
              "ttft_s": 0.204973784
            },
            {
              "begin_ns": 292844026217438,
              "complete": true,
              "e2e_s": 1.364857801,
              "end_ns": 292845391075239,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423268352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 363.23262170046036,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051275875,
                "rss_peak_bytes": 1223368704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1307.32,
                "predicted_n": 128,
                "predicted_per_second": 97.14530489857114,
                "predicted_per_token_ms": 10.293858267716535
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057438794
            },
            {
              "begin_ns": 292845458779709,
              "complete": true,
              "e2e_s": 0.551476436,
              "end_ns": 292846010256145,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.65657641264906,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050918574,
                "rss_peak_bytes": 1276088320,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.054,
                "predicted_n": 34,
                "predicted_per_second": 95.91517610607639,
                "predicted_per_token_ms": 10.425878787878787
              },
              "tool_call_valid": true,
              "ttft_s": 0.304744015,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292846081176708,
              "complete": true,
              "e2e_s": 0.523884337,
              "end_ns": 292846605061045,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476020736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.264931767,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050472062,
                "rss_peak_bytes": 1276121088,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.143,
                "predicted_n": 25,
                "predicted_per_second": 95.94511939170795,
                "predicted_per_token_ms": 10.422625
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273708831,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293137251197155,
              "complete": true,
              "e2e_s": 0.157222393,
              "end_ns": 293137408419548,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.88988620541123,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050007499,
                "rss_peak_bytes": 1210310656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.548,
                "predicted_n": 10,
                "predicted_per_second": 94.19349436932222,
                "predicted_per_token_ms": 10.616444444444445
              },
              "ttft_s": 0.061618817,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293137480350804,
              "complete": true,
              "e2e_s": 0.148533851,
              "end_ns": 293137628884655,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 28.86297397447045,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050668531,
                "rss_peak_bytes": 1210310656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.261,
                "predicted_n": 9,
                "predicted_per_second": 93.82953519194005,
                "predicted_per_token_ms": 10.657625
              },
              "ttft_s": 0.063232562,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 293137701181788,
              "complete": true,
              "e2e_s": 0.537340982,
              "end_ns": 293138238522770,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419790848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.5039731103683,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055974513,
                "rss_peak_bytes": 1210363904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 404.488,
                "predicted_n": 39,
                "predicted_per_second": 93.94592670239908,
                "predicted_per_token_ms": 10.644421052631579
              },
              "ttft_s": 0.132896315,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 293138337936992,
              "complete": true,
              "e2e_s": 0.306447647,
              "end_ns": 293138644384639,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 68.15403235501688,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055276617,
                "rss_peak_bytes": 1213431808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.223,
                "predicted_n": 23,
                "predicted_per_second": 95.97640725407136,
                "predicted_per_token_ms": 10.419227272727273
              },
              "ttft_s": 0.077166496,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 293138716929005,
              "complete": true,
              "e2e_s": 0.254702304,
              "end_ns": 293138971631309,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422756352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.52532591551655,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050127913,
                "rss_peak_bytes": 1213431808,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.646,
                "predicted_n": 18,
                "predicted_per_second": 95.6959346115308,
                "predicted_per_token_ms": 10.449764705882352
              },
              "ttft_s": 0.077008477,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 293139044693403,
              "complete": true,
              "e2e_s": 0.398805712,
              "end_ns": 293139443499115,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475471872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 90.37101739931317,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0534631,
                "rss_peak_bytes": 1266147328,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.428,
                "predicted_n": 29,
                "predicted_per_second": 96.07861976199953,
                "predicted_per_token_ms": 10.408142857142858
              },
              "ttft_s": 0.107402643,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293139515733670,
              "complete": true,
              "e2e_s": 1.029503871,
              "end_ns": 293140545237541,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475938816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 277.48472275592803,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053410022,
                "rss_peak_bytes": 1266614272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.252,
                "predicted_n": 16,
                "predicted_per_second": 94.19033983874614,
                "predicted_per_token_ms": 10.616800000000001
              },
              "ttft_s": 0.870216048,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 293140615084051,
              "complete": true,
              "e2e_s": 0.205200751,
              "end_ns": 293140820284802,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 50.12632813649083,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052270402,
                "rss_peak_bytes": 1213939712,
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
              "ttft_s": 0.205069423
            },
            {
              "begin_ns": 293140885093317,
              "complete": true,
              "e2e_s": 1.366625876,
              "end_ns": 293142251719193,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423264256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 350.9294486078133,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050755686,
                "rss_peak_bytes": 1213939712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.875,
                "predicted_n": 128,
                "predicted_per_second": 97.02989208289563,
                "predicted_per_token_ms": 10.306102362204724
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057661928
            },
            {
              "begin_ns": 293142324109601,
              "complete": true,
              "e2e_s": 0.550345899,
              "end_ns": 293142874455500,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475975680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 139.4581936012643,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052168889,
                "rss_peak_bytes": 1266651136,
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
              "ttft_s": 0.302966904,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293142952785706,
              "complete": true,
              "e2e_s": 0.523168879,
              "end_ns": 293143475954585,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476016640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.52249802349513,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052030049,
                "rss_peak_bytes": 1266692096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.029,
                "predicted_n": 25,
                "predicted_per_second": 95.98886529162618,
                "predicted_per_token_ms": 10.417875
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273151525,
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
          "gpu_j_per_correct_token": 10.92424997579714,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 475832320,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6157762560,
              "gpu_energy_j": 3009.7946254237786,
              "gpu_owned_peak_bytes": 5903482880,
              "max_sample_gap_s": 0.056872832,
              "rss_peak_bytes": 5998845952,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 475791360,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6157762560,
              "gpu_energy_j": 2911.148861458271,
              "gpu_owned_peak_bytes": 5903482880,
              "max_sample_gap_s": 0.067332021,
              "rss_peak_bytes": 5997858816,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5920.94348688205,
          "raw_requests": [
            {
              "begin_ns": 292814992831999,
              "complete": true,
              "e2e_s": 0.157266443,
              "end_ns": 292815150098442,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 33.57045945829925,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050745301,
                "rss_peak_bytes": 1180536832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.086,
                "predicted_n": 10,
                "predicted_per_second": 93.66609079366401,
                "predicted_per_token_ms": 10.676222222222222
              },
              "ttft_s": 0.061135371,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292815204865183,
              "complete": true,
              "e2e_s": 0.148990211,
              "end_ns": 292815353855394,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 29.27106353722263,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050424137,
                "rss_peak_bytes": 1180536832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.772,
                "predicted_n": 9,
                "predicted_per_second": 93.27053117567505,
                "predicted_per_token_ms": 10.7215
              },
              "ttft_s": 0.06322142,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 292815415188513,
              "complete": true,
              "e2e_s": 0.527274574,
              "end_ns": 292815942463087,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 138.35871442856276,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.051653887,
                "rss_peak_bytes": 1180536832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 395.03,
                "predicted_n": 39,
                "predicted_per_second": 96.19522567906236,
                "predicted_per_token_ms": 10.395526315789473
              },
              "ttft_s": 0.132220045,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 292815998712689,
              "complete": true,
              "e2e_s": 0.305460929,
              "end_ns": 292816304173618,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411992064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 73.95962688625896,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.052178421,
                "rss_peak_bytes": 1180540928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.472,
                "predicted_n": 23,
                "predicted_per_second": 95.87226328266628,
                "predicted_per_token_ms": 10.430545454545454
              },
              "ttft_s": 0.07596758,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 292816361698570,
              "complete": true,
              "e2e_s": 0.254447414,
              "end_ns": 292816616145984,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411992064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 62.21460197730683,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050070254,
                "rss_peak_bytes": 1180540928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.918,
                "predicted_n": 18,
                "predicted_per_second": 95.54963522521611,
                "predicted_per_token_ms": 10.465764705882354
              },
              "ttft_s": 0.076472705,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 292816672748225,
              "complete": true,
              "e2e_s": 0.401132233,
              "end_ns": 292817073880458,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464707584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 99.40112140893851,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.051191463,
                "rss_peak_bytes": 1233256448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.862,
                "predicted_n": 29,
                "predicted_per_second": 96.2655829912467,
                "predicted_per_token_ms": 10.387928571428573
              },
              "ttft_s": 0.110214191,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292817136856320,
              "complete": true,
              "e2e_s": 1.954736059,
              "end_ns": 292819091592379,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475758592,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 516.5861619305756,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.056212274,
                "rss_peak_bytes": 1244307456,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.92,
                "predicted_n": 16,
                "predicted_per_second": 94.38711301283665,
                "predicted_per_token_ms": 10.594666666666665
              },
              "ttft_s": 1.795766415,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 292819150246076,
              "complete": true,
              "e2e_s": 0.434978919,
              "end_ns": 292819585224995,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475779072,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 111.62961108533094,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.05062927,
                "rss_peak_bytes": 1244327936,
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
              "ttft_s": 0.434843636
            },
            {
              "begin_ns": 292819633738285,
              "complete": true,
              "e2e_s": 1.371574812,
              "end_ns": 292821005313097,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423084032,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 369.1916273521542,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.050934339,
                "rss_peak_bytes": 1191632896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1310.959,
                "predicted_n": 128,
                "predicted_per_second": 96.87564599655671,
                "predicted_per_token_ms": 10.322511811023622
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.060354691
            },
            {
              "begin_ns": 292821067575871,
              "complete": true,
              "e2e_s": 0.678732055,
              "end_ns": 292821746307926,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475795456,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 175.94462285112283,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.053315832,
                "rss_peak_bytes": 1244344320,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.367,
                "predicted_n": 34,
                "predicted_per_second": 95.82799745620224,
                "predicted_per_token_ms": 10.435363636363636
              },
              "tool_call_valid": true,
              "ttft_s": 0.43017229,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292821815287396,
              "complete": true,
              "e2e_s": 0.646658435,
              "end_ns": 292822461945831,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475832320,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 160.3660419697409,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.05233855,
                "rss_peak_bytes": 1244381184,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.423,
                "predicted_n": 25,
                "predicted_per_second": 95.83784237070876,
                "predicted_per_token_ms": 10.434291666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.396204742,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293162669140187,
              "complete": true,
              "e2e_s": 0.156906814,
              "end_ns": 293162826047001,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 36.49194012449121,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050394897,
                "rss_peak_bytes": 1176936448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 96.509,
                "predicted_n": 10,
                "predicted_per_second": 93.25555129573407,
                "predicted_per_token_ms": 10.723222222222223
              },
              "ttft_s": 0.06043006,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293162933584275,
              "complete": true,
              "e2e_s": 0.148346605,
              "end_ns": 293163081930880,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 33.78942232603117,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050059153,
                "rss_peak_bytes": 1176936448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.016,
                "predicted_n": 9,
                "predicted_per_second": 94.09993413004611,
                "predicted_per_token_ms": 10.627
              },
              "ttft_s": 0.063318299,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 293163190225501,
              "complete": true,
              "e2e_s": 0.526254644,
              "end_ns": 293163716480145,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 139.08276784002743,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050532255,
                "rss_peak_bytes": 1176936448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.396,
                "predicted_n": 39,
                "predicted_per_second": 96.34986156046207,
                "predicted_per_token_ms": 10.378842105263159
              },
              "ttft_s": 0.13185018,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 293163831325695,
              "complete": true,
              "e2e_s": 0.305747133,
              "end_ns": 293164137072828,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 76.54211901354212,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050124332,
                "rss_peak_bytes": 1176936448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.827,
                "predicted_n": 23,
                "predicted_per_second": 95.72417514043173,
                "predicted_per_token_ms": 10.446681818181817
              },
              "ttft_s": 0.07592915,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 293164252257226,
              "complete": true,
              "e2e_s": 0.253969427,
              "end_ns": 293164506226653,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 411987968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 62.946551283055136,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.050941243,
                "rss_peak_bytes": 1176936448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.941,
                "predicted_n": 18,
                "predicted_per_second": 95.53728483036512,
                "predicted_per_token_ms": 10.467117647058824
              },
              "ttft_s": 0.075934703,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 293164583049675,
              "complete": true,
              "e2e_s": 0.398894841,
              "end_ns": 293164981944516,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 464703488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6149373952,
                "gpu_energy_j": 99.41074932038624,
                "gpu_owned_peak_bytes": 5895094272,
                "max_sample_gap_s": 0.05257116,
                "rss_peak_bytes": 1229651968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 292.026,
                "predicted_n": 29,
                "predicted_per_second": 95.88187353180881,
                "predicted_per_token_ms": 10.4295
              },
              "ttft_s": 0.106848754,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293165054819037,
              "complete": true,
              "e2e_s": 1.952227822,
              "end_ns": 293167007046859,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475717632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 535.766256474297,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.05100003,
                "rss_peak_bytes": 1240666112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 158.747,
                "predicted_n": 16,
                "predicted_per_second": 94.48997461369348,
                "predicted_per_token_ms": 10.583133333333334
              },
              "ttft_s": 1.793400263,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 293167085316390,
              "complete": true,
              "e2e_s": 0.435772808,
              "end_ns": 293167521089198,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475729920,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 108.9245281916936,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.050400537,
                "rss_peak_bytes": 1240678400,
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
              "ttft_s": 0.435631745
            },
            {
              "begin_ns": 293167586272841,
              "complete": true,
              "e2e_s": 1.370052902,
              "end_ns": 293168956325743,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423034880,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 374.6016881056166,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.051913883,
                "rss_peak_bytes": 1187983360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1310.895,
                "predicted_n": 128,
                "predicted_per_second": 96.88037562123588,
                "predicted_per_token_ms": 10.322007874015748
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.058980412
            },
            {
              "begin_ns": 293169027202583,
              "complete": true,
              "e2e_s": 0.676790092,
              "end_ns": 293169703992675,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475750400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 173.98485097126277,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.053522063,
                "rss_peak_bytes": 1240698880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.811,
                "predicted_n": 34,
                "predicted_per_second": 96.26295538941282,
                "predicted_per_token_ms": 10.38821212121212
              },
              "tool_call_valid": true,
              "ttft_s": 0.429811179,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293169799972655,
              "complete": true,
              "e2e_s": 0.644961904,
              "end_ns": 293170444934559,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475791360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6157762560,
                "gpu_energy_j": 166.11982060827762,
                "gpu_owned_peak_bytes": 5903482880,
                "max_sample_gap_s": 0.056264256,
                "rss_peak_bytes": 1240739840,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.597,
                "predicted_n": 25,
                "predicted_per_second": 95.77129814004158,
                "predicted_per_token_ms": 10.441541666666668
              },
              "tool_facts_valid": true,
              "ttft_s": 0.394350216,
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
          "gpu_j_per_correct_token": 26.45580748169722,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 773029888,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7550.573037242246,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.084022783,
              "rss_peak_bytes": 11910426624,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772706304,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7158.85592258141,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.071741857,
              "rss_peak_bytes": 12141015040,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14709.428959823656,
          "raw_requests": [
            {
              "begin_ns": 292907215279349,
              "complete": true,
              "e2e_s": 0.466300837,
              "end_ns": 292907681580186,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612245504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.96116846169762,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051166482,
                "rss_peak_bytes": 1073741824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.136,
                "predicted_n": 10,
                "predicted_per_second": 34.33332316049684,
                "predicted_per_token_ms": 29.126222222222225
              },
              "ttft_s": 0.204145194,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292907745854491,
              "complete": true,
              "e2e_s": 0.57420757,
              "end_ns": 292908320062061,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612245504,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 138.04689814944837,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050894895,
                "rss_peak_bytes": 1074135040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.961,
                "predicted_n": 14,
                "predicted_per_second": 35.04411514957098,
                "predicted_per_token_ms": 28.53546153846154
              },
              "ttft_s": 0.203237136,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292908384056360,
              "complete": true,
              "e2e_s": 1.767005288,
              "end_ns": 292910151061648,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612249600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 469.57409876760687,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.054390915,
                "rss_peak_bytes": 1074925568,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1246.409,
                "predicted_n": 45,
                "predicted_per_second": 35.30141390185725,
                "predicted_per_token_ms": 28.327477272727275
              },
              "ttft_s": 0.520567317,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292910216098506,
              "complete": true,
              "e2e_s": 0.989002224,
              "end_ns": 292911205100730,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615223296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 261.56075020941205,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052800433,
                "rss_peak_bytes": 1078771712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.509,
                "predicted_n": 28,
                "predicted_per_second": 35.31678502149745,
                "predicted_per_token_ms": 28.31514814814815
              },
              "ttft_s": 0.224482352,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292911276217751,
              "complete": true,
              "e2e_s": 0.844724871,
              "end_ns": 292912120942622,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615223296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 219.7329122947822,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051219777,
                "rss_peak_bytes": 1079296000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.249,
                "predicted_n": 23,
                "predicted_per_second": 35.298893379692544,
                "predicted_per_token_ms": 28.3295
              },
              "ttft_s": 0.221466547,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292912223182558,
              "complete": true,
              "e2e_s": 1.143385834,
              "end_ns": 292913366568392,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772145152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 297.22316576030255,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051188198,
                "rss_peak_bytes": 1236631552,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.407,
                "predicted_n": 29,
                "predicted_per_second": 35.38002570106153,
                "predicted_per_token_ms": 28.264535714285717
              },
              "ttft_s": 0.351912436,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292913441153650,
              "complete": true,
              "e2e_s": 3.773845092,
              "end_ns": 292917214998742,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772612096,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1008.6537964122524,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055259421,
                "rss_peak_bytes": 1237295104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.872,
                "predicted_n": 21,
                "predicted_per_second": 34.49037028861542,
                "predicted_per_token_ms": 28.993599999999997
              },
              "ttft_s": 3.193912566,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292917278289969,
              "complete": true,
              "e2e_s": 0.719440174,
              "end_ns": 292917997730143,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615727104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 178.3289413207162,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054885814,
                "rss_peak_bytes": 1080410112,
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
              "ttft_s": 0.719283254
            },
            {
              "begin_ns": 292918063039037,
              "complete": true,
              "e2e_s": 3.775092699,
              "end_ns": 292921838131736,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615727104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1039.3468044251845,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054095572,
                "rss_peak_bytes": 1080410112,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3578.204,
                "predicted_n": 128,
                "predicted_per_second": 35.492666153187464,
                "predicted_per_token_ms": 28.174834645669293
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.196751134
            },
            {
              "begin_ns": 292921903008286,
              "complete": true,
              "e2e_s": 1.700331207,
              "end_ns": 292923603339493,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772997120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 446.5290697655888,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052389671,
                "rss_peak_bytes": 1237680128,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.095,
                "predicted_n": 34,
                "predicted_per_second": 35.14021478125216,
                "predicted_per_token_ms": 28.457424242424242
              },
              "tool_call_valid": true,
              "ttft_s": 1.024905472,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292923673129715,
              "complete": true,
              "e2e_s": 1.774181227,
              "end_ns": 292925447310942,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 773029888,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 450.79410253785187,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055011397,
                "rss_peak_bytes": 1237712896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.806,
                "predicted_n": 25,
                "predicted_per_second": 35.20062891790333,
                "predicted_per_token_ms": 28.408583333333336
              },
              "tool_facts_valid": true,
              "ttft_s": 1.092270095,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293089483218182,
              "complete": true,
              "e2e_s": 0.4698414,
              "end_ns": 293089953059582,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 106.26305397266654,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051279242,
                "rss_peak_bytes": 1249280000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 263.647,
                "predicted_n": 10,
                "predicted_per_second": 34.136553801105265,
                "predicted_per_token_ms": 29.29411111111111
              },
              "ttft_s": 0.206187725,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293090023235329,
              "complete": true,
              "e2e_s": 0.574655231,
              "end_ns": 293090597890560,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 145.06599621748197,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053069112,
                "rss_peak_bytes": 1249280000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 372.338,
                "predicted_n": 14,
                "predicted_per_second": 34.914513157399995,
                "predicted_per_token_ms": 28.641384615384617
              },
              "ttft_s": 0.202248424,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 293090668309173,
              "complete": true,
              "e2e_s": 1.768613135,
              "end_ns": 293092436922308,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612270080,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 477.8818690335903,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.055379872,
                "rss_peak_bytes": 1249280000,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1248.43,
                "predicted_n": 45,
                "predicted_per_second": 35.24426679909967,
                "predicted_per_token_ms": 28.373409090909092
              },
              "ttft_s": 0.5201546,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 293092504403822,
              "complete": true,
              "e2e_s": 0.9914872,
              "end_ns": 293093495891022,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 267.8484471327913,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05475374,
                "rss_peak_bytes": 1252581376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 765.939,
                "predicted_n": 28,
                "predicted_per_second": 35.25084895794574,
                "predicted_per_token_ms": 28.36811111111111
              },
              "ttft_s": 0.225561437,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 293093565980112,
              "complete": true,
              "e2e_s": 0.848996121,
              "end_ns": 293094414976233,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 227.8369891375314,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053068826,
                "rss_peak_bytes": 1252581376,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.5,
                "predicted_n": 23,
                "predicted_per_second": 35.28468323977546,
                "predicted_per_token_ms": 28.34090909090909
              },
              "ttft_s": 0.2254533,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 293094496747740,
              "complete": true,
              "e2e_s": 1.148987262,
              "end_ns": 293095645735002,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772165632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 295.8882715987728,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053928298,
                "rss_peak_bytes": 1409503232,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 792.411,
                "predicted_n": 29,
                "predicted_per_second": 35.33519852702701,
                "predicted_per_token_ms": 28.300392857142857
              },
              "ttft_s": 0.356512742,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293095718784895,
              "complete": true,
              "e2e_s": 3.788396304,
              "end_ns": 293099507181199,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772628480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1017.5991926460069,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054249253,
                "rss_peak_bytes": 1410031616,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.037,
                "predicted_n": 21,
                "predicted_per_second": 34.48055899882249,
                "predicted_per_token_ms": 29.00185
              },
              "ttft_s": 3.208361145,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 293099578258352,
              "complete": true,
              "e2e_s": 0.722291564,
              "end_ns": 293100300549916,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615747584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 182.6006168632591,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053285271,
                "rss_peak_bytes": 1253150720,
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
              "ttft_s": 0.722162742
            },
            {
              "begin_ns": 293100362190448,
              "complete": true,
              "e2e_s": 3.772751262,
              "end_ns": 293104134941710,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615747584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1056.2974374658743,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054707191,
                "rss_peak_bytes": 1253150720,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3577.002,
                "predicted_n": 128,
                "predicted_per_second": 35.504592952422165,
                "predicted_per_token_ms": 28.165370078740157
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195661585
            },
            {
              "begin_ns": 293104203460978,
              "complete": true,
              "e2e_s": 1.708706561,
              "end_ns": 293105912167539,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772669440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.2690553986795,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052125818,
                "rss_peak_bytes": 1410072576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 941.686,
                "predicted_n": 34,
                "predicted_per_second": 35.043528309861244,
                "predicted_per_token_ms": 28.535939393939394
              },
              "tool_call_valid": true,
              "ttft_s": 1.030836945,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293105988121680,
              "complete": true,
              "e2e_s": 1.776667441,
              "end_ns": 293107764789121,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772706304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 462.745768861891,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053761255,
                "rss_peak_bytes": 1410109440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 683.209,
                "predicted_n": 25,
                "predicted_per_second": 35.128342864335806,
                "predicted_per_token_ms": 28.467041666666663
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093431213,
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
          "gpu_j_per_correct_token": 32.3211925044391,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 800169984,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12944146432,
              "gpu_energy_j": 8947.642419134569,
              "gpu_owned_peak_bytes": 12689866752,
              "max_sample_gap_s": 0.084338825,
              "rss_peak_bytes": 12140515328,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 800100352,
              "energy_complete": true,
              "gpu_device_peak_bytes": 12944146432,
              "gpu_energy_j": 9022.940613333567,
              "gpu_owned_peak_bytes": 12689866752,
              "max_sample_gap_s": 0.079297873,
              "rss_peak_bytes": 12141002752,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 17970.583032468137,
          "raw_requests": [
            {
              "begin_ns": 292964581662534,
              "complete": true,
              "e2e_s": 0.467517896,
              "end_ns": 292965049180430,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618835968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 104.59535109580463,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.051270708,
                "rss_peak_bytes": 1227419648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.441,
                "predicted_n": 10,
                "predicted_per_second": 34.29342214059541,
                "predicted_per_token_ms": 29.160111111111107
              },
              "ttft_s": 0.205034974,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 292965144704397,
              "complete": true,
              "e2e_s": 0.573514297,
              "end_ns": 292965718218694,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618835968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 138.307291728107,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.052292449,
                "rss_peak_bytes": 1227419648,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 369.841,
                "predicted_n": 14,
                "predicted_per_second": 35.1502402383727,
                "predicted_per_token_ms": 28.44930769230769
              },
              "ttft_s": 0.20363132,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 292965813179707,
              "complete": true,
              "e2e_s": 1.757880401,
              "end_ns": 292967571060108,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618852352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 477.2225980453058,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.05075878,
                "rss_peak_bytes": 1227436032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1238.591,
                "predicted_n": 45,
                "predicted_per_second": 35.52423681425103,
                "predicted_per_token_ms": 28.14979545454545
              },
              "ttft_s": 0.519272352,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 292967676185137,
              "complete": true,
              "e2e_s": 0.988357266,
              "end_ns": 292968664542403,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618868736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 259.1953714802111,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.050938324,
                "rss_peak_bytes": 1227452416,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 762.437,
                "predicted_n": 28,
                "predicted_per_second": 35.41276197246461,
                "predicted_per_token_ms": 28.238407407407408
              },
              "ttft_s": 0.225912741,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 292968728546050,
              "complete": true,
              "e2e_s": 0.846749486,
              "end_ns": 292969575295536,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618868736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 223.0917042934674,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.05218198,
                "rss_peak_bytes": 1227452416,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 621.368,
                "predicted_n": 23,
                "predicted_per_second": 35.40574989378275,
                "predicted_per_token_ms": 28.244000000000003
              },
              "ttft_s": 0.22528397,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 292969638094761,
              "complete": true,
              "e2e_s": 1.148045343,
              "end_ns": 292970786140104,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 778768384,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 286.00866704114486,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.051029307,
                "rss_peak_bytes": 1387352064,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.663,
                "predicted_n": 29,
                "predicted_per_second": 35.36858486502464,
                "predicted_per_token_ms": 28.273678571428572
              },
              "ttft_s": 0.356304854,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 292970850954640,
              "complete": true,
              "e2e_s": 8.512958649,
              "end_ns": 292979363913289,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800088064,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 2000.2442815487416,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.057482424,
                "rss_peak_bytes": 1408671744,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 577.573,
                "predicted_n": 21,
                "predicted_per_second": 34.62765745628691,
                "predicted_per_token_ms": 28.87865
              },
              "ttft_s": 7.935365305,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 292979431190565,
              "complete": true,
              "e2e_s": 1.896473245,
              "end_ns": 292981327663810,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800112640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 431.9385235088738,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.051185347,
                "rss_peak_bytes": 1408696320,
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
              "ttft_s": 1.896289771
            },
            {
              "begin_ns": 292981385895227,
              "complete": true,
              "e2e_s": 3.769567071,
              "end_ns": 292985155462298,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 643215360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 1049.9564022681823,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.054046885,
                "rss_peak_bytes": 1251799040,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3569.4,
                "predicted_n": 128,
                "predicted_per_second": 35.58020955902953,
                "predicted_per_token_ms": 28.10551181102362
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.200060607
            },
            {
              "begin_ns": 292985223675930,
              "complete": true,
              "e2e_s": 2.225068758,
              "end_ns": 292987448744688,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800129024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 554.8407267905848,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.053376517,
                "rss_peak_bytes": 1408712704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.271,
                "predicted_n": 34,
                "predicted_per_second": 35.208600287430215,
                "predicted_per_token_ms": 28.402151515151512
              },
              "tool_call_valid": true,
              "ttft_s": 1.550144957,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 292987528047195,
              "complete": true,
              "e2e_s": 2.349415897,
              "end_ns": 292989877463092,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800169984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 549.4946035886875,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.05508355,
                "rss_peak_bytes": 1408753664,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.45,
                "predicted_n": 25,
                "predicted_per_second": 35.21901826986573,
                "predicted_per_token_ms": 28.39375
              },
              "tool_facts_valid": true,
              "ttft_s": 1.66802153,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 293028198217586,
              "complete": true,
              "e2e_s": 0.463373756,
              "end_ns": 293028661591342,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618819584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 106.99437538641118,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.051340964,
                "rss_peak_bytes": 1228140544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.059,
                "predicted_n": 10,
                "predicted_per_second": 34.3434112165581,
                "predicted_per_token_ms": 29.11766666666667
              },
              "ttft_s": 0.2012867,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 293028728909294,
              "complete": true,
              "e2e_s": 0.574967987,
              "end_ns": 293029303877281,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618819584,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 136.4170158387709,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.053628218,
                "rss_peak_bytes": 1228140544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.555,
                "predicted_n": 14,
                "predicted_per_second": 35.08251136808301,
                "predicted_per_token_ms": 28.50423076923077
              },
              "ttft_s": 0.204468981,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 293029367732545,
              "complete": true,
              "e2e_s": 1.759793978,
              "end_ns": 293031127526523,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618835968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 475.30673475462186,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.079297873,
                "rss_peak_bytes": 1228156928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1239.003,
                "predicted_n": 45,
                "predicted_per_second": 35.51242410228224,
                "predicted_per_token_ms": 28.15915909090909
              },
              "ttft_s": 0.520702716,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 293031195188136,
              "complete": true,
              "e2e_s": 0.984327326,
              "end_ns": 293032179515462,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618848256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 260.22306006010916,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.05144809,
                "rss_peak_bytes": 1228169216,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 762.539,
                "predicted_n": 28,
                "predicted_per_second": 35.40802503216229,
                "predicted_per_token_ms": 28.242185185185186
              },
              "ttft_s": 0.221731822,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 293032246170027,
              "complete": true,
              "e2e_s": 0.84620478,
              "end_ns": 293033092374807,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 618852352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12925272064,
                "gpu_energy_j": 218.40394747877406,
                "gpu_owned_peak_bytes": 12670992384,
                "max_sample_gap_s": 0.0541716,
                "rss_peak_bytes": 1228173312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 623.87,
                "predicted_n": 23,
                "predicted_per_second": 35.26375687242535,
                "predicted_per_token_ms": 28.357727272727274
              },
              "ttft_s": 0.222302183,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 293033163673153,
              "complete": true,
              "e2e_s": 1.148607088,
              "end_ns": 293034312280241,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 778743808,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12927369216,
                "gpu_energy_j": 296.45475471175064,
                "gpu_owned_peak_bytes": 12673089536,
                "max_sample_gap_s": 0.053521714,
                "rss_peak_bytes": 1388064768,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.641,
                "predicted_n": 29,
                "predicted_per_second": 35.36956777124985,
                "predicted_per_token_ms": 28.272892857142857
              },
              "ttft_s": 0.35691884,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 293034382859985,
              "complete": true,
              "e2e_s": 8.503552757,
              "end_ns": 293042886412742,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800018432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 2037.268071781151,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.055475825,
                "rss_peak_bytes": 1409339392,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 578.352,
                "predicted_n": 21,
                "predicted_per_second": 34.58101640523418,
                "predicted_per_token_ms": 28.9176
              },
              "ttft_s": 7.925220617,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 293042953841910,
              "complete": true,
              "e2e_s": 1.895333529,
              "end_ns": 293044849175439,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800043008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 440.2520265478208,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.05254184,
                "rss_peak_bytes": 1409363968,
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
              "ttft_s": 1.89518449
            },
            {
              "begin_ns": 293044908149016,
              "complete": true,
              "e2e_s": 3.781034751,
              "end_ns": 293048689183767,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 643145728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 1054.6560908905108,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.056284749,
                "rss_peak_bytes": 1252466688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3580.459,
                "predicted_n": 128,
                "predicted_per_second": 35.47031260517158,
                "predicted_per_token_ms": 28.1925905511811
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.200415648
            },
            {
              "begin_ns": 293048761161542,
              "complete": true,
              "e2e_s": 2.227091996,
              "end_ns": 293050988253538,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800059392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 557.8410600537779,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.051941392,
                "rss_peak_bytes": 1409380352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 938.324,
                "predicted_n": 34,
                "predicted_per_second": 35.16908871562488,
                "predicted_per_token_ms": 28.434060606060605
              },
              "tool_call_valid": true,
              "ttft_s": 1.551689776,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 293051066980614,
              "complete": true,
              "e2e_s": 2.342809762,
              "end_ns": 293053409790376,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 800100352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 12944146432,
                "gpu_energy_j": 569.6021333690489,
                "gpu_owned_peak_bytes": 12689866752,
                "max_sample_gap_s": 0.054623238,
                "rss_peak_bytes": 1409421312,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.031,
                "predicted_n": 25,
                "predicted_per_second": 35.18901633503462,
                "predicted_per_token_ms": 28.41795833333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.660749894,
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
