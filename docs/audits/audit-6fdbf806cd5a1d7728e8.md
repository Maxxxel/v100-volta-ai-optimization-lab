# Public audit excerpt

Original SHA256: `6fdbf806cd5a1d7728e814168e4b1f7c03e72a665b279a91b501543b00ffa92d`

Original file: `RESULTS.json`; 266251 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "gpu_j_per_correct_token": 9.626426568458866,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470323200,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2701.5047216058692,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.206036309,
              "rss_peak_bytes": 7725658112,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470319104,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2708.5470098680134,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.057709764,
              "rss_peak_bytes": 7726272512,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5410.051731473883,
          "raw_requests": [
            {
              "begin_ns": 288194723176580,
              "complete": true,
              "e2e_s": 0.182577999,
              "end_ns": 288194905754579,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414064640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 41.84337367434739,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050079757,
                "rss_peak_bytes": 1464844288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.007,
                "predicted_n": 10,
                "predicted_per_second": 77.58152525278646,
                "predicted_per_token_ms": 12.889666666666667
              },
              "ttft_s": 0.066522089,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288194956992705,
              "complete": true,
              "e2e_s": 0.233973914,
              "end_ns": 288195190966619,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414064640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 55.9515930049452,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050735156,
                "rss_peak_bytes": 1464844288,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.39,
                "predicted_n": 14,
                "predicted_per_second": 78.12969529418837,
                "predicted_per_token_ms": 12.799230769230768
              },
              "ttft_s": 0.067498939,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288195253089718,
              "complete": true,
              "e2e_s": 0.66588028,
              "end_ns": 288195918969998,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414064640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 175.71415688276005,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050714871,
                "rss_peak_bytes": 1464954880,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.024,
                "predicted_n": 44,
                "predicted_per_second": 79.33228048942482,
                "predicted_per_token_ms": 12.605209302325582
              },
              "ttft_s": 0.123835591,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288195980215152,
              "complete": true,
              "e2e_s": 0.359401765,
              "end_ns": 288196339616917,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 85.18140615796754,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050567802,
                "rss_peak_bytes": 1464963072,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.099,
                "predicted_n": 23,
                "predicted_per_second": 78.82507640657975,
                "predicted_per_token_ms": 12.686318181818182
              },
              "ttft_s": 0.080299603,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288196393450069,
              "complete": true,
              "e2e_s": 0.295316597,
              "end_ns": 288196688766666,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 70.77108829450536,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050309665,
                "rss_peak_bytes": 1464967168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.121,
                "predicted_n": 18,
                "predicted_per_second": 78.65963973885,
                "predicted_per_token_ms": 12.713000000000001
              },
              "ttft_s": 0.079157513,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288196745833142,
              "complete": true,
              "e2e_s": 0.470573895,
              "end_ns": 288197216407037,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469778432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 112.4820681862572,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050817575,
                "rss_peak_bytes": 1520668672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 355.321,
                "predicted_n": 29,
                "predicted_per_second": 78.80198468427139,
                "predicted_per_token_ms": 12.690035714285715
              },
              "ttft_s": 0.115261201,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288197267710832,
              "complete": true,
              "e2e_s": 1.074711766,
              "end_ns": 288198342422598,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470249472,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 281.88260002892196,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055462262,
                "rss_peak_bytes": 1521139712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.443,
                "predicted_n": 21,
                "predicted_per_second": 77.99004067180621,
                "predicted_per_token_ms": 12.822149999999999
              },
              "ttft_s": 0.818277656,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288198398015166,
              "complete": true,
              "e2e_s": 0.197751468,
              "end_ns": 288198595766634,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417566720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 48.32147787193244,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051017998,
                "rss_peak_bytes": 1468456960,
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
              "ttft_s": 0.197634809
            },
            {
              "begin_ns": 288198648131957,
              "complete": true,
              "e2e_s": 1.670412934,
              "end_ns": 288200318544891,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417566720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 440.13059800966323,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053094855,
                "rss_peak_bytes": 1468456960,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1607.162,
                "predicted_n": 128,
                "predicted_per_second": 79.0212809909642,
                "predicted_per_token_ms": 12.654818897637796
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063188801
            },
            {
              "begin_ns": 288200394399930,
              "complete": true,
              "e2e_s": 0.618419086,
              "end_ns": 288201012819016,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470282240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 157.13044766772018,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052729798,
                "rss_peak_bytes": 1521172480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.639,
                "predicted_n": 34,
                "predicted_per_second": 79.01560917443055,
                "predicted_per_token_ms": 12.655727272727272
              },
              "tool_call_valid": true,
              "ttft_s": 0.317400303,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288201078140708,
              "complete": true,
              "e2e_s": 0.558757626,
              "end_ns": 288201636898334,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470323200,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 142.6202510887466,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050907468,
                "rss_peak_bytes": 1521213440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.144,
                "predicted_n": 25,
                "predicted_per_second": 78.9099900047346,
                "predicted_per_token_ms": 12.672666666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254568991,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288657897155525,
              "complete": true,
              "e2e_s": 0.184655409,
              "end_ns": 288658081810934,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 37.595420241502865,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053384704,
                "rss_peak_bytes": 1470259200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 118.64,
                "predicted_n": 10,
                "predicted_per_second": 75.85974376264329,
                "predicted_per_token_ms": 13.182222222222222
              },
              "ttft_s": 0.066013285,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288658184403665,
              "complete": true,
              "e2e_s": 0.240481666,
              "end_ns": 288658424885331,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 51.635535403209495,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055946686,
                "rss_peak_bytes": 1470259200,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 170.04,
                "predicted_n": 14,
                "predicted_per_second": 76.45259938837921,
                "predicted_per_token_ms": 13.08
              },
              "ttft_s": 0.070414923,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288658503875442,
              "complete": true,
              "e2e_s": 0.665702296,
              "end_ns": 288659169577738,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 180.91573307201844,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050798778,
                "rss_peak_bytes": 1470304256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.079,
                "predicted_n": 44,
                "predicted_per_second": 79.32423133897458,
                "predicted_per_token_ms": 12.606488372093022
              },
              "ttft_s": 0.123600685,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288659246320179,
              "complete": true,
              "e2e_s": 0.358085853,
              "end_ns": 288659604406032,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 90.3079390819389,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050485963,
                "rss_peak_bytes": 1470308352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.3,
                "predicted_n": 23,
                "predicted_per_second": 79.05138339920948,
                "predicted_per_token_ms": 12.65
              },
              "ttft_s": 0.079737259,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288659685785113,
              "complete": true,
              "e2e_s": 0.295482745,
              "end_ns": 288659981267858,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414081024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 69.80818451100647,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052752522,
                "rss_peak_bytes": 1470312448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.303,
                "predicted_n": 18,
                "predicted_per_second": 78.59345455217913,
                "predicted_per_token_ms": 12.723705882352942
              },
              "ttft_s": 0.079162364,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288660056991684,
              "complete": true,
              "e2e_s": 0.468584601,
              "end_ns": 288660525576285,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469774336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 119.83253205798718,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050446339,
                "rss_peak_bytes": 1526005760,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.896,
                "predicted_n": 29,
                "predicted_per_second": 79.11928928272712,
                "predicted_per_token_ms": 12.639142857142858
              },
              "ttft_s": 0.11464629,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288660608251185,
              "complete": true,
              "e2e_s": 1.080395684,
              "end_ns": 288661688646869,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 286.2199090080113,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.055579787,
                "rss_peak_bytes": 1526472704,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.324,
                "predicted_n": 21,
                "predicted_per_second": 78.02624802983723,
                "predicted_per_token_ms": 12.8162
              },
              "ttft_s": 0.82400396,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288661773104546,
              "complete": true,
              "e2e_s": 0.198355435,
              "end_ns": 288661971459981,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.347018888861605,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056521395,
                "rss_peak_bytes": 1473810432,
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
              "ttft_s": 0.198223901
            },
            {
              "begin_ns": 288662037189186,
              "complete": true,
              "e2e_s": 1.657678203,
              "end_ns": 288663694867389,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 448.9049950741121,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05079675,
                "rss_peak_bytes": 1473810432,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.019,
                "predicted_n": 128,
                "predicted_per_second": 79.67282698637847,
                "predicted_per_token_ms": 12.551330708661418
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063489312
            },
            {
              "begin_ns": 288663769184414,
              "complete": true,
              "e2e_s": 0.619246142,
              "end_ns": 288664388430556,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 162.68305470544172,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051262109,
                "rss_peak_bytes": 1526525952,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.519,
                "predicted_n": 34,
                "predicted_per_second": 78.84946681034792,
                "predicted_per_token_ms": 12.68239393939394
              },
              "tool_call_valid": true,
              "ttft_s": 0.317052195,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288664479876213,
              "complete": true,
              "e2e_s": 0.559813893,
              "end_ns": 288665039690106,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470319104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.49502021961592,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05242836,
                "rss_peak_bytes": 1526550528,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 304.629,
                "predicted_n": 25,
                "predicted_per_second": 78.78435736584501,
                "predicted_per_token_ms": 12.692875
              },
              "tool_facts_valid": true,
              "ttft_s": 0.255196199,
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
          "gpu_j_per_correct_token": 10.014127623037192,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 470327296,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2663.0156186113095,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.074932368,
              "rss_peak_bytes": 7726104576,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 470335488,
              "energy_complete": true,
              "gpu_device_peak_bytes": 7713849344,
              "gpu_energy_j": 2964.9241055355915,
              "gpu_owned_peak_bytes": 7459569664,
              "max_sample_gap_s": 0.111806628,
              "rss_peak_bytes": 7544651776,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 5627.939724146901,
          "raw_requests": [
            {
              "begin_ns": 288224091582008,
              "complete": true,
              "e2e_s": 0.183558479,
              "end_ns": 288224275140487,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 427122688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 36.79794592354611,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050855313,
                "rss_peak_bytes": 1467445248,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.553,
                "predicted_n": 10,
                "predicted_per_second": 77.21808962446269,
                "predicted_per_token_ms": 12.950333333333333
              },
              "ttft_s": 0.067014253,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288224333076140,
              "complete": true,
              "e2e_s": 0.233080646,
              "end_ns": 288224566156786,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 53.577781521553014,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050613805,
                "rss_peak_bytes": 1454391296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 165.873,
                "predicted_n": 14,
                "predicted_per_second": 78.37321324145582,
                "predicted_per_token_ms": 12.759461538461538
              },
              "ttft_s": 0.067136139,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288224629706122,
              "complete": true,
              "e2e_s": 0.666254346,
              "end_ns": 288225295960468,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414068736,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.23654752309662,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05020333,
                "rss_peak_bytes": 1454436352,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.614,
                "predicted_n": 44,
                "predicted_per_second": 79.24602019114877,
                "predicted_per_token_ms": 12.61893023255814
              },
              "ttft_s": 0.123603301,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288225356996224,
              "complete": true,
              "e2e_s": 0.358742753,
              "end_ns": 288225715738977,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414072832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 89.3800098337494,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050739797,
                "rss_peak_bytes": 1454440448,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 279.569,
                "predicted_n": 23,
                "predicted_per_second": 78.6925589031688,
                "predicted_per_token_ms": 12.707681818181818
              },
              "ttft_s": 0.07917529,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288225778083721,
              "complete": true,
              "e2e_s": 0.295705857,
              "end_ns": 288226073789578,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414076928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 68.66752911717177,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05147328,
                "rss_peak_bytes": 1454444544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.227,
                "predicted_n": 18,
                "predicted_per_second": 78.62107877369615,
                "predicted_per_token_ms": 12.719235294117647
              },
              "ttft_s": 0.079441998,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288226130192004,
              "complete": true,
              "e2e_s": 0.472316486,
              "end_ns": 288226602508490,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469770240,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 114.66337990462351,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.053425898,
                "rss_peak_bytes": 1510137856,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 354.631,
                "predicted_n": 29,
                "predicted_per_second": 78.95530847557039,
                "predicted_per_token_ms": 12.665392857142857
              },
              "ttft_s": 0.117667503,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288226664937369,
              "complete": true,
              "e2e_s": 1.07770704,
              "end_ns": 288227742644409,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470241280,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 283.960234387577,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051390049,
                "rss_peak_bytes": 1510608896,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.453,
                "predicted_n": 21,
                "predicted_per_second": 77.98699956717216,
                "predicted_per_token_ms": 12.82265
              },
              "ttft_s": 0.821320573,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288227803036673,
              "complete": true,
              "e2e_s": 0.19792713,
              "end_ns": 288228000963803,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 49.69463967772282,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051709358,
                "rss_peak_bytes": 1457946624,
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
              "ttft_s": 0.197800927
            },
            {
              "begin_ns": 288228052005923,
              "complete": true,
              "e2e_s": 1.6582682,
              "end_ns": 288229710274123,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417579008,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 447.3072815547656,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052157146,
                "rss_peak_bytes": 1457946624,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1594.575,
                "predicted_n": 128,
                "predicted_per_second": 79.6450464857407,
                "predicted_per_token_ms": 12.555708661417324
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.063538257
            },
            {
              "begin_ns": 288229769231396,
              "complete": true,
              "e2e_s": 0.618040886,
              "end_ns": 288230387272282,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470294528,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 162.3884625039269,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052008782,
                "rss_peak_bytes": 1510662144,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 417.587,
                "predicted_n": 34,
                "predicted_per_second": 79.02544858915627,
                "predicted_per_token_ms": 12.654151515151515
              },
              "tool_call_valid": true,
              "ttft_s": 0.316705568,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288230457117183,
              "complete": true,
              "e2e_s": 0.558438321,
              "end_ns": 288231015555504,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470327296,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 139.50552782179122,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.051083367,
                "rss_peak_bytes": 1510694912,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 303.98,
                "predicted_n": 25,
                "predicted_per_second": 78.95256266859661,
                "predicted_per_token_ms": 12.665833333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 0.254430139,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288628153993571,
              "complete": true,
              "e2e_s": 0.182279255,
              "end_ns": 288628336272826,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 40.772041162560434,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050610545,
                "rss_peak_bytes": 1287852032,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 116.414,
                "predicted_n": 10,
                "predicted_per_second": 77.31028914048139,
                "predicted_per_token_ms": 12.934888888888889
              },
              "ttft_s": 0.065864488,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288628422763920,
              "complete": true,
              "e2e_s": 0.233698118,
              "end_ns": 288628656462038,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 57.22460854167768,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050569068,
                "rss_peak_bytes": 1288310784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 166.373,
                "predicted_n": 14,
                "predicted_per_second": 78.137678589675,
                "predicted_per_token_ms": 12.797923076923077
              },
              "ttft_s": 0.067307224,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288628728667854,
              "complete": true,
              "e2e_s": 0.666580799,
              "end_ns": 288629395248653,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414085120,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 177.74324777795613,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052128662,
                "rss_peak_bytes": 1289666560,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 542.796,
                "predicted_n": 44,
                "predicted_per_second": 79.2194489274055,
                "predicted_per_token_ms": 12.623162790697675
              },
              "ttft_s": 0.123727048,
              "usage": {
                "completion_tokens": 44,
                "total_tokens": 119
              }
            },
            {
              "begin_ns": 288629472048625,
              "complete": true,
              "e2e_s": 0.357432761,
              "end_ns": 288629829481386,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414089216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 87.82577652511688,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050943733,
                "rss_peak_bytes": 1289932800,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 278.945,
                "predicted_n": 23,
                "predicted_per_second": 78.86859416730897,
                "predicted_per_token_ms": 12.679318181818182
              },
              "ttft_s": 0.078419748,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288629908176177,
              "complete": true,
              "e2e_s": 0.295374101,
              "end_ns": 288630203550278,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 414093312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 73.7982218070026,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05007133,
                "rss_peak_bytes": 1290919936,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 216.497,
                "predicted_n": 18,
                "predicted_per_second": 78.523028032721,
                "predicted_per_token_ms": 12.735117647058825
              },
              "ttft_s": 0.07887792,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288630276757182,
              "complete": true,
              "e2e_s": 0.468860254,
              "end_ns": 288630745617436,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 469790720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 117.19134152603425,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.050287123,
                "rss_peak_bytes": 1347076096,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 353.957,
                "predicted_n": 29,
                "predicted_per_second": 79.10565407662513,
                "predicted_per_token_ms": 12.641321428571429
              },
              "ttft_s": 0.11484269,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288630822670211,
              "complete": true,
              "e2e_s": 1.079843064,
              "end_ns": 288631902513275,
              "model": "omnicoder2",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470261760,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 283.26829063209783,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052915568,
                "rss_peak_bytes": 1347874816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 256.838,
                "predicted_n": 21,
                "predicted_per_second": 77.87009710401108,
                "predicted_per_token_ms": 12.8419
              },
              "ttft_s": 0.822943955,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288631980253813,
              "complete": true,
              "e2e_s": 0.197464559,
              "end_ns": 288632177718372,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 46.82022092726927,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.056212527,
                "rss_peak_bytes": 1295212544,
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
              "ttft_s": 0.197338405
            },
            {
              "begin_ns": 288632245806341,
              "complete": true,
              "e2e_s": 1.657626119,
              "end_ns": 288633903432460,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 417599488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 445.7454323176683,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.052722566,
                "rss_peak_bytes": 1295212544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1593.805,
                "predicted_n": 128,
                "predicted_per_second": 79.68352464699257,
                "predicted_per_token_ms": 12.549645669291339
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.0637015
            },
            {
              "begin_ns": 288633974715926,
              "complete": true,
              "e2e_s": 0.619465788,
              "end_ns": 288634594181714,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470310912,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 165.0396100859288,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.05358754,
                "rss_peak_bytes": 1347923968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 418.345,
                "predicted_n": 34,
                "predicted_per_second": 78.8822622476664,
                "predicted_per_token_ms": 12.677121212121213
              },
              "tool_call_valid": true,
              "ttft_s": 0.318514371,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288634680578606,
              "complete": true,
              "e2e_s": 0.574443022,
              "end_ns": 288635255021628,
              "model": "omnicoder2",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 470335488,
                "energy_complete": true,
                "gpu_device_peak_bytes": 7713849344,
                "gpu_energy_j": 143.5949301683023,
                "gpu_owned_peak_bytes": 7459569664,
                "max_sample_gap_s": 0.062573225,
                "rss_peak_bytes": 1347948544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 317.386,
                "predicted_n": 25,
                "predicted_per_second": 75.61770210406256,
                "predicted_per_token_ms": 13.224416666666668
              },
              "tool_facts_valid": true,
              "ttft_s": 0.25699112,
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
          "gpu_j_per_correct_token": 8.888899214263331,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476000256,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2243.065897881791,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.081672006,
              "rss_peak_bytes": 5995515904,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476041216,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2574.717476248934,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.070311461,
              "rss_peak_bytes": 5940084736,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4817.783374130725,
          "raw_requests": [
            {
              "begin_ns": 288278706644218,
              "complete": true,
              "e2e_s": 0.157287661,
              "end_ns": 288278863931879,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 33.5694100570083,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050218833,
                "rss_peak_bytes": 1213882368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.897,
                "predicted_n": 10,
                "predicted_per_second": 93.85069397374266,
                "predicted_per_token_ms": 10.655222222222223
              },
              "ttft_s": 0.061365868,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288278924121014,
              "complete": true,
              "e2e_s": 0.148266585,
              "end_ns": 288279072387599,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.13448399562669,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050165667,
                "rss_peak_bytes": 1213882368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.132,
                "predicted_n": 9,
                "predicted_per_second": 93.9717145139313,
                "predicted_per_token_ms": 10.6415
              },
              "ttft_s": 0.063150826,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288279135145152,
              "complete": true,
              "e2e_s": 0.525303695,
              "end_ns": 288279660448847,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 130.4085611737127,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050906457,
                "rss_peak_bytes": 1213947904,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 393.25,
                "predicted_n": 39,
                "predicted_per_second": 96.63064208518755,
                "predicted_per_token_ms": 10.348684210526315
              },
              "ttft_s": 0.132015125,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288279728177041,
              "complete": true,
              "e2e_s": 0.306272712,
              "end_ns": 288280034449753,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 67.98216924482306,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050913816,
                "rss_peak_bytes": 1216978944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.133,
                "predicted_n": 23,
                "predicted_per_second": 96.01410534493066,
                "predicted_per_token_ms": 10.415136363636364
              },
              "ttft_s": 0.077074472,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288280090146873,
              "complete": true,
              "e2e_s": 0.254643754,
              "end_ns": 288280344790627,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.13951377730243,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050000391,
                "rss_peak_bytes": 1216978944,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.22,
                "predicted_n": 18,
                "predicted_per_second": 95.38772303894063,
                "predicted_per_token_ms": 10.483529411764707
              },
              "ttft_s": 0.076412168,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288280406158357,
              "complete": true,
              "e2e_s": 0.398726786,
              "end_ns": 288280804885143,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475492352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 93.48673010535066,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051483245,
                "rss_peak_bytes": 1269694464,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.243,
                "predicted_n": 29,
                "predicted_per_second": 96.13964970831918,
                "predicted_per_token_ms": 10.401535714285714
              },
              "ttft_s": 0.107471104,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288280866990372,
              "complete": true,
              "e2e_s": 1.026239274,
              "end_ns": 288281893229646,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475922432,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 272.79716914075397,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.081672006,
                "rss_peak_bytes": 1270124544,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.459,
                "predicted_n": 16,
                "predicted_per_second": 94.06806765375426,
                "predicted_per_token_ms": 10.6306
              },
              "ttft_s": 0.86674821,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288281957340885,
              "complete": true,
              "e2e_s": 0.204333138,
              "end_ns": 288282161674023,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 49.62947723105224,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052156673,
                "rss_peak_bytes": 1217462272,
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
              "ttft_s": 0.204205802
            },
            {
              "begin_ns": 288282217014880,
              "complete": true,
              "e2e_s": 1.36692784,
              "end_ns": 288283583942720,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423260160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 344.8590576454095,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052824536,
                "rss_peak_bytes": 1217462272,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1308.986,
                "predicted_n": 128,
                "predicted_per_second": 97.0216640972478,
                "predicted_per_token_ms": 10.306976377952756
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057819741
            },
            {
              "begin_ns": 288283647092072,
              "complete": true,
              "e2e_s": 0.549180653,
              "end_ns": 288284196272725,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475975680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.61771031741074,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050588192,
                "rss_peak_bytes": 1270177792,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.887,
                "predicted_n": 34,
                "predicted_per_second": 96.24161895901565,
                "predicted_per_token_ms": 10.390515151515151
              },
              "tool_call_valid": true,
              "ttft_s": 0.30183804,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288284264188831,
              "complete": true,
              "e2e_s": 0.523767136,
              "end_ns": 288284787955967,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476000256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.70515683021594,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052005027,
                "rss_peak_bytes": 1270202368,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 251.343,
                "predicted_n": 25,
                "predicted_per_second": 95.48704360177129,
                "predicted_per_token_ms": 10.472624999999999
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272436206,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288562694207223,
              "complete": true,
              "e2e_s": 0.156512956,
              "end_ns": 288562850720179,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 472506368,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 30.298730265195207,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05050861,
                "rss_peak_bytes": 1210404864,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.617,
                "predicted_n": 10,
                "predicted_per_second": 94.1255216122656,
                "predicted_per_token_ms": 10.624111111111112
              },
              "ttft_s": 0.06090556,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288562923203995,
              "complete": true,
              "e2e_s": 0.148920639,
              "end_ns": 288563072124634,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.952590232301823,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.0502281,
                "rss_peak_bytes": 1157775360,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.433,
                "predicted_n": 9,
                "predicted_per_second": 93.64063066964755,
                "predicted_per_token_ms": 10.679125
              },
              "ttft_s": 0.063480528,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288563138781371,
              "complete": true,
              "e2e_s": 0.525865486,
              "end_ns": 288563664646857,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.04717904612028,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051301101,
                "rss_peak_bytes": 1157828608,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 392.942,
                "predicted_n": 39,
                "predicted_per_second": 96.70638414829669,
                "predicted_per_token_ms": 10.34057894736842
              },
              "ttft_s": 0.132921929,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288563773104435,
              "complete": true,
              "e2e_s": 0.306332241,
              "end_ns": 288564079436676,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 72.23646004078526,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050821836,
                "rss_peak_bytes": 1160896512,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.188,
                "predicted_n": 23,
                "predicted_per_second": 95.9910641045779,
                "predicted_per_token_ms": 10.417636363636364
              },
              "ttft_s": 0.077125243,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288564157211518,
              "complete": true,
              "e2e_s": 0.25407524,
              "end_ns": 288564411286758,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.76577036991073,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051560158,
                "rss_peak_bytes": 1161027584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.898,
                "predicted_n": 18,
                "predicted_per_second": 95.56037729485435,
                "predicted_per_token_ms": 10.464588235294118
              },
              "ttft_s": 0.076104945,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288564480118001,
              "complete": true,
              "e2e_s": 0.397875746,
              "end_ns": 288564877993747,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475488256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 92.80375706216581,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05011661,
                "rss_peak_bytes": 1213870080,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.975,
                "predicted_n": 29,
                "predicted_per_second": 96.22819829882292,
                "predicted_per_token_ms": 10.391964285714286
              },
              "ttft_s": 0.10690793,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288564952752703,
              "complete": true,
              "e2e_s": 1.028109227,
              "end_ns": 288565980861930,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475951104,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 276.2615710195458,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.054200985,
                "rss_peak_bytes": 1214332928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.159,
                "predicted_n": 16,
                "predicted_per_second": 94.24537726424519,
                "predicted_per_token_ms": 10.6106
              },
              "ttft_s": 0.868884461,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288566054723497,
              "complete": true,
              "e2e_s": 0.206331822,
              "end_ns": 288566261055319,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423292928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 51.1748556094427,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050791026,
                "rss_peak_bytes": 1161674752,
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
              "ttft_s": 0.206194068
            },
            {
              "begin_ns": 288566322556498,
              "complete": true,
              "e2e_s": 1.379587318,
              "end_ns": 288567702143816,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423292928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 353.5080732531146,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.055380974,
                "rss_peak_bytes": 1161674752,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1321.163,
                "predicted_n": 128,
                "predicted_per_second": 96.12742712292123,
                "predicted_per_token_ms": 10.402858267716535
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.05830897
            },
            {
              "begin_ns": 288567774102739,
              "complete": true,
              "e2e_s": 0.552203006,
              "end_ns": 288568326305745,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476004352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 137.6458525942229,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052136608,
                "rss_peak_bytes": 1214451712,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 344.411,
                "predicted_n": 34,
                "predicted_per_second": 95.81575501363197,
                "predicted_per_token_ms": 10.43669696969697
              },
              "tool_call_valid": true,
              "ttft_s": 0.305357279,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288568406160482,
              "complete": true,
              "e2e_s": 0.523703234,
              "end_ns": 288568929863716,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476041216,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.2296925003194,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056109577,
                "rss_peak_bytes": 1214488576,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.441,
                "predicted_n": 25,
                "predicted_per_second": 95.83095419679685,
                "predicted_per_token_ms": 10.435041666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273216167,
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
          "gpu_j_per_correct_token": 8.947042936681097,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 476033024,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2504.5391843049806,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.089288974,
              "rss_peak_bytes": 5915451392,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 476000256,
              "energy_complete": true,
              "gpu_device_peak_bytes": 6245842944,
              "gpu_energy_j": 2344.7580873761735,
              "gpu_owned_peak_bytes": 5991563264,
              "max_sample_gap_s": 0.057363056,
              "rss_peak_bytes": 5995921408,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 4849.297271681155,
          "raw_requests": [
            {
              "begin_ns": 288253632123558,
              "complete": true,
              "e2e_s": 0.157792096,
              "end_ns": 288253789915654,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.126933923098136,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050177134,
                "rss_peak_bytes": 1104252928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.688,
                "predicted_n": 10,
                "predicted_per_second": 94.05568096313017,
                "predicted_per_token_ms": 10.632
              },
              "ttft_s": 0.062101473,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288253848084761,
              "complete": true,
              "e2e_s": 0.148300036,
              "end_ns": 288253996384797,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 29.341239216155557,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050759658,
                "rss_peak_bytes": 1104252928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.21,
                "predicted_n": 9,
                "predicted_per_second": 93.88569416735126,
                "predicted_per_token_ms": 10.65125
              },
              "ttft_s": 0.06305074,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288254062329883,
              "complete": true,
              "e2e_s": 0.528507696,
              "end_ns": 288254590837579,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419811328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.0461136302566,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051048175,
                "rss_peak_bytes": 1104502784,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 394.555,
                "predicted_n": 39,
                "predicted_per_second": 96.31103394963947,
                "predicted_per_token_ms": 10.383026315789474
              },
              "ttft_s": 0.133902738,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288254652742645,
              "complete": true,
              "e2e_s": 0.306290465,
              "end_ns": 288254959033110,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 71.73946274507877,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050825002,
                "rss_peak_bytes": 1107767296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 228.816,
                "predicted_n": 23,
                "predicted_per_second": 96.14712257884065,
                "predicted_per_token_ms": 10.400727272727273
              },
              "ttft_s": 0.077463385,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288255016114652,
              "complete": true,
              "e2e_s": 0.254048971,
              "end_ns": 288255270163623,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422776832,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 58.50380636435783,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050732911,
                "rss_peak_bytes": 1107767296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 177.962,
                "predicted_n": 18,
                "predicted_per_second": 95.52601117092414,
                "predicted_per_token_ms": 10.46835294117647
              },
              "ttft_s": 0.076067064,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288255334138298,
              "complete": true,
              "e2e_s": 0.401031751,
              "end_ns": 288255735170049,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475492352,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 89.42760513663478,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051415627,
                "rss_peak_bytes": 1160646656,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 291.271,
                "predicted_n": 29,
                "predicted_per_second": 96.13040776459036,
                "predicted_per_token_ms": 10.402535714285715
              },
              "ttft_s": 0.109699347,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288255793771973,
              "complete": true,
              "e2e_s": 1.026045746,
              "end_ns": 288256819817719,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475963392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 270.78444082031103,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.089288974,
                "rss_peak_bytes": 1161015296,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.262,
                "predicted_n": 16,
                "predicted_per_second": 94.18442566337231,
                "predicted_per_token_ms": 10.617466666666667
              },
              "ttft_s": 0.866801776,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288256884135828,
              "complete": true,
              "e2e_s": 0.204770295,
              "end_ns": 288257088906123,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423297024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 47.96276955615703,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05251456,
                "rss_peak_bytes": 1108320256,
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
              "ttft_s": 0.204614859
            },
            {
              "begin_ns": 288257147579995,
              "complete": true,
              "e2e_s": 1.368563227,
              "end_ns": 288258516143222,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423297024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 343.22331593597846,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05285533,
                "rss_peak_bytes": 1108320256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.028,
                "predicted_n": 128,
                "predicted_per_second": 97.01855116926453,
                "predicted_per_token_ms": 10.307307086614173
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.059407783
            },
            {
              "begin_ns": 288258584233751,
              "complete": true,
              "e2e_s": 0.548051465,
              "end_ns": 288259132285216,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476008448,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 132.10950627633818,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050918405,
                "rss_peak_bytes": 1161031680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 342.209,
                "predicted_n": 34,
                "predicted_per_second": 96.43229722187317,
                "predicted_per_token_ms": 10.369969696969697
              },
              "tool_call_valid": true,
              "ttft_s": 0.301541491,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288259197571978,
              "complete": true,
              "e2e_s": 0.523722902,
              "end_ns": 288259721294880,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476033024,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.896373463327,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.051179556,
                "rss_peak_bytes": 1161056256,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.521,
                "predicted_n": 25,
                "predicted_per_second": 95.80035206629384,
                "predicted_per_token_ms": 10.438374999999999
              },
              "tool_facts_valid": true,
              "ttft_s": 0.273166049,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288588433323655,
              "complete": true,
              "e2e_s": 0.157632691,
              "end_ns": 288588590956346,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419799040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 31.616260973402746,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.05012469,
                "rss_peak_bytes": 1213779968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 95.691,
                "predicted_n": 10,
                "predicted_per_second": 94.05273223187133,
                "predicted_per_token_ms": 10.632333333333333
              },
              "ttft_s": 0.061948903,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288588668106226,
              "complete": true,
              "e2e_s": 0.148468748,
              "end_ns": 288588816574974,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419799040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 32.24017158461504,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050801073,
                "rss_peak_bytes": 1213845504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 85.34,
                "predicted_n": 9,
                "predicted_per_second": 93.74267635340989,
                "predicted_per_token_ms": 10.6675
              },
              "ttft_s": 0.06308506,
              "usage": {
                "completion_tokens": 9,
                "total_tokens": 51
              }
            },
            {
              "begin_ns": 288588897180450,
              "complete": true,
              "e2e_s": 0.538074966,
              "end_ns": 288589435255416,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 419799040,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 133.29912885369788,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.056120762,
                "rss_peak_bytes": 1213898752,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 402.299,
                "predicted_n": 39,
                "predicted_per_second": 94.45710777307426,
                "predicted_per_token_ms": 10.586815789473684
              },
              "ttft_s": 0.135698254,
              "usage": {
                "completion_tokens": 39,
                "total_tokens": 114
              }
            },
            {
              "begin_ns": 288589507927651,
              "complete": true,
              "e2e_s": 0.306616328,
              "end_ns": 288589814543979,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 74.51443439753815,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050914943,
                "rss_peak_bytes": 1216933888,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 229.085,
                "predicted_n": 23,
                "predicted_per_second": 96.03422310496103,
                "predicted_per_token_ms": 10.412954545454546
              },
              "ttft_s": 0.077488214,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 88
              }
            },
            {
              "begin_ns": 288589891138428,
              "complete": true,
              "e2e_s": 0.254424581,
              "end_ns": 288590145563009,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 422768640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 59.211517941324075,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050563637,
                "rss_peak_bytes": 1216933888,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 178.097,
                "predicted_n": 18,
                "predicted_per_second": 95.45360112747547,
                "predicted_per_token_ms": 10.47629411764706
              },
              "ttft_s": 0.076340771,
              "usage": {
                "completion_tokens": 18,
                "total_tokens": 85
              }
            },
            {
              "begin_ns": 288590221878239,
              "complete": true,
              "e2e_s": 0.398618613,
              "end_ns": 288590620496852,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475484160,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 94.51286460909155,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.052260905,
                "rss_peak_bytes": 1269649408,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 290.61,
                "predicted_n": 29,
                "predicted_per_second": 96.34905887615705,
                "predicted_per_token_ms": 10.378928571428572
              },
              "ttft_s": 0.107956366,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288590693816208,
              "complete": true,
              "e2e_s": 1.031102272,
              "end_ns": 288591724918480,
              "model": "qwen35",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475918336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 273.53724228047025,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.057363056,
                "rss_peak_bytes": 1270083584,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 159.465,
                "predicted_n": 16,
                "predicted_per_second": 94.06452826639074,
                "predicted_per_token_ms": 10.631
              },
              "ttft_s": 0.871609944,
              "usage": {
                "completion_tokens": 16,
                "total_tokens": 2218
              }
            },
            {
              "begin_ns": 288591802636117,
              "complete": true,
              "e2e_s": 0.20518628,
              "end_ns": 288592007822397,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 48.91577547549416,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050281151,
                "rss_peak_bytes": 1217409024,
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
              "ttft_s": 0.205061716
            },
            {
              "begin_ns": 288592072154853,
              "complete": true,
              "e2e_s": 1.366904368,
              "end_ns": 288593439059221,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 423243776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 352.4167631642444,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.053437702,
                "rss_peak_bytes": 1217409024,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1309.387,
                "predicted_n": 128,
                "predicted_per_second": 96.99195119548308,
                "predicted_per_token_ms": 10.310133858267717
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.057426042
            },
            {
              "begin_ns": 288593516146429,
              "complete": true,
              "e2e_s": 0.550126865,
              "end_ns": 288594066273294,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 475963392,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 139.12960699644864,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050410336,
                "rss_peak_bytes": 1270128640,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 343.194,
                "predicted_n": 34,
                "predicted_per_second": 96.15552719453136,
                "predicted_per_token_ms": 10.399818181818182
              },
              "tool_call_valid": true,
              "ttft_s": 0.303042238,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288594148550094,
              "complete": true,
              "e2e_s": 0.52291936,
              "end_ns": 288594671469454,
              "model": "qwen35",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 476000256,
                "energy_complete": true,
                "gpu_device_peak_bytes": 6245842944,
                "gpu_energy_j": 131.6376490705029,
                "gpu_owned_peak_bytes": 5991563264,
                "max_sample_gap_s": 0.050577734,
                "rss_peak_bytes": 1270165504,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 250.162,
                "predicted_n": 25,
                "predicted_per_second": 95.93783228467953,
                "predicted_per_token_ms": 10.423416666666666
              },
              "tool_facts_valid": true,
              "ttft_s": 0.272725805,
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
          "gpu_j_per_correct_token": 26.782625925228693,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 667353088,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7762.763993722565,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.084698369,
              "rss_peak_bytes": 11303104512,
              "swap_peak_bytes": 206970880
            },
            {
              "anon_peak_bytes": 772722688,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7128.376020704588,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.095509525,
              "rss_peak_bytes": 12139454464,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14891.140014427154,
          "raw_requests": [
            {
              "begin_ns": 288347440865467,
              "complete": true,
              "e2e_s": 0.525024781,
              "end_ns": 288347965890248,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 605986816,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 109.80538582433,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050553358,
                "rss_peak_bytes": 791339008,
                "swap_peak_bytes": 163233792
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 274.615,
                "predicted_n": 10,
                "predicted_per_second": 32.77315514447499,
                "predicted_per_token_ms": 30.512777777777778
              },
              "ttft_s": 0.24456717,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288348029181300,
              "complete": true,
              "e2e_s": 0.634988288,
              "end_ns": 288348664169588,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 450830336,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 143.1346361105087,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05195765,
                "rss_peak_bytes": 637784064,
                "swap_peak_bytes": 161697792
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 397.705,
                "predicted_n": 14,
                "predicted_per_second": 32.68754478822243,
                "predicted_per_token_ms": 30.592692307692307
              },
              "ttft_s": 0.23290051,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288348726042969,
              "complete": true,
              "e2e_s": 1.862783263,
              "end_ns": 288350588826232,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 451915776,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 483.4204188775134,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.05227183,
                "rss_peak_bytes": 640536576,
                "swap_peak_bytes": 161095680
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1247.245,
                "predicted_n": 45,
                "predicted_per_second": 35.277752165773364,
                "predicted_per_token_ms": 28.34647727272727
              },
              "ttft_s": 0.56684235,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 288350658680574,
              "complete": true,
              "e2e_s": 1.040755127,
              "end_ns": 288351699435701,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 456241152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 269.65278253981353,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050554809,
                "rss_peak_bytes": 646660096,
                "swap_peak_bytes": 159318016
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 766.369,
                "predicted_n": 28,
                "predicted_per_second": 35.23107015028009,
                "predicted_per_token_ms": 28.38403703703704
              },
              "ttft_s": 0.270140734,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 288351772297369,
              "complete": true,
              "e2e_s": 0.925797859,
              "end_ns": 288352698095228,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 457113600,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 235.94501926968493,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050819037,
                "rss_peak_bytes": 648163328,
                "swap_peak_bytes": 158445568
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 628.015,
                "predicted_n": 23,
                "predicted_per_second": 35.03101040580241,
                "predicted_per_token_ms": 28.546136363636364
              },
              "ttft_s": 0.253357614,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 288352759163532,
              "complete": true,
              "e2e_s": 1.186771572,
              "end_ns": 288353945935104,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 614899712,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 292.63085061227156,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05197944,
                "rss_peak_bytes": 806473728,
                "swap_peak_bytes": 157458432
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 796.152,
                "predicted_n": 29,
                "predicted_per_second": 35.169163677287756,
                "predicted_per_token_ms": 28.434
              },
              "ttft_s": 0.385927592,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288354010202643,
              "complete": true,
              "e2e_s": 3.807323523,
              "end_ns": 288357817526166,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615944192,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1004.3605737919864,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.054580328,
                "rss_peak_bytes": 807686144,
                "swap_peak_bytes": 156897280
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 581.916,
                "predicted_n": 21,
                "predicted_per_second": 34.36922167460595,
                "predicted_per_token_ms": 29.095800000000004
              },
              "ttft_s": 3.222428135,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288357879102791,
              "complete": true,
              "e2e_s": 0.718305998,
              "end_ns": 288358597408789,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 459132928,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.04198406369036,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052997473,
                "rss_peak_bytes": 650874880,
                "swap_peak_bytes": 156667904
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
              "ttft_s": 0.718184983
            },
            {
              "begin_ns": 288358652130562,
              "complete": true,
              "e2e_s": 3.778665778,
              "end_ns": 288362430796340,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 459149312,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1031.8236617804919,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053608177,
                "rss_peak_bytes": 650891264,
                "swap_peak_bytes": 156663808
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3583.12,
                "predicted_n": 128,
                "predicted_per_second": 35.44397061778562,
                "predicted_per_token_ms": 28.213543307086614
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.195464731
            },
            {
              "begin_ns": 288362497276265,
              "complete": true,
              "e2e_s": 1.703853049,
              "end_ns": 288364201129314,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 616087552,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 461.77190975342086,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053546171,
                "rss_peak_bytes": 807829504,
                "swap_peak_bytes": 156647424
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 938.413,
                "predicted_n": 34,
                "predicted_per_second": 35.165753245106366,
                "predicted_per_token_ms": 28.436757575757575
              },
              "tool_call_valid": true,
              "ttft_s": 1.028288076,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288364312814882,
              "complete": true,
              "e2e_s": 1.770776758,
              "end_ns": 288366083591640,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 616136704,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 448.676121930868,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055174465,
                "rss_peak_bytes": 807878656,
                "swap_peak_bytes": 156639232
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 681.992,
                "predicted_n": 25,
                "predicted_per_second": 35.19102863376696,
                "predicted_per_token_ms": 28.41633333333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.088721464,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288514056290447,
              "complete": true,
              "e2e_s": 0.466287355,
              "end_ns": 288514522577802,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612278272,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 107.1530316550803,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052301705,
                "rss_peak_bytes": 1257074688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.308,
                "predicted_n": 10,
                "predicted_per_second": 34.31081019259801,
                "predicted_per_token_ms": 29.145333333333333
              },
              "ttft_s": 0.203954049,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288514593658078,
              "complete": true,
              "e2e_s": 0.573047336,
              "end_ns": 288515166705414,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612278272,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 140.7267660336991,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052370019,
                "rss_peak_bytes": 1257074688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 370.794,
                "predicted_n": 14,
                "predicted_per_second": 35.059898488109305,
                "predicted_per_token_ms": 28.522615384615385
              },
              "ttft_s": 0.202189218,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288515241066197,
              "complete": true,
              "e2e_s": 1.759883241,
              "end_ns": 288517000949438,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612278272,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 484.2228660843733,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050780269,
                "rss_peak_bytes": 1257074688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1240.185,
                "predicted_n": 45,
                "predicted_per_second": 35.4785777928293,
                "predicted_per_token_ms": 28.186022727272725
              },
              "ttft_s": 0.51972211,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 288517085340041,
              "complete": true,
              "e2e_s": 0.990594623,
              "end_ns": 288518075934664,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615251968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 264.1394006609953,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051571828,
                "rss_peak_bytes": 1260371968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.773,
                "predicted_n": 28,
                "predicted_per_second": 35.350817585853385,
                "predicted_per_token_ms": 28.28788888888889
              },
              "ttft_s": 0.226778923,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 288518146254873,
              "complete": true,
              "e2e_s": 0.846346719,
              "end_ns": 288518992601592,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615251968,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 228.15578646030409,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05200029,
                "rss_peak_bytes": 1260371968,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.963,
                "predicted_n": 23,
                "predicted_per_second": 35.31509897056487,
                "predicted_per_token_ms": 28.316499999999998
              },
              "ttft_s": 0.22338463,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 288519078109247,
              "complete": true,
              "e2e_s": 1.146953889,
              "end_ns": 288520225063136,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772165632,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 292.7734166990453,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053802989,
                "rss_peak_bytes": 1417285632,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.452,
                "predicted_n": 29,
                "predicted_per_second": 35.3780140804496,
                "predicted_per_token_ms": 28.266142857142857
              },
              "ttft_s": 0.35542054,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288520297123281,
              "complete": true,
              "e2e_s": 3.780590579,
              "end_ns": 288524077713860,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772628480,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1014.3493532006878,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.071780702,
                "rss_peak_bytes": 1417748480,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.741,
                "predicted_n": 21,
                "predicted_per_second": 34.49816383522987,
                "predicted_per_token_ms": 28.98705
              },
              "ttft_s": 3.200808246,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288524158159194,
              "complete": true,
              "e2e_s": 0.719883515,
              "end_ns": 288524878042709,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615759872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 184.16311562621263,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050729727,
                "rss_peak_bytes": 1260879872,
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
              "ttft_s": 0.719752875
            },
            {
              "begin_ns": 288524934699849,
              "complete": true,
              "e2e_s": 3.773973511,
              "end_ns": 288528708673360,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615759872,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1046.0983789108059,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052907872,
                "rss_peak_bytes": 1260879872,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3580.066,
                "predicted_n": 128,
                "predicted_per_second": 35.474206341447335,
                "predicted_per_token_ms": 28.189496062992124
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.193730767
            },
            {
              "begin_ns": 288528781233694,
              "complete": true,
              "e2e_s": 1.697943608,
              "end_ns": 288530479177302,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772681728,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 450.8270963148254,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051486739,
                "rss_peak_bytes": 1417801728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 937.055,
                "predicted_n": 34,
                "predicted_per_second": 35.21671620129021,
                "predicted_per_token_ms": 28.39560606060606
              },
              "tool_call_valid": true,
              "ttft_s": 1.023451811,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288530557620547,
              "complete": true,
              "e2e_s": 1.775590557,
              "end_ns": 288532333211104,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772722688,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 457.23025596007284,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051975528,
                "rss_peak_bytes": 1417842688,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.349,
                "predicted_n": 25,
                "predicted_per_second": 35.17261694528752,
                "predicted_per_token_ms": 28.431208333333334
              },
              "tool_facts_valid": true,
              "ttft_s": 1.093261734,
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
          "gpu_j_per_correct_token": 25.514515676236133,
          "lifecycle_energy_intervals": [
            {
              "anon_peak_bytes": 772751360,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7095.82530156711,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.092258889,
              "rss_peak_bytes": 12139388928,
              "swap_peak_bytes": 0
            },
            {
              "anon_peak_bytes": 772669440,
              "energy_complete": true,
              "gpu_device_peak_bytes": 13057392640,
              "gpu_energy_j": 7090.245414420179,
              "gpu_owned_peak_bytes": 12803112960,
              "max_sample_gap_s": 0.078708091,
              "rss_peak_bytes": 12139470848,
              "swap_peak_bytes": 0
            }
          ],
          "lifecycle_gpu_j": 14186.070715987289,
          "raw_requests": [
            {
              "begin_ns": 288404924812232,
              "complete": true,
              "e2e_s": 0.465574356,
              "end_ns": 288405390386588,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612302848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.0967328840809,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.051937248,
                "rss_peak_bytes": 1257033728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.559,
                "predicted_n": 10,
                "predicted_per_second": 34.27800989491885,
                "predicted_per_token_ms": 29.173222222222225
              },
              "ttft_s": 0.202976919,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288405457105515,
              "complete": true,
              "e2e_s": 0.575615629,
              "end_ns": 288406032721144,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612302848,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 139.04818875208554,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052813629,
                "rss_peak_bytes": 1257033728,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.342,
                "predicted_n": 14,
                "predicted_per_second": 35.008159594120784,
                "predicted_per_token_ms": 28.56476923076923
              },
              "ttft_s": 0.204216508,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288406096312821,
              "complete": true,
              "e2e_s": 1.768853043,
              "end_ns": 288407865165864,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612306944,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 475.6268127573637,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.052562475,
                "rss_peak_bytes": 1257037824,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1248.186,
                "predicted_n": 45,
                "predicted_per_second": 35.25115647828129,
                "predicted_per_token_ms": 28.367863636363634
              },
              "ttft_s": 0.520559224,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 288407932584642,
              "complete": true,
              "e2e_s": 0.989578683,
              "end_ns": 288408922163325,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615280640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 258.33969764722605,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051576789,
                "rss_peak_bytes": 1260335104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 763.114,
                "predicted_n": 28,
                "predicted_per_second": 35.381345382210256,
                "predicted_per_token_ms": 28.26348148148148
              },
              "ttft_s": 0.226460504,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 288408986100493,
              "complete": true,
              "e2e_s": 0.847526881,
              "end_ns": 288409833627374,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615280640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 224.92170090461255,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053655346,
                "rss_peak_bytes": 1260335104,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 624.695,
                "predicted_n": 23,
                "predicted_per_second": 35.217185986761535,
                "predicted_per_token_ms": 28.395227272727276
              },
              "ttft_s": 0.222822413,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 288409897365068,
              "complete": true,
              "e2e_s": 1.146779668,
              "end_ns": 288411044144736,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772194304,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 289.2914335161696,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.050953865,
                "rss_peak_bytes": 1415544832,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.492,
                "predicted_n": 29,
                "predicted_per_second": 35.37622616526762,
                "predicted_per_token_ms": 28.267571428571426
              },
              "ttft_s": 0.355176705,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288411113197940,
              "complete": true,
              "e2e_s": 3.780816511,
              "end_ns": 288414894014451,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772657152,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1010.2841977310879,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.092258889,
                "rss_peak_bytes": 1416007680,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 580.376,
                "predicted_n": 21,
                "predicted_per_second": 34.46041876300881,
                "predicted_per_token_ms": 29.0188
              },
              "ttft_s": 3.20027062,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288414957100051,
              "complete": true,
              "e2e_s": 0.718801994,
              "end_ns": 288415675902045,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615792640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 188.54352310273356,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055955445,
                "rss_peak_bytes": 1259143168,
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
              "ttft_s": 0.718625174
            },
            {
              "begin_ns": 288415731277883,
              "complete": true,
              "e2e_s": 3.773677958,
              "end_ns": 288419504955841,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615792640,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1039.6015251936544,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053173016,
                "rss_peak_bytes": 1259143168,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3578.978,
                "predicted_n": 128,
                "predicted_per_second": 35.48499040787622,
                "predicted_per_token_ms": 28.180929133858267
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.194512539
            },
            {
              "begin_ns": 288419569150542,
              "complete": true,
              "e2e_s": 1.704510841,
              "end_ns": 288421273661383,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772710400,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 446.44030875838445,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051498934,
                "rss_peak_bytes": 1416060928,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 939.074,
                "predicted_n": 34,
                "predicted_per_second": 35.141000602721405,
                "predicted_per_token_ms": 28.45678787878788
              },
              "tool_call_valid": true,
              "ttft_s": 1.028564695,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288421345794844,
              "complete": true,
              "e2e_s": 1.772769127,
              "end_ns": 288423118563971,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772751360,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 455.76813070988163,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.053463554,
                "rss_peak_bytes": 1416101888,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.549,
                "predicted_n": 25,
                "predicted_per_second": 35.16231069124707,
                "predicted_per_token_ms": 28.439541666666667
              },
              "tool_facts_valid": true,
              "ttft_s": 1.090197166,
              "usage": {
                "completion_tokens": 25,
                "total_tokens": 417
              }
            },
            {
              "begin_ns": 288459277178481,
              "complete": true,
              "e2e_s": 0.467537742,
              "end_ns": 288459744716223,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 105.37233580850514,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050575653,
                "rss_peak_bytes": 1257066496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 262.669,
                "predicted_n": 10,
                "predicted_per_second": 34.26365501829299,
                "predicted_per_token_ms": 29.185444444444443
              },
              "ttft_s": 0.204883329,
              "usage": {
                "completion_tokens": 10,
                "total_tokens": 45
              }
            },
            {
              "begin_ns": 288459811841274,
              "complete": true,
              "e2e_s": 0.574042309,
              "end_ns": 288460385883583,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 141.0233780447586,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.053729435,
                "rss_peak_bytes": 1257066496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 371.822,
                "predicted_n": 14,
                "predicted_per_second": 34.96296615046985,
                "predicted_per_token_ms": 28.601692307692307
              },
              "ttft_s": 0.202183459,
              "usage": {
                "completion_tokens": 14,
                "total_tokens": 56
              }
            },
            {
              "begin_ns": 288460455233603,
              "complete": true,
              "e2e_s": 1.761864435,
              "end_ns": 288462217098038,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 612265984,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13055295488,
                "gpu_energy_j": 469.99862574131436,
                "gpu_owned_peak_bytes": 12801015808,
                "max_sample_gap_s": 0.050649928,
                "rss_peak_bytes": 1257066496,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 1241.898,
                "predicted_n": 45,
                "predicted_per_second": 35.429640759547084,
                "predicted_per_token_ms": 28.224954545454544
              },
              "ttft_s": 0.519864124,
              "usage": {
                "completion_tokens": 45,
                "total_tokens": 120
              }
            },
            {
              "begin_ns": 288462289119533,
              "complete": true,
              "e2e_s": 0.987289249,
              "end_ns": 288463276408782,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615239680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 259.945271459437,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052219863,
                "rss_peak_bytes": 1260363776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 764.275,
                "predicted_n": 28,
                "predicted_per_second": 35.32759805043996,
                "predicted_per_token_ms": 28.30648148148148
              },
              "ttft_s": 0.223063424,
              "usage": {
                "completion_tokens": 28,
                "total_tokens": 93
              }
            },
            {
              "begin_ns": 288463358635260,
              "complete": true,
              "e2e_s": 0.843860918,
              "end_ns": 288464202496178,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615239680,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 222.42368055957894,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051032267,
                "rss_peak_bytes": 1260363776,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 622.877,
                "predicted_n": 23,
                "predicted_per_second": 35.319974890708764,
                "predicted_per_token_ms": 28.312590909090908
              },
              "ttft_s": 0.220953063,
              "usage": {
                "completion_tokens": 23,
                "total_tokens": 90
              }
            },
            {
              "begin_ns": 288464290086588,
              "complete": true,
              "e2e_s": 1.143239957,
              "end_ns": 288465433326545,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772153344,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 290.035482891841,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.051518804,
                "rss_peak_bytes": 1417277440,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 791.292,
                "predicted_n": 29,
                "predicted_per_second": 35.38516754876834,
                "predicted_per_token_ms": 28.260428571428573
              },
              "ttft_s": 0.351918363,
              "usage": {
                "completion_tokens": 29,
                "total_tokens": 106
              }
            },
            {
              "begin_ns": 288465526159149,
              "complete": true,
              "e2e_s": 3.770138185,
              "end_ns": 288469296297334,
              "model": "qwen38",
              "profiler": false,
              "quality_pass": true,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772579328,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1009.2875773724629,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.057048549,
                "rss_peak_bytes": 1417703424,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 579.456,
                "predicted_n": 21,
                "predicted_per_second": 34.515131433620496,
                "predicted_per_token_ms": 28.9728
              },
              "ttft_s": 3.190693759,
              "usage": {
                "completion_tokens": 21,
                "total_tokens": 2223
              }
            },
            {
              "begin_ns": 288469403292467,
              "complete": true,
              "e2e_s": 0.723219153,
              "end_ns": 288470126511620,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615710720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 186.4060467443214,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.056749148,
                "rss_peak_bytes": 1260834816,
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
              "ttft_s": 0.723093536
            },
            {
              "begin_ns": 288470220010446,
              "complete": true,
              "e2e_s": 3.778366416,
              "end_ns": 288473998376862,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 615710720,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 1033.5562691043551,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.05229753,
                "rss_peak_bytes": 1260834816,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 3581.072,
                "predicted_n": 128,
                "predicted_per_second": 35.464240875357994,
                "predicted_per_token_ms": 28.197417322834646
              },
              "tokens_evaluated": 31,
              "tokens_predicted": 128,
              "ttft_s": 0.197186679
            },
            {
              "begin_ns": 288474077436703,
              "complete": true,
              "e2e_s": 1.705828107,
              "end_ns": 288475783264810,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772632576,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 444.75680996130455,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.055380971,
                "rss_peak_bytes": 1417756672,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 941.595,
                "predicted_n": 34,
                "predicted_per_second": 35.04691507495261,
                "predicted_per_token_ms": 28.53318181818182
              },
              "tool_call_valid": true,
              "ttft_s": 1.030118635,
              "usage": {
                "completion_tokens": 34,
                "total_tokens": 350
              }
            },
            {
              "begin_ns": 288475876196036,
              "complete": true,
              "e2e_s": 1.775929289,
              "end_ns": 288477652125325,
              "model": "qwen38",
              "profiler": false,
              "rep": 0,
              "telemetry": {
                "anon_peak_bytes": 772669440,
                "energy_complete": true,
                "gpu_device_peak_bytes": 13057392640,
                "gpu_energy_j": 454.26895460207714,
                "gpu_owned_peak_bytes": 12803112960,
                "max_sample_gap_s": 0.052127245,
                "rss_peak_bytes": 1417793536,
                "swap_peak_bytes": 0
              },
              "timings": {
                "cache_n": 0,
                "predicted_ms": 682.901,
                "predicted_n": 25,
                "predicted_per_second": 35.144186346190736,
                "predicted_per_token_ms": 28.45420833333333
              },
              "tool_facts_valid": true,
              "ttft_s": 1.09303572,
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
