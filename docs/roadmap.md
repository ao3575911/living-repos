# Roadmap
v0.1 scaffold, v0.2 demos, v0.3 snapshot demo and tooling, v0.4 conformance, v1.0 launch.

## v0.1: scaffold (shipped)

Docs, example template and CI. [Release](https://github.com/ao3575911/living-repos/releases/tag/v0.1.0).

## v0.2: first demo and protocol tooling (shipped)

- Working hello demo with a CI smoke test: [examples/hello](https://github.com/ao3575911/living-repos/tree/main/examples/hello).
- Single protocol pin in [`PROTOCOL_VERSION`](https://github.com/ao3575911/living-repos/blob/main/PROTOCOL_VERSION).
- Validation through the published protocol action, pinned to protocol v0.2.0.
- Completed architecture, QA and roadmap docs.

## v0.3: snapshot demo and project tooling (shipped)

- Snapshot and restore demo: [examples/snapshot](https://github.com/ao3575911/living-repos/tree/main/examples/snapshot).
- Generated README and guide tables, docs site, labels, issue forms, AGENTS.md.

## v0.4: conformance (shipped)

- Demos run in CI inside their declared isolation profile ([#17](https://github.com/ao3575911/living-repos/issues/17)).
- Negative test: the hello bootstrap refuses an unsupported capability ([#18](https://github.com/ao3575911/living-repos/issues/18)).
- CI fails if an example is missing from the guide ([#20](https://github.com/ao3575911/living-repos/issues/20)).
- Pinned to protocol v0.4.0 (runtime capability document, `read_secrets`).

## v1.0: launch

- Handoff demo (`handoff` capability, [#19](https://github.com/ao3575911/living-repos/issues/19)).
- Protocol 1.0 pinned, with a stability promise.
