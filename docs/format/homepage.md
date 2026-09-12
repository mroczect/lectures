---
title: Halaman Homepage
description: Panduan membuat halaman dengan layout home — hero, features, dan struktur landing page di dokumentasi Lectures.
outline: deep
---

# Panduan Halaman Homepage

Halaman ini menjelaskan cara membuat **halaman dengan layout `home`** — halaman yang menjadi landing page dengan hero section dan feature cards.

::: info Kapan Pakai Layout Home?
Gunakan `layout: home` untuk halaman yang menjadi **titik masuk** (landing page) dari suatu bagian — bukan halaman konten biasa. Contoh:

- Homepage utama (`docs/index.md`)
- Landing page versi (`docs/v1/index.md`)
- Landing page mata kuliah (`docs/v1/courses/rpl101-pengantar-rpl/index.md`)
- Landing page informasi (`docs/v1/information/index.md`)

:::

## Frontmatter Minimum

```yaml
---
title: Judul Halaman
description: Deskripsi singkat halaman.
layout: home
---
```

## Struktur Hero

Hero section adalah area utama di bagian atas halaman. Strukturnya:

```yaml
hero:
  name: Nama Singkat
  text: Teks Besar
  tagline: Kalimat deskriptif yang lebih panjang.
  actions:
    - theme: brand
      text: Tombol Utama
      link: /path/tujuan
    - theme: alt
      text: Tombol Sekunder
      link: /path/lain
    - theme: alt
      text: Tombol Ketiga
      link: https://external.com
```

### Field Hero

| Field     | Wajib | Keterangan                                 |
| --------- | :---: | ------------------------------------------ |
| `name`    |  Ya   | Nama pendek — biasanya kode atau singkatan |
| `text`    |  Ya   | Teks utama yang besar                      |
| `tagline` | Tidak | Kalimat deskriptif di bawah teks utama     |
| `actions` | Tidak | Tombol call-to-action                      |

### Tombol Aksi

Setiap tombol punya:

- `theme`: `brand` (warna utama) atau `alt` (netral)
- `text`: Teks tombol
- `link`: URL tujuan — bisa anchor (`#section`) atau path (`/v1/courses/`)

**Rekomendasi:**

- Maksimal **3 tombol** — lebih dari itu membingungkan.
- Tombol pertama pakai `theme: brand` sebagai aksi utama.
- Tombol berikutnya pakai `theme: alt`.

## Struktur Features

Features adalah grid kartu di bawah hero. Strukturnya:

```yaml
features:
  - title: Judul Kartu
    details: Deskripsi singkat kartu.
    link: /path/tujuan # opsional
    linkText: Buka Halaman # opsional, wajib jika link ada
  - title: Kartu Kedua
    details: Deskripsi kartu kedua.
```

### Field Feature

| Field      |      Wajib      | Keterangan                        |
| ---------- | :-------------: | --------------------------------- |
| `title`    |       Ya        | Judul kartu — singkat dan jelas   |
| `details`  |       Ya        | Deskripsi 1–2 baris               |
| `link`     |      Tidak      | URL tujuan jika kartu bisa diklik |
| `linkText` | Jika `link` ada | Teks tombol di dalam kartu        |

**Rekomendasi:**

- **4–8 kartu** — kurang dari 4 terasa kosong, lebih dari 8 terlalu penuh.
- Setiap kartu fokus pada **satu konsep**.
- Jika kartu punya `link`, wajib punya `linkText`.

## Contoh Lengkap

```yaml
---
title: Mata Kuliah
description: Daftar mata kuliah TRPL Polibatam beserta materi, tugas, dan referensinya.
layout: home

hero:
  name: Mata Kuliah
  text: Daftar Mata Kuliah TRPL Polibatam
  tagline: Tujuh mata kuliah, satu kurikulum terhubung — dari fondasi pemrograman hingga aplikasi web.
  actions:
    - theme: brand
      text: Jelajahi Mata Kuliah
      link: '#daftar'
    - theme: alt
      text: Informasi Perkuliahan
      link: /v1/information/

features:
  - title: RPL101 — Pengantar RPL
    details: Siklus hidup perangkat lunak, metodologi, dan peran profesional.
    link: /v1/courses/rpl101-pengantar-rpl/
    linkText: Buka Mata Kuliah
  - title: RPL105 — Pemrograman Web
    details: HTML, CSS, JavaScript, PHP, MySQL, dan autentikasi.
    link: /v1/courses/rpl105-pemrograman-web/
    linkText: Buka Mata Kuliah
---
## Daftar Mata Kuliah

Konten markdown di bawah frontmatter akan ditampilkan setelah section hero dan features.
```

## Setelah Hero & Features

Setelah hero dan features, kamu **bisa menulis konten markdown biasa**. Konten ini akan dirender di bawah kartu-kartu.

```markdown
## Section Pertama

Paragraf biasa, tabel, code block, dan admonitions — semua bisa dipakai.

## Section Kedua

Konten lanjutan.
```

::: tip Gunakan Anchor untuk Tombol
Tombol aksi yang menunjuk ke `#section` akan smooth-scroll ke section tersebut di halaman yang sama. Ini cara praktis untuk mengarahkan pembaca ke bagian penting.
:::

## Kombinasi yang Sering Dipakai

### Pola 1 — Landing Page Sederhana

Hero + 6 features + sedikit konten.

Cocok untuk: **homepage versi**, **landing page section kecil**.

### Pola 2 — Landing Page dengan Navigasi

Hero + 3 tombol + 6 features + beberapa section lengkap.

Cocok untuk: **homepage mata kuliah**, **homepage informasi**.

### Pola 3 — Landing Page Kompleks

Hero + features + banyak section dengan diagram, tabel, dan FAQ.

Cocok untuk: **homepage utama** yang menjadi pintu masuk seluruh dokumentasi.

## Checklist Halaman Homepage

- [ ] Frontmatter memiliki `layout: home`
- [ ] `title` dan `description` diisi
- [ ] `hero.name` singkat dan jelas
- [ ] `hero.text` menarik perhatian
- [ ] `hero.tagline` menjelaskan value proposition
- [ ] Maksimal **3 tombol** di `hero.actions`
- [ ] Tombol pertama memakai `theme: brand`
- [ ] `features` berisi **4–8 kartu**
- [ ] Setiap kartu punya `title` dan `details`
- [ ] Kartu dengan `link` juga punya `linkText`
- [ ] Konten tambahan di bawah features (opsional)

## Contoh Referensi

Lihat halaman-halaman berikut sebagai contoh nyata:

| Halaman                                                     | Tipe                            |
| ----------------------------------------------------------- | ------------------------------- |
| [Root Home](/)                                              | Homepage utama proyek           |
| [Version 1](/v1/)                                           | Landing page versi              |
| [Mata Kuliah](/v1/courses/)                                 | Landing page daftar mata kuliah |
| [RPL101 — Pengantar RPL](/v1/courses/rpl101-pengantar-rpl/) | Landing page mata kuliah        |

## Halaman Terkait

| Halaman                            | Deskripsi                      |
| ---------------------------------- | ------------------------------ |
| [**Format & Rules**](/format/page) | Landing page panduan format    |
| [**Halaman Konten**](/format/page) | Panduan halaman konten standar |
| [**Halaman Tugas**](/format/task)  | Panduan halaman tugas          |

::: warning Perhatian
Jangan pakai `layout: home` untuk halaman konten biasa — layout ini dirancang untuk landing page dan akan membuat halaman terasa "over-designed" untuk konten sederhana.
:::
