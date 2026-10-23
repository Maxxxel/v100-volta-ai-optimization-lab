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
      const d = window.V100Leaderboard, m = window.V100MasterTable.build(d);
      return { profiles: m.rows.length, columns: m.columns.length,
        official: m.benchmarks.filter(b => b.scope === 'OFFICIAL_LOCAL').length,
        current: m.benchmarks.find(b => b.scope === 'OFFICIAL_LOCAL' && m.rows.some(r => r.scores[b.key]?.n))?.key,
        missing: m.benchmarks.find(b => b.scope === 'OFFICIAL_LOCAL' && !m.rows.some(r => r.scores[b.key]?.n))?.key };
    });
    assert.equal(await page.locator('.master-table tbody tr').count(), expected.profiles);
    assert.equal(await page.locator('.master-benchmark-choices input').count(), expected.official);
    assert((await page.locator('.master-counter').innerText()).includes(String(expected.profiles)));
    assert.equal(await page.locator('.master-pagination').count(), 0);
    const initialIds = await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.dataset.configurationId));
    const measuredIds = await page.evaluate(() => [...new Set(window.V100Leaderboard.history.runs.map(r => r.runtime_configuration_id))]);
    assert.deepEqual(initialIds.slice().sort(), measuredIds.slice().sort());
    const geometry = await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.getBoundingClientRect().height));
    assert(Math.max(...geometry) <= 52, 'Compact rows including offscreen cells: ' + Math.max(...geometry));
    assert(Math.max(...geometry) - Math.min(...geometry) <= 2, 'Uniform result row heights');
    assert.equal(await page.locator('.master-scroll').evaluate(e => getComputedStyle(e).maxHeight), 'none');
    assert(await page.locator('.master-scroll').evaluate(e => e.clientHeight >= e.scrollHeight - 2));
    assert.equal(await page.locator('.master-table thead').evaluate(e => getComputedStyle(e).position), 'sticky');
    assert.equal(await page.locator('.master-table tbody td').first().evaluate(e => getComputedStyle(e).position), 'sticky');
    report.checks.push('rows, register definitions, sticky header and model column');

    if (expected.current && expected.missing) {
      await page.locator(`input[data-benchmark-key="${expected.missing}"]`).check();
      assert((await page.locator('.master-counter').innerText()).includes('0 mit vollständigem'));
      const averageCells = await page.locator('.master-table tbody td[data-column-key="average"]').allTextContents();
      assert(averageCells.every(s => s === 'NICHT ERFASST'));
      await page.locator(`input[data-benchmark-key="${expected.missing}"]`).uncheck();
      await page.locator(`.master-table th[data-column-key="${expected.current}"] button`).click();
      const result = await page.locator(`.master-table tbody td[data-column-key="${expected.current}"] strong`).allTextContents();
      const numbers = result.map(s => Number(s.replace('%', '').replaceAll('.', '').replace(',', '.').trim()));
      assert(numbers.every((x, i) => !i || numbers[i - 1] >= x));
      await page.locator('.master-score-details').first().click();
      assert(await page.locator('.master-cell-dialog a[href*="/audits/"]').count() > 0);
      assert(await page.locator('.master-cell-dialog a[href*="/experiments/"]').count() > 0);
      assert((await page.locator('.master-cell-dialog pre').innerText()).includes('audit_hash'));
      await page.getByRole('button', { name: 'Schließen', exact: true }).click();
      report.checks.push('missing benchmark prevents average; numeric sorting; direct audit/run links');
    }

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
      return M.build(window.V100Leaderboard).rows.filter(r => M.canonical({ values: r.values, runs: r.runs }).toLowerCase().includes('bonsai')).map(r => r.id);
    });
    assert((await page.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.dataset.configurationId))).every(id => expectedSearch.includes(id)));
    await global.fill(''); report.checks.push('per-parameter numeric filter and global search');

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
    const scopes = await page.locator('.master-benchmark-choices input').evaluateAll(inputs => inputs.map(i => window.V100Leaderboard.master.benchmark_columns.find(b => b.key === i.value).scope));
    assert(scopes.length > 0 && scopes.every(s => s !== 'OFFICIAL_LOCAL'));
    await mode.selectOption('official'); report.checks.push('official and exploratory benchmark selections stay separate');

    const presets = page.getByLabel('Ansicht', { exact: true });
    for (const preset of ['Qualität', 'Geschwindigkeit', 'Energie', 'Vollständig']) {
      await presets.selectOption(preset);
      assert(await page.locator('.master-table tbody tr').count() > 0);
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
    const csv = await fs.readFile(downloaded, 'utf8'); assert(csv.includes('runtime_configuration_id')); assert(csv.includes('NICHT ERFASST')); assert(csv.includes('mean_percent'));
    const allIds = await page.evaluate(() => [...new Set(window.V100Leaderboard.history.runs.map(r => r.runtime_configuration_id))]);
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
    assert.equal(await phone.locator('.master-scroll').evaluate(e => getComputedStyle(e).maxHeight), 'none');
    const mobileHeights = await phone.locator('.master-table tbody tr').evaluateAll(rows => rows.map(r => r.getBoundingClientRect().height));
    assert(Math.max(...mobileHeights) <= 52, 'Mobile row heights stay compact');
    await phone.locator('.master-table').evaluate(e => window.scrollTo(0, window.scrollY + e.getBoundingClientRect().top - 100));
    await phone.screenshot({ path: path.join(artifacts, 'mobile-results.png'), animations: 'disabled' });
    await mobile.close(); report.checks.push('desktop horizontal scrolling and 390px mobile layout');
    assert.deepEqual(errors, []); report.console_errors = errors; report.passed = true;
    await fs.writeFile(path.join(artifacts, 'browser-report.json'), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify(report));
  } finally { await browser.close(); }
}
main().catch(e => { console.error(e); process.exitCode = 1; });
