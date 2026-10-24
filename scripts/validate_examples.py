"""Validate every examples/*/.living/manifest.yaml against the pinned protocol schema."""
import json, pathlib, urllib.request
import jsonschema, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = "https://raw.githubusercontent.com/ao3575911/living-repos-protocol/v0.1.0/schemas/manifest.schema.json"
schema = json.load(urllib.request.urlopen(URL))
manifests = sorted(ROOT.glob("examples/*/.living/manifest.yaml"))
assert manifests, "no example manifests found"
for m in manifests:
    jsonschema.validate(yaml.safe_load(m.read_text()), schema)
    print(f"ok {m.relative_to(ROOT)}")
