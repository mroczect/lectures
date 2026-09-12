---
title: Tugas RPL103 — Teori Himpunan
description: Tugas Matematika Diskrit tentang operasi himpunan, inklusi-eksklusi, dan fuzzy set — TRPL Politeknik Negeri Batam.
layout: home

hero:
  name: Tugas RPL103
  text: Teori Himpunan
  tagline: Lima soal penerapan teori himpunan pada sistem nyata — e-commerce, analitik web, login multi-platform, rekomendasi produk, dan penilaian kinerja.
  actions:
    - theme: brand
      text: Daftar Soal
      link: '#daftar-soal'
    - theme: alt
      text: Kembali
      link: /v1/task/

features:
  - title: 5 Soal
    details: Soal dengan konteks sistem nyata, bukan abstrak.
  - title: Kerja Kelompok
    details: Dikerjakan 2–3 orang atau sesuai Tim PBL.
  - title: Luaran PPT / PDF
    details: Ringkasan 1 halaman untuk dipresentasikan.
---

::: tip Sebelum Mengerjakan
Baca materi: operasi himpunan, kardinalitas, inklusi-eksklusi, dan fuzzy set.
:::

## Petunjuk

1. Baca materi dari referensi yang tersedia.
2. Diskusikan dalam kelompok kecil (2–3 orang) atau Tim PBL.
3. Kerjakan 5 soal di bawah.
4. Susun ringkasan **1 halaman** (PPT atau PDF).
5. Presentasikan pada pertemuan berikutnya.

**Pengumpulan:** e-learning IF Polibatam.

## Daftar Soal

### Soal 1 — Back-end E-commerce

Kategori A (Produk Terlaris) didefinisikan eksplisit:
$$A = \{101, 102, 105, 108, 112\}$$

Kategori B (Promo Flash Sale) didefinisikan dengan syarat:
$$B = \{x \mid 100 \leq x \leq 115, \ x \text{ habis dibagi } 3\}$$

**Pertanyaan:**

a. Nyatakan $B$ dengan enumerasi.
b. Nyatakan $A$ dengan notasi pembentuk himpunan.
c. Hitung $|A \cup B|$.

### Soal 2 — Analitik Lalu Lintas Web

Log User ID yang mengakses modul pembayaran:

```text
[1102, 1105, 1102, 1103, 1108, 1105, 1102, 1109, 1110, 1103,
 1102, 1112, 1115, 1108, 1110, 1112, 1105, 1102, 1118, 1109,
 1103, 1108, 1112, 1120, 1105, 1102, 1115, 1108, 1103, 1112]
```

**Pertanyaan:**

a. Tuliskan himpunan User ID unik (hilangkan duplikasi).
b. Jika $K$ = User ID kelipatan 5 dan $G$ = User ID ganjil, tentukan $K \cap G$ dan $K \cup G$.
c. Hitung jumlah User ID yang **bukan** kelipatan 5 dan **bukan** ganjil.

### Soal 3 — Login Multi-platform

Diketahui:

- $|W| = 120$ · $|A| = 85$ · $|I| = 60$
- $|W \cap A| = 40$ · $|W \cap I| = 25$ · $|A \cap I| = 20$
- $|W \cap A \cap I| = 10$ · $|U| = 200$

**Pertanyaan:**

a. Hitung pengguna aktif di minimal satu platform.
b. Hitung pengguna yang tidak aktif di platform manapun.
c. Hitung pengguna yang aktif **hanya di Web**.

> **Rumus:** $|W \cup A \cup I| = |W| + |A| + |I| - |W \cap A| - |W \cap I| - |A \cap I| + |W \cap A \cap I|$

### Soal 4 — Rekomendasi Produk

Data dari 300 pelanggan:

- Elektronik ($E$) = 180 · Fashion ($F$) = 150 · Rumah Tangga ($R$) = 120
- $E \cap F = 60$ · $E \cap R = 50$ · $F \cap R = 40$
- $E \cap F \cap R = 20$

**Pertanyaan:**

a. Hitung pelanggan yang melihat **hanya Elektronik**.
b. Hitung pelanggan yang melihat **tepat dua kategori**.
c. Hitung pelanggan yang **tidak melihat satupun** kategori.

### Soal 5 — Penilaian Kinerja (Fuzzy Set)

| Karyawan | Nilai | $\mu$ |
| -------- | :---: | :---: |
| Andi     |  95   |  1.0  |
| Budi     |  85   |  0.8  |
| Citra    |  75   |  0.5  |
| Dewi     |  60   |  0.2  |
| Eko      |  45   |  0.0  |

**Pertanyaan:**

a. Jelaskan perbedaan himpunan klasik dan fuzzy.
b. Tentukan $\alpha$-cut untuk $\alpha = 0.5$.
c. Siapa yang berhak bonus jika syaratnya $\mu \geq 0.7$?

## Konsep Kunci

**Operasi dasar:**

| Operasi   | Notasi          | Arti                            |
| --------- | --------------- | ------------------------------- |
| Gabungan  | $A \cup B$      | Elemen di $A$ atau $B$          |
| Irisan    | $A \cap B$      | Elemen di $A$ dan $B$           |
| Selisih   | $A - B$         | Elemen di $A$, bukan di $B$     |
| Komplemen | $U \setminus A$ | Elemen di semesta, bukan di $A$ |

**Inklusi-eksklusi 3 himpunan:**
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$$

**Fuzzy set:**

- **Derajat keanggotaan** $\mu(x) \in [0,1]$.
- **$\alpha$-cut** = $\{x \mid \mu(x) \geq \alpha\}$.

## Referensi

- Munir, R. _Matematika Diskrit_. Informatika, 2012.
- Epp, S. _Discrete Mathematics with Applications_, 4th ed.
- Rosen, K. H. _Discrete Mathematics and Its Applications_.
- [E-Learning IF Polibatam](https://learningif.polibatam.ac.id)

## Format Pengumpulan

::: warning Wajib

- **Bentuk:** PPT atau PDF
- **Panjang:** 1 halaman ringkasan
- **Isi:** Identitas kelompok, jawaban 5 soal, langkah pengerjaan
- **Pengumpulan:** e-learning IF Polibatam
- **Presentasi:** Pertemuan berikutnya

:::

## Tips

- Kerjakan berurutan: Soal 1–2 pemanasan, 3–4 menantang, 5 paling sulit.
- Gambar diagram Venn untuk Soal 3 & 4.
- Tulis langkah, bukan hanya jawaban akhir.
- Cek ulang dengan cara berbeda.

## Info Tugas

| Field           | Value                          |
| --------------- | ------------------------------ |
| **Mata Kuliah** | RPL103 — Matematika Diskrit    |
| **Dosen**       | Supardianto                    |
| **Tipe**        | Kelompok (2–3 orang / Tim PBL) |
| **Luaran**      | PPT / PDF 1 halaman            |
| **Presentasi**  | Pertemuan berikutnya           |

## Halaman Terkait

| Halaman                                                      | Deskripsi                |
| ------------------------------------------------------------ | ------------------------ |
| [Daftar Tugas](/v1/task/)                                    | Semua tugas semester ini |
| [Matematika Diskrit](/v1/courses/rpl103-matematika-diskrit/) | Materi lengkap RPL103    |
