# Public audit excerpt

Original SHA256: `7e9bfbb559a6609066ffe1fed339c04d7cd9367d35569a4d58d7674356479d12`

Original file: `RESULTS.json`; 39703 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6727364465000001,
              "format_passes": 2,
              "gpu_energy_j": 179.99876814804503,
              "semantic_passes": 2,
              "tokens_per_s": 78.37578586306824,
              "ttft_s": 0.124011072
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6593860005,
              "format_passes": 0,
              "gpu_energy_j": 454.16914274630454,
              "semantic_passes": 0,
              "tokens_per_s": 79.58154277985514,
              "ttft_s": 0.0633444345
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23819456249999998,
              "format_passes": 2,
              "gpu_energy_j": 53.98677094902611,
              "semantic_passes": 2,
              "tokens_per_s": 78.2380786775341,
              "ttft_s": 0.0720073375
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24236716549999998,
              "format_passes": 0,
              "gpu_energy_j": 57.27106795730463,
              "semantic_passes": 0,
              "tokens_per_s": 77.7290389649568,
              "ttft_s": 0.1265622825
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1831209205,
              "format_passes": 2,
              "gpu_energy_j": 38.00525248440472,
              "semantic_passes": 2,
              "tokens_per_s": 77.28456159452438,
              "ttft_s": 0.066639231
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358095422,
              "format_passes": 0,
              "gpu_energy_j": 91.43695358417703,
              "semantic_passes": 0,
              "tokens_per_s": 78.93141219974206,
              "ttft_s": 0.07931990450000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46928937,
              "format_passes": 0,
              "gpu_energy_j": 117.31364908625068,
              "semantic_passes": 2,
              "tokens_per_s": 79.16628957854817,
              "ttft_s": 0.1155697425
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0799390835,
              "format_passes": 2,
              "gpu_energy_j": 286.7844228280533,
              "semantic_passes": 2,
              "tokens_per_s": 78.0724110665026,
              "ttft_s": 0.8237158135
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2346392135,
              "format_passes": 0,
              "gpu_energy_j": 55.88758443082091,
              "semantic_passes": 0,
              "tokens_per_s": 78.1611965835265,
              "ttft_s": 0.06831121500000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.198961216,
              "format_passes": 0,
              "gpu_energy_j": 48.89313007548688,
              "semantic_passes": 0,
              "tokens_per_s": 2551.3043500632402,
              "ttft_s": 0.198832081
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7158750094999999,
              "format_passes": 0,
              "gpu_energy_j": 189.6524154944609,
              "semantic_passes": 0,
              "tokens_per_s": 2866.03278540304,
              "ttft_s": 0.715615307
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.414859221,
              "format_passes": 0,
              "gpu_energy_j": 380.3392454521228,
              "semantic_passes": 0,
              "tokens_per_s": 2898.299479802327,
              "ttft_s": 1.414590809
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2954288815,
              "format_passes": 2,
              "gpu_energy_j": 71.37020307709395,
              "semantic_passes": 2,
              "tokens_per_s": 78.64255511845923,
              "ttft_s": 0.079229507
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35358965200000003,
              "format_passes": 2,
              "gpu_energy_j": 88.27032290956762,
              "semantic_passes": 2,
              "tokens_per_s": 78.831864179715,
              "ttft_s": 0.074477076
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36920581900000005,
              "format_passes": 2,
              "gpu_energy_j": 93.77988726532183,
              "semantic_passes": 2,
              "tokens_per_s": 78.91353249650393,
              "ttft_s": 0.07769369549999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6196963795,
              "format_passes": 0,
              "gpu_energy_j": 159.25144546654485,
              "semantic_passes": 0,
              "tokens_per_s": 78.94576477349595,
              "ttft_s": 0.318167211
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560675595,
              "format_passes": 0,
              "gpu_energy_j": 143.50602182285184,
              "semantic_passes": 0,
              "tokens_per_s": 78.75411028624355,
              "ttft_s": 0.2561312685
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
              "e2e_s": 0.6666116925,
              "format_passes": 2,
              "gpu_energy_j": 178.87954700174242,
              "semantic_passes": 2,
              "tokens_per_s": 79.32087370747678,
              "ttft_s": 0.1244754765
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6591761434999999,
              "format_passes": 0,
              "gpu_energy_j": 447.9278745058949,
              "semantic_passes": 0,
              "tokens_per_s": 79.59056609919077,
              "ttft_s": 0.06340475000000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24086142,
              "format_passes": 2,
              "gpu_energy_j": 56.19347204367773,
              "semantic_passes": 2,
              "tokens_per_s": 78.2540746471033,
              "ttft_s": 0.074727714
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241892394,
              "format_passes": 0,
              "gpu_energy_j": 57.88130596823554,
              "semantic_passes": 0,
              "tokens_per_s": 77.57484071192093,
              "ttft_s": 0.1258454115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1840665515,
              "format_passes": 2,
              "gpu_energy_j": 41.639174552371685,
              "semantic_passes": 2,
              "tokens_per_s": 77.23864728103072,
              "ttft_s": 0.067545105
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35835427200000003,
              "format_passes": 0,
              "gpu_energy_j": 90.74290540438565,
              "semantic_passes": 0,
              "tokens_per_s": 78.76402970560184,
              "ttft_s": 0.0790196165
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4764664515,
              "format_passes": 0,
              "gpu_energy_j": 115.8815347529806,
              "semantic_passes": 2,
              "tokens_per_s": 78.11602938929637,
              "ttft_s": 0.11788681200000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.083445882,
              "format_passes": 2,
              "gpu_energy_j": 288.65716379421207,
              "semantic_passes": 2,
              "tokens_per_s": 76.65165052591477,
              "ttft_s": 0.822507246
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23379406749999998,
              "format_passes": 0,
              "gpu_energy_j": 56.914494545986194,
              "semantic_passes": 0,
              "tokens_per_s": 78.34019955490268,
              "ttft_s": 0.06780299349999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19894863299999999,
              "format_passes": 0,
              "gpu_energy_j": 48.268777128945686,
              "semantic_passes": 0,
              "tokens_per_s": 2552.080930928925,
              "ttft_s": 0.198817764
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7158806449999999,
              "format_passes": 0,
              "gpu_energy_j": 189.60426870710205,
              "semantic_passes": 0,
              "tokens_per_s": 2865.600189877013,
              "ttft_s": 0.715658041
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.413784773,
              "format_passes": 0,
              "gpu_energy_j": 382.96057421791124,
              "semantic_passes": 0,
              "tokens_per_s": 2900.6528842725074,
              "ttft_s": 1.41345222
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29593899,
              "format_passes": 2,
              "gpu_energy_j": 70.62199058460845,
              "semantic_passes": 2,
              "tokens_per_s": 78.52038177283767,
              "ttft_s": 0.0793606585
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3545015925,
              "format_passes": 2,
              "gpu_energy_j": 87.75949862684402,
              "semantic_passes": 2,
              "tokens_per_s": 78.59762267111698,
              "ttft_s": 0.074570011
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369833285,
              "format_passes": 2,
              "gpu_energy_j": 95.09633555497193,
              "semantic_passes": 2,
              "tokens_per_s": 78.75782149034629,
              "ttft_s": 0.077735168
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6192746145,
              "format_passes": 0,
              "gpu_energy_j": 162.1522323654212,
              "semantic_passes": 0,
              "tokens_per_s": 79.05649817358903,
              "ttft_s": 0.3180915775
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561207292,
              "format_passes": 0,
              "gpu_energy_j": 145.67248991100757,
              "semantic_passes": 0,
              "tokens_per_s": 78.8665561441641,
              "ttft_s": 0.2565194785
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
            "e2e_change_pct": -0.9104239902364419,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6217937810452545,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.205841618047332,
            "ttft_change_pct": 0.37448632006020777
          },
          "decode": {
            "e2e_change_pct": -0.012646665690618786,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3742167076057688,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.011338457411635972,
            "ttft_change_pct": 0.0952183099842907
          },
          "energy": {
            "e2e_change_pct": 1.119613089404603,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.087484870571667,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.02044524845135065,
            "ttft_change_pct": 3.7779156881060816
          },
          "filtering": {
            "e2e_change_pct": -0.19588936439493,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0655258103198673,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1983792094810144,
            "ttft_change_pct": -0.5664175659916726
          },
          "german": {
            "e2e_change_pct": 0.5163970328556866,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.561631170476037,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05940942478854794,
            "ttft_change_pct": 1.3593704285092878
          },
          "ha_sim": {
            "e2e_change_pct": 0.07228520223865331,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7590456074768936,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.21206068594926686,
            "ttft_change_pct": -0.37857836805641476
          },
          "jarvis_memory": {
            "e2e_change_pct": 1.529350963138154,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2207567869763958,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.3266507687084927,
            "ttft_change_pct": 2.0049101519803214
          },
          "long_context": {
            "e2e_change_pct": 0.3247218804818708,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6530134892583028,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -1.8197984680883073,
            "ttft_change_pct": -0.14672141534648464
          },
          "math": {
            "e2e_change_pct": -0.3601895810139255,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8374566115599844,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2290176957371548,
            "ttft_change_pct": -0.7439795939803151
          },
          "prefill": {
            "e2e_change_pct": -0.006324348158393001,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2769747929356257,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.030438581961633737,
            "ttft_change_pct": -0.0072005482857573355
          },
          "prefill2048": {
            "e2e_change_pct": 0.0007872184285329098,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.025386856915754485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.015093879184868708,
            "ttft_change_pct": 0.00597164420352847
          },
          "prefill4096": {
            "e2e_change_pct": -0.07594027618101906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.689208068095204,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.08119949255005476,
            "ttft_change_pct": -0.0804889295728417
          },
          "pve_sim": {
            "e2e_change_pct": 0.17266710600871704,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0483541593363177,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15535271639830484,
            "ttft_change_pct": 0.16553365654541352
          },
          "sorting": {
            "e2e_change_pct": 0.2579092727521326,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5787044454872325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.29714064361590076,
            "ttft_change_pct": 0.12478336286994018
          },
          "time": {
            "e2e_change_pct": 0.16995019246972554,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4037639925132295,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19731850955290176,
            "ttft_change_pct": 0.05337949203356729
          },
          "tool-call": {
            "e2e_change_pct": -0.06805994257064185,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8215137014161442,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14026515597231892,
            "ttft_change_pct": -0.023771619885748496
          },
          "tool-final": {
            "e2e_change_pct": 0.09483148628932625,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.509670507646077,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.14278093868604902,
            "ttft_change_pct": 0.15156681270251937
          }
        }
      },
      "complete": true
    }
  }
}
```
