# Public audit excerpt

Original SHA256: `e86e6fff4640125cc4dc6c7e63c5d589b993caa01f4f6c51cf2191f4806eb17a`

Original file: `RESULTS.json`; 39734 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 0.666093703,
              "format_passes": 2,
              "gpu_energy_j": 175.87068078883158,
              "semantic_passes": 2,
              "tokens_per_s": 79.30080063638948,
              "ttft_s": 0.12383386199999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.6583428914999998,
              "format_passes": 0,
              "gpu_energy_j": 443.29225316690224,
              "semantic_passes": 0,
              "tokens_per_s": 79.61673922639143,
              "ttft_s": 0.0631617865
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2381007035,
              "format_passes": 2,
              "gpu_energy_j": 51.41088499385833,
              "semantic_passes": 2,
              "tokens_per_s": 78.12706009679587,
              "ttft_s": 0.071706884
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241196828,
              "format_passes": 0,
              "gpu_energy_j": 58.696258774903995,
              "semantic_passes": 0,
              "tokens_per_s": 77.66100774250933,
              "ttft_s": 0.12527321200000002
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.1823277465,
              "format_passes": 2,
              "gpu_energy_j": 37.924764006909555,
              "semantic_passes": 2,
              "tokens_per_s": 77.49436903277677,
              "ttft_s": 0.066136552
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35798983549999996,
              "format_passes": 0,
              "gpu_energy_j": 89.70462322906734,
              "semantic_passes": 0,
              "tokens_per_s": 78.7697599377471,
              "ttft_s": 0.0785980045
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.46930747250000004,
              "format_passes": 0,
              "gpu_energy_j": 114.52332291153391,
              "semantic_passes": 2,
              "tokens_per_s": 79.09806198260199,
              "ttft_s": 0.11525951400000001
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.07618275,
              "format_passes": 2,
              "gpu_energy_j": 285.5348306813869,
              "semantic_passes": 2,
              "tokens_per_s": 77.72734228261999,
              "ttft_s": 0.818863353
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.2338935925,
              "format_passes": 0,
              "gpu_energy_j": 55.799080742649465,
              "semantic_passes": 0,
              "tokens_per_s": 78.06395602104004,
              "ttft_s": 0.06732685499999999
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.197669988,
              "format_passes": 0,
              "gpu_energy_j": 47.943824808485225,
              "semantic_passes": 0,
              "tokens_per_s": 2568.4649448451914,
              "ttft_s": 0.19749612900000002
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7144966445,
              "format_passes": 0,
              "gpu_energy_j": 186.8206395437078,
              "semantic_passes": 0,
              "tokens_per_s": 2871.2241593977305,
              "ttft_s": 0.7142738245
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.409566841,
              "format_passes": 0,
              "gpu_energy_j": 378.1539963190552,
              "semantic_passes": 0,
              "tokens_per_s": 2909.543156505112,
              "ttft_s": 1.4091944855
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.29483342599999995,
              "format_passes": 2,
              "gpu_energy_j": 72.34619734984224,
              "semantic_passes": 2,
              "tokens_per_s": 78.64112791745544,
              "ttft_s": 0.078621254
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3535558855,
              "format_passes": 2,
              "gpu_energy_j": 82.71821927566363,
              "semantic_passes": 2,
              "tokens_per_s": 78.82084547512483,
              "ttft_s": 0.07440912999999999
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.36922593800000003,
              "format_passes": 2,
              "gpu_energy_j": 91.79349641081751,
              "semantic_passes": 2,
              "tokens_per_s": 78.81840937217594,
              "ttft_s": 0.077419878
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.6195512999999999,
              "format_passes": 0,
              "gpu_energy_j": 158.51521715820536,
              "semantic_passes": 0,
              "tokens_per_s": 78.9640976863947,
              "ttft_s": 0.3178394875
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5596042825,
              "format_passes": 0,
              "gpu_energy_j": 144.65448926779067,
              "semantic_passes": 0,
              "tokens_per_s": 78.85424781040479,
              "ttft_s": 0.255412223
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
              "e2e_s": 0.6659053020000001,
              "format_passes": 2,
              "gpu_energy_j": 174.66034026727579,
              "semantic_passes": 2,
              "tokens_per_s": 79.35638578427955,
              "ttft_s": 0.12400617950000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.657603785,
              "format_passes": 0,
              "gpu_energy_j": 442.24434822569435,
              "semantic_passes": 0,
              "tokens_per_s": 79.6521897442332,
              "ttft_s": 0.0628675315
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.238132852,
              "format_passes": 2,
              "gpu_energy_j": 56.67158921278408,
              "semantic_passes": 2,
              "tokens_per_s": 78.17409371304518,
              "ttft_s": 0.071835061
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.241668391,
              "format_passes": 0,
              "gpu_energy_j": 54.823663546202006,
              "semantic_passes": 0,
              "tokens_per_s": 77.50274969411092,
              "ttft_s": 0.125527753
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.18256086700000002,
              "format_passes": 2,
              "gpu_energy_j": 41.419354845356665,
              "semantic_passes": 2,
              "tokens_per_s": 77.34033221575481,
              "ttft_s": 0.066179563
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.3582253995,
              "format_passes": 0,
              "gpu_energy_j": 88.39447138502328,
              "semantic_passes": 0,
              "tokens_per_s": 78.71508368061993,
              "ttft_s": 0.078737131
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.468983338,
              "format_passes": 0,
              "gpu_energy_j": 114.33657534484621,
              "semantic_passes": 2,
              "tokens_per_s": 79.17578578245286,
              "ttft_s": 0.1152934555
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0756935295,
              "format_passes": 2,
              "gpu_energy_j": 287.5895537258607,
              "semantic_passes": 2,
              "tokens_per_s": 77.96869391484495,
              "ttft_s": 0.8190610575
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.233300667,
              "format_passes": 0,
              "gpu_energy_j": 56.28750116993265,
              "semantic_passes": 0,
              "tokens_per_s": 78.31918978424102,
              "ttft_s": 0.067273444
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.1979643225,
              "format_passes": 0,
              "gpu_energy_j": 48.19243186220801,
              "semantic_passes": 0,
              "tokens_per_s": 2565.112963758639,
              "ttft_s": 0.197804875
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7130161745000001,
              "format_passes": 0,
              "gpu_energy_j": 189.14354162978785,
              "semantic_passes": 0,
              "tokens_per_s": 2877.2735543443405,
              "ttft_s": 0.7127736545
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.4052586695,
              "format_passes": 0,
              "gpu_energy_j": 380.29905360916564,
              "semantic_passes": 0,
              "tokens_per_s": 2918.470548821616,
              "ttft_s": 1.4048634975
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.295458995,
              "format_passes": 2,
              "gpu_energy_j": 71.02995854331819,
              "semantic_passes": 2,
              "tokens_per_s": 78.63111777624528,
              "ttft_s": 0.07921913450000001
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.35288953300000003,
              "format_passes": 2,
              "gpu_energy_j": 89.99867919242246,
              "semantic_passes": 2,
              "tokens_per_s": 78.83856695894696,
              "ttft_s": 0.073810777
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.369042172,
              "format_passes": 2,
              "gpu_energy_j": 91.59103755675031,
              "semantic_passes": 2,
              "tokens_per_s": 78.89899928617703,
              "ttft_s": 0.07752113399999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.618249862,
              "format_passes": 0,
              "gpu_energy_j": 159.78539416327163,
              "semantic_passes": 0,
              "tokens_per_s": 79.03909662694579,
              "ttft_s": 0.3174280865
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.5594181645,
              "format_passes": 0,
              "gpu_energy_j": 143.50892089038584,
              "semantic_passes": 0,
              "tokens_per_s": 78.89546355262439,
              "ttft_s": 0.2547960775
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
            "e2e_change_pct": -0.02828445895095566,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6881991450348957,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.07009405635756139,
            "ttft_change_pct": 0.13915216501929617
          },
          "decode": {
            "e2e_change_pct": -0.0445689792978321,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.23639144012140845,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.044526462884841855,
            "ttft_change_pct": -0.4658750429739511
          },
          "energy": {
            "e2e_change_pct": 0.013502060064252142,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 10.232666135885825,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.060201441332918826,
            "ttft_change_pct": 0.178751317655923
          },
          "filtering": {
            "e2e_change_pct": 0.19550961922270016,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -6.597686649081192,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.20378057534757854,
            "ttft_change_pct": 0.20318869129016814
          },
          "german": {
            "e2e_change_pct": 0.12785793960330416,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 9.21453548876514,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1987716255316685,
            "ttft_change_pct": 0.06503362921006506
          },
          "ha_sim": {
            "e2e_change_pct": 0.06580186827680468,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.4605176376455975,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06941275074391351,
            "ttft_change_pct": 0.1770102191334999
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.06906655423007946,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.16306509620922505,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09826258431966384,
            "ttft_change_pct": 0.02944789442718143
          },
          "long_context": {
            "e2e_change_pct": -0.04545886839386615,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.719605044179894,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.31051059400357683,
            "ttft_change_pct": 0.0241437718852211
          },
          "math": {
            "e2e_change_pct": -0.2535022416229715,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8753198453856692,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.32695468716981146,
            "ttft_change_pct": -0.07933089998038989
          },
          "prefill": {
            "e2e_change_pct": 0.14890196684791412,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5185382157469887,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.1305052301095122,
            "ttft_change_pct": 0.1563301526785743
          },
          "prefill2048": {
            "e2e_change_pct": -0.2072046120014992,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.2433862188639955,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.2106904445899671,
            "ttft_change_pct": -0.21002729605136272
          },
          "prefill4096": {
            "e2e_change_pct": -0.3056379715163815,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.5672443795359694,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.3068314108537695,
            "ttft_change_pct": -0.3073378475834221
          },
          "pve_sim": {
            "e2e_change_pct": 0.2121770955509028,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8193614242904332,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.012728888147006678,
            "ttft_change_pct": 0.7604565808629893
          },
          "sorting": {
            "e2e_change_pct": -0.18847161858375205,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 8.801519158066306,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.022483245029025767,
            "ttft_change_pct": -0.8041392232377875
          },
          "time": {
            "e2e_change_pct": -0.04977060956102841,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.22055903956540446,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.10224757723864553,
            "ttft_change_pct": 0.13078811619928743
          },
          "tool-call": {
            "e2e_change_pct": -0.21006137829101545,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.80129657444723,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.09497853169797565,
            "ttft_change_pct": -0.1294367176451039
          },
          "tool-final": {
            "e2e_change_pct": -0.03325885912962567,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.7919342034965138,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05226825867226115,
            "ttft_change_pct": -0.2412357140793575
          }
        }
      },
      "complete": true
    }
  }
}
```
