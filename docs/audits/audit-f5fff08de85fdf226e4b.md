# Public audit excerpt

Original SHA256: `f5fff08de85fdf226e4b12c0114b6ded1fb473d4a1788e393d5cfd06f129bec2`

Original file: `RESULTS.json`; 39773 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

```json
{}
```

## Selected aggregate measurements

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
              "e2e_s": 1.7922911400000001,
              "format_passes": 2,
              "gpu_energy_j": 478.92074054354873,
              "semantic_passes": 2,
              "tokens_per_s": 35.36757132291166,
              "ttft_s": 0.543778844
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7766730930000003,
              "format_passes": 0,
              "gpu_energy_j": 1067.7051396160887,
              "semantic_passes": 0,
              "tokens_per_s": 35.484022057554604,
              "ttft_s": 0.196765243
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.598708467,
              "format_passes": 2,
              "gpu_energy_j": 146.90335445480815,
              "semantic_passes": 2,
              "tokens_per_s": 34.81392330299437,
              "ttft_s": 0.2225416905
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9470367585,
              "format_passes": 0,
              "gpu_energy_j": 245.728069803974,
              "semantic_passes": 0,
              "tokens_per_s": 34.96904507541673,
              "ttft_s": 0.542840067
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.496979339,
              "format_passes": 2,
              "gpu_energy_j": 108.88987389347442,
              "semantic_passes": 2,
              "tokens_per_s": 33.64426299379362,
              "ttft_s": 0.226534581
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0224333410000002,
              "format_passes": 0,
              "gpu_energy_j": 265.15951336247,
              "semantic_passes": 0,
              "tokens_per_s": 35.1190287405994,
              "ttft_s": 0.24936750800000002
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1725717,
              "format_passes": 0,
              "gpu_energy_j": 296.14340498052815,
              "semantic_passes": 2,
              "tokens_per_s": 35.20209988160722,
              "ttft_s": 0.373069699
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8045162205,
              "format_passes": 2,
              "gpu_energy_j": 1018.1839840878208,
              "semantic_passes": 2,
              "tokens_per_s": 34.11051248909871,
              "ttft_s": 3.2166526515
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5900215655000001,
              "format_passes": 2,
              "gpu_energy_j": 146.6219080703578,
              "semantic_passes": 2,
              "tokens_per_s": 34.88372109550336,
              "ttft_s": 0.2160645035
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7231957965,
              "format_passes": 0,
              "gpu_energy_j": 186.7999149817722,
              "semantic_passes": 0,
              "tokens_per_s": 699.3724120434406,
              "ttft_s": 0.7230651115
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7501434335,
              "format_passes": 0,
              "gpu_energy_j": 735.9099086140882,
              "semantic_passes": 0,
              "tokens_per_s": 745.0506468992567,
              "ttft_s": 2.749918624
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4449742924999995,
              "format_passes": 0,
              "gpu_energy_j": 1474.7840475196613,
              "semantic_passes": 0,
              "tokens_per_s": 752.5011796535046,
              "ttft_s": 5.4446133785
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8709152855,
              "format_passes": 0,
              "gpu_energy_j": 230.3169302604856,
              "semantic_passes": 2,
              "tokens_per_s": 35.09465560508781,
              "ttft_s": 0.2407876675
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0001506880000002,
              "format_passes": 0,
              "gpu_energy_j": 265.56750169308236,
              "semantic_passes": 2,
              "tokens_per_s": 35.00360111369558,
              "ttft_s": 0.22660688099999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.028351378,
              "format_passes": 0,
              "gpu_energy_j": 272.6703234291539,
              "semantic_passes": 2,
              "tokens_per_s": 35.25038744030543,
              "ttft_s": 0.231688416
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7054233760000002,
              "format_passes": 0,
              "gpu_energy_j": 459.47504760785586,
              "semantic_passes": 0,
              "tokens_per_s": 35.07119568824197,
              "ttft_s": 1.0280461975
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.777075363,
              "format_passes": 0,
              "gpu_energy_j": 465.3052760530079,
              "semantic_passes": 0,
              "tokens_per_s": 35.161332621348606,
              "ttft_s": 1.094302787
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
              "e2e_s": 1.762160407,
              "format_passes": 2,
              "gpu_energy_j": 485.4273013734329,
              "semantic_passes": 2,
              "tokens_per_s": 35.45237848409839,
              "ttft_s": 0.5210069495
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.783505497,
              "format_passes": 0,
              "gpu_energy_j": 1067.2653451660685,
              "semantic_passes": 0,
              "tokens_per_s": 35.39837829634755,
              "ttft_s": 0.195971046
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5827409514999999,
              "format_passes": 2,
              "gpu_energy_j": 146.24489758021178,
              "semantic_passes": 2,
              "tokens_per_s": 34.982300676994505,
              "ttft_s": 0.21111568800000002
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9256472714999999,
              "format_passes": 0,
              "gpu_energy_j": 242.32905732464326,
              "semantic_passes": 0,
              "tokens_per_s": 34.91193664795111,
              "ttft_s": 0.524584473
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.467571682,
              "format_passes": 2,
              "gpu_energy_j": 110.0966028494549,
              "semantic_passes": 2,
              "tokens_per_s": 34.152253322279876,
              "ttft_s": 0.203992768
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9882025745,
              "format_passes": 0,
              "gpu_energy_j": 267.44536070906247,
              "semantic_passes": 0,
              "tokens_per_s": 35.333535608596506,
              "ttft_s": 0.2240035625
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1463540115000002,
              "format_passes": 0,
              "gpu_energy_j": 295.89464930462077,
              "semantic_passes": 2,
              "tokens_per_s": 35.31018618861266,
              "ttft_s": 0.3533289125
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8055501865,
              "format_passes": 2,
              "gpu_energy_j": 1019.6989519075726,
              "semantic_passes": 2,
              "tokens_per_s": 34.30032425630267,
              "ttft_s": 3.2224053904999996
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.575724136,
              "format_passes": 2,
              "gpu_energy_j": 142.81982034154237,
              "semantic_passes": 2,
              "tokens_per_s": 35.032458408275716,
              "ttft_s": 0.2045894565
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7268331775,
              "format_passes": 0,
              "gpu_energy_j": 187.72616510779852,
              "semantic_passes": 0,
              "tokens_per_s": 695.7389619862108,
              "ttft_s": 0.7267000245
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7491148819999998,
              "format_passes": 0,
              "gpu_energy_j": 732.4112930439927,
              "semantic_passes": 0,
              "tokens_per_s": 745.2987486444686,
              "ttft_s": 2.7488963525
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.463295263,
              "format_passes": 0,
              "gpu_energy_j": 1478.153401455556,
              "semantic_passes": 0,
              "tokens_per_s": 749.9740322439947,
              "ttft_s": 5.4629465905
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8475335390000001,
              "format_passes": 0,
              "gpu_energy_j": 227.1333514681562,
              "semantic_passes": 2,
              "tokens_per_s": 35.269919087599256,
              "ttft_s": 0.22371455950000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9876594495,
              "format_passes": 0,
              "gpu_energy_j": 262.5631781781252,
              "semantic_passes": 2,
              "tokens_per_s": 35.11601623042362,
              "ttft_s": 0.2187220125
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015385166,
              "format_passes": 0,
              "gpu_energy_j": 271.3180505995821,
              "semantic_passes": 2,
              "tokens_per_s": 35.2570512550644,
              "ttft_s": 0.2211809405
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.70576259,
              "format_passes": 0,
              "gpu_energy_j": 464.0768843279161,
              "semantic_passes": 0,
              "tokens_per_s": 35.08985876140167,
              "ttft_s": 1.0283196905
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7773483525,
              "format_passes": 0,
              "gpu_energy_j": 467.57788044827805,
              "semantic_passes": 0,
              "tokens_per_s": 35.090849783703604,
              "ttft_s": 1.093400839
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
            "e2e_change_pct": -1.6811293839236408,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.3585882337231014,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.23978791309255953,
            "ttft_change_pct": -4.187712477464444
          },
          "decode": {
            "e2e_change_pct": 0.1809106542121297,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.04119062779619487,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2413586629727016,
            "ttft_change_pct": -0.40362667099697047
          },
          "energy": {
            "e2e_change_pct": -2.6669934333833467,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.44822453308847043,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.48364952302188957,
            "ttft_change_pct": -5.13431998935947
          },
          "filtering": {
            "e2e_change_pct": -2.2585698821108724,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.383241435153193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.16331137250804595,
            "ttft_change_pct": -3.362978363201774
          },
          "german": {
            "e2e_change_pct": -5.917279591375535,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1082104449501085,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.5098869265763648,
            "ttft_change_pct": -9.950716089566924
          },
          "ha_sim": {
            "e2e_change_pct": -3.3479704864202153,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8620649953704262,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6107995456865467,
            "ttft_change_pct": -10.171311292087026
          },
          "jarvis_memory": {
            "e2e_change_pct": -2.2359134626905863,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.08399838447313845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3070450551784232,
            "ttft_change_pct": -5.291447296018537
          },
          "long_context": {
            "e2e_change_pct": 0.02717733188857263,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.14879116578414564,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5564612002373792,
            "ttft_change_pct": 0.17884240616770075
          },
          "math": {
            "e2e_change_pct": -2.4232045633593047,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.593123891820426,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4263802945939865,
            "ttft_change_pct": -5.310935768771485
          },
          "prefill": {
            "e2e_change_pct": 0.5029593669658494,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4958514708728323,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.5195300807782077,
            "ttft_change_pct": 0.5027089458734091
          },
          "prefill2048": {
            "e2e_change_pct": -0.03739992203574127,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4754135702132678,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03329998386611965,
            "ttft_change_pct": -0.03717460913491566
          },
          "prefill4096": {
            "e2e_change_pct": 0.33647487601982107,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.22846422441042957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.33583301632478246,
            "ttft_change_pct": 0.3367220172582952
          },
          "pve_sim": {
            "e2e_change_pct": -2.6847325898725294,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3822599965746418,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.4994022009608745,
            "ttft_change_pct": -7.090524268648424
          },
          "sorting": {
            "e2e_change_pct": -1.2489356503847415,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1312843234972503,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.32115300469486296,
            "ttft_change_pct": -3.4795362193789536
          },
          "time": {
            "e2e_change_pct": -1.2608736933106934,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4959369294631588,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.01890423125205931,
            "ttft_change_pct": -4.535175163871807
          },
          "tool-call": {
            "e2e_change_pct": 0.019890310217007823,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.001542247836662,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05321481858104882,
            "ttft_change_pct": 0.02660318190614852
          },
          "tool-final": {
            "e2e_change_pct": 0.015361728921781115,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.48841148214515684,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20045553564204122,
            "ttft_change_pct": -0.08242216054960005
          }
        }
      },
      "complete": true
    }
  }
}
```
