# Living Repositories
Code that brings its own cloud agent.
Examples + demos for per-repo cloud agent runtimes.

[![CI](https://github.com/ao3575911/living-repos/actions/workflows/ci.yml/badge.svg)](https://github.com/ao3575911/living-repos/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/ao3575911/living-repos)](https://github.com/ao3575911/living-repos/releases) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

![Living Repositories](docs/social-preview.png)

## What it is

A showcase of repositories that carry their own cloud agent runtime. Each example declares a `.living/manifest.yaml` that follows the [Living Repositories Protocol](https://github.com/ao3575911/living-repos-protocol). The protocol repo defines the standard; this repo shows implementations.

## Hello demo

[`examples/hello`](examples/hello) is a working example: `cd examples/hello && python bootstrap.py`. CI runs it on every change.

## Quickstart

```sh
git clone https://github.com/ao3575911/living-repos
cd living-repos
cp -r examples/_template examples/my-example
# edit examples/my-example/.living/manifest.yaml, then validate:
pip install -r requirements-ci.txt
python scripts/validate_examples.py
```

## Docs

- [PRD](docs/prd.md), [spec sheet](docs/spec-sheet.md), [architecture](docs/architecture.md)
- [Build plan](docs/build-plan.md), [roadmap](docs/roadmap.md), [risks](docs/risks.md), [QA strategy](docs/qa-strategy.md)
- [ADR-0001: repo split](docs/decisions/ADR-0001-repo-split.md)
- [Protocol compatibility](PROTOCOL.md)
- [Changelog](CHANGELOG.md)

## Status

v0.2.1: hello demo, example template, pinned to protocol release v0.2.1. Snapshot and restore comes in v0.3 (see the [roadmap](docs/roadmap.md)).

## Related

- [living-repos-protocol](https://github.com/ao3575911/living-repos-protocol): the canonical specification and manifest schema.

## Licence

[MIT](LICENSE). See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.
