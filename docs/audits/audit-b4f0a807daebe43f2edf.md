# Public audit excerpt

Original SHA256: `b4f0a807daebe43f2edf52127b00eb976a24d13fdd2c45b2264a5674c0f863be`

Original file: `RESULTS.json`; 40925 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6679645875,
              "format_passes": 2,
              "gpu_energy_j": 175.64770137180824,
              "semantic_passes": 2,
              "tokens_per_s": 79.00149101416037,
              "ttft_s": 0.12351593150000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6585348,
              "format_passes": 0,
              "gpu_energy_j": 458.7841297428157,
              "semantic_passes": 0,
              "tokens_per_s": 79.62087928286911,
              "ttft_s": 0.062711232
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2377275265,
              "format_passes": 2,
              "gpu_energy_j": 56.446225894032295,
              "semantic_passes": 2,
              "tokens_per_s": 78.39646238913548,
              "ttft_s": 0.071829157
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241360758,
              "format_passes": 0,
              "gpu_energy_j": 60.09653549917178,
              "semantic_passes": 0,
              "tokens_per_s": 77.49477421996217,
              "ttft_s": 0.125217351
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18186453000000002,
              "format_passes": 2,
              "gpu_energy_j": 41.78301189061721,
              "semantic_passes": 2,
              "tokens_per_s": 77.55177763138893,
              "ttft_s": 0.06575336200000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3596615015,
              "format_passes": 0,
              "gpu_energy_j": 91.29762540326466,
              "semantic_passes": 0,
              "tokens_per_s": 78.49573682991895,
              "ttft_s": 0.07935621400000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46878905049999997,
              "format_passes": 0,
              "gpu_energy_j": 120.20673046017848,
              "semantic_passes": 2,
              "tokens_per_s": 79.05506611524916,
              "ttft_s": 0.114574806
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.081601139,
              "format_passes": 2,
              "gpu_energy_j": 291.1713779220462,
              "semantic_passes": 2,
              "tokens_per_s": 77.82954811797617,
              "ttft_s": 0.824662317
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23403112650000002,
              "format_passes": 0,
              "gpu_energy_j": 52.969714347230436,
              "semantic_passes": 0,
              "tokens_per_s": 78.07731350094221,
              "ttft_s": 0.067404841
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199596628,
              "format_passes": 0,
              "gpu_energy_j": 49.30286571307407,
              "semantic_passes": 0,
              "tokens_per_s": 2543.8909922894977,
              "ttft_s": 0.199433549
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7195153075,
              "format_passes": 0,
              "gpu_energy_j": 189.66113041527555,
              "semantic_passes": 0,
              "tokens_per_s": 2851.3142416420696,
              "ttft_s": 0.7192465805
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4195830735,
              "format_passes": 0,
              "gpu_energy_j": 379.33923468816374,
              "semantic_passes": 0,
              "tokens_per_s": 2888.9344568884135,
              "ttft_s": 1.4192043895
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295748294,
              "format_passes": 2,
              "gpu_energy_j": 74.41963085205796,
              "semantic_passes": 2,
              "tokens_per_s": 78.59408883020662,
              "ttft_s": 0.0793794315
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3526142675,
              "format_passes": 2,
              "gpu_energy_j": 89.76153144631655,
              "semantic_passes": 2,
              "tokens_per_s": 78.82509377220906,
              "ttft_s": 0.073471112
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36984791100000003,
              "format_passes": 2,
              "gpu_energy_j": 94.48925971705495,
              "semantic_passes": 2,
              "tokens_per_s": 78.69738338430255,
              "ttft_s": 0.07752534050000001
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6207714875,
              "format_passes": 0,
              "gpu_energy_j": 162.85866677842026,
              "semantic_passes": 0,
              "tokens_per_s": 78.93252138127734,
              "ttft_s": 0.31957779799999997
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5608599525,
              "format_passes": 0,
              "gpu_energy_j": 144.26975032963418,
              "semantic_passes": 0,
              "tokens_per_s": 78.82174626315862,
              "ttft_s": 0.2560112645
            }
          }
        },
        "B": {
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 18,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.674411182,
              "format_passes": 2,
              "gpu_energy_j": 177.32752488111024,
              "semantic_passes": 2,
              "tokens_per_s": 78.22736344042187,
              "ttft_s": 0.12472644699999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6735488420000002,
              "format_passes": 0,
              "gpu_energy_j": 460.0353727191769,
              "semantic_passes": 0,
              "tokens_per_s": 78.89159202908856,
              "ttft_s": 0.063499581
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24018805,
              "format_passes": 2,
              "gpu_energy_j": 59.185268654698596,
              "semantic_passes": 2,
              "tokens_per_s": 77.50545389586347,
              "ttft_s": 0.0724159785
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2435533215,
              "format_passes": 0,
              "gpu_energy_j": 59.86109642004048,
              "semantic_passes": 0,
              "tokens_per_s": 76.81919654522892,
              "ttft_s": 0.1263684115
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.183809287,
              "format_passes": 2,
              "gpu_energy_j": 40.56914652509561,
              "semantic_passes": 2,
              "tokens_per_s": 76.79283650059614,
              "ttft_s": 0.06658245900000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3621064985,
              "format_passes": 0,
              "gpu_energy_j": 90.68430673122008,
              "semantic_passes": 0,
              "tokens_per_s": 78.01325757498685,
              "ttft_s": 0.080043513
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4732649505,
              "format_passes": 0,
              "gpu_energy_j": 119.47392257242271,
              "semantic_passes": 2,
              "tokens_per_s": 78.24313490214118,
              "ttft_s": 0.115374103
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0900915690000001,
              "format_passes": 2,
              "gpu_energy_j": 291.31514741506913,
              "semantic_passes": 2,
              "tokens_per_s": 76.28048630272914,
              "ttft_s": 0.8278648225
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2356388025,
              "format_passes": 0,
              "gpu_energy_j": 54.9479733508101,
              "semantic_passes": 0,
              "tokens_per_s": 77.53649813637892,
              "ttft_s": 0.0679743005
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19936501099999998,
              "format_passes": 0,
              "gpu_energy_j": 47.41409431739623,
              "semantic_passes": 0,
              "tokens_per_s": 2546.640146708168,
              "ttft_s": 0.199204509
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7212697994999999,
              "format_passes": 0,
              "gpu_energy_j": 189.73356882554413,
              "semantic_passes": 0,
              "tokens_per_s": 2844.4020952328683,
              "ttft_s": 0.72104272
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.423511778,
              "format_passes": 0,
              "gpu_energy_j": 386.9247191747635,
              "semantic_passes": 0,
              "tokens_per_s": 2880.9142240443934,
              "ttft_s": 1.423161364
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29775019,
              "format_passes": 2,
              "gpu_energy_j": 74.45209743462851,
              "semantic_passes": 2,
              "tokens_per_s": 77.85916422761017,
              "ttft_s": 0.07936571249999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.419125387,
              "format_passes": 0,
              "gpu_energy_j": 107.23680319799603,
              "semantic_passes": 2,
              "tokens_per_s": 78.30490956908051,
              "ttft_s": 0.0742746305
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3746487705,
              "format_passes": 2,
              "gpu_energy_j": 95.63579343350764,
              "semantic_passes": 2,
              "tokens_per_s": 77.53349592189369,
              "ttft_s": 0.07794926099999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6248444424999999,
              "format_passes": 0,
              "gpu_energy_j": 166.9309669441127,
              "semantic_passes": 0,
              "tokens_per_s": 78.15508056893628,
              "ttft_s": 0.320394646
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.564715194,
              "format_passes": 0,
              "gpu_energy_j": 148.4460519607117,
              "semantic_passes": 0,
              "tokens_per_s": 77.88364273228301,
              "ttft_s": 0.256708088
            }
          }
        }
      },
      "comparison": {
        "format_pass_change": -2,
        "note": "Descriptive paired comparison; actual fresh starts per arm: {'A': 2, 'B': 2}. Quality and speed remain separate.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": 0.9651102200084916,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9563595174787887,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9798898271422996,
            "ttft_change_pct": 0.9800480677263801
          },
          "decode": {
            "e2e_change_pct": 0.9052593891909932,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.27273022217717546,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9159497613554501,
            "ttft_change_pct": 1.2571097311562918
          },
          "energy": {
            "e2e_change_pct": 1.0350183406295566,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.852481662473518,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.136541708794614,
            "ttft_change_pct": 0.8169683795676397
          },
          "filtering": {
            "e2e_change_pct": 0.9084175564281205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.39176813967011226,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.8717719117623091,
            "ttft_change_pct": 0.9192500007447091
          },
          "german": {
            "e2e_change_pct": 1.0693437582358412,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.9051648279912134,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9786250605371194,
            "ttft_change_pct": 1.260919555717921
          },
          "ha_sim": {
            "e2e_change_pct": 0.6798050360694585,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6717794349366035,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.6146566354011229,
            "ttft_change_pct": 0.8660934857602776
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.9547791261818483,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6096230094192023,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0270451382892065,
            "ttft_change_pct": 0.697620208058658
          },
          "long_context": {
            "e2e_change_pct": 0.7849871541231845,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.04937624503100757,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.9903261071218314,
            "ttft_change_pct": 0.38834143794155285
          },
          "math": {
            "e2e_change_pct": 0.686949648127233,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.73469826665791,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.692666461374547,
            "ttft_change_pct": 0.8448347204023543
          },
          "prefill": {
            "e2e_change_pct": -0.11604254156037941,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.8309566155238284,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.10806887665402165,
            "ttft_change_pct": -0.11484527109327791
          },
          "prefill2048": {
            "e2e_change_pct": 0.24384359605857941,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.038193598292890485,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.24241966417635208,
            "ttft_change_pct": 0.24972513581522637
          },
          "prefill4096": {
            "e2e_change_pct": 0.2767505877844689,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.9996572442171345,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.27761906556572624,
            "ttft_change_pct": 0.2788163938383992
          },
          "pve_sim": {
            "e2e_change_pct": 0.6768918166608184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.04362636874011283,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9350889024035469,
            "ttft_change_pct": -0.017282814629393517
          },
          "sorting": {
            "e2e_change_pct": 18.86228823681957,
            "format_pass_change": -2,
            "gpu_energy_change_pct": 19.468553477311,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": 1.0936522915292013
          },
          "time": {
            "e2e_change_pct": 1.2980631652127927,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2134010996444955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.4789404836057396,
            "ttft_change_pct": 0.5468153990242364
          },
          "tool-call": {
            "e2e_change_pct": 0.6561118031375379,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.5005117911428565,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.9849435932569373,
            "ttft_change_pct": 0.2556022367987021
          },
          "tool-final": {
            "e2e_change_pct": 0.6873804205159484,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.894786759896184,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.1901582689421875,
            "ttft_change_pct": 0.2721847030289659
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
