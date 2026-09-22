#!/usr/bin/env python3
"""d2build — fully modular D2 → SVG compiler.

Source layout:
    d2-src/<course>/<bundle>.d2

    Example:
        d2-src/rpl106/pertemuan-2.d2
        d2-src/rpl106/pertemuan-3.d2

Each .d2 file may contain:
    - Multiple diagrams split by   # ===== name =====
    - Or a single diagram (whole file = one diagram, name = filename stem)

Output layout (mirrors source, drops .d2):
    static/d2/<course>/<bundle>/<name>.svg

    Example:
        static/d2/rpl106/pertemuan-2/erd-siklus.svg

Markdown usage:
    {{ d2svg(name="erd-siklus") }}

The shortcode resolves the path via page.extra.code + page.extra.pertemuan.

Commands:
    build   compile diagrams
    check   verify shortcode refs in content/ have matching source
    list    show all diagram names
    clean   remove generated SVGs
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

SRC_ROOT = Path("d2-src")
OUT_ROOT = Path("static/d2")
CACHE_FILE = Path(".d2.cache.json")
CONTENT_DIR = Path("content")

SEPARATOR = re.compile(r"^\s*#\s*={3,}\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*={3,}\s*$")
REF_SHORTCODE = re.compile(r"""d2svg\s*\(\s*name\s*=\s*["']([^"']+)["']""")
FRONTMATTER = re.compile(r"^\+{3,}\s*\n(.*?)\n\+{3,}", re.DOTALL)

D2_ARGS_BASE = [
    "--layout",
    "dagre",
    "--pad",
    "20",
    "--no-xml-tag",
    "--center",
    "--scale",
    "1",
]


# ─────────────────────────────────────────────────────────────
#  Utilities
# ─────────────────────────────────────────────────────────────


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def save_cache(c: dict) -> None:
    CACHE_FILE.write_text(
        json.dumps(c, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def split_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current: str | None = None
    buf: list[str] = []

    def flush() -> None:
        if current is not None:
            body = "\n".join(buf).strip()
            if body:
                sections.append((current, body + "\n"))

    for line in text.splitlines():
        m = SEPARATOR.match(line)
        if m:
            flush()
            current = m.group(1)
            buf = []
        elif current is not None:
            buf.append(line)

    flush()
    return sections


def ensure_d2() -> None:
    if shutil.which("d2") is None:
        sys.exit("error: d2 CLI not found in PATH — install from https://d2lang.com")


# ─────────────────────────────────────────────────────────────
#  Job collection — reads d2-src/<course>/<bundle>.d2
# ─────────────────────────────────────────────────────────────


def collect_jobs() -> list[tuple[str, str, Path, str]]:
    """Return [(name, body, out_dir, origin), ...].

    - name     : diagram name (stem or marker)
    - body     : .d2 source body
    - out_dir  : absolute output dir (static/d2/<course>/<bundle>/)
    - origin   : "<course>/<bundle>.d2" (for logging + cache)
    """
    if not SRC_ROOT.is_dir():
        return []

    jobs: list[tuple[str, str, Path, str]] = []
    seen: set[tuple[str, str]] = set()  # (course, name)

    for course_dir in sorted(SRC_ROOT.iterdir()):
        if not course_dir.is_dir() or course_dir.name.startswith("."):
            continue
        course = course_dir.name

        for src in sorted(course_dir.glob("*.d2")):
            bundle = src.stem
            text = src.read_text(encoding="utf-8")
            sections = split_sections(text)
            out_dir = OUT_ROOT / course / bundle
            origin = f"{course}/{src.name}"

            if sections:
                for name, body in sections:
                    key = (course, name)
                    if key in seen:
                        print(
                            f"  ! duplicate '{course}/{name}', skipping",
                            file=sys.stderr,
                        )
                        continue
                    seen.add(key)
                    jobs.append((name, body, out_dir, origin))
            else:
                name = bundle
                key = (course, name)
                if key in seen:
                    print(f"  ! duplicate '{course}/{name}', skipping", file=sys.stderr)
                    continue
                seen.add(key)
                jobs.append((name, text, out_dir, origin))

    return jobs


# ─────────────────────────────────────────────────────────────
#  Compile
# ─────────────────────────────────────────────────────────────


def compile_one(name: str, body: str, out_dir: Path, theme: int) -> tuple[bool, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{name}.svg"
    tmp = out_dir / f".{name}.d2.tmp"

    try:
        tmp.write_text(body, encoding="utf-8")
        args = ["d2", "--theme", str(theme), *D2_ARGS_BASE, str(tmp), str(target)]
        proc = subprocess.run(args, capture_output=True, text=True)
        if proc.returncode != 0:
            return False, (proc.stderr or proc.stdout or "").strip()[:300]
        if not target.exists() or target.stat().st_size < 200:
            return False, "output SVG missing or suspiciously small"
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, f"{type(e).__name__}: {e}"
    finally:
        tmp.unlink(missing_ok=True)


# ─────────────────────────────────────────────────────────────
#  Commands
# ─────────────────────────────────────────────────────────────

def cmd_build(args) -> int:
    ensure_d2()

    if not SRC_ROOT.is_dir():
        sys.exit(f"error: {SRC_ROOT}/ not found")

    jobs = collect_jobs()
    if not jobs:
        sys.exit(f"error: no .d2 files found in {SRC_ROOT}/<course>/*.d2")

    cache = load_cache()
    new_cache: dict = {}
    to_compile: list[tuple[str, str, Path, str, str]] = []

    for name, body, out_dir, origin in jobs:
        key = origin + "::" + name
        digest = sha(body)
        cached = cache.get(key)
        if cached and cached.get("hash") == digest and not args.force:
            new_cache[key] = cached
            continue
        to_compile.append((name, body, out_dir, origin, digest))

    total = len(jobs)
    skipped = total - len(to_compile)
    ok_cnt = 0
    failed: list[tuple[str, str]] = []

    if not args.quiet:
        print(
            f"d2build · {total} diagram(s) · {len(to_compile)} to compile, {skipped} cached"
        )
        print()

    if to_compile:
        t0 = time.monotonic()
        workers = max(1, args.jobs)

        def run(name, body, out_dir, origin, digest):
            ok, err = compile_one(name, body, out_dir, args.theme)
            return (name, origin, digest, ok, err)

        results = []
        if workers == 1 or len(to_compile) == 1:
            for name, body, out_dir, origin, digest in to_compile:
                if not args.quiet:
                    print(f"  · {origin}  →  {name}")
                results.append(run(name, body, out_dir, origin, digest))
        else:
            with cf.ThreadPoolExecutor(max_workers=workers) as pool:
                futures = [
                    pool.submit(run, name, body, out_dir, origin, digest)
                    for name, body, out_dir, origin, digest in to_compile
                ]
                for i, fut in enumerate(cf.as_completed(futures), 1):
                    name, origin, digest, ok, err = fut.result()
                    if not args.quiet:
                        mark = "✓" if ok else "✗"
                        print(f"  [{i}/{len(to_compile)}] {mark} {origin}  →  {name}")
                    results.append((name, origin, digest, ok, err))

        for name, origin, digest, ok, err in results:
            key = origin + "::" + name
            if ok:
                new_cache[key] = {"hash": digest, "origin": origin}
                ok_cnt += 1
            else:
                failed.append((f"{origin}::{name}", err))
                if args.quiet:
                    print(f"  ✗ {origin}::{name}: {err}", file=sys.stderr)

        elapsed = time.monotonic() - t0
        if not args.quiet:
            print()
            print(f"  compiled {ok_cnt} diagram(s) in {elapsed:.1f}s")

    save_cache(new_cache)

    if args.prune:
        known: set[Path] = set()
        for key in new_cache:
            origin, name = key.split("::", 1)
            course, fname = origin.split("/", 1)
            bundle = fname.rsplit(".", 1)[0]
            known.add(OUT_ROOT / course / bundle / f"{name}.svg")

        pruned = 0
        for svg in OUT_ROOT.rglob("*.svg"):
            if svg not in known:
                svg.unlink()
                if not args.quiet:
                    print(f"  pruned {svg.relative_to(OUT_ROOT)}")
                pruned += 1
        # remove empty dirs
        for d in sorted(OUT_ROOT.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
        if pruned and not args.quiet:
            print()
            print(f"  pruned {pruned} orphan SVG(s)")

    if failed:
        print(f"\n{len(failed)} diagram(s) failed:", file=sys.stderr)
        for name, err in failed:
            print(f"  - {name}: {err}", file=sys.stderr)
        return 1

    return 0


def cmd_clean(args) -> int:
    if OUT_ROOT.exists():
        n = 0
        for f in OUT_ROOT.rglob("*.svg"):
            f.unlink()
            n += 1
        for d in sorted(OUT_ROOT.rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
        print(f"removed {n} SVG(s)")
    CACHE_FILE.unlink(missing_ok=True)
    print("cache cleared")
    return 0


def cmd_list(args) -> int:
    jobs = collect_jobs()
    if not jobs:
        print(f"(no diagrams in {SRC_ROOT}/)")
        return 0
    by_origin: dict[str, list[str]] = {}
    for name, _body, _out_dir, origin in jobs:
        by_origin.setdefault(origin, []).append(name)

    print(f"{len(jobs)} diagram(s):\n")
    for origin in sorted(by_origin):
        print(f"  {origin}:")
        for name in by_origin[origin]:
            print(f"    {name}")
    return 0


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    body = m.group(1)
    out: dict[str, str] = {}
    in_extra = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped == "[extra]":
            in_extra = True
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            in_extra = False
            continue
        m2 = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*"?([^"#]*)"?\s*$', line)
        if m2:
            key, val = m2.group(1), m2.group(2).strip()
            if in_extra:
                out["extra." + key] = val
            else:
                out[key] = val
    return out


def cmd_check(args) -> int:
    if not CONTENT_DIR.is_dir():
        sys.exit(f"error: {CONTENT_DIR}/ not found")

    jobs = collect_jobs()
    available: set[tuple[str, str]] = set()  # (course, name)
    for name, _body, out_dir, _origin in jobs:
        # out_dir = static/d2/<course>/<bundle>
        rel = out_dir.relative_to(OUT_ROOT)
        course = rel.parts[0]
        available.add((course, name))

    refs: list[tuple[Path, int, str, str]] = []  # (md_path, line_no, course, name)
    for md in CONTENT_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = parse_frontmatter(text)
        code = fm.get("extra.code", "").lower().replace('"', "").strip()
        if not code:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in REF_SHORTCODE.finditer(line):
                refs.append((md, i, code, m.group(1)))

    if not refs:
        print("no d2svg refs found in content/")
        return 0

    missing: list[tuple[Path, int, str, str]] = []
    matched = 0
    for md, line, course, name in refs:
        if (course, name) in available:
            matched += 1
        else:
            missing.append((md, line, course, name))

    referenced = {(c, n) for _, _, c, n in refs}
    orphan = sorted(available - referenced)

    print(f"references : {len(refs)}")
    print(f"available  : {len(available)}")
    print(f"matched    : {matched}")
    print()

    rc = 0
    if missing:
        rc = 1
        print(f"✗ MISSING ({len(missing)}):")
        for md, line, course, name in missing:
            rel = md.relative_to(CONTENT_DIR)
            print(f"  {course}/{name}.svg")
            print(f"    {rel}:{line}")
        print()

    if orphan:
        print(f"! UNUSED ({len(orphan)}):")
        for course, name in orphan:
            print(f"  {course}/{name}")
        print()

    if not missing and not orphan:
        print("✓ all clean")

    return rc


# ─────────────────────────────────────────────────────────────
#  CLI
# ─────────────────────────────────────────────────────────────


def main() -> int:
    p = argparse.ArgumentParser(
        prog="d2build",
        description="Compile d2-src/<course>/<bundle>.d2 → static/d2/<course>/<bundle>/*.svg",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="compile diagrams")
    b.add_argument("-f", "--force", action="store_true")
    b.add_argument("--prune", action="store_true")
    b.add_argument("--theme", type=int, default=0)
    b.add_argument("--jobs", "-j", type=int, default=4)
    b.add_argument("-q", "--quiet", action="store_true")
    b.set_defaults(func=cmd_build)

    c = sub.add_parser("clean", help="remove generated SVGs")
    c.set_defaults(func=cmd_clean)

    l = sub.add_parser("list", help="list all diagrams")
    l.set_defaults(func=cmd_list)

    k = sub.add_parser("check", help="verify shortcode refs")
    k.set_defaults(func=cmd_check)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
