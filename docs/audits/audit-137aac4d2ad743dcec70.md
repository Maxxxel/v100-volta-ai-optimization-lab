# Public audit excerpt

Original SHA256: `137aac4d2ad743dcec701082fe1055333c383e66cb5b3503a2d9d74808d8aade`

Original file: `RESULTS.json`; 47186 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6673336489999999,
              "format_passes": 2,
              "gpu_energy_j": 177.60583434115375,
              "semantic_passes": 2,
              "tokens_per_s": 79.1251090275172,
              "ttft_s": 0.123826041
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6581079615,
              "format_passes": 0,
              "gpu_energy_j": 457.76628776053076,
              "semantic_passes": 0,
              "tokens_per_s": 79.63950306361667,
              "ttft_s": 0.0630160545
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2386145245,
              "format_passes": 2,
              "gpu_energy_j": 57.777106813404416,
              "semantic_passes": 2,
              "tokens_per_s": 77.9557783912779,
              "ttft_s": 0.071782866
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24198351299999998,
              "format_passes": 0,
              "gpu_energy_j": 60.71582553578792,
              "semantic_passes": 0,
              "tokens_per_s": 77.57951903003988,
              "ttft_s": 0.1259449915
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.182328038,
              "format_passes": 2,
              "gpu_energy_j": 37.01281568519417,
              "semantic_passes": 2,
              "tokens_per_s": 77.40924583774176,
              "ttft_s": 0.06601727900000001
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35846760850000003,
              "format_passes": 0,
              "gpu_energy_j": 90.43221387705246,
              "semantic_passes": 0,
              "tokens_per_s": 78.69064048262275,
              "ttft_s": 0.078844533
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4691708465,
              "format_passes": 0,
              "gpu_energy_j": 116.88106562066628,
              "semantic_passes": 2,
              "tokens_per_s": 79.05443323652162,
              "ttft_s": 0.1149728295
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.200550968,
              "format_passes": 0,
              "gpu_energy_j": 48.890117475926274,
              "semantic_passes": 0,
              "tokens_per_s": 2564.331550536474,
              "ttft_s": 0.2003677225
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0821716315,
              "format_passes": 2,
              "gpu_energy_j": 287.5410531734266,
              "semantic_passes": 2,
              "tokens_per_s": 77.92501725960686,
              "ttft_s": 0.8255050214999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23414659599999998,
              "format_passes": 0,
              "gpu_energy_j": 53.61132861122475,
              "semantic_passes": 0,
              "tokens_per_s": 78.29293714635409,
              "ttft_s": 0.06803967250000001
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19905804,
              "format_passes": 0,
              "gpu_energy_j": 49.214511475852994,
              "semantic_passes": 0,
              "tokens_per_s": 2550.8409002142953,
              "ttft_s": 0.198900274
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7181054255,
              "format_passes": 0,
              "gpu_energy_j": 189.23911375448722,
              "semantic_passes": 0,
              "tokens_per_s": 2857.0677991115763,
              "ttft_s": 0.7178837645
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4151536895,
              "format_passes": 0,
              "gpu_energy_j": 383.17603224789605,
              "semantic_passes": 0,
              "tokens_per_s": 2898.1122819959173,
              "ttft_s": 1.414857719
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2956007805,
              "format_passes": 2,
              "gpu_energy_j": 75.68783619069507,
              "semantic_passes": 2,
              "tokens_per_s": 78.70735082866676,
              "ttft_s": 0.07955688250000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3597052725,
              "format_passes": 2,
              "gpu_energy_j": 90.05296993093447,
              "semantic_passes": 2,
              "tokens_per_s": 77.17367320570418,
              "ttft_s": 0.07451237150000001
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.37203069450000004,
              "format_passes": 2,
              "gpu_energy_j": 90.54376856379359,
              "semantic_passes": 2,
              "tokens_per_s": 78.41477602275977,
              "ttft_s": 0.07866644149999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.619877529,
              "format_passes": 0,
              "gpu_energy_j": 163.28870477764357,
              "semantic_passes": 0,
              "tokens_per_s": 78.94210699404589,
              "ttft_s": 0.31880884649999996
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.56051615,
              "format_passes": 0,
              "gpu_energy_j": 147.78718446416477,
              "semantic_passes": 0,
              "tokens_per_s": 78.77285063733791,
              "ttft_s": 0.25556836549999995
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
              "e2e_s": 0.6666902004999999,
              "format_passes": 2,
              "gpu_energy_j": 174.77356405902628,
              "semantic_passes": 2,
              "tokens_per_s": 79.24208793883325,
              "ttft_s": 0.124007411
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.658730501,
              "format_passes": 0,
              "gpu_energy_j": 461.0585407044482,
              "semantic_passes": 0,
              "tokens_per_s": 79.58545380713454,
              "ttft_s": 0.06282236599999999
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2407482385,
              "format_passes": 2,
              "gpu_energy_j": 58.64275334433044,
              "semantic_passes": 2,
              "tokens_per_s": 77.5517319420034,
              "ttft_s": 0.0731228675
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.24181184249999998,
              "format_passes": 0,
              "gpu_energy_j": 57.04309739146997,
              "semantic_passes": 0,
              "tokens_per_s": 77.48333696394317,
              "ttft_s": 0.12554800300000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1824126435,
              "format_passes": 2,
              "gpu_energy_j": 42.501342373535145,
              "semantic_passes": 2,
              "tokens_per_s": 77.29469277615482,
              "ttft_s": 0.065976953
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3580609155,
              "format_passes": 0,
              "gpu_energy_j": 88.98281795363289,
              "semantic_passes": 0,
              "tokens_per_s": 78.81995258358637,
              "ttft_s": 0.0789092985
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4694075635,
              "format_passes": 0,
              "gpu_energy_j": 116.0387076191428,
              "semantic_passes": 2,
              "tokens_per_s": 79.08178831143043,
              "ttft_s": 0.11529932849999999
            },
            "length-prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.12249731550000001,
              "format_passes": 0,
              "gpu_energy_j": 27.71787158783342,
              "semantic_passes": 0,
              "tokens_per_s": 1051.659983524486,
              "ttft_s": 0.1223280115
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0815682845,
              "format_passes": 2,
              "gpu_energy_j": 288.67424930680676,
              "semantic_passes": 2,
              "tokens_per_s": 78.04166307707428,
              "ttft_s": 0.8252500819999999
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23357782500000002,
              "format_passes": 0,
              "gpu_energy_j": 56.07092693770345,
              "semantic_passes": 0,
              "tokens_per_s": 78.21598636400361,
              "ttft_s": 0.067328525
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1997900275,
              "format_passes": 0,
              "gpu_energy_j": 48.88830328304057,
              "semantic_passes": 0,
              "tokens_per_s": 2541.476126239968,
              "ttft_s": 0.1996559315
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7191593759999999,
              "format_passes": 0,
              "gpu_energy_j": 191.16863222250043,
              "semantic_passes": 0,
              "tokens_per_s": 2852.681783847059,
              "ttft_s": 0.7188966274999999
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4205098395,
              "format_passes": 0,
              "gpu_energy_j": 381.58931003055415,
              "semantic_passes": 0,
              "tokens_per_s": 2886.9315270411025,
              "ttft_s": 1.4201704755
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2952123275,
              "format_passes": 2,
              "gpu_energy_j": 72.35781427399749,
              "semantic_passes": 2,
              "tokens_per_s": 78.63435350243566,
              "ttft_s": 0.0789368785
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.353346082,
              "format_passes": 2,
              "gpu_energy_j": 86.7200075539988,
              "semantic_passes": 2,
              "tokens_per_s": 78.79359843513703,
              "ttft_s": 0.0741145815
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369777365,
              "format_passes": 2,
              "gpu_energy_j": 94.66184604360325,
              "semantic_passes": 2,
              "tokens_per_s": 78.81835931463205,
              "ttft_s": 0.0779106225
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6201162920000001,
              "format_passes": 0,
              "gpu_energy_j": 161.00779659341794,
              "semantic_passes": 0,
              "tokens_per_s": 78.96961210415576,
              "ttft_s": 0.318783288
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561035283,
              "format_passes": 0,
              "gpu_energy_j": 146.61971250062987,
              "semantic_passes": 0,
              "tokens_per_s": 78.84090978885746,
              "ttft_s": 0.256389752
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
            "e2e_change_pct": -0.09642080853621282,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.5946943931397617,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.14784044250146788,
            "ttft_change_pct": 0.14647161334988557
          },
          "decode": {
            "e2e_change_pct": 0.03754517283884873,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.7191995199173906,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.0678673954544351,
            "ttft_change_pct": -0.30736373696644836
          },
          "energy": {
            "e2e_change_pct": 0.8942096062555471,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.49825177941445,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.5183021164210544,
            "ttft_change_pct": 1.8667428241162742
          },
          "filtering": {
            "e2e_change_pct": -0.07094305635607645,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.049045882037996,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.12397868316179617,
            "ttft_change_pct": -0.3152078500874511
          },
          "german": {
            "e2e_change_pct": 0.04640290156581184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 14.82871969272117,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.1479836941275181,
            "ttft_change_pct": -0.06108400802160574
          },
          "ha_sim": {
            "e2e_change_pct": -0.11345320758597843,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6027429400214732,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.16432970956967718,
            "ttft_change_pct": 0.08214329838189816
          },
          "jarvis_memory": {
            "e2e_change_pct": 0.05045432847456954,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7206967159739341,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.03460283476699466,
            "ttft_change_pct": 0.28397926833660936
          },
          "length-prefill": {
            "e2e_change_pct": -38.91960895446787,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -43.305778306869826,
            "same_token_counts": false,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": false,
            "ttft_change_pct": -38.94824477031224
          },
          "long_context": {
            "e2e_change_pct": -0.055753355792897974,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3940989020084995,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.14968981922558466,
            "ttft_change_pct": -0.030882852721692
          },
          "math": {
            "e2e_change_pct": -0.2429123505173547,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.587833187860468,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09828572685507408,
            "ttft_change_pct": -1.0451953601040787
          },
          "prefill": {
            "e2e_change_pct": 0.3677256643338733,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6628292815066938,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.36712497331921057,
            "ttft_change_pct": 0.37991777728774156
          },
          "prefill2048": {
            "e2e_change_pct": 0.1467682129355996,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.019619268834937,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.15351456713352807,
            "ttft_change_pct": 0.1410901109743623
          },
          "prefill4096": {
            "e2e_change_pct": 0.37848539276976734,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4140974601238523,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.3857944022484405,
            "ttft_change_pct": 0.3754975803330174
          },
          "pve_sim": {
            "e2e_change_pct": -0.13141135802922088,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -4.399679108684785,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": -0.09274524610796142,
            "ttft_change_pct": -0.7793216382002033
          },
          "sorting": {
            "e2e_change_pct": -1.767889154307578,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -3.7011132220201803,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 2.0990645671548958,
            "ttft_change_pct": -0.5338576561074948
          },
          "time": {
            "e2e_change_pct": -0.6056837603220955,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 4.548162225993746,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.5146776058572611,
            "ttft_change_pct": -0.9607896144634864
          },
          "tool-call": {
            "e2e_change_pct": 0.038517769854506945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3968560699477828,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.034842128183809606,
            "ttft_change_pct": -0.008016872894389682
          },
          "tool-final": {
            "e2e_change_pct": 0.0926169567103674,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.789968337084046,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "throughput_comparison_eligible": true,
            "tokens_per_s_change_pct": 0.08639924919422448,
            "ttft_change_pct": 0.3213959984417869
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
