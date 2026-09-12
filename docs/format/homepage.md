---
title: Halaman Homepage
description: Panduan membuat halaman dengan layout home — hero, features, dan struktur landing page.
outline: deep
---

# Panduan Halaman Homepage

Cara membuat halaman dengan **layout `home`** — landing page dengan hero section dan feature cards.

::: info Kapan Pakai?
Gunakan `layout: home` untuk halaman **titik masuk** — bukan halaman konten biasa.

Contoh: homepage utama, landing page versi, landing page mata kuliah, landing page informasi.
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

Hero adalah area utama di bagian atas halaman.

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
```

| Field     | Wajib | Keterangan                        |
| --------- | :---: | --------------------------------- |
| `name`    |  Ya   | Nama pendek — kode atau singkatan |
| `text`    |  Ya   | Teks utama besar                  |
| `tagline` | Tidak | Kalimat deskriptif di bawah       |
| `actions` | Tidak | Tombol call-to-action             |

**Tombol aksi:**

- `theme`: `brand` (utama) atau `alt` (netral)
- `text`: teks tombol
- `link`: URL tujuan — bisa anchor (`#section`) atau path (`/v1/courses/`)

**Rekomendasi:** maksimal 3 tombol. Tombol pertama pakai `theme: brand`.

## Struktur Features

Grid kartu di bawah hero.

```yaml
features:
  - title: Judul Kartu
    details: Deskripsi singkat kartu.
    link: /path/tujuan # opsional
    linkText: Buka Halaman # wajib jika ada link
  - title: Kartu Kedua
    details: Deskripsi kartu kedua.
```

| Field      |      Wajib      | Keterangan                        |
| ---------- | :-------------: | --------------------------------- |
| `title`    |       Ya        | Judul kartu — singkat dan jelas   |
| `details`  |       Ya        | Deskripsi 1–2 baris               |
| `link`     |      Tidak      | URL tujuan jika kartu bisa diklik |
| `linkText` | Jika `link` ada | Teks tombol di dalam kartu        |

**Rekomendasi:** 4–8 kartu. Setiap kartu fokus pada satu konsep.

## Contoh Lengkap

```yaml
---
title: Mata Kuliah
description: Daftar mata kuliah TRPL Polibatam.
layout: home

hero:
  name: Mata Kuliah
  text: Daftar Mata Kuliah TRPL Polibatam
  tagline: Tujuh mata kuliah, satu kurikulum terhubung.
  actions:
    - theme: brand
      text: Jelajahi Mata Kuliah
      link: '#daftar'
    - theme: alt
      text: Informasi Perkuliahan
      link: /v1/information/

features:
  - title: RPL101 — Pengantar RPL
    details: Siklus hidup perangkat lunak dan metodologi.
    link: /v1/courses/rpl101-pengantar-rpl/
    linkText: Buka Mata Kuliah
  - title: RPL105 — Pemrograman Web
    details: HTML, CSS, JavaScript, PHP, MySQL.
    link: /v1/courses/rpl105-pemrograman-web/
    linkText: Buka Mata Kuliah
---
## Daftar Mata Kuliah

Konten markdown di bawah frontmatter dirender setelah hero dan features.
```

## Setelah Hero & Features

Setelah hero dan features, kamu bisa menulis **konten markdown biasa** — akan dirender di bawah kartu.

```markdown
## Section Pertama

Paragraf biasa, tabel, code block, dan admonitions.

## Section Kedua

Konten lanjutan.
```

::: tip Anchor untuk Tombol
Tombol aksi yang menunjuk ke `#section` akan smooth-scroll ke section tersebut. Cara praktis mengarahkan pembaca ke bagian penting.
:::

## Pola Umum

| Pola          | Struktur                               | Cocok untuk                       |
| ------------- | -------------------------------------- | --------------------------------- |
| **Sederhana** | Hero + 6 features                      | Landing page versi, section kecil |
| **Navigasi**  | Hero + 3 tombol + 6 features + section | Homepage mata kuliah, informasi   |
| **Kompleks**  | Hero + features + banyak section + FAQ | Homepage utama                    |

## Checklist

- [ ] Frontmatter punya `layout: home`
- [ ] `title` dan `description` diisi
- [ ] `hero.name` singkat dan jelas
- [ ] `hero.text` menarik perhatian
- [ ] `hero.tagline` menjelaskan value proposition
- [ ] Maksimal **3 tombol** di `hero.actions`
- [ ] Tombol pertama pakai `theme: brand`
- [ ] `features` berisi **4–8 kartu**
- [ ] Setiap kartu punya `title` dan `details`
- [ ] Kartu dengan `link` juga punya `linkText`

## Contoh Referensi

| Halaman                                     | Tipe                            |
| ------------------------------------------- | ------------------------------- |
| [Root Home](/)                              | Homepage utama proyek           |
| [Version 1](/v1/)                           | Landing page versi              |
| [Mata Kuliah](/v1/courses/)                 | Landing page daftar mata kuliah |
| [RPL101](/v1/courses/rpl101-pengantar-rpl/) | Landing page mata kuliah        |

## Halaman Terkait

| Halaman                        | Deskripsi                      |
| ------------------------------ | ------------------------------ |
| [Format & Rules](/format/page) | Landing page panduan format    |
| [Halaman Konten](/format/page) | Panduan halaman konten standar |
| [Halaman Tugas](/format/task)  | Panduan halaman tugas          |

::: warning Perhatian
Jangan pakai `layout: home` untuk halaman konten biasa — layout ini dirancang untuk landing page dan akan terasa "over-designed" untuk konten sederhana.
:::
