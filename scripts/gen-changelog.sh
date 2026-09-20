#!/usr/bin/env bash
#
# Generate content/changelog.md from git history.
# Outputs rich changelog with GitHub links, authors, PRs, and stats.
#
# Usage: ./scripts/gen-changelog.sh [--since YYYY-MM-DD] [--limit N]

set -euo pipefail

# ---------- Config ----------
REPO_ROOT="$(git rev-parse --show-toplevel)"
OUTPUT="$REPO_ROOT/content/changelog.md"
LIMIT=500
SINCE=""

GITHUB_REPO="$(grep -E '^[[:space:]]*github_repo[[:space:]]*=' "$REPO_ROOT/zola.toml" 2>/dev/null | head -1 | sed -E 's/.*"(.*)".*/\1/' || true)"
GITHUB_BRANCH="$(grep -E '^[[:space:]]*github_branch[[:space:]]*=' "$REPO_ROOT/zola.toml" 2>/dev/null | head -1 | sed -E 's/.*"(.*)".*/\1/' || true)"
GITHUB_REPO="${GITHUB_REPO:-mroczect/lectures}"
GITHUB_BRANCH="${GITHUB_BRANCH:-master}"

# ---------- Parse args ----------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --since) SINCE="$2"; shift 2 ;;
        --limit) LIMIT="$2"; shift 2 ;;
        -h|--help) echo "Usage: $0 [--since YYYY-MM-DD] [--limit N]"; exit 0 ;;
        *) echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

cd "$REPO_ROOT"

# ---------- Helpers ----------
classify() {
    case "$1" in
        feat*)     echo "feat" ;;
        fix*)      echo "fix" ;;
        docs*)     echo "docs" ;;
        style*)    echo "style" ;;
        refactor*) echo "refactor" ;;
        perf*)     echo "perf" ;;
        test*)     echo "test" ;;
        chore*)    echo "chore" ;;
        ci*)       echo "ci" ;;
        build*)    echo "build" ;;
        revert*)   echo "revert" ;;
        *)         echo "other" ;;
    esac
}

clean_subject() {
    echo "$1" | sed -E 's/^(feat|fix|docs|style|refactor|perf|test|chore|ci|build|revert)(\([^)]*\))?!?:[[:space:]]*//'
}

extract_scope() {
    echo "$1" | sed -nE 's/^[a-z]+\(([^)]+)\).*/\1/p' | head -1
}

extract_pr() {
    echo "$1" | grep -oE '#[0-9]+' | head -1 | tr -d '#' || true
}

# ---------- Collect raw log ----------
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

GIT_ARGS=(log --no-merges --date=short --shortstat
    --pretty=format:'@COMMIT@%h|%H|%ad|%an|%s')
[[ -n "$SINCE" ]] && GIT_ARGS+=(--since="$SINCE")
GIT_ARGS+=(-n "$LIMIT")

git "${GIT_ARGS[@]}" > "$TMP"

if [[ ! -s "$TMP" ]]; then
    echo "No commits found." >&2
    exit 0
fi

# ---------- Parse records ----------
declare -A DAY_COMMITS
DATES=()
TOTAL=0

cur_hash="" cur_full="" cur_date="" cur_author="" cur_subject="" cur_stats=""

flush_commit() {
    [[ -z "$cur_hash" ]] && return

    local type clean scope pr line
    type="$(classify "$cur_subject")"
    clean="$(clean_subject "$cur_subject")"
    scope="$(extract_scope "$cur_subject")"
    pr="$(extract_pr "$cur_subject")"

    line="- "
    case "$type" in
        feat)     line+="**feat** " ;;
        fix)      line+="**fix** " ;;
        docs)     line+="docs " ;;
        chore)    line+="chore " ;;
        ci)       line+="ci " ;;
        refactor) line+="refactor " ;;
        style)    line+="style " ;;
        perf)     line+="perf " ;;
        test)     line+="test " ;;
        build)    line+="build " ;;
        revert)   line+="revert " ;;
    esac
    [[ -n "$scope" ]] && line+="\`$scope\` "
    line+="[$clean](https://github.com/$GITHUB_REPO/commit/$cur_full)"
    [[ -n "$pr" ]] && line+=" ([#$pr](https://github.com/$GITHUB_REPO/pull/$pr))"
    line+=" — @${cur_author// /-}"

    if [[ -n "$cur_stats" ]]; then
        line+=$'\n'
        line+="  <sub>${cur_stats}</sub>"
    fi
    line+=$'\n'

    DAY_COMMITS[$cur_date]+="$line"
    DATES+=("$cur_date")
    TOTAL=$((TOTAL + 1))

    cur_hash="" cur_full="" cur_date="" cur_author="" cur_subject="" cur_stats=""
}

while IFS= read -r line; do
    if [[ "$line" == @COMMIT@* ]]; then
        flush_commit
        line="${line#@COMMIT@}"
        IFS='|' read -r cur_hash cur_full cur_date cur_author cur_subject <<< "$line"
    elif [[ -n "$line" && "$line" == *"file changed"* ]]; then
        cur_stats="$(echo "$line" | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//')"
    fi
done < "$TMP"

flush_commit

# ---------- Group by month ----------
UNIQUE_DATES="$(printf '%s\n' "${DATES[@]}" | sort -r -u)"

declare -A MONTH_DATES
MONTHS=()
while IFS= read -r date; do
    [[ -z "$date" ]] && continue
    month="${date:0:7}"
    if [[ -z "${MONTH_DATES[$month]:-}" ]]; then
        MONTHS+=("$month")
        MONTH_DATES[$month]=""
    fi
    MONTH_DATES[$month]+="$date"$'\n'
done <<< "$UNIQUE_DATES"

IFS=$'\n' MONTHS=($(printf '%s\n' "${MONTHS[@]}" | sort -r))
unset IFS

# ---------- Generate markdown ----------
TODAY="$(date +%Y-%m-%d)"

{
    echo "+++"
    echo "title = \"Changelog\""
    echo "date = $TODAY"
    echo "updated = $TODAY"
    echo "description = \"All notable changes to this project, generated from git history.\""
    echo "[taxonomies]"
    echo "tags = [\"changelog\", \"reference\"]"
    echo "categories = [\"meta\"]"
    echo "+++"
    echo ""
    echo "All notable changes to this project. Generated from git history."
    echo ""
    echo "Source: [\`$GITHUB_REPO\`](https://github.com/$GITHUB_REPO) · Branch: \`$GITHUB_BRANCH\` · Updated: $TODAY · **$TOTAL commits**."
    echo ""

    for month in "${MONTHS[@]}"; do
        pretty_month="$(date -d "${month}-01" +"%B %Y" 2>/dev/null || echo "$month")"
        echo "## $pretty_month"
        echo ""

        month_dates_sorted="$(printf '%s\n' "${MONTH_DATES[$month]}" | sed '/^$/d' | sort -r)"

        while IFS= read -r date; do
            [[ -z "$date" ]] && continue
            pretty_date="$(date -d "$date" +"%A, %b %d, %Y" 2>/dev/null || echo "$date")"
            echo "### $pretty_date"
            echo ""
            printf '%s' "${DAY_COMMITS[$date]}"
            echo ""
        done <<< "$month_dates_sorted"
    done
} > "$OUTPUT"

echo "Wrote $OUTPUT ($TOTAL commits)"
