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
test('all documented configurations including weaker and failed attempts remain available', () => {
  assert.equal(model.rows.length, data.history.profiles.length);
  assert.deepEqual(new Set(model.rows.map(r => r.id)), new Set(data.history.profiles.map(p => p.runtime_configuration_id)));
});
test('every profile leaf and every explicitly recorded startup flag has a selectable column', () => {
  const keys = new Set(model.columns.map(c => c.key));
  for (const profile of data.history.profiles) for (const key of Object.keys(M.parameters(profile))) assert(keys.has(key), key);
  for (const key of ['model.qat', 'model.svd', 'model.parameter_count', 'engine.version', 'engine.build_id',
    'optimizations.speculation_effective', 'optimizations.cuda_graphs.actual_capture_replay']) assert(keys.has(key));
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
