# Tugas Matematika Diskrit

**Jurusan Teknik Informatika**  
**Mata Kuliah:** Pengantar Matematika Diskrit dan Teori Himpunan

---

## Petunjuk Tugas

1. Baca materi tentang operasi himpunan, inklusi-eksklusi, dan fuzzy set dari sumber bacaan (buku referensi atau sumber lain) untuk menyelesaikan soal 3–5.
2. Diskusikan dalam kelompok kecil (2–3 orang) atau sesuai Tim PBL.
3. Siapkan ringkasan jawaban (1 halaman) dalam bentuk PPT atau PDF untuk dipresentasikan pada pertemuan berikutnya.

---

## Tugas 1

Sebuah tim pengembang sedang merancang sistem back-end e-commerce. Sistem menyimpan katalog ID produk digital yang diwakili oleh himpunan bilangan bulat `x`.

- **Kategori A (Produk Terlaris):** Didefinisikan secara eksplisit  
  `A = {101, 102, 105, 108, 112}`
- **Kategori B (Produk Promo Flash Sale):** Didefinisikan dengan syarat  
  `B = {x | x adalah bilangan bulat, 100 ≤ x ≤ 115, dan x habis dibagi 3}`

**Pertanyaan:**

1. Nyatakan himpunan `B` dengan cara Enumerasi!

Jawaban : {102, 105, 108, 111, 114}.

2. Nyatakan himpunan `A` menggunakan Notasi Pembentuk Himpunan (rule-based)!

Jawaban : A = {x | x adalah bilangan bulat, 100 ≤ x ≤ 115, dan x merupakan ID Produk Terlaris}

3. Jika pengembang ingin membuat struktur data array untuk menyimpan seluruh produk unik dari gabungan Kategori A dan B, hitung nilai kardinalitasnya!

jawaban :

Himpunan A: {101, 102, 105, 108, 112}
Himpunan B: {102, 105, 108, 111, 114}

X = {101,102,105,108,111,112,114}

---

## Tugas 2

Sistem analitik lalu lintas web mencatat ID Pengguna (User ID) yang melakukan aktivitas klik pada modul pembayaran selama 1 jam. Data log mentah (array) yang terekam adalah sebagai berikut:

```text
Log = USR01, USR05, USR02, USR01, USR03, USR05, USR01, USR04, USR02
```

**Pertanyaan:**

1. Transformasikan data log mentah di atas menjadi sebuah Himpunan yang melambangkan himpunan pengguna unik (`U`)!
2. Tentukan nilai kardinalitas dari himpunan `U` tersebut!
3. Jelaskan secara singkat mengapa konsep kardinalitas himpunan penting dalam perhitungan _Unique Active Users_ (UAU) dan optimasi penyimpanan basis data!

---

## Tugas 3

Sebuah aplikasi media sosial ingin menganalisis penggunanya. Data yang tersedia:

- `A` = Himpunan pengguna aktif di Instagram.
- `B` = Himpunan pengguna aktif di TikTok.

**Pertanyaan:**

1. Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang aktif di kedua platform sekaligus!
2. Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang hanya aktif di salah satu platform saja!

---

## Tugas 4

Sebuah perusahaan menganalisis data langganan pengguna:

```text
|N| = 120   (Netflix)
|D| = 80    (Disney+)
|V| = 60    (Vidio)
|N ∩ D| = 40
|N ∩ V| = 25
|D ∩ V| = 15
|N ∩ D ∩ V| = 10
```

**Pertanyaan:**

1. Hitung total jumlah pelanggan unik menggunakan Prinsip Inklusi-Eksklusi (`|N ∪ D ∪ V|`)!
2. Apa akibatnya jika kita hanya menjumlahkan total pelanggan (`|N| + |D| + |V|`) tanpa memperhitungkan irisan? Jelaskan dampaknya terhadap analisis data!

---

## Tugas 5

Sebuah sistem rekomendasi film menilai preferensi pengguna dengan derajat keanggotaan:

```text
Suka banget = 1
Suka        = 0,7
Netral      = 0,5
Tidak suka  = 0,2
```

Seorang pengguna memberikan penilaian:

- Film A = Suka (0,7)
- Film B = Netral (0,5)
- Film C = Suka banget (1)

**Pertanyaan:**

1. Bagaimana sistem menentukan urutan rekomendasi film dari yang paling disukai?
2. Mengapa himpunan fuzzy lebih cocok digunakan dibanding himpunan klasik dalam kasus ini?
