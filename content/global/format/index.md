---
title: Format & Aturan
description: Konvensi penulisan, penamaan file, dan panduan kontribusi dokumentasi Lectures.
sidebar_position: 5
---

# Format & Aturan

Acuan penulisan untuk siapa pun yang menambah atau mengedit konten di dokumentasi ini.

Empat prinsip: konsisten, deskriptif, scalable, ramah kontributor. Semua aturan di bawah turun dari situ.

## Penamaan file

Gunakan **kebab-case**, **lowercase**, **deskriptif**.

| Benar              | Salah             |
| ------------------ | ----------------- |
| `kontak-dosen.md`  | `kontakDosen.md`  |
| `jadwal-kuliah.md` | `JadwalKuliah.md` |
| `info-team-pbl.md` | `itp.md`          |

Hindari:

- Spasi (`kontak dosen.md`) — jadi `%20` di URL
- Kapital campur (`JadwalKuliah.md`) — case-sensitive di Linux
- Underscore (`kontak_dosen.md`) — bukan konvensi web
- Singkatan (`jk.md`) — tidak deskriptif
- Karakter unik (`kontak-dosen!.md`) — bisa bermasalah di URL dan Git

## Materi bertimestamp

Untuk file materi (kecuali `index.md`), pakai pola:

```

{YYYY-MM-DD}_{course_id}_{course_name}_{description}.md

```

| Komponen    | Format                  | Contoh                      |
| ----------- | ----------------------- | --------------------------- |
| timestamp   | `YYYY-MM-DD`            | `2026-09-15`                |
| course_id   | kode lowercase          | `rpl101`, `rpl106`, `pk001` |
| course_name | sama dengan nama folder | `pengantar-rpl`             |
| description | kebab-case singkat      | `er-diagram`                |

Contoh:

| Salah                        | Benar                                              |
| ---------------------------- | -------------------------------------------------- |
| `materi-01-pengenalan.md`    | `2026-09-01_rpl101_pengantar-rpl_pengenalan.md`    |
| `materi-02-analisis.md`      | `2026-09-08_rpl101_pengantar-rpl_analisis.md`      |
| `15-09-2026-rpl104-intro.md` | `2026-09-15_rpl104_analisis-kebutuhan-pl_intro.md` |

Timestamp di depan bikin file otomatis urut kronologis saat di-sort — sesuai urutan pertemuan.

**Pengecualian:** `index.md` di setiap folder tidak pakai timestamp. Dia landing page folder.

## Ekstensi

Semua file dokumentasi pakai `.md`. VitePress memproses Markdown secara native dan mendukung **Vue SFC** di dalam `.md` saat perlu komponen interaktif.

`.mdx` **tidak dipakai** — VitePress tidak memakai MDX secara default. Untuk komponen dinamis, gunakan:

- **Vue component** di dalam `.md` langsung (VitePress sudah support)
- **`<script setup>`** di blok `.md`
- **Tema kustom** via `.vitepress/theme/`

Kalau butuh MDX penuh, tambahkan plugin `vite-plugin-mdx` secara manual — tapi untuk proyek ini **tidak disarankan** demi kesederhanaan.

Cek file `.mdx` yang tersisa (kalau migrasi dari Docusaurus):

```bash
find docs -name '*.mdx'
```

Rename massal kalau ada:

```bash
find docs -name '*.mdx' -exec sh -c 'mv "$1" "${1%.mdx}.md"' _ {} \;
```

## Frontmatter

Setiap file wajib punya minimal:

```yaml
---
title: Judul Halaman
description: Deskripsi singkat.
---
```

Field lengkap:

| Field              |   Wajib    | Fungsi                                       |
| ------------------ | :--------: | -------------------------------------------- |
| `title`            |     ✅     | Judul halaman, tampil di tab & TOC           |
| `description`      | disarankan | Untuk SEO dan social preview                 |
| `sidebar_position` | disarankan | Urutan di sidebar, makin kecil makin atas    |
| `outline`          |  opsional  | `deep` untuk TOC 2–3 level (default 2)       |
| `lastUpdated`      |  opsional  | Timestamp update terakhir (auto kalau aktif) |
| `editLink`         |  opsional  | Override link edit di footer                 |
| `prev` / `next`    |  opsional  | Override navigasi halaman                    |

::: tip Slug di VitePress
VitePress **tidak punya** field `slug` seperti Docusaurus. URL ditentukan otomatis dari **path file** relatif terhadap `srcDir`.

Contoh: `docs/v1/courses/rpl106-pengantar-basis-data/er-diagram.md`
→ URL `/v1/courses/rpl106-pengantar-basis-data/er-diagram`

Kalau butuh URL kustom, gunakan **rewrites** di `.vitepress/config.ts`.
:::

**Landing page course:**

```yaml
---
title: RPL106 — Pengantar Basis Data
description: Materi, praktikum, dan referensi mata kuliah RPL106.
sidebar_position: 70
---
```

**Materi bertimestamp** — URL otomatis dari nama file (bersih karena timestamp di depan tapi tetap muncul di URL):

```yaml
---
title: 'Pertemuan 2 — ER Diagram'
description: Pemodelan data konseptual.
sidebar_position: 2
outline: deep
---
```

::: warning Timestamp di URL
Karena VitePress tidak punya `slug`, timestamp akan muncul di URL:

`/v1/courses/rpl106-pengantar-basis-data/2026-09-08_rpl106_pengantar-basis-data_er-diagram`

Kalau tidak mau timestamp di URL, ada dua opsi:

1. **Hapus timestamp** dari nama file, andalkan `sidebar_position` untuk urutan.
2. **Pakai `rewrites`** di `config.ts` untuk mapping path.
   :::

## Struktur folder

```
docs/
├── .vitepress/
│   └── config.ts
├── index.md
├── intro.md
├── global/
│   ├── format/
│   │   └── page.md
│   └── license.md
└── v1/
    ├── index.md
    ├── about.md
    ├── courses/
    │   ├── index.md
    │   ├── rpl101-pengantar-rpl/
    │   │   ├── index.md
    │   │   └── 2026-09-01_pengantar-rpl_pengenalan.md
    │   └── rpl102-algoritma-pemrograman/
    ├── information/
    └── task/
```

Aturan:

- Nama folder = kebab-case
- Setiap folder course punya `index.md`
- Materi disimpan di dalam folder course-nya

Nama folder course: `{kode-lowercase}-{nama-kebab-case}`

| Kode     | Folder                         |
| -------- | ------------------------------ |
| RPL101   | `rpl101-pengantar-rpl`         |
| RPL102   | `rpl102-algoritma-pemrograman` |
| RPL103   | `rpl103-matematika-diskrit`    |
| RPL104   | `rpl104-analisis-kebutuhan-pl` |
| RPL105   | `rpl105-pemrograman-web`       |
| RPL106   | `rpl106-pengantar-basis-data`  |
| PK001RPL | `pk001-pendidikan-agama`       |

## Urutan sidebar

Ada dua cara: **manual via frontmatter** atau **konfigurasi di `config.ts`**.

### Manual — `sidebar_position`

|      Nilai      | Dipakai untuk                       |
| :-------------: | ----------------------------------- |
|        1        | `index.md` (landing page)           |
|       2+        | Materi di dalam folder course       |
| 10, 20, 30, ... | Course dalam kategori, kelipatan 10 |

Course pakai kelipatan 10 supaya mudah menyisipkan course baru tanpa renumber:

```
10  pk001-pendidikan-agama
20  rpl101-pengantar-rpl
30  rpl102-algoritma-pemrograman
40  rpl103-matematika-diskrit
50  rpl104-analisis-kebutuhan-pl
60  rpl105-pemrograman-web
70  rpl106-pengantar-basis-data
```

::: warning `sidebar_position` butuh `generateSidebar`
Secara default VitePress **tidak** membaca `sidebar_position`. Kamu perlu:

- **Plugin eksternal**: [`vitepress-sidebar`](https://github.com/jooy2/vitepress-sidebar)
- **Custom logic** di `.vitepress/config.ts`

Alternatif paling simpel: definisikan sidebar **langsung di `config.ts`** (lihat bawah).
:::

### Via `config.ts` — direkomendasikan

```ts
// .vitepress/config.ts
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Lectures',
  description: 'Dokumentasi Kuliah TRPL — Politeknik Negeri Batam',

  themeConfig: {
    nav: [
      { text: 'Pengantar', link: '/intro' },
      { text: 'V1', link: '/v1/' },
      { text: 'Format', link: '/global/format/page' },
    ],

    sidebar: {
      '/v1/': [
        {
          text: 'Informasi',
          items: [
            { text: 'Tentang', link: '/v1/about' },
            { text: 'Kontak Dosen', link: '/v1/information/kontak-dosen' },
            { text: 'Jadwal Kuliah', link: '/v1/information/jadwal-kuliah' },
            { text: 'Info Tim PBL', link: '/v1/information/info-team-pbl' },
            { text: 'Judul & Tim PBL', link: '/v1/information/judul-dan-team-pbl' },
          ],
        },
        {
          text: 'Mata Kuliah',
          items: [
            { text: 'RPL101 — Pengantar RPL', link: '/v1/courses/rpl101-pengantar-rpl/' },
            { text: 'RPL102 — Algoritma', link: '/v1/courses/rpl102-algoritma-pemrograman/' },
            { text: 'RPL103 — Matdis', link: '/v1/courses/rpl103-matematika-diskrit/' },
            {
              text: 'RPL104 — Analisis Kebutuhan',
              link: '/v1/courses/rpl104-analisis-kebutuhan-pl/',
            },
            { text: 'RPL105 — Pemrograman Web', link: '/v1/courses/rpl105-pemrograman-web/' },
            { text: 'RPL106 — Basis Data', link: '/v1/courses/rpl106-pengantar-basis-data/' },
            { text: 'PK001 — Agama', link: '/v1/courses/pk001-pendidikan-agama/' },
          ],
        },
        {
          text: 'Tugas',
          items: [{ text: 'Daftar Tugas', link: '/v1/task/' }],
        },
      ],
    },

    outline: { level: [2, 3] },
    search: { provider: 'local' },
    lastUpdated: true,
    editLink: {
      pattern: 'https://github.com/mroczect/lectures/edit/main/docs/:path',
      text: 'Edit halaman ini di GitHub',
    },
  },
})
```

## Format konten

Struktur halaman standar: H1 → metadata → konten → halaman terkait. Metadata (kode, SKS, dosen), tagline, dan tip e-learning opsional.

### Tabel

Pakai alignment marker:

```markdown
| Kiri | Tengah | Kanan |
| :--- | :----: | ----: |
| teks |  teks  |   100 |
```

`:---` kiri, `:---:` tengah, `---:` kanan.

### Kode

Selalu pakai language tag:

````markdown
```python
def hello():
    print("hi")
```
````

Language yang sering dipakai: `bash`, `python`, `typescript`, `js`, `vue`, `yaml`, `json`, `md`, `text`.

Fitur bawaan VitePress yang berguna:

**Highlight baris:**

````markdown
```ts{2,5-7}
export default defineConfig({
  title: 'Lectures',      // <- highlighted
  // ...
})
```
````

**Focus & diff:**

````markdown
```ts
export default defineConfig({
  title: 'Lectures',
})
```
````

### Admonition

VitePress pakai **spasi** setelah `:::` (kebalikan Docusaurus):

```markdown
::: info
Ini info.
:::

::: tip
Ini tip.
:::

::: warning
Ini peringatan.
:::

::: danger
Ini bahaya.
:::

::: details Klik untuk lihat
Konten tersembunyi.
:::
```

::: warning Perbedaan dengan Docusaurus

- **VitePress**: `::: tip` (pakai **spasi**)
- **Docusaurus**: `:::tip` (tanpa spasi)

Kalau migrasi dari Docusaurus, semua `:::` perlu ditambah spasi.
:::

### Code group

VitePress punya **code group** bawaan untuk tab multi-bahasa:

````markdown
::: code-group

```bash [npm]
npm install
```

```bash [pnpm]
pnpm install
```

```bash [bun]
bun install
```

:::
````

### Komponen Vue

Karena VitePress memakai Vue 3, komponen bisa langsung dipakai di `.md`:

```markdown
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<MyComponent />
```

Atau inline:

```markdown
<script setup>
const semester = 'Ganjil 2026/2027'
</script>

Semester aktif: **{{ semester }}**
```

## Vue/VitePress gotchas

VitePress lebih toleran dari MDX, tapi tetap ada beberapa hal yang perlu diperhatikan.

**HTML comment — boleh!** (beda dari MDX)

```markdown
<!-- ini valid di VitePress -->
```

**Curly braces** — diproses sebagai Vue expression:

```markdown
Teks dengan {variabel} → error (dianggap ekspresi Vue).
Teks dengan `{variabel}` → aman (dalam backtick).
Teks dengan &#123;variabel&#125; → aman (HTML entity).
```

**Self-closing tag:**

```markdown
<br /> ✅ (aman)
<br> ✅ (VitePress toleran, tapi konsisten pakai />)

<img src="..." /> ✅
```

**`<details>`:**

```markdown
<details>
<summary>Judul</summary>

Konten di sini. Butuh blank line setelah `<summary>`.

</details>
```

Atau pakai cara VitePress:

```markdown
::: details Judul
Konten di sini.
:::
```

**Karakter `<` di teks:**

```markdown
Loading < 2 detik. → dianggap tag HTML, bisa error
Loading `< 2 detik`. → aman
Loading &lt; 2 detik. → aman
```

### Konversi dari Docusaurus

| Docusaurus               | VitePress               |
| ------------------------ | ----------------------- |
| `:::tip`                 | `::: tip`               |
| `:::info`                | `::: info`              |
| `:::warning`             | `::: warning`           |
| `:::danger`              | `::: danger`            |
| `<details><summary>`     | `::: details Judul`     |
| `<Tabs>` + `<TabItem>`   | `::: code-group`        |
| `{/* komentar */}`       | `<!-- komentar -->`     |
| `slug:` di frontmatter   | hapus (pakai path file) |
| `.mdx`                   | `.md`                   |
| `sidebar_position`       | `config.ts` sidebar     |
| `<!-- -->` (tidak valid) | `<!-- -->` (valid!)     |

## Checklist kontribusi

Sebelum commit atau PR:

- [ ] Frontmatter lengkap (`title` minimal, `description` disarankan)
- [ ] Ekstensi `.md`
- [ ] Nama file kebab-case lowercase
- [ ] Materi mengikuti format timestamp
- [ ] `sidebar_position` di-set (atau didaftarkan di `config.ts`)
- [ ] Tidak ada `{` atau `}` literal di luar backtick
- [ ] Semua tag self-closing (`<br />`, `<img />`)
- [ ] `<details>` punya blank line (kalau pakai HTML mentah)
- [ ] Link internal valid, tidak ada `.md` di URL
- [ ] Kode pakai language tag
- [ ] Admonition **pakai spasi** setelah `:::`
- [ ] Tidak ada typo

Verifikasi:

```bash
# Cek file .mdx tersisa (sisa dari Docusaurus)
find docs -name '*.mdx'

# Cek admonition tanpa spasi (sisa dari Docusaurus)
grep -rn ':::[a-z]' docs/

# Build — broken link akan muncul sebagai warning
bun run docs:build
```

::: tip Link internal di VitePress
**Jangan** sertakan `.md` di link internal — VitePress otomatis resolve:

- ✅ `[panduan](/global/format/page)`
- ❌ `[panduan](/global/format/page.md)`
  :::

Kalau build gagal:

| Error                        | Solusi                                   |
| ---------------------------- | ---------------------------------------- |
| `Element is missing end tag` | Ada `<` di teks, bungkus dengan backtick |
| `Invalid expression`         | Ada `{` literal, bungkus dengan backtick |
| `Failed to resolve import`   | Cek path komponen Vue                    |
| `Dead link`                  | Cek URL, hapus `.md` dari link internal  |
| `Duplicate routes`           | Ada file sama di path berbeda            |

## Template

**Landing page course:**

```yaml
---
title: RPL1XX — Nama Mata Kuliah
description: Materi, praktikum, dan referensi mata kuliah RPL1XX.
sidebar_position: NN
outline: deep
---
```

**Materi bertimestamp:**

```yaml
---
title: 'Pertemuan N — Topik'
description: Deskripsi singkat.
sidebar_position: N
---
```

## Referensi

- [VitePress — Markdown Extensions](https://vitepress.dev/guide/markdown)
- [VitePress — Frontmatter Config](https://vitepress.dev/reference/frontmatter-config)
- [VitePress — Routing](https://vitepress.dev/guide/routing)
- [VitePress — Theme Config](https://vitepress.dev/reference/default-theme-config)
- [VitePress — Using Vue in Markdown](https://vitepress.dev/guide/using-vue)
