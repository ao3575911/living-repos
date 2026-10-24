# Living Repositories
Code that brings its own cloud agent.
Examples + demos for per-repo cloud agent runtimes.

Runnable examples of the Living Repositories Protocol, each validated against a pinned protocol release in CI.

<!-- BEGIN GENERATED: badges -->
[![CI](https://github.com/ao3575911/living-repos/actions/workflows/ci.yml/badge.svg)](https://github.com/ao3575911/living-repos/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/ao3575911/living-repos)](https://github.com/ao3575911/living-repos/releases) [![Protocol](https://img.shields.io/badge/protocol-v0.2.1-blue)](https://github.com/ao3575911/living-repos-protocol/releases/tag/v0.2.1) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
<!-- END GENERATED: badges -->

![Living Repositories](docs/social-preview.png)

## What it is

A showcase of repositories that carry their own cloud agent runtime. Each example declares a `.living/manifest.yaml` that follows the [Living Repositories Protocol](https://github.com/ao3575911/living-repos-protocol). The protocol repo defines the standard; this repo shows implementations.

## Hello demo

[`examples/hello`](examples/hello) is a working example: `cd examples/hello && python bootstrap.py`. CI runs it on every change.

## Examples

<!-- BEGIN GENERATED: examples -->
| Example | Capabilities | Isolation | State target |
| --- | --- | --- | --- |
| [`_template`](https://github.com/ao3575911/living-repos/tree/main/examples/_template) | run_tasks, publish_state | dedicated-vm | control-process |
| [`hello`](https://github.com/ao3575911/living-repos/tree/main/examples/hello) | run_tasks, publish_state | sandbox-process | file |

Generated from each example's manifest by `scripts/gen_readme.py`.
<!-- END GENERATED: examples -->

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

Docs site: [https://ao3575911.github.io/living-repos/](https://ao3575911.github.io/living-repos/)

- [Strategy](STRATEGY.md): problem, audience, non-goals and alternatives

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
