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
const archivedView = () => ({ ...model, rows:M.mergeConfigurations(model.rows,model), supplementalRows:[] });

function performanceFixture(){
 const record=(id,tasks,solved,tokens,ms,wall,low,high,peak)=>({run_id:id,audit_hash:id,runtime_configuration_id:'cfg-shared',
  benchmark_id:id,benchmark_identity_id:id,tasks,solved,score_percent:100*solved/tasks,metric:'success',official_eligible:true,
  decode_tokens:tokens,decode_engine_ms:ms,wall_s:wall,peak_vram_mib:peak,
  counter_energy:{method:'NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1',tasks,solved,lower_j:low,upper_j:high}});
 const a=record('a',2,1,100,1000,4,10,12,1024),b=record('b',8,2,1000,100000,24,100,110,2048);
 const row={id:'cfg-shared',values:{},scores:{a:M.aggregate([a]),b:M.aggregate([b])}};
 const map=new Map([['a',{key:'a',family_id:'coding',scope:'OFFICIAL_LOCAL',definition:{required_task_count:2},protocol:{benchmark_id:'a'}}],
  ['b',{key:'b',family_id:'tools',scope:'OFFICIAL_LOCAL',definition:{required_task_count:8},protocol:{benchmark_id:'b'}}]]);
 return {a,b,row,map};
}
test('compact performance pools actual tokens/time and task costs, never means unrelated rates or peaks',()=>{
 const {row,map}=performanceFixture(),p=M.performanceSummary(row,['a','b'],map);
 assert.equal(p.tasks,10);assert.equal(p.solved,3);assert.equal(p.decode_tok_s,1100/101);
 assert.equal(p.wall_per_task_s,2.8);assert.equal(p.output_tokens_per_task,110);assert.equal(p.peak_vram_gib,2);
 assert.equal(p.energy.lower,110/3);assert.equal(p.energy.upper,122/3);assert.equal(p.energy_j_per_success,122/3);
 assert.equal(p.energy.sorting,'upper_bound');assert.notEqual(p.decode_tok_s,(100+10)/2);
});
test('missing selected category, repeated category and incompatible configuration prevent performance pooling',()=>{
 const {row,map}=performanceFixture();assert.equal(M.performanceSummary(row,['a','missing'],map).decode_tok_s,null);
 assert.equal(M.performanceSummary(row,['a','a'],map).energy_j_per_success,null);
 row.scores.b.records[0].runtime_configuration_id='cfg-other';assert.equal(M.performanceSummary(row,['a','b'],map).wall_per_task_s,null);
});
test('performance keeps unavailable token measurements and mixed energy methods unknown independently',()=>{
 const {row,map}=performanceFixture();row.scores.b.records[0].decode_tokens=null;
 row.scores.b.records[0].counter_energy=null;row.scores.b.records[0].gpu_j=100;
 const p=M.performanceSummary(row,['a','b'],map);assert.equal(p.decode_tok_s,null);assert.equal(p.output_tokens_per_task,null);
 assert.equal(p.energy_j_per_success,null);assert.equal(p.energy_status,'MISSING_OR_MIXED_ENERGY_METHODS');assert.equal(p.wall_per_task_s,2.8);
});
test('performance excludes partial/subset costs and avoids an energy-per-success division by zero',()=>{
 const {row,map}=performanceFixture();row.scores.b.records[0].measurement_conditions={performance_tasks:7};
 let p=M.performanceSummary(row,['a','b'],map);assert.equal(p.wall_per_task_s,null);assert.equal(p.decode_tok_s,null);assert.equal(p.energy_j_per_success,null);
 delete row.scores.b.records[0].measurement_conditions;
 for(const group of Object.values(row.scores)){group.records[0].solved=0;group.records[0].counter_energy.solved=0;}
 p=M.performanceSummary(row,['a','b'],map);assert.equal(p.energy_j_per_success,null);assert.equal(p.energy_status,'NO_SUCCESSES');
 row.scores.a.records[0].status='PARTIAL';assert.equal(M.performanceSummary(row,['a','b'],map).decode_tok_s,null);
});
test('compact performance and CSV use the original full Omni coding/tool costs and both counter bounds',()=>{
 const v=M.comparisonView(M.build(data)),row=v.rows.find(r=>r.runs.some(x=>x.experiment_id==='R478'));
 const keys=['R471','R478'].map(e=>data.master.run_columns[row.runs.find(x=>x.experiment_id===e).run_id]);
 const p=M.performanceSummary(row,keys,v.benchmarkMap);assert.equal(p.tasks,364);assert.equal(p.solved,309);
 assert.equal(p.decode_tok_s,1000*(37503+34046)/(469652.68+429179.679));assert.equal(p.output_tokens_per_task,(37503+34046)/364);
 assert.equal(p.wall_per_task_s,(492.064461986+502.544043479)/364);assert.equal(p.peak_vram_gib,7356.5/1024);
 assert.equal(p.energy.lower,(140482.936+141208.7)/309);assert.equal(p.energy.upper,(140584.646+141312.049)/309);
 const column=v.columns.find(c=>c.key==='summary:energy_j_per_success'),state={allMeasured:true,mode:'official'};
 assert.equal(M.value(row,column,state,v.benchmarkMap),p.energy.upper);
 const csv=M.csv([row],[column],state,v.benchmarkMap);for(const text of ['upper_bound','NVML_REPORTED_COUNTER_GROUP_BRACKETS_V1','R471','R478','lower','upper'])assert(csv.includes(text));
});

test('Ornith primary tools171/200 retains native Thinking, exact200-request cost and partial coding separately',()=>{
 const r=data.history.runs.find(x=>x.experiment_id==='R479'&&x.counter_energy);assert(r&&r.official_eligible);
 assert.equal(r.tasks,200);assert.equal(r.solved,171);assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,171);
 assert.equal(r.counter_energy.j_per_success_lower,1750.5530467836256);assert.equal(r.gpu_j,null);
 const v=M.comparisonView(M.build(data)),row=v.rows.find(x=>x.runs.some(y=>y.run_id===r.run_id));assert(row);
 assert.equal(row.values['requested.thinking'],true);
 const coding=data.history.runs.find(x=>x.experiment_id==='R460');assert(coding&&coding.tasks===93&&coding.status==='PARTIAL');
 assert(!row.runs.some(x=>x.experiment_id==='R460'));
 assert.equal(M.average(row.scores,[data.master.run_columns[coding.run_id],data.master.run_columns[r.run_id]],true,v.benchmarkMap),null);
});

test('Omni reference177/200 joins its unchanged native coding profile and preserves exact200-request costs', () => {
 const r=data.history.runs.find(r=>r.experiment_id==='R478'&&r.counter_energy);assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,200);assert.equal(r.solved,177);assert.equal(r.official_eligible,true);
 assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,177);assert.equal(r.gpu_j,null);
 assert.equal(r.counter_energy.j_per_success_lower,797.7892655367232);
 const v=M.comparisonView(M.build(data));const row=v.rows.find(row=>row.runs.some(x=>x.run_id===r.run_id));assert(row);
 assert(row.runs.some(x=>x.experiment_id==='R471'));assert(row.memberIds.length>=2);
 assert.equal(row.profile.model.artifact_sha256,'b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b');
});

test('LFM24 complex-tool6/200 is a complete measured low score, not missing or a global model rejection', () => {
 const r=data.history.runs.find(r=>r.experiment_id==='R477'&&r.counter_energy);assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,200);assert.equal(r.solved,6);assert.equal(r.score_percent,3);assert.equal(r.official_eligible,true);
 assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,6);assert.equal(r.gpu_j,null);
 assert.equal(r.counter_energy.j_per_success_lower,9622.955833333333);
 const p=data.history.profiles.find(p=>p.runtime_configuration_id===r.runtime_configuration_id);
 assert.equal(p.model.family_id,'lfm25_24b');assert.equal(p.model.quantization,'QAD Q4_0');
 const v=M.comparisonView(M.build(data));assert(v.rows.some(row=>row.runs.some(x=>x.run_id===r.run_id)));
});

test('LFM8 complex-tool170/200 preserves full category, actual Q6 identity and200-request costs', () => {
 const r=data.history.runs.find(r=>r.experiment_id==='R476'&&r.counter_energy);assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,200);assert.equal(r.solved,170);assert.equal(r.official_eligible,true);
 assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,170);assert.equal(r.gpu_j,null);
 assert.equal(r.counter_energy.j_per_success_lower,730.922294117647);
 const p=data.history.profiles.find(p=>p.runtime_configuration_id===r.runtime_configuration_id);
 assert.equal(p.model.artifact_sha256,'7ccf57a2d410d8822d1560a1ca10c8318f3e15d6a8f6d42d1903d58e80ea20a6');assert.equal(p.model.quantization,'Q6_K');
 assert.equal(p.model.family_id,'lfm25_8b_a1b_q6');
 const v=M.comparisonView(M.build(data));assert(v.rows.some(row=>row.runs.some(x=>x.run_id===r.run_id)));
});

test('Qwen3.5 parallel176/200 is category qualified with exact200-task counter bounds', () => {
 const r=data.history.runs.find(r=>r.experiment_id==='R474'&&r.counter_energy);assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,200);assert.equal(r.solved,176);assert.equal(r.official_eligible,true);
 assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,176);
 assert.equal(r.gpu_j,null);assert.equal(r.counter_energy.j_per_success_lower,123638.996/176);
 const v=M.comparisonView(M.build(data)),row=v.rows.find(row=>row.runs.some(x=>x.run_id===r.run_id));assert(row);
 assert.equal(row.scores[data.master.run_columns[r.run_id]].n,1);
});
test('Bonsai parallel145/171 stays partial after native task cap with exact171-task energy', () => {
 const r=data.history.runs.find(r=>r.experiment_id==='R475'&&r.counter_energy);assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,171);assert.equal(r.solved,145);assert.equal(r.official_eligible,false);
 assert.equal(r.status,'PARTIAL');assert.equal(r.counter_energy.tasks,171);assert.equal(r.counter_energy.solved,145);
 assert.equal(r.gpu_j,null);assert.equal(r.counter_energy.j_per_success_lower,324509.274/145);
 const v=archivedView(),row=v.rows.find(row=>row.runs.some(x=>x.run_id===r.run_id));assert(row);
 assert.equal(row.scores[data.master.run_columns[r.run_id]].n,1);
});
test('Qwen3.8 parallel165/197 wrapper-limited prefix remains partial with its exact197-task counter scope',()=>{
 const r=data.history.runs.find(r=>r.experiment_id==='R473');assert(r);
 assert.equal(r.tasks,197);assert.equal(r.intended_tasks,200);assert.equal(r.solved,165);assert.equal(r.status,'PARTIAL');assert.equal(r.termination_kind,'STOPPED_GPU_WRAPPER_TIME_BUDGET');assert.equal(r.official_eligible,false);
 assert.match(r.status_reason,/wrapper timeout/);assert.equal(r.gpu_j,null);assert.equal(r.task_phase_s??null,null);
 assert.equal(r.counter_energy.tasks,197);assert.equal(r.counter_energy.solved,165);assert.equal(r.counter_energy.j_per_success_lower,331828.269/165);assert.equal(r.counter_energy.j_per_success_upper,331938.119/165);
 const v=archivedView(),row=v.rows.find(x=>x.runs.some(y=>y.run_id===r.run_id)),key=data.master.run_columns[r.run_id];assert(row);
 assert.equal(row.values['model.quantization'],'GSQ/RCO IQ3_S');assert.equal(row.values['requested.MTP'],false);assert.equal(row.values['requested.thinking'],false);
 assert.equal(M.average(row.scores,[key],true,v.benchmarkMap),null,'No full200/official average from partial197');
});
test('parallel_multiple200 has a separate selectable BFCL protocol and exact original200-task costs',()=>{
 const r=data.history.runs.find(r=>r.experiment_id==='R472');assert(r);
 assert.equal(r.benchmark_id,'bfcl-v4-parallel-multiple-full200');assert.equal(r.tasks,200);assert.equal(r.solved,154);assert.equal(r.score_percent,77);assert.equal(r.official_eligible,true);
 assert.equal(r.gpu_j,null);assert.equal(r.counter_energy.tasks,200);assert.equal(r.counter_energy.solved,154);
 assert.equal(r.counter_energy.j_per_success_lower,81366.541/154);assert.equal(r.counter_energy.j_per_success_upper,81464.148/154);
 const v=M.comparisonView(M.build(data)),row=v.rows.find(x=>x.runs.some(y=>y.run_id===r.run_id));assert(row);
 const family=v.families.find(x=>x.id==='bfcl'),column=v.columns.find(x=>x.key===family.key),key=data.master.run_columns[r.run_id];assert(family.protocols.some(x=>x.key===key));
 const other=model.benchmarks.find(x=>x.protocol.benchmark_id==='bfcl-v4-simple-python-full400'&&x.scope==='OFFICIAL_LOCAL');assert(other);
 assert(!family.protocols.some(x=>x.protocol.benchmark_id==='bfcl-v4-simple-python-full400'));
 const state={protocols:new Map([[family.id,other.key]])};assert.equal(M.value(row,column,state,v.benchmarkMap),null,'No fallback between categories');
 state.protocols.set(family.id,key);assert.equal(M.value(row,column,state,v.benchmarkMap),77);
 assert.equal(row.values['model.quantization'],'Q4_0');assert.equal(row.values['requested.thinking'],false);assert.equal(row.values['requested.MTP'],false);
 assert(row.profiles.some(p=>p.runtime.native_HTTP_timeout_policy==='REMAINING_TASK_TIME'));
});
test('LFM24B deadline prefix77/85 stays partial and cannot enter full164 rankings', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R468');assert(r);
  assert.equal(r.solved,77);assert.equal(r.tasks,85);assert.equal(r.status,'PARTIAL');assert.equal(r.official_eligible,false);
  assert.equal(r.gpu_j,null);assert.equal(r.counter_energy.tasks,85);assert.equal(r.counter_energy.solved,77);
  assert.equal(r.counter_energy.j_per_success_lower,196290.95/77);
  assert.equal(r.counter_energy.j_per_success_upper,196353.257/77);
  const tools=data.history.runs.find(r=>r.experiment_id==='R467');assert.equal(r.model_artifact_id,tools.model_artifact_id);
  assert.notEqual(r.runtime_configuration_id,tools.runtime_configuration_id,'Original capture identities remain distinct');
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.profile.model.quantization,'QAD Q4_0');assert.equal(row.values['requested.MTP'],false);
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s??null,null,'Missing task-end marker is not imputed from1200s budget');
});
test('LFM24B full native tools retain QAD identity, exact sampler and400-task cost scope', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R467');assert(r&&r.official_eligible);
  assert.equal(r.solved,374);assert.equal(r.tasks,400);assert.equal(r.qualification_audit.category_only,true);
  assert.equal(r.gpu_j,null);assert.equal(r.gpu_j_per_success,null);
  assert.equal(r.counter_energy.tasks,400);assert.equal(r.counter_energy.solved,374);
  assert.equal(r.counter_energy.j_per_success_lower,58123.844/374);
  assert.equal(r.counter_energy.j_per_success_upper,58190.832/374);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.profile.model.name,'LFM2.5 24B A2B');assert.equal(row.profile.model.family_id,'lfm25_24b');
  assert.equal(row.profile.model.artifact_sha256,'d1c03f73ecaf61017d70419eec9e5dc0b05d50ae26c23d522829b934fbabf8a5');
  assert.equal(row.values['model.quantization'],'QAD Q4_0');assert.equal(row.values['requested.MTP'],false);
  assert.equal(row.values['runtime.sampling.temperature'],.1);assert.equal(row.values['runtime.sampling.top_k'],50);
  assert.equal(Number(row.values['runtime.batch']),512);assert.equal(Number(row.values['runtime.microbatch']),128);
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,362.70372274);assert.equal(r.peak_vram_mib,13798.5);
  assert(model.rows.some(x=>x.profile.model.name==='LFM2.5 8B A1B'&&x.profile.model.artifact_sha256!==row.profile.model.artifact_sha256));
});
test('Qwen3.8 complete-artifact native coding149/164 keeps explicit no-speculation and full task cost', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R466'&&r.counter_energy);assert(r&&r.official_eligible);
  assert.equal(r.solved,149);assert.equal(r.tasks,164);assert.equal(r.gpu_j,null);assert.equal(r.gpu_j_per_success,null);
  assert.equal(r.counter_energy.tasks,164);assert.equal(r.counter_energy.solved,149);
  assert.equal(r.counter_energy.j_per_success_lower,316842.769/149);
  assert.equal(r.counter_energy.j_per_success_upper,316944.086/149);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['model.quantization'],'GSQ/RCO IQ3_S');assert.equal(row.values['requested.thinking'],false);
  assert.equal(row.values['requested.MTP'],false);assert.equal(row.values['runtime.max_output'],4096);
  assert.equal(row.profile.model.artifact_sha256,'58fd826723939933dc86f45b7fe04545cbc2de1c70f6fe2cdd3858c87a98c12f');
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,1111.838883905);
});
test('source-bound descriptive-label corrections preserve raw profiles, tuning and scores', () => {
  const before=M.canonical(data.history), corrections=(data.register.profile_label_reviews||[]).flatMap(r=>r.corrections);
  for(const c of corrections){
    const row=model.rows.find(r=>r.id===c.runtime_configuration_id);assert(row);
    assert.equal(row.profile.model.variant,c.original_descriptive_label);
    assert.equal(row.values['model.historical_variant_label'],c.original_descriptive_label);
    assert.equal(row.values['model.variant'],null);assert.equal(row.values['model.quantization'],c.recorded_quantization);
    assert.equal(row.values['runtime.sampling.temperature'],c.recorded_temperature);
  }
  assert.equal(M.canonical(data.history),before);
  if(corrections.length){
    const copy=JSON.parse(JSON.stringify(data));copy.register.profile_label_reviews[0].corrections[0].model_artifact_sha256='0'.repeat(64);
    assert.throws(()=>M.build(copy),/Unbound profile-description correction/);
  }
});
test('Qwen3.5 native coding135/164 retains unknown MTP and exact task-energy denominator', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R465'&&r.counter_energy);assert(r&&r.official_eligible);
  assert.equal(r.solved,135);assert.equal(r.tasks,164);assert.equal(r.gpu_j,null);assert.equal(r.gpu_j_per_success,null);
  assert.equal(r.counter_energy.tasks,164);assert.equal(r.counter_energy.solved,135);
  assert.equal(r.counter_energy.j_per_success_lower,142594.513/135);
  assert.equal(r.counter_energy.j_per_success_upper,142667.995/135);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['model.quantization'],'Q4_K_M');assert.equal(row.values['requested.thinking'],false);
  assert.equal(row.values['requested.MTP'],null);assert.equal(row.values['runtime.max_output'],4096);
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,521.349310776);
  assert.equal(row.scores[data.master.run_columns[r.run_id]].n,1);
});
test('Gemma native coding result retains full164 qualification and separate coding energy scope', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R464'&&r.counter_energy);assert(r&&r.official_eligible);
  assert.equal(r.solved,156);assert.equal(r.tasks,164);assert.equal(r.gpu_j,null);assert.equal(r.gpu_j_per_success,null);
  assert.equal(r.counter_energy.tasks,164);assert.equal(r.counter_energy.solved,156);
  assert.equal(r.counter_energy.j_per_success_lower,187683.969/156);
  assert.equal(r.counter_energy.j_per_success_upper,187773.403/156);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['model.quantization'],'Q4_0');assert.equal(row.values['requested.thinking'],false);
  assert.equal(row.values['requested.MTP'],false);assert.equal(row.values['runtime.max_output'],4096);
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,757.254538861);
  assert.equal(row.scores[data.master.run_columns[r.run_id]].n,1);
});
test('Qwen3.8 full native category retains complete publisher artifact and no-speculation profile', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R462'&&r.counter_energy);assert(r&&r.official_eligible);
  assert.equal(r.solved,383);assert.equal(r.tasks,400);assert.equal(r.gpu_j,null);
  assert.equal(r.counter_energy.tasks,400);assert.equal(r.counter_energy.solved,383);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['requested.thinking'],false);assert.equal(row.values['requested.MTP'],false);
  assert.equal(row.values['model.quantization'],'GSQ/RCO IQ3_S');
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,942.946128526);
  const key=data.master.run_columns[r.run_id];assert.equal(row.scores[key].n,1);
  assert.equal(M.value(row,model.columns.find(c=>c.key==='metric:'+key+':counter_energy.j_per_success_lower'),{selected:new Set(),mode:'official'},model.benchmarkMap),r.counter_energy.j_per_success_lower);
});
test('Qwen3.5 native full category keeps actual Q4 profile and400-task energy identity', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R461');assert(r&&r.official_eligible);
  assert.equal(r.solved,372);assert.equal(r.tasks,400);assert.equal(r.gpu_j,null);
  assert.equal(r.counter_energy.tasks,400);assert.equal(r.counter_energy.solved,372);
  assert.equal(r.counter_energy.j_per_success_lower,r.counter_energy.lower_j/372);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['requested.thinking'],false);assert.equal(row.values['runtime.max_output'],4096);
  assert.equal(row.values['model.quantization'],'Q4_K_M');
  assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,335.993795138);
});
test('Ornith native coding prefix remains partial with exact93-task energy scope', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R460');assert(r);
  assert.equal(r.solved,85);assert.equal(r.tasks,93);assert.equal(r.intended_tasks,164);
  assert.equal(r.status,'PARTIAL');assert.equal(r.official_eligible,false);
  assert.equal(r.gpu_j,null);assert.equal(r.gpu_j_per_success,null);
  assert.equal(r.counter_energy.tasks,93);assert.equal(r.counter_energy.solved,85);
  assert.equal(r.counter_energy.j_per_success_lower,r.counter_energy.lower_j/85);
  assert.equal(r.counter_energy.j_per_success_upper,r.counter_energy.upper_j/85);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);assert(row);
  assert.equal(row.values['requested.thinking'],true);assert.equal(row.values['runtime.max_output'],4096);
});
test('Gemma QAT native category exposes its declared fast profile and bounded full400 energy', () => {
  const r=data.history.runs.find(r=>r.experiment_id==='R458');assert(r&&r.official_eligible);
  assert.equal(r.solved,374);assert.equal(r.tasks,400);assert.equal(r.gpu_j,null);
  assert.equal(r.counter_energy.tasks,400);assert.equal(r.counter_energy.solved,374);
  assert.equal(r.counter_energy.j_per_success_lower,r.counter_energy.lower_j/374);
  const row=model.rows.find(x=>x.id===r.runtime_configuration_id);
  const observed=row.runs.find(x=>x.run_id===r.run_id);
  assert.equal(observed.task_phase_s,291.184270093);
  assert(observed.task_phase_s>observed.wall_s);
  assert.equal(observed.successful_tasks_per_task_phase_s,374/291.184270093);
  assert.equal(row.values['requested.thinking'],false);assert.equal(row.values['runtime.max_output'],4096);
  assert.equal(row.values['model.quantization'],'Q4_0');
});
test('Ornith full native category retains missing power-integral energy alongside bounded counters', () => {
  const run=data.history.runs.find(r => r.experiment_id==='R457');
  assert(run && run.official_eligible); assert.equal(run.solved,369); assert.equal(run.tasks,400);
  assert.equal(run.gpu_j,null); assert.equal(run.gpu_j_per_success,null);
  assert.equal(run.counter_energy.tasks,400); assert.equal(run.counter_energy.solved,369);
  assert(run.counter_energy.lower_j<=run.counter_energy.upper_j);
  assert.equal(run.counter_energy.j_per_success_upper,run.counter_energy.upper_j/369);
  assert(run.audit_ids.includes(run.counter_energy.audit_id));
});
test('MiMo native full-category result keeps its own thinking profile and full400 cost scope', () => {
  const r = data.history.runs.find(r => r.experiment_id === 'R456');
  assert(r && r.official_eligible); assert.equal(r.tasks, 400); assert.equal(r.solved, 320);
  assert.equal(r.practical_protocol.complete, 398, 'Length-limited replies remain failures');
  assert.equal(r.gpu_j_per_success, r.gpu_j / 320);
  assert(r.wall_s > 0 && r.wall_s < 1200);
  const row = model.rows.find(row => row.id === r.runtime_configuration_id);
  assert.equal(row.values['requested.thinking'], true);
  assert.equal(row.values['model.quantization'], 'Q8_0');
  assert(row.runs.find(run => run.run_id === r.run_id).decode_tok_s > 0);
  assert.notEqual(r.runtime_configuration_id, data.history.runs.find(r => r.experiment_id === 'R454').runtime_configuration_id);
});
test('reused BFCL quality retains independent new-task cost denominators and counter bounds', () => {
  const run = data.history.runs.find(r => r.experiment_id === 'R455');
  assert(run, 'Audited R455 is exported');
  assert.equal(run.tasks, 400); assert.equal(run.solved, 372);
  for (const k of ['wall_s', 'gpu_j', 'gpu_j_per_success']) assert.equal(run[k], null);
  const p = run.matched_performance;
  assert.equal(p.tasks, 360); assert.equal(p.solved, 335);
  assert.equal(p.gpu_j, null, 'Failed power integration remains unknown');
  assert(p.counter_energy.lower_j <= p.counter_energy.upper_j);
  assert.equal(p.counter_energy.j_per_success_lower, p.counter_energy.lower_j / 335);
  assert.equal(run.matched_reference.counter_energy.tasks, 360);
  assert.equal(run.matched_reference.counter_energy.solved, 336);
  assert(model.columns.some(c => c.path === 'matched_performance.counter_energy.lower_j' && c.label.startsWith('Neue Aufgaben:')));
});
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
  for (const row of model.rows) for (const key of Object.keys(row.values)) if(key !== 'evidence.experiments') assert(keys.has(key), key);
  assert(!keys.has('evidence.experiments'), 'Run links belong to the result cell');
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
test('pinned metadata can fill explicit historical unknown markers but cannot replace known values', () => {
  const evidence = data.history.configuration_evidence.find(e => e.fields['model.quantization'] === 'Q8_0');
  assert(evidence, 'Observed historical Q8 metadata has pinned provenance');
  for (const marker of [null, 'NOT MEASURED', 'NICHT ERFASST']) {
    const copy = structuredClone(data), profile = copy.history.profiles.find(p => p.runtime_configuration_id === evidence.runtime_configuration_id);
    profile.model.quantization = marker;
    const before = M.canonical(copy.history), view = M.build(copy);
    assert.equal(view.rows.find(r => r.id === profile.runtime_configuration_id).values['model.quantization'], 'Q8_0');
    assert.equal(M.canonical(copy.history), before);
  }
  for (const known of ['Q6_K', false, 0]) {
    const copy = structuredClone(data); copy.history.profiles.find(p => p.runtime_configuration_id === evidence.runtime_configuration_id).model.quantization = known;
    assert.throws(() => M.build(copy), /Conflicting configuration evidence/);
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
test('one observation retains a later counter supplement without filling power integral or adding a replicate', () => {
  const first={...score(50),run_id:'original',gpu_j:null,audit_ids:['original-audit']};
  const later={...first,run_id:'supplement',counter_energy:{lower_j:100,upper_j:101},audit_ids:['counter-audit']};
  const before=M.canonical([first,later]);const a=M.aggregate([first,later]);
  assert.equal(a.n,1);assert.equal(a.score,50);assert.equal(a.records[0].gpu_j,null);
  assert.equal(a.records[0].counter_energy.lower_j,100);assert.equal(a.records[0].measurement_view_run_ids.length,2);
  assert(a.records[0].audit_ids.includes('counter-audit'));assert.equal(M.canonical([first,later]),before);
  const conflicting={...later,run_id:'conflicting',counter_energy:{lower_j:50,upper_j:51}};
  const b=M.aggregate([first,later,conflicting]);assert.equal(b.n,1);assert.equal(b.score,50);assert.equal(b.records[0].counter_energy,null);assert.equal(b.records[0].counter_energy_conflict,true);
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
  const view=M.comparisonView(model),state={mode:'official',allMeasured:true};
  const target = view.columns.find(c => c.key === 'average'); const a = M.analysis(view.rows, target, state, view);
  const expected = view.rows.filter(r => M.availableAverage(r,state,view.benchmarkMap).score!==null).length;
  assert(expected>0);assert.equal(a.measuredConfigurations, expected); assert.equal(a.top.length, Math.min(5, expected));
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
test('OmniCoder original-template full400 reference retains exact identity and measured counter scope', () => {
  const run = data.history.runs.find(r => r.experiment_id === 'R463' && r.counter_energy);
  assert(run); assert.equal(run.solved, 373); assert.equal(run.tasks, 400);
  assert.equal(run.official_eligible, true); assert.equal(run.qualification_audit.category_only, true);
  assert.equal(run.gpu_j, null); assert.equal(run.gpu_j_per_success, null);
  assert.equal(run.counter_energy.tasks, 400); assert.equal(run.counter_energy.solved, 373);
  assert.equal(run.counter_energy.j_per_success_lower, 105077.717 / 373);
  assert.equal(run.counter_energy.j_per_success_upper, 105181.844 / 373);
  const row = model.rows.find(r => r.id === run.runtime_configuration_id);
  assert.equal(row.profile.model.quantization, 'Q6_K');
  assert.equal(row.profile.model.artifact_sha256, 'b0c1664c86338be24090a45d8b86bd106ba755d004f8746d99ee5ad69258fc3b');
  assert.equal(row.values['requested.thinking'], false);
  assert.equal(row.values['requested.MTP'], false);
  assert.equal(row.scores[data.master.run_columns[run.run_id]].n, 1);
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
test('equally qualified family defaults prefer broad measured coverage over arbitrary hash order',()=>{
 const narrow={key:'a',scope:'OFFICIAL_LOCAL',records:1},broad={key:'z',scope:'OFFICIAL_LOCAL',records:10};
 assert.equal(M.defaultProtocol({protocols:[narrow,broad]}),'z');
 const family=model.families.find(f=>f.id==='bfcl');
 assert.equal(model.benchmarkMap.get(M.defaultProtocol(family)).protocol.benchmark_id,'bfcl-v4-simple-python-full400');
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
  for (const field of ['selected_protocols', key, 'scorer_version', 'evaluated_task_set_hash', 'benchmark_revision', 'qualification_track', 'NICHT BERECHENBAR', 'NICHT GEMESSEN']) assert(csv.includes(field), field);
  const before = M.canonical(data.history); M.build(data); assert.equal(M.canonical(data.history), before);
});

test('comparison contains exactly one fixed benchmark per coding/tools/agents category, preserving every archive record', () => {
  const before = M.canonical(data), view = M.comparisonView(model);
  const selected=new Set(['humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200','terminal-bench-2.1']);
  assert.deepEqual(new Set(view.benchmarks.map(b=>b.protocol.benchmark_id)),selected);
  assert.equal(view.families.length,3);
  assert(view.rows.every(r=>r.runs.length&&r.runs.every(x=>selected.has(x.benchmark_id)&&x.official_eligible===true&&x.status!=='PARTIAL'&&x.tasks===view.benchmarkMap.get(data.master.run_columns[x.run_id]).definition.required_task_count)));
  assert(view.benchmarks.every(b => b.scope !== 'LOCAL_SUPPLEMENTAL' && !b.protocol.benchmark_id.startsWith('local-')));
  assert(view.families.every(f => !f.id.startsWith('local-')));
  assert(view.columns.every(c => !c.benchmark || view.benchmarkMap.has(c.benchmark.key)));
  assert(view.columns.every(c => !c.key.startsWith('attempt_metrics.')));
  assert(view.rows.every(r => view.benchmarks.some(b => r.scores[b.key]?.n > 0)));
  assert.equal(view.rows.reduce((n,r)=>n+r.memberIds.length,0) + view.supplementalRows.length, model.rows.length);
  for (const row of model.rows) assert(view.rows.some(r=>r.memberIds.includes(row.id)) || view.supplementalRows.includes(row));
  assert.equal(M.canonical(data), before);
  assert(model.benchmarks.some(b => b.scope === 'LOCAL_SUPPLEMENTAL'));
});

test('OmniCoder historical V2 labels collapse to one display family without losing configurations', () => {
  const view = M.comparisonView(M.build(data));
  const omni = view.rows.filter(r => data.register.model_family_labels?.[r.profile.model.family_id] === 'OmniCoder 9B');
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
test('one-table default displays partial results without pretending an official score exists', () => {
  const full = { key: 'full', family_id: 'h', scope: 'OFFICIAL_LOCAL', protocol: { tasks: 164 } };
  const partial = { key: 'part', family_id: 'h', scope: 'PARTIAL', protocol: { tasks: 140 } };
  const small = { key: 'small', family_id: 'h', scope: 'PARTIAL', protocol: { tasks: 8 } };
  const column = { kind: 'family', family: { id: 'h', protocols: [full, partial, small] } };
  const row = { scores: { part: M.aggregate([{ ...score(70, 'partial'), solved: 99, tasks: 140, score_percent: 100 * 99 / 140, official_eligible: false, status: 'PARTIAL' }]), small: M.aggregate([{ ...score(100, 'small'), solved: 8, tasks: 8, score_percent: 100, official_eligible: false, status: 'PARTIAL' }]) } };
  const state = { protocols: new Map([['h', 'full']]), allMeasured: true, officialOnly: false, strictProtocols: new Set() }, map = new Map([full, partial, small].map(x => [x.key, x]));
  assert.equal(M.resolvedScore(row, column, state, map).key, 'part', 'Coverage, not maximum percentage, chooses the partial result');
  assert.equal(M.value(row, column, state, map), 100 * 99 / 140);
  assert.equal(M.average(row.scores, ['full'], true, map), null);
  assert.equal(M.resolvedScore(row, column, { ...state, officialOnly: true }, map).a, undefined);
  assert.equal(M.resolvedScore(row, column, { ...state, strictProtocols: new Set(['h']) }, map).a, undefined);
  const csv = M.csv([{ ...row, id: 'cfg-a' }], [column], { ...state, visible: new Set([column.key]), selected: new Set(), mode: 'official' }, map);
  assert(csv.includes('PARTIAL') && csv.includes('140') && csv.includes('selected_reference_protocol'));
});


test('capture-independent rows join all seven evidenced coding/tool pairs without changing source records', () => {
  const before=M.canonical(data), view=archivedView();
  for(const pair of [['R452','R453'],['R454','R456'],['R460','R457'],['R464','R458'],['R465','R461'],['R466','R462'],['R468','R467']]) {
    const rows=pair.map(id=>view.rows.find(r=>r.runs.some(run=>run.experiment_id===id)));
    assert(rows[0]);assert.strictEqual(rows[0],rows[1],pair.join('/'));
    assert(rows[0].memberIds.length>=2);
    for(const id of pair){
      const original=data.history.runs.find(r=>r.experiment_id===id);
      const record=rows[0].runs.find(r=>r.run_id===original.run_id);
      assert.equal(record.runtime_configuration_id,original.runtime_configuration_id);
      assert.equal(record.audit_hash,original.audit_hash);assert.equal(record.score_percent,original.score_percent);
      assert(rows[0].profiles.some(p=>p.runtime_configuration_id===record.runtime_configuration_id));
      assert.equal(rows[0].scores[data.master.run_columns[record.run_id]].n,1);
    }
  }
  assert.equal(M.canonical(data),before);assert(view.rows.length <= model.rows.length-view.supplementalRows.length-7, 'At least seven verified pairs; later valid joins are allowed');
  assert(view.columns.every(c=>c.key!=='evidence.experiments'&&c.label!=='Lauf'));
  const expected=new Set(model.rows.filter(r=>!view.supplementalRows.some(s=>s.id===r.id)).flatMap(r=>r.runs.map(x=>x.run_id)));
  assert.deepEqual(new Set(view.rows.flatMap(r=>r.runs.map(x=>x.run_id))),expected);
});
test('different actual execution settings, kernels, weights and unknown identities cannot merge', () => {
  const get=e=>JSON.parse(JSON.stringify(model.rows.find(r=>r.runs.some(x=>x.experiment_id===e))));
  for(const field of ['weight','server','kernel','context','temperature','MTP','environment','launch','unknown-model','unknown-engine','unknown-template','observed-sampler']){
    const a=get('R467'),b=get('R468');
    if(field==='weight')b.profile.model.artifact_sha256='1'.repeat(64);
    if(field==='server')b.profile.engine.binary_sha256='1'.repeat(64);
    if(field==='kernel')b.profile.engine.kernel_library_sha256='1'.repeat(64);
    if(field==='context')b.profile.runtime.context='16384';
    if(field==='temperature')b.profile.runtime.sampling.temperature=.8;
    if(field==='MTP')b.profile.optimizations.speculation_type='draft-mtp';
    if(field==='environment')b.profile.start_parameters.environment.GGML_CUDA_GRAPH_OPT='1';
    if(field==='launch')b.profile.start_parameters.argv.push('--spec-draft-n-max','3');
    if(field==='unknown-model')a.profile.model.artifact_sha256=b.profile.model.artifact_sha256=null;
    if(field==='unknown-engine')a.profile.engine.binary_sha256=b.profile.engine.binary_sha256=null;
    if(field==='unknown-template')a.profile.runtime.chat_template_sha256=b.profile.runtime.chat_template_sha256=null;
    if(field==='observed-sampler')b.values['runtime.observed_request_sampling.temperature']=.9;
    assert.equal(M.mergeConfigurations([a,b],model).length,2,field);
  }
});
test('evaluation cutoffs do not split identical inference rows; all original conditions and protocols survive',()=>{
 const before=M.canonical(data),v=archivedView();
 for(const ids of [['R461','R465','R474'],['R462','R466','R473'],['R458','R464','R472'],['R467','R468','R477'],['R463','R471','R478']]){
  const rows=ids.map(e=>v.rows.find(r=>r.runs.some(x=>x.experiment_id===e)));
  rows.forEach(r=>assert.strictEqual(r,rows[0],ids.join('/')));
  for(const e of ids){
   const raw=data.history.runs.find(x=>x.experiment_id===e),profile=data.history.profiles.find(p=>p.runtime_configuration_id===raw.runtime_configuration_id);
   assert.deepEqual(rows[0].profiles.find(p=>p.runtime_configuration_id===profile.runtime_configuration_id),profile);
   assert(rows[0].scores[data.master.run_columns[raw.run_id]].n>0);
  }
 }
 assert.equal(M.canonical(data),before);
 const q=v.rows.find(r=>r.runs.some(x=>x.experiment_id==='R473'));
 assert(q.runs.some(x=>x.status==='PARTIAL'&&x.tasks===197));
 assert(q.runs.some(x=>x.official_eligible&&x.tasks===400));
});
test('benchmark tool-adapter choices remain per-run evidence and conflicting tool profiles stay separate',()=>{
  const a=JSON.parse(JSON.stringify(model.rows.find(r=>r.runs.some(x=>x.experiment_id==='R467'))));
  const b=JSON.parse(JSON.stringify(a));b.id='cfg-other-choice';b.values['runtime.native_tool_choice_requested']='required';
  assert.equal(M.mergeConfigurations([a,b],model).length,2);
  const copy=JSON.parse(JSON.stringify(data));copy.history.runs[0].comparison_configuration_id='forged';
  assert.throws(()=>M.build(copy),/Reserved presentation identity/);
});
test('merged exact configuration supports cross-benchmark averages and CSV retaining every original identity',()=>{
  const view=M.comparisonView(M.build(data));const row=view.rows.find(r=>r.runs.some(x=>x.experiment_id==='R464'));
  const runs=['R464','R472'].map(e=>row.runs.find(r=>r.experiment_id===e));
  const keys=runs.map(r=>data.master.run_columns[r.run_id]);
  assert.equal(M.average(row.scores,keys,true,view.benchmarkMap),(100*156/164+100*154/200)/2);
  const selected=new Map(keys.map(key=>[view.benchmarkMap.get(key).family_id,key]));
  const csv=M.csv([row],[...selected.keys()].map(id=>view.columns.find(c=>c.key==='family:'+id)),{mode:'official',selected:new Set(keys),protocols:selected},view.benchmarkMap);
  for(const r of runs){assert(csv.includes(r.runtime_configuration_id));assert(csv.includes(r.experiment_id));assert(csv.includes(r.run_id));}
  assert(csv.includes('source_runtime_configuration_ids'));
});

test('joining configurations retains every physical-observation view and its reviewed counter supplement',()=>{
 const view=archivedView();
 const row=view.rows.find(r=>r.runs.some(x=>x.experiment_id==='R462'));
 const original=data.history.runs.find(r=>r.experiment_id==='R462'&&r.counter_energy);
 const a=row.scores[data.master.run_columns[original.run_id]];
 assert.equal(a.n,1);assert.equal(a.records[0].counter_energy.j_per_success_lower,original.counter_energy.j_per_success_lower);
 assert.equal(a.records[0].counter_energy.j_per_success_upper,original.counter_energy.j_per_success_upper);
 assert(a.records[0].measurement_view_run_ids.includes(original.run_id));
});

test('Qwen3.6 coding122/130 stays partial with exact independent replay and130-request counter scope',()=>{
 const rs=data.history.runs.filter(r=>r.experiment_id==='R469');assert(rs.length);
 const record=rs.find(r=>r.counter_energy);assert(record);
 assert.equal(record.solved,122);assert.equal(record.tasks,130);assert.equal(record.status,'PARTIAL');assert.equal(record.official_eligible,false);
 assert.equal(record.gpu_j,null);assert.equal(record.gpu_j_per_success,null);assert.equal(record.peak_vram_mib,12752.5);
 assert.equal(record.counter_energy.tasks,130);assert.equal(record.counter_energy.solved,122);
 assert.equal(record.counter_energy.j_per_success_lower,331024.748/122);assert.equal(record.counter_energy.j_per_success_upper,331115.022/122);
 const view=archivedView(),row=view.rows.find(r=>r.runs.some(x=>x.run_id===record.run_id));assert(row);
 assert.equal(row.values['model.quantization'],'Q3_K_S');assert.equal(row.values['requested.MTP'],false);assert.equal(row.values['requested.thinking'],false);
 assert.equal(row.values['runtime.sampling.temperature'],.7);assert.equal(row.values['runtime.sampling.presence_penalty'],1.5);
 const key=data.master.run_columns[record.run_id];assert.equal(row.scores[key].n,1,'Counter review is not an inference replicate');
 assert.equal(M.average(row.scores,[key],true,view.benchmarkMap),null,'Observed prefix never enters full official mean');
 assert.equal(row.runs.find(r=>r.run_id===record.run_id).task_phase_s??null,null);
});

test('Qwen3.6 tools242/260 transport failure remains partial, distinct from task deadline and full400',()=>{
 const r=data.history.runs.find(r=>r.experiment_id==='R470'&&r.counter_energy);assert(r);
 assert.equal(r.solved,242);assert.equal(r.tasks,260);assert.equal(r.intended_tasks,400);
 assert.equal(r.official_eligible,false);assert.equal(r.status,'PARTIAL');assert.equal(r.termination_kind,'STOPPED_NATIVE_TRANSPORT_TIMEOUT');
 assert(r.status_reason.includes('total task budget was not exhausted'));
 assert.equal(r.gpu_j,null);assert.equal(r.counter_energy.tasks,260);assert.equal(r.counter_energy.solved,242);
 assert.equal(r.counter_energy.j_per_success_lower,236391.946/242);assert.equal(r.counter_energy.j_per_success_upper,236519.987/242);
 const v=archivedView(),row=v.rows.find(row=>row.runs.some(x=>x.experiment_id==='R470'));assert(row);
 assert(row.runs.some(x=>x.experiment_id==='R469'),'Same model/engine/launch/sampler capture shares the coding row');
 const key=data.master.run_columns[r.run_id];assert.equal(row.scores[key].n,1);assert.equal(M.average(row.scores,[key],true,v.benchmarkMap),null);
});

test('OmniCoder native132/164 reference profile is complete with explicit bounded client and immutable tuning identity',()=>{
 const r=data.history.runs.find(r=>r.experiment_id==='R471'&&r.counter_energy);assert(r&&r.official_eligible);
 assert.equal(r.solved,132);assert.equal(r.tasks,164);assert.equal(r.peak_vram_mib,7354.5);assert.equal(r.gpu_j,null);
 assert.equal(r.counter_energy.tasks,164);assert.equal(r.counter_energy.solved,132);
 assert.equal(r.counter_energy.j_per_success_lower,140482.936/132);assert.equal(r.counter_energy.j_per_success_upper,140584.646/132);
 const v=M.comparisonView(M.build(data)),row=v.rows.find(x=>x.runs.some(y=>y.run_id===r.run_id));assert(row);
 assert.equal(row.values['model.quantization'],'Q6_K');assert.equal(row.values['requested.MTP'],false);assert.equal(row.values['requested.thinking'],false);
 assert.equal(row.values['runtime.native_HTTP_timeout_policy'],'REMAINING_TASK_TIME');assert.equal(row.values['runtime.max_output'],4096);
 assert.equal(row.runs.find(x=>x.run_id===r.run_id).task_phase_s,492.647250806);
 const old=data.history.runs.find(r=>r.experiment_id==='R217'&&r.official_eligible);assert(old);
 assert.notEqual(old.runtime_configuration_id,r.runtime_configuration_id);assert.notEqual(old.model_artifact_id,r.model_artifact_id);
 assert.equal(old.solved,132);assert.equal(old.tasks,164);
});


test('available category mean automatically includes both full results and discloses missing coverage',()=>{
 const v=M.comparisonView(M.build(data)),row=v.rows.find(r=>r.runs.some(x=>x.experiment_id==='R478'));
 const state={allMeasured:true},a=M.availableAverage(row,state,v.benchmarkMap);
 assert.equal(a.score,(100*132/164+100*177/200)/2);assert.equal(a.count,2);assert.equal(a.total,3);
 const column=v.columns.find(c=>c.key==='average');assert.equal(M.value(row,column,state,v.benchmarkMap),a.score);
 const oldCheckboxState={...state,selected:new Set([a.keys[0]])};
 assert.equal(M.value(row,column,oldCheckboxState,v.benchmarkMap),a.score,'Obsolete hidden selection cannot select coding only');
 const csv=M.csv([row],[column],state,v.benchmarkMap);for(const field of ['AVAILABLE_DISPLAYED_COMPLETE_CATEGORIES_ARITHMETIC_MEAN','count','total','mean_protocols'])assert(csv.includes(field));
});
test('available mean counts measured zero, excludes missing or partial categories and never joins configurations',()=>{
 const {row,map}=performanceFixture();
 const state={allMeasured:true};map.set('c',{key:'c',family_id:'agents',scope:'OFFICIAL_LOCAL',definition:{required_task_count:89},protocol:{tasks:89}});
 row.scores.a=M.aggregate([{...row.scores.a.records[0],solved:0,score_percent:0}]);
 let a=M.availableAverage(row,state,map);assert.equal(a.score,12.5);assert.equal(a.count,2);assert.equal(a.total,3);
 row.scores.b.records[0].status='PARTIAL';a=M.availableAverage(row,state,map);assert.equal(a.score,0);assert.equal(a.count,1);
 row.scores.b.records[0].status='QUALIFIED';row.scores.b.records[0].runtime_configuration_id='other';
 assert.equal(M.availableAverage(row,state,map).score,null);
 assert.equal(M.availableAverage({scores:{}},state,map).score,null);
});
test('strict protocol choice cannot borrow another result for the available mean',()=>{
 const {row,map}=performanceFixture(),other={...map.get('b'),key:'b-other'};map.set(other.key,other);
 const state={allMeasured:true,strictProtocols:new Set(['tools']),protocols:new Map([['tools','b-other']])};
 const a=M.availableAverage(row,state,map);assert.equal(a.score,50);assert.equal(a.count,1);assert.equal(a.total,2);assert.deepEqual(a.keys,['a']);
});
