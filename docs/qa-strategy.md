# QA Strategy
Static checks, smoke tests, protocol compatibility checks.

## Checks in CI (`test` job)

| Check | What fails it |
| --- | --- |
| markdownlint | Any Markdown rule violation outside the disabled set in `.markdownlint.yaml`. |
| Required files | Missing `README.md`, `PROTOCOL.md` or `docs/prd.md`. |
| Protocol pin | `PROTOCOL.md` naming a different release than `PROTOCOL_VERSION`. |
| Manifest validation | Any `examples/*/.living/manifest.yaml` invalid against the pinned schema. |
| Demo smoke test | `examples/hello/bootstrap.py` output differing from `expected-output.txt`, or wrong state file. |

The ruleset requires `test` to pass before any merge to `main`.

## Adding an example

An example is done when its manifest validates, its README lists exact commands and expected output, and CI runs it.

## Not covered yet

- Running demos inside their declared isolation profile.
- Negative tests for the bootstrap (unsupported capability). The protocol repo covers invalid manifests.
