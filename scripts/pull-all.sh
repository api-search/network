#!/bin/bash
# Refresh every provider repo in the api-evangelist mirror via git pull --ff-only.
# Run before build.py so the build reflects the latest upstream content.
#
# Usage:  EVANGELIST_DIR=/path/to/mirror scripts/pull-all.sh
# Default EVANGELIST_DIR resolves to ../../api-evangelist relative to this script.

set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NETWORK_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$NETWORK_DIR")"
MIRROR_DIR="${EVANGELIST_DIR:-$ROOT_DIR/api-evangelist}"
PARALLEL="${PULL_PARALLEL:-24}"
LOG="${PULL_LOG:-/tmp/pull-all.log}"

if [ ! -d "$MIRROR_DIR" ]; then
  echo "ERROR: mirror dir not found: $MIRROR_DIR" >&2
  exit 1
fi

echo "Pulling provider repos under $MIRROR_DIR (parallel=$PARALLEL)..."

# One repo per xargs invocation — using a small helper avoids the
# command-line-too-long failure seen when passing inline bash -c.
PULL_ONE="$(mktemp)"
trap 'rm -f "$PULL_ONE"' EXIT
cat > "$PULL_ONE" <<'PULLONE'
#!/bin/bash
d="$1"
cd "$d" 2>/dev/null || exit 0
out=$(git pull --ff-only --quiet 2>&1)
rc=$?
if [ $rc -ne 0 ]; then
  echo "FAIL: $d :: $out"
elif [ -n "$out" ]; then
  echo "PULLED: $d"
fi
PULLONE
chmod +x "$PULL_ONE"

cd "$MIRROR_DIR"
find . -mindepth 2 -maxdepth 2 -type d -name ".git" 2>/dev/null \
  | sed 's|/.git$||' \
  | xargs -P "$PARALLEL" -I REPO "$PULL_ONE" REPO \
  > "$LOG" 2>&1

pulled=$(grep -c '^PULLED' "$LOG" 2>/dev/null | tr -d '[:space:]')
failed=$(grep -c '^FAIL' "$LOG" 2>/dev/null | tr -d '[:space:]')
echo "Pull complete: ${pulled:-0} updated, ${failed:-0} failed (full log: $LOG)"
