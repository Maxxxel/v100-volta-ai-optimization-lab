# Public audit excerpt

Original SHA256: `3dc281ae51c34f38e0b448f26a7f1ba419397c91b00eadcda16f25197c4a62ea`

Original file: `RESULTS.json`; 39934 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7629352485,
              "format_passes": 2,
              "gpu_energy_j": 484.6658010436971,
              "semantic_passes": 2,
              "tokens_per_s": 35.42573769201699,
              "ttft_s": 0.5208323475000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7872930575000003,
              "format_passes": 0,
              "gpu_energy_j": 1070.1198987695493,
              "semantic_passes": 0,
              "tokens_per_s": 35.361803213422604,
              "ttft_s": 0.19533253750000001
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.580534915,
              "format_passes": 2,
              "gpu_energy_j": 144.88031495412164,
              "semantic_passes": 2,
              "tokens_per_s": 34.899030798074904,
              "ttft_s": 0.207981896
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9249518910000001,
              "format_passes": 0,
              "gpu_energy_j": 245.45181345238302,
              "semantic_passes": 0,
              "tokens_per_s": 34.95617526190105,
              "ttft_s": 0.524418614
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4645058045,
              "format_passes": 2,
              "gpu_energy_j": 107.88603986698135,
              "semantic_passes": 2,
              "tokens_per_s": 34.20759739059876,
              "ttft_s": 0.20139551
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9897348345,
              "format_passes": 0,
              "gpu_energy_j": 265.28210099258797,
              "semantic_passes": 0,
              "tokens_per_s": 35.280357034656184,
              "ttft_s": 0.22442924
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1471070805,
              "format_passes": 0,
              "gpu_energy_j": 302.1867416540363,
              "semantic_passes": 2,
              "tokens_per_s": 35.22000771044405,
              "ttft_s": 0.352100205
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.797061861,
              "format_passes": 2,
              "gpu_energy_j": 1022.5096002886817,
              "semantic_passes": 2,
              "tokens_per_s": 34.364600434758586,
              "ttft_s": 3.2150240875
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5739561705,
              "format_passes": 2,
              "gpu_energy_j": 143.64002291164667,
              "semantic_passes": 2,
              "tokens_per_s": 34.960451364809124,
              "ttft_s": 0.20208102249999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7274960779999999,
              "format_passes": 0,
              "gpu_energy_j": 189.57210004339012,
              "semantic_passes": 0,
              "tokens_per_s": 695.1489020645229,
              "ttft_s": 0.72734398
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7525069985000004,
              "format_passes": 0,
              "gpu_energy_j": 736.8526211387966,
              "semantic_passes": 0,
              "tokens_per_s": 744.3806467891028,
              "ttft_s": 2.7522679465
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.465728704,
              "format_passes": 0,
              "gpu_energy_j": 1473.0000866001174,
              "semantic_passes": 0,
              "tokens_per_s": 749.6381215091751,
              "ttft_s": 5.4653318665
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.845423974,
              "format_passes": 0,
              "gpu_energy_j": 228.4929235462979,
              "semantic_passes": 2,
              "tokens_per_s": 35.27807353958849,
              "ttft_s": 0.2217939725
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9849807555000001,
              "format_passes": 0,
              "gpu_energy_j": 265.20319322621833,
              "semantic_passes": 2,
              "tokens_per_s": 35.098180688729485,
              "ttft_s": 0.215644816
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0138676750000002,
              "format_passes": 0,
              "gpu_energy_j": 274.57469330069137,
              "semantic_passes": 2,
              "tokens_per_s": 35.28271694013811,
              "ttft_s": 0.22026855499999998
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7095470160000001,
              "format_passes": 0,
              "gpu_energy_j": 455.8099442693349,
              "semantic_passes": 0,
              "tokens_per_s": 34.9708913020219,
              "ttft_s": 1.029579908
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7781093605,
              "format_passes": 0,
              "gpu_energy_j": 467.68659577043394,
              "semantic_passes": 0,
              "tokens_per_s": 35.07818143477102,
              "ttft_s": 1.094128415
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
              "e2e_s": 1.767225697,
              "format_passes": 2,
              "gpu_energy_j": 485.5909041365532,
              "semantic_passes": 2,
              "tokens_per_s": 35.295637625158264,
              "ttft_s": 0.5205735765
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.785559277,
              "format_passes": 0,
              "gpu_energy_j": 1071.402519458356,
              "semantic_passes": 0,
              "tokens_per_s": 35.36835029388888,
              "ttft_s": 0.1957613675
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.58179458,
              "format_passes": 2,
              "gpu_energy_j": 144.8698196220668,
              "semantic_passes": 2,
              "tokens_per_s": 34.87896423952074,
              "ttft_s": 0.209013481
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.925211776,
              "format_passes": 0,
              "gpu_energy_j": 246.64560480827777,
              "semantic_passes": 0,
              "tokens_per_s": 34.97876384004397,
              "ttft_s": 0.5249816495
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465180069,
              "format_passes": 2,
              "gpu_energy_j": 111.59714749550484,
              "semantic_passes": 2,
              "tokens_per_s": 34.22730552965814,
              "ttft_s": 0.202236258
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9896407215,
              "format_passes": 0,
              "gpu_energy_j": 264.6264204320447,
              "semantic_passes": 0,
              "tokens_per_s": 35.22932349787954,
              "ttft_s": 0.223188828
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1447273675,
              "format_passes": 0,
              "gpu_energy_j": 297.3454613180669,
              "semantic_passes": 2,
              "tokens_per_s": 35.255669835889066,
              "ttft_s": 0.35048368399999996
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8034467695,
              "format_passes": 2,
              "gpu_energy_j": 1031.9500453033863,
              "semantic_passes": 2,
              "tokens_per_s": 34.37143885731651,
              "ttft_s": 3.2215304535
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5738467085000001,
              "format_passes": 2,
              "gpu_energy_j": 144.97067191812926,
              "semantic_passes": 2,
              "tokens_per_s": 34.97475720966216,
              "ttft_s": 0.2021102335
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7269615945000001,
              "format_passes": 0,
              "gpu_energy_j": 190.44882197064024,
              "semantic_passes": 0,
              "tokens_per_s": 695.6806598350843,
              "ttft_s": 0.726831132
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.752654996,
              "format_passes": 0,
              "gpu_energy_j": 734.9181669476206,
              "semantic_passes": 0,
              "tokens_per_s": 744.3573434519421,
              "ttft_s": 2.7523808929999998
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.475610843,
              "format_passes": 0,
              "gpu_energy_j": 1471.9158812708242,
              "semantic_passes": 0,
              "tokens_per_s": 748.2742370215528,
              "ttft_s": 5.475291754
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8485195320000001,
              "format_passes": 0,
              "gpu_energy_j": 226.20834462889275,
              "semantic_passes": 2,
              "tokens_per_s": 35.15136006795795,
              "ttft_s": 0.2226209695
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.983513817,
              "format_passes": 0,
              "gpu_energy_j": 267.6028862281486,
              "semantic_passes": 2,
              "tokens_per_s": 35.105671677659416,
              "ttft_s": 0.21437396949999998
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0159816985,
              "format_passes": 0,
              "gpu_energy_j": 272.98937434666936,
              "semantic_passes": 2,
              "tokens_per_s": 35.21486084558488,
              "ttft_s": 0.2208117495
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7089199515,
              "format_passes": 0,
              "gpu_energy_j": 458.7385768492363,
              "semantic_passes": 0,
              "tokens_per_s": 34.9717435715677,
              "ttft_s": 1.0300832
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7808534645,
              "format_passes": 0,
              "gpu_energy_j": 467.61814545460015,
              "semantic_passes": 0,
              "tokens_per_s": 35.03726648772809,
              "ttft_s": 1.0952781324999998
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
            "e2e_change_pct": 0.24336960212523184,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.19087443159058193,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3672473047414915,
            "ttft_change_pct": -0.049684126042126575
          },
          "decode": {
            "e2e_change_pct": -0.045778884117952945,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11985766177056156,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.018514554890658452,
            "ttft_change_pct": 0.21953843711266519
          },
          "energy": {
            "e2e_change_pct": 0.21698350391206045,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.007244139452733389,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.05749889923954976,
            "ttft_change_pct": 0.495997497782219
          },
          "filtering": {
            "e2e_change_pct": 0.02809713700018257,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4863648547157151,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.06461970731543865,
            "ttft_change_pct": 0.107363751966294
          },
          "german": {
            "e2e_change_pct": 0.14515738952407542,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 3.439840440059827,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05761333903209209,
            "ttft_change_pct": 0.417461143994724
          },
          "ha_sim": {
            "e2e_change_pct": -0.009508910540412252,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.24716351313939233,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1446514181432823,
            "ttft_change_pct": -0.5526962529481483
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.20745343137127392,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.6020823115767469,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.1012553027762042,
            "ttft_change_pct": -0.4591082246032885
          },
          "long_context": {
            "e2e_change_pct": 0.1681539235791618,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9232622375417776,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.019899613181628695,
            "ttft_change_pct": 0.202373787036203
          },
          "math": {
            "e2e_change_pct": -0.01907149110438322,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9263776066793517,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04092008053258045,
            "ttft_change_pct": 0.014455093129805974
          },
          "prefill": {
            "e2e_change_pct": -0.07346891841248926,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.4624741336143101,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07649552045354557,
            "ttft_change_pct": -0.07050969198919566
          },
          "prefill2048": {
            "e2e_change_pct": 0.005376825565939214,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.2625293221032887,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.0031305673060089134,
            "ttft_change_pct": 0.0041037610507110855
          },
          "prefill4096": {
            "e2e_change_pct": 0.18080185708391205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.07360524545491076,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.18193905145544864,
            "ttft_change_pct": 0.18223756110857803
          },
          "pve_sim": {
            "e2e_change_pct": 0.3661545088855078,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.9998466831915853,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.35918478226523165,
            "ttft_change_pct": 0.3728672112584208
          },
          "sorting": {
            "e2e_change_pct": -0.1489306762400111,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.9048507194569622,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.021342955056180557,
            "ttft_change_pct": -0.5893239279167295
          },
          "time": {
            "e2e_change_pct": 0.20851079012849105,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5773725666283092,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.19232105812133637,
            "ttft_change_pct": 0.24660555838305065
          },
          "tool-call": {
            "e2e_change_pct": -0.03668015527688029,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6425117785870293,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.002437082710993188,
            "ttft_change_pct": 0.048883238308095045
          },
          "tool-final": {
            "e2e_change_pct": 0.15432706564395549,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.01463593706828581,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11663930503070796,
            "ttft_change_pct": 0.10508067282029021
          }
        }
      },
      "complete": true
    }
  }
}
```
