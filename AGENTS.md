# AGENTS.md

Instructions for coding agents working in this repository. Humans: see [CONTRIBUTING.md](CONTRIBUTING.md).

## Setup

```sh
pip install -r requirements-ci.txt
```

## Checks (the CI `test` job runs all of these)

```sh
python scripts/validate_examples.py                       # pin consistency + manifests vs pinned schema
(cd examples/hello && python bootstrap.py | diff -u expected-output.txt -)
npx markdownlint-cli2 "**/*.md"
```

## Layout

- `examples/<name>/`: self-contained example with `.living/manifest.yaml`, a bootstrap script, `expected-output.txt` and a README.
- `PROTOCOL_VERSION`: the protocol release tag. `PROTOCOL.md` and the action ref in `.github/workflows/ci.yml` must match it.

## Rules

- A new example needs a manifest valid in strict mode, deterministic output, a README with exact commands and a CI step that diffs output.
- Bump the protocol pin in one PR that changes `PROTOCOL_VERSION`, `PROTOCOL.md` and the action ref together.
- Add a CHANGELOG entry under Unreleased (Keep a Changelog).
- Pin actions; keep permissions at `contents: read` unless a job needs more.
- `main` is protected: open a PR, `test` must pass, squash merge, signed commits.
- No placeholder text and no marketing language.
