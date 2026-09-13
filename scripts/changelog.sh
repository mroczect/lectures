#!/usr/bin/env bash
set -euo pipefail

OUT="docs/changelog.md"
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

cat > "$OUT" <<'EOF'
---
title: Changelog
description: Riwayat perubahan dokumentasi.
outline: deep
order: 99
---

# Changelog

> Auto-generated dari `git log`. Jangan edit manual.

EOF

TMP="$(mktemp)"

git log --no-merges \
  --pretty=format:'%ad|%s|%h' \
  --date=short \
  | grep -v -E '\|(chore|docs): (update|generate) changelog' \
  | grep -v -E '\|(initial|init)( |$)' \
  | awk -F'|' '
  {
    date = $1; subject = $2; hash = $3

    if (match(subject, /^(feat|fix|docs|chore|refactor|style|test|perf|ci|build|revert)(\(.+\))?:/)) {
      type = substr(subject, RSTART, RLENGTH)
      sub(/:$/, "", type); sub(/\(.+\)/, "", type)
      sub(/^[^:]+:/, "", subject); sub(/^ /, "", subject)
    } else {
      type = "other"
    }

    print date "|" type "|" subject "|" hash
  }
  ' \
  | sort -t'|' -k1,1r -k2,2 -k3,3 \
  > "$TMP"

awk -F'|' '
  {
    if ($1 != last_date) {
      if (last_date != "") print ""
      printf "## %s\n\n", $1
      last_date = $1
    }
    printf "- **%s**: %s (%s)\n", $2, $3, $4
  }
' "$TMP" >> "$OUT"

cat >> "$OUT" <<EOF

---

Terakhir diperbarui: $(date +%Y-%m-%d).
EOF

rm -f "$TMP"
echo "✓ $OUT"
