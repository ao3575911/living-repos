# Contributing
- Keep examples protocol-pinned
- Keep setup deterministic
- Document expected outputs
- Run `python scripts/validate_examples.py` before opening a PR

## Generated README sections

Parts of README.md between `BEGIN GENERATED` and `END GENERATED` markers come from source files. Edit the source, then run `python scripts/gen_readme.py`. CI fails if they drift.

## Releases

Run the Release Please workflow to open a PR with the next SemVer version from Conventional Commit titles. Before merging, move the CHANGELOG Unreleased entries under the new version. After merge, a maintainer tags the merge commit and publishes the release with the CHANGELOG notes.
