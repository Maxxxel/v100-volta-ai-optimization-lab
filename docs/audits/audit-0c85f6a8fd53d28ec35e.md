# Public audit excerpt

Original SHA256: `0c85f6a8fd53d28ec35e25253ed062929d8535db75138eaf218895d43ffffc12`

Original file: `RESULTS.json`; 46564 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6661065505,
              "format_passes": 2,
              "gpu_energy_j": 174.8615666940134,
              "semantic_passes": 2,
              "tokens_per_s": 79.27280183023468,
              "ttft_s": 0.12361609700000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.660163078,
              "format_passes": 0,
              "gpu_energy_j": 444.6893642925637,
              "semantic_passes": 0,
              "tokens_per_s": 79.50809749291807,
              "ttft_s": 0.062766902
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24107042299999998,
              "format_passes": 2,
              "gpu_energy_j": 56.55845166560563,
              "semantic_passes": 2,
              "tokens_per_s": 77.2482916720229,
              "ttft_s": 0.07273083899999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24330127299999998,
              "format_passes": 0,
              "gpu_energy_j": 58.17431400909631,
              "semantic_passes": 0,
              "tokens_per_s": 76.2748269290079,
              "ttft_s": 0.1252015295
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1821430705,
              "format_passes": 2,
              "gpu_energy_j": 41.616337175661414,
              "semantic_passes": 2,
              "tokens_per_s": 77.59491404362133,
              "ttft_s": 0.06615586600000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3580878555,
              "format_passes": 0,
              "gpu_energy_j": 88.60435364943208,
              "semantic_passes": 0,
              "tokens_per_s": 78.77960944635225,
              "ttft_s": 0.0788018135
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.469730066,
              "format_passes": 0,
              "gpu_energy_j": 117.96684663136298,
              "semantic_passes": 2,
              "tokens_per_s": 78.86314244505508,
              "ttft_s": 0.11466188699999999
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.076124808,
              "format_passes": 2,
              "gpu_energy_j": 287.46522813055435,
              "semantic_passes": 2,
              "tokens_per_s": 77.16181220414967,
              "ttft_s": 0.8168530700000001
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2336891295,
              "format_passes": 0,
              "gpu_energy_j": 54.43300450215604,
              "semantic_passes": 0,
              "tokens_per_s": 78.07582674495248,
              "ttft_s": 0.0671549305
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19739721049999998,
              "format_passes": 0,
              "gpu_energy_j": 47.2390048031002,
              "semantic_passes": 0,
              "tokens_per_s": 2572.0623222792883,
              "ttft_s": 0.19725939250000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7130301705,
              "format_passes": 0,
              "gpu_energy_j": 185.50050456893405,
              "semantic_passes": 0,
              "tokens_per_s": 2877.448140981001,
              "ttft_s": 0.712781345
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.406853768,
              "format_passes": 0,
              "gpu_energy_j": 381.2632532517756,
              "semantic_passes": 0,
              "tokens_per_s": 2915.0224304481453,
              "ttft_s": 1.4065123449999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2951825195,
              "format_passes": 2,
              "gpu_energy_j": 73.92353800818992,
              "semantic_passes": 2,
              "tokens_per_s": 78.49746903044094,
              "ttft_s": 0.0786103715
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35618919800000004,
              "format_passes": 2,
              "gpu_energy_j": 85.15731842712921,
              "semantic_passes": 2,
              "tokens_per_s": 78.47603096333607,
              "ttft_s": 0.075750244
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369094809,
              "format_passes": 2,
              "gpu_energy_j": 92.5753623859305,
              "semantic_passes": 2,
              "tokens_per_s": 78.96973099891562,
              "ttft_s": 0.0777866665
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.618763641,
              "format_passes": 0,
              "gpu_energy_j": 156.37700876094925,
              "semantic_passes": 0,
              "tokens_per_s": 79.01681221677262,
              "ttft_s": 0.3173891985
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.559928301,
              "format_passes": 0,
              "gpu_energy_j": 144.16660102061417,
              "semantic_passes": 0,
              "tokens_per_s": 78.69256673850379,
              "ttft_s": 0.255249293
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
              "e2e_s": 0.7316483245000001,
              "format_passes": 2,
              "gpu_energy_j": 180.14836038858394,
              "semantic_passes": 2,
              "tokens_per_s": 71.6931779792163,
              "ttft_s": 0.1318431155
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8319769890000002,
              "format_passes": 0,
              "gpu_energy_j": 458.0981687911142,
              "semantic_passes": 0,
              "tokens_per_s": 72.08881493912827,
              "ttft_s": 0.070035565
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.263491813,
              "format_passes": 2,
              "gpu_energy_j": 60.53497332941759,
              "semantic_passes": 2,
              "tokens_per_s": 70.7363248865166,
              "ttft_s": 0.0796696845
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.261239658,
              "format_passes": 0,
              "gpu_energy_j": 59.91871288451499,
              "semantic_passes": 0,
              "tokens_per_s": 70.18287433815712,
              "ttft_s": 0.1329058505
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.20185019599999998,
              "format_passes": 2,
              "gpu_energy_j": 43.24566726367622,
              "semantic_passes": 2,
              "tokens_per_s": 70.29891975461857,
              "ttft_s": 0.073784772
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.394299872,
              "format_passes": 0,
              "gpu_energy_j": 92.34000534286649,
              "semantic_passes": 0,
              "tokens_per_s": 71.45922372964793,
              "ttft_s": 0.08638715899999999
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5132478625000001,
              "format_passes": 0,
              "gpu_energy_j": 118.31106481316638,
              "semantic_passes": 2,
              "tokens_per_s": 71.66073858695017,
              "ttft_s": 0.122474597
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1123482925000001,
              "format_passes": 2,
              "gpu_energy_j": 289.92344176803454,
              "semantic_passes": 2,
              "tokens_per_s": 70.57491618126559,
              "ttft_s": 0.8288711295
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2582362815,
              "format_passes": 0,
              "gpu_energy_j": 58.1716016628465,
              "semantic_passes": 0,
              "tokens_per_s": 70.84768945771742,
              "ttft_s": 0.0747032
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.205727135,
              "format_passes": 0,
              "gpu_energy_j": 49.637255521193204,
              "semantic_passes": 0,
              "tokens_per_s": 2467.2656269221307,
              "ttft_s": 0.205556996
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7207220355,
              "format_passes": 0,
              "gpu_energy_j": 190.04242605932933,
              "semantic_passes": 0,
              "tokens_per_s": 2846.2708973313183,
              "ttft_s": 0.720498451
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.417054787,
              "format_passes": 0,
              "gpu_energy_j": 383.2844497775588,
              "semantic_passes": 0,
              "tokens_per_s": 2894.008393998838,
              "ttft_s": 1.4167227009999999
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.32559256400000003,
              "format_passes": 2,
              "gpu_energy_j": 75.0100789582576,
              "semantic_passes": 2,
              "tokens_per_s": 71.09340212928534,
              "ttft_s": 0.0864564885
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.391950766,
              "format_passes": 2,
              "gpu_energy_j": 86.30725870171375,
              "semantic_passes": 2,
              "tokens_per_s": 70.81215620304971,
              "ttft_s": 0.0811875685
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.40747382899999995,
              "format_passes": 2,
              "gpu_energy_j": 94.10149747364272,
              "semantic_passes": 2,
              "tokens_per_s": 71.36009356609352,
              "ttft_s": 0.085072305
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6698330735,
              "format_passes": 0,
              "gpu_energy_j": 165.94780414540645,
              "semantic_passes": 0,
              "tokens_per_s": 71.57592484410503,
              "ttft_s": 0.336788425
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.598514344,
              "format_passes": 0,
              "gpu_energy_j": 146.69468880544818,
              "semantic_passes": 0,
              "tokens_per_s": 71.27869941959409,
              "ttft_s": 0.26182647150000005
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
            "e2e_change_pct": 9.839533022277358,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.023416634383591,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.561443112923396,
            "ttft_change_pct": 6.655297084812495
          },
          "decode": {
            "e2e_change_pct": 10.349218897638934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.015319361163926,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.33148042493489,
            "ttft_change_pct": 11.580407457420794
          },
          "energy": {
            "e2e_change_pct": 9.30076353663678,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 7.030817758807495,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -8.429916888200584,
            "ttft_change_pct": 9.540444734866881
          },
          "filtering": {
            "e2e_change_pct": 7.37291045739823,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.9985723168921563,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -7.986845511325525,
            "ttft_change_pct": 6.1535358479786195
          },
          "german": {
            "e2e_change_pct": 10.819585639959861,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.9151213167498256,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.40267075352541,
            "ttft_change_pct": 11.531715116540076
          },
          "ha_sim": {
            "e2e_change_pct": 10.11260670916554,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.216103994409481,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.292234079542371,
            "ttft_change_pct": 9.625851440588985
          },
          "jarvis_memory": {
            "e2e_change_pct": 9.264426454660901,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.29179230574760684,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.132788315052121,
            "ttft_change_pct": 6.813693899874518
          },
          "long_context": {
            "e2e_change_pct": 3.3661043989239525,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8551342551815555,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -8.536471390092416,
            "ttft_change_pct": 1.4712633081001902
          },
          "math": {
            "e2e_change_pct": 10.504190782224644,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.868254278601094,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.25784277744116,
            "ttft_change_pct": 11.240082364466142
          },
          "prefill": {
            "e2e_change_pct": 4.21987954080032,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.076844290198945,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -4.074422864850713,
            "ttft_change_pct": 4.206442793338705
          },
          "prefill2048": {
            "e2e_change_pct": 1.078757297830224,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 2.4484685370262493,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -1.0835032334954087,
            "ttft_change_pct": 1.0826750803922813
          },
          "prefill4096": {
            "e2e_change_pct": 0.7250944790446967,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.53013147963894,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.720887641543011,
            "ttft_change_pct": 0.7259343322720602
          },
          "pve_sim": {
            "e2e_change_pct": 10.302115637304876,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.4698172995281977,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.432236469031052,
            "ttft_change_pct": 9.981020125315144
          },
          "sorting": {
            "e2e_change_pct": 10.040048435157756,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.350371636665093,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.765879678429346,
            "ttft_change_pct": 7.177963017518474
          },
          "time": {
            "e2e_change_pct": 10.398146780763827,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.6485326639608777,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.636144553824789,
            "ttft_change_pct": 9.366179099601846
          },
          "tool-call": {
            "e2e_change_pct": 8.2534637002047,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 6.120334095332325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.41684075061704,
            "ttft_change_pct": 6.11212561476
          },
          "tool-final": {
            "e2e_change_pct": 6.891247134872014,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.7535877012682999,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -9.421305755022647,
            "ttft_change_pct": 2.5767665887325597
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 407717394335877,
          "end_ns": 407719154812368,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 407763648537949,
          "end_ns": 407765108248662,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        }
      ]
    }
  }
}
```
