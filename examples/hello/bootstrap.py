"""Hello demo: read the manifest, run one task, publish state to a file.

Run from this directory: python bootstrap.py [MANIFEST]
MANIFEST defaults to .living/manifest.yaml.
Requires PyYAML.
"""
import json, pathlib, sys
import yaml

HERE = pathlib.Path(__file__).resolve().parent
SUPPORTED = {"run_tasks", "publish_state"}


def log(event, **fields):
    print(json.dumps({"event": event, **fields}, sort_keys=True))


manifest_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / ".living/manifest.yaml"
manifest = yaml.safe_load(manifest_path.read_text())
unsupported = set(manifest["agent_capabilities"]) - SUPPORTED
if unsupported:
    log("refused", unsupported=sorted(unsupported))
    sys.exit(1)
log("start", project_id=manifest["project_id"], protocol_version=manifest["protocol_version"])

result = f"hello from {manifest['project_id']}"
log("task", name="greet", result=result)

target = manifest["state_publication"]
if target["target"] == "file":
    path = HERE / target["path"]
    path.write_text(json.dumps({"status": "ready", "last_task": "greet"}, sort_keys=True) + "\n")
    log("state", path=target["path"], status="ready")
log("done")
