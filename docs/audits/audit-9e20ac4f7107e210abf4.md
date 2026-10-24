# Public audit excerpt

Original SHA256: `9e20ac4f7107e210abf4f5210dc2698f098bbb98bbb57a6c70ed701e56dabd98`

Original file: `RESULTS.json`; 39857 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
    "qwen38": {
      "arms": {
        "A": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.7655735965,
              "format_passes": 2,
              "gpu_energy_j": 476.49261972713106,
              "semantic_passes": 2,
              "tokens_per_s": 35.355704867057085,
              "ttft_s": 0.5210627274999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7838731780000003,
              "format_passes": 0,
              "gpu_energy_j": 1068.5681314664644,
              "semantic_passes": 0,
              "tokens_per_s": 35.388362105839015,
              "ttft_s": 0.1948023115
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5819342974999999,
              "format_passes": 2,
              "gpu_energy_j": 146.34079076575523,
              "semantic_passes": 2,
              "tokens_per_s": 34.90127593244653,
              "ttft_s": 0.209420999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9260951055,
              "format_passes": 0,
              "gpu_energy_j": 244.82418671743824,
              "semantic_passes": 0,
              "tokens_per_s": 34.8018447975565,
              "ttft_s": 0.523785233
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46763593849999996,
              "format_passes": 2,
              "gpu_energy_j": 110.03980544460302,
              "semantic_passes": 2,
              "tokens_per_s": 33.84635702477837,
              "ttft_s": 0.2016379735
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9909915954999999,
              "format_passes": 0,
              "gpu_energy_j": 263.5018330650801,
              "semantic_passes": 0,
              "tokens_per_s": 35.219797942508094,
              "ttft_s": 0.2243256555
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.14608985,
              "format_passes": 0,
              "gpu_energy_j": 296.9409924213718,
              "semantic_passes": 2,
              "tokens_per_s": 35.28906159786404,
              "ttft_s": 0.3525642375
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7961230305,
              "format_passes": 2,
              "gpu_energy_j": 1019.7504735319449,
              "semantic_passes": 2,
              "tokens_per_s": 34.35588224501171,
              "ttft_s": 3.2138956690000002
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574639913,
              "format_passes": 2,
              "gpu_energy_j": 143.42435901276426,
              "semantic_passes": 2,
              "tokens_per_s": 34.98524333083148,
              "ttft_s": 0.2030285565
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7250325885,
              "format_passes": 0,
              "gpu_energy_j": 187.322342870601,
              "semantic_passes": 0,
              "tokens_per_s": 697.4862028367457,
              "ttft_s": 0.724899306
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7515325595,
              "format_passes": 0,
              "gpu_energy_j": 740.024867591035,
              "semantic_passes": 0,
              "tokens_per_s": 744.636993688006,
              "ttft_s": 2.7512966445
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.469019703,
              "format_passes": 0,
              "gpu_energy_j": 1481.1079154228123,
              "semantic_passes": 0,
              "tokens_per_s": 749.1830692268043,
              "ttft_s": 5.468677415
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8464685255,
              "format_passes": 0,
              "gpu_energy_j": 222.09513795151491,
              "semantic_passes": 2,
              "tokens_per_s": 35.18931275226826,
              "ttft_s": 0.2212408225
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9849829969999999,
              "format_passes": 0,
              "gpu_energy_j": 261.3405837531127,
              "semantic_passes": 2,
              "tokens_per_s": 35.068349939914114,
              "ttft_s": 0.215033149
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0146039500000001,
              "format_passes": 0,
              "gpu_energy_j": 276.8642197886421,
              "semantic_passes": 2,
              "tokens_per_s": 35.25756388973268,
              "ttft_s": 0.2203598645
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7073090739999999,
              "format_passes": 0,
              "gpu_energy_j": 460.76736011759033,
              "semantic_passes": 0,
              "tokens_per_s": 35.0177991232776,
              "ttft_s": 1.0281506215
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7773535215,
              "format_passes": 0,
              "gpu_energy_j": 467.18942550241434,
              "semantic_passes": 0,
              "tokens_per_s": 35.089655959886116,
              "ttft_s": 1.0940072065000002
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 20,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.877629687,
              "format_passes": 2,
              "gpu_energy_j": 491.51452719349027,
              "semantic_passes": 2,
              "tokens_per_s": 32.47973179937635,
              "ttft_s": 0.5228929805
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 4.059117382,
              "format_passes": 0,
              "gpu_energy_j": 1100.3543059625651,
              "semantic_passes": 0,
              "tokens_per_s": 32.88813302307314,
              "ttft_s": 0.19759694249999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6192120720000001,
              "format_passes": 2,
              "gpu_energy_j": 151.89299099106998,
              "semantic_passes": 2,
              "tokens_per_s": 31.994889944941036,
              "ttft_s": 0.2128197135
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9650924705,
              "format_passes": 0,
              "gpu_energy_j": 249.06504257560178,
              "semantic_passes": 0,
              "tokens_per_s": 31.948680322243632,
              "ttft_s": 0.5268458469999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.48663604149999995,
              "format_passes": 2,
              "gpu_energy_j": 109.48340363587545,
              "semantic_passes": 2,
              "tokens_per_s": 31.757999001257897,
              "ttft_s": 0.203231112
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0605301195,
              "format_passes": 0,
              "gpu_energy_j": 276.6429607094959,
              "semantic_passes": 0,
              "tokens_per_s": 32.31286062042116,
              "ttft_s": 0.2248860465
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.220015745,
              "format_passes": 0,
              "gpu_energy_j": 302.70491324097475,
              "semantic_passes": 2,
              "tokens_per_s": 32.37931391850847,
              "ttft_s": 0.35521697799999996
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.85038578,
              "format_passes": 2,
              "gpu_energy_j": 1028.0600825341894,
              "semantic_passes": 2,
              "tokens_per_s": 31.7690830841276,
              "ttft_s": 3.220767077
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.609032502,
              "format_passes": 2,
              "gpu_energy_j": 148.2860928397483,
              "semantic_passes": 2,
              "tokens_per_s": 32.079813356139,
              "ttft_s": 0.20367099900000002
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7291295605,
              "format_passes": 0,
              "gpu_energy_j": 187.3031647190125,
              "semantic_passes": 0,
              "tokens_per_s": 693.6268416513176,
              "ttft_s": 0.7289623715
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.751362714,
              "format_passes": 0,
              "gpu_energy_j": 741.357758671802,
              "semantic_passes": 0,
              "tokens_per_s": 744.6927614935319,
              "ttft_s": 2.7511366705
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.468044781,
              "format_passes": 0,
              "gpu_energy_j": 1481.549449939415,
              "semantic_passes": 0,
              "tokens_per_s": 749.3108000413192,
              "ttft_s": 5.467737941499999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.905861973,
              "format_passes": 0,
              "gpu_energy_j": 230.94731599114124,
              "semantic_passes": 2,
              "tokens_per_s": 32.24269254345048,
              "ttft_s": 0.2234762
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0521547985000002,
              "format_passes": 0,
              "gpu_energy_j": 266.8788447990988,
              "semantic_passes": 2,
              "tokens_per_s": 32.35832907208599,
              "ttft_s": 0.2177237135
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0873194695000001,
              "format_passes": 0,
              "gpu_energy_j": 282.36158800259057,
              "semantic_passes": 2,
              "tokens_per_s": 32.38578658114734,
              "ttft_s": 0.222727944
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7931246220000001,
              "format_passes": 0,
              "gpu_energy_j": 473.1067391316732,
              "semantic_passes": 0,
              "tokens_per_s": 32.153419911183335,
              "ttft_s": 1.0550096125000001
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.836441427,
              "format_passes": 0,
              "gpu_energy_j": 475.51505898208325,
              "semantic_passes": 0,
              "tokens_per_s": 32.455283144762646,
              "ttft_s": 1.0966529905
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
            "e2e_change_pct": 6.346724414215044,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.152600238585368,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.134396071284211,
            "ttft_change_pct": 0.3512538708691393
          },
          "decode": {
            "e2e_change_pct": 7.274139249706102,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9746511766618466,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -7.065116705001007,
            "ttft_change_pct": 1.434598480110938
          },
          "energy": {
            "e2e_change_pct": 6.405839054365092,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.794020926265218,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.327449097078787,
            "ttft_change_pct": 1.6229100788503148
          },
          "filtering": {
            "e2e_change_pct": 4.210946021461304,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7322046138595226,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.198313887984444,
            "ttft_change_pct": 0.5843261335318983
          },
          "german": {
            "e2e_change_pct": 4.0630117225261,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5056368524821497,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -6.170111666645894,
            "ttft_change_pct": 0.7900984483956819
          },
          "ha_sim": {
            "e2e_change_pct": 7.017064959558494,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.987110522745475,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.253702439838362,
            "ttft_change_pct": 0.2498113730018625
          },
          "jarvis_memory": {
            "e2e_change_pct": 6.450270456544049,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.941099735877394,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.245466293531845,
            "ttft_change_pct": 0.7524133811217748
          },
          "long_context": {
            "e2e_change_pct": 1.4294254707770238,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8148668932179026,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -7.52942143192874,
            "ttft_change_pct": 0.21380308223066802
          },
          "math": {
            "e2e_change_pct": 5.985067904602737,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.389754613824958,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.30472993203969,
            "ttft_change_pct": 0.31642962501188254
          },
          "prefill": {
            "e2e_change_pct": 0.5650741863170827,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.010238048112476417,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5533243768452656,
            "ttft_change_pct": 0.5605006745585284
          },
          "prefill2048": {
            "e2e_change_pct": -0.006172759955680451,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1801143636031899,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.007489260673132492,
            "ttft_change_pct": -0.005814494788103364
          },
          "prefill4096": {
            "e2e_change_pct": -0.017826266002762825,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.029811096950127514,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.017049346115993735,
            "ttft_change_pct": -0.017179172013770394
          },
          "pve_sim": {
            "e2e_change_pct": 7.016616177774249,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.9857594908533356,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.373622496017175,
            "ttft_change_pct": 1.0103820238690497
          },
          "sorting": {
            "e2e_change_pct": 6.819589952779692,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1191737488495344,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -7.727825439381819,
            "ttft_change_pct": 1.2512324320749224
          },
          "time": {
            "e2e_change_pct": 7.1668870892923175,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9855827589946973,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.145138210815595,
            "ttft_change_pct": 1.0746419296332466
          },
          "tool-call": {
            "e2e_change_pct": 5.026362789658556,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.678006317750836,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -8.179780808069703,
            "ttft_change_pct": 2.612359554946786
          },
          "tool-final": {
            "e2e_change_pct": 3.3244880540216126,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7820680488894958,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -7.507548145057452,
            "ttft_change_pct": 0.24184337948416346
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
