# Public audit excerpt

Original SHA256: `75bddb0260502a4b1ebe86e44d2f8dd7ce4e4028953fcd2f5efbfb77a18e9017`

Original file: `RESULTS.json`; 39606 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

```json
{
  "models": {
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5257807695000001,
              "format_passes": 2,
              "gpu_energy_j": 132.07139071693598,
              "semantic_passes": 2,
              "tokens_per_s": 96.57016633453703,
              "ttft_s": 0.13224113599999998
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3662996095,
              "format_passes": 0,
              "gpu_energy_j": 358.1643282646311,
              "semantic_passes": 0,
              "tokens_per_s": 97.08578294002697,
              "ttft_s": 0.0580738455
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.204814773,
              "format_passes": 2,
              "gpu_energy_j": 44.68101861068608,
              "semantic_passes": 2,
              "tokens_per_s": 95.00111700456065,
              "ttft_s": 0.06796701799999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229723837,
              "format_passes": 0,
              "gpu_energy_j": 54.79242107990859,
              "semantic_passes": 0,
              "tokens_per_s": 94.03259367704842,
              "ttft_s": 0.13397871249999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15669408899999998,
              "format_passes": 2,
              "gpu_energy_j": 33.88539581379799,
              "semantic_passes": 2,
              "tokens_per_s": 94.02732240316021,
              "ttft_s": 0.060964252499999996
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3075977175,
              "format_passes": 0,
              "gpu_energy_j": 70.84305457135912,
              "semantic_passes": 0,
              "tokens_per_s": 95.47467494702744,
              "ttft_s": 0.077155036
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.401074043,
              "format_passes": 0,
              "gpu_energy_j": 94.01379957751385,
              "semantic_passes": 2,
              "tokens_per_s": 95.3319602681695,
              "ttft_s": 0.107336194
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0348487155,
              "format_passes": 2,
              "gpu_energy_j": 272.2713542073657,
              "semantic_passes": 2,
              "tokens_per_s": 93.91074121708307,
              "ttft_s": 0.875070676
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.14890119400000001,
              "format_passes": 0,
              "gpu_energy_j": 29.868773963840372,
              "semantic_passes": 0,
              "tokens_per_s": 93.5781593545477,
              "ttft_s": 0.0633473245
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2062275815,
              "format_passes": 0,
              "gpu_energy_j": 50.60431352412051,
              "semantic_passes": 0,
              "tokens_per_s": 2461.297340106679,
              "ttft_s": 0.2060862945
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7569769465,
              "format_passes": 0,
              "gpu_energy_j": 200.99283452195706,
              "semantic_passes": 0,
              "tokens_per_s": 2710.100911873623,
              "ttft_s": 0.7567099205000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4998589075000002,
              "format_passes": 0,
              "gpu_energy_j": 405.5939087462914,
              "semantic_passes": 0,
              "tokens_per_s": 2733.8919276914226,
              "ttft_s": 1.4995434799999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.254807135,
              "format_passes": 2,
              "gpu_energy_j": 60.45155999649549,
              "semantic_passes": 2,
              "tokens_per_s": 95.49709559766214,
              "ttft_s": 0.076748384
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35183988099999997,
              "format_passes": 0,
              "gpu_energy_j": 81.90302516090708,
              "semantic_passes": 2,
              "tokens_per_s": 96.08731330846445,
              "ttft_s": 0.070837439
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314502709,
              "format_passes": 0,
              "gpu_energy_j": 73.69133018353199,
              "semantic_passes": 0,
              "tokens_per_s": 95.99406623050014,
              "ttft_s": 0.0748695445
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5505048269999999,
              "format_passes": 0,
              "gpu_energy_j": 140.55884580100042,
              "semantic_passes": 0,
              "tokens_per_s": 96.20177909462308,
              "ttft_s": 0.30337204799999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5247525075,
              "format_passes": 0,
              "gpu_energy_j": 131.7981419621969,
              "semantic_passes": 0,
              "tokens_per_s": 95.75089801671463,
              "ttft_s": 0.27388640200000003
            }
          }
        },
        "B": {
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 16,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5261542275,
              "format_passes": 2,
              "gpu_energy_j": 131.45298039538574,
              "semantic_passes": 2,
              "tokens_per_s": 96.46839830507918,
              "ttft_s": 0.1322147225
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4123527425,
              "format_passes": 0,
              "gpu_energy_j": 367.41856703469904,
              "semantic_passes": 0,
              "tokens_per_s": 96.99839790249044,
              "ttft_s": 0.1026756295
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25438433650000003,
              "format_passes": 2,
              "gpu_energy_j": 59.56401075679783,
              "semantic_passes": 2,
              "tokens_per_s": 94.9668572898197,
              "ttft_s": 0.11746145999999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.22954426649999998,
              "format_passes": 0,
              "gpu_energy_j": 54.30297955663466,
              "semantic_passes": 0,
              "tokens_per_s": 94.17833135998426,
              "ttft_s": 0.13396200400000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20180764750000002,
              "format_passes": 2,
              "gpu_energy_j": 41.60899637753557,
              "semantic_passes": 2,
              "tokens_per_s": 93.74561870892703,
              "ttft_s": 0.1057883635
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3480427995,
              "format_passes": 0,
              "gpu_energy_j": 86.61312462182407,
              "semantic_passes": 0,
              "tokens_per_s": 95.7685546141472,
              "ttft_s": 0.11826292499999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4924845205,
              "format_passes": 0,
              "gpu_energy_j": 120.42915807037147,
              "semantic_passes": 2,
              "tokens_per_s": 96.29803630064042,
              "ttft_s": 0.2017263535
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0327619525,
              "format_passes": 2,
              "gpu_energy_j": 277.76878356081295,
              "semantic_passes": 2,
              "tokens_per_s": 94.06401298153739,
              "ttft_s": 0.8733128745000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20222410899999999,
              "format_passes": 0,
              "gpu_energy_j": 46.76165083367724,
              "semantic_passes": 0,
              "tokens_per_s": 93.36829697314369,
              "ttft_s": 0.11652758299999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205662395,
              "format_passes": 0,
              "gpu_energy_j": 52.1936373935001,
              "semantic_passes": 0,
              "tokens_per_s": 2468.5094391836765,
              "ttft_s": 0.205502568
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.755052795,
              "format_passes": 0,
              "gpu_energy_j": 199.09196155915004,
              "semantic_passes": 0,
              "tokens_per_s": 2716.951698085931,
              "ttft_s": 0.7547828515
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4990286985,
              "format_passes": 0,
              "gpu_energy_j": 406.97996160270145,
              "semantic_passes": 0,
              "tokens_per_s": 2735.6129125477346,
              "ttft_s": 1.4986564869999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.296270526,
              "format_passes": 2,
              "gpu_energy_j": 69.79750689277483,
              "semantic_passes": 2,
              "tokens_per_s": 95.61779887048792,
              "ttft_s": 0.11844883149999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.349588337,
              "format_passes": 2,
              "gpu_energy_j": 83.68660531365582,
              "semantic_passes": 2,
              "tokens_per_s": 95.5284448507928,
              "ttft_s": 0.119268662
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3572114635,
              "format_passes": 2,
              "gpu_energy_j": 88.14698944333223,
              "semantic_passes": 2,
              "tokens_per_s": 95.93346690088464,
              "ttft_s": 0.117422542
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6047475010000001,
              "format_passes": 0,
              "gpu_energy_j": 151.46866094184128,
              "semantic_passes": 0,
              "tokens_per_s": 95.99574777912098,
              "ttft_s": 0.3574051695
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.525520733,
              "format_passes": 0,
              "gpu_energy_j": 133.29025350250936,
              "semantic_passes": 0,
              "tokens_per_s": 95.72890181206881,
              "ttft_s": 0.274903785
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 4,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 2,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.0710292239016308,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4682394258084699,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10538247299410886,
            "ttft_change_pct": -0.019973739487533226
          },
          "decode": {
            "e2e_change_pct": 3.3706467219772662,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5837968886813334,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.09000806800982808,
            "ttft_change_pct": 76.80184361133793
          },
          "energy": {
            "e2e_change_pct": 24.20214263548266,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 33.30942894518585,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.036062433602024324,
            "ttft_change_pct": 72.82126457276676
          },
          "filtering": {
            "e2e_change_pct": -0.07816798741699937,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8932650056841518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1549863480702962,
            "ttft_change_pct": -0.012471011019721256
          },
          "german": {
            "e2e_change_pct": 28.79084896431545,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 22.793301887866857,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2995976988745097,
            "ttft_change_pct": 73.52523677707687
          },
          "ha_sim": {
            "e2e_change_pct": 13.148693796793221,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 22.260573243041073,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.30780902609286453,
            "ttft_change_pct": 53.27959279288004
          },
          "jarvis_memory": {
            "e2e_change_pct": 22.79142195696768,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 28.09732040569035,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.013381063132801,
            "ttft_change_pct": 87.93879863114955
          },
          "long_context": {
            "e2e_change_pct": -0.20164908829128914,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0190994272795804,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16321004654835658,
            "ttft_change_pct": -0.20087537477943007
          },
          "math": {
            "e2e_change_pct": 35.81093849388473,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 56.556981181375775,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.22426427582197261,
            "ttft_change_pct": 83.95028348829476
          },
          "prefill": {
            "e2e_change_pct": -0.27405960729846024,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.140688527712232,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.293020227969909,
            "ttft_change_pct": -0.2832437263313503
          },
          "prefill2048": {
            "e2e_change_pct": -0.25418891670303534,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9457416565760046,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.252787126202314,
            "ttft_change_pct": -0.25466416493215016
          },
          "prefill4096": {
            "e2e_change_pct": -0.05535247321255543,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3417341401142915,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06294999589706585,
            "ttft_change_pct": -0.05915086903648392
          },
          "pve_sim": {
            "e2e_change_pct": 16.272460737804685,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 15.460224511693577,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1263947055880177,
            "ttft_change_pct": 54.333974641081674
          },
          "sorting": {
            "e2e_change_pct": -0.6399342773765748,
            "format_pass_change": 2,
            "gpu_energy_change_pct": 2.1776731070002775,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5816256469545977,
            "ttft_change_pct": 68.36952843538005
          },
          "time": {
            "e2e_change_pct": 13.579773171365584,
            "format_pass_change": 2,
            "gpu_energy_change_pct": 19.616499286683652,
            "same_token_counts": true,
            "semantic_pass_change": 2,
            "tokens_per_s_change_pct": -0.06312820364332561,
            "ttft_change_pct": 56.83619124996815
          },
          "tool-call": {
            "e2e_change_pct": 9.853260378405393,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.761742122076543,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2141658059145124,
            "ttft_change_pct": 17.810843766331462
          },
          "tool-final": {
            "e2e_change_pct": 0.14639768062469916,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.132118797805548,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.022972322037106974,
            "ttft_change_pct": 0.37146166898784916
          }
        }
      },
      "complete": true
    }
  }
}
```
