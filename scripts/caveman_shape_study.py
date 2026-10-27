#!/usr/bin/env python3
"""Generate safe CaveBench-inspired fixtures and run pinned Caveman engine CPU-only.

Requires an existing Caveman source checkout at the pinned commit. No downloads,
model requests, GPU devices, production files, or external services are used.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile

PIN = "9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4"
ARCHIVE_SHA256 = "73d93ead989462f5e7d274359d7191d649520b9d387337901069031d18692fba"
LAB_ONLY_TEST = "engine/compressors/lab_critical_test.go"
LAB_ONLY_TEST_SHA256 = "03687c98c6fad342177b90e6f78bd0a91d108a6d50d5e300a6b5ad8bf8e0bc8a"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def make_fixtures(root: Path) -> list[dict]:
    cases: list[dict] = []

    def add(case_id: str, filename: str, query: str, required: list[str], scope: str,
            expected_passthrough: bool = False) -> None:
        payload = (root / filename).read_bytes()
        cases.append({"id": case_id, "file": filename, "query": query,
                      "must_include": required, "scope": scope,
                      "expected_passthrough": expected_passthrough,
                      "input_bytes": len(payload), "input_sha256": sha(payload)})

    lines = [f"2026-10-27T12:{i%60:02d}:{i%60:02d}Z INFO worker=worker-{i%7} heartbeat status=healthy retry={i%3} source=synthetic-fixture-{i%11}\n" for i in range(740)]
    lines.insert(370, "2026-10-27T12:44:19Z ERROR service=payments deployment=rev-7f2a status=403 permission=false retries=0 request=req-88421 source=fixture:needle-17\n")
    (root / "sre-log-needle.log").write_text("".join(lines))
    add("sre-log-needle", "sre-log-needle.log", "Find failed payments request req-88421; report revision, status, permission, retries and source.",
        ["req-88421", "rev-7f2a", "403", "permission=false", "retries=0", "fixture:needle-17"], "CaveBench-inspired")

    services = [dict(name=f"service-{i:04d}", region=f"region-{i%4}", version=f"1.{i%9}.0", healthy=True,
                     owner=f"team-{i%8}", note="routine synchronized deployment; no action required") for i in range(500)]
    services.insert(250, dict(name="billing-api", region="eu-west", version="4.8.2", healthy=False,
                              owner="payments", permission="read-only", status=503, drift="expected 4.8.1",
                              note="do not restart; approval=false"))
    (root / "deployment-json-drift.json").write_text(json.dumps({"snapshot": "synthetic-2026-10-27", "services": services}, separators=(",", ":")))
    add("deployment-json-drift", "deployment-json-drift.json", "Find the version drift; report name, region, actual/expected version, status, permission and restart approval.",
        ["billing-api", "eu-west", "4.8.2", "4.8.1", "503", "read-only", "approval"], "CaveBench-inspired")

    out = io.StringIO(newline="")
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(["txn_id", "merchant", "country", "amount_eur", "review", "permission", "source"])
    for i in range(1160):
        writer.writerow([f"tx-{i:06d}", f"merchant-{i%31:02d}", "DE", f"{(i%97)+1}.00", "false", "read-only", f"fixture:{i%13}"])
    writer.writerow(["tx-884211", "merchant-07", "DE", "98765.43", "true", "read-only", "fixture:fraud-needle"])
    (root / "fraud-csv-outlier.csv").write_text(out.getvalue())
    add("fraud-csv-outlier", "fraud-csv-outlier.csv", "Find the anomalous transaction; report ID, amount, review, permission and source.",
        ["tx-884211", "98765.43", "true", "read-only", "fraud-needle"], "CaveBench-inspired")

    testlog = "".join(f"PASS test_module_{i%47:02d}::case_{i:04d} - 0.002s\n" for i in range(1600))
    testlog += "FAIL test_auth::denies_restart_without_approval - 0.018s\nAssertionError: expected restart_allowed=false, got false; observed status=403; approval=false; command=systemctl restart payments (NOT EXECUTED)\nsource=fixture:test-output:line-1602\n"
    (root / "test-output-failure.txt").write_text(testlog)
    add("test-output-failure", "test-output-failure.txt", "Identify failed test; report restart permission, status, approval, execution and source.",
        ["denies_restart_without_approval", "restart_allowed=false", "403", "approval=false", "NOT EXECUTED", "fixture:test-output:line-1602"], "CaveBench-inspired")

    yaml = ["services:\n"]
    for i in range(500):
        yaml.append(f"  service-{i:04d}:\n    region: region-{i%4}\n    replicas: 2\n    enabled: true\n    permission: read-only\n    note: routine deployment; no restart requested\n")
    yaml.append("  payments:\n    region: eu-west\n    version: 4.8.2\n    expected_version: 4.8.1\n    replicas: 0\n    enabled: false\n    permission: read-only\n    restart_approved: false\n    status: 503\n    source: fixture:yaml-needle-22\n")
    (root / "config-yaml-drift.yaml").write_text("".join(yaml))
    add("config-yaml-drift", "config-yaml-drift.yaml", "Report payments actual/expected version, replicas, enabled, permission, approval, status and source.",
        ["payments", "4.8.2", "4.8.1", "replicas: 0", "enabled: false", "read-only", "restart_approved: false", "503", "fixture:yaml-needle-22"], "CaveBench-inspired")

    html = ['<!doctype html><html><body><main>']
    for i in range(600):
        html.append(f'<section class="card"><h2>Service {i%73:02d}</h2><p>Status healthy; region region-{i%4}; no action required. Snapshot synthetic-{i:04d}.</p></section>')
    html.append('<section class="alert" id="payments-alert"><h2>Payments deployment drift</h2><p>service=payments version=4.8.2 expected=4.8.1 status=503 permission=read-only restart_approved=false source=fixture:html-needle-4</p></section></main></body></html>')
    (root / "dashboard-html-alert.html").write_text("".join(html))
    add("dashboard-html-alert", "dashboard-html-alert.html", "Find payments alert; report actual/expected version, status, permission, approval and source.",
        ["payments", "4.8.2", "4.8.1", "503", "read-only", "restart_approved=false", "fixture:html-needle-4"], "CaveBench-inspired")

    # Synthetic Jarvis-shaped payloads are separate from the six CaveBench shapes.
    repo = [f"FILE src/module_{i:04d}.py sha256={i:064x} status=unchanged\n" for i in range(500)]
    repo.insert(251, "FILE src/auth/permissions.py sha256=" + "a"*64 + " status=changed source=fixture:repo-needle-1\n")
    (root / "repository-scan.txt").write_text("".join(repo))
    add("repository-scan", "repository-scan.txt", "Find changed permissions.py and return its hash and status.",
        ["src/auth/permissions.py", "a"*64, "status=changed", "fixture:repo-needle-1"], "Jarvis-shaped")

    diff = [f"diff --git a/src/module_{i:04d}.py b/src/module_{i:04d}.py\nindex 1234567..7654321 100644\n--- a/src/module_{i:04d}.py\n+++ b/src/module_{i:04d}.py\n@@ -1,2 +1,2 @@\n-old_value = {i}\n+new_value = {i+1}\n" for i in range(300)]
    diff.insert(150, "diff --git a/src/auth.py b/src/auth.py\n--- a/src/auth.py\n+++ b/src/auth.py\n@@ -4 +4 @@\n-allow_restart = True\n+allow_restart = False  # fixture:diff-needle-9\n")
    (root / "repository-diff.diff").write_text("".join(diff))
    add("repository-diff", "repository-diff.diff", "Find the auth change and report old/new restart permission and source.",
        ["src/auth.py", "allow_restart = True", "allow_restart = False", "fixture:diff-needle-9"], "Jarvis-shaped")

    states = [dict(entity_id=f"sensor" + f".synthetic_{i:04d}", state="ok", writable=False, source=f"fixture:{i%9}") for i in range(600)]
    states.insert(300, dict(entity_id="switch" + ".mock_heating", state="off", writable=False, action_authorized=False,
                            temperature_c=19.5, note="do not change; no user approval", source="fixture:ha-needle-8"))
    (root / "mock-home-state.json").write_text(json.dumps({"kind": "synthetic_only", "entities": states}, separators=(",", ":")))
    add("mock-home-state", "mock-home-state.json", "Report mock_heating state, writability, authorization, temperature and source.",
        ["switch" + ".mock_heating", "off", "writable", "false", "action_authorized", "19.5", "ha-needle-8"], "Jarvis-shaped")

    context = ["# Recurrent synthetic task context\nTask status: open. Pending action: inspect only; do not execute. Permission: read-only.\n"]
    for i in range(450):
        context.append(f"## Observation {i:04d}\nSource: fixture:context-{i%17}. Summary: service-{i%29} remains healthy; no write action was taken.\n")
    context.append("## Authoritative state\nTask status: blocked. Pending action: inspect source line 44 only. Permission: read-only. No command was executed. Evidence: fixture:context-authority-4.\n")
    (root / "recurrent-context.md").write_text("\n".join(context))
    add("recurrent-context", "recurrent-context.md", "Return authoritative task status, pending action, permission, execution status and evidence.",
        ["Task status: blocked", "inspect source line 44 only", "Permission: read-only", "No command was executed", "context-authority-4"], "Jarvis-shaped")

    # Deterministic, effectively unstructured text is an explicit no-op control.
    noise = "\n".join(hashlib.sha256(f"issue18-noop-{i}".encode()).hexdigest() for i in range(1200)) + "\n"
    (root / "no-op-control.txt").write_text(noise)
    add("no-op-control", "no-op-control.txt", "Find the nonexistent SHA-256 value 000000.",
        [noise.splitlines()[0]], "negative-control", expected_passthrough=True)

    # Within-format size sensitivity: expand only irrelevant records while keeping
    # the one oracle-bearing record unchanged. These are not upstream fixtures.
    originals = [c for c in cases if c["scope"] == "CaveBench-inspired"]
    for case in originals:
        original_path = root / case["file"]
        base = original_path.read_text()
        for scale in (1.5, 2.0):
            target = int(len(base.encode()) * scale)
            payload = base
            i = 0
            while len(payload.encode()) < target:
                i += 1
                cid = case["id"]
                if cid == "sre-log-needle":
                    payload += f"2026-10-27T13:{i%60:02d}:00Z INFO worker=aux-{i%7} heartbeat status=healthy retry=0 source=synthetic-padding-{i}\n"
                elif cid == "deployment-json-drift":
                    obj = json.loads(payload)
                    obj["services"].append(dict(name=f"padding-{i:05d}", region="region-0", version="1.0.0", healthy=True,
                                                 owner="synthetic", note="routine synchronized deployment; no action required"))
                    payload = json.dumps(obj, separators=(",", ":"))
                elif cid == "fraud-csv-outlier":
                    payload += f"pad-{i:06d},merchant-00,DE,1.00,false,read-only,fixture:padding\n"
                elif cid == "test-output-failure":
                    payload += f"PASS test_padding::case_{i:06d} - 0.001s\n"
                elif cid == "config-yaml-drift":
                    payload += f"  padding-{i:05d}:\n    region: region-0\n    replicas: 2\n    enabled: true\n    permission: read-only\n    note: routine deployment; no restart requested\n"
                elif cid == "dashboard-html-alert":
                    payload = payload.replace("</main>", f'<section class="card"><h2>Padding {i}</h2><p>Status healthy; no action required.</p></section></main>')
                else:
                    raise RuntimeError(f"no size expansion rule for {cid}")
            suffix = "1p5x" if scale == 1.5 else "2x"
            filename = f"{case['id']}-{suffix}.{case['file'].split('.', 1)[1]}"
            (root / filename).write_text(payload)
            body = (root / filename).read_bytes()
            cases.append({"id": f"{case['id']}-{suffix}", "file": filename, "query": case["query"],
                          "must_include": case["must_include"], "scope": "CaveBench-inspired-size-sweep",
                          "expected_passthrough": False, "scale_vs_base": scale,
                          "input_bytes": len(body), "input_sha256": sha(body)})
    return cases


def verify_archive(source: Path, archive: Path) -> None:
    """Verify exact pinned source archive and byte-for-byte extracted tree."""
    raw = archive.read_bytes()
    if sha(raw) != ARCHIVE_SHA256:
        raise SystemExit("Caveman archive SHA-256 does not match the reviewed pin")
    expected: dict[str, str] = {}
    with tarfile.open(archive, "r:gz") as tf:
        members = tf.getmembers()
        roots = {m.name.split("/", 1)[0] for m in members}
        if len(roots) != 1:
            raise SystemExit("unexpected source archive layout")
        prefix = next(iter(roots)) + "/"
        for member in members:
            if member.issym() or member.islnk() or not (member.isfile() or member.isdir()):
                raise SystemExit("unsupported member in pinned source archive")
            if member.isfile():
                relative = member.name.removeprefix(prefix)
                stream = tf.extractfile(member)
                if stream is None:
                    raise SystemExit("cannot read pinned source member")
                expected[relative] = sha(stream.read())
    actual: dict[str, str] = {}
    for p in source.rglob("*"):
        if p.is_symlink():
            raise SystemExit("symlink found in extracted source tree")
        if p.is_file():
            actual[p.relative_to(source).as_posix()] = sha(p.read_bytes())
    extras = {k: v for k, v in actual.items() if k not in expected}
    if extras not in ({}, {LAB_ONLY_TEST: LAB_ONLY_TEST_SHA256}):
        raise SystemExit("unexpected files in extracted source tree")
    actual_upstream = {k: v for k, v in actual.items() if k in expected}
    if actual_upstream != expected:
        raise SystemExit("extracted source tree differs from the reviewed archive")


RUNNER = r'''package main
import (
 "crypto/sha256"
 "encoding/hex"
 "encoding/json"
 "os"
 "path/filepath"
 "time"
 "github.com/JuliusBrussee/caveman/engine"
 "github.com/JuliusBrussee/caveman/engine/ccr"
)
type Case struct { ID string `json:"id"`; File string `json:"file"`; Query string `json:"query"`; MustInclude []string `json:"must_include"`; Scope string `json:"scope"`; ExpectedPassthrough bool `json:"expected_passthrough"`; Scale float64 `json:"scale_vs_base"` }
type Manifest struct { Suite string `json:"suite"`; Cases []Case `json:"cases"` }
func main(){ root:=os.Args[1]; b,e:=os.ReadFile(filepath.Join(root,"manifest.json")); if e!=nil{panic(e)}; var m Manifest; if e=json.Unmarshal(b,&m);e!=nil{panic(e)}; store,e:=ccr.OpenMemory();if e!=nil{panic(e)};defer store.Close();eng:=engine.New(store,nil);out:=map[string]any{"suite":m.Suite,"counter":"engine default offline counter","upstream_commit":"9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4","mode":"engine.Compress(ModeCompress, Query) with in-memory CCR; CPU only; no network/model/GPU","cases":[]any{}};rows:=[]any{}
 for _,c:=range m.Cases { in,e:=os.ReadFile(filepath.Join(root,c.File));if e!=nil{panic(e)};start:=time.Now();r,e:=eng.Compress(in,engine.Options{Mode:engine.ModeCompress,Query:c.Query});elapsed:=time.Since(start).Seconds();if e!=nil{panic(e)};missing:=[]string{};for _,s:=range c.MustInclude{if !contains(r.Output,[]byte(s)){missing=append(missing,s)}};recoverOK:=false;if r.RecoveryHandle!=""{orig,er:=store.Get(r.RecoveryHandle);recoverOK=er==nil&&string(orig)==string(in)};passthrough:=string(r.Output)==string(in);rows=append(rows,map[string]any{"id":c.ID,"scope":c.Scope,"input_bytes":len(in),"output_bytes":len(r.Output),"tokens_before":r.TokensBefore,"tokens_after":r.TokensAfter,"tokens_saved":r.TokensBefore-r.TokensAfter,"reduction_pct":r.Ratio*100,"token_basis":r.TokenCountBasis,"content_type":r.ContentType,"method":r.Method,"lossless_to_model":r.LosslessToModel,"expected_passthrough":c.ExpectedPassthrough,"actual_passthrough":passthrough,"recovery_handle_created":r.RecoveryHandle!="","exact_original_recovery_verified":recoverOK,"oracle_checks":len(c.MustInclude),"oracle_missing":missing,"oracle_pass":len(missing)==0&&(!c.ExpectedPassthrough||passthrough),"input_sha256":hash(in),"output_sha256":hash(r.Output),"processing_seconds":elapsed})};out["cases"]=rows;enc:=json.NewEncoder(os.Stdout);enc.SetIndent("","  ");if e:=enc.Encode(out);e!=nil{panic(e)} }
func hash(b []byte)string{h:=sha256.Sum256(b);return hex.EncodeToString(h[:])}
func contains(a,b []byte)bool{if len(b)==0{return true};for i:=0;i+len(b)<=len(a);i++{ok:=true;for j:=range b{if a[i+j]!=b[j]{ok=false;break}};if ok{return true}};return false}
'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True, help="existing pinned Caveman checkout; no fetch performed")
    ap.add_argument("--archive", type=Path, required=True, help="existing reviewed upstream.tar.gz; no fetch performed")
    ap.add_argument("--out", type=Path, required=True, help="output directory for fixtures and result JSON")
    ap.add_argument("--modcache", type=Path, required=True, help="existing Go module cache; network disabled")
    ap.add_argument("--go-bin", type=Path, required=True, help="existing Go 1.26.10 binary; no install performed")
    args = ap.parse_args()
    verify_archive(args.source, args.archive)
    commit = PIN
    args.out.mkdir(parents=True, exist_ok=False)
    cases = make_fixtures(args.out)
    (args.out / "manifest.json").write_text(json.dumps({"suite": "issue18-cavebench-inspired-v1", "source_commit": commit, "cases": cases}, indent=2) + "\n")
    runner = args.out / "runner.go"
    runner.write_text(RUNNER)
    go_version = subprocess.check_output([str(args.go_bin), "version"], text=True).strip()
    if "go1.26.10" not in go_version:
        raise SystemExit(f"expected Go 1.26.10, got {go_version}")
    env = dict(os.environ, GOTOOLCHAIN="local", GOMODCACHE=str(args.modcache), GOPROXY="off", CGO_ENABLED="0")
    result = subprocess.run([str(args.go_bin), "run", str(runner), str(args.out)],
                            cwd=args.source, env=env, check=True, capture_output=True, text=True)
    payload = json.loads(result.stdout)
    payload["source_archive_sha256"] = ARCHIVE_SHA256
    payload["go_toolchain"] = go_version
    payload["build_environment"] = {"CGO_ENABLED": "0", "GOPROXY": "off", "network_requests": 0,
                                    "model_or_GPU_calls": 0}
    payload["runner_sha256"] = sha(runner.read_bytes())
    payload["manifest_sha256"] = sha((args.out / "manifest.json").read_bytes())
    payload["engine_source_sha256"] = {
        str(p.relative_to(args.source)): sha(p.read_bytes())
        for p in [args.source / "engine/engine.go", args.source / "engine/result.go",
                  args.source / "engine/compressors/compressor.go"]
    }
    payload["fixture_manifest"] = [
        {k: case[k] for k in ("id", "scope", "input_bytes", "input_sha256") if k in case}
        for case in cases
    ]
    (args.out / "results.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({"suite": payload["suite"], "source_commit": commit,
                      "case_count": len(payload["cases"]),
                      "oracle_pass": sum(c["oracle_pass"] for c in payload["cases"]),
                      "input_tokens": sum(c["tokens_before"] for c in payload["cases"]),
                      "output_tokens": sum(c["tokens_after"] for c in payload["cases"])}, indent=2))


if __name__ == "__main__":
    main()
