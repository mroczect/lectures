Berikut adalah ringkasan jawaban untuk **Tugas 1** disertai dengan alasan dan penjelasan lengkap yang dirancang agar mudah dipahami dan siap untuk disalin ke dalam slide presentasi (PPT/PDF).

---

# Jawaban Tugas 1: Operasi Himpunan pada Katalog E-Commerce

## 1. Nyatakan himpunan `B` dengan cara Enumerasi!

**Jawaban:**
`B = {102, 105, 108, 111, 114}`

**Alasan & Penjelasan:**
Enumerasi berarti kita harus mendaftar semua anggota himpunan secara eksplisit (satu per satu). Berdasarkan syarat pada soal, anggota himpunan B harus memenuhi tiga kriteria sekaligus:

1. Merupakan bilangan bulat.
2. Bernilai antara 100 dan 115 (inklusif/biasa termasuk 100 dan 115).
3. Habis dibagi 3.

Jika kita membagi 100 dengan 3, sisanya adalah 1. Artinya, bilangan bulat pertama yang habis dibagi 3 di atas 100 adalah **102** (yaitu 3 x 34). Selanjutnya, kita hanya perlu menjumlahkan dengan 3 berturut-turut hingga mencapai batas 115:

- 102 (valid)
- 105 (valid)
- 108 (valid)
- 111 (valid)
- 114 (valid)
- 117 (Tidak valid, karena melebihi batas 115).
  Maka, hasil enumerasinya adalah `{102, 105, 108, 111, 114}`.

---

## 2. Nyatakan himpunan `A` menggunakan Notasi Pembentuk Himpunan (rule-based)!

**Jawaban:**
`A = {x | x adalah bilangan bulat, 100 ≤ x ≤ 115, dan x merupakan ID Produk Terlaris}`

**Alasan & Penjelasan:**
Notasi pembentuk himpunan (rule-based/set-builder notation) tidak menuliskan elemennya satu per satu, melainkan menggunakan aturan/syarat yang harus dipenuhi oleh anggota himpunan tersebut.
Diketahui dari soal bahwa `A = {101, 102, 105, 108, 112}`. Jika kita perhatikan angka-angka tersebut:

- Semuanya adalah bilangan bulat.
- Semuanya berada di rentang 100 hingga 115.
- Pola selisihnya tidak konsisten (101 ke 102 selisih 1, 102 ke 105 selisih 3, dst). Karena tidak ada pola matematis (seperti kelipatan bilangan tertentu), cara paling tepat untuk membuat aturannya adalah dengan membatasi rentang nilainya dan mendefinisikan atribut bisnisnya (yaitu "merupakan ID Produk Terlaris"). Ini sangat lazim dilakukan dalam konteks sistem basis data.

---

## 3. Hitung nilai kardinalitas array untuk menyimpan seluruh produk unik dari gabungan Kategori A dan B!

**Jawaban:**
Kardinalitas = **7**

**Alasan & Penjelasan:**
Untuk membuat struktur data array yang berisi produk unik dari gabungan dua kategori, kita menggunakan operasi **Union (Gabungan)**, dilambangkan dengan `A ∪ B`.

Langkah penyelesaian:

1. **Himpunan A:** {101, 102, 105, 108, 112}
2. **Himpunan B:** {102, 105, 108, 111, 114}
3. Gabungan (A ∪ B) artinya kita menggabungkan kedua himpunan tersebut, tetapi elemen yang sama (irisan) hanya ditulis satu kali. Irisan kedua himpunan ini adalah {102, 105, 108}.

Maka, himpunan gabungannya adalah:
`A ∪ B = {101, 102, 105, 108, 112, 111, 114}`

Secara matematis, kita juga bisa menggunakan rumus Inklusi-Eksklusi untuk 2 himpunan:
`|A ∪ B| = |A| + |B| - |A ∩ B|`
`|A ∪ B| = 5 + 5 - 3 = 7`

Karena jumlah elemen unik di dalam himpunan gabungan ada 7 angka, maka pengembang sistem (back-end) harus membuat array dengan ukuran/kapasitas **7** untuk menyimpan ID produk tersebut secara optimal tanpa ada data yang ganda/duplikat.

---

_Catatan untuk Presentasi: Anda bisa mengekstrak poin-poin "Jawaban" di atas sebagai teks utama di slide PPT, dan menggunakan poin "Alasan & Penjelasan" sebagai naskah/skrip saat Anda berbicara di depan kelas._
