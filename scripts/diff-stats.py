#!/usr/bin/env python3
"""Compare two network/_data/stats.json snapshots and print before/after deltas.

Used by the rebuild-site workflow:
  1. cp network/_data/stats.json /tmp/network-stats-before.json
  2. (run build)
  3. python3 network/scripts/diff-stats.py /tmp/network-stats-before.json
"""
import json
import sys
from pathlib import Path

KEYS = [
    ('providers', 'Providers'),
    ('apis', 'APIs'),
    ('capabilities', 'Capabilities'),
    ('categories', 'Canonical capabilities'),
    ('schemas', 'Schemas'),
    ('asyncapis', 'AsyncAPIs'),
    ('jsonld', 'JSON-LD documents'),
    ('rules', 'Spectral rulesets'),
]


def fmt_delta(before, after):
    delta = after - before
    sign = '+' if delta > 0 else ('' if delta == 0 else '')
    return f"{sign}{delta}"


def main(before_path, after_path=None):
    if after_path is None:
        after_path = Path(__file__).resolve().parent.parent / '_data' / 'stats.json'
    before = json.loads(Path(before_path).read_text()) if Path(before_path).exists() else {}
    after = json.loads(Path(after_path).read_text())

    rows = []
    any_change = False
    for key, label in KEYS:
        b = before.get(key, 0)
        a = after.get(key, 0)
        d = a - b
        if d != 0:
            any_change = True
        rows.append((label, b, a, d))

    print("=== Network Stats Delta ===")
    print(f"{'metric':28s} {'before':>10s} {'after':>10s} {'delta':>10s}")
    print('-' * 62)
    for label, b, a, d in rows:
        delta = fmt_delta(b, a)
        print(f"{label:28s} {b:>10,d} {a:>10,d} {delta:>10s}")

    print()
    summary = {label: {'before': b, 'after': a, 'delta': a - b} for label, b, a, _ in rows}
    print("=== JSON ===")
    print(json.dumps(summary, indent=2))
    return 0 if any_change else 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: diff-stats.py <before.json> [<after.json>]", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
