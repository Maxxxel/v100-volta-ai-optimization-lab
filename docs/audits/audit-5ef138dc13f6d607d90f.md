# Public audit excerpt

Original SHA256: `5ef138dc13f6d607d90fb8cedd689d601547e96b5ca4499b294f65f00d7d79a8`

Original file: `RESULTS.json`; 39686 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
      "arms": {
        "A": {
          "format_passes": 16,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.6661571155,
              "format_passes": 2,
              "gpu_energy_j": 175.45938076162787,
              "semantic_passes": 2,
              "tokens_per_s": 79.32730679324939,
              "ttft_s": 0.124064073
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658792893,
              "format_passes": 0,
              "gpu_energy_j": 458.62243794243545,
              "semantic_passes": 0,
              "tokens_per_s": 79.61386650074061,
              "ttft_s": 0.06344090899999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.239196338,
              "format_passes": 2,
              "gpu_energy_j": 57.05572834514239,
              "semantic_passes": 2,
              "tokens_per_s": 78.26925045040929,
              "ttft_s": 0.073075398
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24182528650000001,
              "format_passes": 0,
              "gpu_energy_j": 55.83272424464636,
              "semantic_passes": 0,
              "tokens_per_s": 77.55745922868871,
              "ttft_s": 0.125750062
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1835890835,
              "format_passes": 2,
              "gpu_energy_j": 42.930888085073754,
              "semantic_passes": 2,
              "tokens_per_s": 77.46246101524488,
              "ttft_s": 0.067407104
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.357818074,
              "format_passes": 0,
              "gpu_energy_j": 89.11294701084026,
              "semantic_passes": 0,
              "tokens_per_s": 78.90848197546663,
              "ttft_s": 0.078959477
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4698967185,
              "format_passes": 0,
              "gpu_energy_j": 118.45100835835336,
              "semantic_passes": 2,
              "tokens_per_s": 79.00973579517898,
              "ttft_s": 0.1154874085
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.079395697,
              "format_passes": 2,
              "gpu_energy_j": 289.4984298424386,
              "semantic_passes": 2,
              "tokens_per_s": 77.85491971241143,
              "ttft_s": 0.8225179345
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2341574935,
              "format_passes": 0,
              "gpu_energy_j": 58.78749687621795,
              "semantic_passes": 0,
              "tokens_per_s": 78.05033921013263,
              "ttft_s": 0.067528797
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199198724,
              "format_passes": 0,
              "gpu_energy_j": 48.59223436230673,
              "semantic_passes": 0,
              "tokens_per_s": 2549.829370344414,
              "ttft_s": 0.1989916255
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7175722255,
              "format_passes": 0,
              "gpu_energy_j": 189.76532087917127,
              "semantic_passes": 0,
              "tokens_per_s": 2859.0750431672323,
              "ttft_s": 0.7173127754999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4182483065,
              "format_passes": 0,
              "gpu_energy_j": 381.0389405120794,
              "semantic_passes": 0,
              "tokens_per_s": 2891.4828757015434,
              "ttft_s": 1.4179287155
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29586543,
              "format_passes": 2,
              "gpu_energy_j": 71.3452885141838,
              "semantic_passes": 2,
              "tokens_per_s": 78.48944617996402,
              "ttft_s": 0.07925412
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3538422065,
              "format_passes": 2,
              "gpu_energy_j": 88.60871896367806,
              "semantic_passes": 2,
              "tokens_per_s": 78.71642063769107,
              "ttft_s": 0.074338914
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369221296,
              "format_passes": 2,
              "gpu_energy_j": 94.5778770692747,
              "semantic_passes": 2,
              "tokens_per_s": 78.91538911567241,
              "ttft_s": 0.077688953
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6197446765000001,
              "format_passes": 0,
              "gpu_energy_j": 163.06753398883387,
              "semantic_passes": 0,
              "tokens_per_s": 78.98322332473222,
              "ttft_s": 0.31898407900000003
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.560671041,
              "format_passes": 0,
              "gpu_energy_j": 147.18533564046786,
              "semantic_passes": 0,
              "tokens_per_s": 78.7917315491828,
              "ttft_s": 0.2561996655
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
              "e2e_s": 0.6666037705000001,
              "format_passes": 2,
              "gpu_energy_j": 175.763982470131,
              "semantic_passes": 2,
              "tokens_per_s": 79.31124192430237,
              "ttft_s": 0.1244169925
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.65794028,
              "format_passes": 0,
              "gpu_energy_j": 454.4393900417783,
              "semantic_passes": 0,
              "tokens_per_s": 79.65901041076124,
              "ttft_s": 0.0635161155
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2381892315,
              "format_passes": 2,
              "gpu_energy_j": 57.52694850892928,
              "semantic_passes": 2,
              "tokens_per_s": 78.24920164111789,
              "ttft_s": 0.0720352195
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2431978815,
              "format_passes": 0,
              "gpu_energy_j": 57.75690056967627,
              "semantic_passes": 0,
              "tokens_per_s": 77.2397494605176,
              "ttft_s": 0.1266824765
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182938773,
              "format_passes": 2,
              "gpu_energy_j": 40.77285918134455,
              "semantic_passes": 2,
              "tokens_per_s": 77.46516382395995,
              "ttft_s": 0.0667010345
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.358533883,
              "format_passes": 0,
              "gpu_energy_j": 89.41289135545881,
              "semantic_passes": 0,
              "tokens_per_s": 78.76695232918763,
              "ttft_s": 0.0791809455
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47022926,
              "format_passes": 0,
              "gpu_energy_j": 116.78051878112964,
              "semantic_passes": 2,
              "tokens_per_s": 78.8594089536842,
              "ttft_s": 0.1151382295
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.079398712,
              "format_passes": 2,
              "gpu_energy_j": 283.10792545095086,
              "semantic_passes": 2,
              "tokens_per_s": 78.00068643570066,
              "ttft_s": 0.8229392824999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23400192549999999,
              "format_passes": 0,
              "gpu_energy_j": 54.292371608451084,
              "semantic_passes": 0,
              "tokens_per_s": 78.42077432220881,
              "ttft_s": 0.068178079
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1998509735,
              "format_passes": 0,
              "gpu_energy_j": 49.28098767046447,
              "semantic_passes": 0,
              "tokens_per_s": 2540.3487500121946,
              "ttft_s": 0.1996881795
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7167996245,
              "format_passes": 0,
              "gpu_energy_j": 191.2288265802864,
              "semantic_passes": 0,
              "tokens_per_s": 2861.9823090915343,
              "ttft_s": 0.7165567724999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4164674860000002,
              "format_passes": 0,
              "gpu_energy_j": 380.95243000624475,
              "semantic_passes": 0,
              "tokens_per_s": 2895.09032252832,
              "ttft_s": 1.4161651604999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29553997249999997,
              "format_passes": 2,
              "gpu_energy_j": 70.85682417629982,
              "semantic_passes": 2,
              "tokens_per_s": 78.53626892666765,
              "ttft_s": 0.0790607155
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3540657855,
              "format_passes": 2,
              "gpu_energy_j": 88.23990817350659,
              "semantic_passes": 2,
              "tokens_per_s": 78.80392760409399,
              "ttft_s": 0.074847138
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3701166735,
              "format_passes": 2,
              "gpu_energy_j": 95.1104828596225,
              "semantic_passes": 2,
              "tokens_per_s": 78.7071506794839,
              "ttft_s": 0.07781250149999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6199330555,
              "format_passes": 0,
              "gpu_energy_j": 163.4894404094477,
              "semantic_passes": 0,
              "tokens_per_s": 79.06958027195378,
              "ttft_s": 0.319063312
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5604343555,
              "format_passes": 0,
              "gpu_energy_j": 147.94567114498912,
              "semantic_passes": 0,
              "tokens_per_s": 78.81670120254554,
              "ttft_s": 0.2558807575
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
            "e2e_change_pct": 0.0670494977246916,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.17360240711037367,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.020251373198509892,
            "ttft_change_pct": 0.28446551162317757
          },
          "decode": {
            "e2e_change_pct": -0.0513996053152832,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9120896743351592,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.056703576907923825,
            "ttft_change_pct": 0.11854574782339533
          },
          "energy": {
            "e2e_change_pct": -0.4210375913029307,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8258945726472566,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.02561517987718087,
            "ttft_change_pct": -1.4234318641685673
          },
          "filtering": {
            "e2e_change_pct": 0.5675977975115432,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.4463235513972235,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.4096443737723554,
            "ttft_change_pct": 0.7414823381955982
          },
          "german": {
            "e2e_change_pct": -0.3542206800111858,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.0267511341781645,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.003489185186800192,
            "ttft_change_pct": -1.0474704565263449
          },
          "ha_sim": {
            "e2e_change_pct": 0.20004830723001632,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.33658896342196876,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.17935923076431992,
            "ttft_change_pct": 0.28048374737841275
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.0707690619891066,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4102788995851712,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19026369343202454,
            "ttft_change_pct": -0.3023524421712165
          },
          "long_context": {
            "e2e_change_pct": 0.0002793229589626023,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2074400869689814,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1872286604721607,
            "ttft_change_pct": 0.051226603375642554
          },
          "math": {
            "e2e_change_pct": -0.0664373356900616,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -7.64639677928749,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4746105088395236,
            "ttft_change_pct": 0.9614890666570064
          },
          "prefill": {
            "e2e_change_pct": 0.3274365853869643,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4174143609498424,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3718139120398867,
            "ttft_change_pct": 0.35004186646037105
          },
          "prefill2048": {
            "e2e_change_pct": -0.10766874365317758,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.771218731818224,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10168554096716687,
            "ttft_change_pct": -0.10539377323554033
          },
          "prefill4096": {
            "e2e_change_pct": -0.12556478945457972,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.022703849039262813,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.12476113405657241,
            "ttft_change_pct": -0.12437543444334676
          },
          "pve_sim": {
            "e2e_change_pct": -0.11000186807901269,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6846483461719788,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05965483129575233,
            "ttft_change_pct": -0.24403084659825325
          },
          "sorting": {
            "e2e_change_pct": 0.06318607444022462,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.41622404034826754,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11116735961063107,
            "ttft_change_pct": 0.6836580905661194
          },
          "time": {
            "e2e_change_pct": 0.24250429476853075,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5631399296028627,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2638755742346732,
            "ttft_change_pct": 0.15902968855814326
          },
          "tool-call": {
            "e2e_change_pct": 0.03039622721145996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2587310976584156,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10933581029797246,
            "ttft_change_pct": 0.024839170734902716
          },
          "tool-final": {
            "e2e_change_pct": -0.042214682530750114,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5165837352020919,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03169070265598428,
            "ttft_change_pct": -0.1244763529950843
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
