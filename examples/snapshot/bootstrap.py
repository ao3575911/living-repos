"""Snapshot demo: snapshot the declared paths, change them, then restore.

Run from this directory: python bootstrap.py
Requires PyYAML. Writes only under work/ and .living/snapshots/.
"""
import json, pathlib, shutil, sys
import yaml

HERE = pathlib.Path(__file__).resolve().parent
SUPPORTED = {"run_tasks", "snapshot_restore"}
SNAPSHOTS = HERE / ".living/snapshots"


def log(event, **fields):
    print(json.dumps({"event": event, **fields}, sort_keys=True))


def read(path):
    return (HERE / path).read_text().strip()


manifest = yaml.safe_load((HERE / ".living/manifest.yaml").read_text())
unsupported = set(manifest["agent_capabilities"]) - SUPPORTED
if unsupported:
    log("refused", unsupported=sorted(unsupported))
    sys.exit(1)
paths = manifest["snapshot"]["paths"]
log("start", project_id=manifest["project_id"], snapshot_paths=paths,
    retention_days=manifest["snapshot"].get("retention_days", 7))

# Start from a known state so the output is deterministic.
shutil.rmtree(HERE / "work", ignore_errors=True)
shutil.rmtree(SNAPSHOTS, ignore_errors=True)
(HERE / "work").mkdir()
(HERE / "work/notes.txt").write_text("version 1\n")
log("task", name="write", content=read("work/notes.txt"))

snap = SNAPSHOTS / "1"
for p in paths:
    shutil.copytree(HERE / p, snap / p)
log("snapshot", id="1", paths=paths)

(HERE / "work/notes.txt").write_text("version 2\n")
log("task", name="overwrite", content=read("work/notes.txt"))

for p in paths:
    shutil.rmtree(HERE / p)
    shutil.copytree(snap / p, HERE / p)
log("restore", id="1", content=read("work/notes.txt"))
log("done")
