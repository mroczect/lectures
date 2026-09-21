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
