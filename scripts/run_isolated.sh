#!/usr/bin/env bash
# Run an example's bootstrap.py in the isolation its manifest declares.
#
# Usage: scripts/run_isolated.sh EXAMPLE_DIR [ARGS...]
# Needs Docker and Python with PyYAML on the host. ARGS go to bootstrap.py
# and are resolved inside the container, where EXAMPLE_DIR is /work and the
# repository root is /repo (read-only).
#
#   sandbox-process  container with no network, no capabilities, no new privileges
#   container        container with the default network
#   dedicated-vm     not supported here; exits 2
set -euo pipefail
dir=$(cd "$1" && pwd)
shift
root=$(cd "$(dirname "$0")/.." && pwd)
image="python:3.12-slim@sha256:a0f57064cbdcd6285fa45f51237ab0b35ea8ebaed06a1f5973e89e19dfb86704"
profile=$(python -c 'import sys, yaml; print(yaml.safe_load(open(sys.argv[1]))["isolation_profile"])' "$dir/.living/manifest.yaml")
deps=$(mktemp -d)
python -m pip install --quiet --target "$deps" -r "$root/requirements-demo.txt"
case "$profile" in
  sandbox-process) flags=(--network none --cap-drop ALL --security-opt no-new-privileges) ;;
  container) flags=() ;;
  *) echo "isolation_profile $profile is not supported by run_isolated.sh" >&2; exit 2 ;;
esac
echo "running $(basename "$dir") with isolation_profile $profile" >&2
exec docker run --rm "${flags[@]}" --user "$(id -u):$(id -g)" \
  -v "$dir:/work" -v "$root:/repo:ro" -v "$deps:/deps:ro" \
  -e PYTHONPATH=/deps -e PYTHONDONTWRITEBYTECODE=1 -w /work \
  "$image" python bootstrap.py "$@"
