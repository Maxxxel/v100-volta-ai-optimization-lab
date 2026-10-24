# Public audit excerpt

Original SHA256: `aeda02dbb668c945905c48ac8b7b994dc125ef3abc1ca9c87694290ccff89b8e`

Original file: `RESULTS.json`; 39874 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.764805039,
              "format_passes": 2,
              "gpu_energy_j": 481.79685799148626,
              "semantic_passes": 2,
              "tokens_per_s": 35.362695974694645,
              "ttft_s": 0.5205375354999999
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7848488495000003,
              "format_passes": 0,
              "gpu_energy_j": 1070.9279211446828,
              "semantic_passes": 0,
              "tokens_per_s": 35.388205431129194,
              "ttft_s": 0.194318612
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5818174965,
              "format_passes": 2,
              "gpu_energy_j": 150.3595659541246,
              "semantic_passes": 2,
              "tokens_per_s": 34.95063876144502,
              "ttft_s": 0.20989310049999998
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9235597785,
              "format_passes": 0,
              "gpu_energy_j": 242.60345824551104,
              "semantic_passes": 0,
              "tokens_per_s": 35.01962361823051,
              "ttft_s": 0.5237649154999999
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.465026674,
              "format_passes": 2,
              "gpu_energy_j": 109.48267325401113,
              "semantic_passes": 2,
              "tokens_per_s": 34.16000577317429,
              "ttft_s": 0.201572425
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9899195215000001,
              "format_passes": 0,
              "gpu_energy_j": 264.69236890913305,
              "semantic_passes": 0,
              "tokens_per_s": 35.283427596206636,
              "ttft_s": 0.2246420635
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1481475155,
              "format_passes": 0,
              "gpu_energy_j": 293.5189436169838,
              "semantic_passes": 2,
              "tokens_per_s": 35.262605066617304,
              "ttft_s": 0.3541045195
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7888913075,
              "format_passes": 2,
              "gpu_energy_j": 1025.982675884955,
              "semantic_passes": 2,
              "tokens_per_s": 34.45483930274203,
              "ttft_s": 3.2083452405
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5741863995,
              "format_passes": 2,
              "gpu_energy_j": 141.8222115073564,
              "semantic_passes": 2,
              "tokens_per_s": 34.919347153840235,
              "ttft_s": 0.20187703899999998
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.726236639,
              "format_passes": 0,
              "gpu_energy_j": 191.2396502924842,
              "semantic_passes": 0,
              "tokens_per_s": 696.4023655894529,
              "ttft_s": 0.7261085635
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.748495809,
              "format_passes": 0,
              "gpu_energy_j": 734.341076738293,
              "semantic_passes": 0,
              "tokens_per_s": 745.4743705914614,
              "ttft_s": 2.7482463365000003
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.4689275585,
              "format_passes": 0,
              "gpu_energy_j": 1479.4201245401316,
              "semantic_passes": 0,
              "tokens_per_s": 749.1896607896366,
              "ttft_s": 5.468600809
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8466119590000001,
              "format_passes": 0,
              "gpu_energy_j": 228.03202699777205,
              "semantic_passes": 2,
              "tokens_per_s": 35.22784628614109,
              "ttft_s": 0.22213003999999997
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9861582255,
              "format_passes": 0,
              "gpu_energy_j": 260.9644569694502,
              "semantic_passes": 2,
              "tokens_per_s": 35.03523710810906,
              "ttft_s": 0.215462734
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0144652715,
              "format_passes": 0,
              "gpu_energy_j": 274.6546276277903,
              "semantic_passes": 2,
              "tokens_per_s": 35.26997609709963,
              "ttft_s": 0.2205546085
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7073653915,
              "format_passes": 0,
              "gpu_energy_j": 461.9294677228462,
              "semantic_passes": 0,
              "tokens_per_s": 35.025414790496725,
              "ttft_s": 1.02920026
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779811719,
              "format_passes": 0,
              "gpu_energy_j": 467.37241770908076,
              "semantic_passes": 0,
              "tokens_per_s": 35.03951520743583,
              "ttft_s": 1.0947004195
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
              "e2e_s": 1.766586424,
              "format_passes": 2,
              "gpu_energy_j": 487.30286568138604,
              "semantic_passes": 2,
              "tokens_per_s": 35.309298379322776,
              "ttft_s": 0.520366841
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.764287889,
              "format_passes": 0,
              "gpu_energy_j": 1068.8874464284077,
              "semantic_passes": 0,
              "tokens_per_s": 35.3370219177296,
              "ttft_s": 0.170660612
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5646524135,
              "format_passes": 2,
              "gpu_energy_j": 150.41875941531381,
              "semantic_passes": 2,
              "tokens_per_s": 34.92856073517922,
              "ttft_s": 0.1924004455
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.924664107,
              "format_passes": 0,
              "gpu_energy_j": 240.96627224381217,
              "semantic_passes": 0,
              "tokens_per_s": 34.915423385625076,
              "ttft_s": 0.5237239355000001
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4425178635,
              "format_passes": 2,
              "gpu_energy_j": 106.51091006167927,
              "semantic_passes": 2,
              "tokens_per_s": 34.19960892929584,
              "ttft_s": 0.1793976275
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9795945005,
              "format_passes": 0,
              "gpu_energy_j": 266.3187796609061,
              "semantic_passes": 0,
              "tokens_per_s": 35.29439950299522,
              "ttft_s": 0.214582098
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1068241639999998,
              "format_passes": 0,
              "gpu_energy_j": 294.16627179913866,
              "semantic_passes": 2,
              "tokens_per_s": 35.26853470798291,
              "ttft_s": 0.3129159325
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.8021007855,
              "format_passes": 2,
              "gpu_energy_j": 1020.7524726401075,
              "semantic_passes": 2,
              "tokens_per_s": 34.318445613679394,
              "ttft_s": 3.2192557605000003
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.55382902,
              "format_passes": 2,
              "gpu_energy_j": 141.78399214424374,
              "semantic_passes": 2,
              "tokens_per_s": 34.96009853237571,
              "ttft_s": 0.1819631955
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.728684932,
              "format_passes": 0,
              "gpu_energy_j": 188.67569518162995,
              "semantic_passes": 0,
              "tokens_per_s": 694.0171526284007,
              "ttft_s": 0.7285102445
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.755266408,
              "format_passes": 0,
              "gpu_energy_j": 737.8719936087077,
              "semantic_passes": 0,
              "tokens_per_s": 743.6321074495802,
              "ttft_s": 2.7550609955
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.467085592,
              "format_passes": 0,
              "gpu_energy_j": 1481.140198276764,
              "semantic_passes": 0,
              "tokens_per_s": 749.4410119708245,
              "ttft_s": 5.466743692
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.837883224,
              "format_passes": 0,
              "gpu_energy_j": 225.73977784407833,
              "semantic_passes": 2,
              "tokens_per_s": 35.23676289780779,
              "ttft_s": 0.2135246405
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.971178315,
              "format_passes": 0,
              "gpu_energy_j": 259.3616010148028,
              "semantic_passes": 2,
              "tokens_per_s": 35.00976443415683,
              "ttft_s": 0.1999389735
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0049982955,
              "format_passes": 0,
              "gpu_energy_j": 273.3268887002413,
              "semantic_passes": 2,
              "tokens_per_s": 35.22872494832191,
              "ttft_s": 0.210186607
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.690129706,
              "format_passes": 0,
              "gpu_energy_j": 459.8638936950201,
              "semantic_passes": 0,
              "tokens_per_s": 34.98577530858758,
              "ttft_s": 1.01106443
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7787121255,
              "format_passes": 0,
              "gpu_energy_j": 468.5862921673771,
              "semantic_passes": 0,
              "tokens_per_s": 35.05576451877178,
              "ttft_s": 1.094141616
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
            "e2e_change_pct": 0.10093947833520467,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1428068902012312,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.15099978635702005,
            "ttft_change_pct": -0.032791967602485705
          },
          "decode": {
            "e2e_change_pct": -0.543243900023016,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.1905333380508134,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14463438531576722,
            "ttft_change_pct": -12.174850240284762
          },
          "energy": {
            "e2e_change_pct": -2.9502521156993256,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.039367938324108565,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06316916384989657,
            "ttft_change_pct": -8.334078137075307
          },
          "filtering": {
            "e2e_change_pct": 0.11957303963514576,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6748403396797609,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.29754812256517216,
            "ttft_change_pct": -0.007824120857868877
          },
          "german": {
            "e2e_change_pct": -4.840326750804835,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.7143684968643944,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11593427818636926,
            "ttft_change_pct": -11.000908234348028
          },
          "ha_sim": {
            "e2e_change_pct": -1.0430162024034906,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.6144532078789844,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.031096487887039004,
            "ttft_change_pct": -4.478219859300747
          },
          "jarvis_memory": {
            "e2e_change_pct": -3.599132597696264,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.220540512369638,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.0168156645103279,
            "ttft_change_pct": -11.63175975787002
          },
          "long_context": {
            "e2e_change_pct": 0.34863702671681374,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.5097750057364459,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3958622121676303,
            "ttft_change_pct": 0.34006689374550536
          },
          "math": {
            "e2e_change_pct": -3.5454304591204577,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.026948785177194345,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11670143303637026,
            "ttft_change_pct": -9.864342967701234
          },
          "prefill": {
            "e2e_change_pct": 0.3371205566509383,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.3407026769464037,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.3425050055700596,
            "ttft_change_pct": 0.330760594314361
          },
          "prefill2048": {
            "e2e_change_pct": 0.24633834178786618,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.48082791256862656,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.2471262882477787,
            "ttft_change_pct": 0.24796390736496754
          },
          "prefill4096": {
            "e2e_change_pct": -0.03368057960718707,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.11626675263507469,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.03354973971785302,
            "ttft_change_pct": -0.03395963729778684
          },
          "pve_sim": {
            "e2e_change_pct": -1.0310195724509086,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.0052312317147094,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.025311259718452384,
            "ttft_change_pct": -3.87403680294659
          },
          "sorting": {
            "e2e_change_pct": -1.5190169399443954,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.6142046979352056,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.07270587001774187,
            "ttft_change_pct": -7.20484708042366
          },
          "time": {
            "e2e_change_pct": -0.9331986284756622,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4834212840383545,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11695825555467776,
            "ttft_change_pct": -4.700877288628503
          },
          "tool-call": {
            "e2e_change_pct": -1.0094901528288402,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.4471622124495811,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.11317348315859066,
            "ttft_change_pct": -1.7621283927775178
          },
          "tool-final": {
            "e2e_change_pct": -0.06178145071534802,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.2597231698537872,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.04637424701727788,
            "ttft_change_pct": -0.0510462488226171
          }
        }
      },
      "complete": true
    }
  }
}
```

</details>
