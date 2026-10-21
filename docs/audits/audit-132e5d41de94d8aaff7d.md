# Public audit excerpt

Original SHA256: `132e5d41de94d8aaff7deab0819cafdd64e14cdf618ca8db63d4b143f131d3cc`

Original file: `RESULTS.json`; 39806 bytes. The original is retained privately and is not distributed. This allowlisted excerpt is **not byte-identical** and cannot independently verify its originating SHA.

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
              "e2e_s": 1.7601001305000001,
              "format_passes": 2,
              "gpu_energy_j": 484.85463736325744,
              "semantic_passes": 2,
              "tokens_per_s": 35.461738157042106,
              "ttft_s": 0.5193268520000001
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7814284065,
              "format_passes": 0,
              "gpu_energy_j": 1066.1490881679097,
              "semantic_passes": 0,
              "tokens_per_s": 35.413919943256516,
              "ttft_s": 0.195177844
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5803100795,
              "format_passes": 2,
              "gpu_energy_j": 148.7045430180052,
              "semantic_passes": 2,
              "tokens_per_s": 35.008775006094794,
              "ttft_s": 0.20890731
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9233936869999999,
              "format_passes": 0,
              "gpu_energy_j": 243.94288116858294,
              "semantic_passes": 0,
              "tokens_per_s": 35.030213559194806,
              "ttft_s": 0.5236869145
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.4645658975,
              "format_passes": 2,
              "gpu_energy_j": 108.38984438135822,
              "semantic_passes": 2,
              "tokens_per_s": 34.22880167163737,
              "ttft_s": 0.2016038615
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9881124674999999,
              "format_passes": 0,
              "gpu_energy_j": 270.05024030716174,
              "semantic_passes": 0,
              "tokens_per_s": 35.35582624016075,
              "ttft_s": 0.224435506
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.148018495,
              "format_passes": 0,
              "gpu_energy_j": 292.91339569033664,
              "semantic_passes": 2,
              "tokens_per_s": 35.302533849722955,
              "ttft_s": 0.3548513375
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 3.7945942435,
              "format_passes": 2,
              "gpu_energy_j": 1018.7766398773217,
              "semantic_passes": 2,
              "tokens_per_s": 34.35953044385087,
              "ttft_s": 3.2124137944999998
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5735603405,
              "format_passes": 2,
              "gpu_energy_j": 149.00181477179837,
              "semantic_passes": 2,
              "tokens_per_s": 34.953166516160664,
              "ttft_s": 0.2016011235
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 0.7258189740000001,
              "format_passes": 0,
              "gpu_energy_j": 186.87987343339722,
              "semantic_passes": 0,
              "tokens_per_s": 696.7923735038664,
              "ttft_s": 0.725637991
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.7450209914999997,
              "format_passes": 0,
              "gpu_energy_j": 738.6002370145533,
              "semantic_passes": 0,
              "tokens_per_s": 746.4352055827496,
              "ttft_s": 2.7447289155
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 5.470276484999999,
              "format_passes": 0,
              "gpu_energy_j": 1479.6636324649708,
              "semantic_passes": 0,
              "tokens_per_s": 749.0073613687465,
              "ttft_s": 5.469944392
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.8458708635000001,
              "format_passes": 0,
              "gpu_energy_j": 224.11781628141082,
              "semantic_passes": 2,
              "tokens_per_s": 35.217126552604356,
              "ttft_s": 0.2211790295
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9840707375,
              "format_passes": 0,
              "gpu_energy_j": 259.56244792069856,
              "semantic_passes": 2,
              "tokens_per_s": 35.089825889695376,
              "ttft_s": 0.214594058
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.015266731,
              "format_passes": 0,
              "gpu_energy_j": 274.5835874707575,
              "semantic_passes": 2,
              "tokens_per_s": 35.2189746783096,
              "ttft_s": 0.22022561499999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.7100979645,
              "format_passes": 0,
              "gpu_energy_j": 459.9046086126267,
              "semantic_passes": 0,
              "tokens_per_s": 35.03047992208595,
              "ttft_s": 1.0319703785
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.779358919,
              "format_passes": 0,
              "gpu_energy_j": 466.9005240004169,
              "semantic_passes": 0,
              "tokens_per_s": 35.08223746510444,
              "ttft_s": 1.0944056775000002
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
              "e2e_s": 1.763238785,
              "format_passes": 2,
              "gpu_energy_j": 490.06609388568296,
              "semantic_passes": 2,
              "tokens_per_s": 35.411577530779155,
              "ttft_s": 0.520639643
            },
            "decode": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 3.7851224935000003,
              "format_passes": 0,
              "gpu_energy_j": 1071.2168891351844,
              "semantic_passes": 0,
              "tokens_per_s": 35.43503297033535,
              "ttft_s": 0.2004579865
            },
            "energy": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5785503194999999,
              "format_passes": 2,
              "gpu_energy_j": 149.97660953175,
              "semantic_passes": 2,
              "tokens_per_s": 35.071444602906055,
              "ttft_s": 0.2078286785
            },
            "filtering": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.923913982,
              "format_passes": 0,
              "gpu_energy_j": 243.25462486881662,
              "semantic_passes": 0,
              "tokens_per_s": 35.028177685797104,
              "ttft_s": 0.5241960315
            },
            "german": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.466180941,
              "format_passes": 2,
              "gpu_energy_j": 107.17937928107433,
              "semantic_passes": 2,
              "tokens_per_s": 34.308701698073264,
              "ttft_s": 0.2038128335
            },
            "ha_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.9876061604999999,
              "format_passes": 0,
              "gpu_energy_j": 264.9392436988891,
              "semantic_passes": 0,
              "tokens_per_s": 35.33263860027391,
              "ttft_s": 0.223388705
            },
            "jarvis_memory": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.1462089450000001,
              "format_passes": 0,
              "gpu_energy_j": 295.0313012574616,
              "semantic_passes": 2,
              "tokens_per_s": 35.3510259965409,
              "ttft_s": 0.3541244315
            },
            "long_context": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 8.5006392175,
              "format_passes": 2,
              "gpu_energy_j": 2066.210186600841,
              "semantic_passes": 2,
              "tokens_per_s": 34.45510506054919,
              "ttft_s": 7.9201065664999994
            },
            "math": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.5744395515,
              "format_passes": 2,
              "gpu_energy_j": 144.64811391782814,
              "semantic_passes": 2,
              "tokens_per_s": 35.07030247016728,
              "ttft_s": 0.2037043025
            },
            "prefill": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 1.8939166295,
              "format_passes": 0,
              "gpu_energy_j": 448.5747453556521,
              "semantic_passes": 0,
              "tokens_per_s": 266.78977775715697,
              "ttft_s": 1.8937914120000001
            },
            "prefill2048": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 7.3336282485,
              "format_passes": 0,
              "gpu_energy_j": 1782.737995474892,
              "semantic_passes": 0,
              "tokens_per_s": 279.3094946000708,
              "ttft_s": 7.333397714
            },
            "prefill4096": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 14.653623984,
              "format_passes": 0,
              "gpu_energy_j": 3582.2488496900933,
              "semantic_passes": 0,
              "tokens_per_s": 279.5529492070712,
              "ttft_s": 14.6533316685
            },
            "pve_sim": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.846625365,
              "format_passes": 0,
              "gpu_energy_j": 224.41313326627892,
              "semantic_passes": 2,
              "tokens_per_s": 35.29630327818414,
              "ttft_s": 0.22331045900000002
            },
            "sorting": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 0.986541161,
              "format_passes": 0,
              "gpu_energy_j": 262.4798192704553,
              "semantic_passes": 2,
              "tokens_per_s": 35.128482141254246,
              "ttft_s": 0.217609341
            },
            "time": {
              "attempts": 2,
              "complete": 2,
              "e2e_s": 1.0169632124999999,
              "format_passes": 0,
              "gpu_energy_j": 275.4618738753313,
              "semantic_passes": 2,
              "tokens_per_s": 35.29556376398425,
              "ttft_s": 0.22362463999999999
            },
            "tool-call": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.231449232,
              "format_passes": 0,
              "gpu_energy_j": 567.1019026620763,
              "semantic_passes": 0,
              "tokens_per_s": 35.062146689019826,
              "ttft_s": 1.5537198045
            },
            "tool-final": {
              "attempts": 6,
              "complete": 6,
              "e2e_s": 2.3462112470000003,
              "format_passes": 0,
              "gpu_energy_j": 573.2572621552054,
              "semantic_passes": 0,
              "tokens_per_s": 35.12171193322482,
              "ttft_s": 1.6625176115
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
            "e2e_change_pct": 0.17832249686318136,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.074849268384126,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.14144999334442243,
            "ttft_change_pct": 0.25278704441031863
          },
          "decode": {
            "e2e_change_pct": 0.09769025359969152,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.47533698837405325,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.05961787656565409,
            "ttft_change_pct": 2.7052980972573915
          },
          "energy": {
            "e2e_change_pct": -0.3032447758819501,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.8554321797624942,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.17901111021552119,
            "ttft_change_pct": -0.5163206112797192
          },
          "filtering": {
            "e2e_change_pct": 0.05634595593677627,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -0.28213830076504465,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.005811764162566568,
            "ttft_change_pct": 0.09721781963678566
          },
          "german": {
            "e2e_change_pct": 0.34764572877414857,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.1167698479434884,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.23342922490359186,
            "ttft_change_pct": 1.0956992507804797
          },
          "ha_sim": {
            "e2e_change_pct": -0.05123981496569785,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -1.8926095390469966,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -0.06558364590134591,
            "ttft_change_pct": -0.46641506001283695
          },
          "jarvis_memory": {
            "e2e_change_pct": -0.15762376720245275,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.723048381632907,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.13736166084952206,
            "ttft_change_pct": -0.20484803724319933
          },
          "long_context": {
            "e2e_change_pct": 124.0197152056845,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 102.81287435582036,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.27816042729251755,
            "ttft_change_pct": 146.54689816299756
          },
          "math": {
            "e2e_change_pct": 0.15329006172803972,
            "format_pass_change": 0,
            "gpu_energy_change_pct": -2.921911293924895,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.33512258167640585,
            "ttft_change_pct": 1.043237737710312
          },
          "prefill": {
            "e2e_change_pct": 160.93512257782336,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 140.03373777729,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -61.71172534286118,
            "ttft_change_pct": 160.98294679832992
          },
          "prefill2048": {
            "e2e_change_pct": 167.1610989937306,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 141.36710308688473,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -62.580878753968875,
            "ttft_change_pct": 167.18112934894683
          },
          "prefill4096": {
            "e2e_change_pct": 167.87720920837518,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 142.09886430218108,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": -62.67687560557319,
            "ttft_change_pct": 167.88812862395912
          },
          "pve_sim": {
            "e2e_change_pct": 0.08919819000241525,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.1317686339123103,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.22482449117908754,
            "ttft_change_pct": 0.9636670821905335
          },
          "sorting": {
            "e2e_change_pct": 0.25104125200146044,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 1.1239574033637068,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11016370295020561,
            "ttft_change_pct": 1.4051102011408023
          },
          "time": {
            "e2e_change_pct": 0.1670971231696683,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 0.31986121700275927,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.21746540430040984,
            "ttft_change_pct": 1.5434285425880212
          },
          "tool-call": {
            "e2e_change_pct": 30.486631662206154,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 23.308593139091794,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.090397753625715,
            "ttft_change_pct": 50.55856610519949
          },
          "tool-final": {
            "e2e_change_pct": 31.85710999321998,
            "format_pass_change": 0,
            "gpu_energy_change_pct": 22.779314369476577,
            "same_token_counts": true,
            "semantic_pass_change": 0,
            "tokens_per_s_change_pct": 0.11251981336608541,
            "ttft_change_pct": 51.91054338257486
          }
        }
      },
      "complete": true
    }
  }
}
```
