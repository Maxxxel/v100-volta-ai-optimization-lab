# Public export and update policy

Only projected research metadata is publishable. The exporter uses explicitly selected keys, numeric aggregate branches and public HTTPS source domains. It never copies a source file, model, log, prompt, response, system dump, authentication file or network configuration. Local audit locations remain in a private receipt outside this repository.

Publication validates all 162 unique factors, original/additional counters, scientific statuses, reference pointers, evidence links, forbidden content, file paths/sizes and the byte manifest. Selected original audit hashes are checked locally before export. CI only validates the public snapshot and builds static documentation; it cannot independently access the retained originals.

A local serialized synchronization job checks canonical state after audited work, regenerates data and pages, validates, commits and pushes. It skips while the canonical experiment lock is held. Failed authentication/push is recorded locally and retried in bounded later runs; it never blocks GPU work. Publishing requires an authenticated GitHub account and a configured HTTPS origin. It never force-pushes or rewrites history.

No publication is claimed until the repository exists, push succeeds and Pages deployment is verified. Proposed GitHub issues are first retained as public research proposals; remote issues are created only once an authenticated repository is available.

New script/documentation copyright is licensed under MIT. Referenced third-party software, papers, models and benchmark datasets retain their own licenses. No permission to redistribute their weights, code, test data or full papers is implied.
