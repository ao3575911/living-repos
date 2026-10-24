"""Validate every examples/*/.living/manifest.yaml against the pinned protocol schema."""
import json, pathlib, sys, urllib.request
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PIN = (ROOT / "PROTOCOL_VERSION").read_text().strip()
if f"release `{PIN}`" not in (ROOT / "PROTOCOL.md").read_text():
    sys.exit(f"PROTOCOL.md does not name release `{PIN}` from PROTOCOL_VERSION")
URL = f"https://raw.githubusercontent.com/ao3575911/living-repos-protocol/{PIN}/schemas/manifest.schema.json"
schema = json.load(urllib.request.urlopen(URL))
manifests = sorted(ROOT.glob("examples/*/.living/manifest.yaml"))
assert manifests, "no example manifests found"
for m in manifests:
    jsonschema.validate(yaml.safe_load(m.read_text()), schema)
    print(f"ok {m.relative_to(ROOT)} (protocol {PIN})")
