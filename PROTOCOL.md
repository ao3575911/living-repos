# Protocol Compatibility
Source: `ao3575911/living-repos-protocol`
Pinned: release `v0.2.0`, which defines protocol version `v0.1.0-draft`

The pin lives in [`PROTOCOL_VERSION`](PROTOCOL_VERSION): one line holding a release tag of [living-repos-protocol](https://github.com/ao3575911/living-repos-protocol). CI validates every example manifest against the schema at that tag and fails if this file or the CI action ref names a different release. To move to a new protocol release, change `PROTOCOL_VERSION`, the line above and the action ref in `.github/workflows/ci.yml` in one PR.
