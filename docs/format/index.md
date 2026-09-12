---
title: Format & Rules
description: Pusat panduan penulisan, penamaan file, dan kontribusi untuk dokumentasi Lectures.
layout: home

hero:
  name: Format & Rules
  text: Panduan Dokumentasi
  tagline: Satu pusat panduan — dari penamaan file hingga struktur halaman. Referensi yang menjaga dokumentasi Lectures tetap konsisten.
  actions:
    - theme: brand
      text: Mulai
      link: '#panduan-tersedia'
    - theme: alt
      text: Prinsip
      link: '#tiga-prinsip'
    - theme: alt
      text: Checklist
      link: /format/page#checklist-pre-commit

features:
  - title: Halaman Konten
    details: Panduan menulis halaman konten standar — heading, tabel, code block, admonitions.
    link: /format/page
    linkText: Buka
  - title: Halaman Homepage
    details: Panduan layout home — hero, features, dan struktur landing page.
    link: /format/homepage
    linkText: Buka
  - title: Halaman Tugas
    details: Panduan format halaman tugas — daftar tugas dan template instruksi.
    link: /format/task
    linkText: Buka
---

::: tip Tujuan
Folder `format/` adalah **pusat referensi** untuk semua panduan penulisan. Setiap file fokus pada satu aspek — mudah dipelajari dan dipelihara.
:::

## Panduan Tersedia

| Halaman                                | Fokus                                |
| -------------------------------------- | ------------------------------------ |
| [Halaman Konten](/format/page)         | Format penulisan markdown lengkap    |
| [Halaman Homepage](/format/homepage)   | Layout `home` dengan hero + features |
| [Halaman Tugas](/format/task)          | Format halaman tugas & assignment    |
| [Tugas Selesai](/format/task-complite) | Menandai tugas yang sudah selesai    |

## Tiga Prinsip

1. **Keteraturan** — struktur folder, nama file, dan format halaman konsisten di seluruh proyek.
2. **Keterbacaan** — konten mudah dipahami pembaca baru maupun lama. Definisikan istilah, berikan contoh.
3. **Keberlanjutan** — dokumentasi mudah diperbarui tanpa merusak bagian lain. Versioning, pembekuan versi lama, validasi otomatis.

## Mulai dari Mana

| Langkah | Aksi                            | Panduan                                              |
| :-----: | ------------------------------- | ---------------------------------------------------- |
|    1    | Pelajari format penulisan dasar | [Halaman Konten](/format/page)                       |
|    2    | Tentukan tipe halaman           | —                                                    |
|    3    | Buka panduan spesifik           | [Homepage](/format/homepage) · [Tugas](/format/task) |
|    4    | Jalankan checklist              | [Checklist](/format/page#checklist-pre-commit)       |
|    5    | Commit                          | [Commit Rules](/format/page#aturan-git-commit)       |

## Ringkasan Cepat

| Topik             | Aturan                                        |
| ----------------- | --------------------------------------------- |
| **Nama file**     | Lowercase, kebab-case — `pemrograman-web.md`  |
| **Judul**         | Satu `#` per halaman                          |
| **Frontmatter**   | Wajib `title` dan `description`               |
| **Link internal** | Path absolut dengan prefix versi, tanpa `.md` |
| **Code block**    | Sebutkan bahasanya — ` ```ts `                |
| **Admonitions**   | `info`, `tip`, `warning`, `danger`, `details` |
| **Commit**        | `<tipe>: <deskripsi singkat>`                 |

## Halaman Terkait

| Halaman                              | Deskripsi                |
| ------------------------------------ | ------------------------ |
| [Root Home](/)                       | Homepage utama proyek    |
| [Halaman Konten](/format/page)       | Panduan format penulisan |
| [Halaman Homepage](/format/homepage) | Panduan layout `home`    |
| [Halaman Tugas](/format/task)        | Panduan halaman tugas    |
