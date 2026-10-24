# Public audit excerpt

Original SHA256: `60e6ca5883fd80b09c9de35af4a2c449efd4da55cd82babe6636f22b4f31ddc5`

Original file: `RESULTS.json`; 47350 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7658300405,
              "format_passes": 2,
              "gpu_energy_j": 481.4086343234992,
              "semantic_passes": 2,
              "tokens_per_s": 35.30539487239209,
              "ttft_s": 0.5194773815
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7810548219999998,
              "format_passes": 0,
              "gpu_energy_j": 1068.212962682771,
              "semantic_passes": 0,
              "tokens_per_s": 35.42500307093026,
              "ttft_s": 0.195951088
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5822056950000001,
              "format_passes": 2,
              "gpu_energy_j": 147.59241271368805,
              "semantic_passes": 2,
              "tokens_per_s": 34.99129657613861,
              "ttft_s": 0.21063369850000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9246602835,
              "format_passes": 0,
              "gpu_energy_j": 246.37025545376184,
              "semantic_passes": 0,
              "tokens_per_s": 34.96305633916361,
              "ttft_s": 0.524195079
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465007866,
              "format_passes": 2,
              "gpu_energy_j": 108.61266177616469,
              "semantic_passes": 2,
              "tokens_per_s": 34.26402362138033,
              "ttft_s": 0.202296525
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.989066013,
              "format_passes": 0,
              "gpu_energy_j": 266.1190732593434,
              "semantic_passes": 0,
              "tokens_per_s": 35.32696132286253,
              "ttft_s": 0.2247549805
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.14716348,
              "format_passes": 0,
              "gpu_energy_j": 300.5806370459153,
              "semantic_passes": 2,
              "tokens_per_s": 35.32227232838426,
              "ttft_s": 0.3543966075
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7383408094999999,
              "format_passes": 0,
              "gpu_energy_j": 190.12900636113537,
              "semantic_passes": 0,
              "tokens_per_s": 694.2587292310578,
              "ttft_s": 0.738161691
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7964980065000002,
              "format_passes": 2,
              "gpu_energy_j": 1018.4168733876256,
              "semantic_passes": 2,
              "tokens_per_s": 34.33203257650794,
              "ttft_s": 3.2139326759999998
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.574997124,
              "format_passes": 2,
              "gpu_energy_j": 142.23287303431374,
              "semantic_passes": 2,
              "tokens_per_s": 34.92206373021957,
              "ttft_s": 0.202713025
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7234712045,
              "format_passes": 0,
              "gpu_energy_j": 189.87797639342114,
              "semantic_passes": 0,
              "tokens_per_s": 699.023022631083,
              "ttft_s": 0.7233077645
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.752784501,
              "format_passes": 0,
              "gpu_energy_j": 738.6218983065678,
              "semantic_passes": 0,
              "tokens_per_s": 744.3103036644898,
              "ttft_s": 2.7525292095
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4645867015,
              "format_passes": 0,
              "gpu_energy_j": 1480.538776454579,
              "semantic_passes": 0,
              "tokens_per_s": 749.7837932162106,
              "ttft_s": 5.4642449155
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8455916155000001,
              "format_passes": 0,
              "gpu_energy_j": 227.83405167907983,
              "semantic_passes": 2,
              "tokens_per_s": 35.280526540283816,
              "ttft_s": 0.221971937
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9914047155,
              "format_passes": 0,
              "gpu_energy_j": 260.0000635248506,
              "semantic_passes": 2,
              "tokens_per_s": 34.96335993412404,
              "ttft_s": 0.21907240449999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.014036049,
              "format_passes": 0,
              "gpu_energy_j": 271.95540697434643,
              "semantic_passes": 2,
              "tokens_per_s": 35.29075109498249,
              "ttft_s": 0.2205427445
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7077612455,
              "format_passes": 0,
              "gpu_energy_j": 466.08864734945956,
              "semantic_passes": 0,
              "tokens_per_s": 35.04175599553973,
              "ttft_s": 1.029494998
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7801324895000001,
              "format_passes": 0,
              "gpu_energy_j": 467.7426889077509,
              "semantic_passes": 0,
              "tokens_per_s": 34.99426323576289,
              "ttft_s": 1.092530231
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
              "e2e_s": 1.765692886,
              "format_passes": 2,
              "gpu_energy_j": 487.4278108931005,
              "semantic_passes": 2,
              "tokens_per_s": 35.335036731077395,
              "ttft_s": 0.5204267794999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7848793265,
              "format_passes": 0,
              "gpu_energy_j": 1071.6559121940304,
              "semantic_passes": 0,
              "tokens_per_s": 35.37027608701237,
              "ttft_s": 0.19459759799999998
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.581891912,
              "format_passes": 2,
              "gpu_energy_j": 150.83721645996522,
              "semantic_passes": 2,
              "tokens_per_s": 34.931929793038364,
              "ttft_s": 0.209627542
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.925173135,
              "format_passes": 0,
              "gpu_energy_j": 245.23205565060897,
              "semantic_passes": 0,
              "tokens_per_s": 34.95134220057594,
              "ttft_s": 0.5245770645
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46498895,
              "format_passes": 2,
              "gpu_energy_j": 111.18123778604209,
              "semantic_passes": 2,
              "tokens_per_s": 34.25343888684333,
              "ttft_s": 0.2021746495
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9902280485,
              "format_passes": 0,
              "gpu_energy_j": 266.2737063769798,
              "semantic_passes": 0,
              "tokens_per_s": 35.25465010075597,
              "ttft_s": 0.22430250950000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.146148862,
              "format_passes": 0,
              "gpu_energy_j": 300.8823945370903,
              "semantic_passes": 2,
              "tokens_per_s": 35.27852422887172,
              "ttft_s": 0.3524617505
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 11.185747798,
              "format_passes": 0,
              "gpu_energy_j": 3030.6365244987246,
              "semantic_passes": 0,
              "tokens_per_s": 732.5589696816162,
              "ttft_s": 11.18512127
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7991149195,
              "format_passes": 2,
              "gpu_energy_j": 1029.5995300640184,
              "semantic_passes": 2,
              "tokens_per_s": 34.37123926101802,
              "ttft_s": 3.217076432
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.578265594,
              "format_passes": 2,
              "gpu_energy_j": 146.92764155243628,
              "semantic_passes": 2,
              "tokens_per_s": 34.89960798234236,
              "ttft_s": 0.20578155599999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7274922690000001,
              "format_passes": 0,
              "gpu_energy_j": 189.82416869904876,
              "semantic_passes": 0,
              "tokens_per_s": 695.1786000672525,
              "ttft_s": 0.72735558
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7569650035,
              "format_passes": 0,
              "gpu_energy_j": 733.1604278325343,
              "semantic_passes": 0,
              "tokens_per_s": 743.1797819715316,
              "ttft_s": 2.7567334729999997
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4754707025,
              "format_passes": 0,
              "gpu_energy_j": 1481.5796694706298,
              "semantic_passes": 0,
              "tokens_per_s": 748.2950924227143,
              "ttft_s": 5.475138118
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.849056448,
              "format_passes": 0,
              "gpu_energy_j": 230.2656721986308,
              "semantic_passes": 2,
              "tokens_per_s": 35.13693387774198,
              "ttft_s": 0.22291605399999997
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.984827685,
              "format_passes": 0,
              "gpu_energy_j": 262.19648528906123,
              "semantic_passes": 2,
              "tokens_per_s": 35.07705963880086,
              "ttft_s": 0.215039085
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.018812212,
              "format_passes": 0,
              "gpu_energy_j": 277.43029013404214,
              "semantic_passes": 2,
              "tokens_per_s": 35.21730084150397,
              "ttft_s": 0.223701048
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.709590488,
              "format_passes": 0,
              "gpu_energy_j": 465.2741139902621,
              "semantic_passes": 0,
              "tokens_per_s": 34.97272445789196,
              "ttft_s": 1.0292285205
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779777936,
              "format_passes": 0,
              "gpu_energy_j": 468.72447484702695,
              "semantic_passes": 0,
              "tokens_per_s": 35.02197148847168,
              "ttft_s": 1.0938534080000002
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": 0,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.007767140486580892,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2503258438768539,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.083958439758125,
            "ttft_change_pct": 0.18276021898364636
          },
          "decode": {
            "e2e_change_pct": 0.10114914170902267,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.32230928022185523,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15448688545858236,
            "ttft_change_pct": -0.6907284944495995
          },
          "energy": {
            "e2e_change_pct": -0.053895556621108565,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.1984895338567956,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.16966156990229075,
            "ttft_change_pct": -0.477680687926596
          },
          "filtering": {
            "e2e_change_pct": 0.05546377509140221,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.46198750780874764,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03350433232734984,
            "ttft_change_pct": 0.07287086722156388
          },
          "german": {
            "e2e_change_pct": -0.004067888176317869,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.364895554415991,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.03089168585093116,
            "ttft_change_pct": -0.06024596814009353
          },
          "ha_sim": {
            "e2e_change_pct": 0.11748816405847684,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.0581067398674362,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.20469131620376446,
            "ttft_change_pct": -0.20131745200635542
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.08844580721832918,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.10039152692624675,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.12385414818679719,
            "ttft_change_pct": -0.5459581042970396
          },
          "length-prefill": {
            "e2e_change_pct": 1414.9843614326185,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1493.9895666115588,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 1415.2671029090293
          },
          "long_context": {
            "e2e_change_pct": 0.06892965558047415,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.098043146044425,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.11419855326859629,
            "ttft_change_pct": 0.09781648581117519
          },
          "math": {
            "e2e_change_pct": 0.5684324083680137,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.300761925121165,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.06430246519989469,
            "ttft_change_pct": 1.5137315424107456
          },
          "prefill": {
            "e2e_change_pct": 0.5558015958325724,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.028338038667996557,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5499708077368104,
            "ttft_change_pct": 0.5596256114847709
          },
          "prefill2048": {
            "e2e_change_pct": 0.1518645029598753,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7394135601117346,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15188849158640494,
            "ttft_change_pct": 0.15274183051317003
          },
          "prefill4096": {
            "e2e_change_pct": 0.19917336103409955,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.07030501548519474,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.19855067647041036,
            "ttft_change_pct": 0.19935421395735897
          },
          "pve_sim": {
            "e2e_change_pct": 0.4097524663783769,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.0672770385421027,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.40700260631847396,
            "ttft_change_pct": 0.42533169406904214
          },
          "sorting": {
            "e2e_change_pct": -0.6634052064885543,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8447773952181103,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.3251967342127404,
            "ttft_change_pct": -1.8410897115067715
          },
          "time": {
            "e2e_change_pct": 0.4710052472700621,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.0131547376118775,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.20812890403163475,
            "ttft_change_pct": 1.4320595797246982
          },
          "tool-call": {
            "e2e_change_pct": 0.1071134799914164,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1747593218220489,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1969979405614275,
            "ttft_change_pct": -0.02588429283462146
          },
          "tool-final": {
            "e2e_change_pct": -0.019917253468015872,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.20989872478149874,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.07917941441462073,
            "ttft_change_pct": 0.1211112482250476
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
