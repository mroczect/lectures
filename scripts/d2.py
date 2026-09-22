#!/usr/bin/env python3
"""d2build — compile d2-src/*.d2 → static/d2/*.svg.

Modes
─────
Split mode      : satu file .d2 berisi banyak diagram, dipisah marker
                  `# ===== name =====`.  Tiap section → static/d2/<name>.svg
Per-file mode   : d2-src/foo.d2 → static/d2/foo.svg
Mixed           : keduanya boleh hidup bersama

Commands
────────
  build [--force] [--prune] [--jobs N] [--theme N] [--quiet]
  clean
  list
  check

Why static/, not content/
─────────────────────────
Diagram dipakai lintas halaman (mis. /d2/erd-siklus.svg dipakai di
banyak pertemuan).  static/ adalah tempat untuk aset mentah global.
Kalau suatu saat ada diagram yang cuma dipakai 1 halaman, boleh
dipindah ke page bundle — tapi default tetap static/.
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

SRC_DIR    = Path("d2-src")
OUT_DIR    = Path("static/d2")
CACHE_FILE = Path(".d2.cache.json")
CONTENT_DIR = Path("content")

SEPARATOR = re.compile(r"^\s*#\s*={3,}\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*={3,}\s*$")

REF_PATH = re.compile(r"/d2/([A-Za-z0-9][A-Za-z0-9_-]*)\.svg")
REF_SHORTCODE = re.compile(r"""d2\s*\(\s*name\s*=\s*["']([^"']+)["']""")

D2_ARGS_BASE = [
    "--layout",
    "dagre",
    "--pad",
    "20",
    "--no-xml-tag",
    "--omit-version",
    "--center",
    "--scale",
    "1",
]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def log(msg: str, quiet: bool = False) -> None:
    if not quiet:
        print(msg)


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
    """Split `# ===== name =====` blocks. Baris sebelum marker pertama
    dianggap header/komentar dan diabaikan."""
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


def collect_jobs(src_dir: Path) -> list[tuple[str, str, str]]:
    """Return [(name, body, origin), ...] — deduplicated."""
    if not src_dir.is_dir():
        return []

    jobs: list[tuple[str, str, str]] = []
    seen: set[str] = set()

    for src in sorted(src_dir.glob("*.d2")):
        text = src.read_text(encoding="utf-8")
        sections = split_sections(text)

        if sections:
            for name, body in sections:
                if name in seen:
                    print(
                        f"  ! duplicate diagram name '{name}' in {src.name}, skipping",
                        file=sys.stderr,
                    )
                    continue
                seen.add(name)
                jobs.append((name, body, src.name))
        else:
            name = src.stem
            if name in seen:
                print(f"  ! duplicate '{name}', skipping", file=sys.stderr)
                continue
            seen.add(name)
            jobs.append((name, text, src.name))

    return jobs


def ensure_d2() -> None:
    if shutil.which("d2") is None:
        sys.exit("error: d2 CLI not found in PATH — install from https://d2lang.com")


def compile_one(name: str, body: str, out_dir: Path, theme: int) -> tuple[bool, str]:
    """Compile one diagram. Return (ok, stderr_snippet)."""
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



def cmd_build(args) -> int:
    ensure_d2()

    if not SRC_DIR.is_dir():
        sys.exit(f"error: {SRC_DIR}/ not found")

    out_dir = Path(args.out) if args.out else OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    jobs = collect_jobs(SRC_DIR)
    if not jobs:
        sys.exit(f"error: no .d2 files in {SRC_DIR}/")

    cache = load_cache()
    new_cache: dict = {}
    to_compile: list[tuple[str, str, str, str]] = []

    for name, body, origin in jobs:
        digest = sha(body)
        cached = cache.get(name)
        if cached and cached.get("hash") == digest and not args.force:
            new_cache[name] = cached
            continue
        to_compile.append((name, body, origin, digest))

    total = len(jobs)
    skipped = total - len(to_compile)
    ok_cnt = 0
    failed: list[tuple[str, str]] = []

    log(
        f"d2build · {total} diagram(s) · {len(to_compile)} to compile, {skipped} cached"
    )
    log("")

    if to_compile:
        t0 = time.monotonic()
        workers = max(1, args.jobs)

        if workers == 1 or len(to_compile) == 1:
            for name, body, origin, digest in to_compile:
                log(f"  · {name}  ({origin})", args.quiet)
                ok, err = compile_one(name, body, out_dir, args.theme)
                if ok:
                    new_cache[name] = {"hash": digest, "origin": origin}
                    ok_cnt += 1
                else:
                    failed.append((name, err))
                    print(f"  ✗ {name}: {err}", file=sys.stderr)
        else:
            with cf.ThreadPoolExecutor(max_workers=workers) as pool:
                fut_map = {
                    pool.submit(compile_one, name, body, out_dir, args.theme): (
                        name,
                        origin,
                        digest,
                    )
                    for name, body, origin, digest in to_compile
                }
                done = 0
                for fut in cf.as_completed(fut_map):
                    name, origin, digest = fut_map[fut]
                    done += 1
                    ok, err = fut.result()
                    if ok:
                        new_cache[name] = {"hash": digest, "origin": origin}
                        ok_cnt += 1
                        log(f"  [{done}/{len(to_compile)}] ✓ {name}", args.quiet)
                    else:
                        failed.append((name, err))
                        print(
                            f"  [{done}/{len(to_compile)}] ✗ {name}: {err}",
                            file=sys.stderr,
                        )

        elapsed = time.monotonic() - t0
        log("")
        log(f"  compiled {ok_cnt} diagram(s) in {elapsed:.1f}s")

    save_cache(new_cache)

    if args.prune:
        known = {f"{k}.svg" for k in new_cache}
        pruned = 0
        for f in out_dir.glob("*.svg"):
            if f.name not in known:
                f.unlink()
                log(f"  pruned {f.name}", args.quiet)
                pruned += 1
        if pruned:
            log("")
            log(f"  pruned {pruned} orphan SVG(s)")

    if failed:
        print(f"\n{len(failed)} diagram(s) failed to compile:", file=sys.stderr)
        for name, err in failed:
            print(f"  - {name}: {err}", file=sys.stderr)
        return 1

    return 0


def cmd_clean(args) -> int:
    out_dir = Path(args.out) if args.out else OUT_DIR
    if out_dir.exists():
        n = 0
        for f in out_dir.glob("*.svg"):
            f.unlink()
            n += 1
        print(f"removed {n} SVG(s) from {out_dir}")
    CACHE_FILE.unlink(missing_ok=True)
    print("cache cleared")
    return 0


def cmd_list(args) -> int:
    jobs = collect_jobs(SRC_DIR)
    if not jobs:
        print(f"(no diagrams in {SRC_DIR}/)")
        return 0
    width = max(len(n) for n, _, _ in jobs)
    by_origin: dict[str, list[str]] = {}
    for name, _body, origin in jobs:
        by_origin.setdefault(origin, []).append(name)

    print(f"{len(jobs)} diagram(s) in {SRC_DIR}/:\n")
    for origin in sorted(by_origin):
        print(f"  {origin}:")
        for name in by_origin[origin]:
            print(f"    {name}")
    return 0


def cmd_check(args) -> int:
    """Verify every /d2/*.svg reference in content/ has a matching source."""
    if not CONTENT_DIR.is_dir():
        sys.exit(f"error: {CONTENT_DIR}/ not found")

    jobs = collect_jobs(SRC_DIR)
    available = {name for name, _, _ in jobs}

    refs: dict[str, list[tuple[Path, int]]] = {}
    for md in CONTENT_DIR.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in REF_PATH.finditer(line):
                refs.setdefault(m.group(1), []).append((md, i))
            for m in REF_SHORTCODE.finditer(line):
                refs.setdefault(m.group(1), []).append((md, i))

    if not refs:
        print("no /d2/*.svg references found in content/")
        return 0

    referenced = set(refs)
    missing = sorted(referenced - available)
    orphan = sorted(available - referenced)
    matched = sorted(referenced & available)

    print(f"references : {len(referenced)}")
    print(f"available  : {len(available)}")
    print(f"matched    : {len(matched)}")
    print()

    rc = 0

    if missing:
        rc = 1
        print(f"✗ MISSING SOURCE ({len(missing)}):")
        for name in missing:
            print(f"  {name}.svg")
            for path, line in refs[name][:3]:
                rel = path.relative_to(CONTENT_DIR)
                print(f"    {rel}:{line}")
            if len(refs[name]) > 3:
                print(f"    ... and {len(refs[name]) - 3} more")
        print()

    if orphan:
        print(f"! UNUSED SOURCE ({len(orphan)}):")
        for name in orphan:
            print(f"  {name}  →  {SRC_DIR}/")
        print()

    if not missing and not orphan:
        print("✓ all clean")

    return rc


def main() -> int:
    p = argparse.ArgumentParser(
        prog="d2build",
        description="Compile d2-src/*.d2 → static/d2/*.svg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python scripts/d2.py build --prune
  python scripts/d2.py build --jobs 8 --theme 200
  python scripts/d2.py check
  python scripts/d2.py list
  python scripts/d2.py clean
""",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build", help="compile diagrams")
    b.add_argument(
        "-f", "--force", action="store_true", help="recompile even if cached"
    )
    b.add_argument("--prune", action="store_true", help="delete SVGs with no source")
    b.add_argument("--theme", type=int, default=0, help="d2 theme (default: 0)")
    b.add_argument(
        "--jobs", "-j", type=int, default=4, help="parallel workers (default: 4)"
    )
    b.add_argument("--out", help=f"output dir (default: {OUT_DIR})")
    b.add_argument(
        "-q", "--quiet", action="store_true", help="suppress per-file progress"
    )
    b.set_defaults(func=cmd_build)

    c = sub.add_parser("clean", help="remove generated SVGs + cache")
    c.add_argument("--out", help=f"output dir (default: {OUT_DIR})")
    c.set_defaults(func=cmd_clean)

    l = sub.add_parser("list", help="list diagrams that will be built")
    l.set_defaults(func=cmd_list)

    k = sub.add_parser("check", help="verify content/ refs vs sources")
    k.set_defaults(func=cmd_check)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
