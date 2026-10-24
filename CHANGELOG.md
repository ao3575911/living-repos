# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.1] - 2026-10-25

Pinned to [living-repos-protocol v0.2.1](https://github.com/ao3575911/living-repos-protocol/releases/tag/v0.2.1).

### Changed
- Protocol pin moved from v0.2.0 to v0.2.1 in `PROTOCOL_VERSION`, `PROTOCOL.md` and the CI action ref. Validation is lenient by default again: manifests valid under v0.1.0 pass, and full-spec violations are warnings. Both examples also pass strict mode.

## [0.2.0] - 2026-10-25

Pinned to [living-repos-protocol v0.2.0](https://github.com/ao3575911/living-repos-protocol/releases/tag/v0.2.0).

### Added
- Working hello demo in `examples/hello`: reads the manifest, enforces capabilities, runs one task and publishes state to a file. CI smoke-runs it against `expected-output.txt`.
- `PROTOCOL_VERSION`: single source of truth for the protocol pin, checked against `PROTOCOL.md` and the CI action ref.
- Completed `docs/architecture.md`, `docs/qa-strategy.md` and `docs/roadmap.md`.

### Changed
- CI validates example manifests with the published `ao3575911/living-repos-protocol@v0.2.0` action instead of a local copy of the logic.
- Protocol pin moved from v0.1.0 to v0.2.0.
- Dependency bumps: actions/checkout 7.0.1, actions/setup-python 7.1.0, markdownlint-cli2-action 24.2.0, jsonschema 4.26.0, PyYAML 6.0.3.

### Fixed
- `PROTOCOL.md` named `v0.1.0-draft` while the validator fetched release `v0.1.0`. Both now read from `PROTOCOL_VERSION`.

## [0.1.0] - 2026-10-24

### Added
- Initial showcase scaffold: PRD, architecture, roadmap, risks, QA strategy, ADR-0001 and an example template pinned to protocol v0.1.0-draft.
- CI job `test`: Markdown lint and validation of every example manifest against the protocol schema.
- Licence, contributing guide, security policy, code of conduct, issue and PR templates.

[Unreleased]: https://github.com/ao3575911/living-repos/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/ao3575911/living-repos/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/ao3575911/living-repos/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/ao3575911/living-repos/releases/tag/v0.1.0
