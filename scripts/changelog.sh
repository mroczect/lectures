#!/usr/bin/env bash
set -euo pipefail

OUT="docs/changelog.md"
REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# Header + frontmatter
cat > "$OUT" <<EOF
---
title: Changelog
description: Riwayat perubahan dokumentasi — auto-generated dari git log.
outline: deep
order: 99
---

# Changelog

> File ini **auto-generated**. Jangan edit manual.
> Jalankan \`bun run changelog\` untuk regenerate.

EOF

# Ambil commit, group by tanggal + tipe (conventional commits)
# Format: <tanggal>|<tipe>|<subject>|<hash>
git log --no-merges \
  --pretty=format:'%ad|%s|%h' \
  --date=short \
  | awk -F'|' '
  {
    date = $1
    subject = $2
    hash = $3

    # Extract type dari conventional commit
    if (match(subject, /^(feat|fix|docs|chore|refactor|style|test|perf|ci|build|revert)(\(.+\))?:/)) {
      type = substr(subject, RSTART, RLENGTH)
      sub(/:$/, "", type)
      sub(/\(.+\)/, "", type)
      sub(/^[^:]+:/, "", subject)
      sub(/^ /, "", subject)
    } else {
      type = "other"
      # Keep subject as-is
    }

    print date "|" type "|" subject "|" hash
  }
  ' \
  | sort -t'|' -k1,1r -k2,2 \
  | awk -F'|' '
  {
    date = $1
    type = $2
    subject = $3
    hash = $4

    # New date header
    if (date != last_date) {
      if (last_date != "") print ""
      printf "## %s\n\n", date
      last_date = date
      last_type = ""
    }

    # New type subheader
    if (type != last_type) {
      printf "### %s\n\n", type
      last_type = type
    }

    printf "- %s (`%s`)\n", subject, hash
  }
  ' >> "$OUT"

# Footer
cat >> "$OUT" <<EOF

---

_Generated from git log on $(date +%Y-%m-%d)._
EOF

echo "✓ Changelog generated: $OUT"
echo "  $(wc -l < "$OUT") lines"
