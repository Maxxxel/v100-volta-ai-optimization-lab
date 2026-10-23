'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const M = require('../docs/javascripts/master-table.js');
const context = { window: {} };
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(__dirname, '../docs/assets/benchmarks/leaderboard-data.js'), 'utf8'), context);
const data = context.window.V100Leaderboard;
const model = M.build(data);
const score = (n, audit = 'a') => ({ run_id: 'run-' + audit, audit_hash: audit, experiment_id: 'R1',
  runtime_configuration_id: 'cfg-a', benchmark_id: 'b', benchmark_identity_id: 'definition-1',
  benchmark_revision: 'r1', dataset_split_hash: 'data-1', evaluated_task_set_hash: 'tasks-1',
  scorer_version: 'scorer-1', metric: 'pass_at_1_percent', solved: n, tasks: 100,
  score_percent: n, official_eligible: true, audit_ids: [] });
test('artifact-specific identity labels preserve immutable model names, runs and scores', () => {
  const copy = JSON.parse(JSON.stringify(data));
  const target = model.rows.find(r => r.profile.model.artifact_sha256);
  const hash = target.profile.model.artifact_sha256;
  copy.register.model_label_annotations = [{ artifact_sha256: hash, display_name: 'Verified weight-equivalent artifact', review_id: 'fixture' }];
  copy.register.model_family_labels = {};
  const before = JSON.stringify(copy.history), view = M.build(copy);
  for (const row of view.rows) {
    if (row.profile.model.artifact_sha256 === hash) {
      assert.equal(row.displayName, 'Verified weight-equivalent artifact');
      assert.equal(row.values['model.historical_name'], row.profile.model.name);
      assert.equal(row.values['model.name'], row.displayName);
    } else assert.equal(row.displayName, row.profile.model.name);
  }
  assert.equal(JSON.stringify(copy.history), before);
  assert(view.columns.some(c => c.key === 'model.historical_name'));
  assert(view.columns.some(c => c.key === 'model.identity_annotation'));
});
test('exactly every measured configuration is shown and result-free profiles stay in the archive', () => {
  const ids = new Set(data.history.runs.map(r => r.runtime_configuration_id));
  assert.equal(model.rows.length, ids.size);
  assert.deepEqual(new Set(model.rows.map(r => r.id)), ids);
  assert(model.rows.every(r => r.runs.length > 0 && Object.values(r.scores).some(s => s.n > 0)));
  assert.equal(model.archive.length + model.rows.length, data.history.profiles.length);
  assert(model.archive.every(p => !ids.has(p.runtime_configuration_id)));
});
test('every measured profile leaf, evidence field and startup flag has a selectable column', () => {
  const keys = new Set(model.columns.map(c => c.key));
  for (const row of model.rows) for (const key of Object.keys(row.values)) assert(keys.has(key), key);
  for (const key of ['model.qat', 'model.svd', 'model.parameter_count', 'engine.version', 'engine.build_id',
    'optimizations.speculation_effective', 'optimizations.cuda_graphs.actual_capture_replay']) assert(keys.has(key));
});
test('all measured protocol tracks stay present without pagination or a bounded vertical viewport', () => {
  const js = fs.readFileSync(path.join(__dirname, '../docs/javascripts/master-table.js'), 'utf8');
  const css = fs.readFileSync(path.join(__dirname, '../docs/stylesheets/lab.css'), 'utf8');
  assert(!/pageSize|state\.page|master-pagination|filtered\.slice/.test(js));
  assert(!/master-scroll\s*\{[^}]*max-height/.test(css));
  assert(js.includes('officialOnly: false'));
  assert(js.includes('filtered.forEach(row =>'));
  for (const r of data.history.runs) assert(model.rows.some(row => row.runs.some(x => x.run_id === r.run_id)));
});
test('configuration and timing annotations preserve original identities and provenance', () => {
  const before = M.canonical(data.history);
  const view = M.build(data);
  assert.equal(M.canonical(data.history), before);
  for (const e of data.history.configuration_evidence || []) {
    const row = view.rows.find(r => r.id === e.runtime_configuration_id); assert(row);
    for (const [key, v] of Object.entries(e.fields)) assert.equal(M.canonical(row.values[key]), M.canonical(v));
    assert(e.sources.every(s => /^[a-f0-9]{64}$/.test(s.sha256) && s.authority_audit_id));
  }
  for (const e of data.history.measurement_evidence || []) {
    const row = view.rows.find(r => r.id === e.runtime_configuration_id); const run = row.runs.find(r => r.run_id === e.run_id); assert(run);
    for (const [key, v] of Object.entries(e.values)) assert.equal(run[key], v);
    assert(e.sources.length); assert(run.timing_provenance);
  }
});
test('every current official register definition has a distinct column even without measurements', () => {
  for (const d of data.register.definitions) assert(model.benchmarks.some(b => b.scope === 'OFFICIAL_LOCAL' && b.protocol.benchmark_id === d.benchmark_id));
  assert.equal(new Set(model.benchmarks.map(b => b.key)).size, model.benchmarks.length);
  for (const run of data.history.runs) {
    const b = model.benchmarkMap.get(data.master.run_columns[run.run_id]); assert(b);
    assert.equal(M.canonical(b.protocol.scorer_version), M.canonical(run.scorer_version));
    assert.equal(b.protocol.evaluated_task_set_hash, run.evaluated_task_set_hash);
    assert.equal(b.protocol.tasks, run.tasks);
  }
});
test('BFCL subsets and official full benchmarks never share a result column', () => {
  for (const r of data.history.runs.filter(r => r.benchmark_id === 'bfcl-v4-full')) {
    assert.equal(model.benchmarkMap.get(data.master.run_columns[r.run_id]).scope, 'HISTORICAL');
  }
  assert(model.benchmarks.some(b => b.protocol.benchmark_id === 'bfcl-v4-simple-python-full400' && b.protocol.tasks === 400));
});
test('arithmetic average gives equal weight to selected benchmarks', () => {
  const scores = { a: M.aggregate([score(50)]), b: M.aggregate([score(100, 'b')]) };
  const columns = new Map([['a', { scope: 'OFFICIAL_LOCAL' }], ['b', { scope: 'OFFICIAL_LOCAL' }]]);
  assert.equal(M.average(scores, ['a', 'b'], true, columns), 75);
  assert.equal(M.average(scores, [], true, columns), null);
});
test('a missing result is not zero and prevents the selected average', () => {
  const columns = new Map([['a', { scope: 'OFFICIAL_LOCAL' }], ['b', { scope: 'OFFICIAL_LOCAL' }]]);
  assert.equal(M.average({ a: M.aggregate([score(100)]) }, ['a', 'b'], true, columns), null);
  assert.equal(M.aggregate([]).score, null);
  assert.equal(M.aggregate([score(0)]).score, 0);
});
test('the average cannot join different configurations, even for the same model', () => {
  const columns = new Map([['a', { scope: 'OFFICIAL_LOCAL' }], ['b', { scope: 'OFFICIAL_LOCAL' }]]);
  const a = M.aggregate([score(100)]), b = M.aggregate([{ ...score(50, 'b'), runtime_configuration_id: 'cfg-other-tuning' }]);
  assert.equal(M.average({ a, b }, ['a', 'b'], true, columns), null);
  assert(M.aggregate([score(100), { ...score(50, 'b'), runtime_configuration_id: 'cfg-other-tuning' }]).conflict);
});
test('benchmark percentages are averaged without weighting by task-set size', () => {
  const a = M.aggregate([score(95)]), b = M.aggregate([{ ...score(50, 'b'), solved: 1, tasks: 2 }]);
  const columns = new Map([['a', { scope: 'OFFICIAL_LOCAL' }], ['b', { scope: 'OFFICIAL_LOCAL' }]]);
  assert.equal(M.average({ a, b }, ['a', 'b'], true, columns), 72.5);
});
test('unqualified and historical results cannot enter an official average', () => {
  const columns = new Map([['a', { scope: 'OFFICIAL_LOCAL' }], ['b', { scope: 'HISTORICAL' }]]);
  assert.equal(M.average({ a: M.aggregate([{ ...score(80), official_eligible: false }]) }, ['a'], true, columns), null);
  assert.equal(M.average({ a: M.aggregate([{ ...score(80), official_eligible: 'false' }]) }, ['a'], true, columns), null);
  const b = M.aggregate([{ ...score(80), official_eligible: false }]);
  assert.equal(M.average({ b }, ['b'], true, columns), null);
  assert.equal(M.average({ b }, ['b'], false, columns), 80);
});
test('independent replicates use their mean, sample count and dispersion, never their maximum', () => {
  const a = M.aggregate([score(50, 'first'), score(100, 'second')]);
  assert.equal(a.score, 75); assert.equal(a.n, 2); assert.equal(a.min, 50); assert.equal(a.max, 100);
  assert(Math.abs(a.sd - Math.sqrt(1250)) < 1e-10); assert.equal(a.solved, 150); assert.equal(a.tasks, 200);
});
test('admission-history duplicates do not become extra replicates', () => {
  const a = M.aggregate([score(50), { ...score(50), run_id: 'new-history-record' }]);
  assert.equal(a.n, 1); assert.equal(a.score, 50); assert.equal(a.sd, null);
});
test('conflicting judgments for one observation fail closed', () => {
  const a = M.aggregate([score(50), score(80)]); assert(a.conflict); assert.equal(a.score, null);
});
test('different tasks, revisions or scorers cannot be pooled as replicates', () => {
  for (const field of ['benchmark_revision', 'dataset_split_hash', 'evaluated_task_set_hash', 'scorer_version']) {
    const a = M.aggregate([score(50), { ...score(80, 'b'), [field]: 'changed' }]); assert(a.conflict, field); assert.equal(a.score, null);
  }
});
test('unknown flags and engine versions are not synthesized from build IDs', () => {
  const v = M.parameters({ model: { name: 'Test' }, engine: { build_id: 'hash' }, start_parameters: { argv: ['server', '--batch-size', '0', '--flag', '--repeat', 'a', '--repeat', 'b'] } });
  assert.equal(v['engine.version'], undefined); assert.equal(v['optimizations.speculation_type'], undefined);
  assert.equal(v['requested.MTP'], null); assert.equal(v['requested.thinking'], null);
  assert.equal(M.parameters({ optimizations: { speculation_type: 'none' } })['requested.MTP'], false);
  assert.equal(M.parameters({ optimizations: { speculation_type: 'draft-mtp' } })['requested.MTP'], true);
  assert.equal(M.parameters({ runtime: { thinking_reasoning_requested: 'on' } })['requested.thinking'], null);
  assert.equal(v['launch_flags.--batch-size'], '0'); assert.equal(v['launch_flags.--flag'], true);
  assert.deepEqual(v['launch_flags.--repeat'], ['a', 'b']);
});
test('parameter filters handle numeric limits, exact text, zero, false and missing values', () => {
  assert(M.matches(0, '=0')); assert(M.matches(false, '=false')); assert(M.matches('8192', '>=4096'));
  assert(!M.matches(null, '=0')); assert(M.matches(null, '?')); assert(M.matches(null, 'NICHT ERFASST'));
  assert(M.matches('Q6_K', 'q6')); assert(!M.matches(20, '>80'));
  assert(!M.matches('Q6_K', '>80')); assert(!M.matches(false, '=0'));
  assert(M.matches(false, '=Aus')); assert(M.matches(true, 'Ein'));
});
test('numeric sorting keeps missing values last in both directions', () => {
  assert.deepEqual([null, 2, 100, 10].sort((a, b) => M.compare(a, b, true)), [100, 10, 2, null]);
  assert.deepEqual([null, 2, 100, 10].sort((a, b) => M.compare(a, b, false)), [2, 10, 100, null]);
});
test('CSV exports missing markers, full identities, replica provenance and safe formula-like text', () => {
  const row = { id: 'cfg', values: { name: '=DANGER()', unknown: null }, scores: { b: M.aggregate([score(50)]) } };
  const out = M.csv([row], [{ key: 'name', label: 'Name', kind: 'parameter' }, { key: 'unknown', label: 'Unknown', kind: 'parameter' }, { key: 'b', label: 'Benchmark', kind: 'benchmark' }], {}, new Map());
  assert(out.includes("'=DANGER()")); assert(out.includes('NICHT ERFASST')); assert(out.includes('run-a')); assert(out.includes('mean_percent'));
});
test('Top-5 analysis counts real measured configurations and records unknown parameter coverage', () => {
  const benchmark = model.benchmarks.find(b => b.scope === 'OFFICIAL_LOCAL' && model.rows.some(r => r.scores[b.key]?.n));
  const state = { mode: 'official', selected: new Set([benchmark.key]) };
  const target = model.columns.find(c => c.key === 'average'); const a = M.analysis(model.rows, target, state, model);
  const expected = model.rows.filter(r => M.average(r.scores, [benchmark.key], true, model.benchmarkMap) !== null).length;
  assert.equal(a.measuredConfigurations, expected); assert.equal(a.top.length, Math.min(5, expected));
  assert(a.coverage.some(c => c.column.key === 'engine.version'));
});

test('archived source-identity diagnostics do not change benchmark scores or qualification', () => {
  for (const original of data.history.runs) {
    const observed = model.rows.find(r => r.id === original.runtime_configuration_id).runs.find(r => r.run_id === original.run_id);
    assert.equal(observed.score_percent, original.score_percent); assert.equal(observed.official_eligible, original.official_eligible);
    if ((data.register.archived_diagnostics || []).some(d => d.experiment_id === original.experiment_id)) {
      assert(observed.archived_diagnostic); assert(observed.archived_diagnostic.weight_identity_status);
    }
  }
});

test('family columns are unique, while every original protocol remains selectable', () => {
  const human = model.families.filter(f => f.id === 'humanevalplus');
  assert.equal(human.length, 1); assert(human[0].protocols.length > 1);
  assert.equal(model.columns.filter(c => c.kind === 'family' && c.label === 'HumanEval+').length, 1);
  assert.equal(model.families.flatMap(f => f.protocols).length, model.benchmarks.length);
  assert.equal(new Set(model.families.flatMap(f => f.protocols.map(p => p.key))).size, model.benchmarks.length);
  for (const b of model.benchmarks) {
    assert(b.family_id && b.family_name);
    assert(model.columns.some(c => c.kind === 'benchmark' && c.key === b.key));
  }
});
test('family defaults prefer qualified official protocols without any per-row fallback', () => {
  const family = model.families.find(f => f.id === 'humanevalplus');
  const key = M.defaultProtocol(family); assert.equal(model.benchmarkMap.get(key).scope, 'OFFICIAL_LOCAL');
  const c = model.columns.find(c => c.key === family.key), state = { protocols: new Map([[family.id, key]]) };
  const historic = family.protocols.find(b => b.scope === 'HISTORICAL'); assert(historic);
  const row = { scores: { [historic.key]: M.aggregate([score(87)]) } };
  assert.equal(M.value(row, c, state, model.benchmarkMap), null);
  state.protocols.set(family.id, historic.key);
  assert.equal(M.value(row, c, state, model.benchmarkMap), 87);
  state.protocols.set(family.id, model.families.find(f => f.id !== family.id).protocols[0].key);
  assert.equal(M.value(row, c, state, model.benchmarkMap), null, 'Cross-family protocol selection fails closed');
  const officialEmpty = { ...family.protocols.find(b => b.scope === 'OFFICIAL_LOCAL'), records: 0 };
  assert.equal(M.defaultProtocol({ protocols: [historic, officialEmpty] }), officialEmpty.key);
});
test('a family can never be weighted twice, including exploratory averages', () => {
  const columns = new Map([['a', { family_id: 'humanevalplus', scope: 'OFFICIAL_LOCAL' }], ['b', { family_id: 'humanevalplus', scope: 'HISTORICAL' }]]);
  const scores = { a: M.aggregate([score(50)]), b: M.aggregate([score(100, 'b')]) };
  assert.equal(M.average(scores, ['a', 'b'], false, columns), null);
  assert.equal(M.average(scores, ['a', 'a'], true, columns), null);
  assert.equal(M.average(scores, ['a'], true, columns), 50);
  columns.get('b').family_id = 'mbppplus';
  assert.equal(M.average(scores, ['a', 'b'], false, columns), 75);
});
test('family CSV preserves exact selected protocol identities even for missing measurements', () => {
  const family = model.families.find(f => f.id === 'humanevalplus'), key = M.defaultProtocol(family);
  const column = model.columns.find(c => c.key === family.key);
  const state = { mode: 'official', selected: new Set([key]), protocols: new Map([[family.id, key]]) };
  const row = { id: 'cfg-empty-fixture', values: {}, scores: {} };
  const csv = M.csv([row], [column, { key: 'average', label: 'Average', kind: 'average' }], state, model.benchmarkMap);
  for (const field of ['selected_protocols', key, 'scorer_version', 'evaluated_task_set_hash', 'benchmark_revision', 'qualification_track', 'NICHT BERECHENBAR', 'NICHT ERFASST']) assert(csv.includes(field), field);
  const before = M.canonical(data.history); M.build(data); assert.equal(M.canonical(data.history), before);
});

test('comparison view excludes own supplemental tests without deleting any source evidence', () => {
  const before = M.canonical(data), view = M.comparisonView(model);
  assert(view.benchmarks.every(b => b.scope !== 'LOCAL_SUPPLEMENTAL' && !b.protocol.benchmark_id.startsWith('local-')));
  assert(view.families.every(f => !f.id.startsWith('local-')));
  assert(view.columns.every(c => !c.benchmark || view.benchmarkMap.has(c.benchmark.key)));
  assert(view.columns.every(c => !c.key.startsWith('attempt_metrics.')));
  assert(view.rows.every(r => view.benchmarks.some(b => r.scores[b.key]?.n > 0)));
  assert.equal(view.rows.length + view.supplementalRows.length, model.rows.length);
  for (const row of model.rows) assert(view.rows.includes(row) || view.supplementalRows.includes(row));
  assert.equal(M.canonical(data), before);
  assert(model.benchmarks.some(b => b.scope === 'LOCAL_SUPPLEMENTAL'));
});

test('OmniCoder historical V2 labels collapse to one display family without losing configurations', () => {
  const view = M.comparisonView(M.build(data));
  const omni = view.rows.filter(r => Object.hasOwn(data.register.model_family_labels || {}, r.profile.model.family_id));
  assert(omni.length > 1);
  assert(omni.every(r => r.displayName === 'OmniCoder 9B'));
  assert.equal(new Set(omni.map(r => r.id)).size, omni.length);
  assert(omni.every(r => r.values['model.historical_name'] === r.profile.model.name));
});
test('engine source labels require the exact recorded server, CUDA library and build tuple', () => {
  const view = M.comparisonView(M.build(data)), column = view.columns.find(c => c.key === 'engine.version');
  assert(view.rows.every(r => typeof M.value(r, column, {}, view.benchmarkMap) === 'string'));
  assert(view.rows.every(r => r.profile.engine.version === null), 'No synthetic upstream release written into immutable profiles');
  const copy = JSON.parse(JSON.stringify(data)), review = copy.register.engine_source_reviews?.[0]; assert(review);
  review.engines.forEach(e => { e.kernel_library_sha256 = '0'.repeat(64); });
  const wrong = M.comparisonView(M.build(copy));
  assert(wrong.rows.every(r => r.values['engine.source_version_label'] === undefined));
});
