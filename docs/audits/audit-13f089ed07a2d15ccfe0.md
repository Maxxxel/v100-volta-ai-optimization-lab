# Public audit excerpt

Original SHA256: `13f089ed07a2d15ccfe07ffbe9e8b218e7a9b230dc88a4ac145790e6ac9a87d1`

Original file: `RESULTS.json`; 38281 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "omnicoder2": {
      "arms": {
        "A": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6672974574999999,
              "format_passes": 2,
              "gpu_energy_j": 178.24621586177244,
              "semantic_passes": 2,
              "tokens_per_s": 79.27247256426944,
              "ttft_s": 0.1248179635
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6588460999999999,
              "format_passes": 0,
              "gpu_energy_j": 454.5539016902633,
              "semantic_passes": 0,
              "tokens_per_s": 79.60431022652095,
              "ttft_s": 0.063170525
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238106971,
              "format_passes": 2,
              "gpu_energy_j": 56.92521829505132,
              "semantic_passes": 2,
              "tokens_per_s": 78.13167120801872,
              "ttft_s": 0.0716716365
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241782937,
              "format_passes": 0,
              "gpu_energy_j": 58.788417357669,
              "semantic_passes": 0,
              "tokens_per_s": 77.56681533679345,
              "ttft_s": 0.12571607099999998
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1830616745,
              "format_passes": 2,
              "gpu_energy_j": 38.99532428775486,
              "semantic_passes": 2,
              "tokens_per_s": 77.5006888950124,
              "ttft_s": 0.0669120445
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357769039,
              "format_passes": 0,
              "gpu_energy_j": 90.70531673711582,
              "semantic_passes": 0,
              "tokens_per_s": 78.86449862554943,
              "ttft_s": 0.0787486495
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46908006550000003,
              "format_passes": 0,
              "gpu_energy_j": 117.39874731340056,
              "semantic_passes": 2,
              "tokens_per_s": 79.05305734185384,
              "ttft_s": 0.114865822
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0776259375000001,
              "format_passes": 2,
              "gpu_energy_j": 289.5274991404934,
              "semantic_passes": 2,
              "tokens_per_s": 78.04756539823879,
              "ttft_s": 0.821257539
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.234019526,
              "format_passes": 0,
              "gpu_energy_j": 52.84123267299613,
              "semantic_passes": 0,
              "tokens_per_s": 78.20793846666993,
              "ttft_s": 0.06774290699999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.197721793,
              "format_passes": 0,
              "gpu_energy_j": 48.74988643822746,
              "semantic_passes": 0,
              "tokens_per_s": 2566.8688074158913,
              "ttft_s": 0.197586576
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.715713649,
              "format_passes": 0,
              "gpu_energy_j": 188.76009593566835,
              "semantic_passes": 0,
              "tokens_per_s": 2866.635303043766,
              "ttft_s": 0.715439239
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954302765,
              "format_passes": 2,
              "gpu_energy_j": 74.0018125472804,
              "semantic_passes": 2,
              "tokens_per_s": 78.60037209683897,
              "ttft_s": 0.0790993925
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35382859850000004,
              "format_passes": 2,
              "gpu_energy_j": 85.18128339469759,
              "semantic_passes": 2,
              "tokens_per_s": 78.75133476195295,
              "ttft_s": 0.0744478375
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36860501,
              "format_passes": 2,
              "gpu_energy_j": 94.30727551699482,
              "semantic_passes": 2,
              "tokens_per_s": 78.94787941985311,
              "ttft_s": 0.0772420785
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6195459235,
              "format_passes": 0,
              "gpu_energy_j": 162.9312275395646,
              "semantic_passes": 0,
              "tokens_per_s": 78.9850661810334,
              "ttft_s": 0.317966488
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559584053,
              "format_passes": 0,
              "gpu_energy_j": 147.94951168449887,
              "semantic_passes": 0,
              "tokens_per_s": 78.83458903464603,
              "ttft_s": 0.25507305
            }
          }
        },
        "B": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6658820635,
              "format_passes": 2,
              "gpu_energy_j": 180.285411294395,
              "semantic_passes": 2,
              "tokens_per_s": 79.30075320722554,
              "ttft_s": 0.1236269555
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657959955,
              "format_passes": 0,
              "gpu_energy_j": 451.7730997971031,
              "semantic_passes": 0,
              "tokens_per_s": 79.65955981306486,
              "ttft_s": 0.06317280049999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2373775545,
              "format_passes": 2,
              "gpu_energy_j": 57.75055472802384,
              "semantic_passes": 2,
              "tokens_per_s": 78.43305758823763,
              "ttft_s": 0.071596571
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2415793205,
              "format_passes": 0,
              "gpu_energy_j": 61.61180775680469,
              "semantic_passes": 0,
              "tokens_per_s": 77.64346583744594,
              "ttft_s": 0.125632758
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182417944,
              "format_passes": 2,
              "gpu_energy_j": 42.91540936944532,
              "semantic_passes": 2,
              "tokens_per_s": 77.60094889569874,
              "ttft_s": 0.0663459275
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357913725,
              "format_passes": 0,
              "gpu_energy_j": 90.97653111616964,
              "semantic_passes": 0,
              "tokens_per_s": 78.80392827547053,
              "ttft_s": 0.078751562
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4689043995,
              "format_passes": 0,
              "gpu_energy_j": 116.40175309665568,
              "semantic_passes": 2,
              "tokens_per_s": 79.0841479401963,
              "ttft_s": 0.11485679900000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0791778220000001,
              "format_passes": 2,
              "gpu_energy_j": 286.9072236377659,
              "semantic_passes": 2,
              "tokens_per_s": 77.94880994864823,
              "ttft_s": 0.822562903
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233594045,
              "format_passes": 0,
              "gpu_energy_j": 57.68101046767798,
              "semantic_passes": 0,
              "tokens_per_s": 78.13137695781923,
              "ttft_s": 0.067145344
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1980565815,
              "format_passes": 0,
              "gpu_energy_j": 47.12490367735742,
              "semantic_passes": 0,
              "tokens_per_s": 2563.122012785012,
              "ttft_s": 0.19791166599999999
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7179963935,
              "format_passes": 0,
              "gpu_energy_j": 191.42980144564453,
              "semantic_passes": 0,
              "tokens_per_s": 2857.4942321717776,
              "ttft_s": 0.717757064
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.294712325,
              "format_passes": 2,
              "gpu_energy_j": 71.79719113736499,
              "semantic_passes": 2,
              "tokens_per_s": 78.75368519815268,
              "ttft_s": 0.0787896795
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35269591499999997,
              "format_passes": 2,
              "gpu_energy_j": 89.81715927341367,
              "semantic_passes": 2,
              "tokens_per_s": 78.89108280176302,
              "ttft_s": 0.07379713700000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36925567000000004,
              "format_passes": 2,
              "gpu_energy_j": 93.55002734407955,
              "semantic_passes": 2,
              "tokens_per_s": 78.93594575999786,
              "ttft_s": 0.07787585350000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196075325,
              "format_passes": 0,
              "gpu_energy_j": 162.87974274147388,
              "semantic_passes": 0,
              "tokens_per_s": 79.00738009007746,
              "ttft_s": 0.31885386250000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5606281295,
              "format_passes": 0,
              "gpu_energy_j": 145.87851412154913,
              "semantic_passes": 0,
              "tokens_per_s": 78.80272452180313,
              "ttft_s": 0.255631422
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.21210840594276803,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1440329449708742,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03567523762195712,
            "ttft_change_pct": -0.9541959879837414
          },
          "decode": {
            "e2e_change_pct": -0.05341936180818241,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6117650476257563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06940527012506692,
            "ttft_change_pct": 0.0036021546440778707
          },
          "energy": {
            "e2e_change_pct": -0.3063398341243806,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.449860813347592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3857416276384251,
            "ttft_change_pct": -0.10473529511216828
          },
          "filtering": {
            "e2e_change_pct": -0.0842145862427035,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.80263039223896,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09881867692991264,
            "ttft_change_pct": -0.06627076342528015
          },
          "german": {
            "e2e_change_pct": -0.3516467888531216,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.052705428895292,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1293665928855825,
            "ttft_change_pct": -0.8460614291945667
          },
          "ha_sim": {
            "e2e_change_pct": 0.04044117411736714,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.29900604375801,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0768030623848781,
            "ttft_change_pct": 0.0036984761243363806
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.03744904397350313,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8492375255788387,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03932877410168789,
            "ttft_change_pct": -0.00785525219154648
          },
          "long_context": {
            "e2e_change_pct": 0.1440095719670742,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.90501783440472,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.12653238968654001,
            "ttft_change_pct": 0.1589469731491988
          },
          "math": {
            "e2e_change_pct": -0.1818143157849117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.159093287305463,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09789480499262648,
            "ttft_change_pct": -0.882104158890018
          },
          "prefill": {
            "e2e_change_pct": 0.16932301438312702,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.333305735858705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1459675157551743,
            "ttft_change_pct": 0.1645304081791421
          },
          "prefill2048": {
            "e2e_change_pct": 0.31894662106688454,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.414337864548476,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.31887805408250536,
            "ttft_change_pct": 0.3239723059137445
          },
          "pve_sim": {
            "e2e_change_pct": -0.24301893106747352,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.9791451506770206,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19505391288074936,
            "ttft_change_pct": -0.39154915127824763
          },
          "sorting": {
            "e2e_change_pct": -0.3201220887180667,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.442364442004477,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17745482058495465,
            "ttft_change_pct": -0.8740354614060974
          },
          "time": {
            "e2e_change_pct": 0.17651957579198907,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8029583812744212,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.015115871310211748,
            "ttft_change_pct": 0.8205048495685041
          },
          "tool-call": {
            "e2e_change_pct": 0.009944218445001596,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.03159909789436366,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.028250794894457698,
            "ttft_change_pct": 0.27907799516282417
          },
          "tool-final": {
            "e2e_change_pct": 0.18658081737721322,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.399800201683754,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.04041945703414651,
            "ttft_change_pct": 0.2189067014331636
          }
        }
      },
      "complete": true
    }
  }
}
```
