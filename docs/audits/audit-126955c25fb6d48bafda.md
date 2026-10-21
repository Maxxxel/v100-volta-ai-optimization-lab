# Public audit excerpt

Original SHA256: `126955c25fb6d48bafdaa171135a68581850b376bf18d59ff4330c47e0467df2`

Original file: `RESULTS.json`; 48146 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.667367244,
              "format_passes": 2,
              "gpu_energy_j": 176.11984603669276,
              "semantic_passes": 2,
              "tokens_per_s": 79.17375257801012,
              "ttft_s": 0.124200816
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6616319315,
              "format_passes": 0,
              "gpu_energy_j": 464.57388834916514,
              "semantic_passes": 0,
              "tokens_per_s": 79.47909666173507,
              "ttft_s": 0.063321366
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2386106155,
              "format_passes": 2,
              "gpu_energy_j": 55.73236003116297,
              "semantic_passes": 2,
              "tokens_per_s": 78.09907040598779,
              "ttft_s": 0.0721186685
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24235601150000002,
              "format_passes": 0,
              "gpu_energy_j": 60.50654829615725,
              "semantic_passes": 0,
              "tokens_per_s": 77.30962551038098,
              "ttft_s": 0.1259127665
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182384172,
              "format_passes": 2,
              "gpu_energy_j": 43.380677154692385,
              "semantic_passes": 2,
              "tokens_per_s": 77.35761700429353,
              "ttft_s": 0.06603503250000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358767405,
              "format_passes": 0,
              "gpu_energy_j": 89.7641106573052,
              "semantic_passes": 0,
              "tokens_per_s": 78.5974154376335,
              "ttft_s": 0.07890334199999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4758328075,
              "format_passes": 0,
              "gpu_energy_j": 121.12805749687195,
              "semantic_passes": 2,
              "tokens_per_s": 77.61019892229635,
              "ttft_s": 0.114936704
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0877730374999999,
              "format_passes": 2,
              "gpu_energy_j": 288.1998770037296,
              "semantic_passes": 2,
              "tokens_per_s": 77.49575471034296,
              "ttft_s": 0.8296391830000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2340107665,
              "format_passes": 0,
              "gpu_energy_j": 55.428244126939845,
              "semantic_passes": 0,
              "tokens_per_s": 78.00833988819286,
              "ttft_s": 0.067362203
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1996219135,
              "format_passes": 0,
              "gpu_energy_j": 48.62327874043037,
              "semantic_passes": 0,
              "tokens_per_s": 2545.8250724704644,
              "ttft_s": 0.1994744425
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7214277469999999,
              "format_passes": 0,
              "gpu_energy_j": 192.07369212441841,
              "semantic_passes": 0,
              "tokens_per_s": 2844.5593517553557,
              "ttft_s": 0.7210942364999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4245458405,
              "format_passes": 0,
              "gpu_energy_j": 386.0582566278878,
              "semantic_passes": 0,
              "tokens_per_s": 2879.2227296002366,
              "ttft_s": 1.42414778
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2959113245,
              "format_passes": 2,
              "gpu_energy_j": 75.52363525239261,
              "semantic_passes": 2,
              "tokens_per_s": 78.41997627523395,
              "ttft_s": 0.0791257225
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.354395047,
              "format_passes": 2,
              "gpu_energy_j": 91.529749792812,
              "semantic_passes": 2,
              "tokens_per_s": 78.49468754514913,
              "ttft_s": 0.07414356650000001
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.531129825,
              "format_passes": 0,
              "gpu_energy_j": 1001.7546175384625,
              "semantic_passes": 0,
              "tokens_per_s": 79.34014001702178
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.592582525,
              "format_passes": 0,
              "gpu_energy_j": 1019.87006157617,
              "semantic_passes": 0,
              "tokens_per_s": 79.30249153154318
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.416105182,
              "format_passes": 0,
              "gpu_energy_j": 970.3451159960957,
              "semantic_passes": 0,
              "tokens_per_s": 79.34350252442432
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3703755715,
              "format_passes": 2,
              "gpu_energy_j": 96.21556637519626,
              "semantic_passes": 2,
              "tokens_per_s": 78.62845735658289,
              "ttft_s": 0.077856092
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6236757184999999,
              "format_passes": 0,
              "gpu_energy_j": 164.77030562366684,
              "semantic_passes": 0,
              "tokens_per_s": 78.634844386123,
              "ttft_s": 0.32090498999999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56232081,
              "format_passes": 0,
              "gpu_energy_j": 149.60917846601342,
              "semantic_passes": 0,
              "tokens_per_s": 78.62536651224532,
              "ttft_s": 0.2572192335
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
              "e2e_s": 0.7022975165,
              "format_passes": 2,
              "gpu_energy_j": 185.59769761781808,
              "semantic_passes": 2,
              "tokens_per_s": 74.38792742436785,
              "ttft_s": 0.124244906
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.4771059214999998,
              "format_passes": 0,
              "gpu_energy_j": 576.663910378496,
              "semantic_passes": 0,
              "tokens_per_s": 52.62195700832319,
              "ttft_s": 0.063073236
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.28462169550000005,
              "format_passes": 2,
              "gpu_energy_j": 65.3416865901836,
              "semantic_passes": 2,
              "tokens_per_s": 61.46855053476472,
              "ttft_s": 0.0730320215
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.243536031,
              "format_passes": 0,
              "gpu_energy_j": 64.5208620176139,
              "semantic_passes": 0,
              "tokens_per_s": 76.54606888263442,
              "ttft_s": 0.1259454215
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1845791925,
              "format_passes": 2,
              "gpu_energy_j": 43.91709431703509,
              "semantic_passes": 2,
              "tokens_per_s": 76.16059203184403,
              "ttft_s": 0.06644348650000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.439457891,
              "format_passes": 0,
              "gpu_energy_j": 101.44098025701459,
              "semantic_passes": 0,
              "tokens_per_s": 61.06057887536025,
              "ttft_s": 0.0791239815
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.605504145,
              "format_passes": 0,
              "gpu_energy_j": 136.0486220606134,
              "semantic_passes": 2,
              "tokens_per_s": 57.13358144116782,
              "ttft_s": 0.11537802250000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.175345918,
              "format_passes": 2,
              "gpu_energy_j": 302.5474663882109,
              "semantic_passes": 2,
              "tokens_per_s": 57.66346223351698,
              "ttft_s": 0.8284769329999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.31267553950000004,
              "format_passes": 0,
              "gpu_energy_j": 70.47474695000429,
              "semantic_passes": 0,
              "tokens_per_s": 53.1204888702499,
              "ttft_s": 0.067898669
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.20011339449999999,
              "format_passes": 0,
              "gpu_energy_j": 48.85810880418428,
              "semantic_passes": 0,
              "tokens_per_s": 2541.892244280649,
              "ttft_s": 0.199876067
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7217531355,
              "format_passes": 0,
              "gpu_energy_j": 192.43688470391015,
              "semantic_passes": 0,
              "tokens_per_s": 2843.1809613517603,
              "ttft_s": 0.7215183185
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.423848752,
              "format_passes": 0,
              "gpu_energy_j": 385.54679594210006,
              "semantic_passes": 0,
              "tokens_per_s": 2880.5758091126204,
              "ttft_s": 1.423481314
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.379270142,
              "format_passes": 2,
              "gpu_energy_j": 84.03179010733663,
              "semantic_passes": 2,
              "tokens_per_s": 56.72411794269482,
              "ttft_s": 0.079472608
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4546880585,
              "format_passes": 2,
              "gpu_energy_j": 104.0310429178838,
              "semantic_passes": 2,
              "tokens_per_s": 57.92024679229206,
              "ttft_s": 0.0747733115
            },
            "spec-branch": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.5539001025,
              "format_passes": 0,
              "gpu_energy_j": 1005.8856853812495,
              "semantic_passes": 0,
              "tokens_per_s": 78.75415374319692
            },
            "spec-code": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.9992485705,
              "format_passes": 0,
              "gpu_energy_j": 1075.9755494170545,
              "semantic_passes": 0,
              "tokens_per_s": 70.4154131623113
            },
            "spec-repeat": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 4.407696376500001,
              "format_passes": 0,
              "gpu_energy_j": 1108.3444385676426,
              "semantic_passes": 0,
              "tokens_per_s": 60.65112415068186
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4704153415,
              "format_passes": 2,
              "gpu_energy_j": 107.95877032671453,
              "semantic_passes": 2,
              "tokens_per_s": 58.62472130354282,
              "ttft_s": 0.078018229
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6828946395,
              "format_passes": 0,
              "gpu_energy_j": 156.60764207608787,
              "semantic_passes": 0,
              "tokens_per_s": 68.91406541547704,
              "ttft_s": 0.397550792
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5712810005,
              "format_passes": 0,
              "gpu_energy_j": 141.0526023214894,
              "semantic_passes": 0,
              "tokens_per_s": 76.51675123820888,
              "ttft_s": 0.257093561
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 5.23404059969117,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.381478461632705,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -6.044711786177858,
            "ttft_change_pct": 0.03549896161711974
          },
          "decode": {
            "e2e_change_pct": 49.076692289118995,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 24.127490769581538,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -33.791450559279134,
            "ttft_change_pct": -0.39185825523725404
          },
          "energy": {
            "e2e_change_pct": 19.282914091473025,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 17.241915744546855,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -21.29413293240431,
            "ttft_change_pct": 1.2664584898707698
          },
          "filtering": {
            "e2e_change_pct": 0.4868950816183659,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.634511196718851,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9876604920871612,
            "ttft_change_pct": 0.02593462196702756
          },
          "german": {
            "e2e_change_pct": 1.2035147984222894,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.236534783516352,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.54739121860884,
            "ttft_change_pct": 0.6185413780178006
          },
          "ha_sim": {
            "e2e_change_pct": 22.4910303654815,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 13.00839446211246,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -22.312230579882886,
            "ttft_change_pct": 0.27963264217629735
          },
          "jarvis_memory": {
            "e2e_change_pct": 27.25144955457912,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.318008620031563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -26.383926037388207,
            "ttft_change_pct": 0.3839665525818603
          },
          "long_context": {
            "e2e_change_pct": 8.050657396442439,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.978346810431011,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -25.591456655856103,
            "ttft_change_pct": -0.1400910207492112
          },
          "math": {
            "e2e_change_pct": 33.615877669457596,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 27.145912810453577,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -31.904090067310765,
            "ttft_change_pct": 0.7963902249455757
          },
          "prefill": {
            "e2e_change_pct": 0.24620593570254812,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4829581012163464,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15448147762954223,
            "ttft_change_pct": 0.20134133223608242
          },
          "prefill2048": {
            "e2e_change_pct": 0.04510340797858614,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1890902265035299,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.04845708010081662,
            "ttft_change_pct": 0.058810898566941106
          },
          "prefill4096": {
            "e2e_change_pct": -0.048934086933649645,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.13248277352106985,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.04699461067994015,
            "ttft_change_pct": -0.046797531082065635
          },
          "pve_sim": {
            "e2e_change_pct": 28.17020188086785,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 11.265552600203366,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -27.666239347474743,
            "ttft_change_pct": 0.4383978926701282
          },
          "sorting": {
            "e2e_change_pct": 28.299777987585696,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 13.658174695516912,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -26.211252501671424,
            "ttft_change_pct": 0.8493589258347756
          },
          "spec-branch": {
            "e2e_change_pct": 0.644843962937558,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4123832094667934,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.7385747916491492
          },
          "spec-code": {
            "e2e_change_pct": 11.319602059802358,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.5012388297952075,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -11.206556310651328
          },
          "spec-repeat": {
            "e2e_change_pct": 29.026951503860367,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.221674360661396,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -23.558801639728955
          },
          "time": {
            "e2e_change_pct": 27.01035859218377,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 12.205097775681327,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -25.440834941378032,
            "ttft_change_pct": 0.20825216862925267
          },
          "tool-call": {
            "e2e_change_pct": 9.495146154226951,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.953965167863672,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -12.361923071804837,
            "ttft_change_pct": 23.88426618108994
          },
          "tool-final": {
            "e2e_change_pct": 1.5934303587306298,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.7192855627289045,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -2.681851122065082,
            "ttft_change_pct": -0.04885812708868009
          }
        }
      },
      "complete": true,
      "speculation": {
        "arms": {
          "A": {
            "accepted_n": 0,
            "checkpoint_events": 0,
            "draft_n": 0,
            "median_e2e_s": 3.5640341935,
            "restore_events": 0,
            "starts": 2
          },
          "B": {
            "acceptance_pct": 0.0,
            "accepted_n": 0,
            "checkpoint_events": 252,
            "draft_n": 1608,
            "median_e2e_s": 3.92441585,
            "restore_events": 252,
            "starts": 2
          }
        },
        "change_exercised": true,
        "note": "Token drift is reported separately from semantic quality and protocol validity. No draft is inactivity, not an optimization gain. Internal RAM checkpoint trace is not a new model checkpoint."
      }
    }
  }
}
```
