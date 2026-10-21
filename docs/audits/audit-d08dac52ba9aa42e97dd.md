# Public audit excerpt

Original SHA256: `d08dac52ba9aa42e97dd44003afd3edd21b0fc7aef4872e41bd24ef0e10b0762`

Original file: `RESULTS.json`; 39513 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.5276170474999999,
              "format_passes": 2,
              "gpu_energy_j": 130.43072283735023,
              "semantic_passes": 2,
              "tokens_per_s": 96.4355977757564,
              "ttft_s": 0.133517168
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.3667071769999999,
              "format_passes": 0,
              "gpu_energy_j": 356.6500188830561,
              "semantic_passes": 0,
              "tokens_per_s": 97.06452761903586,
              "ttft_s": 0.058112612
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20547787299999998,
              "format_passes": 2,
              "gpu_energy_j": 45.717464864579625,
              "semantic_passes": 2,
              "tokens_per_s": 94.89928115257115,
              "ttft_s": 0.06845535999999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.230201043,
              "format_passes": 0,
              "gpu_energy_j": 53.68232948193116,
              "semantic_passes": 0,
              "tokens_per_s": 94.07141115666268,
              "ttft_s": 0.1344912125
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15740101750000002,
              "format_passes": 2,
              "gpu_energy_j": 31.949419011410246,
              "semantic_passes": 2,
              "tokens_per_s": 93.96632091747706,
              "ttft_s": 0.061603275
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.307648714,
              "format_passes": 0,
              "gpu_energy_j": 73.16477849122981,
              "semantic_passes": 0,
              "tokens_per_s": 95.70382682914996,
              "ttft_s": 0.0777751405
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3987166585,
              "format_passes": 0,
              "gpu_energy_j": 93.58350293614679,
              "semantic_passes": 2,
              "tokens_per_s": 96.30585628532597,
              "ttft_s": 0.10795856300000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0320972880000001,
              "format_passes": 2,
              "gpu_energy_j": 273.90709500546814,
              "semantic_passes": 2,
              "tokens_per_s": 94.08413893912962,
              "ttft_s": 0.8725688415
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.148871769,
              "format_passes": 0,
              "gpu_energy_j": 31.94778545052383,
              "semantic_passes": 0,
              "tokens_per_s": 93.76231373853597,
              "ttft_s": 0.0635158465
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2061700135,
              "format_passes": 0,
              "gpu_energy_j": 50.297728165030875,
              "semantic_passes": 0,
              "tokens_per_s": 2461.997537039907,
              "ttft_s": 0.2059831325
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7555689905,
              "format_passes": 0,
              "gpu_energy_j": 201.357220878965,
              "semantic_passes": 0,
              "tokens_per_s": 2715.2650897368476,
              "ttft_s": 0.7552827065000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4954201435,
              "format_passes": 0,
              "gpu_energy_j": 406.17277831143383,
              "semantic_passes": 0,
              "tokens_per_s": 2742.524967758218,
              "ttft_s": 1.494918915
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2551740945,
              "format_passes": 2,
              "gpu_energy_j": 55.13634260032148,
              "semantic_passes": 2,
              "tokens_per_s": 95.53164800064462,
              "ttft_s": 0.0772309585
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3517332355,
              "format_passes": 0,
              "gpu_energy_j": 85.27139304633079,
              "semantic_passes": 2,
              "tokens_per_s": 96.04971438870183,
              "ttft_s": 0.0706094595
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.321329505,
              "format_passes": 0,
              "gpu_energy_j": 72.4637382890577,
              "semantic_passes": 0,
              "tokens_per_s": 94.99947609546165,
              "ttft_s": 0.0791072645
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.551270197,
              "format_passes": 0,
              "gpu_energy_j": 138.26056977056496,
              "semantic_passes": 0,
              "tokens_per_s": 96.01368633487772,
              "ttft_s": 0.30368709
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5246688865,
              "format_passes": 0,
              "gpu_energy_j": 131.97749022058332,
              "semantic_passes": 0,
              "tokens_per_s": 95.87173847677677,
              "ttft_s": 0.27449760700000003
            }
          }
        },
        "B": {
          "format_passes": 10,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5271668865,
              "format_passes": 2,
              "gpu_energy_j": 130.7822145180827,
              "semantic_passes": 2,
              "tokens_per_s": 96.29692774531932,
              "ttft_s": 0.1325172895
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.367641999,
              "format_passes": 0,
              "gpu_energy_j": 356.6152024079678,
              "semantic_passes": 0,
              "tokens_per_s": 96.95844576889274,
              "ttft_s": 0.05779192
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.205089221,
              "format_passes": 2,
              "gpu_energy_j": 47.85042097662155,
              "semantic_passes": 2,
              "tokens_per_s": 94.82131834461009,
              "ttft_s": 0.067952782
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.229777597,
              "format_passes": 0,
              "gpu_energy_j": 54.90381956297679,
              "semantic_passes": 0,
              "tokens_per_s": 94.17778818875976,
              "ttft_s": 0.13418746850000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15703239800000002,
              "format_passes": 2,
              "gpu_energy_j": 31.826992965287406,
              "semantic_passes": 2,
              "tokens_per_s": 93.63100735802908,
              "ttft_s": 0.0608711425
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3080608775,
              "format_passes": 0,
              "gpu_energy_j": 69.67479584611115,
              "semantic_passes": 0,
              "tokens_per_s": 95.46630549421874,
              "ttft_s": 0.077627799
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3984994815,
              "format_passes": 0,
              "gpu_energy_j": 93.37312431785864,
              "semantic_passes": 2,
              "tokens_per_s": 96.27831551933463,
              "ttft_s": 0.107605005
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0305118580000001,
              "format_passes": 2,
              "gpu_energy_j": 275.7299938886274,
              "semantic_passes": 2,
              "tokens_per_s": 94.0992081033292,
              "ttft_s": 0.871058659
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.149236491,
              "format_passes": 0,
              "gpu_energy_j": 31.39338801831426,
              "semantic_passes": 0,
              "tokens_per_s": 93.35856526375179,
              "ttft_s": 0.06352353599999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205909266,
              "format_passes": 0,
              "gpu_energy_j": 50.71721612642579,
              "semantic_passes": 0,
              "tokens_per_s": 2465.1914232744657,
              "ttft_s": 0.205780025
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7559549985,
              "format_passes": 0,
              "gpu_energy_j": 201.4277417854588,
              "semantic_passes": 0,
              "tokens_per_s": 2713.760965882554,
              "ttft_s": 0.7557204475
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4967761025000001,
              "format_passes": 0,
              "gpu_energy_j": 405.82877787096606,
              "semantic_passes": 0,
              "tokens_per_s": 2739.569710848071,
              "ttft_s": 1.4964913004999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2545616785,
              "format_passes": 2,
              "gpu_energy_j": 59.17152547272536,
              "semantic_passes": 2,
              "tokens_per_s": 95.51985768741268,
              "ttft_s": 0.0765807745
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35126909900000003,
              "format_passes": 0,
              "gpu_energy_j": 86.82816541858963,
              "semantic_passes": 2,
              "tokens_per_s": 96.23387800943193,
              "ttft_s": 0.070671082
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.314689719,
              "format_passes": 0,
              "gpu_energy_j": 74.94454523805358,
              "semantic_passes": 0,
              "tokens_per_s": 95.96305003838808,
              "ttft_s": 0.074935341
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.550457977,
              "format_passes": 0,
              "gpu_energy_j": 140.9395568304542,
              "semantic_passes": 0,
              "tokens_per_s": 96.16985866656242,
              "ttft_s": 0.3034424055
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.524227082,
              "format_passes": 0,
              "gpu_energy_j": 132.42284253250205,
              "semantic_passes": 0,
              "tokens_per_s": 95.91329438341063,
              "ttft_s": 0.2740614605
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
            "e2e_change_pct": -0.08531964653775148,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2694853429362487,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14379547971438145,
            "ttft_change_pct": -0.7488763542378263
          },
          "decode": {
            "e2e_change_pct": 0.0683995822757133,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.009762084184750108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10929002875228466,
            "ttft_change_pct": -0.551845785214411
          },
          "energy": {
            "e2e_change_pct": -0.18914542686550018,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.665517036782307,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.08215321234701367,
            "ttft_change_pct": -0.734168953314962
          },
          "filtering": {
            "e2e_change_pct": -0.18394616917526418,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.2754043888068676,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11308114844787998,
            "ttft_change_pct": -0.22584672585950205
          },
          "german": {
            "e2e_change_pct": -0.2341913069272228,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.38318708105182786,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.35684440571261966,
            "ttft_change_pct": -1.1884636003524074
          },
          "ha_sim": {
            "e2e_change_pct": 0.13397211860277647,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.77003104101108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.24818373810197025,
            "ttft_change_pct": -0.18944549511936692
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.054469005839141715,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22480310277730453,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.028597187184287165,
            "ttft_change_pct": -0.32749417014749094
          },
          "long_context": {
            "e2e_change_pct": -0.1536124567357633,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6655172196700088,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.016016689284192864,
            "ttft_change_pct": -0.17307316376367066
          },
          "math": {
            "e2e_change_pct": 0.2449907074053792,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.735323511133957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4306084808338495,
            "ttft_change_pct": 0.012106427645575124
          },
          "prefill": {
            "e2e_change_pct": -0.12647207786111725,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8340097588872109,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12972743418739885,
            "ttft_change_pct": -0.09860394758294255
          },
          "prefill2048": {
            "e2e_change_pct": 0.05108838568725904,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.03502278497189426,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05539510156775673,
            "ttft_change_pct": 0.057957238558858926
          },
          "prefill4096": {
            "e2e_change_pct": 0.09067411629393174,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.08469313032198889,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.10775679145640371,
            "ttft_change_pct": 0.10518199242932624
          },
          "pve_sim": {
            "e2e_change_pct": -0.23999928409660365,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.318553756194102,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.012341787751701805,
            "ttft_change_pct": -0.8418696499798095
          },
          "sorting": {
            "e2e_change_pct": -0.13195696430000625,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.8256678079751731,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.19173781192602934,
            "ttft_change_pct": 0.08727230095848526
          },
          "time": {
            "e2e_change_pct": -2.0663480622484465,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4235149987707603,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.0142939545878749,
            "ttft_change_pct": -5.273755231417454
          },
          "tool-call": {
            "e2e_change_pct": -0.14733609841781625,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9376363516618422,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.16265632291212473,
            "ttft_change_pct": -0.08057125510340102
          },
          "tool-final": {
            "e2e_change_pct": -0.08420634639633162,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3374456592365682,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04334531457768076,
            "ttft_change_pct": -0.158888998984974
          }
        }
      },
      "complete": true
    }
  }
}
```
