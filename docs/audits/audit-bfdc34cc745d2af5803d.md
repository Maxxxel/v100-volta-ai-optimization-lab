# Public audit excerpt

Original SHA256: `bfdc34cc745d2af5803dfb53143d6350cb33eb0143d68cf58d40248c96293555`

Original file: `RESULTS.json`; 40686 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
    "qwen35": {
      "arms": {
        "A": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.632562022,
              "format_passes": 2,
              "gpu_energy_j": 148.96148149263493,
              "semantic_passes": 2,
              "tokens_per_s": 84.2102012863642,
              "ttft_s": 0.1338005385
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.567992087,
              "format_passes": 0,
              "gpu_energy_j": 370.69634689269344,
              "semantic_passes": 0,
              "tokens_per_s": 84.18047820827559,
              "ttft_s": 0.0593693225
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2263551765,
              "format_passes": 2,
              "gpu_energy_j": 49.27076660912483,
              "semantic_passes": 2,
              "tokens_per_s": 82.88768288407917,
              "ttft_s": 0.0694293565
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.245352474,
              "format_passes": 0,
              "gpu_energy_j": 56.69733164986074,
              "semantic_passes": 0,
              "tokens_per_s": 82.11942252227506,
              "ttft_s": 0.1357020205
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.17187683199999998,
              "format_passes": 2,
              "gpu_energy_j": 34.64713701191033,
              "semantic_passes": 2,
              "tokens_per_s": 82.0827308314685,
              "ttft_s": 0.062195005
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.343134629,
              "format_passes": 0,
              "gpu_energy_j": 74.78270641892951,
              "semantic_passes": 0,
              "tokens_per_s": 83.25323879576048,
              "ttft_s": 0.07876930400000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.44465754,
              "format_passes": 0,
              "gpu_energy_j": 96.06150844458193,
              "semantic_passes": 2,
              "tokens_per_s": 83.43541869165944,
              "ttft_s": 0.1090265545
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.055224242,
              "format_passes": 2,
              "gpu_energy_j": 276.8710582319502,
              "semantic_passes": 2,
              "tokens_per_s": 81.92739288648085,
              "ttft_s": 0.872093185
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.16213439950000003,
              "format_passes": 0,
              "gpu_energy_j": 34.32384091953853,
              "semantic_passes": 0,
              "tokens_per_s": 81.97484044133344,
              "ttft_s": 0.0644725355
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.207394373,
              "format_passes": 0,
              "gpu_energy_j": 50.89065983674851,
              "semantic_passes": 0,
              "tokens_per_s": 2446.7099936753903,
              "ttft_s": 0.2072564065
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.75511857,
              "format_passes": 0,
              "gpu_energy_j": 202.02033376165053,
              "semantic_passes": 0,
              "tokens_per_s": 2716.8992389919968,
              "ttft_s": 0.75488022
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.500408569,
              "format_passes": 0,
              "gpu_energy_j": 405.2517631910282,
              "semantic_passes": 0,
              "tokens_per_s": 2733.2941948642,
              "ttft_s": 1.5000437935000002
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.283014898,
              "format_passes": 2,
              "gpu_energy_j": 59.98693293992849,
              "semantic_passes": 2,
              "tokens_per_s": 83.05229408134521,
              "ttft_s": 0.078283755
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.33524609699999997,
              "format_passes": 2,
              "gpu_energy_j": 76.20440863441476,
              "semantic_passes": 2,
              "tokens_per_s": 83.62571526306586,
              "ttft_s": 0.072113092
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3563061385,
              "format_passes": 0,
              "gpu_energy_j": 77.76722984490132,
              "semantic_passes": 0,
              "tokens_per_s": 83.02762790740775,
              "ttft_s": 0.079251294
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6020399855,
              "format_passes": 0,
              "gpu_energy_j": 143.84102473651927,
              "semantic_passes": 0,
              "tokens_per_s": 83.89443065219281,
              "ttft_s": 0.31839018249999995
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.562617692,
              "format_passes": 0,
              "gpu_energy_j": 132.7489108191093,
              "semantic_passes": 0,
              "tokens_per_s": 83.60956986934177,
              "ttft_s": 0.275534881
            }
          }
        },
        "B": {
          "format_passes": 12,
          "quality_attempts": 24,
          "quality_passes": 14,
          "tasks": {
            "code": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.576685733,
              "format_passes": 2,
              "gpu_energy_j": 142.8924144243634,
              "semantic_passes": 2,
              "tokens_per_s": 94.62735230298648,
              "ttft_s": 0.132784778
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.398053688,
              "format_passes": 0,
              "gpu_energy_j": 358.1456039410525,
              "semantic_passes": 0,
              "tokens_per_s": 94.79398238211678,
              "ttft_s": 0.058379997
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2081836735,
              "format_passes": 2,
              "gpu_energy_j": 46.70731452860495,
              "semantic_passes": 2,
              "tokens_per_s": 92.9720673885225,
              "ttft_s": 0.0683270775
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23178350050000002,
              "format_passes": 0,
              "gpu_energy_j": 57.09100260443226,
              "semantic_passes": 0,
              "tokens_per_s": 92.0848405982211,
              "ttft_s": 0.134026057
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.15911295749999999,
              "format_passes": 2,
              "gpu_energy_j": 31.298199685233747,
              "semantic_passes": 2,
              "tokens_per_s": 91.89216714052486,
              "ttft_s": 0.061175229
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3147912905,
              "format_passes": 0,
              "gpu_energy_j": 72.16739036641926,
              "semantic_passes": 0,
              "tokens_per_s": 93.04083401575694,
              "ttft_s": 0.078245396
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4046968305,
              "format_passes": 0,
              "gpu_energy_j": 92.76026252163652,
              "semantic_passes": 2,
              "tokens_per_s": 94.1945198454343,
              "ttft_s": 0.1073925915
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.034285976,
              "format_passes": 2,
              "gpu_energy_j": 273.3143678368606,
              "semantic_passes": 2,
              "tokens_per_s": 92.60691173773449,
              "ttft_s": 0.872282824
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1503382235,
              "format_passes": 0,
              "gpu_energy_j": 29.76239617959649,
              "semantic_passes": 0,
              "tokens_per_s": 91.73965902710046,
              "ttft_s": 0.063090457
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.206130092,
              "format_passes": 0,
              "gpu_energy_j": 50.41416013408619,
              "semantic_passes": 0,
              "tokens_per_s": 2463.4693023827117,
              "ttft_s": 0.205961571
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7551354025,
              "format_passes": 0,
              "gpu_energy_j": 199.6872273050661,
              "semantic_passes": 0,
              "tokens_per_s": 2716.742636543694,
              "ttft_s": 0.7549047600000001
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4955842995,
              "format_passes": 0,
              "gpu_energy_j": 404.7345551440127,
              "semantic_passes": 0,
              "tokens_per_s": 2742.0867975069536,
              "ttft_s": 1.495262541
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.25941860299999997,
              "format_passes": 2,
              "gpu_energy_j": 56.245297025823646,
              "semantic_passes": 2,
              "tokens_per_s": 93.21578995630325,
              "ttft_s": 0.07700873250000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3053490875,
              "format_passes": 2,
              "gpu_energy_j": 72.4988842558119,
              "semantic_passes": 2,
              "tokens_per_s": 93.68488420887473,
              "ttft_s": 0.07048476449999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3196203225,
              "format_passes": 0,
              "gpu_energy_j": 75.75366596180731,
              "semantic_passes": 0,
              "tokens_per_s": 94.04608225678172,
              "ttft_s": 0.0750146795
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.557245087,
              "format_passes": 0,
              "gpu_energy_j": 139.1014295711465,
              "semantic_passes": 0,
              "tokens_per_s": 94.36417431993641,
              "ttft_s": 0.305396447
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.529147283,
              "format_passes": 0,
              "gpu_energy_j": 133.15603390200448,
              "semantic_passes": 0,
              "tokens_per_s": 94.02419264306104,
              "ttft_s": 0.2737559975
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
            "e2e_change_pct": -8.833329706284509,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.074252623871488,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.370414578630262,
            "ttft_change_pct": -0.7591602480733095
          },
          "decode": {
            "e2e_change_pct": -10.837962793877276,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.3857207002026435,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.608035021589847,
            "ttft_change_pct": -1.666391763187125
          },
          "energy": {
            "e2e_change_pct": -8.027871631201688,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.20278505276014,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.166324541303242,
            "ttft_change_pct": -1.5876266979372056
          },
          "filtering": {
            "e2e_change_pct": -5.530400113267242,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6943377106398474,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.135275395102664,
            "ttft_change_pct": -1.2350320900343492
          },
          "german": {
            "e2e_change_pct": -7.426175099620169,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -9.665841438862177,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.950670024852128,
            "ttft_change_pct": -1.6396429263089485
          },
          "ha_sim": {
            "e2e_change_pct": -8.260121860215985,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.4972203838937843,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.756413758277562,
            "ttft_change_pct": -0.6651169597741036
          },
          "jarvis_memory": {
            "e2e_change_pct": -8.986850757101749,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.436595964813427,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.895124543613502,
            "ttft_change_pct": -1.49868351567507
          },
          "long_context": {
            "e2e_change_pct": -1.9842480078276936,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.2846017268117516,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 13.035345657894016,
            "ttft_change_pct": 0.02174526796698828
          },
          "math": {
            "e2e_change_pct": -7.275554130633466,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -13.289435616004974,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 11.911970225492974,
            "ttft_change_pct": -2.1436701523860457
          },
          "prefill": {
            "e2e_change_pct": -0.6096023637054082,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9363205432802002,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.684973239601061,
            "ttft_change_pct": -0.6247505309323165
          },
          "prefill2048": {
            "e2e_change_pct": 0.0022291201234647673,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1548869428842257,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.005764013845455107,
            "ttft_change_pct": 0.0032508468694736337
          },
          "prefill4096": {
            "e2e_change_pct": -0.32153038843382165,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.12762635329280902,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.32168519068582757,
            "ttft_change_pct": -0.31874086081474795
          },
          "pve_sim": {
            "e2e_change_pct": -8.337474516977561,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.2374182688282325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.237465547915448,
            "ttft_change_pct": -1.6287191384725785
          },
          "sorting": {
            "e2e_change_pct": -8.917929177263462,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.862611553591146,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.028798694474796,
            "ttft_change_pct": -2.258019251206167
          },
          "time": {
            "e2e_change_pct": -10.296150426833018,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.5892189899394014,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 13.270828791666457,
            "ttft_change_pct": -5.3457985178134715
          },
          "tool-call": {
            "e2e_change_pct": -7.440518832448895,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.29502322029096,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.479664724287565,
            "ttft_change_pct": -4.081072914363471
          },
          "tool-final": {
            "e2e_change_pct": -5.949050212235408,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.30668657119901077,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 12.45625684953815,
            "ttft_change_pct": -0.6456109997920678
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
