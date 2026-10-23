"""Pinned model-research projection; never loads models or runs repository code."""
import collections, hashlib, json, pathlib, re


def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def pick(value, keys):
    return {k: value[k] for k in keys if k in value}


def cpu_result(row):
    result = pick(row, ('repository', 'kind', 'classification', 'adapter_tensor_count',
                       'vision_named_tensor_count', 'parameters', 'full_tensor_census',
                       'training_or_quality_improvement_proven', 'quality_gain_proven',
                       'correct_base_revision_or_complete_adapter_composition_proven'))
    pair_keys = ('base_tensor', 'candidate_tensor', 'shape', 'base_dtype', 'candidate_dtype',
                 'compared_values', 'exact_changed_values', 'max_abs_difference', 'rmse',
                 'same_stored_dtype', 'A_tensor', 'B_tensor', 'A_shape', 'B_shape',
                 'A_nonzero_values', 'B_probed_nonzero_values', 'effective_delta_probed_cells',
                 'effective_delta_nonzero_cells', 'max_abs_unscaled_delta')
    result['pairs'] = [pick(p, pair_keys) for p in row['pairs']]
    if row.get('full_tensor_census') is not False:
        raise ValueError('Bounded probes cannot be promoted to full tensor census')
    if any(row.get(k) is True for k in ('training_or_quality_improvement_proven',
                                       'quality_gain_proven',
                                       'correct_base_revision_or_complete_adapter_composition_proven')):
        raise ValueError('Unsupported training, composition or quality claim')
    return result


def projection(a, cpu, replay, gguf, proposals, history):
    """Strict positive projection. Raw headers/fragments/code/templates stay private."""
    if a['new_GPU_runs'] != 0 or a['model_requests'] != 0 or a['new_full_model_downloads'] != 0 or a['existing_weights_modified_or_deleted'] is not False:
        raise ValueError('Not a read-only CPU research review')
    if cpu['status'] != 'COMPLETE_BOUNDED_CPU_PROBES' or cpu['execution_uid'] == 0 or cpu['new_GPU_runs'] != 0 or cpu['model_execution'] is not False or cpu['full_model_downloads'] != 0 or not all(cpu['controls'].values()):
        raise ValueError('CPU probe controls not established')
    if replay['source_audit_sha256'] != a['CPU_audit_sha256'] or replay['status'] != 'BOUNDED_CPU_RESULTS_INDEPENDENTLY_REPLAYED' or replay['raw_fragment_hashes_verified'] != len(cpu['range_receipts']) or replay['new_GPU_runs'] != 0 or replay['models_executed'] is not False or replay['full_model_identity_or_quality_proven'] is not False:
        raise ValueError('Independent CPU replay is incomplete')
    if gguf['new_GPU_runs'] != 0 or gguf['model_execution'] is not False or gguf['full_model_downloads'] != 0:
        raise ValueError('GGUF inspection was not header-only')
    if a['phase_C_gate'] != 'SEPARATE_USER_APPROVAL_REQUIRED_NO_AUTO_GPU_EXECUTION':
        raise ValueError('Research GPU approval gate changed')
    cpu_rows = [cpu_result(r) for r in cpu['results']]
    if replay['same_dtype_source_sample_pairs_replayed'] != sum(len(r['pairs']) for r in cpu_rows if r['kind'] == 'BOUNDED_UNQUANTIZED_SOURCE_VALUE_PROBE') or replay['low_rank_delta_blocks_replayed'] != sum(len(r['pairs']) for r in cpu_rows if r['kind'] == 'LORA_STRUCTURAL_AND_EFFECTIVE_DELTA_PROBE'):
        raise ValueError('CPU replay scope does not cover the original probes')
    by_repo = {r['repository']: r for r in cpu_rows}
    candidate_keys = ('repository', 'revision', 'created_at', 'updated_at', 'license',
                      'license_status', 'kind', 'discovery_route', 'base_models',
                      'original_training_base_revision', 'published_base_revision_limit',
                      'model_type', 'architectures', 'published_parameter_count', 'text_layers',
                      'declared_context_tokens', 'vision_configuration_present',
                      'full_weight_object_matches_baseline_metadata', 'GGUF_quantizations_available',
                      'metadata_sha256', 'card_sha256', 'config_sha256', 'adapter_config_sha256',
                      'decision', 'reason', 'method_evidence', 'priority')
    candidates = []
    for r in a['candidates']:
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', r['repository']) or not re.fullmatch('[a-f0-9]{40}', r['revision']):
            raise ValueError('Candidate repository/revision is not pinned')
        if any(r.get(k) != 'NOT MEASURED' for k in ('local_quality', 'local_latency', 'local_energy', 'local_VRAM')) or r['local_gpu_qualified'] is not False:
            raise ValueError('A research candidate cannot carry local GPU scores')
        row = pick(r, candidate_keys)
        row['artifacts'] = [pick(f, ('filename', 'bytes', 'published_sha256', 'format', 'hash_class')) for f in r['artifacts']]
        for f in row['artifacts']:
            if f.get('published_sha256') is not None and not re.fullmatch('[a-f0-9]{64}', f['published_sha256']):
                raise ValueError('Invalid published artifact identity')
        row['adapter'] = pick(r['adapter'], ('peft_type', 'r', 'lora_alpha', 'revision', 'task_type', 'target_modules')) if r.get('adapter') else None
        row['CPU_integrity'] = by_repo.get(r['repository'])
        if r.get('CPU_integrity') is not None and r['CPU_integrity'] != row['CPU_integrity']:
            raise ValueError('Candidate probe summary differs from the original CPU audit')
        row.update(local_quality='NOT MEASURED', local_latency='NOT MEASURED',
                   local_energy='NOT MEASURED', local_VRAM='NOT MEASURED', local_gpu_qualified=False)
        candidates.append(row)
    if len({r['repository'] for r in candidates}) != len(candidates) or len(candidates) != a['counts']['unique_inventory_repositories']:
        raise ValueError('Duplicated or missing research repositories')
    candidates_by_repo = {r['repository']: r for r in candidates}
    if not set(a['requested_six']).issubset(candidates_by_repo):
        raise ValueError('Requested seeds are missing')
    headers = []
    for g in gguf['results']:
        h = g['header']; metadata = h['metadata']
        if h['tensor_count'] != len(h['tensors']) or dict(collections.Counter(t['type_name'] for t in h['tensors'].values())) != h['type_counts']:
            raise ValueError('GGUF header tensor census mismatch')
        headers.append({'repository': g['repository'], 'revision': g['revision'],
                        'filename': g['file']['rfilename'], 'published_sha256': g['file']['lfs']['sha256'],
                        'published_bytes': g['file']['size'], 'header_sha256': g['header_sha256'],
                        'gguf_version': h['gguf_version'], 'tensor_count': h['tensor_count'],
                        'type_counts': h['type_counts'], 'architecture': metadata.get('general.architecture'),
                        'layers': metadata.get('qwen35.block_count'),
                        'declared_context_tokens': metadata.get('qwen35.context_length'),
                        'MTP_tensors': sum('mtp' in n.lower() for n in h['tensors']),
                        'GPU_load_confirmed': False})
    profile_keys = ('profile_id', 'research_priority_rank', 'quality_rank', 'repository', 'revision',
                    'filename', 'model_sha256', 'bytes', 'quantization', 'quantizer', 'declared_upstream',
                    'template_sha256', 'whole_benchmark_wall_budget_s', 'budget_covers', 'status',
                    'new_GPU_execution_authorized', 'reason', 'prerequisites', 'comparison_limit',
                    'planned_argv', 'runtime_identity_note')
    engine_keys = ('name', 'version', 'build_id', 'binary_sha256', 'kernel_library_sha256',
                   'source_attested_commit', 'upstream_contract_commit', 'repository',
                   'source_inputs_sha256', 'source_proof_sha256', 'build_receipt_sha256',
                   'CUDA_compiler_record', 'driver_observed', 'loaded_driver_or_runtime_limit', 'patch_receipts')
    runtime_keys = ('context_tokens', 'max_output_tokens', 'thinking_requested', 'thinking_effective',
                    'MTP_requested', 'spec_type', 'external_draft', 'flash_attention_requested',
                    'flash_attention_effective', 'KV_K', 'KV_V', 'batch', 'microbatch', 'CPU_threads',
                    'GPU_offload_layers', 'power_limit_w', 'actual_graph_capture',
                    'prefix_reuse_requested', 'cache_prompt')
    profiles = []
    if len(proposals['profiles']) > 3:
        raise ValueError('More than three coding proposals')
    if proposals['specialist_plan']['GPU_allowed'] is not False or proposals['specialist_plan']['quality'] != 'NOT MEASURED':
        raise ValueError('GUI specialist feasibility is not GPU qualification')
    for p in proposals['profiles']:
        if p['new_GPU_execution_authorized'] is not False or p['quality_rank'] is not None or p['whole_benchmark_wall_budget_s'] != 900 or set(p['metrics'].values()) != {'NOT MEASURED'} or p['status'] != 'PROPOSED_NOT_GPU_ADMITTED_NOT_DOWNLOADED':
            raise ValueError('Proposal is not an unmeasured, gated whole900s profile')
        g = next((g for g in headers if g['repository'] == p['repository'] and g['revision'] == p['revision'] and g['filename'] == p['filename']), None)
        if g is None or g['published_sha256'] != p['model_sha256'] or g['published_bytes'] != p['bytes']:
            raise ValueError('Proposed artifact does not match inspected GGUF identity')
        row = pick(p, profile_keys); row['engine'] = pick(p['engine'], engine_keys)
        row['runtime'] = pick(p['runtime'], runtime_keys)
        sampler = ('temperature', 'top_p', 'top_k', 'min_p', 'seed', 'repeat_penalty', 'presence_penalty')
        row['runtime']['sampling'] = pick(p['runtime']['sampling'], sampler)
        row['runtime']['environment'] = pick(p['runtime']['environment'], ('GGML_CUDA_GRAPH_OPT', 'GGML_CUDA_O2_WEIGHT_CACHE_MIB'))
        row['request_options'] = pick(p['request_options'], (*sampler, 'model', 'max_tokens', 'cache_prompt', 'stream', 'return_tokens', 'verbose'))
        row['request_options']['chat_template_kwargs'] = pick(p['request_options']['chat_template_kwargs'], ('enable_thinking',))
        row['benchmark'] = pick(p['benchmark'], ('benchmark_id', 'benchmark_revision', 'dataset_split_hash', 'scorer_version', 'required_task_count', 'expected_task_ids_hash'))
        row['metrics'] = dict(p['metrics']); profiles.append(row)
    if [p['repository'] for p in profiles] != a['coding_shortlist']:
        raise ValueError('Research shortlist/proposal order mismatch')
    references = []
    for r in a['references']:
        original = next((run for run in history['runs'] if run['run_id'] == r['run_id']), None)
        if original is None or any(original[k] != r[k] for k in ('runtime_configuration_id', 'audit_hash', 'score_percent', 'solved', 'tasks', 'official_eligible', 'benchmark_identity_id')):
            raise ValueError('Historical reference score/identity changed')
        references.append(pick(r, ('run_id', 'experiment_id', 'model_family_id', 'model_name', 'benchmark_id', 'benchmark_identity_id', 'runtime_configuration_id', 'model_artifact_id', 'solved', 'tasks', 'score_percent', 'official_eligible', 'audit_hash', 'recorded_configuration', 'warning', 'artifact_availability_limit')))
    claims = []
    for c in a['publisher_claims']:
        if c['evidence_class'] != 'PUBLISHER_REPORTED_NOT_LOCAL' or c['official_ranking_eligible'] is not False:
            raise ValueError('Publisher claims cannot enter local rankings')
        claim = pick(c, ('repository', 'benchmark', 'score_percent', 'evidence_class',
                               'official_ranking_eligible', 'settings', 'baseline_score_percent',
                               'publisher_wall_minutes', 'baseline_publisher_wall_minutes',
                               'format_compliance_percent', 'stderr_percent', 'attribution', 'limit'))
        claim['settings'] = pick(c['settings'], ('dataset_revision', 'engine', 'hardware', 'harness',
                                               'max_output', 'presence_penalty', 'quantization', 'sampling',
                                               'scorer_version', 'tasks', 'temperature', 'thinking', 'top_k', 'top_p'))
        claims.append(claim)
    structure = []
    for repo, shards in cpu['headers'].items():
        structure.append({'repository': repo, 'tensor_count': sum(len(h['tensors']) for h in shards),
                          'parameters': sum(h['parameters'] for h in shards),
                          'dtype_counts': dict(sum((collections.Counter(h['dtype_counts']) for h in shards), collections.Counter())),
                          'header_sha256': [h['header_sha256'] for h in shards]})
    result = pick(a, ('research_id', 'at_utc', 'status', 'inventory_scope', 'counts', 'requested_six',
                      'coding_shortlist', 'phase_C_gate', 'conclusions', 'source_failures',
                      'scientific_labels', 'source_review_notes', 'coverage_notes'))
    result.update(candidates=candidates, publisher_claims=claims, references=references, proposed_profiles=profiles,
                  cpu_results=cpu_rows, cpu_structure=structure, gguf_headers=headers,
                  cpu_controls=dict(cpu['controls']),
                  cpu_range_receipts=[pick(x, ('repository', 'revision', 'file', 'remote_published_lfs_sha256', 'range', 'bytes', 'sha256')) for x in cpu['range_receipts']],
                  independent_replay=pick(replay, ('status', 'source_audit_sha256', 'raw_fragment_hashes_verified',
                                                   'same_dtype_source_sample_pairs_replayed', 'low_rank_delta_blocks_replayed',
                                                   'numpy_used', 'models_executed', 'full_model_identity_or_quality_proven')),
                  specialist_plan=pick(proposals['specialist_plan'], ('repository', 'status', 'requirements', 'quality', 'GPU_allowed')),
                  storage_review=pick(a['storage_review'], ('observed_at_utc', 'free_bytes', 'shortlist_weights_published_bytes',
                                                           'minimum_free_reserve_bytes', 'fits_at_observed_time', 'download_executed', 'rule')),
                  technical_limits=pick(a['technical_limits'], ('GPU', 'compute_capability', 'device_total_MiB',
                                                               'existing_broker_VRAM_limit_MiB', 'FP16_compute',
                                                               'KV_8K_F16_analytical_bytes', 'KV_estimate_limit',
                                                               'new_models_actual_VRAM', 'MTP', 'max_context')),
                  weight_identity_baseline=dict(a['weight_identity_baseline']), new_GPU_runs=0,
                  model_requests=0, new_full_model_downloads=0, existing_weights_modified_or_deleted=False)
    return result


def render(reviews, docs, labels=None):
    """Generate English research pages; no measured-history or leaderboard writes."""
    import html
    docs = pathlib.Path(docs); labels = labels or {}
    def pretty(value):
        return '```json\n' + json.dumps(value, ensure_ascii=False, indent=2).replace('</', '<\\/') + '\n```\n\n'
    def table(headers, rows):
        def cell(value):
            return str(value if value is not None else 'NOT MEASURED').replace('|', '&#124;').replace('\n', ' ')
        return '| ' + ' | '.join(headers) + ' |\n| ' + ' | '.join('---' for _ in headers) + ' |\n' + ''.join('| ' + ' | '.join(cell(v) for v in row) + ' |\n' for row in rows) + '\n'
    def card(row):
        return '[' + row['repository'] + '](https://huggingface.co/' + row['repository'] + '/blob/' + row['revision'] + '/README.md)'
    def write(name, content):
        p = docs / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(content)
    if not reviews:
        return
    page = '# OmniCoder derivatives: evidence and proposed tests\n\n'
    page += '**Research inventory, not a model leaderboard.** Source publication, CPU weight differences, GPU compatibility and independently measured quality are separate gates. No candidate on this page has a new local GPU benchmark or qualification. [Measured configurations](configuration-comparison.md) retain their original scores and identities.\n\n'
    for r in reviews:
        candidates = {c['repository']: c for c in r['candidates']}
        page += 'Review: `' + r['research_id'] + '` · ' + r['at_utc'] + '. ' + r['inventory_scope'] + '\n\n'
        page += table(['Inventory item', 'Count / meaning'], [
            ['Name-search hits', r['counts']['name_search_hits']],
            ['Distinct inventoried repositories', len(candidates)],
            ['Pinned source metadata files', len(r['sources'])],
            ['Coding proposals', len(r['proposed_profiles'])],
            ['New GPU measurements / quality qualifications', '0 / 0'],
            ['Counter scope', 'Repositories are not trained checkpoints, optimization factors, model challengers or GPU runs. The existing 162 factors and 11 challenger tracks are unchanged.']])
        page += 'The retained **OmniCoder 9B** baseline has byte-identical typed Q6_K payloads across all 427 tensors in the compared mradermacher V1/V2 artifacts, despite different file metadata and hashes. [Original complete comparison](weight-integrity-same-quantizer.md). This finding is specific to those quantized artifacts and does not prove training history for every source release. New derivative names and different file hashes are never sufficient evidence of a new fine-tune.\n\n'
        page += '## Coding shortlist — research priority only\n\nNo quality ordering is established. Readiness, provenance, coding relevance and additional information per bounded experiment determine this order. No model should be rejected on an unmeasured quality claim or an output-format/configuration mistake.\n\n'
        page += table(['Priority', 'Pinned Q6 artifact', 'Why investigate', 'Local quality / cost'], [[p['research_priority_rank'], card(candidates[p['repository']]), p['reason'], 'NOT MEASURED'] for p in r['proposed_profiles']])
        page += '[Complete repository inventory](model-research/omnicoder-inventory.md) · [Proposed configurations and gated test plan](model-research/omnicoder-proposals.md)\n\n'
        page += '## Six requested seed models\n\n'
        for name in r['requested_six']:
            c = candidates[name]
            page += '### ' + name + '\n\n' + card(c) + ' · revision `' + c['revision'] + '` · ' + c['kind'] + ' · license: ' + str(c['license'] or 'UNRESOLVED') + '.\n\n'
            page += '**Decision:** ' + c['decision'] + '. ' + c['reason'] + '\n\n'
            page += 'Method evidence: `' + str(c.get('method_evidence', 'NOT RECORDED')) + '`. Exact historical training/base revision: ' + str(c.get('original_training_base_revision') or 'NOT RECORDED') + '. Published base tags are not historical training provenance.\n\n'
        page += '## Locally observed CPU weight evidence\n\n**LOKAL GEMESSEN / LOCALLY MEASURED, CPU ONLY.** Matching BF16 source samples differ for Claude-distill, Nexus upstream and HDL; nonzero low-rank products are observed in three adapters. These observations disprove identity at the probed positions. A conversion or rounding round trip can also change same-dtype values: a difference alone proves neither training history nor quality. Unchanged sampled positions cannot establish full-model identity. The inspected GGUF headers are not quantized-payload comparisons or complete-file SHA verification. Small source changes can disappear under quantization.\n\n'
        page += table(['Source / adapter', 'Bounded observation', 'Compared scope', 'Limit'], [[x['repository'], x['classification'], sum(p.get('compared_values', p.get('effective_delta_probed_cells', 0)) for p in x['pairs']), 'Not a complete tensor census; no quality claim'] for x in r['cpu_results']])
        page += 'The independent standard-library replay checked ' + str(r['independent_replay']['raw_fragment_hashes_verified']) + ' fragment hashes, ' + str(r['independent_replay']['same_dtype_source_sample_pairs_replayed']) + ' source-sample pairs and ' + str(r['independent_replay']['low_rank_delta_blocks_replayed']) + ' low-rank blocks. Numerical probes and structural summaries are available in the public benchmark register; raw weight fragments, templates and foreign code are not redistributed.\n\n'
        page += table(['Source', 'Header tensor count', 'Parameter count in source headers', 'Dtypes'], [[x['repository'], x['tensor_count'], x['parameters'], x['dtype_counts']] for x in r['cpu_structure']])
        page += '## V100 and deployment compatibility\n\n'
        page += table(['Selected GGUF', 'Architecture / layers', 'Tensor formats', 'MTP tensors', 'Actual GPU load / VRAM'], [[x['repository'], str(x['architecture']) + ' / ' + str(x['layers']), x['type_counts'], x['MTP_tensors'], 'NOT MEASURED'] for x in r['gguf_headers']])
        page += pretty(r['technical_limits'])
        page += 'All three inspected text GGUFs have 427 tensors (250 Q6_K, 177 F32), 32 layers and no MTP-named tensors. Declared 262144 context is metadata, not established usable capacity on 16GB. Selected Q6 artifacts are about 7.36GB on disk; **file size is not peak VRAM**. FP16 compute and compatible quantized weights are the intended SM70 route; no native BF16/FP8/FP4 Tensor Core assumption. External MTP needs its own tokenizer/state/acceptance/quality qualification for each target.\n\n'
        page += 'The GUI adapter has no vision-named adapter tensors; this does not disprove multimodality, because a frozen visual tower can be reused. It also does not demonstrate an executable screenshot path. Exact raw-base versus Vision-SFT-substrate composition, image processor, vision tower, merge/key mapping and matching projector remain unresolved. Text GGUF alone does not read screenshots. HDL remains a domain specialist without an established local HDL score.\n\n'
        page += '## Published claims — external, not our benchmark results\n\n**EXTERN BELEGT** here means the publisher statement is traceable to a pinned card; the stated training execution and benchmark quality are not independently reproduced. Missing revisions, scorers and task identities prevent direct comparison. Copied parent-model tables are not attributed as child-model measurements. No value below enters the official local leaderboard or the user-selected local average.\n\n'
        page += table(['Publisher model / source', 'Reported evaluation', 'Score %', 'Baseline % if stated', 'Tasks', 'Known limits'], [[card(candidates[x['repository']]) if x['repository'] in candidates else x['repository'], x['benchmark'], x['score_percent'], x.get('baseline_score_percent'), x['settings'].get('tasks'), x.get('attribution', x.get('limit', 'Publisher protocol; see exact settings below'))] for x in r['publisher_claims']])
        page += '<details><summary>Exact publisher settings and missing protocol fields</summary>\n\n' + pretty(r['publisher_claims']) + '</details>\n\n'
        page += 'Tessera reports less output with lower LiveCodeBench/IFEval scores; efficiency is a quality tradeoff, not a free gain. Slopus reports shorter reasoning under a small custom GSM8K protocol, with a lower thinking score than its stated baseline. These workloads, hardware and scorers do not establish superiority on this V100. Neither a merge of strong parents nor a distillation title proves additive capabilities or teacher provenance.\n\n'
        page += '## Existing measured references\n\nThese unchanged records supply context, **not a controlled comparison** with the unmeasured proposals. Historical templates, sampling, output limits, MTP and weights differ. R217 also uses a derived artifact whose current availability is limited; preserve its audit and disclose reconstruction requirements.\n\n'
        page += table(['Model', 'Experiment / immutable configuration', 'HumanEval+ under recorded local protocol', 'Audit SHA256'], [[labels.get(x['model_family_id'], x['model_name']), '[' + x['experiment_id'] + '](configuration-profiles/' + x['runtime_configuration_id'] + '.md)', str(x['solved']) + '/' + str(x['tasks']), '`' + x['audit_hash'] + '`'] for x in r['references']])
        page += '## Decisions for Jarvis\n\n' + '\n\n'.join('**' + k.replace('_', ' ') + ':** ' + v for k, v in r['conclusions'].items()) + '\n\n'
        page += '**NICHT VERIFIZIERT / NOT VERIFIED:** a local coding, agent, native-tool, German-conversation, memory, latency or energy advantage for any new derivative. Retain the qualified deployed baseline; assess model switching only after successful tasks and GPU-J/success are actually measured. No production changes.\n\n'
        page += '## Provenance and reproduction\n\n' + table(['Evidence', 'SHA256'], [[x['kind'], '`' + x['sha256'] + '`'] for x in r['evidence']])
        page += 'Original review: [audit](audits/' + r['evidence'][0]['audit_id'] + '.md). Public metadata, source-receipt hashes, numerical summaries and proposals are under `candidate_research` in [benchmark-register.json](https://github.com/Maxxxel/v100-volta-ai-optimization-lab/blob/main/data/benchmark-register.json). The originals and raw fragments remain retained locally. No raw model data or model-repository program is executed or exported. Every inventory row links a revision-pinned model card; the register also pins metadata/card/config hashes.\n\n'
        page += 'To reproduce the bounded numerical probe, retrieve the revision-pinned safetensors headers and inclusive HTTP byte ranges in `cpu_range_receipts`, verify each SHA256, and resolve tensor offsets from the headers. Compare the first 256 row-major scalar values of each listed full-model tensor pair. Decode little-endian BF16 by shifting each unsigned16-bit word left 16 bits and interpreting it as float32; compute differences and RMSE in float64. Adapter probes multiply the first 8 rows of B by the first 16 columns of A in float64; the reported product is **unscaled**, with alpha/r supplied separately by the pinned adapter config. No model or repository code is executed. This is a bounded probe, not a complete identity test.\n\n'
        if r['source_failures']:
            page += 'Unavailable originals: ' + '; '.join(x['url'] + ' — HTTP' + str(x['status']) + ': ' + x['meaning'] for x in r['source_failures']) + '\n\n'
        inventory = '# OmniCoder derivative repository inventory\n\n[Research decisions](../omnicoder-derivatives.md). Quantization exports and reuploads are repositories, not independent trained models. Publication/license fields are declarations, not inferred permission. All new local quality/performance cells are NOT MEASURED.\n\n'
        inventory += table(['Repository / pinned card', 'Kind', 'License', 'Quantizations', 'Decision'], [[card(c), c['kind'], c['license'] or 'UNRESOLVED', ', '.join(c['GGUF_quantizations_available']) or 'NONE RECORDED', c['decision']] for c in r['candidates']])
        for c in r['candidates']:
            inventory += '<details><summary>' + html.escape(c['repository']) + '</summary>\n\n' + pretty(c) + '</details>\n\n'
        write('model-research/omnicoder-inventory.md', inventory)
        proposed = '# Proposed OmniCoder derivative test profiles\n\n[Research decisions](../omnicoder-derivatives.md). **PROPOSED, NOT EXECUTED OR GPU-ADMITTED.** No profile here is inserted into the measured configuration history. Separate user approval is mandatory before new derivative GPU trials.\n\nAfter any future pinned download, verify the complete file SHA256 and compare quantized tensor payloads against the retained baseline before attributing a result to changed weights. A source BF16 difference is not proof that the selected quantized export retains that difference. Identical weights with a different template are a template/profile comparison, not a newly trained-model result.\n\nThe 900-second budget covers the whole benchmark, all parts, startup, retries, evaluation phases and cleanup. The trusted broker migration is still required; the old per-job contract must not be bypassed or reset. A full benchmark score requires every official task and evaluator to finish. An interrupted run is PARTIAL, not a zero score, a complete benchmark or grounds to reject the model. No task-selected output/sampling tuning on official tests.\n\n'
        proposed += 'At most three coding candidates are proposed. Use pinned native templates and explicit thinking controls; requested FA, graph, MTP and cache controls do not prove the executed paths. Actual VRAM, quality and energy remain unmeasured. Historical reference settings differ and cannot support a causal improvement claim. Standard full benchmarks are the target; no small private quality pre-screen is used to discard a candidate.\n\n'
        for p in r['proposed_profiles']:
            proposed += '## Priority ' + str(p['research_priority_rank']) + ' — ' + p['repository'] + '\n\n' + pretty(p)
        proposed += '## GUI specialist — separate feasibility gate\n\n' + pretty(r['specialist_plan'])
        proposed += '## Storage snapshot, not a reservation\n\n' + pretty(r['storage_review'])
        write('model-research/omnicoder-proposals.md', proposed)
    write('omnicoder-derivatives.md', page)


def collect(root, item, history, receipt):
    root = pathlib.Path(root).resolve()
    def pinned(relative, expected):
        p = (root / relative).resolve()
        if not p.is_relative_to(root) or not p.is_file() or digest(p) != expected:
            raise ValueError('Derivative research evidence changed or escaped source root')
        return p
    ap = pinned(item['audit_path'], item['audit_sha256']); a = json.loads(ap.read_text())
    linked = {}
    for prefix in ('query_receipt', 'CPU_audit', 'GGUF_audit', 'profiles', 'CPU_replay'):
        p = pinned(a[prefix + '_path'], a[prefix + '_sha256'])
        linked[prefix] = json.loads(p.read_text())
    for source in a['sources']:
        p = pinned(source['path'], source['sha256'])
        if p.stat().st_size != source['bytes']:
            raise ValueError('Research source byte count mismatch')
    cpu = linked['CPU_audit']
    pinned(str((ap.parent / 'CPU_INTEGRITY_PLAN.json').relative_to(root)), cpu['plan_sha256'])
    pinned(str((ap.parent / 'cpu_integrity.py').relative_to(root)), cpu['script_sha256'])
    for fragment in cpu['range_receipts']:
        p = (ap.parent / 'cpu-integrity' / fragment['private_fragment']).resolve()
        if not p.is_relative_to((ap.parent / 'cpu-integrity').resolve()) or digest(p) != fragment['sha256'] or p.stat().st_size != fragment['bytes']:
            raise ValueError('CPU fragment evidence changed')
    result = projection(a, linked['CPU_audit'], linked['CPU_replay'], linked['GGUF_audit'], linked['profiles'], history)
    result['evidence'] = [{'kind': 'research_audit', 'sha256': item['audit_sha256'], 'audit_id': receipt(ap, item['audit_sha256'])}]
    # Receipt summaries contain no raw model fragments or foreign source code.
    for prefix in ('CPU_audit', 'GGUF_audit', 'profiles', 'CPU_replay'):
        result['evidence'].append({'kind': prefix, 'sha256': a[prefix + '_sha256']})
    result['sources'] = [{'file': str(pathlib.Path(s['path']).relative_to(ap.parent.relative_to(root))),
                          'sha256': s['sha256'], 'bytes': s['bytes']} for s in a['sources']]
    from validate import content_errors
    errors = content_errors(json.dumps(result, ensure_ascii=False))
    if errors:
        raise ValueError('Derivative public projection failed content scan: ' + ', '.join(errors))
    return result
