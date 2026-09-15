---
title: D2 Full Cheat Sheet
description: Cheat sheet lengkap D2 (Declarative Diagramming) — dari hello world, shape, koneksi, container, sampai sequence diagram, SQL table, dan CLI reference.
date: 2026-09-15
tags: [tools, diagram, d2, cheatsheet]
outline: deep
---

# D2 Full Cheat Sheet

> **D2 (Declarative Diagramming)** — bahasa scripting untuk bikin diagram dari teks. Lo tulis teks, dia generate diagram. Gak perlu drag-and-drop.

---

## Daftar Isi

1. [Hello World](#1-hello-world)
2. [Shapes (Bentuk)](#2-shapes-bentuk)
3. [Connections (Koneksi)](#3-connections-koneksi)
4. [Containers (Wadah)](#4-containers-wadah)
5. [Strings & Comments](#5-strings--comments)
6. [Text & Code](#6-text--code)
7. [Icons & Images](#7-icons--images)
8. [Styles](#8-styles)
9. [Classes](#9-classes)
10. [Globs](#10-globs)
11. [Vars (Variabel)](#11-vars-variabel)
12. [Imports](#12-imports)
13. [Composition (Layers/Scenarios/Steps)](#13-composition-layersscenariossteps)
14. [Grid Diagrams](#14-grid-diagrams)
15. [Sequence Diagrams](#15-sequence-diagrams)
16. [SQL Tables](#16-sql-tables)
17. [UML Classes](#17-uml-classes)
18. [Interactive (Tooltip & Link)](#18-interactive-tooltip--link)
19. [Positions (Near)](#19-positions-near)
20. [Overrides & Null](#20-overrides--null)
21. [Layouts](#21-layouts)
22. [Themes](#22-themes)
23. [Exports](#23-exports)
24. [CLI Reference](#24-cli-reference)
25. [Troubleshooting](#25-troubleshooting)

---

## 1. Hello World

```text
x -> y: hello world
```

**Penjelasan:**

- `x` dan `y` = dua shape yang otomatis dibuat
- `->` = koneksi (arrow)
- `hello world` = label koneksi

Install & run:

```bash
# Install
curl -fsSL https://d2lang.com/install.sh | sh -s --

# Render
d2 input.d2 output.svg

# Watch mode (auto-reload)
d2 -w input.d2 output.svg
```

---

## 2. Shapes (Bentuk)

### Deklarasi dasar

```text
imAShape
im_a_shape
im a shape
i'm a shape
a-shape
```

Semua di atas valid. Key-nya case-insensitive.

### Multiple shape satu baris

```text
SQLite; Cassandra
```

### Label berbeda dari key

```text
pg: PostgreSQL
```

`pg` = key (dipakai buat referensi), `PostgreSQL` = label (yang tampil).

### Katalog shape lengkap

| Shape           | Deskripsi              |
| --------------- | ---------------------- |
| `rectangle`     | Default                |
| `square`        | 1:1 ratio              |
| `page`          | Dokumen                |
| `parallelogram` | Miring                 |
| `document`      | Dokumen dengan lipatan |
| `cylinder`      | Database               |
| `queue`         | Antrian                |
| `package`       | Kotak dengan tab       |
| `step`          | Proses                 |
| `callout`       | Balon percakapan       |
| `stored_data`   | Data tersimpan         |
| `person`        | Orang                  |
| `diamond`       | Decision               |
| `oval`          | Elips                  |
| `circle`        | 1:1 ratio              |
| `hexagon`       | Segi enam              |
| `cloud`         | Cloud                  |
| `c4-person`     | Person ala C4          |

### Contoh penggunaan

```text
Cloud: my cloud
Cloud.shape: cloud

DB: PostgreSQL
DB.shape: cylinder

User: User
User.shape: person
```

### 1:1 Ratio shapes

`circle` dan `square` selalu punya lebar = tinggi. Kalau label panjang, otomatis membesar.

```text
Circle1: Ini label panjang banget
Circle1.shape: circle
```

---

## 3. Connections (Koneksi)

### 4 tipe koneksi

```text
a -- b    # garis biasa
a -> b    # arrow ke b
a <- b    # arrow ke a
a <-> b   # dua arah
```

### Label koneksi

```text
Read Replica -- Read Replica 2: Kept in sync
```

### Koneksi HARUS pakai key, bukan label

```text
be: Backend
fe: Frontend

#  Ini bikin shape baru!
Backend -> Frontend

#  Ini pakai shape yang udah ada
be -> fe
```

### Chaining (rantai koneksi)

```text
High Mem -> EC2 <- High CPU: Hosted By
```

Label berlaku untuk semua koneksi dalam rantai.

### Cycle OK

```text
Stage One -> Stage Two -> Stage Three
Stage Three -> Stage One: repeat
```

### Koneksi berulang = koneksi baru

```text
Database -> S3: backup
Database -> S3: realtime
```

Dua-duanya tampil, bukan overwrite.

### Arrowheads

```text
a -> b: To err is human {
  source-arrowhead: 1
  target-arrowhead: * {
    shape: diamond
  }
}
```

**Opsi shape arrowhead:**

| Shape                          | Catatan                   |
| ------------------------------ | ------------------------- |
| `triangle`                     | Default                   |
| `arrow`                        | Lebih lancip              |
| `diamond`                      | Bisa `style.filled: true` |
| `circle`                       | Bisa `style.filled: true` |
| `box`                          | Bisa `style.filled: true` |
| `cf-one` / `cf-one-required`   | Crow's foot               |
| `cf-many` / `cf-many-required` | Crow's foot               |
| `cross`                        | Silang                    |

### Referensi koneksi (by index)

```text
x -> y: hi
x -> y: hello

(x -> y)[0].style.stroke: red
(x -> y)[1].style.stroke: blue
```

---

## 4. Containers (Wadah)

### Container dasar

```text
server.process
```

`process` ada di dalam `server`.

### Deklarasi satu baris

```text
im a parent.im a child
```

### Nested syntax (lebih rapi)

```text
clouds: {
  aws: {
    load_balancer -> api
    api -> db
  }
  gcloud: {
    auth -> db
  }
  gcloud -> aws
}
```

### Container label

```text
# Shorthand
gcloud: Google Cloud {
  ...
}

# Pakai keyword label
gcloud: {
  label: Google Cloud
  ...
}
```

### Reference parent (underscore)

```text
christmas: {
  presents
}
birthdays: {
  presents
  _.christmas.presents -> presents: regift
  _.christmas.style.fill: "#ACE1AF"
}
```

`_` = referensi ke parent scope.

---

## 5. Strings & Comments

### Unquoted strings (default)

```text
Office Bulb: Philips
Switch -> Office Bulb
```

Whitespace di awal/akhir di-trim.

### Quoted strings

```text
"x(int y)": "[]int"
'$dollarbills$'
```

Pakai quote kalau ada karakter reserved.

### Line comments

```text
# Ini komentar
x -> y  # Ini juga komentar
```

### Block comments

```text
x -> y

"""
Ini komentar
multi-baris
"""

y -> z
```

### Block strings (buat code)

```text
my_code: |go
  func main() {
    fmt.Println("hi")
  }
|
```

Kalau code-nya pakai `|`, tambahin pipe:

```text
my_code: ||ts
  const x: number = 1 || 2;
||
```

Atau pakai simbol unik:

```text
my_code: |`ts
  const x = a || b;
`|
```

---

## 6. Text & Code

### Markdown (default untuk standalone text)

```text
md_text: |md
  # Heading
  - **Bold**
  - *Italic*
|
```

### Markdown label di shape

```text
my_shape: |md
  # Title
  Content here
|
my_shape.shape: rectangle
```

### Code block (syntax highlighting)

```text
code: |python
  def hello():
      print("hi")
|
```

**Alias bahasa:**

| Alias | Full         |
| ----- | ------------ |
| `md`  | `markdown`   |
| `tex` | `latex`      |
| `js`  | `javascript` |
| `go`  | `golang`     |
| `py`  | `python`     |
| `rb`  | `ruby`       |
| `ts`  | `typescript` |

### LaTeX

```text
formula: |latex
  \frac{1}{2}
|
```

### Non-Markdown text

```text
plain: Ini teks biasa
plain.shape: text
```

### Multi-byte support

D2 support emoji, Chinese, Japanese, Korean, etc.

```text
hello世界: 你好世界
emoji:
```

---

## 7. Icons & Images

### Icon dasar

```text
my_service: {
  icon: https://icons.d2lang.com/dev%2Fgo.svg
}
```

**Katalog icon gratis:** https://icons.d2lang.com

### Local image

```text
my_shape: {
  icon: ./my_cat.png
}
```

### Image as shape

```text
logo: {
  shape: image
  icon: https://example.com/logo.png
}
```

### Icon placement

Otomatis. Bisa di-override dengan `near`:

```text
x: {
  icon: ./cat.png
  icon.near: top-left
}
```

---

## 8. Styles

Semua style di-set di dalam `style.*`.

### Katalog lengkap

```text
x: {
  style.opacity: 0.5
  style.stroke: red
  style.stroke-width: 3
  style.stroke-dash: 5
  style.fill: "#ACE1AF"
  style.fill-pattern: dots
  style.border-radius: 10
  style.shadow: true
  style.3d: true
  style.multiple: true
  style.double-border: true
  style.font: mono
  style.font-size: 20
  style.font-color: white
  style.bold: true
  style.italic: true
  style.underline: true
  style.animated: true
  style.text-transform: uppercase
}
```

### Detail tiap style

| Style                       | Value                                     | Catatan                         |
| --------------------------- | ----------------------------------------- | ------------------------------- |
| `opacity`                   | 0–1                                       | Transparansi                    |
| `stroke`                    | CSS color / hex                           | Warna garis                     |
| `stroke-width`              | 1–15                                      | Ketebalan garis                 |
| `stroke-dash`               | 0–10                                      | Garis putus-putus               |
| `fill`                      | CSS color / hex                           | Warna isi                       |
| `fill-pattern`              | `dots`, `lines`, `grain`, `none`          | Pola isi                        |
| `border-radius`             | 0–20                                      | Sudut melengkung                |
| `shadow`                    | true/false                                | Bayangan                        |
| `3d`                        | true/false                                | Efek 3D (rectangle/square only) |
| `multiple`                  | true/false                                | Tumpukan                        |
| `double-border`             | true/false                                | Border ganda                    |
| `font`                      | `mono`                                    | Font monospace                  |
| `font-size`                 | 8–100                                     | Ukuran font                     |
| `font-color`                | CSS color / hex                           | Warna font                      |
| `animated`                  | true/false                                | Animasi garis                   |
| `bold`/`italic`/`underline` | true/false                                | Text decoration                 |
| `text-transform`            | `uppercase`, `lowercase`, `title`, `none` | Ubah case                       |

### Style untuk connections

```text
a -> b: {
  style.stroke: red
  style.stroke-dash: 3
  style.animated: true
  style.bold: true
}
```

### Root style (diagram background)

```text
style.fill: "#F6F9FC"
style.stroke: "#CBD6E0"
style.stroke-width: 2
style.double-border: true
```

### Gradient

```text
x.style.fill: "linear-gradient(red, blue)"
```

---

## 9. Classes

Classes = kumpulan style yang bisa di-reuse.

### Deklarasi

```text
classes: {
  base: {
    style: {
      bold: true
      font-size: 20
    }
  }
  error: {
    style.fill: "#e07d7d"
    style.stroke: "#a60c0c"
  }
  success: {
    style.fill: "#86f499"
    style.stroke: "#017f07"
  }
}
```

### Aplikasi ke shape

```text
server-1.class: base
server-2.class: [base; error]
server-3.class: [base; success]
```

### Class ke connection

```text
a -> b: {class: something}
```

### Override class

Shape bisa override attribute dari class:

```text
classes: {
  base: {
    style.fill: blue
  }
}

x.class: base
x.style.fill: red  # override jadi merah
```

### Multiple classes

```text
x.class: [base; error]
```

Diapply kiri ke kanan.

### Classes sebagai tag

Class akan muncul di SVG sebagai CSS class. Berguna buat post-processing.

---

## 10. Globs

Globs = operasi global untuk semua shape/connection.

### Basic glob

```text
*.style.fill: aquamarine

x
y
z
```

Semua shape jadi aquamarine.

### Glob berlaku backward & forward

```text
a
*.style.fill: red  # apply ke a
b                   # apply ke b juga
c                   # apply ke c juga
```

### Case-insensitive

```text
X
*.style.fill: red  # apply ke X juga
```

### Multiple globs

```text
*.style.fill: red
*.style.stroke: blue
```

### Glob connections

```text
* -> *: connected
```

Self-connections tidak termasuk.

### Scoped globs

Glob hanya berlaku di scope-nya:

```text
a: {
  *.style.fill: red
  x
  y
}
b: {
  x  # tidak kena
}
```

### Recursive globs (`**`)

```text
**.style.fill: red
```

Apply ke semua descendant.

### Global globs (`***`)

```text
***.style.fill: yellow
```

Apply ke seluruh diagram, termasuk nested layers.

### Filters (`&`)

```text
*: {
  &shape: circle
  style.fill: red
}
```

Filter berdasarkan keyword:

```text
*: {
  &shape: circle
  &connected: true
  &leaf: true
  style.fill: red
}
```

**Special filters:**

- `&connected: true|false`
- `&leaf: true|false`
- `&src.<property>` — filter source connection
- `&dst.<property>` — filter destination
- `&level: N` — filter by nesting level

### Inverse filter (`!&`)

```text
*: {
  !&shape: circle
  style.fill: red
}
```

Semua yang BUKAN circle jadi merah.

### Nested globs

```text
*: {
  &shape: rectangle
  *: {
    &connected: true
    style.fill: red
  }
}
```

---

## 11. Vars (Variabel)

### Deklarasi

```text
vars: {
  color: aquamarine
  size: 20
  d2-config: {
    theme-id: 3
    layout-engine: elk
  }
}

x.style.fill: ${color}
x.style.font-size: ${size}
```

### Nested vars

```text
vars: {
  colors: {
    primary: "#2E7D32"
    secondary: "#66BB6A"
  }
}

x.style.fill: ${colors.primary}
```

### Scoped vars

Vars berlaku di scope-nya dan scope yang lebih dalam:

```text
vars: {color: red}

a: {
  vars: {color: blue}
  x.style.fill: ${color}  # blue
}

y.style.fill: ${color}  # red
```

### Single quotes bypass substitution

```text
vars: {color: red}
x.label: '${color}'  # literal: ${color}
```

### Spread substitutions

```text
vars: {
  shared: {
    style.fill: red
    style.stroke: blue
  }
}

x: {
  ...${shared}
}
```

### Configuration vars

```text
vars: {
  d2-config: {
    theme-id: 3
    layout-engine: elk
    pad: 0
    sketch: true
    center: true
  }
  d2-legend: "Keterangan" {
    # Legend items
  }
}
```

---

## 12. Imports

### Regular import

`x.d2`:

```text
x: {
  shape: circle
}
```

`y.d2`:

```text
a: @x
a -> b
```

### Spread import

`y.d2`:

```text
a: {
  ...@x
}
a -> b
```

### Omit extension

```text
x: @x    #
x: @x.d2 #  (autoformat akan ubah)
```

### Partial import

Ambil objek spesifik dari file:

```text
x: @people.alice
```

### Relative import

```text
x: @../shared/models
```

### Absolute import

```text
x: @/absolute/path/file

# Windows
x: @"C:\path\to\file"
```

### Use case: Model-View

`models.d2`:

```text
user: {shape: person}
order: {shape: rectangle}
```

`view.d2`:

```text
...@models
user -> order
```

---

## 13. Composition (Layers/Scenarios/Steps)

### Layers

Layer = abstraksi berbeda, tidak inherit.

```text
x -> y

layers: {
  physical: {
    server1 -> server2
  }
  logical: {
    service1 -> service2
  }
}
```

### Scenarios

Scenario = view berbeda dari base layer. Inherit dari layer.

```text
x -> y

scenarios: {
  success: {
    x -> y: success
  }
  failure: {
    x -> y: failure
  }
}
```

### Steps

Step = urutan kejadian. Inherit dari step sebelumnya.

```text
step1: {
  a -> b
}
step2: {
  b -> c
}
```

Atau dengan `steps`:

```text
steps: {
  init: {a}
  process: {a -> b}
  done: {b -> c}
}
```

### Linking antar boards

```text
root.link: layers.physical
```

Atau:

```text
x.link: scenarios.success
```

Backlinks (underscore):

```text
layers: {
  next: {
    a.link: _._   # kembali ke root
  }
}
```

---

## 14. Grid Diagrams

### Basic grid

```text
grid-rows: 3
grid-columns: 3

a; b; c
d; e; f
g; h; i
```

### Grid gap

```text
grid-gap: 0
vertical-gap: 10
horizontal-gap: 10
```

### Grid dimensions

```text
my_grid: {
  grid-rows: 2
  grid-columns: 3
  width: 600
  height: 400
  a; b; c
  d; e; f
}
```

### Dominant direction

Keyword yang dideklarasi duluan = dominant direction.

```text
grid-rows: 4
grid-columns: 2
# fill row by row

grid-columns: 2
grid-rows: 4
# fill column by column
```

### Connections antar grid cells

```text
grid: {
  grid-rows: 2
  a -> b
}
```

### Nested grid

```text
outer: {
  grid-rows: 2
  inner: {
    grid-rows: 2
    x; y
    z; w
  }
}
```

### Align dengan invisible elements

```text
grid: {
  grid-columns: 4
  invisible1: {style.opacity: 0}
  a; b
  invisible2: {style.opacity: 0}
}
```

---

## 15. Sequence Diagrams

### Basic

```text
shape: sequence_diagram

alice -> bob: Hello
bob -> alice: Hi
```

### Actors

```text
shape: sequence_diagram

alice; bob; charlie  # deklarasi urutan

charlie -> alice: msg
```

### Order matters

Urutan deklarasi = urutan tampil.

### Spans

```text
shape: sequence_diagram

alice
bob

alice -> bob: start
alice.t1 -> bob: request
alice.t1 <- bob: response
alice -> bob: end
```

### Groups

```text
shape: sequence_diagram

alice; bob

group1: {
  alice -> bob: msg1
  bob -> alice: msg2
}
```

### Notes

```text
shape: sequence_diagram

alice; bob

alice.note: |md
  Ini catatan
|
alice -> bob: msg
```

### Self-messages

```text
shape: sequence_diagram

alice
alice -> alice: thinking
```

### Customization

```text
shape: sequence_diagram

alice -> bob: {
  style.stroke: red
  style.stroke-dash: 3
}
```

### Lifeline inherit actor style

```text
shape: sequence_diagram

alice: {
  style.stroke: red
  style.stroke-dash: 5
}
alice -> bob: msg
```

---

## 16. SQL Tables

### Basic

```text
users: {
  shape: sql_table
  id: int {constraint: primary_key}
  name: varchar
  email: varchar {constraint: unique}
}
```

### Constraints

| Constraint    | Short |
| ------------- | ----- |
| `primary_key` | `PK`  |
| `foreign_key` | `FK`  |
| `unique`      | `UNQ` |

Multiple constraints:

```text
id: int {constraint: [primary_key; unique]}
```

### Foreign key connection

```text
users: {
  shape: sql_table
  id: int {constraint: primary_key}
}

orders: {
  shape: sql_table
  user_id: int {constraint: foreign_key}
}

orders.user_id -> users.id
```

### Nested in container

```text
db: {
  users: {
    shape: sql_table
    id: int {constraint: primary_key}
  }
  orders: {
    shape: sql_table
    user_id: int
  }
}
```

### Escape reserved keyword

```text
my_table: {
  shape: sql_table
  "label": string
}
```

---

## 17. UML Classes

### Basic

```text
my_class: {
  shape: class
  field1: int
  field2: string
  method1(): void
  method2(x: int): bool
}
```

### Visibility

| Prefix | Arti      |
| ------ | --------- |
| (none) | public    |
| `+`    | public    |
| `-`    | private   |
| `#`    | protected |

```text
my_class: {
  shape: class
  +public_field: int
  -private_field: string
  #protected_field: bool
  +getData(): void
}
```

### Escape reserved keyword

```text
my_class: {
  shape: class
  "class": string
}
```

---

## 18. Interactive (Tooltip & Link)

### Tooltip

```text
x: {
  tooltip: "Ini tooltip"
}
```

Muncul saat hover. Di PNG export, muncul di appendix.

### Link

```text
x: {
  link: https://example.com
}
```

Klik untuk buka URL.

### Link ke board lain

```text
x.link: layers.physical
```

### URL schemes

Support `http`, `https`, `mailto`, `vscode://`, dll.

### Tooltip always visible

```text
x: {
  tooltip: "Selalu tampil"
  tooltip.near: top-center
}
```

---

## 19. Positions (Near)

### Constant values

```text
title: |md
  # Diagram Title
| {
  near: top-center
}
```

**Nilai yang valid:**

- `top-left`, `top-center`, `top-right`
- `center-left`, `center-right`
- `bottom-left`, `bottom-center`, `bottom-right`

### Near container

```text
legend: {
  near: bottom-right
  a; b; c
}
```

### Label positioning

```text
x: {
  near: top-center
  label.near: outside-top-center
}
```

**Prefix:**

- `outside-` — di luar bounding box
- `border-x` — di border

### Icon positioning

```text
x: {
  icon: ./cat.png
  icon.near: top-left
}
```

### Near object (TALA only)

```text
vars: {
  d2-config: {
    layout-engine: tala
  }
}

aws: {...}
gcloud: {...}

text: |md
  # Notes
| {
  near: aws
}
```

### Top & Left (TALA only)

```text
x: {
  top: 100
  left: 100
}
```

Lock position di TALA.

---

## 20. Overrides & Null

### Merge on redeclare

```text
x: {style.fill: red}
x: {style.stroke: blue}

# Hasil: x punya fill red DAN stroke blue
```

### Null keyword

```text
x: {style.fill: red}
x: null  # hapus x
```

### Null connection

```text
a -> b
(a -> b)[0]: null
```

### Null attribute

```text
x: {style.fill: red}
x.style.fill: null
```

### Implicit nulls

Null shape dengan koneksi → koneksinya juga hilang.

```text
a -> b
a: null  # connection a->b juga hilang
```

Null parent → semua children hilang.

```text
parent: {
  child1
  child2
}
parent: null  # child1, child2 hilang
```

---

## 21. Layouts

### 3 layout engines

| Engine  | Karakteristik                                               |
| ------- | ----------------------------------------------------------- |
| `dagre` | Default, cepat, hierarchical                                |
| `elk`   | Lebih mature, orthogonal routes, bagus untuk container      |
| `tala`  | Baru, untuk software architecture, support `near` ke object |

### Set layout

```bash
d2 --layout=elk input.d2 output.svg
d2 -l dagre input.d2
D2_LAYOUT=elk d2 input.d2
```

Atau di code:

```text
vars: {
  d2-config: {
    layout-engine: elk
  }
}
```

### Direction

```text
direction: right

a -> b -> c
```

Opsi: `up`, `down`, `right`, `left`

### Direction per container (TALA only)

```text
vars: {d2-config: {layout-engine: tala}}
direction: down

a -> b -> c

b: {
  direction: right
  1 -> 2 -> 3
}
```

### ELK algorithms

```bash
d2 --layout=elk --elk-algorithm=layered input.d2
d2 --layout=elk --elk-algorithm=force input.d2
d2 --layout=elk --elk-algorithm=stress input.d2
d2 --layout=elk --elk-algorithm=mrtree input.d2
d2 --layout=elk --elk-algorithm=radial input.d2
```

---

## 22. Themes

### Set theme

```bash
d2 -t 101 input.d2
d2 --theme=300 input.d2
D2_THEME=101 d2 input.d2
```

Atau di code:

```text
vars: {
  d2-config: {
    theme-id: 3
  }
}
```

### Dark theme

```bash
d2 --dark-theme 200 input.d2
```

### List themes

```bash
d2 themes
```

### Special themes

- `Terminal`
- `Terminal Grayscale`
- `Origami`

Contoh Terminal theme: caps lock on, no border radius, monospace, fill-pattern dots, double-border.

### Custom theme

```text
vars: {
  d2-config: {
    theme-overrides: {
      B1: "#2E7D32"
      B2: "#66BB6A"
      B3: "#A5D6A7"
    }
  }
}
```

---

## 23. Exports

### Format yang didukung

| Format | Command             | Catatan          |
| ------ | ------------------- | ---------------- |
| SVG    | `d2 in.d2 out.svg`  | Default          |
| PNG    | `d2 in.d2 out.png`  | No dependencies  |
| PDF    | `d2 in.d2 out.pdf`  | Multi-page       |
| PPTX   | `d2 in.d2 out.pptx` | Untuk presentasi |
| GIF    | `d2 in.d2 out.gif`  | Untuk animasi    |
| ASCII  | `d2 in.d2 out.txt`  | Text art (beta)  |
| Stdout | `d2 - -`            | Default SVG      |

### Examples

```bash
# SVG
d2 input.d2 output.svg

# PNG
d2 input.d2 output.png

# PDF
d2 input.d2 output.pdf

# PPTX
d2 input.d2 output.pptx

# GIF dengan animasi
d2 --animate-interval=1000 input.d2 output.gif

# ASCII (extended)
d2 input.d2 output.txt

# ASCII (standard)
d2 --ascii-mode standard input.d2 output.txt

# Stdout
echo "x -> y" | d2 - -

# PNG ke stdout
echo "x -> y" | d2 --stdout-format=png - - > out.png
```

### Multi-board exports

- **Multiple SVGs**: output ke folder
- **Animated SVG**: `--animate-interval=N` (ms)
- **GIF**: animated
- **PDF**: multi-page
- **PPTX**: untuk presentasi

### Force appendix

```bash
d2 --force-appendix input.d2 out.svg
```

Tambah appendix untuk tooltip/link di SVG.

---

## 24. CLI Reference

### Basic commands

```bash
d2 input.d2                    # → input.svg
d2 input.d2 output.svg         # → output.svg
d2 input.d2 output.png         # → output.png
d2 - -                         # stdin → stdout (SVG)
d2 -w input.d2 output.svg      # watch mode
```

### Subcommands

```bash
d2 layout              # list layout engines
d2 layout dagre        # detail dagre
d2 themes              # list themes
d2 fmt input.d2        # format
d2 fmt --check input.d2 # cek format
d2 play input.d2       # buka di playground
d2 validate input.d2   # validasi
```

### Flags lengkap

```
-w, --watch              watch mode
-h, --host               host untuk watch
-p, --port               port untuk watch
-t, --theme              theme ID
--dark-theme             dark theme ID
-s, --sketch             hand-drawn style
--center                 center SVG
--scale                  scale (default -1 = fit to screen)
--font-regular           custom regular font
--font-italic            custom italic font
--font-bold              custom bold font
--font-semibold          custom semibold font
--font-mono              custom mono font
--font-mono-bold         custom mono bold
--font-mono-italic       custom mono italic
--font-mono-semibold     custom mono semibold
--pad                    padding (default 100)
--animate-interval       interval animasi (ms)
--browser                browser executable (0 = none)
-l, --layout             layout engine
-b, --bundle             bundle assets
--force-appendix         force appendix
--target                 target board
-d, --debug              debug logs
--img-cache              cache images
--timeout                timeout (default 120s)
--check                  check format
--salt                   salt untuk unique IDs
--stdout-format          format untuk stdout
--no-xml-tag             tanpa XML tag
--omit-version           tanpa version
--ascii-mode             mode ASCII
-h, --help               help
-v, --version            version
```

### Environment variables

```
D2_WATCH
D2_LAYOUT
D2_THEME
D2_DARK_THEME
D2_PAD
D2_CENTER
D2_SKETCH
D2_BUNDLE
D2_FORCE_APPENDIX
D2_FONT_REGULAR
D2_FONT_ITALIC
D2_FONT_BOLD
D2_FONT_SEMIBOLD
D2_FONT_MONO
D2_FONT_MONO_BOLD
D2_FONT_MONO_ITALIC
D2_FONT_MONO_SEMIBOLD
D2_ANIMATE_INTERVAL
D2_TIMEOUT
D2_CHECK
D2_ASCII_MODE
DEBUG
IMG_CACHE
HOST
PORT
BROWSER
D2_STDOUT_FORMAT
D2_NO_XML_TAG
OMIT_VERSION
```

---

## 25. Troubleshooting

### Label tidak kecompile

Pakai quote:

```text
"x(int y)": "[]int"
```

### Text kepanjangan

Tambah newline:

```text
x: When you go out to buy,\ndon't show your silver.
```

### Connection berantakan

Set width/height manual:

```text
x: {
  width: 200
  height: 100
}
```

### Reserved keyword jadi key

Quote:

```text
x: {
  "width": width
}
```

### HTML di Markdown bikin error

Pakai HTML semantic:

```text
x: |md
  Text <br/> next line
|
```

### SVG tidak interaktif di HTML

Bukan masalah D2, tapi cara embed. Pakai `<object>` atau `<iframe>`, bukan `<img>`.

### Non-ASCII bikin error

Karakter `：` (Chinese colon) ≠ `:`. Pakai ASCII.

---

## Contoh Diagram Kompleks

### Software architecture

```text
vars: {
  d2-config: {
    layout-engine: elk
    theme-id: 3
  }
}

direction: right

users: Users {shape: person}
web: Web App {shape: rectangle}
api: API Gateway {shape: hexagon}
auth: Auth Service {shape: rectangle}
db: Database {shape: cylinder}
cache: Redis {shape: cylinder}

users -> web: HTTPS
web -> api: REST
api -> auth: gRPC
api -> db: SQL
api -> cache: Redis protocol
auth -> db: SQL
```

### ERD

```text
users: {
  shape: sql_table
  id: int {constraint: primary_key}
  email: varchar {constraint: unique}
  name: varchar
  created_at: timestamp
}

orders: {
  shape: sql_table
  id: int {constraint: primary_key}
  user_id: int {constraint: foreign_key}
  total: decimal
  status: varchar
}

order_items: {
  shape: sql_table
  id: int {constraint: primary_key}
  order_id: int {constraint: foreign_key}
  product_id: int {constraint: foreign_key}
  qty: int
}

products: {
  shape: sql_table
  id: int {constraint: primary_key}
  name: varchar
  price: decimal
}

orders.user_id -> users.id
order_items.order_id -> orders.id
order_items.product_id -> products.id
```

### Sequence diagram

```text
shape: sequence_diagram

client; server; db

client -> server: POST /login
server -> db: SELECT user
db -> server: user data
server -> server: verify password
server -> client: 200 OK + JWT

client -> server: GET /api/products
server -> db: SELECT products
db -> server: products
server -> client: 200 OK
```

### Flowchart

```text
start: Start {shape: circle}
input: Input Data {shape: parallelogram}
process: Process {shape: rectangle}
decision: Valid? {shape: diamond}
output: Output {shape: parallelogram}
end: End {shape: circle}

start -> input
input -> process
process -> decision
decision -> output: Yes
decision -> process: No
output -> end
```

---

## Referensi Cepat

| Konsep        | Sintaks                              |
| ------------- | ------------------------------------ |
| Shape         | `key: Label`                         |
| Shape type    | `key.shape: circle`                  |
| Connection    | `a -> b: label`                      |
| Container     | `parent.child`                       |
| Label         | `key: Label`                         |
| Comment       | `# comment`                          |
| Block comment | `"""..."""`                          |
| Markdown      | `\|md ... \|`                        |
| Code          | `\|python ... \|`                    |
| Icon          | `key.icon: url`                      |
| Style         | `key.style.fill: red`                |
| Class         | `classes: {...}` + `key.class: name` |
| Var           | `vars: {x: value}` + `${x}`          |
| Import        | `x: @file`                           |
| Spread import | `x: {...@file}`                      |
| Glob          | `*.style.fill: red`                  |
| Layer         | `layers: {...}`                      |
| Scenario      | `scenarios: {...}`                   |
| Step          | `steps: {...}`                       |
| Grid          | `grid-rows: N` + `grid-columns: N`   |
| Sequence      | `shape: sequence_diagram`            |
| SQL           | `shape: sql_table`                   |
| UML           | `shape: class`                       |
| Tooltip       | `key.tooltip: text`                  |
| Link          | `key.link: url`                      |
| Near          | `key.near: top-center`               |
| Null          | `key: null`                          |

---

## Link Berguna

- **Docs**: https://d2lang.com/tour/intro
- **Playground**: https://play.d2lang.com
- **Icons**: https://icons.d2lang.com
- **GitHub**: https://github.com/d2lang/d2
- **Discord**: https://discord.gg/NF6X8K4eDq
- **Examples**: https://d2lang.com/examples/overview

---

## Tips Belajar

1. **Mulai dari hello world** — `x -> y`
2. **Coba playground** — https://play.d2lang.com (langsung render)
3. **Bikin diagram yang lo butuh** — bukan contoh abstrak
4. **Baca error message** — D2 kasih pesan yang jelas
5. **Pakai watch mode** — `d2 -w input.d2 out.svg` (auto-reload)
6. **Eksperimen** — gak ada yang rusak, tinggal undo
7. **Lihat examples** — banyak contoh nyata di docs
8. **Autoformat** — `d2 fmt` biar rapi
9. **Mulai dari layout default** — baru ganti kalau perlu
10. **Jangan hafal** — pakai cheat sheet ini sebagai referensi

---

**Selamat belajar D2! **

Kalau ada yang bingung, inget: D2 itu cuma teks. Gak ada yang bisa rusak permanen. Tinggal coba, lihat hasilnya, ulangi.
