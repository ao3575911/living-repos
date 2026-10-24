"""Regenerate the README sections between BEGIN/END GENERATED markers.

Sources: examples/*/.living/manifest.yaml (examples table) and
PROTOCOL_VERSION (badges). Run with --check to fail if README.md is out of date.
"""
import pathlib, re, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "ao3575911/living-repos"


def badges():
    base = f"https://github.com/{REPO}"
    pin = (ROOT / "PROTOCOL_VERSION").read_text().strip()
    return (f"[![CI]({base}/actions/workflows/ci.yml/badge.svg)]({base}/actions/workflows/ci.yml) "
            f"[![Release](https://img.shields.io/github/v/release/{REPO})]({base}/releases) "
            f"[![Protocol](https://img.shields.io/badge/protocol-{pin}-blue)](https://github.com/ao3575911/living-repos-protocol/releases/tag/{pin}) "
            "[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)")


def examples():
    rows = ["| Example | Capabilities | Isolation | State target |", "| --- | --- | --- | --- |"]
    for m in sorted(ROOT.glob("examples/*/.living/manifest.yaml")):
        d = yaml.safe_load(m.read_text())
        name = m.parent.parent.name
        rows.append(f"| [`{name}`](examples/{name}) | {', '.join(d['agent_capabilities'])} | "
                    f"{d['isolation_profile']} | {d['state_publication']['target']} |")
    rows.append("")
    rows.append("Generated from each example's manifest by `scripts/gen_readme.py`.")
    return "\n".join(rows)


SECTIONS = {"badges": badges, "examples": examples}


def render(text):
    for name, fn in SECTIONS.items():
        text = re.sub(rf"(<!-- BEGIN GENERATED: {name} -->\n).*?(\n<!-- END GENERATED: {name} -->)",
                      lambda m: m.group(1) + fn() + m.group(2), text, flags=re.S)
    return text


readme = ROOT / "README.md"
current = readme.read_text()
new = render(current)
if "--check" in sys.argv:
    if new != current:
        sys.exit("README.md is out of date. Run: python scripts/gen_readme.py")
    print("ok README.md up to date")
else:
    readme.write_text(new)
