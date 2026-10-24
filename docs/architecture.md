# Architecture
Protocol repo defines standards; this repo demonstrates implementations.

## Pieces

- **Manifest** (`examples/<name>/.living/manifest.yaml`): declares the agent's capabilities, isolation, state target and logging. Format defined by [living-repos-protocol](https://github.com/ao3575911/living-repos-protocol/blob/main/docs/spec.md).
- **Bootstrap** (for example `examples/hello/bootstrap.py`): reads the manifest, refuses unsupported capabilities, runs tasks and publishes state.
- **Pin** ([`PROTOCOL_VERSION`](../PROTOCOL_VERSION)): the protocol release every example is validated against.
- **CI**: lints Markdown, validates every manifest against the pinned schema and smoke-runs each demo against its expected output.

## Flow

1. Clone the repository.
2. A runtime (here, the bootstrap script) reads `.living/manifest.yaml`.
3. It checks the declared capabilities against what it supports and stops if any are missing.
4. It runs the agent's tasks inside the declared isolation profile.
5. It publishes state to the declared target and logs in the declared format.

## Decisions

- Each example is self-contained in its own directory, so it can be copied out as a starting point.
- Demos must be deterministic so CI can diff their output.
- Validation uses the published protocol schema, never a local copy, so drift shows up as a CI failure.

## Open questions

- Whether demos should run inside the isolation profile they declare (container, VM) in CI.
- How to show handoff between two runtimes in a single repository.
