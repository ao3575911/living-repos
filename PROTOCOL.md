# Protocol Compatibility
Source: `ao3575911/living-repos-protocol`
Pinned: release `v0.1.0`, which defines protocol version `v0.1.0-draft`

The pin lives in [`PROTOCOL_VERSION`](PROTOCOL_VERSION): one line holding a release tag of [living-repos-protocol](https://github.com/ao3575911/living-repos-protocol). CI validates every example manifest against the schema at that tag and fails if this file names a different release. To move to a new protocol release, change `PROTOCOL_VERSION` and the line above in one PR.
