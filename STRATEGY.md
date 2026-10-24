# Strategy

## Problem

The [Living Repositories Protocol](https://github.com/ao3575911/living-repos-protocol) defines a manifest for a repository's cloud agent. A specification alone does not show whether it works or how to adopt it. Adopters need small, runnable examples they can copy.

## Audience

- Maintainers adding a manifest to their own repository.
- Runtime authors who want reference behaviour to test against.
- Protocol contributors who need proof a proposed field is useful.

## What this repository ships

Self-contained examples under `examples/`, each with a manifest, a deterministic bootstrap and expected output that CI checks. Every manifest is validated against the pinned protocol release.

## Non-goals

- A production runtime or hosted service.
- Defining protocol rules. Those live in the protocol repository.
- Covering every language or cloud. Examples stay minimal.

## Alternatives and how this differs

| Alternative | What it gives you | Why examples here |
| --- | --- | --- |
| [Template repositories](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository) | A one-time copy of a starting repository. | Examples here stay validated against each protocol release, so copying one gives a current manifest. |
| [devcontainers/templates](https://github.com/devcontainers/templates) | Ready-made dev container definitions. | Those define environments; these show agent capabilities, isolation and state publication. |
| [AGENTS.md](https://agents.md/) examples | Instruction files for coding agents. | Instructions, not an enforceable contract. Examples here can include both. |

## Principles

1. **Runnable.** Every example runs with one command and CI diffs its output.
2. **Pinned.** One protocol release in `PROTOCOL_VERSION`; bumping it is one PR.
3. **Minimal.** An example shows one capability well.
4. **Proof before spec.** A new protocol field ships with an example here in the same release.
