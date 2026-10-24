# QA Strategy
Static checks, smoke tests, protocol compatibility checks.

## Checks in CI (`test` job)

| Check | What fails it |
| --- | --- |
| markdownlint | Any Markdown rule violation outside the disabled set in `.markdownlint.yaml`. |
| Generated sections | `README.md` or `docs/index.md` out of date with `scripts/gen_readme.py`, or a directory under `examples/` without `.living/manifest.yaml` (so every example is listed in the guide). |
| Required files | Missing `README.md`, `PROTOCOL.md` or `docs/prd.md`. |
| Protocol pin | `PROTOCOL.md` or the action ref in `ci.yml` naming a different release than `PROTOCOL_VERSION`. |
| Manifest validation | Any `examples/*/.living/manifest.yaml` invalid against the pinned schema. |
| Demo smoke tests | Run through `scripts/run_isolated.sh` in the isolation the manifest declares (`sandbox-process`: Docker container with no network, no Linux capabilities and no new privileges; `container`: Docker container). Fails on `examples/hello/bootstrap.py` or `examples/snapshot/bootstrap.py` output differing from its `expected-output.txt`, a wrong state file, or a snapshot not restored. |
| Unsupported capability | `examples/hello/bootstrap.py` run against `tests/unsupported-capability.yaml` (declares `handoff`) not exiting 1 with exactly one `refused` log line. |

The ruleset requires `test` to pass before any merge to `main`.

## Adding an example

An example is a directory under `examples/` with a `.living/manifest.yaml`; `python scripts/gen_readme.py` adds it to the README and the guide. It is done when its manifest validates, its README lists exact commands and expected output, and CI runs it.

## Not covered yet

- The `container` branch of `scripts/run_isolated.sh`: no example declares `container` yet, so CI exercises only `sandbox-process`.
- The container image is pinned by digest in `scripts/run_isolated.sh`; Dependabot does not track it, so it is updated by hand.
- `dedicated-vm` examples: `scripts/run_isolated.sh` refuses them, and no example uses that profile.
