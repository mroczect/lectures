---
title: Halaman Konten
description: Panduan menulis halaman konten standar — heading, tabel, code block, admonitions, dan aturan penulisan.
outline: deep
---

# Panduan Halaman Konten

Cara menulis **halaman konten standar** — format markdown, konvensi penamaan file, dan aturan kontribusi.

::: info Untuk Siapa?
Untuk halaman **konten** — bukan `layout: home` ([Homepage](/format/homepage)), bukan halaman tugas ([Tugas](/format/task)).
:::

## Struktur Folder

```text
docs/
├── index.md
├── license.md
├── format/
│   ├── index.md
│   ├── homepage.md
│   ├── page.md
│   ├── task.md
│   └── task-complite.md
├── public/
│   ├── favicon.svg
│   └── images/
└── v1/
    ├── index.md
    ├── about.md
    ├── courses/
    ├── information/
    └── task/
```

Versi baru disimpan di folder baru (`v2/`, `v3/`). Halaman global seperti `format/` dan `public/` tidak bergantung versi.

## Penamaan File

**Aturan umum:** lowercase, hyphen sebagai pemisah, deskriptif dan ringkas.

| Tipe        | Format                  | Contoh                            |
| ----------- | ----------------------- | --------------------------------- |
| Mata kuliah | `<kode-mk>/index.md`    | `rpl105-pemrograman-web/index.md` |
| Materi      | `materi-XX-<topik>.md`  | `materi-03-linux-basics.md`       |
| Tugas       | `tugas-XX-<nama>.md`    | `tugas-01-resume-paper.md`        |
| Catatan     | `catatan-YYYY-MM-DD.md` | `catatan-2026-09-12.md`           |
| Lab         | `lab-XX-<nama>.md`      | `lab-02-html-css.md`              |
| UTS         | `uts-YYYY-MM-DD.md`     | `uts-2026-10-20.md`               |
| Referensi   | `ref-<topik>.md`        | `ref-algoritma-sorting.md`        |

## Frontmatter

Wajib di bagian paling atas:

```yaml
---
title: Judul Halaman
description: Deskripsi singkat halaman.
---
```

| Field         | Wajib | Fungsi                                    |
| ------------- | :---: | ----------------------------------------- |
| `title`       |  Ya   | Judul di tab dan sidebar                  |
| `description` |  Ya   | Deskripsi singkat untuk SEO               |
| `outline`     | Tidak | Set `deep` untuk daftar isi detail        |
| `layout`      | Tidak | Set `home` untuk landing page             |
| `order`       | Tidak | Urutan tampil di sidebar                  |
| `draft`       | Tidak | Set `true` untuk menyembunyikan sementara |

**Contoh lengkap:**

```yaml
---
title: Pemrograman Berbasis Web
description: Materi, tugas, dan catatan untuk mata kuliah Pemrograman Berbasis Web.
outline: deep
order: 6
---
```

## Format Markdown

### Heading

- `#` untuk judul halaman, **hanya sekali**.
- `##` untuk section utama, `###` untuk sub-section.
- **Jangan lompati level** — jangan `##` langsung ke `####`.

### Paragraf

Pisahkan dengan **satu baris kosong**. Usahakan 3–4 baris per paragraf.

### Penekanan

| Format        | Sintaks      | Contoh          |
| ------------- | ------------ | --------------- |
| Bold          | `**teks**`   | **penting**     |
| Italic        | `_teks_`     | _istilah asing_ |
| Inline code   | `` `kode` `` | `bun install`   |
| Strikethrough | `~~teks~~`   | ~~salah~~       |

### Daftar

```markdown
- Item pertama
- Item kedua
  - Sub-item

1. Langkah pertama
2. Langkah kedua
```

### Link

- **Internal:** `[Teks](/v1/path/tanpa-ekstensi)`
- **Eksternal:** `[Teks](https://contoh.com)`
- **Selalu deskriptif** — hindari "klik di sini"

## Tabel

```markdown
| Kolom 1 | Kolom 2 | Kolom 3 |
| ------- | ------- | ------- |
| Data 1  | Data 2  | Data 3  |
```

**Alignment:**

| Kiri | Tengah | Kanan |
| :--- | :----: | ----: |
| a    |   b    |     c |

```markdown
| Kiri | Tengah | Kanan |
| :--- | :----: | ----: |
| a    |   b    |     c |
```

## Code Block

Selalu sebutkan bahasa untuk syntax highlighting:

````markdown
```ts
const hello = 'world';
```

```bash
bun install
```
````

Bahasa umum: `ts`, `js`, `bash`, `json`, `yaml`, `markdown`, `html`, `css`, `sql`, `python`.

**Line highlighting:**

````markdown
```ts{2}
const a = 1;
const b = 2;
const c = 3;
```
````

## Admonitions

```markdown
::: info Judul Opsional
Informasi umum.
:::

::: tip Tips
Saran atau praktik baik.
:::

::: warning Peringatan
Hal yang perlu dihati-hati.
:::

::: danger Bahaya
Tindakan berisiko.
:::

::: details Detail
Konten yang bisa diperluas.
:::
```

| Tipe      | Kapan Dipakai                        |
| --------- | ------------------------------------ |
| `info`    | Konteks atau penjelasan tambahan     |
| `tip`     | Saran, shortcut, praktik baik        |
| `warning` | Hal yang mungkin menimbulkan masalah |
| `danger`  | Tindakan berbahaya atau terlarang    |
| `details` | Konten opsional atau spoiler         |

## Gambar

Simpan di `docs/public/images/`. Referensikan dengan path absolut:

```markdown
![Teks alt](/images/screenshot-web.png)
```

**Aturan:** selalu beri alt text · ukuran di bawah 500 KB · `.svg` untuk diagram, `.png` untuk screenshot, `.jpg` untuk foto.

## Fitur Lanjutan

| Fitur             | Sintaks                              |
| ----------------- | ------------------------------------ |
| Task list         | `- [x] Selesai` · `- [ ] Belum`      |
| Footnote          | `teks[^1]` + `[^1]: isi`             |
| Abbreviation      | `*[HTML]: HyperText Markup Language` |
| Highlight         | `==teks disorot==`                   |
| Insert            | `++teks disisipkan++`                |
| Subscript         | `~~teks~~`                           |
| Superscript       | `^teks^`                             |
| Matematika inline | `$E = mc^2$`                         |
| Matematika block  | `$$ ... $$`                          |
| Mermaid           | ` ```mermaid `                       |

## Aturan Konten

- **Bahasa:** konsisten dalam satu halaman — Indonesia atau Inggris.
- **Nada:** formal tapi tidak kaku. Objektif. Ringkas.
- **Struktur halaman mata kuliah:** frontmatter → judul → info singkat (kode, SKS, dosen, jadwal) → materi → tugas → referensi.

## Tanggal

Selalu **ISO 8601**:

| Format         | Contoh              | Kapan                      |
| -------------- | ------------------- | -------------------------- |
| `YYYY-MM-DD`   | `2026-09-12`        | Nama file, tanggal teknis  |
| `DD MMMM YYYY` | `12 September 2026` | Konten yang dibaca manusia |

## Aturan Git Commit

Format: `<tipe>: <deskripsi singkat>`

| Tipe       | Fungsi                            |
| ---------- | --------------------------------- |
| `feat`     | Konten baru                       |
| `fix`      | Perbaikan konten atau typo        |
| `docs`     | Perubahan dokumentasi             |
| `chore`    | Tugas rutin                       |
| `refactor` | Restrukturisasi tanpa ubah konten |
| `style`    | Formatting, whitespace            |

Contoh:

```text
feat: add RPL105 lecture note for session 3
fix: correct typo in class schedule
docs: update writing format rules
```

## Link Internal

- **Path absolut** dari root, dengan prefix versi.
- **Jangan** sertakan ekstensi `.md`.
- **Jangan** pakai path relatif.

```markdown
✅ Benar: [Pemrograman Web](/v1/courses/rpl105-pemrograman-web/)
❌ Salah: [Pemrograman Web](../courses/rpl105-pemrograman-web.md)
❌ Salah: [Pemrograman Web](./rpl105-pemrograman-web)
```

## Sidebar

Dikonfigurasi di `docs/.vitepress/sidebar.json`. VitePress memilih key dengan prefix terpanjang yang cocok.

```json
{
  "/v1/courses/": [
    {
      "text": "Courses",
      "items": [{ "text": "Overview", "link": "/v1/courses/" }]
    }
  ]
}
```

Setiap halaman baru **wajib** diikuti update sidebar.

## Checklist Pre-Commit

- [ ] Frontmatter dengan `title` dan `description`
- [ ] Nama file **kebab-case**
- [ ] Heading **tidak melompati level**
- [ ] Code block **menyebutkan bahasa**
- [ ] Link internal **path absolut** dengan prefix versi
- [ ] Tabel rapi dan konsisten
- [ ] Tidak ada typo
- [ ] File terformat dengan benar
- [ ] **Sidebar diperbarui** jika menambah halaman
- [ ] Commit message mengikuti `<tipe>: <deskripsi>`

## Validasi Otomatis

| Command                | Fungsi                                |
| ---------------------- | ------------------------------------- |
| `bun run format`       | Auto-format dengan Prettier           |
| `bun run format:check` | Cek format tanpa mengubah             |
| `bun run lint`         | Cek kualitas kode                     |
| `bun run typecheck`    | Cek tipe TypeScript                   |
| `bun run rebuild`      | Full clean + format + build + preview |

## Versioning

**Menambah versi baru:**

1. Duplikasi folder: `cp -r docs/v1 docs/v2`
2. Update konten di `docs/v2/`
3. Tambahkan blok `/v2/` di `sidebar.json`
4. Daftarkan di array `VERSIONS` di `config.ts`
5. Update link navigasi di `themeConfig.nav`
6. Update tabel versi di `docs/index.md`

**Mengedit versi lama:** dibekukan. Jangan edit kecuali kesalahan faktual kritis, link rusak, atau koreksi keamanan.

**Deprekasi versi:** tandai sebagai `deprecated` di tabel versi. Simpan folder dan entri sidebar agar link lama tetap valid.

## Aksesibilitas

- Beri `alt` text deskriptif untuk setiap gambar.
- Gunakan teks link deskriptif, bukan URL mentah.
- Jaga kontras warna yang cukup.
- Jangan mengandalkan warna saja untuk menyampaikan makna.
- Jaga hierarki heading tetap logis.

## SEO & Performa

**SEO:** build hook otomatis mengisi `og:title`, `og:image`, dan `canonical`. Untuk menjaga kualitas: tulis `description` unik, gunakan judul bermakna, hindari duplikasi antar versi.

**Performa:** prefer `.svg` untuk ikon dan diagram · ukuran gambar di bawah 500 KB · hindari gambar base64 besar · gunakan code group untuk blok berulang.

## FAQ

::: details Ada aturan yang tidak cocok?
Aturan ini komprehensif tapi tidak kaku. Diskusikan dengan maintainer, dokumentasikan pengecualian, dan update halaman ini jika pengecualian berguna umum.
:::

::: details Bisa pakai link relatif?
**Tidak.** Semua link internal wajib **path absolut dengan prefix versi**.
:::

::: details Kapan sidebar perlu diupdate?
**Setiap kali menambah halaman baru.** Sidebar tidak auto-update.
:::

## Halaman Terkait

| Halaman                                | Deskripsi                      |
| -------------------------------------- | ------------------------------ |
| [Format & Rules](/format/page)         | Landing page panduan format    |
| [Halaman Homepage](/format/homepage)   | Panduan layout `home`          |
| [Halaman Tugas](/format/task)          | Panduan halaman tugas          |
| [Tugas Selesai](/format/task-complite) | Panduan menandai tugas selesai |
