# Snapcat Output

```
scripts/
    ├── d2.pyd2.py
    ├── docgen.pydocgen.py
    ├── docrel.pydocrel.py
    └── gen_changelog.pygen_changelog.py

0 directories, 4 files
```

## Files

### d2.py
```
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
```

SHA256: `56c7a7e3a8ac952a623ef172afc01bb2f49a7f056cefd367f492157edc3057e8`

### docgen.py
```
#!/usr/bin/env python3
"""docgen — generate markdown docs with standard frontmatter.

Filename: YYYY-MM-DD-{slug}.md

Usage:
    python scripts/docgen.py <type> <slug> [options]

Examples:
    python scripts/docgen.py note fix-auth-bug
    python scripts/docgen.py rps rpl106 --set code=RPL106 --set course="Pengantar Basis Data"
    python scripts/docgen.py announce rilis-v1 -o content/posts/
    python scripts/docgen.py modul praktikum-01 --set pertemuan=1
    python scripts/docgen.py --list-types
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from string import Template

TODAY = dt.date.today().isoformat()

TEMPLATES: dict[str, Template] = {}


def _register(name: str, body: str) -> None:
    TEMPLATES[name] = Template(body)


_register(
    "note",
    """+++
title = "$title"
description = "$description"
date = $date
tags = [$tags]

[extra]
category = "note"
author = "$author"
status = "$status"
+++

## Ringkasan

$summary

## Catatan

-

## Referensi

-
""",
)

_register(
    "log",
    """+++
title = "$title"
description = "$description"
date = $date
tags = [$tags]

[extra]
category = "log"
author = "$author"
status = "$status"
+++

## Ringkasan

$summary

## Yang berubah

-

## Catatan

-
""",
)

_register(
    "announce",
    """+++
title = "$title"
description = "$description"
date = $date
tags = [$tags]

[extra]
category = "announcement"
priority = "$priority"
author = "$author"
status = "$status"
+++

## Ringkasan

$summary

## Detail

-

## Tindakan

- [ ]
""",
)

_register(
    "rps",
    """+++
title = "RPS — $course"
description = "$description"
date = $date
tags = [$tags]

[extra]
code = "$code"
course = "$course"
sks = "$sks"
semester = "$semester"
author = "$author"
status = "$status"
+++

## Identitas

| Field | Nilai |
|---|---|
| Kode | $code |
| Nama | $course |
| SKS | $sks |
| Semester | $semester |
| Pengampu | $author |
| Prasyarat | — |

## Deskripsi

$summary

## Capaian Pembelajaran

-

## Rencana Pembelajaran

| Pertemuan | Materi | Aktivitas | Estimasi |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| **ATS** | | | |
| 4 | | | |
| 5 | | | |
| **AAS** | | | |

## Penilaian

| Komponen | Bobot |
|---|---|
| Tugas | 30% |
| ATS | 30% |
| AAS | 40% |

## Referensi

-
""",
)

_register(
    "modul",
    """+++
title = "$title"
description = "$description"
date = $date
tags = [$tags]

[extra]
code = "$code"
course = "$course"
pertemuan = "$pertemuan"
author = "$author"
status = "$status"
+++

## Tujuan

-

## Alat dan Bahan

-

## Langkah Kerja

1.
2.
3.

## Latihan

-

## Pengumpulan

- Format nama file: `${code}_P${pertemuan}_${nim}_${nama}`
- Deadline:
""",
)

_register(
    "adr",
    """+++
title = "ADR — $title"
description = "$description"
date = $date
tags = [$tags]

[extra]
category = "adr"
status = "$status"
author = "$author"
+++

## Konteks

$summary

## Keputusan

-

## Konsekuensi

**Positif**

-

**Negatif**

-

## Alternatif

| Alternatif | Alasan ditolak |
|---|---|
| | |
""",
)


DEFAULTS: dict[str, str] = {
    "date": TODAY,
    "author": "",
    "status": "draft",
    "tags": "",
    "description": "",
    "summary": "",
    "title": "",
    "priority": "normal",
    "code": "",
    "course": "",
    "sks": "3 SKS",
    "semester": "Ganjil 2026/2027",
    "pertemuan": "1",
    "nim": "",
    "nama": "",
}


SLUG_RE = re.compile(r"[^a-z0-9]+")
PLACEHOLDER_RE = re.compile(r"\$([a-zA-Z_][a-zA-Z0-9_]*)")


def slugify(s: str) -> str:
    return SLUG_RE.sub("-", s.lower().strip()).strip("-")


def cmd_list_types() -> int:
    for name in sorted(TEMPLATES):
        print(name)
    return 0


def cmd_generate(args) -> int:
    slug = slugify(args.slug)
    if not slug:
        print("error: slug must contain letters or digits", file=sys.stderr)
        return 1

    if args.template:
        tp = Path(args.template).expanduser()
        if not tp.is_file():
            print(f"error: template not found: {tp}", file=sys.stderr)
            return 1
        tmpl = Template(tp.read_text(encoding="utf-8"))
    else:
        if args.type not in TEMPLATES:
            print(f"error: unknown type '{args.type}'", file=sys.stderr)
            print(f"available: {', '.join(sorted(TEMPLATES))}", file=sys.stderr)
            return 1
        tmpl = TEMPLATES[args.type]

    ctx = dict(DEFAULTS)
    ctx["title"] = slug.replace("-", " ").title()

    for kv in args.set:
        if "=" not in kv:
            print(f"error: invalid --set '{kv}' (expected key=value)", file=sys.stderr)
            return 1
        k, v = kv.split("=", 1)
        ctx[k.strip()] = v.strip()

    for flag in ("title", "author", "tags", "description"):
        val = getattr(args, flag)
        if val:
            ctx[flag] = val

    # ensure all placeholders in the template have a value
    for key in set(PLACEHOLDER_RE.findall(tmpl.template)):
        ctx.setdefault(key, "")

    content = tmpl.substitute(ctx)

    filename = f"{ctx['date']}-{slug}.md"
    out_dir = Path(args.out).expanduser() if args.out else Path(".")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename

    if out_path.exists() and not args.force:
        print(f"error: file exists: {out_path}", file=sys.stderr)
        print("use --force to overwrite", file=sys.stderr)
        return 1

    if args.dry_run:
        print(f"--- {out_path} ---")
        print(content)
        return 0

    out_path.write_text(content, encoding="utf-8")
    print(f"created: {out_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="docgen",
        description="Generate markdown docs with standard frontmatter.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
types:
  note      catatan umum
  log       catatan harian / changelog
  announce  pengumuman
  rps       rencana pembelajaran semester
  modul     modul praktikum
  adr       architecture decision record

examples:
  docgen note fix-auth-bug
  docgen rps rpl106 --set code=RPL106 --set course="Pengantar Basis Data"
  docgen announce rilis-v1 -o content/posts/
  docgen modul praktikum-01 --set pertemuan=1 --set code=RPL106
  docgen --list-types
""",
    )
    p.add_argument("type", nargs="?", help="document type")
    p.add_argument("slug", nargs="?", help="short slug for filename")
    p.add_argument("-o", "--out", help="output directory")
    p.add_argument("-t", "--template", help="custom template file")
    p.add_argument("--title")
    p.add_argument("--author")
    p.add_argument("--tags")
    p.add_argument("--description")
    p.add_argument(
        "--set",
        action="append",
        default=[],
        help="KEY=VALUE placeholder override (repeatable)",
    )
    p.add_argument("-f", "--force", action="store_true", help="overwrite existing file")
    p.add_argument("--dry-run", action="store_true", help="print, don't write")
    p.add_argument("--list-types", action="store_true", help="show available types")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_types:
        return cmd_list_types()

    if not args.type or not args.slug:
        parser.print_help()
        return 1

    return cmd_generate(args)


if __name__ == "__main__":
    sys.exit(main())
```

SHA256: `fd11826e909216742eeb4d663974cd0453144c4e2b92433f04c0d1ac7de1ada7`

### docrel.py
```
#!/usr/bin/env python3
"""docrel — manage document releases on GitHub.

Keep PDF/DOCX/archives out of git history. Upload them to GitHub Releases
instead, and reference download URLs from your content.

Single file, stdlib only, uses `gh` CLI for authentication.

Requirements:
    Python 3.8+
    gh      https://cli.github.com/  (authenticated: `gh auth login`)
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

VERSION = "0.3.0"

CONFIG_FILE = ".docrel.json"
CACHE_FILE = ".docrel.cache.json"
MANIFEST_FILE = ".docrel.releases.json"


# ============================================================
#  Terminal
# ============================================================


def _tty() -> bool:
    return sys.stdout.isatty() and os.environ.get("NO_COLOR") is None


class C:
    RED = "\033[31m" if _tty() else ""
    YEL = "\033[33m" if _tty() else ""
    GRN = "\033[32m" if _tty() else ""
    CYA = "\033[36m" if _tty() else ""
    DIM = "\033[2m" if _tty() else ""
    BLD = "\033[1m" if _tty() else ""
    RST = "\033[0m" if _tty() else ""


def die(msg: str, code: int = 1) -> None:
    print(f"{C.RED}error:{C.RST} {msg}", file=sys.stderr)
    sys.exit(code)


def info(msg: str) -> None:
    print(f"{C.DIM}·{C.RST} {msg}")


def ok(msg: str) -> None:
    print(f"{C.GRN}✓{C.RST} {msg}")


def warn(msg: str) -> None:
    print(f"{C.YEL}!{C.RST} {msg}")


def step(msg: str) -> None:
    print(f"{C.BLD}{msg}{C.RST}")


def human_size(n: int) -> str:
    x = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if x < 1024:
            return f"{x:.0f} {unit}" if unit == "B" else f"{x:.1f} {unit}"
        x /= 1024
    return f"{x:.1f} TB"


def confirm(prompt: str, default: bool = False) -> bool:
    suffix = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"{prompt} {suffix} ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    return default if not ans else ans in ("y", "yes")


# ============================================================
#  Config
# ============================================================


@dataclass
class Config:
    large_file_mb: int = 5
    files_dir: str = "static/files"
    content_dir: str = "content"
    release_prefix: str = ""
    parallel: int = 4

    @classmethod
    def load(cls, path: Path = Path(CONFIG_FILE)) -> Config:
        if not path.exists():
            return cls()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            die(f"{path} invalid JSON: {e}")
        known = {f for f in cls.__dataclass_fields__}
        return cls(**{k: v for k, v in data.items() if k in known})

    def save(self, path: Path = Path(CONFIG_FILE)) -> None:
        path.write_text(
            json.dumps(asdict(self), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def tag(self, name: str) -> str:
        return f"{self.release_prefix}{name}" if self.release_prefix else name


# ============================================================
#  Cache (SHA256 per uploaded file)
# ============================================================


class Cache:
    def __init__(self, path: Path = Path(CACHE_FILE)):
        self.path = path
        self.data: dict[str, dict[str, str]] = {}
        if path.exists():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                self.data = {}

    def get(self, tag: str, filename: str) -> str | None:
        return self.data.get(tag, {}).get(filename)

    def set(self, tag: str, filename: str, digest: str) -> None:
        self.data.setdefault(tag, {})[filename] = digest

    def forget(self, tag: str, filename: str) -> None:
        self.data.get(tag, {}).pop(filename, None)

    def drop_tag(self, tag: str) -> None:
        self.data.pop(tag, None)

    def save(self) -> None:
        self.path.write_text(
            json.dumps(self.data, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )


# ============================================================
#  Release metadata
# ============================================================


@dataclass
class ReleaseMeta:
    """Structured metadata for a release.

    Stored in .docrel.releases.json. Used to generate the GitHub
    release body and to make the release self-describing.
    """

    title: str = ""
    summary: str = ""
    body: str = ""
    category: str = ""
    tags: list[str] = field(default_factory=list)
    author: str = ""
    date: str = ""
    version: str = ""
    status: str = "stable"  # draft | stable | deprecated
    license: str = ""
    homepage: str = ""

    @classmethod
    def from_dict(cls, d: dict) -> ReleaseMeta:
        known = set(cls.__dataclass_fields__)
        return cls(**{k: v for k, v in d.items() if k in known})

    def to_dict(self) -> dict:
        return asdict(self)

    def is_empty(self) -> bool:
        return (
            not any(
                getattr(self, f)
                for f in (
                    "title",
                    "summary",
                    "body",
                    "category",
                    "author",
                    "date",
                    "version",
                    "license",
                    "homepage",
                )
            )
            and not self.tags
        )


class Manifest:
    """Map of tag -> ReleaseMeta, persisted to .docrel.releases.json."""

    def __init__(self, path: Path = Path(MANIFEST_FILE)):
        self.path = path
        self.data: dict[str, ReleaseMeta] = {}
        if path.exists():
            try:
                raw = json.loads(path.read_text(encoding="utf-8"))
                self.data = {k: ReleaseMeta.from_dict(v) for k, v in raw.items()}
            except (json.JSONDecodeError, TypeError):
                self.data = {}

    def get(self, tag: str) -> ReleaseMeta:
        return self.data.get(tag, ReleaseMeta())

    def set(self, tag: str, meta: ReleaseMeta) -> None:
        self.data[tag] = meta

    def remove(self, tag: str) -> bool:
        return self.data.pop(tag, None) is not None

    def save(self) -> None:
        raw = {k: v.to_dict() for k, v in self.data.items()}
        self.path.write_text(
            json.dumps(raw, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )


def body_from_meta(meta: ReleaseMeta) -> str:
    """Render a release body from metadata, Markdown-friendly."""
    parts: list[str] = []

    if meta.summary:
        parts.append(meta.summary)

    fields = [
        ("Category", meta.category),
        ("Author", meta.author),
        ("Date", meta.date),
        ("Version", meta.version),
        ("Status", meta.status),
        ("License", meta.license),
        ("Homepage", meta.homepage),
    ]
    fields = [(k, v) for k, v in fields if v]
    if fields:
        table_lines = ["| Field | Value |", "|---|---|"]
        for k, v in fields:
            table_lines.append(f"| {k} | {v} |")
        parts.append("\n".join(table_lines))

    if meta.tags:
        parts.append("Tags: " + ", ".join(f"`{t}`" for t in meta.tags))

    if meta.body:
        parts.append(meta.body)

    return "\n\n".join(parts).strip()

@dataclass
class Asset:
    name: str
    size: int
    url: str = ""
    state: str = ""


class Gh:
    def __init__(self):
        if shutil.which("gh") is None:
            die("gh CLI not found. Install: https://cli.github.com/")
        self._repo: str | None = None

    def _run(self, args: list[str], check: bool = True) -> subprocess.CompletedProcess:
        proc = subprocess.run(
            ["gh", *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        if check and proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "").strip()
            die(f"gh {' '.join(args)} failed: {err}")
        return proc

    def repo(self) -> str:
        if self._repo is None:
            self._repo = self._run(
                ["repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"]
            ).stdout.strip()
        return self._repo

    def exists(self, tag: str) -> bool:
        return self._run(["release", "view", tag], check=False).returncode == 0

    def releases(self) -> list[dict]:
        proc = self._run(
            [
                "release",
                "list",
                "--limit",
                "200",
                "--json",
                "tagName,name,publishedAt,isDraft,isPrerelease,assets",
                "-q",
                ".",
            ],
            check=False,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            return []
        try:
            return json.loads(proc.stdout)
        except json.JSONDecodeError:
            return []

    def assets(self, tag: str) -> list[Asset]:
        proc = self._run(
            [
                "release",
                "view",
                tag,
                "--json",
                "assets",
                "-q",
                ".assets[] | {name: .name, size: .size, url: .url, state: .state}",
            ],
            check=False,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            return []
        out: list[Asset] = []
        for line in proc.stdout.splitlines():
            if not line.strip():
                continue
            try:
                j = json.loads(line)
                out.append(
                    Asset(j["name"], j["size"], j.get("url", ""), j.get("state", ""))
                )
            except json.JSONDecodeError:
                continue
        return out

    def create(
        self,
        tag: str,
        title: str,
        notes: str,
        files: list[Path],
        draft: bool,
        prerelease: bool,
    ) -> None:
        args = [
            "release",
            "create",
            tag,
            "--title",
            title or tag,
            "--notes",
            notes or "",
        ]
        if draft:
            args.append("--draft")
        if prerelease:
            args.append("--prerelease")
        args += [str(f) for f in files]
        subprocess.run(["gh", *args], check=True)

    def upload(self, tag: str, files: list[Path]) -> None:
        args = ["release", "upload", tag, *[str(f) for f in files], "--clobber"]
        subprocess.run(["gh", *args], check=True)

    def delete_asset(self, tag: str, name: str) -> None:
        self._run(["release", "delete-asset", tag, name, "-y"])

    def delete_release(self, tag: str) -> None:
        self._run(["release", "delete", tag, "-y"])

    def edit(
        self,
        tag: str,
        title: str = "",
        notes: str | None = None,
        draft: bool | None = None,
        prerelease: bool | None = None,
    ) -> None:
        args = ["release", "edit", tag]
        if title:
            args += ["--title", title]
        if notes is not None:
            args += ["--notes", notes]
        if draft is True:
            args.append("--draft")
        if prerelease is True:
            args.append("--prerelease")
        self._run(args)

    def view(self, tag: str) -> dict | None:
        proc = self._run(
            [
                "release",
                "view",
                tag,
                "--json",
                "tagName,name,body,publishedAt,isDraft,isPrerelease,assets",
            ],
            check=False,
        )
        if proc.returncode != 0 or not proc.stdout.strip():
            return None
        try:
            return json.loads(proc.stdout)
        except json.JSONDecodeError:
            return None

    def download(
        self, tag: str, pattern: str, dest: Path, clobber: bool = True
    ) -> None:
        args = ["release", "download", tag, "--pattern", pattern, "--dir", str(dest)]
        if clobber:
            args.append("--clobber")
        self._run(args, check=False)

    def download_url(self, tag: str, name: str) -> str:
        return f"https://github.com/{self.repo()}/releases/download/{tag}/{name}"

    def web_url(self, tag: str) -> str:
        return f"https://github.com/{self.repo()}/releases/tag/{tag}"


# ============================================================
#  Helpers
# ============================================================

TAG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def validate_tag(tag: str) -> None:
    if not TAG_RE.match(tag):
        die(f"invalid tag '{tag}': use letters, digits, dash, dot, underscore")


def sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(chunk), b""):
            h.update(block)
    return h.hexdigest()


def file_size(p: Path) -> int:
    try:
        return p.stat().st_size
    except OSError:
        return 0


def resolve_files(paths: list[str]) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        path = Path(p).expanduser().resolve()
        if not path.is_file():
            die(f"file not found: {p}")
        out.append(path)
    return out


def dir_files(src: Path) -> dict[str, Path]:
    if not src.is_dir():
        die(f"directory not found: {src}")
    return {
        f.name: f for f in src.iterdir() if f.is_file() and not f.name.startswith(".")
    }


def find_release_links(content_dir: Path) -> list[tuple[Path, int, str]]:
    pattern = re.compile(
        r"https://github\.com/[^/\s]+/[^/\s]+/releases/download/[^\s\)\"'>]+"
    )
    hits: list[tuple[Path, int, str]] = []
    if not content_dir.is_dir():
        return hits
    for md in content_dir.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for m in pattern.finditer(line):
                hits.append((md, i, m.group(0)))
    return hits


def parse_set_args(pairs: list[str], meta: ReleaseMeta) -> None:
    """Apply KEY=VALUE pairs to meta. Supports tags=a,b and body_file=path."""
    for pair in pairs:
        if "=" not in pair:
            die(f"invalid set: {pair} (expected key=value)")
        key, val = pair.split("=", 1)
        key = key.strip()
        val = val.strip()
        if key == "tags":
            meta.tags = [t.strip() for t in val.split(",") if t.strip()]
        elif key == "body_file":
            p = Path(val).expanduser()
            if not p.is_file():
                die(f"body file not found: {val}")
            meta.body = p.read_text(encoding="utf-8")
        elif hasattr(meta, key):
            setattr(meta, key, val)
        else:
            warn(f"unknown field: {key}")


# ============================================================
#  Commands
# ============================================================


def cmd_init(args) -> int:
    cfg = Config.load()
    if args.large_mb is not None:
        cfg.large_file_mb = args.large_mb
    if args.files_dir is not None:
        cfg.files_dir = args.files_dir
    if args.content_dir is not None:
        cfg.content_dir = args.content_dir
    if args.prefix is not None:
        cfg.release_prefix = args.prefix
    if args.parallel is not None:
        cfg.parallel = args.parallel

    cfg.save()
    ok(f"wrote {CONFIG_FILE}")
    print(json.dumps(asdict(cfg), indent=2, ensure_ascii=False))
    return 0


def cmd_check(args) -> int:
    cfg = Config.load()
    threshold_mb = args.threshold or cfg.large_file_mb
    threshold_bytes = threshold_mb * 1024 * 1024

    step("Repo size")
    if Path(".git").exists():
        total = sum(
            os.path.getsize(os.path.join(r, f))
            for r, _, fs in os.walk(".git")
            for f in fs
            if os.path.exists(os.path.join(r, f))
        )
        print(f"  {human_size(total):>10}  .git")
    print()

    step(f"Tracked files > {threshold_mb} MB")
    proc = subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True)
    tracked = [f for f in proc.stdout.split("\0") if f]
    big = sorted(
        (
            (file_size(Path(f)), f)
            for f in tracked
            if Path(f).is_file() and file_size(Path(f)) > threshold_bytes
        ),
        reverse=True,
    )
    if not big:
        ok("none")
    else:
        for sz, f in big:
            print(f"  {C.RED}{human_size(sz):>10}{C.RST}  {f}")
        warn("Move to a release: docrel new <tag> <files...>")
    print()

    step("Junk files")
    junk_re = re.compile(
        r"(^|/)(\.DS_Store|Thumbs\.db|Desktop\.ini)$|\.(swp|swo|bak|old|orig)$"
    )
    junk = [f for f in tracked if junk_re.search(f)]
    if not junk:
        ok("clean")
    else:
        for f in junk:
            print(f"  {C.RED}junk{C.RST}  {f}")
    print()

    step("Cache")
    cache = Cache()
    tags = len(cache.data)
    total = sum(len(v) for v in cache.data.values())
    print(f"  {tags} tag(s), {total} file(s) recorded")
    print()

    step("Manifest")
    m = Manifest()
    print(f"  {len(m.data)} release meta record(s)")
    print()

    step("Git status")
    proc = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
    if not proc.stdout.strip():
        ok("clean working tree")
    else:
        print(proc.stdout.rstrip())
    return 0 if not big else 1


def cmd_status(args) -> int:
    cfg = Config.load()
    gh = Gh()
    m = Manifest()

    step(f"docrel {VERSION}")
    print(f"  repo:         {gh.repo()}")
    print(f"  files_dir:    {cfg.files_dir}")
    print(f"  content_dir:  {cfg.content_dir}")
    print(f"  large_file:   {cfg.large_file_mb} MB")
    print(f"  prefix:       {cfg.release_prefix or '(none)'}")
    print()

    releases = gh.releases()
    if not releases:
        warn("no releases yet")
        return 0

    step(f"Releases ({len(releases)})")
    for r in releases:
        tag = r["tagName"]
        name = r.get("name") or ""
        date = (r.get("publishedAt") or "")[:10]
        n = len(r.get("assets") or [])
        total = sum(a.get("size", 0) for a in (r.get("assets") or []))
        flags = []
        if r.get("isDraft"):
            flags.append("draft")
        if r.get("isPrerelease"):
            flags.append("pre")
        flag_s = f" {C.DIM}[{','.join(flags)}]{C.RST}" if flags else ""

        meta = m.get(tag)
        meta_bits = []
        if meta.category:
            meta_bits.append(meta.category)
        if meta.version:
            meta_bits.append(f"v{meta.version}")
        if meta.tags:
            meta_bits.append(" ".join(f"#{t}" for t in meta.tags[:3]))
        meta_s = f"  {C.CYA}{' · '.join(meta_bits)}{C.RST}" if meta_bits else ""

        print(
            f"  {C.BLD}{tag}{C.RST}  {date}  {n} file(s)  {human_size(total)}{flag_s}{meta_s}"
        )
        if name:
            print(f"    {C.DIM}{name}{C.RST}")
    return 0


def cmd_list(args) -> int:
    gh = Gh()
    tag = Config.load().tag(args.tag)
    if not gh.exists(tag):
        die(f"release '{tag}' not found")
    assets = gh.assets(tag)
    if not assets:
        warn("no files in this release")
        return 0
    print(f"{C.BLD}{tag}{C.RST}  ({len(assets)} file(s))")
    print()
    for a in sorted(assets, key=lambda x: x.name):
        print(f"  {human_size(a.size):>10}  {a.name}")
        if args.urls:
            print(f"              {C.DIM}{gh.download_url(tag, a.name)}{C.RST}")
    return 0


def _collect_meta(args, meta: ReleaseMeta) -> None:
    """Merge CLI args into meta."""
    if getattr(args, "title", None):
        meta.title = args.title
    if getattr(args, "summary", None):
        meta.summary = args.summary
    if getattr(args, "body", None):
        meta.body = args.body
    if getattr(args, "body_file", None):
        p = Path(args.body_file).expanduser()
        if not p.is_file():
            die(f"body file not found: {args.body_file}")
        meta.body = p.read_text(encoding="utf-8")
    if getattr(args, "category", None):
        meta.category = args.category
    if getattr(args, "tags", None):
        meta.tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    if getattr(args, "author", None):
        meta.author = args.author
    if getattr(args, "version", None):
        meta.version = args.version
    if getattr(args, "status", None):
        meta.status = args.status
    if getattr(args, "license", None):
        meta.license = args.license
    if getattr(args, "homepage", None):
        meta.homepage = args.homepage
    if getattr(args, "date", None):
        meta.date = args.date
    if not meta.date:
        meta.date = time.strftime("%Y-%m-%d")


def cmd_new(args) -> int:
    cfg = Config.load()
    tag = cfg.tag(args.tag)
    validate_tag(tag)

    gh = Gh()
    m = Manifest()
    meta = m.get(tag)
    _collect_meta(args, meta)

    if not meta.title:
        die("title required (use --title or set it via `docrel meta-set`)")

    body = body_from_meta(meta)

    # Persist meta first
    m.set(tag, meta)
    m.save()

    if gh.exists(tag):
        warn(f"release '{tag}' already exists")
        if args.force or confirm("Upload files to existing release?"):
            return _upload(tag, resolve_files(args.files), gh, cfg)
        return 1

    files = resolve_files(args.files)

    if args.dry_run:
        step("would create release")
        print(f"  tag:    {tag}")
        print(f"  title:  {meta.title}")
        for f in files:
            print(f"  file:   {f.name}  ({human_size(file_size(f))})")
        print()
        step("body preview")
        print(body)
        return 0

    info(f"creating release {tag}...")
    gh.create(tag, meta.title, body, files, args.draft, args.prerelease)
    ok(f"release created: {tag}")

    cache = Cache()
    for f in files:
        cache.set(tag, f.name, sha256_of(f))
    cache.save()

    print(f"  {C.DIM}{gh.web_url(tag)}{C.RST}")
    return 0


def _upload(tag: str, files: list[Path], gh: Gh, cfg: Config) -> int:
    if not files:
        warn("no files to upload")
        return 0

    step(f"Uploading to {tag}")
    for f in files:
        print(f"  {human_size(file_size(f)):>10}  {f.name}")

    gh.upload(tag, files)

    cache = Cache()
    for f in files:
        cache.set(tag, f.name, sha256_of(f))
    cache.save()

    ok(f"uploaded {len(files)} file(s)")
    return 0


def cmd_add(args) -> int:
    cfg = Config.load()
    tag = cfg.tag(args.tag)
    gh = Gh()
    if not gh.exists(tag):
        die(f"release '{tag}' not found; use 'new' to create it")
    return _upload(tag, resolve_files(args.files), gh, cfg)


def cmd_rm(args) -> int:
    tag = Config.load().tag(args.tag)
    gh = Gh()
    if not gh.exists(tag):
        die(f"release '{tag}' not found")

    assets = {a.name: a for a in gh.assets(tag)}
    to_remove: list[str] = []
    for name in args.files:
        base = Path(name).name
        if base in assets:
            to_remove.append(base)
        else:
            warn(f"not found in release: {name}")

    if not to_remove:
        return 1

    if not args.yes:
        step("will remove")
        for n in to_remove:
            print(f"  {human_size(assets[n].size):>10}  {n}")
        if not confirm("Continue?"):
            return 1

    cache = Cache()
    for n in to_remove:
        gh.delete_asset(tag, n)
        cache.forget(tag, n)
        ok(f"removed {n}")
    cache.save()
    return 0


def cmd_delete(args) -> int:
    tag = Config.load().tag(args.tag)
    gh = Gh()
    if not gh.exists(tag):
        die(f"release '{tag}' not found")
    if not args.yes and not confirm(f"Delete release {tag} and all its files?"):
        return 1
    gh.delete_release(tag)
    cache = Cache()
    cache.drop_tag(tag)
    cache.save()

    if not args.keep_meta:
        m = Manifest()
        if m.remove(tag):
            m.save()
            info(f"removed metadata for {tag}")

    ok(f"deleted release {tag}")
    return 0


def cmd_url(args) -> int:
    tag = Config.load().tag(args.tag)
    gh = Gh()
    print(gh.download_url(tag, args.filename))
    return 0


def cmd_open(args) -> int:
    tag = Config.load().tag(args.tag)
    gh = Gh()
    url = gh.web_url(tag)
    info(f"opening {url}")
    opener = {"darwin": "open", "win32": "start", "linux": "xdg-open"}.get(
        sys.platform, "xdg-open"
    )
    subprocess.run([opener, url], check=False)
    return 0


def cmd_sync(args) -> int:
    cfg = Config.load()
    tag = cfg.tag(args.tag)
    validate_tag(tag)

    src = Path(args.dir).expanduser().resolve()
    local = dir_files(src)
    if not local:
        warn(f"no files in {src}")
        return 0

    gh = Gh()
    if not gh.exists(tag):
        info(f"release {tag} does not exist")
        if args.dry_run:
            step(f"would create release {tag} with {len(local)} file(s)")
            for name, p in sorted(local.items()):
                print(f"  {human_size(file_size(p)):>10}  {name}")
            return 0
        if not confirm("Create it now?"):
            return 1
        files = [p for _, p in sorted(local.items())]

        m = Manifest()
        meta = m.get(tag)
        _collect_meta(args, meta)
        if not meta.title:
            meta.title = tag
        if not meta.date:
            meta.date = time.strftime("%Y-%m-%d")
        m.set(tag, meta)
        m.save()

        gh.create(tag, meta.title, body_from_meta(meta), files, False, False)
        cache = Cache()
        for f in files:
            cache.set(tag, f.name, sha256_of(f))
        cache.save()
        ok(f"created {tag} with {len(files)} file(s)")
        return 0

    remote = {a.name: a for a in gh.assets(tag)}
    cache = Cache()

    to_upload: list[Path] = []
    unchanged: list[str] = []
    changed: list[str] = []

    for name, path in sorted(local.items()):
        if name not in remote:
            to_upload.append(path)
            continue
        prev = cache.get(tag, name)
        cur = sha256_of(path)
        if prev == cur:
            unchanged.append(name)
        else:
            changed.append(name)
            to_upload.append(path)

    only_remote = sorted(set(remote) - set(local))

    step(f"Sync {src} → {tag}")
    print(f"  local:    {len(local)}")
    print(f"  remote:   {len(remote)}")
    print(f"  changed:  {len(changed)}")
    print(f"  new:      {len(to_upload) - len(changed)}")
    print(f"  same:     {len(unchanged)}")
    print()

    if changed:
        step("Changed")
        for n in changed:
            print(f"  {n}")
    if only_remote:
        step("Only in release")
        for n in only_remote:
            print(f"  {n}")
    if to_upload:
        step(f"To upload ({len(to_upload)})")
        for p in to_upload:
            print(f"  {human_size(file_size(p)):>10}  {p.name}")

    if not to_upload:
        ok("nothing to do")
        return 0

    if args.dry_run:
        return 0

    if not args.yes and not confirm(f"Upload {len(to_upload)} file(s)?"):
        return 1

    gh.upload(tag, to_upload)
    for f in to_upload:
        cache.set(tag, f.name, sha256_of(f))
    cache.save()
    ok(f"uploaded {len(to_upload)} file(s)")
    return 0


def cmd_manifest(args) -> int:
    tag = Config.load().tag(args.tag)
    gh = Gh()
    if not gh.exists(tag):
        die(f"release '{tag}' not found")
    assets = gh.assets(tag)
    if not assets:
        warn("no files")
        return 0

    lines = [f"## Files — {tag}", ""]
    for a in sorted(assets, key=lambda x: x.name):
        url = gh.download_url(tag, a.name)
        lines.append(f"- [{a.name}]({url}) — {human_size(a.size)}")
    out = "\n".join(lines)

    if args.output:
        Path(args.output).write_text(out + "\n", encoding="utf-8")
        ok(f"wrote {args.output}")
    else:
        print(out)
    return 0


def cmd_prune(args) -> int:
    gh = Gh()
    releases = gh.releases()
    if not releases:
        warn("no releases")
        return 0

    now = time.time()
    cutoff = now - args.days * 86400 if args.days else None
    pat = re.compile(args.match) if args.match else None

    candidates = []
    for r in releases:
        tag = r["tagName"]
        if pat and not pat.search(tag):
            continue
        if cutoff is not None:
            pub = r.get("publishedAt") or ""
            try:
                ts = time.mktime(time.strptime(pub[:19], "%Y-%m-%dT%H:%M:%S"))
            except (ValueError, TypeError):
                continue
            if ts >= cutoff:
                continue
        candidates.append(r)

    if not candidates:
        ok("nothing to prune")
        return 0

    step(f"Would delete {len(candidates)} release(s)")
    for r in candidates:
        tag = r["tagName"]
        date = (r.get("publishedAt") or "")[:10]
        n = len(r.get("assets") or [])
        total = sum(a.get("size", 0) for a in (r.get("assets") or []))
        print(f"  {tag}  {date}  {n} file(s)  {human_size(total)}")
    print()

    if args.dry_run:
        return 0
    if not args.yes and not confirm("Delete these releases?"):
        return 1

    cache = Cache()
    m = Manifest()
    for r in candidates:
        tag = r["tagName"]
        gh.delete_release(tag)
        cache.drop_tag(tag)
        m.remove(tag)
        ok(f"deleted {tag}")
    cache.save()
    m.save()
    return 0


def cmd_backup(args) -> int:
    gh = Gh()
    releases = gh.releases()
    if not releases:
        warn("no releases")
        return 0

    out_root = Path(args.dir).expanduser().resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    total_files = 0
    total_bytes = 0
    for r in releases:
        tag = r["tagName"]
        assets = gh.assets(tag)
        if not assets:
            continue
        dest = out_root / tag
        dest.mkdir(exist_ok=True)
        step(f"{tag}  ({len(assets)} file(s))")
        for a in assets:
            target = dest / a.name
            if target.exists() and not args.force:
                print(f"  {C.DIM}skip{C.RST}  {a.name}")
                continue
            print(f"  {human_size(a.size):>10}  {a.name}")
            gh.download(tag, a.name, dest, clobber=True)
            total_files += 1
            total_bytes += a.size

    # Also save manifest snapshot
    if args.with_meta:
        m = Manifest()
        snapshot = out_root / "manifest.json"
        snapshot.write_text(
            json.dumps(
                {k: v.to_dict() for k, v in m.data.items()},
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        info(f"wrote {snapshot}")

    ok(f"backed up {total_files} file(s), {human_size(total_bytes)} → {out_root}")
    return 0


def cmd_link_check(args) -> int:
    cfg = Config.load()
    content_dir = Path(cfg.content_dir)
    hits = find_release_links(content_dir)
    if not hits:
        ok("no release links found")
        return 0

    gh = Gh()
    known_tags: dict[str, set[str]] = {}
    for r in gh.releases():
        tag = r["tagName"]
        known_tags[tag] = {a["name"] for a in (r.get("assets") or [])}

    broken = 0
    for md, line, url in hits:
        m = re.match(
            r"https://github\.com/[^/]+/[^/]+/releases/download/([^/]+)/(.+)$", url
        )
        if not m:
            continue
        tag, fname = m.group(1), m.group(2)
        tag = tag.replace("%2F", "/")

        rel = md.relative_to(content_dir)
        if tag not in known_tags:
            print(f"  {C.RED}MISSING TAG{C.RST}  {rel}:{line}")
            print(f"                    {url}")
            broken += 1
            continue
        if fname not in known_tags[tag]:
            print(f"  {C.RED}MISSING FILE{C.RST}  {rel}:{line}")
            print(f"                    {url}")
            broken += 1

    if broken:
        warn(f"{broken} broken link(s)")
        return 1
    ok(f"{len(hits)} link(s) OK")
    return 0


def cmd_export(args) -> int:
    gh = Gh()
    releases = gh.releases()
    if not releases:
        warn("no releases")
        return 0

    m = Manifest()
    rows = []
    for r in releases:
        tag = r["tagName"]
        meta = m.get(tag)
        for a in r.get("assets") or []:
            rows.append(
                {
                    "tag": tag,
                    "title": meta.title or r.get("name") or "",
                    "category": meta.category,
                    "version": meta.version,
                    "status": meta.status,
                    "author": meta.author,
                    "date": meta.date or (r.get("publishedAt") or "")[:10],
                    "tags": ",".join(meta.tags),
                    "file": a.get("name", ""),
                    "size": a.get("size", 0),
                    "url": gh.download_url(tag, a.get("name", "")),
                }
            )

    fmt = args.format.lower()
    if fmt == "json":
        text = json.dumps(rows, indent=2, ensure_ascii=False)
    elif fmt == "csv":
        import io

        s = io.StringIO()
        if rows:
            w = csv.DictWriter(s, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        text = s.getvalue()
    else:
        die(f"unknown format: {fmt}")

    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
        ok(f"wrote {args.output}  ({len(rows)} rows)")
    else:
        print(text)
    return 0


def cmd_stats(args) -> int:
    gh = Gh()
    releases = gh.releases()
    if not releases:
        warn("no releases")
        return 0

    total_files = 0
    total_bytes = 0
    oldest = None
    newest = None

    for r in releases:
        n = len(r.get("assets") or [])
        sz = sum(a.get("size", 0) for a in (r.get("assets") or []))
        total_files += n
        total_bytes += sz
        d = (r.get("publishedAt") or "")[:10]
        if d:
            oldest = d if oldest is None or d < oldest else oldest
            newest = d if newest is None or d > newest else newest

    step("Release stats")
    print(f"  releases:     {len(releases)}")
    print(f"  files:        {total_files}")
    print(f"  total size:   {human_size(total_bytes)}")
    if oldest:
        print(f"  oldest:       {oldest}")
        print(f"  newest:       {newest}")
    print()

    by_tag = sorted(
        (
            (sum(a.get("size", 0) for a in (r.get("assets") or [])), r["tagName"])
            for r in releases
        ),
        reverse=True,
    )
    step("Top releases by size")
    for sz, tag in by_tag[:10]:
        print(f"  {human_size(sz):>10}  {tag}")
    return 0


# ---------- metadata commands ----------


def cmd_meta(args) -> int:
    tag = Config.load().tag(args.tag)
    m = Manifest()
    meta = m.get(tag)

    if meta.is_empty():
        warn(f"no metadata for '{tag}'")
        return 0

    if args.json:
        print(json.dumps(meta.to_dict(), indent=2, ensure_ascii=False))
        return 0

    step(f"Metadata — {tag}")
    fields = [
        ("title", meta.title),
        ("summary", meta.summary),
        ("category", meta.category),
        ("author", meta.author),
        ("date", meta.date),
        ("version", meta.version),
        ("status", meta.status),
        ("license", meta.license),
        ("homepage", meta.homepage),
    ]
    for k, v in fields:
        print(f"  {k + ':':<10} {v or C.DIM + '(empty)' + C.RST}")
    if meta.tags:
        print(f"  {'tags:':<10} {', '.join(meta.tags)}")
    if meta.body:
        print()
        step("Body")
        print(meta.body)
    return 0


def cmd_meta_set(args) -> int:
    tag = Config.load().tag(args.tag)
    m = Manifest()
    meta = m.get(tag)
    parse_set_args(args.set, meta)
    m.set(tag, meta)
    m.save()
    ok(f"updated metadata for {tag}")
    return 0


def cmd_meta_edit(args) -> int:
    tag = Config.load().tag(args.tag)
    m = Manifest()
    meta = m.get(tag)

    editor = os.environ.get("EDITOR") or os.environ.get("VISUAL") or "vi"

    with tempfile.NamedTemporaryFile(
        "w+", suffix=".json", delete=False, encoding="utf-8"
    ) as f:
        json.dump(meta.to_dict(), f, indent=2, ensure_ascii=False)
        tmp = f.name

    try:
        subprocess.run([editor, tmp], check=True)
        raw = json.loads(Path(tmp).read_text(encoding="utf-8"))
        m.set(tag, ReleaseMeta.from_dict(raw))
        m.save()
        ok(f"updated metadata for {tag}")
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        die(f"edit failed: {e}")
    finally:
        Path(tmp).unlink(missing_ok=True)
    return 0


def cmd_meta_rm(args) -> int:
    tag = Config.load().tag(args.tag)
    m = Manifest()
    if not args.yes and not confirm(f"Remove metadata for {tag}?"):
        return 1
    if m.remove(tag):
        m.save()
        ok(f"removed metadata for {tag}")
    else:
        warn(f"no metadata for {tag}")
    return 0


def cmd_edit(args) -> int:
    """Push current metadata to the GitHub release (title + body)."""
    tag = Config.load().tag(args.tag)
    gh = Gh()
    if not gh.exists(tag):
        die(f"release '{tag}' not found")

    m = Manifest()
    meta = m.get(tag)
    _collect_meta(args, meta)

    title = meta.title or args.title or tag
    body = body_from_meta(meta)

    if args.dry_run:
        step("would update release")
        print(f"  tag:    {tag}")
        print(f"  title:  {title}")
        print()
        step("body preview")
        print(body)
        return 0

    m.set(tag, meta)
    m.save()

    gh.edit(tag, title=title, notes=body)
    ok(f"updated release {tag}")
    return 0


# ============================================================
#  CLI
# ============================================================


def _add_meta_flags(sp: argparse.ArgumentParser) -> None:
    sp.add_argument("--title")
    sp.add_argument("--summary")
    sp.add_argument("--body")
    sp.add_argument("--body-file", dest="body_file")
    sp.add_argument("--category")
    sp.add_argument("--tags", help="comma-separated")
    sp.add_argument("--author")
    sp.add_argument("--version")
    sp.add_argument("--status", choices=["draft", "stable", "deprecated"])
    sp.add_argument("--license")
    sp.add_argument("--homepage")
    sp.add_argument("--date", help="YYYY-MM-DD")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="docrel",
        description="Manage document releases on GitHub without bloating git history.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  docrel init
  docrel check
  docrel new rpl106-2026-ganjil \\
      --title "RPL106 — Materi Ganjil 2026/2027" \\
      --category course --author mroczect --version 1.0 \\
      --tags rpl106,database,2026 \\
      static/files/rpl106/rps.pdf
  docrel meta-set rpl106-2026-ganjil summary="RPS + modul praktikum"
  docrel meta-edit rpl106-2026-ganjil
  docrel edit rpl106-2026-ganjil
  docrel sync rpl106-2026-ganjil --dir static/files/rpl106
  docrel link-check
""",
    )
    p.add_argument("--version", action="version", version=f"docrel {VERSION}")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name: str, **kw):
        sp = sub.add_parser(name, **kw)
        sp.set_defaults(func=globals()[f"cmd_{name.replace('-', '_')}"])
        return sp

    sp = add("init", help="create or update .docrel.json")
    sp.add_argument("--large-mb", type=int, dest="large_mb")
    sp.add_argument("--files-dir")
    sp.add_argument("--content-dir")
    sp.add_argument("--prefix")
    sp.add_argument("--parallel", type=int)

    sp = add("check", help="scan repo for large files, junk, cache, manifest")
    sp.add_argument("-t", "--threshold", type=int)

    add("status", help="show config and releases")

    sp = add("list", help="list files in a release")
    sp.add_argument("tag")
    sp.add_argument("-u", "--urls", action="store_true")

    sp = add("new", help="create a new release (with metadata)")
    sp.add_argument("tag")
    _add_meta_flags(sp)
    sp.add_argument("--draft", action="store_true")
    sp.add_argument("--prerelease", action="store_true")
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--force", action="store_true")
    sp.add_argument("files", nargs="*")

    sp = add("add", help="upload files to an existing release")
    sp.add_argument("tag")
    sp.add_argument("files", nargs="+")

    sp = add("rm", help="remove files from a release")
    sp.add_argument("tag")
    sp.add_argument("files", nargs="+")
    sp.add_argument("-y", "--yes", action="store_true")

    sp = add("delete", help="delete an entire release")
    sp.add_argument("tag")
    sp.add_argument("-y", "--yes", action="store_true")
    sp.add_argument("--keep-meta", action="store_true")

    sp = add("url", help="print download URL")
    sp.add_argument("tag")
    sp.add_argument("filename")

    sp = add("open", help="open release in browser")
    sp.add_argument("tag")

    sp = add("sync", help="sync a local dir to a release (hash-based)")
    sp.add_argument("tag")
    sp.add_argument("--dir", required=True)
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("-y", "--yes", action="store_true")
    _add_meta_flags(sp)

    sp = add("manifest", help="print markdown list of files in a release")
    sp.add_argument("tag")
    sp.add_argument("-o", "--output")

    sp = add("prune", help="delete old releases by age or pattern")
    sp.add_argument("--days", type=int, default=0)
    sp.add_argument("--match", default="")
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("-y", "--yes", action="store_true")

    sp = add("backup", help="download all release assets into a directory")
    sp.add_argument("--dir", default="backup/releases")
    sp.add_argument("--force", action="store_true")
    sp.add_argument("--with-meta", action="store_true")

    add("link-check", help="verify release URLs in content/**/*.md")

    sp = add("export", help="export release inventory")
    sp.add_argument("--format", choices=["json", "csv"], default="json")
    sp.add_argument("-o", "--output")

    add("stats", help="summary across all releases")

    # metadata commands
    sp = add("meta", help="show metadata for a release")
    sp.add_argument("tag")
    sp.add_argument("--json", action="store_true")

    sp = add("meta-set", help="set metadata fields (KEY=VALUE ...)")
    sp.add_argument("tag")
    sp.add_argument("set", nargs="+")

    sp = add("meta-edit", help="edit metadata in $EDITOR (JSON)")
    sp.add_argument("tag")

    sp = add("meta-rm", help="remove metadata for a release")
    sp.add_argument("tag")
    sp.add_argument("-y", "--yes", action="store_true")

    sp = add("edit", help="push metadata to GitHub release (title + body)")
    sp.add_argument("tag")
    _add_meta_flags(sp)
    sp.add_argument("--dry-run", action="store_true")

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        print()
        return 130


if __name__ == "__main__":
    sys.exit(main())
```

SHA256: `5f3751870c783d4ae2df5f989d33ab09f152951c1028cd6cb38d88d1aa1ebd64`

### gen_changelog.py
```
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
```

SHA256: `49211827a249312f789a5d5846189c77432e04934b92d3ca7d9f7fa232ecfeb2`

