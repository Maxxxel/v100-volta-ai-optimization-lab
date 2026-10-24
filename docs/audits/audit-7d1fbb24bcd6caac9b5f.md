# Public audit excerpt

Original SHA256: `7d1fbb24bcd6caac9b5f68a609de3247f7e2467a310e13c47c75d572ed83aea0`

Original file: `RESULTS.json`; 40904 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
          "format_passes": 14,
          "quality_attempts": 24,
          "quality_passes": 16,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.7331468665,
              "format_passes": 2,
              "gpu_energy_j": 183.3189957423796,
              "semantic_passes": 2,
              "tokens_per_s": 70.74864409889022,
              "ttft_s": 0.125307817
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8570789374999999,
              "format_passes": 0,
              "gpu_energy_j": 475.6643241186931,
              "semantic_passes": 0,
              "tokens_per_s": 70.8664824782381,
              "ttft_s": 0.06461635199999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.259570849,
              "format_passes": 2,
              "gpu_energy_j": 59.34753883940806,
              "semantic_passes": 2,
              "tokens_per_s": 69.76464778938383,
              "ttft_s": 0.073159214
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2570335675,
              "format_passes": 0,
              "gpu_energy_j": 61.67788589119098,
              "semantic_passes": 0,
              "tokens_per_s": 69.28364039359843,
              "ttft_s": 0.1270775165
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.197564455,
              "format_passes": 2,
              "gpu_energy_j": 43.6483131081353,
              "semantic_passes": 2,
              "tokens_per_s": 69.17800269144644,
              "ttft_s": 0.067399972
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.394548374,
              "format_passes": 0,
              "gpu_energy_j": 96.26891760634373,
              "semantic_passes": 0,
              "tokens_per_s": 70.05034533578049,
              "ttft_s": 0.08045931149999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5209804695,
              "format_passes": 0,
              "gpu_energy_j": 124.09436807408485,
              "semantic_passes": 2,
              "tokens_per_s": 69.58519365903788,
              "ttft_s": 0.1184542455
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1104422915,
              "format_passes": 2,
              "gpu_energy_j": 291.29175557433024,
              "semantic_passes": 2,
              "tokens_per_s": 69.64649181936011,
              "ttft_s": 0.8232039794999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.255445524,
              "format_passes": 0,
              "gpu_energy_j": 59.918750048261444,
              "semantic_passes": 0,
              "tokens_per_s": 69.63836035903296,
              "ttft_s": 0.068749371
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.2004559645,
              "format_passes": 0,
              "gpu_energy_j": 48.30935709837952,
              "semantic_passes": 0,
              "tokens_per_s": 2533.022844108576,
              "ttft_s": 0.2003220885
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7201192765,
              "format_passes": 0,
              "gpu_energy_j": 189.4818217969747,
              "semantic_passes": 0,
              "tokens_per_s": 2849.163128378603,
              "ttft_s": 0.719887748
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4229563305,
              "format_passes": 0,
              "gpu_energy_j": 381.32289141280296,
              "semantic_passes": 0,
              "tokens_per_s": 2882.2121360658675,
              "ttft_s": 1.4226151885
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3232864375,
              "format_passes": 2,
              "gpu_energy_j": 77.2844377765103,
              "semantic_passes": 2,
              "tokens_per_s": 70.02857686546645,
              "ttft_s": 0.08049574749999999
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.389453233,
              "format_passes": 2,
              "gpu_energy_j": 92.9290881745003,
              "semantic_passes": 2,
              "tokens_per_s": 70.3444371727658,
              "ttft_s": 0.0766650995
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.406018843,
              "format_passes": 0,
              "gpu_energy_j": 97.86167751034938,
              "semantic_passes": 0,
              "tokens_per_s": 70.40650819856405,
              "ttft_s": 0.079334955
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6735727435,
              "format_passes": 0,
              "gpu_energy_j": 167.63178202448023,
              "semantic_passes": 0,
              "tokens_per_s": 70.32371404420613,
              "ttft_s": 0.33449672500000005
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5706745285,
              "format_passes": 0,
              "gpu_energy_j": 140.90525097122992,
              "semantic_passes": 0,
              "tokens_per_s": 70.25196518978342,
              "ttft_s": 0.257674272
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
              "e2e_s": 0.675522971,
              "format_passes": 2,
              "gpu_energy_j": 177.26101060934195,
              "semantic_passes": 2,
              "tokens_per_s": 77.96771072014533,
              "ttft_s": 0.1239370405
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.686938289,
              "format_passes": 0,
              "gpu_energy_j": 462.2938451470949,
              "semantic_passes": 0,
              "tokens_per_s": 78.22135793822704,
              "ttft_s": 0.0632030055
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24101366200000002,
              "format_passes": 2,
              "gpu_energy_j": 59.25351735783397,
              "semantic_passes": 2,
              "tokens_per_s": 76.8588449705421,
              "ttft_s": 0.0718404325
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2438628685,
              "format_passes": 0,
              "gpu_energy_j": 63.012755905664704,
              "semantic_passes": 0,
              "tokens_per_s": 76.18100286356777,
              "ttft_s": 0.125632238
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.186987078,
              "format_passes": 2,
              "gpu_energy_j": 41.83477373137638,
              "semantic_passes": 2,
              "tokens_per_s": 75.07824727989822,
              "ttft_s": 0.06705525000000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36789916,
              "format_passes": 0,
              "gpu_energy_j": 92.96476347017102,
              "semantic_passes": 0,
              "tokens_per_s": 76.17971587568631,
              "ttft_s": 0.07900436999999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.47792258200000004,
              "format_passes": 0,
              "gpu_energy_j": 121.36129591059765,
              "semantic_passes": 2,
              "tokens_per_s": 77.30844506897003,
              "ttft_s": 0.11572036799999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0848154435,
              "format_passes": 2,
              "gpu_energy_j": 291.9454222430837,
              "semantic_passes": 2,
              "tokens_per_s": 76.67956693099364,
              "ttft_s": 0.8239167665
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23771805000000001,
              "format_passes": 0,
              "gpu_energy_j": 57.20466162910655,
              "semantic_passes": 0,
              "tokens_per_s": 77.01217452814792,
              "ttft_s": 0.0688669415
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199446758,
              "format_passes": 0,
              "gpu_energy_j": 48.76307102001399,
              "semantic_passes": 0,
              "tokens_per_s": 2545.602084940647,
              "ttft_s": 0.199305342
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7180744059999999,
              "format_passes": 0,
              "gpu_energy_j": 187.24672865378267,
              "semantic_passes": 0,
              "tokens_per_s": 2857.1349190578467,
              "ttft_s": 0.7178411165
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.417205566,
              "format_passes": 0,
              "gpu_energy_j": 383.0646463890962,
              "semantic_passes": 0,
              "tokens_per_s": 2893.9983476862517,
              "ttft_s": 1.4168890539999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29979099,
              "format_passes": 2,
              "gpu_energy_j": 73.38237644336014,
              "semantic_passes": 2,
              "tokens_per_s": 77.10698322333036,
              "ttft_s": 0.0792776865
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3582737805,
              "format_passes": 2,
              "gpu_energy_j": 88.48960098924508,
              "semantic_passes": 2,
              "tokens_per_s": 77.4588533387791,
              "ttft_s": 0.074247394
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37437384500000004,
              "format_passes": 0,
              "gpu_energy_j": 94.54785717204084,
              "semantic_passes": 0,
              "tokens_per_s": 77.55808242175078,
              "ttft_s": 0.077771764
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.62768967,
              "format_passes": 0,
              "gpu_energy_j": 166.99831176423942,
              "semantic_passes": 0,
              "tokens_per_s": 77.70959260359304,
              "ttft_s": 0.32137728099999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5402599459999999,
              "format_passes": 0,
              "gpu_energy_j": 143.0556877716645,
              "semantic_passes": 0,
              "tokens_per_s": 77.40892314660027,
              "ttft_s": 0.255644362
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
            "e2e_change_pct": -7.85980246701361,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3046139645839023,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.203823286230795,
            "ttft_change_pct": -1.0939273644835712
          },
          "decode": {
            "e2e_change_pct": -9.16173486567261,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.8109064089199776,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.378496579461949,
            "ttft_change_pct": -2.1872892174414016
          },
          "energy": {
            "e2e_change_pct": -7.149179914266868,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.15842524123621526,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.168756534936296,
            "ttft_change_pct": -1.802618464435668
          },
          "filtering": {
            "e2e_change_pct": -5.124116327724392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.164260326348777,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 9.955254127504865,
            "ttft_change_pct": -1.13732038507377
          },
          "german": {
            "e2e_change_pct": -5.353886659419582,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.154889954775609,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 8.529076236514888,
            "ttft_change_pct": -0.511457185768549
          },
          "ha_sim": {
            "e2e_change_pct": -6.754359099196283,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.432212824583558,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 8.749950497067772,
            "ttft_change_pct": -1.8082947428651575
          },
          "jarvis_memory": {
            "e2e_change_pct": -8.264779587865135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.2024143447473388,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.098986729526805,
            "ttft_change_pct": -2.3079607560372417
          },
          "long_context": {
            "e2e_change_pct": -2.3078054750042987,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.22440273582913228,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.098247489442835,
            "ttft_change_pct": 0.08658692350260733
          },
          "math": {
            "e2e_change_pct": -6.9398256514371255,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.529614547981787,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.58872456372888,
            "ttft_change_pct": 0.17101320097896444
          },
          "prefill": {
            "e2e_change_pct": -0.5034554609124609,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9391843503744113,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.4966098454788126,
            "ttft_change_pct": -0.5075558604711761
          },
          "prefill2048": {
            "e2e_change_pct": -0.28396274988481407,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1795818311198691,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.27979411216725314,
            "ttft_change_pct": -0.28429869874656566
          },
          "prefill4096": {
            "e2e_change_pct": -0.4041420229656034,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4567664348290368,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.40892935925500584,
            "ttft_change_pct": -0.40250761739988317
          },
          "pve_sim": {
            "e2e_change_pct": -7.26768734305473,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.048961272687347,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.107882631204124,
            "ttft_change_pct": -1.5131991910504294
          },
          "sorting": {
            "e2e_change_pct": -8.0059554929924,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.777284779679358,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.113686955146584,
            "ttft_change_pct": -3.15359337660549
          },
          "time": {
            "e2e_change_pct": -7.793972754116729,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3862288309518207,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.157547087859387,
            "ttft_change_pct": -1.9703685468782428
          },
          "tool-call": {
            "e2e_change_pct": -6.81189581122057,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.3778938889692829,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.502685558877168,
            "ttft_change_pct": -3.922144230261171
          },
          "tool-final": {
            "e2e_change_pct": -5.329584724929603,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.5261580286129117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 10.18755551888486,
            "ttft_change_pct": -0.7877814048893317
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
