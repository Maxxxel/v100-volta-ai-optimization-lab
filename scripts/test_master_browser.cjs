/* Published/local browser acceptance of the owner-selected category table.
 * Original historical measurements are covered independently by Python/Node.
 * No GPU, model API, credentials or production services are used here.
 */
'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs/promises'),path=require('node:path');
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const base=process.argv[2],artifacts=process.argv[3];
if(!base||!artifacts)throw Error('Supply site-root URL and artifact directory');
async function main(){
 await fs.mkdir(artifacts,{recursive:true});
 const args=['--disable-gpu'];if(process.env.BROWSER_NO_SANDBOX==='1')args.push('--no-sandbox');
 const browser=await chromium.launch({headless:true,args}),errors=[];
 const report={site:base,checks:[],GPU_access:false};
 const screeningData=JSON.parse(await fs.readFile(path.join(__dirname,'../data/screening.json'),'utf8'));const qualificationExpected=screeningData.qualification_phase;
 const validationExpected=screeningData.independent_validation16.rows.filter(r=>r.groups);
 const nativeExpected=JSON.parse(await fs.readFile(path.join(__dirname,'../data/experiments.json'),'utf8')).filter(e=>e.aggregate_metrics?.native_agent18_development);
 try{
  const context=await browser.newContext({viewport:{width:1600,height:1000},acceptDownloads:true});
  async function overrides(ctx){
   if(!process.env.MASTER_SOURCE_DIR)return;
   for(const file of ['javascripts/master-table.js','stylesheets/lab.css'])await ctx.route('**/'+file+'*',r=>r.fulfill({path:path.join(process.env.MASTER_SOURCE_DIR,'docs',file)}));
   report.development_source_override=true;
  }
  await overrides(context);const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
  await page.goto(new URL('configuration-comparison/',base).href,{waitUntil:'networkidle'});
  await page.locator('.master-table tbody tr').first().waitFor();
  const sourceBefore=await page.evaluate(()=>window.V100MasterTable.canonical(window.V100Leaderboard.history));
  const expected=await page.evaluate(()=>{
   const d=window.V100Leaderboard,M=window.V100MasterTable,v=M.comparisonView(M.build(d));
   return {rows:v.rows.length,ids:v.rows.map(r=>r.id),families:v.families.map(f=>f.id),
    benchmarks:[...new Set(v.benchmarks.map(b=>b.protocol.benchmark_id))],
    raw_extra_runs:d.history.runs.filter(r=>!v.benchmarks.some(b=>b.protocol.benchmark_id===r.benchmark_id)).length};
  });
  assert.deepEqual(new Set(expected.benchmarks),new Set(['humanevalplus-v0.1.10','bfcl-v4-parallel-multiple-full200','terminal-bench-2.1']));
  assert.equal(expected.raw_extra_runs>0,true,'Additional historical data must remain preserved');
  assert.equal(await page.locator('select[data-action=comparison-view]').inputValue(),'models');
  const groups=await page.evaluate(()=>window.V100MasterTable.artifactGroups(window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard)).rows).filter(g=>g.rows.length>1).length);
  assert.equal(await page.locator('.master-artifact-group').count(),groups);
  const toggle=page.locator('.master-artifact-group button').first();
  if(await toggle.count()){await toggle.click();assert.equal(await toggle.getAttribute('aria-expanded'),'true');await page.locator('.master-artifact-group button').first().click();}
  await page.screenshot({path:path.join(artifacts,'desktop-model-overview.png'),animations:'disabled'});
  await page.locator('select[data-action=comparison-view]').selectOption('configurations');
  assert.equal(await page.locator('.master-artifact-group').count(),0);
  report.checks.push('default exact-artifact model groups expand variants without pooled scores; scientific view preserves all configuration rows');
  assert.equal(await page.locator('.master-table tbody tr').count(),expected.rows);
  async function noBlankResultRows(){
    const empty=await page.locator('.master-table tbody tr').evaluateAll(rows=>rows.filter(r=>!r.querySelector('td[data-kind="family"] .master-score-line strong')).map(r=>r.dataset.configurationId));
    assert.deepEqual(empty,[],'Every displayed row needs a measured result in a visible category');
  }
  await noBlankResultRows();
  assert.equal(await page.locator('.md-content table').count(),1);assert.equal(await page.locator('.master-pagination').count(),0);
  for(const id of expected.families)assert.equal(await page.locator(`.master-table thead th[data-column-key="family:${id}"]`).count(),1);
  assert.equal(await page.locator('.master-table thead th[data-column-key^="family:"]').count(),3);
  assert.equal(await page.locator('.master-table thead th[data-column-key="evidence.experiments"]').count(),0);
  assert.equal(await page.locator('.master-table thead th[data-column-key="engine.build_id"]').count(),0);
  assert.equal(await page.locator('select[data-protocol-family]').count(),3);
  assert.equal(await page.locator('.master-family-choice[data-family-id=mbppplus]').count(),0);
  const agentValues=await page.locator('td[data-column-key="family:terminal-bench"]').allTextContents();
  assert.equal(agentValues.length,expected.rows);assert(agentValues.every(v=>v.startsWith('NICHT GEMESSEN')));
  report.checks.push('exactly three fixed category benchmarks in one continuous table; original extra runs preserved outside this view; agent results missing rather than zero');

  const primaryRuns=await page.evaluate(()=>{
   const d=window.V100Leaderboard,M=window.V100MasterTable,v=M.comparisonView(M.build(d));
   return v.rows.flatMap(r=>r.runs).map(r=>({id:r.runtime_configuration_id,exp:r.experiment_id,bench:r.benchmark_id,solved:r.solved,tasks:r.tasks}));
  });
  assert(primaryRuns.every(r=>expected.benchmarks.includes(r.bench)));
  const latest=primaryRuns.find(r=>r.exp==='R478');assert(latest);
  const omni=page.locator(`tr[data-configuration-ids~="${latest.id}"]`);
  assert((await omni.locator('td[data-column-key="family:humanevalplus"]').innerText()).includes('132/164'));
  assert((await omni.locator('td[data-column-key="family:bfcl"]').innerText()).includes('177/200'));
  assert.equal(await omni.locator('td[data-column-key="family:bfcl"] a').filter({hasText:'R478'}).count(),1);
  const qwen=primaryRuns.find(r=>r.exp==='R474');assert(qwen);
  const qrow=page.locator(`tr[data-configuration-ids~="${qwen.id}"]`);
  assert((await qrow.locator('td[data-column-key="family:humanevalplus"]').innerText()).includes('135/164'));
  assert((await qrow.locator('td[data-column-key="family:bfcl"]').innerText()).includes('176/200'));
  assert.equal(await page.locator(`tr[data-configuration-ids~="${qwen.id}"]`).count(),1);
  const alt=primaryRuns.find(r=>r.exp==='R517');assert(alt);
  const altrow=page.locator(`tr[data-configuration-ids~="${alt.id}"]`);
  assert((await altrow.locator('td[data-column-key="family:humanevalplus"]').innerText()).includes('134/164'));
  assert((await altrow.locator('td[data-column-key="family:bfcl"]').innerText()).includes('178/200'));
  assert.equal(await altrow.getByRole('link',{name:'R478',exact:true}).count(),0);
  report.checks.push('identical inference captures share coding/tool rows despite collection-limit differences; run links remain attached to their exact result');

  assert(!primaryRuns.some(r=>['R473','R475','R460','R468','R469','R470'].includes(r.exp)),'Partials and excluded benchmarks cannot enter this table');
  const low=primaryRuns.find(r=>r.exp==='R477');assert(low);
  const lowCell=page.locator(`tr[data-configuration-ids~="${low.id}"] td[data-column-key="family:bfcl"]`);
  assert((await lowCell.innerText()).includes('6/200'));
  let details;
  await omni.locator('td[data-column-key="family:bfcl"] button').click();details=await page.locator('.master-cell-dialog').innerText();
  for(const text of ['runtime_configuration_id','model_sha256','engine_version','build_id','797.789'])assert(details.includes(text),text);
  await page.getByRole('button',{name:'Schließen',exact:true}).click();
  report.checks.push('only complete qualified runs appear; low complete scores stay visible and details retain exact profiles, energy and audits; partial history remains untouched');

  assert((await omni.locator('td[data-column-key=average]').innerText()).includes('84,49 % · 2/3'),'Default must average both results without any selection');
  const displayedMeans=await page.locator('.master-table tbody tr').evaluateAll(rows=>rows.map(row=>({
   values:[...row.querySelectorAll('td[data-kind="family"] .master-score-line strong')].map(el=>Number(el.textContent.split('%')[0].trim().replace(',','.'))),
   mean:row.querySelector('td[data-column-key="average"]').textContent
  })));
  for(const row of displayedMeans){
   const mean=Number(row.mean.split('%')[0].trim().replace(',','.'));
   assert(Math.abs(mean-row.values.reduce((a,b)=>a+b,0)/row.values.length)<.02);
   assert(row.mean.includes(row.values.length+'/3'));
  }

  const settings=page.getByText('Tabelleneinstellungen',{exact:true});await settings.click();
  const choices=page.getByText('Benchmarkprotokolle auswählen',{exact:true});await choices.click();
  const keys=await page.evaluate(()=>{
   const d=window.V100Leaderboard;const r=e=>d.history.runs.find(r=>r.experiment_id===e&&r.counter_energy);
   return {coding:d.master.run_columns[r('R471').run_id],tools:d.master.run_columns[r('R478').run_id]};
  });
  await page.locator('select[data-protocol-family=humanevalplus]').selectOption(keys.coding);
  await page.locator('select[data-protocol-family=bfcl]').selectOption(keys.tools);
  await noBlankResultRows();
  assert.equal(await page.locator('.master-family-choice input[type=checkbox]').count(),0);
  const shown=await omni.locator('td[data-column-key=average]').innerText();
  const mean=Number(shown.split('%')[0].trim().replace(',','.'));
  assert(Math.abs(mean-(100*132/164+100*177/200)/2)<.011);assert(shown.includes('2/3'));
  assert((await omni.locator('td[data-column-key="family:terminal-bench"]').innerText()).startsWith('NICHT GEMESSEN'));
  for(const key of ['decode_tok_s','wall_per_task_s','output_tokens_per_task','energy_j_per_success','peak_vram_gib']){
   const cell=omni.locator(`td[data-column-key="summary:${key}"]`);assert(!(await cell.innerText()).includes('NICHT GEMESSEN'),key);
  }
  await omni.locator('td[data-column-key="summary:energy_j_per_success"] button').click();
  details=await page.locator('.master-cell-dialog').innerText();
  for(const text of ['upper_bound','lower','upper','R471','R478'])assert(details.includes(text),text);
  await page.getByRole('button',{name:'Schließen',exact:true}).click();
  await noBlankResultRows();await choices.click();await settings.click();await page.getByRole('button',{name:'Filter zurücksetzen',exact:true}).click();
  report.checks.push('automatic arithmetic mean includes every available complete category of the same configuration, displays 2/3 coverage without a zero for missing agents; compact pooled performance retains audit links and energy bounds');

  const search=page.getByRole('searchbox',{name:'Alle Parameter durchsuchen'});
  // Locate the existing global search by its stable placeholder if the browser
  // does not expose an explicit accessible name on this input.
  const globalSearch=await search.count()?search:page.locator('.master-toolbar input[type=search]').first();
  await globalSearch.fill('Qwen3.5');const visible=await page.locator('.master-table tbody tr').count();assert(visible>0&&visible<expected.rows);
  await page.getByRole('button',{name:'Filter zurücksetzen',exact:true}).click();assert.equal(await page.locator('.master-table tbody tr').count(),expected.rows);
  const preset=page.getByLabel('Ansicht',{exact:true});
  for(const name of ['Kompakt','Qualität','Geschwindigkeit','Energie','Vollständig']){
   await preset.selectOption(name);assert.equal(await page.locator('.master-table thead th[data-column-key^="family:"]').count(),3);
   await noBlankResultRows();
   assert.equal(await page.locator('.master-table thead th[data-column-key^="benchmark-"]').count(),0);
   const rendered=await page.evaluate(()=>{
    const M=window.V100MasterTable,v=M.comparisonView(M.build(window.V100Leaderboard));
    return v.columns.filter(c=>c.benchmark).map(c=>c.benchmark.protocol.benchmark_id);
   });assert(rendered.every(id=>expected.benchmarks.includes(id)));
  }
  await page.getByLabel('Filter: Kontext',{exact:true}).fill('>=8192');assert(await page.locator('.master-table tbody tr').count()>0);
  await page.getByRole('button',{name:'Filter zurücksetzen',exact:true}).click();
  report.checks.push('search, parameter filters and all presets work; none can reintroduce an additional benchmark or extra score column');

  await preset.selectOption('Kompakt');
  const avgHeader=page.locator('th[data-column-key=average] button');await avgHeader.click();await avgHeader.click();
  await settings.click();const pickerSummary=page.getByText('Spaltenauswahl nach Kategorien',{exact:true});await pickerSummary.click();
  const contextBox=page.locator('.master-column-picker input[data-column-key="runtime.context"]');await contextBox.setChecked(true);
  assert.equal(await page.locator('th[data-column-key="runtime.context"]').count(),1);
  await pickerSummary.click();await settings.click();
  const downloaded=page.waitForEvent('download');await page.locator('[data-action=export-csv]').click();const download=await downloaded;const csvPath=path.join(artifacts,'configuration-export.csv');await download.saveAs(csvPath);const csv=await fs.readFile(csvPath,'utf8');
  for(const text of ['source_runtime_configuration_ids','selected_protocols',keys.coding,keys.tools,'R478','NICHT GEMESSEN','mean_protocols','AVAILABLE_DISPLAYED_COMPLETE_CATEGORIES_ARITHMETIC_MEAN'])assert(csv.includes(text),text);
  assert(!csv.split(/\r?\n/)[0].includes('mbpp'),'No removed benchmark column in export');
  assert.equal(csv.split(/\r?\n/).length,expected.rows+1,'No hidden pagination or truncated CSV');
  assert.equal(await page.locator('.master-insights select option').count(),4,'Analysis offers only mean and three categories');
  assert.equal(await page.evaluate(()=>window.V100MasterTable.canonical(window.V100Leaderboard.history)),sourceBefore);
  report.checks.push('sorting, column picker and complete CSV retain identities/selected protocols while excluded benchmarks cannot affect the analysis or original history');

  assert.equal(await page.locator('[data-action=official-only]').count(),0,'No control may reintroduce partial/unqualified runs');
  await noBlankResultRows();
  const heights=await page.locator('.master-table tbody tr').evaluateAll(rows=>rows.map(r=>r.getBoundingClientRect().height));assert(Math.max(...heights)<=70);
  const style=await page.locator('.master-scroll').evaluate(el=>({max:getComputedStyle(el).maxHeight,overflow:getComputedStyle(el).overflowX,width:el.clientWidth,content:el.scrollWidth}));assert.equal(style.max,'none');assert(style.content>style.width);
  await page.locator('.master-scroll').scrollIntoViewIfNeeded();
  await page.screenshot({path:path.join(artifacts,'desktop-results.png'),animations:'disabled'});
  report.checks.push('complete-only comparison has no partial toggle; compact rows have uniform height and ordinary vertical page scrolling');

  const phone=await browser.newContext({viewport:{width:390,height:844},isMobile:true,deviceScaleFactor:1});await overrides(phone);const mobile=await phone.newPage();mobile.on('pageerror',e=>errors.push(e.message));
  await mobile.goto(new URL('configuration-comparison/',base).href,{waitUntil:'networkidle'});await mobile.locator('.master-table tbody tr').first().waitFor();
  assert.equal(await mobile.locator('select[data-action=comparison-view]').inputValue(),'models');
  const controlSizes=await mobile.locator('.master-toolbar label').evaluateAll(labels=>labels.map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})));
  assert(controlSizes.every(r=>r.width>=120&&r.height<=90),'Mobile controls must retain readable labels and normal heights');
  await mobile.screenshot({path:path.join(artifacts,'mobile-model-overview.png'),animations:'disabled'});
  await mobile.locator('select[data-action=comparison-view]').selectOption('configurations');
  assert.equal(await mobile.locator('.master-table tbody tr').count(),expected.rows);assert.equal(await mobile.locator('th[data-column-key^="family:"]').count(),3);
  const phoneSize=await mobile.evaluate(()=>({body:document.documentElement.scrollWidth,view:innerWidth,scroll:document.querySelector('.master-scroll').scrollWidth,client:document.querySelector('.master-scroll').clientWidth}));assert(phoneSize.body<=phoneSize.view+1);assert(phoneSize.scroll>phoneSize.client);
  await mobile.locator('.master-scroll').evaluate(el=>{el.scrollLeft=el.scrollWidth;});
  assert(await mobile.locator('.master-scroll').evaluate(el=>el.scrollLeft>0));
  await mobile.locator('.master-scroll').evaluate(el=>{el.scrollLeft=0;});
  await mobile.locator('.master-scroll').scrollIntoViewIfNeeded();
  await mobile.screenshot({path:path.join(artifacts,'mobile-results.png'),animations:'disabled'});
  report.checks.push('390px mobile layout keeps all category rows accessible through horizontal table scrolling without widening the page');
  for(const [name,tab] of [['desktop',page],['mobile',mobile]]){
   await tab.goto(base,{waitUntil:'networkidle'});
   assert.equal(await tab.locator('.lab-kpis>div').count(),4);
   assert.equal(await tab.locator('.lab-results>a').count(),3);
   assert.equal(await tab.locator('.lab-status>span').count(),6);
   assert(await tab.locator('.lab-result').allTextContents().then(v=>v.some(t=>t.includes('Not measured'))));
   const bounds=await tab.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));assert(bounds.width<=bounds.viewport+1);
   for(const href of await tab.locator('.lab-result').evaluateAll(a=>a.map(x=>x.getAttribute('href'))))assert(!href.endsWith('.md'),'HTML card links must target rendered routes');
   await tab.screenshot({path:path.join(artifacts,name+'-overview.png'),animations:'disabled',fullPage:true});
   await tab.goto(new URL('archive/',base).href,{waitUntil:'networkidle'});assert.equal(await tab.locator('.lab-links>a').count(),6);
  }
  await page.goto(new URL('experiments/R482/',base).href,{waitUntil:'networkidle'});
  assert(await page.locator('details.lab-evidence').count()>0);
  assert.equal(await page.locator('details.lab-evidence[open]').count(),0);
  report.checks.push('desktop/mobile overview exposes evidence-backed KPIs and three category cards without overflow; archive routes work and structured experiment evidence is collapsed, not deleted');
  for(const [name,tab] of [['desktop',page],['mobile',mobile]]){
   await tab.goto(new URL('screening/',base).href,{waitUntil:'networkidle'});
   const rows=tab.locator('#screening-table tbody tr');assert.equal(await rows.count(),screeningData.rows.length);
   for(const expected of screeningData.rows.filter(r=>r.configuration.tool_transport)){
    const adapted=rows.filter({hasText:expected.configuration.screening_configuration_id});assert.equal(await adapted.count(),1);
    assert.equal(await adapted.locator('small[title*="no native tool-training claim"]').count(),1);
    assert.match(await adapted.innerText(),/tool bridge/);
   }
   const omni=rows.filter({has:tab.locator('td:first-child',{hasText:/^OmniCoder-9B$/})});
   assert.match(await omni.innerText(),/13\/16/);assert.match(await omni.innerText(),/14\/16/);
   const alternate=rows.filter({has:tab.locator('td:first-child',{hasText:'bartowski Q6'})});
   assert.equal(await alternate.count(),1);assert.match(await alternate.innerText(),/14\/16/);
   assert.equal(await alternate.getByRole('link',{name:'R516',exact:true}).count(),1);
   const review=tab.getByRole('link',{name:'CPU review',exact:true,includeHidden:true});assert.equal(await review.count(),1);
   await review.evaluate(el=>el.closest('details').open=true);
   await review.click();await tab.waitForURL('**/audits/**');assert((await tab.locator('main').innerText()).includes('a6d64223c65f59269a00'));
   await tab.goto(new URL('screening/',base).href,{waitUntil:'networkidle'});
   const all=await rows.count();const expectedOmni=(await rows.locator('td:first-child').allTextContents()).filter(x=>x.includes('OmniCoder')).sort();await tab.locator('#screening-search').fill('OmniCoder');
   assert.deepEqual((await tab.locator('#screening-table tbody tr:visible td:first-child').allTextContents()).sort(),expectedOmni,'Search must retain all measured artifact profiles of the model');
   await tab.locator('#screening-search').fill('');assert.equal(await tab.locator('#screening-table tbody tr:visible').count(),all);
   await tab.locator('#screening-table thead button').first().click();
   await omni.locator('summary').click();assert.match(await omni.innerText(),/b0c1664c86338be2/);await omni.locator('summary').click();
   const bounds=await tab.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));assert(bounds.width<=bounds.viewport+2);
   await tab.screenshot({path:path.join(artifacts,name+'-screening.png'),animations:'disabled',fullPage:true});
  }
  report.checks.push('separate screening preserves all measured native profiles,16+16 development scores, search/sort/details and responsive layout; official rankings remain unchanged');
  for(const [name,tab] of [['desktop',page],['mobile',mobile]]){
   await tab.goto(new URL('pipeline-methods/#native-agent18-development-evidence',base).href,{waitUntil:'networkidle'});
   assert.equal(await tab.locator('#native-agent18-development-evidence').count(),1);
   if(qualificationExpected){
    const section=await tab.evaluate(()=>{const h=document.querySelector('#jarvis-qualification');if(!h)return null;const out=[];for(let n=h.nextElementSibling;n&&n.tagName!=='H2';n=n.nextElementSibling)out.push(n.innerText);return out.join('\n');});
    assert(section,'Current qualification section must exist');
    for(const c of qualificationExpected.candidates)assert(section.includes(c.profile),c.profile);
    assert(section.includes(qualificationExpected.validation.cases+' frozen cases / '+qualificationExpected.validation.generalization_groups+' related-task groups'));
    if(qualificationExpected.model_validation?.length){
     assert(!section.includes('zero model responses'));
     assert(section.includes('not Terminal-Bench or an official Agents score'));
     for(const r of qualificationExpected.model_validation){
      const row=tab.getByRole('link',{name:r.experiment_id,exact:true}).locator('xpath=ancestor::tr');
      const cells=await row.locator('td').allTextContents();
      assert.equal(cells[0].trim(),r.model);
      assert.equal(cells[1].trim(),r.metrics.solved+'/'+r.metrics.tasks);
      assert.equal(cells[2].trim(),r.metrics.task_phase_s.toFixed(2)+'s');
      assert.equal(cells[4].trim(),r.metrics.gpu_j_per_success_lower.toFixed(2)+'–'+r.metrics.gpu_j_per_success_upper.toFixed(2));
     }
     report.agent_validation33_profiles_verified=qualificationExpected.model_validation.length;
     if(qualificationExpected.decision_review){
      const decisions=tab.locator('#qualification-decisions');
      assert.equal(await decisions.locator('tbody tr').count(),qualificationExpected.decision_review.profiles.length);
      for(const d of qualificationExpected.decision_review.profiles){
       const row=decisions.getByRole('link',{name:'Evidence '+d.experiment_id,exact:true}).locator('xpath=ancestor::tr');
       const cells=await row.locator('td').allTextContents();
       assert.equal(cells[0].trim(),d.model);assert.equal(cells[1].trim(),d.policy_gate_passes+'/33');assert.equal(cells[2].trim(),d.reason);
      }
      report.qualification_decisions_verified=qualificationExpected.decision_review.profiles.length;
     }
    }else{
     assert(section.includes('zero model responses'));assert(section.includes('harness checks, not model scores'));
    }
    assert(section.includes('failed during startup, before any task'));assert(section.includes('No local official score'));
    assert(section.includes('1200s task allowance (400s per arm)'));
    report.qualification_shortlist_profiles_verified=qualificationExpected.candidates.length;
   }

   const validationTable=tab.getByRole('link',{name:validationExpected[0].experiment_id,exact:true}).locator('xpath=ancestor::table');
   assert.equal(await validationTable.locator('tbody tr').count(),validationExpected.length);
   for(const r of validationExpected){
    const link=validationTable.getByRole('link',{name:r.experiment_id,exact:true});assert.equal(await link.count(),1);
    const values=await link.locator('xpath=ancestor::tr/td').allTextContents();
    assert.equal(values[0].trim(),r.model);
    assert.equal(values[1].trim(),r.groups.coding.successes+'/'+r.groups.coding.completed);
    assert.equal(values[2].trim(),r.groups.tools.successes+'/'+r.groups.tools.completed);
   }
   report.reserved_validation_profiles_verified=validationExpected.length;

   const content=await tab.locator('main').innerText();
   for(const text of ['13/18','258.25','5447.82–5455.78','Not Terminal-Bench'])assert(content.includes(text),text);
   assert.equal(await tab.getByRole('link',{name:'R518',exact:true}).count(),1);
   assert(content.includes('Preflight / HTTP failures'));
   const nativeTable=tab.getByRole('link',{name:'R518',exact:true}).locator('xpath=ancestor::table');
   assert.equal(await nativeTable.locator('tbody tr').count(),nativeExpected.length);
   for(const experiment of nativeExpected){
    const m=experiment.aggregate_metrics.native_agent18_development;
    const link=nativeTable.getByRole('link',{name:experiment.id,exact:true});assert.equal(await link.count(),1);
    const row=await link.locator('xpath=ancestor::tr').innerText();
    for(const value of [m.solved+'/'+m.tasks,Number(m.task_phase_s).toFixed(2),String(m.technical_preflight_cases)+' / '+String(m.technical_request_errors)])assert(row.includes(value),experiment.id+': '+value);
   }
   report.agent_development_profiles_verified=nativeExpected.length;

   const roleResults=qualificationExpected?.multi_agent_plan?.results||[];
   if(roleResults.length){
    const table=tab.locator('#native-role-comparison');
    assert.equal(await table.locator('tbody tr').count(),roleResults.reduce((n,r)=>n+r.arms.length,0));
    let index=0;
    for(const result of roleResults)for(const arm of result.arms){
     const row=table.locator('tbody tr').nth(index++),cells=await row.locator('td').allTextContents();
     assert(cells[0].includes(arm.arm.replaceAll('_',' ')));
     assert.equal(cells[1].trim(),arm.solved+'/5');assert.equal(cells[2].trim(),arm.policy_gate_passes+'/5');
     assert.equal(cells[3].trim(),arm.arm_wall_s.toFixed(2)+'s');
     assert.equal(cells[5].trim(),arm.gpu_j_per_success_lower.toFixed(2)+'–'+arm.gpu_j_per_success_upper.toFixed(2));
     assert.equal(await row.getByRole('link',{name:result.experiment_id,exact:true}).count(),1);
    }
    assert(content.includes('five paired tasks'));assert(!content.includes('GPU source/admission review remains pending'));
    report.role_comparison_arms_verified=index;
    await table.scrollIntoViewIfNeeded();
    await tab.screenshot({path:path.join(artifacts,name+'-role-comparison.png'),animations:'disabled'});
   }

   const bounds=await tab.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));assert(bounds.width<=bounds.viewport+2);
   await tab.locator('#native-agent18-development-evidence').scrollIntoViewIfNeeded();
   await tab.screenshot({path:path.join(artifacts,name+'-agent-development.png'),animations:'disabled'});
  }
  report.checks.push('native Agent18 development outcomes and counter-cost bounds render on desktop/mobile with original experiment links, outside official agent rankings');
  const roleExpected=JSON.parse(await fs.readFile(path.join(__dirname,'../data/benchmark-register.json'),'utf8')).role_comparison;
  if(roleExpected){
   for(const width of [1600,390]){
    const tab=await context.newPage();await tab.setViewportSize({width,height:900});
    await tab.goto(new URL('configurations/',base).href,{waitUntil:'networkidle'});
    const content=await tab.locator('.md-content').innerText();
    assert(content.includes('Jarvis role selection'));assert(content.includes('NOT MEASURED'));assert(content.includes('no overall Champion'));
    const details=tab.locator('details').filter({has:tab.locator('summary', {hasText:'Observed Pareto tradeoffs'})}).first();
    await details.locator('summary').first().click();
    const tables=details.locator('table');assert.equal(await tables.count(),2);
    for(const [i,role]of ['coding','tools'].entries()){
     const points=roleExpected.categories[role].points;assert.equal(await tables.nth(i).locator('tbody tr').count(),points.length);
     for(const p of points){const row=tables.nth(i).getByRole('link',{name:p.experiment_id,exact:true}).locator('xpath=ancestor::tr');
      const cells=await row.locator('td').allTextContents();assert.equal(cells[2].trim(),p.solved+'/'+p.tasks);assert.equal(cells[6].trim(),p.pareto_status);}
    }
    const agentDetail=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Separate local Agent33 evidence'})}).first();
    await agentDetail.locator('summary').first().click();
    assert.equal(await agentDetail.locator('tbody tr').count(),roleExpected.agents_development.length);
    for(const p of roleExpected.agents_development){const row=agentDetail.getByRole('link',{name:p.experiment_id,exact:true}).locator('xpath=ancestor::tr');
     const cells=await row.locator('td').allTextContents();assert.equal(cells[2].trim(),p.solved+'/33');
     assert.equal(cells[3].trim(),p.policy_gate_passes===null?'NOT MEASURED / not recorded':p.policy_gate_passes+'/33');}
    const diagnostics=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Agent33 safety and output diagnostics'})}).first();
    await diagnostics.locator('summary').first().click();
    assert.equal(await diagnostics.locator('tbody tr').count(),roleExpected.agents_development.length);
    for(const p of roleExpected.agents_development){const d=p.quality_diagnostics;assert(d);
     const row=diagnostics.getByRole('link',{name:p.experiment_id,exact:true}).locator('xpath=ancestor::tr');
     const cells=await row.locator('td').allTextContents();assert.equal(cells[2].trim(),String(d.policy_violation_cases));
     assert.equal(cells[3].trim(),d.rejected_tool_call_cases+' / '+d.rejected_tool_call_events);
     assert.equal(cells[5].trim(),String(d.final_contract_failure_cases));
     assert.equal(cells[6].trim(),d.parse_failed_cases+' / '+d.parse_failed_rounds);}
    assert((await diagnostics.innerText()).includes('not executed production writes'));
    assert(await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'Role comparison overflows viewport');
    await tab.screenshot({path:path.join(artifacts,width===390?'mobile-role-selection.png':'desktop-role-selection.png'),animations:'disabled'});await tab.close();
   }
   report.checks.push('role-specific observed Pareto evidence preserves exact profiles, costs, development-agent separation and mobile layout');
  }
  for(const width of [1600,390]){
   const tab=await context.newPage();await tab.setViewportSize({width,height:900});
   await tab.goto(new URL('reproduce/',base).href,{waitUntil:'networkidle'});
   const content=await tab.locator('.md-content').innerText();
   assert(content.includes('PROPOSAL ONLY'));assert(content.includes('14,336'));assert(content.includes('1,200-second TASK'));
   assert(content.includes('not a runnable launch or broker approval'));assert(content.includes('bit-identical independent rebuild'));
   assert.equal(await tab.locator('pre code').filter({hasText:'--export-profile'}).count(),1);
   const detail=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Selected exact benchmark-profile pointers'})}).first();await detail.locator('summary').first().click();
   assert.equal(await detail.locator('tbody tr').count(),9);
   for(const a of await detail.locator('a[href*="configuration-profiles"]').all())assert(/cfg-[a-f0-9]{64}/.test(await a.getAttribute('href')));
   assert(await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'Reproduction proposal overflows viewport');
   await tab.screenshot({path:path.join(artifacts,width===390?'mobile-reproduction.png':'desktop-reproduction.png'),animations:'disabled'});await tab.close();
  }
  report.checks.push('exact profile export instructions and controlled deployment proposal preserve broker/resource boundaries on desktop/mobile');
  const sourcePackage=JSON.parse(await fs.readFile(path.join(__dirname,'../data/benchmark-register.json'),'utf8')).engine_source_reviews.find(r=>r.reproduction_package)?.reproduction_package;
  if(sourcePackage){
   for(const a of sourcePackage.source_assets){const response=await context.request.get(new URL(a.url,base).href);assert.equal(response.status(),200);const bytes=await response.body();assert.equal(bytes.length,a.bytes);assert.equal(require('node:crypto').createHash('sha256').update(bytes).digest('hex'),a.sha256);}
   report.checks.push('all four published MIT source-reproduction assets match their archived exact byte hashes');
  }

  const finalRegister=JSON.parse(await fs.readFile(path.join(__dirname,'../data/benchmark-register.json'),'utf8'));
  if(finalRegister.final_evidence_review){
   const expected=finalRegister.final_evidence_review;
   for(const width of [1600,390]){
    const tab=await context.newPage();await tab.setViewportSize({width,height:900});
    await tab.goto(new URL('best-of-v100-2026/',base).href,{waitUntil:'networkidle'});
    const text=await tab.locator('.md-content').innerText();const released=!!roleExpected&&!!JSON.parse(await fs.readFile(path.join(__dirname,'../data/benchmark-register.json'),'utf8')).final_research_gate;
    if(released){assert(text.includes('Reviewed research decision'));assert(text.includes('available ahead of the deadline'));assert(!text.includes('freeze audit is still pending'));assert(text.includes('not a claimed31-October execution'));
     const checklist=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Completion scope and retained limits'})}).first();await checklist.locator('summary').first().click();assert.equal(await checklist.locator('tbody tr').count(),10);}
    else{assert(text.includes('Pre-freeze draft'));assert(text.includes('freeze audit is still pending'));}assert(text.includes('NOT MEASURED / TECHNICALLY BLOCKED'));assert(text.includes(expected.sample_count.toLocaleString('en-US')));assert(text.includes('LOKAL GEMESSEN'));assert(text.includes('NICHT VERIFIZIERT'));
    const detail=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Original capture-level hardware evidence'})}).first();await detail.locator('summary').first().click();assert.equal(await detail.locator('tbody tr').count(),expected.capture_count);
    assert(await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'Final snapshot overflows viewport');await tab.screenshot({path:path.join(artifacts,width===390?'mobile-final-snapshot.png':'desktop-final-snapshot.png'),animations:'disabled'});await tab.close();
   }
   report.checks.push('dated research decision preserves release gates, local measurements, missing official agents and bounded hardware evidence');
  }
  const issueExpected=JSON.parse(await fs.readFile(path.join(__dirname,'../data/research-issues.json'),'utf8'));
  for(const width of [1600,390]){
   const tab=await context.newPage();await tab.setViewportSize({width,height:900});await tab.goto(new URL('questions/',base).href,{waitUntil:'networkidle'});
   const table=tab.locator('.md-content table').first();assert.equal(await table.locator('tbody tr').count(),issueExpected.filter(x=>x.github_state==='OPEN').length);
   const closed=tab.locator('details').filter({has:tab.locator('summary',{hasText:'Closed scoped workflow records'})}).first();await closed.locator('summary').first().click();assert.equal(await closed.locator('tbody tr').count(),issueExpected.filter(x=>x.github_state==='CLOSED').length);
   assert(await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'Issue registry overflows viewport');await tab.close();
  }
  report.checks.push('current issue snapshot preserves open/closed workflow states, scientific dispositions and mobile access');
  const pipelineExpected=JSON.parse(await fs.readFile(path.join(__dirname,'../data/pipeline-performance.json'),'utf8'));
  for(const [name,width] of [['desktop',1600],['mobile',390]]){
   const tab=await context.newPage();await tab.setViewportSize({width,height:900});
   await tab.goto(new URL('pipeline-performance/',base).href,{waitUntil:'networkidle'});
   const content=await tab.locator('.md-content').innerText();
   assert(content.includes(pipelineExpected.observed_at_utc));assert(content.includes('not a live monitor'));
   const table=tab.locator('.md-content table').first();assert.equal(await table.locator('tbody tr').count(),pipelineExpected.experiments.length);
   const partial=table.getByRole('link',{name:'R538',exact:true}).locator('xpath=ancestor::tr');
   assert((await partial.innerText()).includes('PARTIAL'));assert.equal((await partial.locator('td').allTextContents())[4].trim(),'NOT MEASURED');
   assert((await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2)),'Pipeline page overflows viewport');
   await tab.screenshot({path:path.join(artifacts,name+'-pipeline.png'),animations:'disabled'});await tab.close();
  }
  report.checks.push('pipeline snapshot, preserved partial task clock and desktop/mobile layout');
  const mtpConfirmations=JSON.parse(await fs.readFile(path.join(__dirname,'../data/experiments.json'),'utf8')).filter(e=>e.mtp_confirmation);
  for(const experiment of mtpConfirmations){
   const mtpExpected=experiment.mtp_confirmation;
   for(const width of [1600,390]){
    const tab=await context.newPage();await tab.setViewportSize({width,height:900});
    await tab.goto(new URL('experiments/'+experiment.id+'/',base).href,{waitUntil:'networkidle'});
    const table=tab.getByRole('columnheader',{name:'Response seconds',exact:true}).locator('xpath=ancestor::table');
    assert.equal(await table.locator('tbody tr').count(),2);
    for(let i=0;i<2;i++){
     const cells=await table.locator('tbody tr').nth(i).locator('td').allTextContents(),arm=mtpExpected.arms[i];
     assert.equal(cells[0].trim(),arm.arm);assert.equal(Number(cells[3]),Number(arm.response_wall_s.toFixed(3)));
    }
    assert((await tab.locator('.md-content').innerText()).includes('Not an official benchmark score or Champion'));
    assert(await tab.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await tab.close();
   }
   report.checks.push(experiment.id+': fresh MTP A/B development response metrics and setup costs remain distinct on desktop/mobile');
  }
  assert.deepEqual(errors,[]);report.console_errors=errors;report.passed=true;
 }finally{await browser.close();await fs.writeFile(path.join(artifacts,'browser-report.json'),JSON.stringify(report,null,2)+'\n');}
 process.stdout.write(JSON.stringify(report)+'\n');
}
main().catch(error=>{process.stderr.write(error.stack+'\n');process.exitCode=1;});
