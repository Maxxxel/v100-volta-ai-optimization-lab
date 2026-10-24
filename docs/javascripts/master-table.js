/* Offline configuration explorer. Pure calculations are shared with Node tests. */
(function (root) {
  'use strict';
  const UNKNOWN = 'NICHT ERFASST';
  const NOT_MEASURED = 'NICHT GEMESSEN';
  // Evaluation cutoffs describe which answers were collected, not how the
  // model generated them. Keep them in original profiles/result evidence.
  const measurementRuntimeFields = new Set(['benchmark_task_limit_s', 'timing_scope',
    'startup_limit_s', 'GPU_wrapper_limit_s', 'CPU_scoring_limit_s', 'native_HTTP_timeout_policy']);
  const measurementRuntimePath = key => key.startsWith('runtime.') && measurementRuntimeFields.has(key.slice(8));
  const summaryMetrics = [
    ['decode_tok_s','Decode tok/s','Gemeldete Decode-Token / gemeldete Decode-Zeit; über die ausgewählten vollständigen Benchmarks gepoolt.'],
    ['wall_per_task_s','Ø Latenz s/Aufgabe','Summe der vollständigen Anfragezeiten / Aufgaben. Modellstart, Warmup und CPU-Auswertung sind nicht enthalten.'],
    ['output_tokens_per_task','Ø Output-Token/Aufgabe','Gemeldete Engine-Output-Token / Aufgaben, einschließlich gemeldeter Reasoning-Token. Tokenizer unterscheiden sich zwischen Modellen.'],
    ['energy_j_per_success','GPU J/Erfolg','Gemessene GPU-Energie / Erfolge einschließlich fehlgeschlagener Aufgaben. Zählerbereiche bleiben Bereiche; Sortierung nach oberer Grenze.'],
    ['peak_vram_gib','Peak-VRAM GiB','Höchster gemessener Session-Peak der ausgewählten Benchmarks; kein Durchschnitt.']
  ];
  const finite = x => typeof x === 'number' && Number.isFinite(x);
  const absent = x => x === null || x === undefined;
  const unrecordedMetadata = x => absent(x) || x === 'NOT MEASURED' || x === UNKNOWN;
  const canonical = x => JSON.stringify(x === undefined ? null : x, function (k, v) {
    return v && typeof v === 'object' && !Array.isArray(v)
      ? Object.fromEntries(Object.keys(v).sort().map(key => [key, v[key]])) : v;
  });
  function flatten(value, prefix = '', out = {}) {
    if (value && typeof value === 'object' && !Array.isArray(value) && Object.keys(value).length) {
      Object.keys(value).sort().forEach(key => flatten(value[key], prefix ? prefix + '.' + key : key, out));
    } else if (prefix) out[prefix] = value;
    return out;
  }
  function parameters(profile) {
    const out = flatten(profile);
    const speculation = profile.optimizations?.speculation_type;
    out['requested.MTP'] = speculation === 'draft-mtp' ? true : speculation === 'none' ? false : null;
    const kwargs = profile.runtime?.native_template_controls;
    out['requested.thinking'] = typeof kwargs?.enable_thinking === 'boolean' ? kwargs.enable_thinking : null;
    out['requested.thinking_level'] = kwargs?.reasoning_effort ?? profile.runtime?.thinking_level ?? null;
    out['requested.reasoning_budget'] = kwargs?.thinking_budget ?? profile.runtime?.reasoning_budget_tokens ?? null;
    const argv = profile.start_parameters?.argv || [];
    for (let i = 0; i < argv.length; i++) {
      if (typeof argv[i] !== 'string' || !argv[i].startsWith('--')) continue;
      const name = 'launch_flags.' + argv[i], values = [];
      while (i + 1 < argv.length && !String(argv[i + 1]).startsWith('--')) values.push(argv[++i]);
      const value = values.length === 0 ? true : values.length === 1 ? values[0] : values;
      if (Object.hasOwn(out, name)) out[name] = [out[name], value]; else out[name] = value;
    }
    return out;
  }
  const required = [
    'model.parameter_count', 'model.qat', 'model.svd', 'model.hf_repository', 'model.hf_revision',
    'engine.version', 'engine.git_commit', 'engine.fork_repository', 'engine.cuda_version', 'engine.driver_version',
    'engine.executed_kernel_backend_path', 'runtime.thinking_level', 'runtime.reasoning_budget_tokens',
    'optimizations.speculation_effective', 'optimizations.flash_attention_effective'
  ];
  const labels = {
    'evidence.execution_status': 'Ausführungsnachweis', 'engine.reported_build_number': 'Buildnummer (Startlog)',
    'engine.version_provenance_note': 'Versionsbeleg / Einschränkung',
    'runtime.observed_template_controls.enable_thinking': 'Thinking (beobachtete Anfrage)',
    'model.name': 'Modell', 'model.historical_name': 'Historische Modellbezeichnung', 'model.identity_annotation': 'Beleg zur Modellidentität', 'model.family_id': 'Modellfamilie', 'model.quantization': 'Quantisierung',
    'model.parameter_count': 'Parameterzahl', 'model.qat': 'QAT', 'model.svd': 'SVD',
    'model.hf_repository': 'Hugging Face', 'model.hf_revision': 'Modellrevision',
    'model.artifact_sha256': 'Modell SHA256', 'engine.name': 'Engine', 'engine.version': 'Engine-Version / Quellstand',
    'engine.git_commit': 'Engine-Commit', 'engine.build_id': 'Build-ID', 'engine.binary_sha256': 'Binary SHA256',
    'engine.source_base_commit': 'Belegter Engine-Basiscommit', 'engine.source_version_label': 'Belegter Engine-Quellstand',
    'engine.cuda_version': 'CUDA-Version', 'engine.driver_version': 'Treiber',
    'engine.executed_kernel_backend_path': 'Kernelpfad (nachgewiesen)',
    'runtime.context': 'Kontext', 'runtime.max_output': 'Output-Limit',
    'runtime.thinking_reasoning_requested': 'Reasoning-Parser (angefordert)', 'runtime.thinking_level': 'Thinking-Level (Rohfeld)',
    'requested.MTP': 'MTP (angefordert)', 'requested.thinking': 'Thinking (Template explizit)',
    'model.historical_variant_label': 'Historische Profilbeschreibung (korrigiert)',
    'model.variant_correction': 'Beleg zur Profilbeschreibung',
    'requested.thinking_level': 'Thinking-Level (explizit)', 'requested.reasoning_budget': 'Reasoning-Budget (explizit)',
    'runtime.reasoning_budget_tokens': 'Reasoning-Budget', 'runtime.batch': 'Batch', 'runtime.microbatch': 'Microbatch',
    'runtime.CPU_threads': 'CPU-Threads', 'runtime.GPU_offload': 'GPU-Offload', 'runtime.power_limit_w': 'Power-Limit W',
    'optimizations.speculation_type': 'Spekulation (angefordert)',
    'optimizations.speculation_effective': 'Spekulation (nachgewiesen)',
    'optimizations.flash_attention_requested': 'Flash Attention (angefordert)',
    'optimizations.flash_attention_effective': 'Flash Attention (nachgewiesen)',
    'optimizations.cuda_graphs.actual_capture_replay': 'CUDA Graphs (nachgewiesen)',
    'optimizations.HBM_conversion_weight_cache_limit_mib': 'HBM-Cache-Limit MiB (angefordert)',
    'optimizations.KV_precision.k': 'KV K (angefordert)', 'optimizations.KV_precision.v': 'KV V (angefordert)',
    'optimizations.prefix_reuse': 'Prefix-Reuse', 'optimizations.GDN_state_changes': 'GDN-State',
    'optimizations.draft_head_or_model': 'Draft-Modell / Head', 'optimizations.draft_parameters.--spec-draft-n-max': 'Draft-Tokens max'
  };
  const text = x => absent(x) ? UNKNOWN : typeof x === 'object' ? canonical(x) : String(x);
  const category = key => measurementRuntimePath(key) ? 'Evaluationsbedingungen (je Lauf)' : key.startsWith('recorded_plan.') ? 'Planparameter (deklariert, hashgebunden)' : key.startsWith('model.') ? 'Modell' : key.startsWith('engine.') ? 'Engine'
    : key.startsWith('runtime.') ? 'Kontext und Inferenz' : /^(optimizations|requested)\./.test(key) ? 'Optimierungen'
    : /^(start_parameters|launch_flags)\./.test(key) ? 'Startparameter und Flags' : 'Identitäten und Herkunft';
  const uniqueRuns = runs => {
    const groups = new Map();
    runs.forEach(run => {
      const key = canonical([run.audit_hash, run.experiment_id, run.runtime_configuration_id,
        run.benchmark_identity_id, run.dataset_split_hash, run.evaluated_task_set_hash, run.scorer_version]);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(run);
    });
    let conflict = false;
    const records = [...groups.values()].map(group => {
      if (new Set(group.map(r => canonical([r.score_percent, r.solved, r.tasks]))).size !== 1) conflict = true;
      // Later audit views can add a separately verified counter supplement to
      // the same physical observation. Keep one sample and every source ID.
      const counters = group.filter(r => r.counter_energy);
      if (!counters.length) return group[0];
      const record = { ...group[0], audit_ids: [...new Set(group.flatMap(r => r.audit_ids || []))],
        measurement_view_run_ids: group.map(r => r.run_id) };
      if (new Set(counters.map(r => canonical(r.counter_energy))).size === 1) record.counter_energy = counters[0].counter_energy;
      else { record.counter_energy = null; record.counter_energy_conflict = true; }
      return record;
    });
    return { records, conflict };
  };
  function aggregate(runs) {
    const unique = uniqueRuns(runs), records = unique.records;
    const protocols = new Set(records.map(r => canonical([r.benchmark_id, r.benchmark_identity_id,
      r.benchmark_revision, r.dataset_split_hash, r.evaluated_task_set_hash, r.scorer_version, r.tasks, r.metric])));
    const invalid = records.some(r => !Number.isInteger(r.tasks) || r.tasks <= 0 || !Number.isInteger(r.solved)
      || r.solved < 0 || r.solved > r.tasks || !finite(r.score_percent)
      || Math.abs(r.score_percent - 100 * r.solved / r.tasks) > 1e-8);
    const configs = new Set(records.map(r => r.comparison_configuration_id || r.runtime_configuration_id));
    const conflict = unique.conflict || protocols.size > 1 || configs.size > 1 || invalid;
    const scores = records.map(r => r.score_percent);
    if (!records.length || conflict || scores.some(x => !finite(x))) return { score: null, n: records.length, conflict, records };
    const score = scores.reduce((a, b) => a + b, 0) / scores.length;
    return { score, n: records.length, conflict: false, records,
      solved: records.reduce((n, r) => n + r.solved, 0), tasks: records.reduce((n, r) => n + r.tasks, 0),
      min: Math.min(...scores), max: Math.max(...scores),
      sd: scores.length > 1 ? Math.sqrt(scores.reduce((n, x) => n + (x - score) ** 2, 0) / (scores.length - 1)) : null };
  }
  function average(scores, selected, official = true, columns = new Map()) {
    if (!selected.length) return null;
    const families = selected.map(key => columns.get(key)?.aggregation_family_id || columns.get(key)?.family_id || key);
    if (new Set(families).size !== selected.length) return null;
    const configurations = new Set(selected.flatMap(key => scores[key]?.records.map(r => r.comparison_configuration_id || r.runtime_configuration_id) || []));
    if (configurations.size !== 1 || [...configurations].some(id => typeof id !== 'string' || !id)) return null;
    const values = selected.map(key => {
      if (official && columns.get(key)?.scope !== 'OFFICIAL_LOCAL') return null;
      const a = scores[key];
      if (!a || a.conflict || !finite(a.score) || official && a.records.some(r => r.official_eligible !== true)) return null;
      return a.score;
    });
    return values.some(x => x === null) ? null : values.reduce((a, b) => a + b, 0) / values.length;
  }
  function measuredValue(a, path) {
    if (!a?.records.length) return null;
    if (path.startsWith('counter_energy.') && a.records.some(r => r.counter_energy_conflict)) return null;
    const values = a.records.map(r => flatten(r)[path]);
    if (values.every(absent)) return null;
    if (values.every(finite)) return values.reduce((n, x) => n + x, 0) / values.length;
    const unique = [...new Map(values.map(v => [canonical(v), v])).values()];
    return unique.length === 1 ? unique[0] : values;
  }
  function performanceSummary(row, selected, benchmarkMap) {
    const empty={decode_tok_s:null,wall_per_task_s:null,output_tokens_per_task:null,energy_j_per_success:null,peak_vram_gib:null};
    const keys=[...selected],groups=keys.map(key=>row.scores[key]);
    const families=keys.map(key=>benchmarkMap.get(key)?.family_id);
    if(!keys.length||new Set(families).size!==keys.length||families.some(absent)
      ||groups.some(a=>!a?.n||a.conflict))return {...empty,status:'MISSING_SELECTED_BENCHMARK'};
    const records=groups.flatMap(a=>a.records);
    const configs=new Set(records.map(r=>r.comparison_configuration_id||r.runtime_configuration_id));
    if(configs.size!==1||[...configs].some(id=>typeof id!=='string'||!id)||records.some(r=>r.official_eligible!==true||r.status==='PARTIAL')
      ||keys.some((key,i)=>{const b=benchmarkMap.get(key);return b.scope!=='OFFICIAL_LOCAL'||groups[i].records.some(r=>r.tasks!==b.definition.required_task_count);}))
      return {...empty,status:'INCOMPATIBLE_OR_INCOMPLETE'};
    const physical=records.map(r=>canonical([r.audit_hash||r.run_id,r.runtime_configuration_id,r.benchmark_identity_id]));
    if(new Set(physical).size!==records.length)return {...empty,status:'DUPLICATE_OBSERVATION'};
    const tasks=records.reduce((n,r)=>n+r.tasks,0),solved=records.reduce((n,r)=>n+r.solved,0);
    const result={...empty,status:'COMPLETE_SELECTED_BASIS',tasks,solved,observations:records.length,
      benchmark_count:keys.length,basis:keys.map(key=>({key,protocol:benchmarkMap.get(key).protocol})),
      runs:records.map(r=>({run_id:r.run_id,experiment_id:r.experiment_id,runtime_configuration_id:r.runtime_configuration_id,
        audit_hash:r.audit_hash,audit_ids:r.audit_ids,measurement_conditions:r.measurement_conditions,timing_provenance:r.timing_provenance}))};
    const covered=records.every(r=>absent(r.measurement_conditions?.performance_tasks)||r.measurement_conditions.performance_tasks===r.tasks);
    const sum=key=>records.reduce((n,r)=>n+r[key],0);
    if(covered&&records.every(r=>Number.isInteger(r.decode_tokens)&&r.decode_tokens>=0)){
      result.output_tokens=sum('decode_tokens');result.output_tokens_per_task=result.output_tokens/tasks;
      if(records.every(r=>finite(r.decode_engine_ms)&&r.decode_engine_ms>=0)&&sum('decode_engine_ms')>0){
        result.decode_engine_ms=sum('decode_engine_ms');result.decode_tok_s=1000*result.output_tokens/result.decode_engine_ms;
      }
    }
    if(covered&&records.every(r=>finite(r.wall_s)&&r.wall_s>=0)){
      result.wall_s=sum('wall_s');result.wall_per_task_s=result.wall_s/tasks;
    }
    if(records.every(r=>finite(r.peak_vram_mib)&&r.peak_vram_mib>=0))result.peak_vram_gib=Math.max(...records.map(r=>r.peak_vram_mib))/1024;
    const counters=covered&&records.every(r=>!r.counter_energy_conflict&&r.counter_energy?.method==='NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1'
      &&r.counter_energy.tasks===r.tasks&&r.counter_energy.solved===r.solved&&finite(r.counter_energy.lower_j)&&finite(r.counter_energy.upper_j)
      &&r.counter_energy.lower_j>=0&&r.counter_energy.upper_j>=r.counter_energy.lower_j);
    if(counters&&solved>0){
      const lower=records.reduce((n,r)=>n+r.counter_energy.lower_j,0)/solved,upper=records.reduce((n,r)=>n+r.counter_energy.upper_j,0)/solved;
      result.energy={lower,upper,method:'NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1',sorting:'upper_bound',scope:'GPU only; request groups include failures/setup, exclude model loading/warmup/CPU/system energy. Query-time brackets, not statistical confidence intervals.'};
      result.energy_j_per_success=upper;
    }else if(covered&&solved>0&&records.every(r=>finite(r.gpu_j)&&r.gpu_j>=0)){
      const value=sum('gpu_j')/solved;result.energy={lower:value,upper:value,method:'STORED_COMPLETE_GPU_ENERGY',sorting:'recorded_value',scope:'Original recorded full-task GPU energy; source conditions remain attached.'};result.energy_j_per_success=value;
    }else result.energy_status=solved===0?'NO_SUCCESSES':'MISSING_OR_MIXED_ENERGY_METHODS';
    return result;
  }
  function availableAverage(row,state,benchmarkMap){
    const groups=new Map();
    benchmarkMap.forEach(b=>{if(!groups.has(b.family_id))groups.set(b.family_id,[]);groups.get(b.family_id).push(b);});
    const values=[],keys=[],records=[];let total=0;
    groups.forEach((protocols,id)=>{
      if(state.visible&&!state.visible.has('family:'+id))return;
      total++;
      const result=resolvedScore(row,{kind:'family',family:{id,protocols}},state,benchmarkMap),a=result.a,b=result.benchmark;
      if(!a?.n||a.conflict||!finite(a.score)||b?.scope!=='OFFICIAL_LOCAL'
        ||a.records.some(r=>r.official_eligible!==true||r.status==='PARTIAL'||r.tasks!==b.definition.required_task_count))return;
      values.push(a.score);keys.push(result.key);records.push(...a.records);
    });
    const configs=new Set(records.map(r=>r.comparison_configuration_id||r.runtime_configuration_id));
    const valid=configs.size===1&&![...configs].some(id=>typeof id!=='string'||!id);
    return {score:values.length&&valid?values.reduce((n,x)=>n+x,0)/values.length:null,count:values.length,total,keys,
      policy:'Arithmetic mean of available displayed complete qualified category scores; missing categories excluded, never zero. Same evidenced inference configuration only.'};
  }
  function build(data) {
    const benchmarks = data.master.benchmark_columns, benchmarkMap = new Map(benchmarks.map(b => [b.key, b]));
    const measuredIds = new Set(data.history.runs.map(r => r.runtime_configuration_id));
    const archive = data.history.profiles.filter(p => !measuredIds.has(p.runtime_configuration_id));
    const rows = data.history.profiles.filter(p => measuredIds.has(p.runtime_configuration_id)).map(profile => {
      const runs = data.history.runs.filter(r => r.runtime_configuration_id === profile.runtime_configuration_id).map(original => {
        if (Object.hasOwn(original, 'comparison_configuration_id')) throw new Error('Reserved presentation identity in original run');
        const run = { ...original };
        const diagnosis = (data.register.archived_diagnostics || []).find(d => d.experiment_id === run.experiment_id);
        if (diagnosis) run.archived_diagnostic = { audit_id: diagnosis.audit_id, weight_provenance_audit_id: diagnosis.weight_provenance_audit_id, weight_identity_status: diagnosis.weight_provenance.next_decision, report: 'oxcoder-diagnostic' };
        (data.history.measurement_evidence || []).filter(e => e.run_id === run.run_id).forEach(e => {
          if (e.runtime_configuration_id !== run.runtime_configuration_id) throw new Error('Timing evidence/profile mismatch');
          Object.entries(e.values).forEach(([key, v]) => { if (!absent(run[key]) && canonical(run[key]) !== canonical(v)) throw new Error('Conflicting measured evidence: ' + key); run[key] = v; });
          run.timing_provenance = { evidence_id: e.evidence_id, sources: e.sources, aggregation: e.aggregation };
        }); return run;
      });
      const attempts = data.history.attempts.filter(r => r.runtime_configuration_id === profile.runtime_configuration_id);
      const values = parameters(profile), scores = {};
      const evidence = (data.history.configuration_evidence || []).filter(e => e.runtime_configuration_id === profile.runtime_configuration_id);
      evidence.forEach(e => Object.entries(e.fields).forEach(([key, v]) => {
        if (!unrecordedMetadata(values[key]) && canonical(values[key]) !== canonical(v)) throw new Error("Conflicting configuration evidence: " + key);
        values[key] = v;
      }));
      const identityLabel = (data.register.model_label_annotations || []).find(a => a.artifact_sha256 === profile.model.artifact_sha256);
      if (identityLabel) {
        values['model.historical_name'] = profile.model.name;
        values['model.name'] = identityLabel.display_name;
        values['model.identity_annotation'] = identityLabel;
      }
      const familyLabel = data.register.model_family_labels?.[profile.model.family_id];
      if (familyLabel) { values['model.historical_name'] = profile.model.name; values['model.name'] = familyLabel; }
      const corrections = (data.register.profile_label_reviews || []).flatMap(review => review.corrections.map(c => ({ ...c, audit_id: review.audit_id })))
        .filter(c => c.runtime_configuration_id === profile.runtime_configuration_id);
      if (corrections.length > 1) throw new Error('Ambiguous profile-description correction');
      if (corrections.length) {
        const c = corrections[0];
        if (c.model_artifact_sha256 !== profile.model.artifact_sha256 || c.original_descriptive_label !== profile.model.variant || c.checkpoint_variant !== null || c.classification !== 'COPIED_RUN_DESCRIPTION_NOT_CHECKPOINT_OR_TUNING_EVIDENCE') throw new Error('Unbound profile-description correction');
        values['model.historical_variant_label'] = profile.model.variant;
        values['model.variant'] = null;
        values['model.variant_correction'] = c;
      }
      const sourceReviews = (data.register.engine_source_reviews || []).flatMap(review => review.engines.map(engine => ({ ...engine, audit_id: review.audit_id, audit_sha256: review.audit_sha256 })));
      const source = sourceReviews.find(e => e.build_id === profile.engine.build_id && e.binary_sha256 === profile.engine.binary_sha256 && e.kernel_library_sha256 === profile.engine.kernel_library_sha256);
      if (source) {
        values['engine.source_base_commit'] = source.source_base_commit;
        values['engine.source_version_label'] = source.source_version_label;
        values['engine.source_evidence'] = source;
      }
      values["evidence.metadata_receipts"] = evidence.map(e => ({ evidence_id: e.evidence_id, sources: e.sources }));
      benchmarks.forEach(b => { scores[b.key] = aggregate(runs.filter(r => data.master.run_columns[r.run_id] === b.key)); });
      const paths = new Set(attempts.flatMap(a => Object.keys(flatten(a.lab_metrics || {}))));
      paths.forEach(path => {
        values['attempt_metrics.' + path] = attempts.filter(a => !absent(flatten(a.lab_metrics || {})[path]))
          .map(a => ({ experiment: a.experiment_id, value: flatten(a.lab_metrics || {})[path] }));
      });
      values['evidence.execution_status'] = [...new Set(attempts.map(a => a.execution_status))];
      values['evidence.scientific_status'] = [...new Set(attempts.map(a => a.scientific_status))];
      values['evidence.experiments'] = [...new Set([...runs, ...attempts].map(a => a.experiment_id))];
      return { id: profile.runtime_configuration_id, profile, displayName: values['model.name'], runs, attempts, values, scores };
    });
    const paths = new Set([...required, ...rows.flatMap(r => Object.keys(r.values))]);
    paths.delete('evidence.experiments'); // Run provenance belongs to its score, never a configuration column.
    const columns = [...paths].sort().map(path => ({ key: path, label: labels[path] || path,
      category: path.startsWith('attempt_metrics.') ? 'Labor-Messungen (mit Herkunft)' : category(path), kind: 'parameter' }));
    benchmarks.forEach(b => {
      const suffix = b.scope === 'OFFICIAL_LOCAL' ? 'lokal zugelassen' : b.scope === 'HISTORICAL' ? 'historisch / Teilumfang' : b.scope === 'UNQUALIFIED_FULL' ? 'Vollumfang, noch nicht zugelassen' : b.scope === 'PARTIAL' ? 'PARTIAL / Teilumfang' : 'Laborergänzung';
      columns.push({ key: b.key, label: b.name + ' · ' + suffix + ' · n=' + text(b.protocol.tasks) + ' · ' + b.key.slice(-6),
        shortLabel: b.name + ' · ' + b.key.slice(-6), category: 'Benchmarks', kind: 'benchmark', benchmark: b });
      const fixed = ['prefill_tok_s', 'decode_tok_s', 'ttft_s', 'wall_s', 'gpu_j', 'gpu_j_per_success', 'gpu_j_per_output_token', 'peak_vram_mib', 'repeat_range', 'date', 'status', 'status_reason', 'warning'];
      const extra = rows.flatMap(row => row.runs).filter(r => data.master.run_columns[r.run_id] === b.key)
        .flatMap(r => Object.keys(flatten(r)).filter(k => /prefill|decode|latency|wall|energy|gpu_j|vram|repeat|task_phase|startup_s|timing_provenance|^matched_performance\.|^measurement_conditions\./i.test(k)));
      [...new Set([...fixed, ...extra])].sort().forEach(path => columns.push({ key: 'metric:' + b.key + ':' + path,
        label: (path.startsWith('matched_performance.') ? 'Neue Aufgaben: ' + path.slice('matched_performance.'.length) : path) + ' · ' + b.name + ' · ' + b.scope + ' · Qualität n=' + text(b.protocol.tasks) + ' · ' + b.key.slice(-6), category: 'Performance je Benchmarkprotokoll', kind: 'metric', benchmark: b, path }));
    });
    const groups = new Map();
    benchmarks.forEach(b => {
      const id = b.family_id || b.protocol.benchmark_id;
      if (!groups.has(id)) groups.set(id, { id, name: b.family_name || b.name, key: 'family:' + id, protocols: [] });
      groups.get(id).protocols.push(b);
    });
    const families = [...groups.values()];
    families.forEach(f => columns.push({ key: f.key, label: f.name, category: 'Benchmarkfamilien (gewähltes Protokoll)', kind: 'family', family: f }));
    summaryMetrics.forEach(([path,label,description])=>columns.push({key:'summary:'+path,path,label,description,
      category:'Gemessene Performance · ausgewählte Benchmarks',kind:'summary_metric'}));
    columns.push({ key: 'average', label: 'Ø Benchmarks (%)', description: 'Arithmetischer Schnitt vorhandener vollständiger Kategorie-Ergebnisse; Abdeckung n/3. Kein offizieller Gesamtbenchmark.', category: 'Auswertung', kind: 'average' });
    return { rows, archive, columns, benchmarks, benchmarkMap, families, runColumns: data.master.run_columns,
      comparisonCategories: data.master.comparison_categories };
  }
  function protocols(family, mode) {
    return family.protocols.filter(b => mode === 'official' ? b.scope === 'OFFICIAL_LOCAL' : b.scope !== 'OFFICIAL_LOCAL');
  }
  function defaultProtocol(family, mode = 'all') {
    const options = mode === 'all' ? family.protocols : protocols(family, mode);
    const priority = b => b.scope === 'OFFICIAL_LOCAL' ? 0 : b.scope === 'UNQUALIFIED_FULL' ? 1 : b.scope === 'HISTORICAL' ? 2 : 3;
    // Deterministic protocol choice, independent of a model's score. Never fall
    // back to a different protocol for an individual configuration.
    return options.slice().sort((a, b) => priority(a) - priority(b) || (b.records || 0) - (a.records || 0) || a.key.localeCompare(b.key))[0]?.key || null;
  }
  function protocolKey(column, state) {
    if (column.kind !== 'family') return column.key;
    const key = state.protocols?.get(column.family.id);
    return column.family.protocols.some(p => p.key === key) ? key : null;
  }
  function resolvedScore(row, column, state, benchmarkMap) {
    const chosen = protocolKey(column, state);
    let key = chosen;
    if (column.kind === 'family' && state.allMeasured && !state.officialOnly && !state.strictProtocols?.has(column.family.id)) {
      const candidates = column.family.protocols.filter(b => row.scores[b.key]?.n > 0);
      const priority = b => b.scope === 'OFFICIAL_LOCAL' ? 0 : b.scope === 'UNQUALIFIED_FULL' ? 1 : b.scope === 'PARTIAL' ? 3 : 2;
      // Prefer qualification and coverage, never the largest observed score.
      candidates.sort((a, b) => priority(a) - priority(b) || (b.protocol.tasks || 0) - (a.protocol.tasks || 0) || Number(b.key === chosen) - Number(a.key === chosen) || a.key.localeCompare(b.key));
      if (candidates.length) key = candidates[0].key;
    }
    const benchmark=benchmarkMap.get(key), score=row.scores[key];
    const excluded=state.officialOnly && (benchmark?.scope!=='OFFICIAL_LOCAL' || score?.records.some(r=>r.official_eligible!==true));
    return { key, selectedKey: chosen, benchmark, a:excluded ? undefined : score };
  }
  // A capture ID binds one immutable plan/audit. It is not an inference setting.
  // Only complete broker-native captures can share a presentation row. Original
  // profile/run IDs and exact benchmark identities are never rewritten.
  function configurationKey(row) {
    const p = row.profile, sha = v => typeof v === 'string' && /^[a-f0-9]{64}$/.test(v);
    if (p.source_provenance?.kind !== 'BROKER_NATIVE_CAPTURED_CONFIGURATION'
        || p.incomplete_identity_run || !sha(p.model?.artifact_sha256)
        || !sha(p.engine?.binary_sha256) || !sha(p.engine?.kernel_library_sha256)
        || !sha(p.engine?.build_id) || !sha(p.runtime?.chat_template_sha256)
        || !p.start_parameters?.argv?.length || !p.runtime?.sampling
        || absent(p.runtime.context) || absent(p.runtime.max_output)) return 'capture:' + row.id;
    const copy = { ...p };
    // These fields describe the capture, not model execution. Weight identity is
    // the exact artifact SHA, independent of historical names/profile labels.
    ['runtime_configuration_id', 'model_artifact_id', 'source_plan_sha256',
      'source_provenance', 'evaluation_exposure', 'provenance_status'].forEach(k => delete copy[k]);
    copy.model = { ...p.model };
    ['name', 'family_id', 'variant'].forEach(k => delete copy.model[k]);
    copy.runtime = { ...p.runtime };
    measurementRuntimeFields.forEach(k => delete copy.runtime[k]);
    copy.start_parameters = { ...p.start_parameters };
    ['exact_private_launch_sha256', 'note', 'redacted_argument_positions'].forEach(k => delete copy.start_parameters[k]);
    // A differing observed runtime/engine/optimization field must also prevent
    // a merge, even when it was discovered later in a source-bound receipt.
    const evidence = Object.fromEntries(Object.entries(row.values).filter(([k]) =>
      k !== 'runtime.native_tool_choice_requested' && !measurementRuntimePath(k) && /^(runtime|optimizations)\./.test(k) || /^engine\./.test(k) && !/source_evidence|provenance_note/.test(k)));
    return canonical({ execution: copy, evidence });
  }
  function mergeConfigurations(rows, model) {
    const groups = new Map();
    rows.forEach(row => { const key = configurationKey(row); if (!groups.has(key)) groups.set(key, []); groups.get(key).push(row); });
    // Tool-choice is a benchmark adapter option, absent from coding requests.
    // Conflicting settings among tool runs are distinct profiles, never pooled.
    const compatible = [...groups.values()].flatMap(group => {
      const tools = group.filter(r => r.runs.some(run => run.benchmark_id.startsWith('bfcl-')));
      return new Set(tools.map(r => canonical(r.values['runtime.native_tool_choice_requested']))).size > 1 ? group.map(r => [r]) : [group];
    });
    return compatible.map(members => {
      const first = members[0], ids = members.map(r => r.id), values = {};
      const runs = members.flatMap(r => r.runs.map(run => ({ ...run, comparison_configuration_id: first.id })));
      const paths = new Set(members.flatMap(r => Object.keys(r.values)));
      paths.forEach(key => {
        const entries = members.map(r => ({ runtime_configuration_id: r.id, value: r.values[key] ?? null }));
        values[key] = new Set(entries.map(e => canonical(e.value))).size === 1 ? entries[0].value : entries;
      });
      values['evidence.experiments'] = [...new Set(runs.map(r => r.experiment_id))];
      const scores = Object.fromEntries(model.benchmarks.map(b => [b.key,
        aggregate(runs.filter(r => model.runColumns[r.run_id] === b.key))]));
      return { ...first, memberIds: ids, profiles: members.map(r => r.profile), values, runs,
        attempts: members.flatMap(r => r.attempts), scores };
    });
  }
  function comparisonView(model) {
    // One fixed benchmark per decision category in every comparison preset.
    // The complete immutable ledger remains available outside this view.
    if (!Array.isArray(model.comparisonCategories) || model.comparisonCategories.length !== 3
      || new Set(model.comparisonCategories.map(c=>c.category)).size !== 3) throw new Error('Missing fixed comparison categories');
    const selected = new Map(model.comparisonCategories.map(c=>[c.benchmark_id,c]));
    const benchmarks = model.benchmarks.filter(b => selected.has(b.protocol.benchmark_id) && b.scope === 'OFFICIAL_LOCAL'
      && Number.isInteger(b.definition.required_task_count) && b.protocol.tasks===b.definition.required_task_count);
    const benchmarkMap = new Map(benchmarks.map(b => [b.key, b]));
    const families = model.comparisonCategories.map(c=>({ id:c.family_id, name:c.label, key:'family:'+c.family_id,
      protocols:benchmarks.filter(b=>b.protocol.benchmark_id===c.benchmark_id) })).filter(f=>f.protocols.length);
    const familyMap = new Map(families.map(f => [f.id, f]));
    const columns = model.columns.filter(c => c.kind !== 'benchmark' && !c.key.startsWith('attempt_metrics.') && (!c.benchmark || benchmarkMap.has(c.benchmark.key)) && (!c.family || familyMap.has(c.family.id)))
      .map(c => c.family ? { ...c, label:familyMap.get(c.family.id).name, family: familyMap.get(c.family.id) } : c);
    const complete = r => {
      const b=benchmarkMap.get(model.runColumns[r.run_id]);
      return b && r.official_eligible===true && r.status!=='PARTIAL' && r.tasks===b.definition.required_task_count;
    };
    const hasBenchmark = row => row.runs.some(complete);
    const measured = model.rows.filter(hasBenchmark).map(row=>({ ...row,
      runs:row.runs.filter(complete),
      scores:Object.fromEntries(benchmarks.map(b=>[b.key,row.scores[b.key]])) }));
    return { ...model, benchmarks, benchmarkMap, families, columns,
      rows: mergeConfigurations(measured, { ...model, benchmarks }), supplementalRows: model.rows.filter(r => !hasBenchmark(r)) };
  }
  function value(row, column, state, benchmarkMap) {
    if(column.kind==='summary_metric')return performanceSummary(row,availableAverage(row,state,benchmarkMap).keys,benchmarkMap)[column.path];
    if (column.kind === 'average') return availableAverage(row,state,benchmarkMap).score;
    if (column.kind === 'benchmark' || column.kind === 'family') return resolvedScore(row, column, state, benchmarkMap).a?.score ?? null;
    if (column.kind === 'metric') return measuredValue(row.scores[column.benchmark.key], column.path);
    if (column.key === 'engine.version') return row.values['engine.version'] ?? row.values['engine.source_version_label'] ?? null;
    return row.values[column.key] ?? null;
  }
  function matches(v, expression) {
    let q = expression.trim(); if (!q) return true;
    if (typeof v === 'boolean') q = q.replace(/\bein\b/ig, 'true').replace(/\baus\b/ig, 'false');
    if (q.toUpperCase() === UNKNOWN || q === '?') return absent(v);
    const match = q.match(/^(>=|<=|!=|=|>|<)\s*(.*)$/);
    if (match) {
      const [_, op, target] = match;
      if (absent(v)) return false;
      const numeric = target !== '' && Number.isFinite(Number(target)) && (finite(v)
        || typeof v === 'string' && v.trim() !== '' && Number.isFinite(Number(v)));
      if (!numeric && !['=', '!='].includes(op)) return false;
      const a = numeric ? Number(v) : text(v).toLowerCase(), b = numeric ? Number(target) : target.toLowerCase();
      return op === '>=' ? a >= b : op === '<=' ? a <= b : op === '>' ? a > b : op === '<' ? a < b : op === '!=' ? a !== b : a === b;
    }
    return text(v).toLowerCase().includes(q.toLowerCase());
  }
  function compare(a, b, descending) {
    if (absent(a) || absent(b)) return absent(a) === absent(b) ? 0 : absent(a) ? 1 : -1;
    const numeric = (finite(a) || typeof a === 'string' && a.trim() !== '' && Number.isFinite(Number(a)))
      && (finite(b) || typeof b === 'string' && b.trim() !== '' && Number.isFinite(Number(b)));
    const c = numeric ? Number(a) - Number(b) : text(a).localeCompare(text(b), undefined, { numeric: true });
    return descending ? -c : c;
  }
  function csvCell(x) {
    let s = text(x);
    if (typeof x !== 'number' && /^[\s]*[=+\-@\t\r]/.test(s)) s = "'" + s;
    return '"' + s.replaceAll('"', '""') + '"';
  }
  function csv(rows, columns, state, benchmarkMap) {
    const selected = columns.filter(c => c.key !== 'runtime_configuration_id');
    const identity = key => { const b = benchmarkMap.get(key); return { column_id: key ?? null, family_id: b?.family_id ?? null, qualification_track: b?.scope ?? null, protocol: b?.protocol ?? null }; };
    const selection = { mode: state.mode ?? null, mean_policy:'AVAILABLE_DISPLAYED_COMPLETE_CATEGORIES_ARITHMETIC_MEAN',
      displayed_family_protocols: [...(state.protocols || [])].map(([family_id, key]) => ({ family_id, ...identity(key) })) };
    return '\uFEFF' + [[csvCell('runtime_configuration_id'), csvCell('source_runtime_configuration_ids'), csvCell('selected_protocols'), ...selected.map(c => csvCell(c.label + ' [' + c.key + ']'))].join(','), ...rows.map(row => [csvCell(row.id), csvCell(row.memberIds || [row.id]), csvCell({...selection,mean:availableAverage(row,state,benchmarkMap),mean_protocols:availableAverage(row,state,benchmarkMap).keys.map(identity)}), ...selected.map(c => {
      if (c.kind === 'benchmark' || c.kind === 'family') {
        const { key, selectedKey, a } = resolvedScore(row, c, state, benchmarkMap);
        return csvCell({ ...identity(key), selected_reference_protocol: identity(selectedKey), measurement: !a?.n ? null : { mean_percent: a.score, distinct_original_observations: a.n, conflict: a.conflict,
          solved: a.solved, tasks: a.tasks, min: a.min, max: a.max, sd: a.sd,
          runs: a.records.map(r => ({ run_id: r.run_id, experiment_id: r.experiment_id, runtime_configuration_id: r.runtime_configuration_id, status: r.status, audits: r.audit_ids })) }, missing_label: !a?.n ? NOT_MEASURED : null });
      }
      const v = value(row, c, state, benchmarkMap);
      if(c.kind==='summary_metric'){
        const p=performanceSummary(row,availableAverage(row,state,benchmarkMap).keys,benchmarkMap);
        return csvCell({value:v,energy:c.path==='energy_j_per_success'?p.energy:null,tasks:p.tasks,solved:p.solved,
          basis:p.basis,runs:p.runs,status:p.status,missing_label:absent(v)?NOT_MEASURED:null});
      }
      return csvCell(c.kind === 'average' && absent(v) ? 'NICHT BERECHENBAR' : v);
    })].join(','))].join('\r\n');
  }
  function analysis(rows, target, state, model) {
    const ranked = rows.map(row => ({ row, score: value(row, target, state, model.benchmarkMap) })).filter(x => finite(x.score))
      .sort((a, b) => b.score - a.score || a.row.id.localeCompare(b.row.id));
    const top = ranked.slice(0, 5), parameters = model.columns.filter(c => c.kind === 'parameter' && /^(model|engine|runtime|optimizations|requested|launch_flags)\./.test(c.key));
    const coverage = parameters.map(c => {
      const counts = new Map(); let missing = 0;
      top.forEach(({ row }) => { const v = row.values[c.key]; if (absent(v)) missing++; else counts.set(text(v), (counts.get(text(v)) || 0) + 1); });
      const all = new Set(ranked.map(({ row }) => row.values[c.key]).filter(v => !absent(v)).map(text));
      return { column: c, counts: [...counts].sort((a, b) => b[1] - a[1]), missing, testedValues: all.size };
    });
    return { top, measuredConfigurations: ranked.length, coverage };
  }
  const API = { UNKNOWN, canonical, flatten, parameters, aggregate, average, build, value, matches, compare, csv, analysis, protocols, defaultProtocol, protocolKey, resolvedScore, comparisonView, configurationKey, mergeConfigurations, performanceSummary, availableAverage };
  if (typeof module !== 'undefined' && module.exports) module.exports = API;
  root.V100MasterTable = API;
  if (typeof document === 'undefined') return;

  const E = (tag, content, className) => { const e = document.createElement(tag); if (content !== undefined) e.textContent = content; if (className) e.className = className; return e; };
  const link = (label, href) => { const a = E('a', label); a.href = href; return a; };
  const labelInput = (label, input) => { const e = E('label'); input.setAttribute('aria-label', label); e.append(E('span', label), input); return e; };
  const button = (label, handler) => { const b = E('button', label); b.type = 'button'; b.addEventListener('click', handler); return b; };
  const number = v => finite(v) ? v.toLocaleString('de-DE', { maximumFractionDigits: 2 }) : UNKNOWN;
  function mount(target, data) {
    const model = comparisonView(build(data)), byKey = new Map(model.columns.map(c => [c.key, c]));
    const state = { mode: 'official', protocols: new Map(model.families.map(f => [f.id, defaultProtocol(f)])), visible: new Set(), filters: new Map(), search: '', sort: 'average', descending: true, officialOnly: false, allMeasured: true, strictProtocols: new Set() };
    const base = ['model.name', 'model.quantization', 'engine.name', 'engine.version', 'requested.MTP', 'requested.thinking', 'runtime.context'];
    summaryMetrics.forEach(([path])=>base.push('summary:'+path));
    const chosenBenchmarks = () => [...state.protocols.values()].map(k => model.benchmarkMap.get(k)).filter(Boolean);
    const columnAllowed = c => !state.officialOnly || !(c?.benchmark || c?.family) || model.benchmarkMap.get(protocolKey(c, state))?.scope === 'OFFICIAL_LOCAL';
    let presetName = 'Kompakt', filtered = [], shownColumns = [], headerCells = new Map();
    target.textContent = ''; target.append(E('h2', 'Alle gemessenen Ergebnisse'));
    const toolbar = E('div', undefined, 'master-toolbar'), search = E('input'); search.type = 'search'; search.placeholder = 'Modell, Engine, Parameter oder Experiment suchen'; search.setAttribute('aria-label', search.placeholder);
    const presets = E('select'); ['Kompakt', 'Vollständig', 'Qualität', 'Geschwindigkeit', 'Energie'].forEach(t => presets.append(E('option', t)));
    const exportButton = button('CSV exportieren', () => {
      const blob = new Blob([csv(filtered, shownColumns, state, model.benchmarkMap)], { type: 'text/csv;charset=utf-8' });
      const url = URL.createObjectURL(blob), a = link('Download', url); a.download = 'v100-configuration-results.csv'; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    }); exportButton.dataset.action = 'export-csv';
    const officialOnly = E('input'); officialOnly.type = 'checkbox'; officialOnly.dataset.action = 'official-only';
    toolbar.append(search, labelInput('Ansicht', presets), exportButton, button('Filter zurücksetzen', () => { state.filters.clear(); state.search = ''; search.value = ''; state.strictProtocols.clear(); renderTable(); }));
    target.append(toolbar);
    const chooser = E('details', undefined, 'master-panel'); chooser.append(E('summary', 'Spaltenauswahl nach Kategorien'));
    const pickerSearch = E('input'); pickerSearch.type = 'search'; pickerSearch.placeholder = 'Spaltenname oder Quellpfad'; pickerSearch.setAttribute('aria-label', 'Spalten suchen'); const picker = E('div', undefined, 'master-column-picker'); chooser.append(pickerSearch, picker); target.append(chooser);
    const selection = E('details', undefined, 'master-panel'); selection.append(E('summary', 'Benchmarkprotokolle auswählen'));
    selection.append(E('p', 'Genau ein festgelegter Benchmark je Kategorie; ausschließlich vollständige, lokal qualifizierte Ergebnisse. Protokollauswahl hält Revision, Scorer und Aufgaben identisch. Ø Benchmarks mittelt automatisch alle vorhandenen vollständigen Ergebnisse der sichtbaren Kategorien je Konfiguration. Fehlende Kategorien werden ausgelassen, niemals als null gewertet. Die Abdeckung steht direkt am Durchschnitt (z. B. 2/3). Kein offizieller Gesamtbenchmark; unterschiedliche Abdeckung ist kein fairer Gesamtrangvergleich. Replikate werden arithmetisch gemittelt, niemals nach Bestwert ausgewählt.'));
    const benchmarkChoices = E('div', undefined, 'master-benchmark-choices'), selectionWarning = E('p', undefined, 'benchmark-warning'); selection.append(benchmarkChoices, selectionWarning); target.append(selection);
    const definitions = E('details', undefined, 'master-panel'); definitions.append(E('summary', 'Exakte Benchmarkdefinitionen und Messprotokolle'));
    model.benchmarks.forEach(b => {
      const d = E('details'); d.append(E('summary', b.name + ' · ' + b.scope + ' · ' + b.key.slice(-6)));
      const dl = E('dl'); Object.entries({ ...b.definition, ...b.protocol, qualification_track: b.scope, column_id: b.key }).forEach(([key, v]) => dl.append(E('dt', key), E('dd', text(v)))); d.append(dl); definitions.append(d);
    }); target.append(definitions);
    const counter = E('p', undefined, 'master-counter'); counter.setAttribute('aria-live', 'polite'); target.append(counter);
    const basisSummary=E('p',undefined,'master-performance-basis');target.append(basisSummary);
    const scroll = E('div', undefined, 'master-scroll'); scroll.tabIndex = 0; scroll.setAttribute('aria-label', 'Alle gemessenen Ergebnisse, horizontal scrollbar');
    const table = E('table', undefined, 'master-table'); table.append(E('caption', 'Unveränderliche Konfigurationen und nach Protokoll getrennte Benchmarkergebnisse'));
    const head = E('thead'), body = E('tbody'); table.append(head, body); scroll.append(table); target.append(scroll);
    // Horizontal overflow establishes a scroll container; follow document Y
    // scrolling explicitly without imposing a vertical table viewport.
    let stickyFrame = 0;
    const followHeader = () => {
      stickyFrame = 0;
      if (!target.isConnected) { root.removeEventListener('scroll', scheduleHeader); root.removeEventListener('resize', scheduleHeader); return; }
      const rect = table.getBoundingClientRect(), siteHeader = document.querySelector('.md-header');
      const top = Math.max(0, siteHeader?.getBoundingClientRect().bottom || 0);
      head.style.transform = 'translateY(' + Math.max(0, Math.min(rect.height - head.offsetHeight, top - rect.top)) + 'px)';
    };
    const scheduleHeader = () => { if (!stickyFrame) stickyFrame = root.requestAnimationFrame(followHeader); };
    root.addEventListener('scroll', scheduleHeader, { passive: true }); root.addEventListener('resize', scheduleHeader);

    const insights = E('section', undefined, 'master-insights'); insights.append(E('h2', 'Beobachtungen zu den Top 5'));
    insights.append(E('p', 'Korrelation ist keine Kausalität. Diese Übersicht priorisiert Forschungsfragen; sie prognostiziert keine Gewinne und startet keine Versuche. Unterschiede unbekannter Parameter bleiben mögliche Störfaktoren.'));
    const analysisSelect = E('select'), analysisBody = E('div'); insights.append(labelInput('Sortiermetrik der Analyse', analysisSelect), analysisBody); target.append(insights);
    const dialog = E('dialog', undefined, 'master-cell-dialog'), dialogTitle = E('h3'), dialogValue = E('pre'), dialogLinks = E('div');
    dialog.append(dialogTitle, dialogValue, dialogLinks, button('Schließen', () => dialog.close())); target.append(dialog);

    function preset(name) {
      presetName = name; state.visible = new Set(base); state.visible.add('average');
      model.families.forEach(f => state.visible.add(f.key));
      const bench = chosenBenchmarks();
      if (name === 'Vollständig') model.columns.filter(c => c.kind !== 'family' && c.key !== 'engine.build_id').forEach(c => state.visible.add(c.key));
      if (name === 'Qualität') model.columns.filter(c => /thinking|reasoning|sampling|native_template|quantization|draft/.test(c.key)).forEach(c => state.visible.add(c.key));
      if (name !== 'Kompakt') ['requested.thinking', 'requested.MTP', 'runtime.context', 'runtime.max_output', 'runtime.batch', 'runtime.microbatch'].forEach(k => state.visible.add(k));
      if (name === 'Geschwindigkeit') model.columns.filter(c => /runtime\.(batch|microbatch|CPU_threads)|flash_attention|cuda_graphs|prefill_tok_s|decode_tok_s|ttft_s|:wall_s$|:task_phase_s$|:startup_s$|:successful_tasks_per_task_phase_s$|matched_performance\.(tasks|solved|wall_s|successful_tasks_per_s)$/.test(c.key) && (c.kind !== 'metric' || bench.some(b => b.key === c.benchmark.key))).forEach(c => state.visible.add(c.key));
      if (name === 'Energie') { state.visible.add('runtime.power_limit_w'); model.columns.filter(c => c.kind === 'metric' && /:(gpu_j|gpu_j_per_success|peak_vram_mib)$|matched_performance\.(tasks|solved|gpu_j|gpu_j_per_success|peak_vram_mib)$|counter_energy\.(lower_j|upper_j|j_per_success_lower|j_per_success_upper)$/.test(c.key) && bench.some(b => b.key === c.benchmark.key)).forEach(c => state.visible.add(c.key)); }
      renderPicker(); renderTable();
    }
    function renderPicker() {
      picker.textContent = ''; const query = pickerSearch.value.toLowerCase();
      const groups = new Map(); model.columns.forEach(c => { if (!(c.label + ' ' + c.key).toLowerCase().includes(query)) return; if (!groups.has(c.category)) groups.set(c.category, []); groups.get(c.category).push(c); });
      groups.forEach((columns, name) => {
        const field = E('fieldset'); field.append(E('legend', name + ' (' + columns.length + ')'));
        columns.forEach(c => { const box = E('input'); box.type = 'checkbox'; box.checked = state.visible.has(c.key); box.dataset.columnKey = c.key; box.disabled = c.key === 'model.name';
          box.disabled = box.disabled || !columnAllowed(c);
          const label = labelInput(c.label, box); label.title = c.key + (columnAllowed(c) ? '' : ' · Anderer Auswertungsmodus');
          box.addEventListener('change', () => { if (box.checked) state.visible.add(c.key); else state.visible.delete(c.key); renderTable(); }); field.append(label); }); picker.append(field);
      });
    }
    function renderBenchmarks() {
      const previousAnalysis = analysisSelect.value;
      benchmarkChoices.textContent = ''; analysisSelect.textContent = ''; const meanOption = E('option', 'Nutzerdefinierter Durchschnitt'); meanOption.value = 'average'; analysisSelect.append(meanOption);
      model.families.forEach(f => {
        const selectedKey = state.protocols.get(f.id), b = model.benchmarkMap.get(selectedKey);
        const field = E('div', undefined, 'master-family-choice'); field.dataset.familyId = f.id;
        const select = E('select'); select.dataset.protocolFamily = f.id;
        f.protocols.forEach(p => {
          const option = E('option', p.name + ' · ' + p.scope + ' · Aufgaben=' + text(p.protocol.tasks) + ' · ' + p.key.slice(-10)); option.value = p.key; select.append(option);
        }); select.value = selectedKey;
        const identity = E('small', b ? 'Revision: ' + text(b.protocol.benchmark_revision) + ' · Dataset: ' + text(b.definition.hf_dataset_id) + ' · Split: ' + text(b.definition.dataset_split) + ' · Scorer: ' + text(b.protocol.scorer_version) + ' · Task-Set: ' + text(b.protocol.evaluated_task_set_hash) : UNKNOWN);
        identity.title = b ? text({ ...b.protocol, definition: b.definition, scope: b.scope }) : UNKNOWN;
        select.title = identity.title;
        select.addEventListener('change', () => {
          state.strictProtocols.add(f.id);
          state.protocols.set(f.id, select.value);
          renderBenchmarks(); preset(presetName);
        });
        field.append(labelInput('Protokoll: ' + f.name, select), identity); benchmarkChoices.append(field);
        const option = E('option', f.name + ' (gewähltes Protokoll)'); option.value = f.key; analysisSelect.append(option);
      });
      if ([...analysisSelect.options].some(o => o.value === previousAnalysis)) analysisSelect.value = previousAnalysis;
    }
    function renderTable() {
      state.visible.add('model.name');
      const params = model.columns.filter(c => c.kind === 'parameter' && state.visible.has(c.key));
      params.sort((a, b) => { const rank = c => base.includes(c.key) ? base.indexOf(c.key) : base.length + model.columns.indexOf(c); return rank(a) - rank(b); });
      shownColumns = [...params, ...model.columns.filter(c => c.kind === 'summary_metric' && state.visible.has(c.key)), ...model.columns.filter(c => c.kind === 'metric' && state.visible.has(c.key) && columnAllowed(c)),
        ...model.columns.filter(c => c.kind === 'family' && state.visible.has(c.key) && columnAllowed(c)),
        ...model.columns.filter(c => c.kind === 'benchmark' && state.visible.has(c.key) && columnAllowed(c)),
        ...model.columns.filter(c => c.kind === 'average' && state.visible.has(c.key))];
      head.textContent = ''; headerCells = new Map(); const names = E('tr'), filters = E('tr');
      shownColumns.forEach(c => {
        const th = E('th'); th.scope = 'col'; th.dataset.columnKey = c.key; const b = button((c.shortLabel || c.label) + ' ↕', () => { state.descending = state.sort === c.key ? !state.descending : c.kind !== 'parameter'; state.sort = c.key; renderRows(); }); b.title = (c.description || c.label + '\n' + c.key); th.append(b);
        if (c.kind === 'family') {
          const p = model.benchmarkMap.get(protocolKey(c, state));
          const note = E('small', p ? (state.allMeasured ? (finite(p.protocol.tasks) ? 'n je Zelle · Vollumfang ' + p.protocol.tasks : 'Umfang je Zelle') : p.scope + ' · n=' + text(p.protocol.tasks)) : UNKNOWN, 'master-protocol-note');
          note.title = p ? text(p.protocol) : UNKNOWN; th.append(note);
        }
        names.append(th); headerCells.set(c.key, th);
        const cell = E('th'), input = E('input'); input.type = 'search'; input.placeholder = c.kind === 'parameter' ? 'Filter / ?' : 'z. B. >=80'; input.value = state.filters.get(c.key) || ''; input.setAttribute('aria-label', 'Filter: ' + c.label);
        input.addEventListener('input', () => { state.filters.set(c.key, input.value); renderRows(); }); cell.append(input); filters.append(cell);
      }); head.append(names, filters); renderRows();
    }
    function renderRows() {
      const query = state.search.toLowerCase();
      const resultColumns=shownColumns.filter(c=>c.kind==='family'||c.kind==='benchmark');
      filtered = model.rows.filter(row => (!state.officialOnly || row.runs.some(r => r.official_eligible === true)) && (!query || canonical({ values: row.values, runs: row.runs }).toLowerCase().includes(query))
        && resultColumns.some(c=>{const a=resolvedScore(row,c,state,model.benchmarkMap).a;return a?.n>0&&!a.conflict&&finite(a.score);})
        && [...state.filters].every(([key, expression]) => !expression.trim() || matches(value(row, byKey.get(key), state, model.benchmarkMap), expression)));
      const sort = byKey.get(state.sort) || byKey.get('model.name');
      filtered.sort((a, b) => compare(value(a, sort, state, model.benchmarkMap), value(b, sort, state, model.benchmarkMap), state.descending) || a.id.localeCompare(b.id));
      body.textContent = '';
      filtered.forEach(row => {
        const tr = E('tr'); tr.dataset.configurationId = row.id; tr.dataset.configurationIds = row.memberIds.join(' ');
        shownColumns.forEach(c => {
          const td = E('td'); td.dataset.columnKey = c.key; td.dataset.kind = c.kind;
          if (c.kind === 'benchmark' || c.kind === 'family') renderScore(td, row, c);
          else if(c.kind==='summary_metric')renderSummary(td,row,c);
          else {
            const v = value(row, c, state, model.benchmarkMap), display = c.kind === 'average' && finite(v) ? number(v) + ' % · ' + availableAverage(row,state,model.benchmarkMap).count + '/' + availableAverage(row,state,model.benchmarkMap).total
              : c.kind === 'average' && absent(v) ? 'NICHT BERECHENBAR' : ['requested.MTP', 'requested.thinking'].includes(c.key) && typeof v === 'boolean' ? (v ? 'Ein' : 'Aus') : text(v);
            if (c.key === 'model.name') { const modelLink = link(row.displayName, '../configuration-profiles/' + row.id + '/'); modelLink.title = row.displayName; td.append(modelLink); }
            else if (c.key === 'engine.version' && absent(v) && row.values['engine.version_provenance_note']) {
              td.append(button(UNKNOWN + ' ⓘ', () => {
                dialogTitle.textContent = 'Engine-Version · ' + row.displayName;
                dialogValue.textContent = row.values['engine.version_provenance_note']; dialogLinks.textContent = ''; dialog.showModal();
              }));
            }
            else if (display.length > 42) { const full = button(display.slice(0, 36) + '…', () => {
              dialogTitle.textContent = c.label + ' · ' + row.displayName; dialogLinks.textContent = '';
              dialogValue.textContent = typeof v === 'object' ? JSON.stringify(v, null, 2) : display;
              dialog.showModal();
            }); full.className = 'master-value-button'; full.setAttribute('aria-label', 'Vollständiger Wert: ' + c.label); td.append(full); }
            else td.textContent = display;
            td.title = c.key + '\n' + text(c.kind==='average'?availableAverage(row,state,model.benchmarkMap):v); if (absent(v)) td.classList.add('master-missing');
          } tr.append(td);
        }); body.append(tr);
      });
      headerCells.forEach((th, key) => { th.removeAttribute('aria-sort'); if (key === state.sort) th.setAttribute('aria-sort', state.descending ? 'descending' : 'ascending'); });
      const complete = filtered.filter(r => finite(availableAverage(r,state,model.benchmarkMap).score)).length;
      counter.textContent = filtered.length + ' / ' + model.rows.length + ' Konfigurationen mit Kategorie-Ergebnis · ' + model.supplementalRows.length + ' weitere gemessene Profile im Originalarchiv · ' + complete + ' mit berechenbarem Benchmark-Durchschnitt · ' + [...state.filters.values()].filter(x => x.trim()).length + ' Parameterfilter. Fehlende Daten sind keine Nullpunkte.';
      selectionWarning.textContent = 'Nur vollständige, geprüfte Kategorie-Ergebnisse. Partials und zusätzliche Benchmarks bleiben ausgeschlossen. Ø Benchmarks = Summe vorhandener Kategorie-Prozentwerte / Anzahl vorhandener Kategorien derselben Konfiguration. Keine Bestwertselektion. Kein offizieller Gesamtbenchmark.';
      basisSummary.textContent='Messbasis je Zeile: vorhandene vollständige Ergebnisse der sichtbaren Kategorien; Abdeckung n/3 am Durchschnitt. Unterschiedliche Abdeckung beachten. Decode = Token/Zeit; Latenz und Output-Token je Aufgabe; VRAM = höchster Peak. Fehlende Einzelmetriken bleiben unbekannt. ⓘ öffnet Messbedingungen und Quellen.';
      renderAnalysis(); scheduleHeader();
    }
    function renderSummary(td,row,column){
      const p=performanceSummary(row,availableAverage(row,state,model.benchmarkMap).keys,model.benchmarkMap),v=p[column.path];
      let display=finite(v)?number(v):NOT_MEASURED;
      if(column.path==='energy_j_per_success'&&p.energy){
        display=number(p.energy.lower)+(p.energy.upper!==p.energy.lower?'–'+number(p.energy.upper):'');
      }else if(column.path==='energy_j_per_success'&&p.energy_status==='NO_SUCCESSES')display='KEIN ERFOLG';
      const b=button(display+' ⓘ',()=>{
        dialogTitle.textContent=column.label+' · '+row.displayName;
        dialogValue.textContent=JSON.stringify({definition:column.description,selected_benchmark_summary:p,
          source_runtime_configuration_ids:row.memberIds,aggregation:'Totals over unique recorded observations from every selected exact benchmark. No best-run selection, partials, cross-configuration joins or interpolation. Missing required data stays unknown.'},null,2);
        dialogLinks.textContent='';
        (p.runs||[]).forEach(r=>{const line=E('div');line.append(link(r.experiment_id,'../experiments/'+r.experiment_id+'/'),document.createTextNode(' · '),link('Konfiguration','../configuration-profiles/'+r.runtime_configuration_id+'/'));(r.audit_ids||[]).forEach(id=>line.append(document.createTextNode(' · '),link('Audit '+id,'../audits/'+id+'/')));dialogLinks.append(line);});
        dialog.showModal();
      });b.className='master-value-button';td.append(b);td.title=column.description;
      if(!finite(v))td.classList.add('master-missing');
    }
    function renderScore(td, row, column) {
      const { key, benchmark, a } = resolvedScore(row, column, state, model.benchmarkMap);
      if (!a?.n) { td.textContent = NOT_MEASURED; td.className = 'master-missing'; return; }
      if (a.conflict) { td.textContent = 'WIDERSPRÜCHLICHE AUDITS'; td.className = 'benchmark-warning'; return; }
      const partialEvidence = a.records.some(r => r.status === 'PARTIAL' || Number.isInteger(benchmark.definition.required_task_count) && r.tasks < benchmark.definition.required_task_count);
      const scope = partialEvidence ? 'PARTIAL' : { OFFICIAL_LOCAL: 'OFFIZIELL', HISTORICAL: 'HISTORISCH', UNQUALIFIED_FULL: 'VOLLSTÄNDIG', PARTIAL: 'PARTIAL', LOCAL_SUPPLEMENTAL: 'LOKAL' }[benchmark.scope];
      const line = E('span', undefined, 'master-score-line');
      line.append(E('strong', number(a.score) + ' %'), document.createTextNode(' (' + a.solved + '/' + a.tasks + ') · '));
      const category = { 'bfcl-v4-simple-python-full400': 'Simple Python', 'bfcl-v4-parallel-multiple-full200': 'Parallel Multiple' }[benchmark.protocol.benchmark_id];
      const details = button((category ? category + ' · ' : '') + scope + (a.n > 1 ? ' · n=' + a.n : '') + ' ⓘ', () => {
        dialogTitle.textContent = column.label + ' · ' + row.displayName;
        dialogValue.textContent = JSON.stringify({ mean_percent: a.score, solved: a.solved, tasks: a.tasks, n: a.n,
          min: a.min, max: a.max, sample_sd: a.sd, protocol: benchmark.protocol, definition: benchmark.definition, qualification_track: benchmark.scope,
          model_sha256: row.profile.model.artifact_sha256, runtime_configuration_id: a.records[0].runtime_configuration_id, source_runtime_configuration_ids: row.memberIds,
          engine_version: row.values['engine.version'] ?? null, build_id: row.values['engine.build_id'] ?? null,
          thinking: row.values['requested.thinking'], MTP: row.values['requested.MTP'], context: row.values['runtime.context'], output_limit: row.values['runtime.max_output'],
          prefill_tok_s: measuredValue(a, 'prefill_tok_s'), decode_tok_s: measuredValue(a, 'decode_tok_s'), ttft_s: measuredValue(a, 'ttft_s'),
          wall_s: measuredValue(a, 'wall_s'), gpu_j: measuredValue(a, 'gpu_j'), gpu_j_per_success: measuredValue(a, 'gpu_j_per_success'), peak_vram_mib: measuredValue(a, 'peak_vram_mib'),
          engine_source_evidence: row.values['engine.source_evidence'],
          configuration: row.profiles.find(p => p.runtime_configuration_id === a.records[0].runtime_configuration_id), captured_profiles: row.profiles, runs: a.records, metadata_evidence: row.values['evidence.metadata_receipts'] }, (k, v) => absent(v) ? UNKNOWN : v, 2);
        dialogLinks.textContent = '';
        a.records.forEach(r => {
          const section = E('div');
          if (r.archived_diagnostic) section.append(link('Response and weight provenance diagnosis', '../' + r.archived_diagnostic.report + '/'), document.createTextNode(' · '));
          section.append(link(r.experiment_id, '../experiments/' + r.experiment_id + '/'), document.createTextNode(' · '), link('Konfiguration', '../configuration-profiles/' + r.runtime_configuration_id + '/'));
          r.audit_ids.forEach(id => section.append(document.createTextNode(' · '), link('Audit ' + id, '../audits/' + id + '/')));
          if (r.qualification_audit_id) section.append(link(' Zulassung', '../audits/' + r.qualification_audit_id + '/'));
          dialogLinks.append(section);
        }); dialog.showModal();
      }); details.className = 'master-score-details'; line.append(details);
      [...new Set(a.records.map(r => r.experiment_id))].forEach(id => { line.append(document.createTextNode(' · '), link(id, '../experiments/' + id + '/')); });
      td.append(line);
      td.title = key + '\n' + text(benchmark.protocol);
    }
    function renderAnalysis() {
      analysisBody.textContent = ''; const column = byKey.get(analysisSelect.value || 'average');
      const result = analysis(filtered, column, state, model); analysisBody.append(E('p', result.measuredConfigurations + ' Konfigurationen mit tatsächlich vorhandenem Ergebnis für diese Metrik. Gezeigt werden höchstens fünf; Gleichstände sind keine Überlegenheit.'));
      if (!result.top.length) { analysisBody.append(E('p', UNKNOWN + ' – keine vollständigen vergleichbaren Ergebnisse für die gewählte Auswertung.')); return; }
      const top = E('ol'); result.top.forEach(({ row, score }) => { const li = E('li'); li.append(link(row.displayName + ' · ' + row.id.slice(0, 16), '../configuration-profiles/' + row.id + '/'), document.createTextNode(' · ' + number(score) + ' %')); top.append(li); }); analysisBody.append(top);
      const details = E('details'); details.append(E('summary', 'Häufige Werte, Unterschiede und fehlende Abdeckung – alle Parameter'));
      const grid = E('dl');
      result.coverage.forEach(c => { grid.append(E('dt', c.column.label), E('dd', (c.counts.map(([v, n]) => v + ' (' + n + ')').join('; ') || UNKNOWN) + ' · unbekannt: ' + c.missing + '/' + result.top.length + ' · erfasste Ausprägungen: ' + c.testedValues)); }); details.append(grid); analysisBody.append(details);
      analysisBody.append(E('p', 'Abdeckung bezieht sich nur auf diese Ergebnisprofile. Fehlende Metadaten beweisen keinen ungetesteten Matrixfaktor. Vor weiteren Versuchen die kanonischen Audits prüfen; gültige Tests nicht wiederholen.'));
      const proposals = E('ul'); result.coverage.filter(c => /^(runtime|optimizations|requested)\./.test(c.column.key) && !/sha|identity|budget|artifact/i.test(c.column.key)).slice(0, 8).forEach(c => {
        proposals.append(E('li', c.column.label + ': ' + (c.missing ? 'Zuerst fehlende Einstellungen aus Originalbelegen erfassen. ' : '') + (c.testedValues < 2 ? 'Weniger als zwei belegte Ausprägungen: zusätzlicher isolierter Vergleich könnte die Abdeckung schließen.' : 'Kontrollierten A/B-Vergleich erwägen; vorhandene Gesamtprofile ändern möglicherweise mehrere Faktoren.') + ' Modellartefakt, Engine, Aufgaben, Sampler und übrige Parameter konstant halten; keine Wirkung aus dieser Häufigkeit ableiten.'));
      }); analysisBody.append(E('h3', 'Mögliche nächste Forschungsfragen – keine automatische Zulassung'), proposals);
    }
    search.addEventListener('input', () => { state.search = search.value; renderRows(); });
    pickerSearch.addEventListener('input', renderPicker); presets.addEventListener('change', () => preset(presets.value));
    officialOnly.addEventListener('change', () => { state.officialOnly = officialOnly.checked;
      [...state.filters.keys()].forEach(key => { if (!columnAllowed(byKey.get(key))) state.filters.delete(key); });
      if (!columnAllowed(byKey.get(state.sort))) state.sort = 'average';
      renderPicker(); renderTable(); }); analysisSelect.addEventListener('change', renderAnalysis);
    renderBenchmarks(); preset('Kompakt');
  }
  API.mount = mount;
})(typeof window === 'undefined' ? globalThis : window);
