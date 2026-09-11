==========================================
Pertemuan 1: Algoritma dan Pemrograman
==========================================

.. meta::
   :description: Materi pertemuan 1 mata kuliah Algoritma dan Pemrograman - Pengertian algoritma, pemrograman, IPO, struktur dasar algoritma, dan penulisan algoritma.
   :keywords: algoritma, pemrograman, Python, pseudocode, flowchart, sequence, selection, iteration

Pada pertemuan pertama ini, kita akan membangun fondasi berpikir komputasional.
Fokus utama adalah memahami **apa itu algoritma**, **bagaimana menuliskannya**,
serta **menerjemahkannya ke dalam program Python**. Kita juga akan mengenal
tiga struktur dasar algoritma yang menjadi pondasi semua program.

----------------------
Apa yang Akan Dipelajari?
----------------------

Setelah mengikuti pertemuan ini, mahasiswa diharapkan mampu:

- Memahami pengertian algoritma dan pemrograman.
- Memahami cara berpikir sistematis dalam menyelesaikan masalah.
- Mengidentifikasi komponen input, proses, dan output.
- Mengenal struktur dasar algoritma: *Sequence*, *Selection*, dan *Iteration*.
- Menulis algoritma dalam pseudocode.
- Menggambarkan algoritma dengan flowchart.
- Menerjemahkan algoritma ke program Python.
- Mengenali kesalahan dasar dalam program.

----------------------
Apa Itu Algoritma?
----------------------

**Algoritma** adalah urutan langkah yang **LOGIS**, **TERURUT**, dan
**SISTEMATIS** untuk menyelesaikan suatu masalah hingga **SELESAI**.

.. note::

   Algoritma tidak sama dengan program. Algoritma adalah **logika penyelesaian
   masalah**, sedangkan program adalah **implementasi algoritma** dalam bahasa
   pemrograman seperti Python.

**Contoh: Menghitung Luas Persegi Panjang**

1. Masukkan panjang.
2. Masukkan lebar.
3. Hitung luas = panjang × lebar.
4. Tampilkan luas.

**Perbedaan Algoritma dan Program**

+---------------------------------------+-----------------------------------------+
| Algoritma                             | Program                                 |
+=======================================+=========================================+
| Logika penyelesaian masalah           | Implementasi algoritma dalam bahasa     |
|                                       | pemrograman                             |
+---------------------------------------+-----------------------------------------+
| "Hitung luas = panjang × lebar"       | ``luas = panjang * lebar``              |
+---------------------------------------+-----------------------------------------+

Kesimpulan: Algoritma adalah **solusi logis**, sedangkan program adalah **cara
mengimplementasikannya**.

------------------------------
Ciri-Ciri Algoritma yang Baik
------------------------------

- **Input**: Memiliki 0 atau lebih masukan dari luar.
- **Output**: Menghasilkan minimal satu keluaran.
- **Definiteness**: Setiap instruksi jelas dan tidak ambigu.
- **Finiteness**: Memiliki titik berhenti yang pasti.
- **Effectiveness**: Setiap langkah dapat dilaksanakan secara efektif.

-------------------------------
Belajar Memprogram ≠ Sekadar Coding
-------------------------------

- **Belajar memprogram** berarti memahami masalah → menganalisis → menentukan
  solusi → menyusun algoritma.
- **Belajar bahasa pemrograman** berarti mempelajari sintaks, keyword, dan
  struktur bahasa.

Mulailah dari *"Masalahnya apa?"* — bukan *"Kode Python-nya apa?"*

-----------------------------------
Model IPO: Input – Proses – Output
-----------------------------------

Model IPO adalah dasar dari setiap program komputer.

.. list-table::
   :header-rows: 1
   :widths: 15 55 30

   * - Tahap
     - Deskripsi
     - Contoh pada Luas Persegi Panjang
   * - **INPUT**
     - Data yang diberikan ke program untuk diproses.
     - Panjang = 8, Lebar = 5
   * - **PROSES**
     - Langkah-langkah pengolahan data input menjadi hasil yang diinginkan.
     - Luas = Panjang × Lebar = 8 × 5 = 40
   * - **OUTPUT**
     - Hasil akhir yang dihasilkan program setelah proses selesai.
     - Luas = 40 satuan², ditampilkan ke pengguna.

------------------------------
Tiga Struktur Dasar Algoritma
------------------------------

1. **Sequence** : instruksi dijalankan secara berurutan dari atas ke bawah.
2. **Selection** : pengambilan keputusan berdasarkan kondisi tertentu (``if/else``).
3. **Iteration** : instruksi diulang selama kondisi terpenuhi (``for``/``while``).

-----------------------
Sequence dalam Python
-----------------------

Sequence adalah struktur di mana instruksi dijalankan secara berurutan dari
atas ke bawah, satu per satu tanpa ada percabangan.

.. code-block:: python

   nama = input("Nama: ")
   umur = int(input("Umur: "))
   print("Nama:", nama)
   print("Umur:", umur)

Alur eksekusi:

1. Masukkan nama.
2. Masukkan umur.
3. Tampilkan nama.
4. Tampilkan umur.

Setiap baris dieksekusi tepat satu kali, secara berurutan — itulah inti dari
struktur *Sequence*.

------------------------------
Selection: Pengambilan Keputusan
------------------------------

Struktur selection memungkinkan program mengambil keputusan berdasarkan kondisi
tertentu.

Contoh Python — Menentukan Kelulusan:

.. code-block:: python

   nilai = float(input("Nilai: "))
   if nilai >= 60:
       print("Lulus")
   else:
       print("Tidak Lulus")

Alur keputusan:

- Jika kondisi **BENAR** (nilai ≥ 60) → jalankan blok ``if`` → "Lulus".
- Jika kondisi **SALAH** (nilai < 60) → jalankan blok ``else`` → "Tidak Lulus".

Kata kunci: ``if``, ``elif``, ``else``. Struktur ini membentuk percabangan
(*branching*) dalam logika program.

-------------------------------
Iteration: Perulangan
-------------------------------

**For loop** — mengulang sejumlah kali yang diketahui:

.. code-block:: python

   for i in range(1, 6):
       print(i)

**While loop** — mengulang selama kondisi terpenuhi:

.. code-block:: python

   i = 1
   while i <= 5:
       print(i)
       i += 1

.. attention::

   Pertanyaan kunci: **Kapan perulangan berhenti?** Pastikan selalu ada kondisi
   berhenti (*finiteness*) agar program tidak berjalan selamanya.

------------------------------
Cara Menuliskan Algoritma
------------------------------

Ada tiga cara umum:

1. **Bahasa Natural** : menuliskan langkah-langkah dengan kalimat sehari-hari
   yang mudah dipahami.

   Contoh: *"Jika A lebih besar dari B, maka tampilkan A sebagai bilangan
   terbesar."*

2. **Pseudocode** : struktur mirip kode program tetapi bebas dari aturan bahasa
   pemrograman tertentu.

3. **Flowchart** : representasi visual alur algoritma menggunakan simbol-simbol
   standar (oval untuk start/end, persegi untuk proses, belah ketupat untuk
   keputusan, dll).

-----------------------
Pseudocode
-----------------------

Pseudocode adalah struktur penulisan yang menyerupai kode program, namun bebas
dari aturan bahasa pemrograman tertentu. Pseudocode berfungsi sebagai jembatan
antara algoritma dan program Python.

Contoh — Menentukan Bilangan Terbesar:

.. code-block:: text

   INPUT A
   INPUT B
   IF A > B THEN
       OUTPUT A
   ELSE
       OUTPUT B

Implementasi Python:

.. code-block:: python

   a = int(input("A: "))
   b = int(input("B: "))
   if a > b:
       print(a)
   else:
       print(b)

Pseudocode memudahkan perancangan logika sebelum menulis kode sesungguhnya.

-----------------------
Simbol-Simbol Flowchart
-----------------------

Berikut simbol-simbol dasar yang digunakan dalam flowchart:

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Simbol
     - Nama
     - Fungsi
   * - Oval / Ellipse
     - Terminator
     - Mulai / Selesai
   * - Persegi Panjang
     - Proses
     - Menyatakan proses/perhitungan
   * - Jajaran Genjang
     - Input/Output
     - Membaca data / menampilkan hasil
   * - Belah Ketupat
     - Decision
     - Percabangan / kondisi
   * - Panah
     - Aliran (Flow)
     - Menghubungkan antar simbol

------------------------------
Contoh Lengkap: Luas Persegi Panjang
------------------------------

**Pseudocode:**

.. code-block:: text

   INPUT panjang
   INPUT lebar
   luas ← panjang × lebar
   OUTPUT luas

**Flowchart Luas Persegi Panjang:**

.. mermaid::

   flowchart TD
       A[Mulai] --> B[Input panjang]
       B --> C[Input lebar]
       C --> D[luas = panjang * lebar]
       D --> E[Output luas]
       E --> F[Selesai]

**Python Code:**

.. code-block:: python

   panjang = float(input("Panjang: "))
   lebar = float(input("Lebar: "))
   luas = panjang * lebar
   print("Luas:", luas)

Ketiga bentuk (flowchart, pseudocode, Python) merepresentasikan logika yang
sama — algoritma adalah fondasinya.

------------------------------
Mengapa Python?
------------------------------

Python adalah bahasa pemrograman tingkat tinggi yang mudah dibaca dan dipahami.
Dalam mata kuliah ini, Python digunakan untuk:

- Menerjemahkan algoritma menjadi program nyata.
- Melatih logika dan kemampuan berpikir sistematis.
- Membuat program yang menyelesaikan masalah.
- Menguji solusi secara langsung.

Contoh sederhana: ``print("Hello World!")`` — satu baris kode, langsung
berjalan. Python memungkinkan kita fokus pada **logika**, bukan kompleksitas
sintaks.

------------------------------
Dari Algoritma Menjadi Program Python
------------------------------

.. list-table::
   :widths: 5 45 50
   :class: algorithm-steps

   * - **Langkah 1**
     - **Pahami Masalah**
     - Baca dan analisis masalah dengan cermat. Tentukan input yang dibutuhkan
       dan output yang diharapkan sebelum mulai menulis kode.
   * - **Langkah 2**
     - **Susun Algoritma**
     - Rancang langkah-langkah logis penyelesaian masalah. Gunakan pseudocode
       atau flowchart sebagai jembatan antara masalah dan program.
   * - **Langkah 3**
     - **Implementasi Python**
     - Terjemahkan algoritma ke dalam kode Python. Pastikan setiap langkah
       algoritma tercermin dalam struktur program yang ditulis.
   * - **Langkah 4**
     - **Testing & Perbaiki**
     - Jalankan program dan uji dengan berbagai data. Identifikasi Syntax Error,
       Runtime Error, atau Logic Error, lalu perbaiki hingga solusi benar.

------------------------------
Testing, Debugging & Kesimpulan
------------------------------

- **Syntax Error** : kesalahan penulisan kode (misal tanda kurung tidak
  ditutup).
- **Runtime Error** : kesalahan saat program berjalan (misal pembagian dengan
  nol).
- **Logic Error** : program berjalan tetapi hasil tidak sesuai harapan (misal
  rumus salah).

.. tip::

   Program baik dimulai dari algoritma yang baik.
   **Problem → Algoritma → Python → Testing → Solusi**

------------------------------
Referensi
------------------------------

- Python 3 Tutorial Documentation: https://docs.python.org/3/tutorial/index.html
- Materi pembelajaran daring: http://learningif.polibatam.ac.id