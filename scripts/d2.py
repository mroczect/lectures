#!/usr/bin/env python3
"""d2build — compile all .d2 files from d2-src/ to static/d2/*.svg."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

SRC_DIR    = Path("d2-src")
OUT_DIR    = Path("static/d2")
CACHE_FILE = Path(".d2.cache.json")


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return {}


def save_cache(c: dict) -> None:
    CACHE_FILE.write_text(json.dumps(c, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def compile_one(name: str, source: str, out_dir: Path, theme: int) -> bool:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{name}.svg"
    tmp = out_dir / f".{name}.d2.tmp"
    tmp.write_text(source, encoding="utf-8")

    args = [
        "d2",
        "--theme", str(theme),
        "--layout", "dagre",
        "--pad", "20",
        "--no-xml-tag",
        "--omit-version",
        "--center",
        "--scale", "1",
        str(tmp), str(target),
    ]
    try:
        subprocess.run(args, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ {name}: {e.stderr.strip()}", file=sys.stderr)
        return False
    finally:
        tmp.unlink(missing_ok=True)


def cmd_build(args) -> int:
    if not shutil.which("d2"):
        print("error: d2 CLI not found in PATH", file=sys.stderr)
        return 1

    if not SRC_DIR.is_dir():
        print(f"error: {SRC_DIR} not found", file=sys.stderr)
        return 1

    cache = load_cache()
    new_cache: dict = {}
    total = 0
    changed = 0

    for src in sorted(SRC_DIR.glob("*.d2")):
        name = src.stem
        source = src.read_text(encoding="utf-8")
        digest = sha(source)
        total += 1
        cached = cache.get(name)

        if cached and cached.get("hash") == digest and not args.force:
            new_cache[name] = cached
            continue

        print(f"  · {name}")
        if compile_one(name, source, OUT_DIR, args.theme):
            new_cache[name] = {"hash": digest}
            changed += 1

    save_cache(new_cache)
    print(f"\n{total} file(s), {changed} recompiled")

    if args.prune:
        known = {f"{k}.svg" for k in new_cache}
        for f in OUT_DIR.glob("*.svg"):
            if f.name not in known:
                f.unlink()
                print(f"  pruned {f.name}")

    return 0


def cmd_clean(args) -> int:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    CACHE_FILE.unlink(missing_ok=True)
    print("cleaned")
    return 0


def cmd_list(args) -> int:
    for src in sorted(SRC_DIR.glob("*.d2")):
        print(src.stem)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(prog="d2build")
    sub = p.add_subparsers(dest="cmd", required=True)

    b = sub.add_parser("build")
    b.add_argument("-f", "--force", action="store_true")
    b.add_argument("--prune", action="store_true")
    b.add_argument("--theme", type=int, default=0)
    b.set_defaults(func=cmd_build)

    c = sub.add_parser("clean")
    c.set_defaults(func=cmd_clean)

    l = sub.add_parser("list")
    l.set_defaults(func=cmd_list)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
