#!/usr/bin/env python3
"""
Generate content/changelog.md from git history.

Outputs rich changelog with GitHub commit links, PR links, authors,
conventional commit types, scopes, and diff stats.

Usage:
    ./scripts/gen_changelog.py [--since YYYY-MM-DD] [--limit N]
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path



def get_repo_root() -> Path:
    out = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
    return Path(out)


def read_config(repo_root: Path) -> tuple[str, str]:
    cfg = repo_root / "zola.toml"
    gh_repo = "mroczect/lectures"
    gh_branch = "master"

    if not cfg.exists():
        return gh_repo, gh_branch

    text = cfg.read_text()
    for line in text.splitlines():
        m = re.match(r'\s*github_repo\s*=\s*"([^"]+)"', line)
        if m:
            gh_repo = m.group(1)
            continue
        m = re.match(r'\s*github_branch\s*=\s*"([^"]+)"', line)
        if m:
            gh_branch = m.group(1)

    return gh_repo, gh_branch



TYPES = {
    "feat": "feat",
    "feature": "feat",
    "fix": "fix",
    "bugfix": "fix",
    "docs": "docs",
    "doc": "docs",
    "style": "style",
    "refactor": "refactor",
    "perf": "perf",
    "test": "test",
    "tests": "test",
    "chore": "chore",
    "ci": "ci",
    "build": "build",
    "revert": "revert",
}

CC_PATTERN = re.compile(
    r"^(?P<type>[a-z]+)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r"!?"
    r":\s*"
    r"(?P<message>.+)$",
    re.IGNORECASE,
)

PR_PATTERN = re.compile(r"\(#(\d+)\)")
PR_PATTERN_ALT = re.compile(r"#(\d+)")


def classify(subject: str) -> str:
    m = CC_PATTERN.match(subject)
    if not m:
        return "other"
    t = m.group("type").lower()
    return TYPES.get(t, "other")


def parse_subject(subject: str) -> tuple[str, str, str | None]:
    m = CC_PATTERN.match(subject)
    if not m:
        return "other", subject, None
    t = TYPES.get(m.group("type").lower(), "other")
    msg = m.group("message").strip()
    scope = m.group("scope")
    return t, msg, scope


def extract_pr(subject: str) -> str | None:
    m = PR_PATTERN.search(subject)
    if m:
        return m.group(1)
    m = PR_PATTERN_ALT.search(subject)
    if m:
        return m.group(1)
    return None




def collect_commits(limit: int, since: str | None) -> list[dict]:
    marker = "@@@COMMIT@@@"
    fmt = f"{marker}%h|%H|%ad|%an|%s"

    args = [
        "git",
        "log",
        "--no-merges",
        "--date=short",
        "--shortstat",
        f"--pretty=format:{fmt}",
        "-n",
        str(limit),
    ]
    if since:
        args.append(f"--since={since}")

    out = subprocess.check_output(args, text=True)

    commits: list[dict] = []
    current: dict | None = None

    for line in out.splitlines():
        if line.startswith(marker):
            if current:
                commits.append(current)
            payload = line[len(marker) :]
            parts = payload.split("|", 4)
            if len(parts) != 5:
                current = None
                continue
            short, full, cdate, author, subject = parts
            current = {
                "short": short,
                "full": full,
                "date": cdate,
                "author": author,
                "subject": subject,
                "stats": "",
            }
        elif current and "file changed" in line:
            current["stats"] = line.strip()

    if current:
        commits.append(current)

    return commits



BADGE_MAP = {
    "feat": "**feat**",
    "fix": "**fix**",
    "docs": "docs",
    "chore": "chore",
    "ci": "ci",
    "refactor": "refactor",
    "style": "style",
    "perf": "perf",
    "test": "test",
    "build": "build",
    "revert": "revert",
}


def render_commit(commit: dict, gh_repo: str) -> str:
    subject = commit["subject"]
    ctype, message, scope = parse_subject(subject)
    pr = extract_pr(subject)
    author = commit["author"].replace(" ", "-")
    full = commit["full"]
    stats = commit.get("stats", "")

    parts = ["- "]

    badge = BADGE_MAP.get(ctype)
    if badge:
        parts.append(f"{badge} ")

    if scope:
        parts.append(f"`{scope}` ")

    parts.append(f"[{message}](https://github.com/{gh_repo}/commit/{full})")

    if pr:
        parts.append(f" ([#{pr}](https://github.com/{gh_repo}/pull/{pr}))")

    parts.append(f" — @{author}")

    line = "".join(parts)

    if stats:
        line += f"\n  <sub>{stats}</sub>"

    return line + "\n"


def pretty_month(month: str) -> str:
    try:
        d = datetime.strptime(month + "-01", "%Y-%m-%d")
        return d.strftime("%B %Y")
    except ValueError:
        return month


def pretty_date(date_str: str) -> str:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%A, %b %d, %Y")
    except ValueError:
        return date_str


def build_markdown(
    commits: list[dict],
    gh_repo: str,
    gh_branch: str,
) -> str:
    if not commits:
        return ""

    by_date: dict[str, list[dict]] = defaultdict(list)
    for c in commits:
        by_date[c["date"]].append(c)

    by_month: dict[str, list[str]] = defaultdict(list)
    for d in sorted(by_date.keys(), reverse=True):
        month = d[:7]
        by_month[month].append(d)

    today = date.today().isoformat()
    total = len(commits)

    out: list[str] = []
    out.append("+++")
    out.append('title = "Changelog"')
    out.append(f"date = {today}")
    out.append(f"updated = {today}")
    out.append(
        'description = "All notable changes to this project, generated from git history."'
    )
    out.append("[taxonomies]")
    out.append('tags = ["changelog", "reference"]')
    out.append('categories = ["meta"]')
    out.append("+++")
    out.append("")
    out.append("All notable changes to this project. Generated from git history.")
    out.append("")
    out.append(
        f"Source: [`{gh_repo}`](https://github.com/{gh_repo}) · "
        f"Branch: `{gh_branch}` · Updated: {today} · **{total} commits**."
    )
    out.append("")

    for month in sorted(by_month.keys(), reverse=True):
        out.append(f"## {pretty_month(month)}")
        out.append("")
        for d in sorted(by_month[month], reverse=True):
            out.append(f"### {pretty_date(d)}")
            out.append("")
            for c in by_date[d]:
                out.append(render_commit(c, gh_repo))
        out.append("")

    return "\n".join(out)




def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate content/changelog.md from git history."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=500,
        help="Max number of commits to include (default: 500)",
    )
    parser.add_argument(
        "--since",
        type=str,
        default=None,
        help="Only include commits since YYYY-MM-DD",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Override output path (default: <repo>/content/changelog.md)",
    )
    args = parser.parse_args()

    repo_root = get_repo_root()
    gh_repo, gh_branch = read_config(repo_root)

    output = (
        Path(args.output) if args.output else repo_root / "content" / "changelog.md"
    )

    commits = collect_commits(args.limit, args.since)
    if not commits:
        print("No commits found.", file=sys.stderr)
        return 0

    md = build_markdown(commits, gh_repo, gh_branch)
    output.write_text(md)
    print(f"Wrote {output} ({len(commits)} commits)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
