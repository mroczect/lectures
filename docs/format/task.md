---
title: Halaman Tugas
description: Panduan membuat halaman tugas di dokumentasi Lectures — daftar tugas, ringkasan status, dan template instruksi.
outline: deep
---

# Panduan Halaman Tugas

Halaman ini menjelaskan cara membuat **halaman tugas** — halaman yang menampilkan daftar tugas, instruksi, dan status pengumpulan.

::: info Kapan Pakai Panduan Ini?
Gunakan panduan ini untuk halaman **task tracker** — seperti [Daftar Tugas](/v1/task/) atau halaman tugas individual seperti [Tugas Teori Himpunan](/v1/task/tugas-matematika-diskrit-materi-himpunan).
:::

## Dua Jenis Halaman Tugas

| Jenis            | Fungsi                                | Contoh                  |
| ---------------- | ------------------------------------- | ----------------------- |
| **Index Tugas**  | Daftar semua tugas + ringkasan status | `/v1/task/`             |
| **Detail Tugas** | Instruksi lengkap satu tugas          | `/v1/task/tugas-xxx.md` |

## Struktur Index Tugas

Halaman index tugas menggunakan `layout: home` dengan struktur berikut:

### Frontmatter Minimum

```yaml
---
title: Tugas
description: Kumpulan tugas mata kuliah — lengkap dengan deadline, status, dan tautan pengumpulan.
layout: home
---
```

### Hero

```yaml
hero:
  name: Tugas
  text: Kumpulan Tugas Mata Kuliah
  tagline: Semua tugas, satu halaman — lengkap dengan deadline, status, dan tautan pengumpulan.
  actions:
    - theme: brand
      text: Lihat Daftar Tugas
      link: '#daftar-tugas'
    - theme: alt
      text: E-Learning
      link: https://learningif.polibatam.ac.id
```

### Features

```yaml
features:
  - title: 7 Mata Kuliah
    details: Semua tugas dari tujuh mata kuliah dikumpulkan dalam satu halaman.
  - title: Status Terkini
    details: Setiap tugas punya status yang jelas — belum, sedang, sudah.
  - title: Deadline Jelas
    details: Tenggat pengumpulan tercatat rapi.
  - title: Tautan Pengumpulan
    details: Langsung menuju halaman tugas di e-learning.
```

## Status Tugas

Gunakan **teks status** (bukan emoji) untuk konsistensi:

| Status                | Warna   | Kapan Dipakai                    |
| --------------------- | ------- | -------------------------------- |
| **Belum dikerjakan**  | Merah   | Belum ada progres                |
| **Sedang dikerjakan** | Kuning  | Sudah mulai, belum selesai       |
| **Sudah dikumpulkan** | Hijau   | Sudah submit sebelum deadline    |
| **Terlewat**          | Abu-abu | Deadline lewat tanpa pengumpulan |

::: warning Konsistensi Status
Gunakan salah satu dari empat status di atas secara konsisten. Jangan mengarang status baru seperti "hampir selesai" atau "setengah jalan".
:::

## Struktur Detail Tugas

Halaman detail tugas menggunakan **layout default** (bukan home):

### Frontmatter

```yaml
---
title: Tugas Matematika Diskrit — Teori Himpunan
description: Tugas mata kuliah Matematika Diskrit tentang operasi himpunan.
outline: deep
---
```

### Section Wajib

Setiap halaman detail tugas minimal berisi:

1. **Petunjuk Tugas** — langkah pengerjaan
2. **Daftar Soal** — 1 hingga N soal
3. **Format Pengumpulan** — bentuk, panjang, deadline
4. **Referensi** — sumber bacaan
5. **Tips** — praktik baik

### Struktur Soal

Setiap soal sebaiknya punya struktur konsisten:

```markdown
### Tugas 1: Judul Soal

::: info Konteks
Deskripsi situasi atau sistem yang menjadi latar soal.
:::

**Data soal:**

[Data dalam bentuk tabel / kode / list]

**Pertanyaan:**

**a.** Pertanyaan pertama.
**b.** Pertanyaan kedua.

::: details Petunjuk Pengerjaan
Langkah atau hint tanpa membocorkan jawaban.
:::
```

## Template Lengkap

Berikut template lengkap untuk halaman **detail tugas**:

```markdown
---
title: Tugas [Nama Tugas]
description: Tugas mata kuliah [Nama Mata Kuliah] tentang [topik].
outline: deep
---

# Tugas [Nama Mata Kuliah]: [Topik]

## Petunjuk Tugas

1. Baca materi tentang [topik] dari sumber bacaan.
2. Diskusikan dalam kelompok kecil (2–3 orang) atau sesuai Tim PBL.
3. Siapkan ringkasan jawaban (1 halaman) dalam bentuk PPT atau PDF.

::: warning Format Pengumpulan

- **Bentuk:** PPT atau PDF
- **Panjang:** 1 halaman ringkasan
- **Pengumpulan:** Melalui e-learning IF Polibatam
  :::

## Daftar Soal

### Soal 1: [Judul]

::: info Konteks
[Deskripsi konteks]
:::

**Pertanyaan:**
**a.** [Pertanyaan pertama]
**b.** [Pertanyaan kedua]

::: details Petunjuk Pengerjaan
[Petunjuk tanpa bocoran jawaban]
:::

## Ringkasan Soal

| No. | Judul   | Konsep Utama | Tingkat Kesulitan |
| --- | ------- | ------------ | :---------------: |
| 1   | [Judul] | [Konsep]     |       Mudah       |

## Referensi

| No. | Referensi        |
| --- | ---------------- |
| 1   | [Buku referensi] |

## Format Pengumpulan

::: warning Format Wajib

- **Bentuk:** PPT atau PDF
- **Panjang:** 1 halaman
- **Pengumpulan:** E-learning
  :::

## Tips Mengerjakan

::: tip Tips

- Kerjakan berurutan.
- Tulis langkah pengerjaan.
- Cek ulang hasil.
  :::
```

## Checklist Halaman Tugas

### Untuk Index Tugas

- [ ] Frontmatter dengan `layout: home`
- [ ] Hero dengan action ke daftar tugas
- [ ] Features 4–6 kartu
- [ ] Section **Daftar Tugas** dengan setiap tugas
- [ ] Section **Ringkasan Status** dalam tabel
- [ ] Section **Tugas per Mata Kuliah**
- [ ] Section **Tips** dan **FAQ**

### Untuk Detail Tugas

- [ ] Frontmatter dengan `title`, `description`, `outline: deep`
- [ ] Section **Petunjuk Tugas**
- [ ] Section **Daftar Soal** — minimal 1 soal
- [ ] Setiap soal punya konteks, pertanyaan, dan petunjuk (opsional)
- [ ] Section **Ringkasan Soal** dalam tabel
- [ ] Section **Referensi**
- [ ] Section **Format Pengumpulan**
- [ ] Section **Tips Mengerjakan**

## Halaman Terkait

| Halaman                                                                               | Deskripsi                       |
| ------------------------------------------------------------------------------------- | ------------------------------- |
| [**Format & Rules**](/format/page)                                                    | Landing page panduan format     |
| [**Halaman Konten**](/format/page)                                                    | Panduan halaman konten standar  |
| [**Halaman Homepage**](/format/homepage)                                              | Panduan layout `home`           |
| [**Tugas Selesai**](/format/task-complite)                                            | Panduan menandai tugas selesai  |
| [**Contoh: Daftar Tugas**](/v1/task/)                                                 | Implementasi nyata index tugas  |
| [**Contoh: Tugas Teori Himpunan**](/v1/task/tugas-matematika-diskrit-materi-himpunan) | Implementasi nyata detail tugas |
