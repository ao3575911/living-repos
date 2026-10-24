# QA Strategy
Static checks, smoke tests, protocol compatibility checks.

## Checks in CI (`test` job)

| Check | What fails it |
| --- | --- |
| markdownlint | Any Markdown rule violation outside the disabled set in `.markdownlint.yaml`. |
| Required files | Missing `README.md`, `PROTOCOL.md` or `docs/prd.md`. |
| Protocol pin | `PROTOCOL.md` or the action ref in `ci.yml` naming a different release than `PROTOCOL_VERSION`. |
| Manifest validation | Any `examples/*/.living/manifest.yaml` invalid against the pinned schema. |
| Demo smoke tests | `examples/hello/bootstrap.py` or `examples/snapshot/bootstrap.py` output differing from its `expected-output.txt`, a wrong state file, or a snapshot not restored. |
| Unsupported capability | `examples/hello/bootstrap.py` run against `tests/unsupported-capability.yaml` (declares `handoff`) not exiting 1 with exactly one `refused` log line. |

The ruleset requires `test` to pass before any merge to `main`.

## Adding an example

An example is done when its manifest validates, its README lists exact commands and expected output, and CI runs it.

## Not covered yet

- Running demos inside their declared isolation profile.
