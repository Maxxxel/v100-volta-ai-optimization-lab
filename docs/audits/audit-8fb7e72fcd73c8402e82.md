# Public audit excerpt

Original SHA256: `8fb7e72fcd73c8402e827d7131d5591e9c3b1a6bca79b27cfdf43b46bd59c44b`

Original file: `RESULTS.json`; 43154 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.6706619460000001,
              "format_passes": 2,
              "gpu_energy_j": 178.88756439264802,
              "semantic_passes": 2,
              "tokens_per_s": 78.62609672325326,
              "ttft_s": 0.123732078
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6720365240000001,
              "format_passes": 0,
              "gpu_energy_j": 461.8688964629017,
              "semantic_passes": 0,
              "tokens_per_s": 78.95635941836993,
              "ttft_s": 0.0634194805
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23963458050000003,
              "format_passes": 2,
              "gpu_energy_j": 59.239749600800266,
              "semantic_passes": 2,
              "tokens_per_s": 77.56407945068455,
              "ttft_s": 0.07197719799999999
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.245724486,
              "format_passes": 0,
              "gpu_energy_j": 59.83050446296181,
              "semantic_passes": 0,
              "tokens_per_s": 76.0385059010155,
              "ttft_s": 0.1272616935
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18318582700000002,
              "format_passes": 2,
              "gpu_energy_j": 41.0588249889744,
              "semantic_passes": 2,
              "tokens_per_s": 76.93067861687149,
              "ttft_s": 0.06614772799999999
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3602688975,
              "format_passes": 0,
              "gpu_energy_j": 91.94348716724718,
              "semantic_passes": 0,
              "tokens_per_s": 78.15901043837593,
              "ttft_s": 0.0787752685
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.473877936,
              "format_passes": 0,
              "gpu_energy_j": 122.92383909986958,
              "semantic_passes": 2,
              "tokens_per_s": 78.27396028638665,
              "ttft_s": 0.1161451245
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0830543415,
              "format_passes": 2,
              "gpu_energy_j": 290.3793142970077,
              "semantic_passes": 2,
              "tokens_per_s": 77.29214552150458,
              "ttft_s": 0.824267561
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.23535841000000002,
              "format_passes": 0,
              "gpu_energy_j": 58.268241781193275,
              "semantic_passes": 0,
              "tokens_per_s": 77.53856823089046,
              "ttft_s": 0.067649006
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.19901504250000002,
              "format_passes": 0,
              "gpu_energy_j": 48.39237346652847,
              "semantic_passes": 0,
              "tokens_per_s": 2552.013269967493,
              "ttft_s": 0.19884866
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.718960103,
              "format_passes": 0,
              "gpu_energy_j": 188.97703044483296,
              "semantic_passes": 0,
              "tokens_per_s": 2853.3753484311364,
              "ttft_s": 0.7187722755
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.421183653,
              "format_passes": 0,
              "gpu_energy_j": 381.22191382146025,
              "semantic_passes": 0,
              "tokens_per_s": 2885.545738361775,
              "ttft_s": 1.420855874
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29710088300000004,
              "format_passes": 2,
              "gpu_energy_j": 75.97069370130305,
              "semantic_passes": 2,
              "tokens_per_s": 77.98976350656385,
              "ttft_s": 0.07906592800000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.355468287,
              "format_passes": 2,
              "gpu_energy_j": 86.28089064639826,
              "semantic_passes": 2,
              "tokens_per_s": 78.19192363022046,
              "ttft_s": 0.0740449825
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3721869765,
              "format_passes": 2,
              "gpu_energy_j": 95.29677648397913,
              "semantic_passes": 2,
              "tokens_per_s": 78.18648342785781,
              "ttft_s": 0.0780258275
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6234221394999999,
              "format_passes": 0,
              "gpu_energy_j": 162.5894711904472,
              "semantic_passes": 0,
              "tokens_per_s": 78.34870143730782,
              "ttft_s": 0.3199390705
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5631492115,
              "format_passes": 0,
              "gpu_energy_j": 145.67956141172084,
              "semantic_passes": 0,
              "tokens_per_s": 78.13263133541665,
              "ttft_s": 0.255888801
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
              "e2e_s": 0.6663954034999999,
              "format_passes": 2,
              "gpu_energy_j": 178.4837984083722,
              "semantic_passes": 2,
              "tokens_per_s": 79.28108896654612,
              "ttft_s": 0.1239945465
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6577630145,
              "format_passes": 0,
              "gpu_energy_j": 462.0556920584303,
              "semantic_passes": 0,
              "tokens_per_s": 79.63548316423058,
              "ttft_s": 0.0628422495
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2385196,
              "format_passes": 2,
              "gpu_energy_j": 55.94021523095968,
              "semantic_passes": 2,
              "tokens_per_s": 78.07345663850677,
              "ttft_s": 0.0719848385
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2416604155,
              "format_passes": 0,
              "gpu_energy_j": 58.35570529974231,
              "semantic_passes": 0,
              "tokens_per_s": 77.43907988344571,
              "ttft_s": 0.125445083
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1820122565,
              "format_passes": 2,
              "gpu_energy_j": 41.429148423882765,
              "semantic_passes": 2,
              "tokens_per_s": 77.63194618688857,
              "ttft_s": 0.066077575
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3588255685,
              "format_passes": 0,
              "gpu_energy_j": 90.87812553277439,
              "semantic_passes": 0,
              "tokens_per_s": 78.85336389376522,
              "ttft_s": 0.07980487850000001
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468718187,
              "format_passes": 0,
              "gpu_energy_j": 120.32171809798903,
              "semantic_passes": 2,
              "tokens_per_s": 79.10803093271488,
              "ttft_s": 0.114733104
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.080253732,
              "format_passes": 2,
              "gpu_energy_j": 287.96110322852695,
              "semantic_passes": 2,
              "tokens_per_s": 77.99460733298645,
              "ttft_s": 0.8237958785
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2337034925,
              "format_passes": 0,
              "gpu_energy_j": 57.350966389294605,
              "semantic_passes": 0,
              "tokens_per_s": 78.16351830870445,
              "ttft_s": 0.06733497599999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.199335871,
              "format_passes": 0,
              "gpu_energy_j": 48.47929411911936,
              "semantic_passes": 0,
              "tokens_per_s": 2547.0216754136436,
              "ttft_s": 0.199170246
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.717366535,
              "format_passes": 0,
              "gpu_energy_j": 190.62501670808464,
              "semantic_passes": 0,
              "tokens_per_s": 2859.7980052863995,
              "ttft_s": 0.71712708
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4167014705,
              "format_passes": 0,
              "gpu_energy_j": 383.4558462095209,
              "semantic_passes": 0,
              "tokens_per_s": 2894.8025101443072,
              "ttft_s": 1.4163444589999998
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295721027,
              "format_passes": 2,
              "gpu_energy_j": 75.33746015994163,
              "semantic_passes": 2,
              "tokens_per_s": 78.44069577075092,
              "ttft_s": 0.078949824
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35292072100000005,
              "format_passes": 2,
              "gpu_energy_j": 90.62796144563102,
              "semantic_passes": 2,
              "tokens_per_s": 78.78444126171712,
              "ttft_s": 0.07366341
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3692104625,
              "format_passes": 2,
              "gpu_energy_j": 94.81632692253308,
              "semantic_passes": 2,
              "tokens_per_s": 78.80930412802525,
              "ttft_s": 0.07734077
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.620345378,
              "format_passes": 0,
              "gpu_energy_j": 161.79826771850864,
              "semantic_passes": 0,
              "tokens_per_s": 78.95454871760471,
              "ttft_s": 0.3189945695
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.561020794,
              "format_passes": 0,
              "gpu_energy_j": 146.21230302263285,
              "semantic_passes": 0,
              "tokens_per_s": 78.76160509894899,
              "ttft_s": 0.25641175
            }
          }
        }
      },
      "change_exercised": true,
      "comparison": {
        "format_pass_change": 0,
        "note": "Existing baseline errors do not suppress speed results. Two starts per arm; no independent confirmation claimed.",
        "quality_pass_change": 0,
        "status": "DESCRIPTIVE_COMPARISON",
        "tasks": {
          "code": {
            "e2e_change_pct": -0.6361688665126874,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22570936422924293,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8330468770417321,
            "ttft_change_pct": 0.21212647863233514
          },
          "decode": {
            "e2e_change_pct": -0.8536601500697905,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.04044342387181654,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8601254552051296,
            "ttft_change_pct": -0.9101793257357271
          },
          "energy": {
            "e2e_change_pct": -0.46528364048027404,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -5.569797968551871,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.6567178923925665,
            "ttft_change_pct": 0.010615167320082719
          },
          "filtering": {
            "e2e_change_pct": -1.6539135216666945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.4649619394943922,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.8419272785993979,
            "ttft_change_pct": -1.4274605735935642
          },
          "german": {
            "e2e_change_pct": -0.640644813640534,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9019338351933026,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.911557759043724,
            "ttft_change_pct": -0.1060550409229366
          },
          "ha_sim": {
            "e2e_change_pct": -0.4006254800277276,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1587135394754755,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8883856787526012,
            "ttft_change_pct": 1.3070218859362104
          },
          "jarvis_memory": {
            "e2e_change_pct": -1.0888350370463318,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.1168562753449693,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 1.065578697278835,
            "ttft_change_pct": -1.2157380743089252
          },
          "long_context": {
            "e2e_change_pct": -0.2585843934775345,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8327766302276385,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.9088398397304465,
            "ttft_change_pct": -0.057224440499359375
          },
          "math": {
            "e2e_change_pct": -0.7031478076351849,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.574228711659409,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8059860944982233,
            "ttft_change_pct": -0.46420489903430395
          },
          "prefill": {
            "e2e_change_pct": 0.1612081659606135,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1796164278881962,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1955943808204852,
            "ttft_change_pct": 0.16172399653082703
          },
          "prefill2048": {
            "e2e_change_pct": -0.2216490168718055,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8720563866267073,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22508979965760734,
            "ttft_change_pct": -0.22888967146869055
          },
          "prefill4096": {
            "e2e_change_pct": -0.3153837641277635,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5859926481316835,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3207979571929309,
            "ttft_change_pct": -0.3175139071142752
          },
          "pve_sim": {
            "e2e_change_pct": -0.4644402218084376,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.8335234424094229,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.5781941679424696,
            "ttft_change_pct": -0.14684454219016096
          },
          "sorting": {
            "e2e_change_pct": -0.7166788411704261,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 5.038277614736497,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7577734425600724,
            "ttft_change_pct": -0.5153252619108928
          },
          "time": {
            "e2e_change_pct": -0.7997362046331502,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5041613989186899,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7965835945827004,
            "ttft_change_pct": -0.8779881251499755
          },
          "tool-call": {
            "e2e_change_pct": -0.49352778880575876,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4866265116341917,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.7732703531553309,
            "ttft_change_pct": -0.2952127723956699
          },
          "tool-final": {
            "e2e_change_pct": -0.37794912192643526,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.3656941342693676,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.8050077832809865,
            "ttft_change_pct": 0.20436572368791595
          }
        }
      },
      "complete": true,
      "numerical_results": [
        {
          "begin_ns": 341380595588371,
          "end_ns": 341381100298211,
          "model": "omnicoder2",
          "passed": true,
          "reference": "existing CPU reference backend",
          "returncode": 0
        },
        {
          "begin_ns": 341425768450088,
          "end_ns": 341426073313509,
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

</details>
