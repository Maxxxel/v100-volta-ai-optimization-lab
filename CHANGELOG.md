# Changelog

## 2026-10-23 — Same-quantizer OmniCoder identity and deduplication

The mradermacher OmniCoder V1 Q6_K and retained V2 Q6_K artifacts have different whole-file hashes but identical payload bytes for all 427 tensors / 8,953,803,264 represented values. Full local file hashes, complete typed layouts and each tensor payload were checked; every V2 payload hash also matches the earlier complete CPU-dequantization audit. All non-weight parsed metadata agree except five naming/source/date fields. This proves equality of these stored quantized weights, without a claim about unquantized training history or the cause of an upstream release problem.

At the user's request, rename the retained main file to OmniCoder-9B.Q6_K.gguf and remove the additional downloaded mradermacher V1 copy. Preserve the original main inode, bytes, SHA256, metadata and old compatibility paths. Show an artifact-hash-bound identity label in the benchmark interface while retaining original historical names and immutable scores/IDs. No new GPU jobs or synthetic benchmark results.

## 2026-10-23 — OmniCoder artifact integrity

Complete CPU-only comparison of all 427 matched V1/V2 tensors (8,953,803,264 values): 248 tensors differ after dequantization and 179 are identical. Different tensor precision policies prevent a conclusion about distinct unquantized checkpoints or new fine-tuning. Publish full per-tensor metrics, artifact/source identities and the explicit inconclusive source-weight verdict. No GPU jobs or changes to historical benchmark records.

Record the user-authorized deletion of 15 other OmniCoder2 artifacts while retaining the main Q6_K model. Historical qualification remains valid; unavailable artifacts require reconstruction before replay. Record that the partial OxCoder source investigation was stopped at the user's request, with no automatic resume.

## Initial public snapshot

Canonical matrix revision 219 with original/additional factor separation, immutable reference identities, public-safe audit excerpts, negative results and explicit reproducibility limits. This initial commit does not reconstruct a fictional historical Git history.

## Matrix revision 219

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 220

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 221

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 222

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 223

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 224

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 225

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 226

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 227

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 228

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 229

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 230

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 232

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 233

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 234

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 235

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 236

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 237

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 238

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 239

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 240

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 241

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 242

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 243

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 244

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 245

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 246

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 248

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 249

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 250

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 251

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 252

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 253

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 254

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 255

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 256

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 258

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 259

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 260

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 261

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 262

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 263

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 264

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 265

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 266

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 267

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 268

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 269

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 270

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 271

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 272

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 273

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 274

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 275

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 276

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 277

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 278

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 279

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 280

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 281

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 283

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 284

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 285

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 287

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 289

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 291

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 292

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 293

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 294

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 295

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 296

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 297

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 298

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 299

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 300

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 301

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 302

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 303

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 304

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 305

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 306

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 307

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 310

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 312

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 313

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 314

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 315

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 316

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Matrix revision 317

Audited public snapshot with distinct factor, experiment and profile inventories. See the commit diff and original audit hashes for additions and corrections. Historical original artifacts remain unchanged.

## Audited research checkpoint R410 / fc8c6ea68f4b

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R411 / fc8c6ea68f4b

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R412 / fc8c6ea68f4b

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R414 / fc8c6ea68f4b

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R416 / fc840336b8c9

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R417 / fc840336b8c9

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R418 / fc840336b8c9

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R420 / fc840336b8c9

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R420 / 7a06204ed1df

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R421 / 7a06204ed1df

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R422 / 7a06204ed1df

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R423 / 4d79c192d9db

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R424 / cad419d3af60

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R425 / e6df3dc75565

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R426 / 1b38fe979380

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R427 / 1b38fe979380

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R428 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R429 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R430 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R431 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R432 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R433 / a0e0619e232a

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R434 / 44d0f0ea0f0e

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R435 / 44d0f0ea0f0e

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R436 / 44d0f0ea0f0e

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R437 / 48869f40b1d3

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R438 / 48869f40b1d3

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R439 / 48869f40b1d3

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R440 / 8618784a56ce

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R441 / 8618784a56ce

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R442 / 8512d6f94c9f

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R443 / 6f4b95ac37bf

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R444 / 6f4b95ac37bf

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R445 / 6f4b95ac37bf

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R446 / 6f4b95ac37bf

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R446 / 2031fa351b98

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R446 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Official benchmark admission and immutable configuration history

Separated full official highscores from frozen BFCL/MBPP subsets, HumanEval scorer exceptions and local agent/QA tests. Removed the mixed partial-suite mean from the current comparison view. Added pinned benchmark definitions, separate publisher claims, offline benchmark selection, selectable profile comparisons and immutable per-configuration detail pages. Historical plan-pin mismatches are exposed as provenance gaps rather than silently reconstructed. No new GPU measurements or historical score changes were made for this documentation update.

## Independent full164 official API verification

Replayed the existing R217, R255, R425, R117 and R118 answers in CPU isolation using the pinned official EvalPlus checker and pass@1 estimator. All 820 original task outcomes (both base and plus verdicts per task) were reproduced without changes; no GPU generation was repeated. Five full164 configurations enter the declared local official-API track. The initial project gate requiring every canonical reference to pass was corrected transparently: the HumanEval/32 anomaly belongs to the unchanged official oracle, and remains disclosed with all164 tasks included, unchanged tolerance, validated remaining controls and explicit local evaluation-resource limits. This does not establish publisher-protocol equivalence, lossless MTP, overall model superiority or production qualification. Earlier supplemental records and startup failures remain preserved.

## Remaining archived full164 profiles verified

Completed the same independent CPU-only verification for Ornith R254 (117/164) and Bonsai’s disjoint R271–R279 campaign (151/164). All original task judgments matched. Seven configurations across six models now have full164 official-API evidence under the same declared local scoring protocol. This adds verification, not new GPU measurements or a claim of overall model superiority. Incomplete native-tool/MBPP cohorts remain separate and no cross-benchmark mean is computed.

## Audited research checkpoint R447 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R448 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## 2026-10-23 — Interactive benchmark master table

The configuration comparison now exposes every recorded profile field and startup option through categorized columns, per-parameter filters, exact-protocol benchmark columns, presets and CSV export. An explicitly unofficial user-selected arithmetic mean requires complete results for one immutable configuration. Historical/subset and unqualified full runs remain separate from admitted results; distinct original observations are averaged without best-value selection. Top-5 observations and coverage gaps are descriptive hypotheses, not causal claims. Browser acceptance covers desktop and mobile; static assets use content hashes to prevent stale table versions. Missing metadata remain explicit.

## Audited research checkpoint R449 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## 2026-10-23 — Measured-result master table correction

The default table now includes exactly the configurations referenced by measured `history.runs`, across admitted, historical, supplemental and pending-qualification tracks. Result-free profiles and attempts remain in a separate configuration archive. Pagination and the bounded vertical table viewport are removed; all measured configurations render continuously with normal document scrolling, compact single-line result cells, an optional official-only filter and click-through evidence dialogs.

Pinned historical plans, launches, hash manifests, server logs and answer timings add explicit evidence annotations without changing any published profile, result, attempt or immutable ID. Requested, declared and observed controls remain separate. Recorded engine prefill/decode token counts and timing sums are projected only when exact task counts and independently recorded request-wall totals match. Gross case-window GPU J/output token includes prefill energy. Non-streaming inference does not provide TTFT. Historical logs reporting build 0 (unknown) cannot identify an upstream engine release or commit; executable and kernel hashes remain separate identifiers.

CPU regression checks, confidentiality validation and desktop/mobile browser acceptance cover complete measured-row inclusion, no pagination, uniform row heights including offscreen columns, document scrolling, optional qualification filtering, all parameter columns, provenance, CSV and arithmetic means. No GPU benchmark is started for this change.

## 2026-10-23 — R448 archived reasoning/output-budget diagnosis

Issue12 now links a reproducible read-only analysis of all164 original OxCoder responses and their scoring inputs. Empty final answers reached the4096-token cap with unclosed reasoning; recorded post-close final text is preserved in all nonempty answers. The report retains the original53/164 score, distinguishes completion counters from missing reasoning-token counters, and compares historical profiles with explicit endpoint/thinking/sampling/output-cap differences. Thinking-off and reasoning-budget proposals require separate GPU approval and a900-second whole-trial deadline. No model generation or new benchmark score was added.

## 2026-10-23 — Compact benchmark families with explicit protocol selection

The compact measured-configuration table now shows one column per benchmark family. Own supplemental tests and local-only configurations are excluded from the master comparison and its mean, with all originals retained in the separate local-tests area. Explicit family selectors retain exact dataset revisions, task sets, scorer identities and qualification tracks; admitted local protocols are preferred without filling their gaps from historical runs. Full view retains every exact protocol and measurement. Build-ID is excluded from all preset columns by request; provenance remains in result details, profiles and the optional column picker. Quality, speed and energy presets remain available. Long model names are truncated visually with full titles and profile links on small screens.

Custom means accept at most one protocol per family and require every selected result on the same immutable configuration. Missing coverage displays NICHT BERECHENBAR. CSV exports identify both displayed protocols and the selected mean, including missing results. Result dialogs include configuration, hashes, benchmark definition, task counts, dispersion, measured metrics and audit links. No original score, qualification, configuration identity or benchmark definition changed; no GPU benchmark was started.

## 2026-10-23 — Recover engine source versions and unify OmniCoder labels

Historical runtime logs reported build0 (unknown), but preserved build receipts independently identify the source bases and patch ancestry. Exact build/server/CUDA-library matching now supplies source revision labels in the Engine-Version / Quellstand column: the shared main source base, its HBM-cache variant and the separate Bonsai PQ2 source. These labels are source revisions with local patches, not fabricated release tags. Original profiles, run identities and scores remain unchanged; source receipts and limitations are available in configuration details.

OmniCoder V1/V2 is displayed uniformly as OmniCoder 9B. Different measured runtime/quantization/MTP configurations remain distinct rows; original model labels stay in the immutable historical records. No new model, GPU run, benchmark score or qualification is introduced.

## 2026-10-23 — Pinned OmniCoder derivative source and CPU review

The existing benchmark register now includes a bounded105-repository research inventory, the six requested seed reviews, publisher claims kept separate from local results, and three proposed Q6 coding profiles. Same-format source samples and nonzero adapter products were observed in CPU-only probes and independently replayed; this is neither a complete weight census nor a quality qualification. Exact source revisions, metadata hashes, byte-range identities, limitations and specialist prerequisites are retained. Raw weights, templates, downloaded code and private infrastructure remain outside the public export.

Nexus, Slopus and Claude-distill are prioritized for investigation, with no measured quality ordering. GUI base/substrate composition and Phase1 adapter/license mapping remain unresolved. The full900-second benchmark budget and separate PhaseC GPU approval apply to all new derivative proposals. No new model benchmark or qualification is added. Existing measured configuration IDs, scores, benchmark definitions, champion records and original artifacts are unchanged.

## Audited research checkpoint R451 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R452 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Single benchmark-table entry point — 2026-10-23

The model comparison has one public result table. Legacy benchmark and supplemental comparison URLs redirect to it; duplicate comparison navigation is removed. Full and partial results retain their measured task counts and qualification within the same family columns. Original datasets, immutable profiles, audits and scores are unchanged. Browser checks cover both old URLs, desktop and mobile.

## Audited research checkpoint R453 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## R453 — full native BFCL Python category, 2026-10-23

LFM2.5-8B-A1B Q6_K completed all400 pinned `simple_python` cases in one broker-admitted model session. The original official AST checker and a second CPU replay both scored371/400 (92.75%); separate practical checks also scored371/400, with400 valid and complete replies. Task phase:802.998s; request windows:801.605s; GPU energy:153913.043J; GPU J per AST success:414.860; peak VRAM:7436.5MiB. This is one official category under the declared local native profile, not BFCL overall or a model/optimization Champion. Complete source identities, shared canonical controls and both scoring receipts are verified by the export pipeline. All original profiles and partial results remain in the same single master table.

## Audited research checkpoint R454 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## R454 — complete MiMo native coding benchmark, 2026-10-23 UTC

MiMo V2.6 Distill Qwen9B Q8_0 completed all164 HumanEval+ cases in one broker-admitted session. Both CPU scoring paths confirmed119/164 (72.56%), with zero changed judgments, under the existing declared local official-API protocol and its disclosed unchanged upstream reference anomaly. Task time:1036.681s; complete-request windows:1034.471s; GPU energy:254420.561J; GPU J per success:2137.988; peak VRAM:9186.5MiB. Thinking was explicitly enabled, output4096, temperature0.6, top-p0.95, top-k20, seed1001, context8192 and no MTP. Three replies reached the output cap and had empty final content; all remain in the denominator. This does not predict a benefit from raising the cap.

The full result and original partial results share the single master table. Previously unknown quantization fields may now be supplemented only by unambiguous hash-pinned engine metadata, without rewriting original profiles or replacing known values. Original audits, scores, A0 and Champions remain unchanged. The next Bonsai tool-category comparison is prepared to retain40 valid historical answers and request only the360 missing tasks; matched LFM360 costs are derived from existing R453 data with zero new GPU requests. No full Bonsai category score or new speedup is claimed.

## Audited research checkpoint R455 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R456 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R457 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.

## Audited research checkpoint R458 / 4c76e5c1cfd5

Audited model results and benchmark visualizations updated from pinned evidence. Task cohorts, partial screens and profile limits remain separate; original audit hashes preserve corrections and negative results.
