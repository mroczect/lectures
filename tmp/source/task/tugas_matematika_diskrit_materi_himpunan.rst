Tugas Matematika Diskrit: Teori Himpunan
=========================================

Petunjuk Tugas
--------------

1. Baca materi tentang operasi himpunan, inklusi-eksklusi, dan fuzzy set dari sumber
   bacaan (buku referensi atau sumber lain) untuk menyelesaikan soal 3 - 5.
2. Diskusikan dalam kelompok kecil (2-3 orang) atau sesuai Tim PBL.
3. Siapkan ringkasan jawaban (1 halaman) dalam bentuk ppt atau pdf untuk
   dipresentasikan pada pertemuan berikutnya.

Tugas 1: Sistem Back-end E-commerce
-----------------------------------

Sebuah tim pengembang sedang merancang sistem back-end e-commerce. Sistem
menyimpan katalog ID produk digital yang diwakili oleh himpunan bilangan
bulat :math:`x`.

Kategori A (Produk Terlaris): Didefinisikan secara eksplisit
:math:`A=\{101,102,105,108,112\}`.

Kategori B (Produk Promo Flash Sale): Didefinisikan dengan syarat
:math:`B=\{x \mid x \text{ adalah bilangan bulat}, 100 \leq x \leq 115
\text{ dan } x \text{ habis dibagi } 3\}`.

Pertanyaan:

a. Nyatakan himpunan :math:`B` dengan cara Enumerasi!
b. Nyatakan himpunan :math:`A` menggunakan Notasi Pembentuk Himpunan
   (rule-based)!
c. Jika pengembang ingin membuat struktur data array untuk menyimpan
   seluruh produk unik dari gabungan Kategori A dan B, hitung nilai
   kardinalitasnya!

Tugas 2: Sistem Analitik Lalu Lintas Web
----------------------------------------

Sistem analitik lalu lintas web mencatat ID Pengguna (User ID) yang
melakukan aktivitas klik pada modul pembayaran selama 1 jam. Data log
mentah (array) yang terekam adalah sebagai berikut::

   Log = [USR01, USR05, USR02, USR01, USR03, USR05, USR01, USR04, USR02]

Pertanyaan:

a. Transformasikan data log mentah di atas menjadi sebuah Himpunan yang
   melambangkan himpunan pengguna unik (:math:`U`)!
b. Tentukan nilai kardinalitas dari himpunan :math:`U` tersebut!
c. Jelaskan secara singkat mengapa konsep kardinalitas himpunan penting
   dalam perhitungan Unique Active Users (UAU) dan optimasi penyimpanan
   basis data!

Tugas 3: Aplikasi Media Sosial
------------------------------

Sebuah aplikasi media sosial ingin menganalisis penggunanya. Data yang
tersedia:

- :math:`A` = Himpunan pengguna aktif di Instagram.
- :math:`B` = Himpunan pengguna aktif di TikTok.

Pertanyaan:

a. Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang
   aktif di kedua platform sekaligus.
b. Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang
   hanya aktif di salah satu platform saja.

Tugas 4: Analisis Data Langganan Pengguna
-----------------------------------------

Sebuah perusahaan menganalisis data langganan pengguna:

- :math:`|N| = 120` (Netflix)
- :math:`|D| = 80` (Disney+)
- :math:`|V| = 60` (Vidio)
- :math:`|N \cap D| = 40`
- :math:`|N \cap V| = 25`
- :math:`|D \cap V| = 15`
- :math:`|N \cap D \cap V| = 10`

Pertanyaan:

a. Hitung total jumlah pelanggan unik menggunakan Prinsip Inklusi-Eksklusi
   (:math:`|N \cup D \cup V|`).
b. Apa akibatnya jika kita hanya menjumlahkan total pelanggan
   (:math:`|N| + |D| + |V|`) tanpa memperhitungkan irisan? Jelaskan
   dampaknya terhadap analisis data!

Tugas 5: Sistem Rekomendasi Film
--------------------------------

Sebuah sistem rekomendasi film menilai preferensi pengguna dengan derajat
keanggotaan:

- Suka banget = 1
- Suka = 0.7
- Netral = 0.5
- Tidak suka = 0.2

Seorang pengguna memberikan penilaian:

- Film A = Suka (0.7)
- Film B = Netral (0.5)
- Film C = Suka banget (1)

Pertanyaan:

Bagaimana sistem menentukan urutan rekomendasi film dari yang paling
disukai? Mengapa himpunan fuzzy lebih cocok digunakan dibandingkan
himpunan klasik dalam kasus ini?

.. note::

   Tugas ini diraksakan untuk dinilai berdasarkan:

   - Ketepatan jawaban matematis (40%)
   - Kemampuan menerapkan konsep ke kasus nyata (30%)
   - Kualitas presentasi dan dokumentasi (30%)
