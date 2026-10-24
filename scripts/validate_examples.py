"""Check the protocol pin is consistent, then validate every example manifest against it.

--pin-only: check consistency only (CI validates through the protocol action).
"""
import json, pathlib, sys, urllib.request
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PIN = (ROOT / "PROTOCOL_VERSION").read_text().strip()
if f"release `{PIN}`" not in (ROOT / "PROTOCOL.md").read_text():
    sys.exit(f"PROTOCOL.md does not name release `{PIN}` from PROTOCOL_VERSION")
if f"ao3575911/living-repos-protocol@{PIN}" not in (ROOT / ".github/workflows/ci.yml").read_text():
    sys.exit(f"ci.yml does not use ao3575911/living-repos-protocol@{PIN}")
if "--pin-only" in sys.argv:
    print(f"ok pin {PIN}")
    sys.exit(0)
URL = f"https://raw.githubusercontent.com/ao3575911/living-repos-protocol/{PIN}/schemas/manifest.schema.json"
schema = json.load(urllib.request.urlopen(URL))
manifests = sorted(ROOT.glob("examples/*/.living/manifest.yaml"))
assert manifests, "no example manifests found"
for m in manifests:
    jsonschema.validate(yaml.safe_load(m.read_text()), schema)
    print(f"ok {m.relative_to(ROOT)} (protocol {PIN})")
