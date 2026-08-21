#!/usr/bin/env bash
# Install the hub's deterministic, read-only repository-policy controls locally.
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 /absolute/path/to/target-repository" >&2
  exit 64
fi

TARGET="$1"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$ROOT/templates/repository-controls"

if [[ ! -d "$TARGET/.git" ]]; then
  echo "Target must be an initialized Git repository: $TARGET" >&2
  exit 65
fi

mkdir -p "$TARGET/.github/workflows" "$TARGET/scripts/ci"
cp "$TEMPLATE/.github/workflows/repository-policy.yml" "$TARGET/.github/workflows/repository-policy.yml"
cp "$TEMPLATE/scripts/ci/repository_policy.py" "$TARGET/scripts/ci/repository_policy.py"
chmod 755 "$TARGET/scripts/ci/repository_policy.py"

echo "Installed repository-policy workflow and validator into: $TARGET"
echo "Review the changes, run python3 scripts/ci/repository_policy.py, then commit them through the target repository's normal review process."
