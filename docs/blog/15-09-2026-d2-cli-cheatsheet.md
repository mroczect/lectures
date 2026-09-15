---
title: 'D2 CLI Cheatsheet: Panduan Lengkap Command Line D2'
description: 'Pelajari cara menggunakan command line interface (CLI) D2 secara maksimal. Panduan lengkap semua flag, subcommand, dan environment variable untuk merender diagram.'
date: 2026-09-15
tags: [tools, diagram, d2, cli, cheatsheet]
outline: deep
---

# D2 CLI Cheatsheet: Panduan Lengkap Command Line D2

::: tip Pembuka dari Dosen
Menggambar diagram dengan D2 itu mudah, tapi menguasai Command Line Interface (CLI)-nya akan membuat Anda 10x lebih cepat! CLI D2 bukan sekadar alat compile, tapi juga _formatter_, _validator_, dan _watch server_. Mari kita bedah semua perintahnya di sini.
:::

## Dasar Penggunaan: Kompilasi & Render

Sintaks dasar D2 adalah mengubah file `.d2` menjadi gambar. Jika Anda tidak menyebutkan format output, D2 akan otomatis menghasilkan file `.svg`.

```bash
d2 input.d2 output.svg
```

**Format Output yang Didukung:**
SVG, PNG, PDF, PPTX (PowerPoint), GIF, dan TXT (ASCII Art).

```bash
d2 input.d2 output.png      # Render ke PNG
d2 input.d2 output.pdf      # Render ke PDF
d2 input.d2 output.txt      # Render ke ASCII Text
```

::: warning Penting: Jangan andalkan keberadaan file output!
Terkadang, saat terjadi _error_ saat _rendering_, D2 tetap mengeluarkan file _render_ parsial yang rusak agar Anda bisa melihat kesalahannya. **Selalu gunakan _exit status_ dari perintah `d2`** untuk mengecek apakah compile berhasil 100%, bukan dengan mengecek apakah file outputnya ada.
:::

## Subcommand Utama

D2 bukan cuma satu perintah. Ada beberapa _subcommand_ yang sangat berguna dalam _workflow_ development.

| Subcommand      | Fungsi                                                   | Contoh Penggunaan     |
| :-------------- | :------------------------------------------------------- | :-------------------- |
| `fmt`           | Merapikan (autoformat) kode `.d2` Anda agar konsisten.   | `d2 fmt file.d2`      |
| `validate`      | Memvalidasi syntax file `.d2` tanpa merender.            | `d2 validate file.d2` |
| `layout`        | Melihat daftar _layout engine_ yang tersedia.            | `d2 layout`           |
| `layout [name]` | Melihat bantuan spesifik untuk _layout engine_ tertentu. | `d2 layout elk`       |
| `themes`        | Melihat daftar tema bawaan D2.                           | `d2 themes`           |
| `play`          | Langsung membuka file `.d2` di web playground resmi.     | `d2 play file.d2`     |

## Mode Pengembangan (Watch & Debug)

Saat Anda sedang membuat diagram, sangat melelahkan jika harus compile manual tiap menyimpan file. Gunakan **Watch Mode**!

```bash
d2 -w input.d2 output.svg
```

Secara _default_, ini akan memutar server lokal dan membuka browser. Jika Anda ingin mengatur manual _host_ dan _port_-nya:

```bash
d2 -w --host 127.0.0.1 --port 8080 input.d2
```

<details>
  <summary><b> Opsi Lanjutan untuk Watch Mode (Klik untuk melihat)</b></summary>

- `--browser true`: Atur _browser executable_ yang akan dibuka (misalnya `--browser firefox`). Set ke `0` agar tidak membuka browser.
- `--img-cache true`: Saat mode _watch_, gambar ikon dari URL akan di-cache. Matikan dengan `--img-cache=0` jika gambar sumber sering berubah.
- `-d, --debug`: Tampilkan log _debug_ di terminal saat proses compile berjalan.

</details>

## Tema, Font, dan Estetika

Salah satu keunggulan D2 adalah dukungan tema dan kustomisasi font secara langsung lewat CLI.

### Mengatur Tema & Dark Mode

```bash
d2 -t 101 input.d2 output.svg         # Menggunakan tema ID 101
d2 --dark-theme 200 input.d2 output.svg # Tema 200 dipakai jika browser user dalam mode gelap
```

::: tip Info Tema
Jalankan `d2 themes` di terminal Anda untuk melihat daftar lengkap tema dan ID-nya (misal: 0 hingga 300+).
:::

### Mode Sketsa Tangan (Sketch)

```bash
d2 -s input.d2 output.svg              # Render diagram agar terlihat seperti digambar tangan
```

### Kustomisasi Font (TTF)

Anda bisa mengganti font bawaan (Source Sans Pro / Source Code Pro) dengan file `.ttf` milik Anda.

```bash
d2 --font-regular=./helvetica.ttf --font-bold=./helvetica-bold.ttf input.d2
```

<details>
  <summary><b> Daftar Flag Font Lengkap</b></summary>

- `--font-regular`
- `--font-italic`
- `--font-bold`
- `--font-semibold`
- `--font-mono`
- `--font-mono-bold`
- `--font-mono-italic`
- `--font-mono-semibold`

</details>

## Layout Engine & Komposisi (Multi-board)

D2 memungkinkan Anda memilih _engine_ tata letak dan mengatur _multi-board_ (diagram dengan banyak lapisan/scenario).

### Pilih Layout Engine

Secara _default_ D2 memakai `dagre`. Anda bisa memakai `elk` atau `tala` (kustom Terrastruct).

```bash
d2 -l elk input.d2 output.svg
```

### Merender Board Spesifik

Jika diagram Anda punya banyak _layers/scenarios_, Anda bisa merender hanya satu bagian menggunakan `--target`.

```bash
d2 --target='layers.x' input.d2 output.svg         # Render hanya layer 'x'
d2 --target='layers.x.*' input.d2 output.svg       # Render layer 'x' beserta semua anaknya
```

### Animasi & Bundle

Jika diagram Anda _multi-board_, Anda bisa menggabungkannya menjadi satu file SVG animasi yang bertransisi otomatis!

```bash
d2 --animate-interval 1200 input.d2 output.svg     # Transisi setiap 1.2 detik
d2 -b input.d2 output.svg                          # Bundle semua aset gambar ke dalam SVG
```

## Opsi Rendering Lanjutan

Sesuaikan detail fisik diagram Anda dengan opsi _padding_, _scaling_, dan format _stdout_.

| Flag               | Deskripsi                                                                                                                       |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `--pad 100`        | Jumlah _pixel_ padding di sekeliling diagram.                                                                                   |
| `--scale 1`        | Skala output. `0.5` untuk mengecilkan setengah. `-1` (default) berarti fit to screen.                                           |
| `--center`         | Memusatkan SVG di tengah _viewbox_ (layar browser).                                                                             |
| `--force-appendix` | PNG tidak interaktif. Flag ini memaksa D2 menambahkan halaman daftar _tooltip/link_ di SVG.                                     |
| `--timeout 120`    | Batas waktu detik sebelum D2 _timeout_ (bagus untuk diagram super besar).                                                       |
| `--salt "mykey"`   | Tambahkan _salt_ ke ID elemen SVG. Berguna jika Anda menyematkan banyak diagram identik di satu HTML agar ID-nya tidak bentrok. |
| `--no-xml-tag`     | Hilangkan `<?xml ...?>` dari SVG. Berguna untuk _direct embed_ di HTML.                                                         |
| `--omit-version`   | Hilangkan tulisan versi D2 dari gambar hasil _render_.                                                                          |

### ASCII Mode

Jika Anda merender ke `.txt`, Anda bisa memilih jenis karakter.

```bash
d2 --ascii-mode standard input.d2 out.txt  # Pakai karakter ASCII dasar (+, -, |)
d2 --ascii-mode extended input.d2 out.txt   # Pakai Unicode (┌, ┐, ┘, ├)
```

## Stdout & Environment Variables

### Menulis ke Stdout

Anda bisa mem-pipe output D2 ke perintah lain tanpa menyimpan file. Gunakan tanda minus `-`.

```bash
echo "x -> y" | d2 - - > my_diagram.svg
echo "x -> y" | d2 --stdout-format=png - - > my_diagram.png
```

::: warning Keamanan Jaringan
Secara _default_, D2 memblokir akses gambar dari jaringan _private/lokal_ (loopback). Jika Anda tahu diagram Anda aman dan butuh gambar lokal, gunakan `--allow-private-network`.
:::

### Environment Variables

Daripada mengetik _flag_ panjang setiap kali, Anda bisa pakai _Environment Variable_ di terminal Anda.

<details>
  <summary><b> Daftar Lengkap Environment Variables (Klik untuk melihat)</b></summary>

| Env Variable                | Korespondensi Flag             |
| :-------------------------- | :----------------------------- |
| `D2_WATCH`                  | `-w`                           |
| `D2_LAYOUT`                 | `-l`                           |
| `D2_THEME`                  | `-t`                           |
| `D2_DARK_THEME`             | `--dark-theme`                 |
| `D2_PAD`                    | `--pad`                        |
| `D2_CENTER`                 | `--center`                     |
| `D2_SKETCH`                 | `-s`                           |
| `D2_BUNDLE`                 | `-b`                           |
| `D2_ALLOW_PRIVATE_NETWORK`  | `--allow-private-network`      |
| `D2_FORCE_APPENDIX`         | `--force-appendix`             |
| `D2_ANIMATE_INTERVAL`       | `--animate-interval`           |
| `D2_TIMEOUT`                | `--timeout`                    |
| `D2_CHECK`                  | `--check`                      |
| `D2_ASCII_MODE`             | `--ascii-mode`                 |
| `DEBUG`                     | `-d`                           |
| `IMG_CACHE`                 | `--img-cache`                  |
| `HOST` / `PORT` / `BROWSER` | Watch mode configurations      |
| `D2_STDOUT_FORMAT`          | `--stdout-format`              |
| `D2_NO_XML_TAG`             | `--no-xml-tag`                 |
| `OMIT_VERSION`              | `--omit-version`               |
| `D2_FONT_*`                 | `--font-*` (semua varian font) |

</details>

## Penutup

Menggunakan CLI D2 secara efektif akan mempercepat _workflow_ dokumentasi Anda. Terutama fitur `fmt` untuk merapikan kode, dan `--watch` untuk _live preview_ saat development.

::: tip Referensi Resmi

- Source Code: [https://github.com/d2lang/d2](https://github.com/d2lang/d2)
- Hosted Icons: [https://icons.d2lang.com](https://icons.d2lang.com)
- Playground: [https://play.d2lang.com](https://play.d2lang.com)
  :::
