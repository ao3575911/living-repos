# Roadmap
v0.1 scaffold, v0.2 demos, v0.3 conformance, v1.0 launch.

## v0.1: scaffold (shipped)

Docs, example template and CI. [Release](https://github.com/ao3575911/living-repos/releases/tag/v0.1.0).

## v0.2: first demo and protocol tooling (this release)

- Working hello demo with a CI smoke test: [examples/hello](../examples/hello).
- Single protocol pin in [`PROTOCOL_VERSION`](../PROTOCOL_VERSION).
- Validation through the published protocol action, pinned to protocol v0.2.0.
- Completed architecture, QA and roadmap docs.

## v0.3: conformance

- Snapshot and restore demo (`snapshot_restore` capability).
- Run demos inside their declared isolation profile in CI.
- Bootstrap negative tests.

## v1.0: launch

- Handoff demo (`handoff` capability).
- Protocol 1.0 pinned, with a stability promise.
