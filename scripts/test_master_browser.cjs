/* Optional real-browser acceptance test. No GPU, credentials or model requests.
 * PLAYWRIGHT_MODULE can point to an isolated Playwright installation.
 * node scripts/test_master_browser.cjs <site-root-url> <artifact-directory>
 */
'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const base = process.argv[2];
const artifacts = process.argv[3];
if (!base || !artifacts) throw new Error('Supply the built/published site root URL and an artifact directory');
async function main() {
  await fs.mkdir(artifacts, { recursive: true });
  const args = ['--disable-gpu'];
  if (process.env.BROWSER_NO_SANDBOX === '1') args.push('--no-sandbox');
  const browser = await chromium.launch({ headless: true, args });
  const errors = [], report = { site: base, checks: [], GPU_access: false };
  try {
    const context = await browser.newContext({ viewport: { width: 1600, height: 1000 }, acceptDownloads: true });
    async function developmentAssets(context) {
      if (!process.env.MASTER_SOURCE_DIR) return;
      await context.route('**/javascripts/master-table.js*', route => route.fulfill({ path: path.join(process.env.MASTER_SOURCE_DIR, 'docs/javascripts/master-table.js') }));
      await context.route('**/stylesheets/lab.css*', route => route.fulfill({ path: path.join(process.env.MASTER_SOURCE_DIR, 'docs/stylesheets/lab.css') }));
      report.development_source_override = true;
    }
    await developmentAssets(context);
    const page = await context.newPage();
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(new URL('configuration-comparison/', base).href, { waitUntil: 'networkidle' });
    await page.locator('.master-table tbody tr').first().waitFor();
    const expected = await page.evaluate(() => {
      const d = window.V100Leaderboard, m = window.V100MasterTable.comparisonView(window.V100MasterTable.build(d));
      return { profiles: m.rows.length, columns: m.columns.filter(c => c.kind !== 'family' && c.key !== 'engine.build_id').length, families: m.families.length,
        official: m.benchmarks.filter(b => b.scope === 'OFFICIAL_LOCAL').length,
        currentFamily: m.families.find(f => f.protocols.some(b => b.scope === 'OFFICIAL_LOCAL' && m.rows.some(r => r.scores[b.key]?.n)))?.key,
        missingFamily: m.families.find(f => f.protocols.some(b => b.scope === 'OFFICIAL_LOCAL' && !m.rows.some(r => r.scores[b.key]?.n)))?.id,
        current: m.benchmarks.find(b => b.scope === 'OFFICIAL_LOCAL' && m.rows.some(r => r.scores[b.key]?.n))?.key,
        missing: m.benchmarks.find(b => b.scope === 'OFFICIAL_LOCAL' && !m.rows.some(r => r.scores[b.key]?.n))?.key };
    });
    assert.equal(await page.locator('.master-table tbody tr').count(), expected.profiles);
    assert.equal(await page.locator('.master-benchmark-choices input').count(), expected.families);
    assert.equal(await page.locator('.master-table th[data-column-key="family:humanevalplus"]').count(), 1);
    assert.equal(await page.locator('.master-table thead th[data-column-key^="benchmark-"]').count(), 0);
    assert.equal(await page.locator('.master-table tbody td[data-kind=metric]').count(), 0);
    assert.equal(await page.locator('.master-family-choice[data-family-id^=local-]').count(), 0);
    assert.equal(await page.locator('.master-table th[data-column-key="engine.build_id"]').count(), 0);
    const engineVersions = await page.locator('.master-table tbody td[data-column-key="engine.version"]').allTextContents();
    assert(engineVersions.every(v => v !== 'NICHT ERFASST'), 'Known source revisions must be displayed without fabricating release tags');
    const modelNames = await page.locator('.master-table tbody td[data-column-key="model.name"] a').allTextContents();
    assert(modelNames.includes('OmniCoder 9B'));
    assert(modelNames.every(v => !/OmniCoder2|OmniCoder-2|V1\/V2/i.test(v)), 'One OmniCoder family label; historic IDs preserved separately');
    assert.equal(await page.locator('.master-benchmark-choices select[data-protocol-family]').count(), expected.families);
    assert((await page.locator('.master-counter').innerText()).includes(String(expected.profiles)));
    assert.equal(await page.locator('.master-pagination').count(), 0);
    assert.equal(await page.locator('.md-content table').count(),1,'Exactly one central table, including optional analysis');
    const partials = await page.evaluate(() => {
      const m=window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard));
      return m.rows.flatMap(row=>row.runs.filter(r=>r.status==='PARTIAL').map(r=>({id:row.id,solved:r.solved,tasks:r.tasks})));
    });
    assert(partials.length>=3,'Retained LFM and MiMo partial benchmark records');
    for(const r of partials){const cell=page.locator(`.master-table tr[data-configuration-id="${r.id}"] td[data-column-key="family:humanevalplus"]`);assert((await cell.textContent()).includes(`${r.solved}/${r.tasks}`));assert((await cell.textContent()).includes('PARTIAL'));}
    report.checks.push('exactly one table; partial results visible by default in the same HumanEval column with original denominators');
    const toolCategories = await page.evaluate(() => window.V100Leaderboard.history.runs.filter(r => r.benchmark_id === 'bfcl-v4-simple-python-full400' && r.official_eligible));
    for (const run of toolCategories) {
      assert.equal(run.tasks, 400);
      const cell = page.locator(`.master-table tr[data-configuration-id="${run.runtime_configuration_id}"] td[data-column-key="family:bfcl"]`);
      assert((await cell.textContent()).includes(`${run.solved}/${run.tasks}`));
      assert((await cell.textContent()).includes('OFFIZIELL'));
      assert.equal(run.qualification_audit.category_only, true);
      assert.equal(run.qualification_audit.official_category, 'simple_python');
    }
    if(toolCategories.length) report.checks.push('full native BFCL Python category appears in the same BFCL column with exact400 denominator and category-only qualification');
    const gemmaCoding=await page.evaluate(()=>window.V100Leaderboard.history.runs.find(r=>r.experiment_id==='R464'&&r.counter_energy));
    if(gemmaCoding){
      assert.equal(gemmaCoding.solved,156);assert.equal(gemmaCoding.tasks,164);assert.equal(gemmaCoding.official_eligible,true);
      const row=page.locator(`.master-table tr[data-configuration-id="${gemmaCoding.runtime_configuration_id}"]`);
      const text=await row.locator('td[data-column-key="family:humanevalplus"]').textContent();assert(text.includes('156/164')&&text.includes('OFFIZIELL'));
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Energie');
      const protocol=await page.evaluate(id=>window.V100Leaderboard.master.run_columns[id],gemmaCoding.run_id);
      assert.notEqual((await row.locator(`td[data-column-key="metric:${protocol}:counter_energy.j_per_success_lower"]`).textContent()).trim(),'NICHT ERFASST');
      assert.equal((await row.locator(`td[data-column-key="metric:${protocol}:gpu_j_per_success"]`).textContent()).trim(),'NICHT ERFASST');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Kompakt');
      report.checks.push('Gemma native156/164 coding result has its own full benchmark identity and164-task reported energy without imputed integral');
    }
    const qwen38=await page.evaluate(()=>window.V100Leaderboard.history.runs.find(r=>r.experiment_id==='R462'&&r.counter_energy));
    if(qwen38){
      assert.equal(qwen38.solved,383);assert.equal(qwen38.tasks,400);
      const row=page.locator(`.master-table tr[data-configuration-id="${qwen38.runtime_configuration_id}"]`);
      assert((await row.locator('td[data-column-key="family:bfcl"]').textContent()).includes('383/400'));
      assert((await row.locator('td[data-column-key="requested.MTP"]').textContent()).includes('Aus'));
      const sampleCount=await page.evaluate(id=>{const d=window.V100Leaderboard,m=window.V100MasterTable.build(d),r=m.rows.find(r=>r.id===id);const run=d.history.runs.find(x=>x.experiment_id==='R462'&&x.counter_energy);return r.scores[d.master.run_columns[run.run_id]].n;},qwen38.runtime_configuration_id);
      assert.equal(sampleCount,1);
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Energie');
      const protocol=await page.evaluate(id=>window.V100Leaderboard.master.run_columns[id],qwen38.run_id);
      assert.notEqual((await row.locator(`td[data-column-key="metric:${protocol}:counter_energy.j_per_success_lower"]`).textContent()).trim(),'NICHT ERFASST');
      assert.equal((await row.locator(`td[data-column-key="metric:${protocol}:gpu_j_per_success"]`).textContent()).trim(),'NICHT ERFASST');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Kompakt');
      report.checks.push('Qwen3.8 counter supplement is visible for383/400 while both history views count as one observation');
    }
    const ornithPrefix=await page.evaluate(()=>window.V100Leaderboard.history.runs.find(r=>r.experiment_id==='R460'));
    if(ornithPrefix){
      assert.equal(ornithPrefix.solved,85);assert.equal(ornithPrefix.tasks,93);assert.equal(ornithPrefix.intended_tasks,164);assert.equal(ornithPrefix.official_eligible,false);
      const row=page.locator(`.master-table tr[data-configuration-id="${ornithPrefix.runtime_configuration_id}"]`);
      const cell=await row.locator('td[data-column-key="family:humanevalplus"]').textContent();assert(cell.includes('85/93')&&cell.includes('PARTIAL'));
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Vollständig');
      const protocol=await page.evaluate(id=>window.V100Leaderboard.master.run_columns[id],ornithPrefix.run_id);
      assert.notEqual((await row.locator(`td[data-column-key="metric:${protocol}:counter_energy.j_per_success_lower"]`).textContent()).trim(),'NICHT ERFASST');
      assert.equal((await row.locator(`td[data-column-key="metric:${protocol}:gpu_j_per_success"]`).textContent()).trim(),'NICHT ERFASST');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Kompakt');
      report.checks.push('Ornith93 coding prefix remains PARTIAL in the same table; counter energy covers exactly93 tasks and85 successes');
    }
    const gemma=await page.evaluate(()=>window.V100Leaderboard.history.runs.find(r=>r.experiment_id==='R458'));
    if(gemma){
      assert.equal(gemma.solved,374);assert.equal(gemma.tasks,400);assert.equal(gemma.official_eligible,true);assert.equal(gemma.gpu_j,null);
      const row=page.locator(`.master-table tr[data-configuration-id="${gemma.runtime_configuration_id}"]`);
      assert((await row.locator('td[data-column-key="family:bfcl"]').textContent()).includes('374/400'));
      assert((await row.locator('td[data-column-key="requested.thinking"]').textContent()).includes('Aus'));
      assert.equal((await row.locator('td[data-column-key="model.quantization"]').textContent()).trim(),'Q4_0');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Energie');
      const protocol=await page.evaluate(id=>window.V100Leaderboard.master.run_columns[id],gemma.run_id);
      assert.notEqual((await row.locator(`td[data-column-key="metric:${protocol}:counter_energy.j_per_success_lower"]`).textContent()).trim(),'NICHT ERFASST');
      assert.equal((await row.locator(`td[data-column-key="metric:${protocol}:gpu_j_per_success"]`).textContent()).trim(),'NICHT ERFASST');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Kompakt');
      report.checks.push('Gemma full400 native QAT profile uses explicit thinking-off and distinct counter energy without filling missing integral data');
    }
    const ornith=await page.evaluate(() => window.V100Leaderboard.history.runs.find(r => r.experiment_id==='R457'));
    if(ornith){
      assert.equal(ornith.solved,369);assert.equal(ornith.tasks,400);assert.equal(ornith.gpu_j,null);assert.equal(ornith.gpu_j_per_success,null);
      const row=page.locator(`.master-table tr[data-configuration-id="${ornith.runtime_configuration_id}"]`);
      assert((await row.locator('td[data-column-key="family:bfcl"]').textContent()).includes('369/400'));
      assert((await row.locator('td[data-column-key="requested.thinking"]').textContent()).includes('Ein'));
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Energie');
      const protocol=await page.evaluate(id=>window.V100Leaderboard.master.run_columns[id],ornith.run_id);
      const lower=row.locator(`td[data-column-key="metric:${protocol}:counter_energy.j_per_success_lower"]`);
      assert.equal(await lower.count(),1);assert.notEqual((await lower.textContent()).trim(),'NICHT ERFASST');
      assert.equal((await row.locator(`td[data-column-key="metric:${protocol}:gpu_j_per_success"]`).textContent()).trim(),'NICHT ERFASST');
      await page.getByLabel('Ansicht',{exact:true}).selectOption('Kompakt');
      report.checks.push('Ornith400 exact thinking profile shows separate energy-counter bounds; invalid power integral stays unknown');
    }
    const mimoTools = await page.evaluate(() => window.V100Leaderboard.history.runs.find(r => r.experiment_id === 'R456'));
    if (mimoTools) {
      assert.equal(mimoTools.tasks, 400); assert.equal(mimoTools.solved, 320);
      assert.equal(mimoTools.official_eligible, true);
      const row=page.locator(`.master-table tr[data-configuration-id="${mimoTools.runtime_configuration_id}"]`);
      assert((await row.locator('td[data-column-key="family:bfcl"]').textContent()).includes('320/400'));
      assert.equal((await row.locator('td[data-column-key="model.quantization"]').textContent()).trim(), 'Q8_0');
      assert((await row.locator('td[data-column-key="requested.thinking"]').textContent()).includes('Ein'));
      assert.equal(mimoTools.practical_protocol.complete, 398);
      report.checks.push('MiMo400 native result uses its own exact thinking/Q8 profile; capped replies remain included failures');
    }
    const reusedTools = await page.evaluate(() => window.V100Leaderboard.history.runs.find(r => r.experiment_id === 'R455'));
    if (reusedTools) {
      assert.equal(reusedTools.solved, 372); assert.equal(reusedTools.tasks, 400);
      for (const k of ['wall_s', 'gpu_j', 'gpu_j_per_success']) assert.equal(reusedTools[k], null);
      assert.equal(reusedTools.matched_performance.tasks, 360);
      assert.equal(reusedTools.matched_performance.solved, 335);
      await page.getByLabel('Ansicht', { exact: true }).selectOption('Energie');
      const row = page.locator(`.master-table tr[data-configuration-id="${reusedTools.runtime_configuration_id}"]`);
      const bounds = row.locator('td[data-column-key$="matched_performance.counter_energy.lower_j"]');
      assert.equal(await bounds.count(), 1);
      assert.notEqual((await bounds.textContent()).trim(), 'NICHT ERFASST');
      assert((await page.locator('th[data-column-key$="matched_performance.counter_energy.lower_j"]').textContent()).includes('Neue Aufgaben:'));
      await page.getByLabel('Ansicht', { exact: true }).selectOption('Kompakt');
      report.checks.push('Bonsai400 quality keeps360-task energy bounds separate; no fabricated full400 costs');
    }
    const mimo = await page.evaluate(() => window.V100Leaderboard.history.runs.find(r => r.experiment_id === 'R454' && r.official_eligible));
    if (mimo) {
      const row = page.locator(`.master-table tr[data-configuration-id="${mimo.runtime_configuration_id}"]`);
      assert((await row.locator('td[data-column-key="family:humanevalplus"]').textContent()).includes(`${mimo.solved}/${mimo.tasks}`));
      assert.equal((await row.locator('td[data-column-key="model.quantization"]').textContent()).trim(), 'Q8_0');
      assert((await row.locator('td[data-column-key="requested.thinking"]').textContent()).includes('Ein'));
      report.checks.push('MiMo full164 score, verified Q8 precision and explicit thinking are present in the same master table');
    }


    for (const legacy of ['benchmarks/', 'supplemental-comparison/']) {
      const old = await context.newPage();
      await old.goto(new URL(legacy, base).href, { waitUntil: 'networkidle' });
      await old.waitForURL('**/configuration-comparison/**');
      await old.locator('.master-table tbody tr').first().waitFor();
      assert.equal(await old.locator('.md-content table').count(), 1);
      assert.equal(await old.locator('.master-table tbody tr').count(), expected.profiles);
      await old.close();
    }
    const nav = await page.locator('.md-nav--primary').innerText();
    assert(!nav.includes('Supplemental Model Comparisons'));
    assert(!nav.includes('Local Supplemental Benchmarks'));
    report.checks.push('legacy result URLs redirect to the same table; no competing comparison navigation');

    const initialIds = await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.dataset.configurationId));
    const measuredIds = await page.evaluate(() => window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard)).rows.map(r => r.id));
    assert.deepEqual(initialIds.slice().sort(), measuredIds.slice().sort());
    const geometry = await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.getBoundingClientRect().height));
    assert(Math.max(...geometry) <= 52, 'Compact rows including offscreen cells: ' + Math.max(...geometry));
    assert(Math.max(...geometry) - Math.min(...geometry) <= 2, 'Uniform result row heights');
    assert.equal(await page.locator('.master-scroll').evaluate(e => getComputedStyle(e).maxHeight), 'none');
    assert(await page.locator('.master-scroll').evaluate(e => e.clientHeight >= e.scrollHeight - 2));
    assert.equal(await page.locator('.master-table thead').evaluate(e => getComputedStyle(e).position), 'sticky');
    assert.equal(await page.locator('.master-table tbody td').first().evaluate(e => getComputedStyle(e).position), 'sticky');
    report.checks.push('rows, register definitions, sticky header and model column');

    await page.getByText('Benchmarkprotokolle und Durchschnitt auswählen', { exact: true }).click();
    if (expected.current && expected.missing) {
      await page.locator(`input[data-family-key="${expected.missingFamily}"]`).check();
      assert((await page.locator('.master-counter').innerText()).includes('0 mit vollständigem'));
      const averageCells = await page.locator('.master-table tbody td[data-column-key="average"]').allTextContents();
      assert(averageCells.every(s => s === 'NICHT BERECHENBAR'));
      await page.locator(`input[data-family-key="${expected.missingFamily}"]`).uncheck();
      await page.locator(`.master-table th[data-column-key="${expected.currentFamily}"] button`).click();
      const result = await page.locator(`.master-table tbody td[data-column-key="${expected.currentFamily}"] strong`).allTextContents();
      const numbers = result.map(s => Number(s.replace('%', '').replaceAll('.', '').replace(',', '.').trim()));
      assert(numbers.every((x, i) => !i || numbers[i - 1] >= x));
      await page.locator('.master-score-details').first().click();
      assert(await page.locator('.master-cell-dialog a[href*="/audits/"]').count() > 0);
      assert(await page.locator('.master-cell-dialog a[href*="/experiments/"]').count() > 0);
      assert((await page.locator('.master-cell-dialog pre').innerText()).includes('audit_hash'));
      await page.getByRole('button', { name: 'Schließen', exact: true }).click();
      report.checks.push('missing benchmark prevents average; numeric sorting; direct audit/run links');
    }

    await page.getByLabel('Ansicht', { exact: true }).selectOption('Qualität');
    const contextFilter = page.getByRole('searchbox', { name: 'Filter: Kontext', exact: true });
    await contextFilter.fill('>=16384');
    const rows = await page.locator('.master-table tbody tr').count();
    if (rows) {
      const values = await page.locator('.master-table tbody td[data-column-key="runtime.context"]').allTextContents();
      assert(values.every(v => Number(v) >= 16384));
    }
    await page.getByRole('button', { name: 'Filter zurücksetzen', exact: true }).click();
    const global = page.getByRole('searchbox', { name: 'Modell, Engine, Parameter oder Experiment suchen', exact: true });
    await global.fill('Bonsai');
    assert(await page.locator('.master-table tbody tr').count() > 0);
    const expectedSearch = await page.evaluate(() => {
      const M = window.V100MasterTable;
      return M.comparisonView(M.build(window.V100Leaderboard)).rows.filter(r => M.canonical({ values: r.values, runs: r.runs }).toLowerCase().includes('bonsai')).map(r => r.id);
    });
    assert((await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.dataset.configurationId))).every(id => expectedSearch.includes(id)));
    await global.fill(''); await page.getByLabel('Ansicht', { exact: true }).selectOption('Kompakt'); report.checks.push('per-parameter numeric filter and global search');

    const picker = page.locator('.master-panel').filter({ has: page.locator('.master-column-picker') });
    await picker.locator('summary').first().click();
    const pickerSearch = page.getByRole('searchbox', { name: 'Spalten suchen', exact: true });
    await pickerSearch.fill('model.artifact_sha256');
    await picker.locator('input[data-column-key="model.artifact_sha256"]').check();
    assert.equal(await page.locator('.master-table th[data-column-key="model.artifact_sha256"]').count(), 1);
    await pickerSearch.fill(''); await picker.locator('summary').first().click();
    report.checks.push('categorized searchable column picker');

    const mode = page.getByLabel('Durchschnittsmodus', { exact: true });
    await mode.selectOption('exploratory');
    assert.equal(await page.locator('.master-benchmark-choices input:disabled').count(), 0);
    await mode.selectOption('official');
    const disabledScopes = await page.locator('.master-benchmark-choices input:not(:disabled)').evaluateAll(inputs => inputs.map(i => window.V100Leaderboard.master.benchmark_columns.find(b => b.key === i.value).scope));
    assert(disabledScopes.every(s => s === 'OFFICIAL_LOCAL'));
    report.checks.push('official-only average rejects historical and supplemental protocols');

    const humanSelect = page.locator('select[data-protocol-family=humanevalplus]');
    const human = await page.evaluate(() => {
      const m = window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard)), f = m.families.find(f => f.id === 'humanevalplus');
      return { official: window.V100MasterTable.defaultProtocol(f), historical: f.protocols.find(p => p.scope === 'HISTORICAL' && p.records)?.key, original: JSON.stringify(window.V100Leaderboard.history) };
    });
    async function verifyHumanProtocol(key) {
      const observations = await page.evaluate(key => {
        const m = window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard));
        return [...document.querySelectorAll('.master-table tbody tr')].map(tr => {
          const expected = m.rows.find(r => r.id === tr.dataset.configurationId).scores[key]?.score ?? null;
          const cell = tr.querySelector('td[data-column-key="family:humanevalplus"]');
          const strong = cell.querySelector('strong');
          return { expected, actual: strong ? Number(strong.textContent.replace('%', '').replaceAll('.', '').replace(',', '.').trim()) : null, text: cell.textContent };
        });
      }, key);
      observations.forEach(o => { if (o.expected === null) { assert.equal(o.actual, null); assert.equal(o.text, 'NICHT ERFASST'); } else assert(Math.abs(o.actual - o.expected) <= .0051); });
    }
    assert.equal(await page.locator('.md-content table').count(),1,'Only one table on the central page');
    await humanSelect.selectOption(human.official); await verifyHumanProtocol(human.official);
    assert(human.historical);
    await humanSelect.selectOption(human.historical); await verifyHumanProtocol(human.historical);
    assert(await page.locator('input[data-family-key=humanevalplus]').isDisabled());
    await mode.selectOption('exploratory');
    assert(!(await page.locator('input[data-family-key=humanevalplus]').isDisabled()));
    await page.locator('input[data-family-key=humanevalplus]').check();
    assert.equal(await page.locator('input[data-family-key=humanevalplus]').count(), 1);
    await humanSelect.selectOption(human.official); await mode.selectOption('official');
    await verifyHumanProtocol(human.official);
    assert.equal(await page.evaluate(() => JSON.stringify(window.V100Leaderboard.history)), human.original);
    report.checks.push('one HumanEval family, exact protocol switching, no historic fallback or duplicate weighting, immutable scores');

    const presets = page.getByLabel('Ansicht', { exact: true });
    for (const preset of ['Qualität', 'Geschwindigkeit', 'Energie', 'Vollständig']) {
      await presets.selectOption(preset);
      assert(await page.locator('.master-table tbody tr').count() > 0);
      assert.equal(await page.locator('.master-table th[data-column-key="engine.build_id"]').count(), 0, 'Build identity stays in details/picker, not presets');
      if (preset === 'Vollständig') assert.equal(await page.locator('.master-table thead tr:first-child th').count(), expected.columns);
    }
    const fullValue = page.locator('.master-table td[data-column-key="start_parameters.argv"] button').first();
    if (await fullValue.count()) {
      await fullValue.click(); await page.locator('.master-cell-dialog').waitFor({ state: 'visible' });
      assert((await page.locator('.master-cell-dialog pre').innerText()).includes('--'));
      await page.getByRole('button', { name: 'Schließen', exact: true }).click();
    }
    await presets.selectOption('Kompakt'); report.checks.push('all presets, full parameter coverage and inline full-value viewer');

    const downloadEvent = page.waitForEvent('download');
    await page.getByRole('button', { name: 'CSV exportieren', exact: true }).click();
    const download = await downloadEvent; const downloaded = path.join(artifacts, 'configuration-export.csv'); await download.saveAs(downloaded);
    const csv = await fs.readFile(downloaded, 'utf8'); assert(csv.includes('runtime_configuration_id')); assert(csv.includes('NICHT ERFASST')); assert(csv.includes('mean_percent')); assert(csv.includes('selected_protocols')); assert(csv.includes('evaluated_task_set_hash')); assert(csv.includes('qualification_track'));
    const allIds = await page.evaluate(() => window.V100MasterTable.comparisonView(window.V100MasterTable.build(window.V100Leaderboard)).rows.map(r => r.id));
    assert(allIds.every(id => csv.includes(id))); report.checks.push('CSV contains all filtered configurations, exact IDs and missing markers');
    assert(await page.locator('.master-insights ol li').count() > 0);
    assert((await page.locator('.master-insights').innerText()).includes('Korrelation ist keine Kausalität'));
    report.checks.push('Top-5 analysis and non-causal interpretation');

    const onlyOfficial = page.locator('input[data-action=official-only]');
    await onlyOfficial.check();
    const officialIds = await page.evaluate(() => [...new Set(window.V100Leaderboard.history.runs.filter(r => r.official_eligible === true).map(r => r.runtime_configuration_id))]);
    assert.deepEqual((await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.dataset.configurationId))).sort(), officialIds.sort());
    await onlyOfficial.uncheck(); assert.equal(await page.locator('.master-table tbody tr').count(), expected.profiles);
    report.checks.push('official-only filter is optional; all measured statuses return by default');
    await page.locator('.master-table').evaluate(e => window.scrollTo(0, window.scrollY + e.getBoundingClientRect().top + 200));
    await page.waitForTimeout(100);
    const headerY = await page.locator('.master-table thead').evaluate(e => e.getBoundingClientRect().top);
    assert(headerY >= 0 && headerY < 120, 'Header follows document scrolling: ' + headerY);
    const stickyBefore = await page.locator('.master-table tbody td').first().boundingBox();
    await page.locator('.master-scroll').evaluate(e => { e.scrollLeft = e.scrollWidth; });
    const stickyAfter = await page.locator('.master-table tbody td').first().boundingBox();
    assert(Math.abs(stickyAfter.x - stickyBefore.x) <= 2);
    await page.screenshot({ path: path.join(artifacts, 'desktop-results.png'), animations: 'disabled' });
    await context.close();

    const mobile = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    await developmentAssets(mobile);
    const phone = await mobile.newPage(); phone.on('pageerror', e => errors.push(e.message));
    await phone.goto(new URL('configuration-comparison/', base).href, { waitUntil: 'networkidle' });
    await phone.locator('.master-table tbody tr').first().waitFor();
    const layout = await phone.evaluate(() => ({ page: document.documentElement.scrollWidth, viewport: innerWidth,
      scroll: document.querySelector('.master-scroll').scrollWidth, width: document.querySelector('.master-scroll').clientWidth }));
    assert(layout.page <= layout.viewport + 2, 'Page itself overflows mobile viewport: ' + JSON.stringify(layout));
    assert(layout.scroll > layout.width, 'Wide table must scroll inside its container');
    assert.equal(await phone.locator('.master-table tbody tr').count(), expected.profiles);
    assert.equal(await phone.locator('.master-pagination').count(), 0);
    assert.equal(await phone.locator('.master-table th[data-column-key="family:humanevalplus"]').count(), 1);
    await phone.getByText('Benchmarkprotokolle und Durchschnitt auswählen', { exact: true }).click();
    const phoneSelect = phone.locator('select[data-protocol-family=humanevalplus]');
    assert(await phoneSelect.isVisible());
    const phoneBounds = await phoneSelect.boundingBox(); assert(phoneBounds.width > 200 && phoneBounds.x + phoneBounds.width <= 392);
    assert.equal(await phone.locator('.master-scroll').evaluate(e => getComputedStyle(e).maxHeight), 'none');
    const mobileHeights = await phone.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.getBoundingClientRect().height));
    assert(Math.max(...mobileHeights) <= 52, 'Mobile row heights stay compact');
    const modelLinks = await phone.locator('.master-table tbody td:first-child a').evaluateAll(links => links.map(a => ({ width: a.getBoundingClientRect().width, cell: a.parentElement.getBoundingClientRect().width, overflow: getComputedStyle(a).overflowX })));
    assert(modelLinks.every(a => a.width <= a.cell && a.overflow === 'hidden'), 'Long model names cannot overlap adjacent cells');
    await phone.locator('.master-table').evaluate(e => window.scrollTo(0, window.scrollY + e.getBoundingClientRect().top - 100));
    await phone.screenshot({ path: path.join(artifacts, 'mobile-results.png'), animations: 'disabled' });
    await mobile.close(); report.checks.push('desktop horizontal scrolling and 390px mobile layout');
    const researchContext = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true });
    const research = await researchContext.newPage(); research.on('pageerror', e => errors.push(e.message));
    await research.goto(new URL('omnicoder-derivatives/', base).href, { waitUntil: 'networkidle' });
    const reviewed = await research.evaluate(() => window.V100Leaderboard?.register.candidate_research || []);
    if (reviewed.length) {
      assert((await research.locator('.md-typeset h1').innerText()).includes('OmniCoder derivatives'));
      assert((await research.locator('.md-content').innerText()).includes('not a model leaderboard'));
      await research.goto(new URL('model-research/omnicoder-inventory/', base).href, { waitUntil: 'networkidle' });
      assert.equal(await research.locator('.md-typeset details').count(), reviewed.at(-1).candidates.length);
      await research.goto(new URL('model-research/omnicoder-proposals/', base).href, { waitUntil: 'networkidle' });
      assert.equal(await research.locator('.md-typeset h2').filter({ hasText: /^Priority [123]/ }).count(), 3);
      assert((await research.locator('.md-content').innerText()).includes('PROPOSED, NOT EXECUTED OR GPU-ADMITTED'));
      const width = await research.evaluate(() => ({ page: document.documentElement.scrollWidth, viewport: innerWidth }));
      assert(width.page <= width.viewport + 2, 'Proposed profiles overflow mobile layout: ' + JSON.stringify(width));
      report.checks.push('pinned derivative inventory and unmeasured proposals render separately on mobile');
    }
    await researchContext.close();
    assert.deepEqual(errors, []); report.console_errors = errors; report.passed = true;
    await fs.writeFile(path.join(artifacts, 'browser-report.json'), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify(report));
  } finally { await browser.close(); }
}
main().catch(e => { console.error(e); process.exitCode = 1; });
