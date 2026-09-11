.. _notasi-himpunan:

=================
Notasi Himpunan
=================

.. contents:: Daftar Isi
   :depth: 2
   :local:

Pengantar
=========

Ada beberapa cara untuk **menyajikan** atau **menuliskan** sebuah himpunan.
Pemilihan cara bergantung pada sifat himpunan dan tujuan penyajiannya. Dalam
konteks pemrograman, cara penyajian himpunan sangat menentukan bagaimana data
disimpan, diproses, dan dioptimalkan.

Secara umum, terdapat empat cara penyajian himpunan:

1. **Enumerasi** — menuliskan seluruh elemen.
2. **Simbol baku** — memakai notasi standar matematika.
3. **Notasi pembentuk himpunan** — menuliskan syarat keanggotaan.
4. **Diagram Venn** — menyajikan secara grafis.

.. admonition:: Driving Question
   :class: tip

   Jika sebuah aplikasi e-commerce memiliki daftar produk elektronik,
   fashion, dan makanan, bagaimana cara paling efektif menyajikan himpunan
   produk tersebut agar mudah diproses dalam program komputer?

   Produk dapat disajikan sebagai:

   - **Daftar eksplisit (list/array):**
     ``Elektronik = {Laptop, HP, TV}``
   - **Deskripsi (rule-based):**
     ``Elektronik = {x | x adalah produk dengan kategori "elektronik"}``

   Apakah dengan penyajian ini, program dapat dengan mudah memproses data
   produk untuk pencarian, filter, atau rekomendasi?

Peta Konsep
===========

.. code-block:: text

   NOTASI HIMPUNAN
   │
   ├── 1. Enumerasi
   │     └── Menuliskan semua elemen
   │
   ├── 2. Simbol Baku
   │     └── ℕ, ℤ, ℚ, ℝ, ℂ
   │
   ├── 3. Notasi Pembentuk Himpunan
   │     └── {x | syarat yang harus dipenuhi}
   │
   └── 4. Diagram Venn
         └── Visualisasi grafis

   Perbandingan:
   ┌─────────────┬──────────────┬───────────────┐
   │ Cara        │ Cocok Untuk  │ Sifat         │
   ├─────────────┼──────────────┼───────────────┤
   │ Enumerasi   │ Himpunan kecil│ Eksplisit    │
   │ Simbol baku │ Bilangan     │ Ringkas       │
   │ Pembentuk   │ Himpunan besar│ Rule-based   │
   │ Venn        │ Presentasi   │ Visual        │
   └─────────────┴──────────────┴───────────────┘

1. Enumerasi
============

**Enumerasi** adalah cara menyajikan himpunan dengan menuliskan **semua
elemen** himpunan tersebut di antara dua kurung kurawal.

Cocok dipakai jika:

- Himpunan **berukuran kecil** (tidak terlalu banyak elemen).
- Elemen-elemennya **mudah didaftarkan** satu per satu.

Format
------

.. math::

   A = \{a_1, a_2, a_3, \dots, a_n\}

Contoh
------

- ``H = {GET, POST, PUT, DELETE}``
- ``A = {1, 2, 3, 4, 5}``
- ``V = {a, i, u, e, o}``
- ``W = {merah, kuning, hijau}``

Contoh di Pemrograman
---------------------

Dalam Python, enumerasi setara dengan ``set`` atau ``list``:

.. code-block:: python

   # Enumerasi himpunan metode HTTP
   http_methods = {"GET", "POST", "PUT", "DELETE"}

   # Enumerasi himpunan vokal
   vokal = {"a", "i", "u", "e", "o"}

.. note::

   Enumerasi tidak efisien untuk himpunan besar. Untuk himpunan dengan
   aturan keanggotaan yang jelas, gunakan **notasi pembentuk himpunan**.

2. Simbol Baku
==============

Terdapat sejumlah **simbol baku** yang biasa dipakai untuk mendefinisikan
himpunan bilangan yang sering digunakan. Simbol ini sudah disepakati secara
internasional.

Daftar Simbol Baku
------------------

.. list-table::
   :name: tbl-simbol-baku
   :header-rows: 1
   :widths: 15 25 60

   * - Simbol
     - Nama
     - Definisi
   * - :math:`\mathbb{N}`
     - Bilangan asli
     - :math:`\{1, 2, 3, \dots\}`
   * - :math:`\mathbb{Z}`
     - Bilangan bulat
     - :math:`\{\dots, -2, -1, 0, 1, 2, \dots\}`
   * - :math:`\mathbb{Q}`
     - Bilangan rasional
     - :math:`\{p/q \mid p, q \in \mathbb{Z}, q \neq 0\}`
   * - :math:`\mathbb{R}`
     - Bilangan riil
     - Gabungan bilangan rasional dan irasional
   * - :math:`\mathbb{C}`
     - Bilangan kompleks
     - :math:`\{a + bi \mid a, b \in \mathbb{R}\}`

.. note::

   Beberapa buku menuliskan :math:`\mathbb{N}` dimulai dari 0, sehingga
   :math:`\mathbb{N} = \{0, 1, 2, \dots\}`. Selalu cek konvensi yang dipakai
   di buku referensi Anda.

Contoh Penggunaan
-----------------

- ``x ∈ ℤ`` → ``x`` adalah bilangan bulat.
- ``n ∈ ℕ`` → ``n`` adalah bilangan asli (bilangan bulat positif).
- ``r ∈ ℚ`` → ``r`` dapat ditulis sebagai pecahan ``p/q``.
- ``z ∈ ℂ`` → ``z`` adalah bilangan kompleks.

Kapan Dipakai
-------------

Simbol baku dipakai jika himpunan yang dimaksud adalah **himpunan bilangan
standar**. Simbol ini mempersingkat penulisan dan menghindari kebingungan.

3. Notasi Pembentuk Himpunan
============================

**Notasi pembentuk himpunan** (*set-builder notation*) adalah cara menyajikan
himpunan dengan menuliskan **syarat** yang harus dipenuhi oleh anggotanya.

Format
------

.. math::

   A = \{x \mid \text{syarat yang harus dipenuhi oleh } x\}

Aturan Penulisan Syarat Keanggotaan
-----------------------------------

1. Bagian **kiri** tanda ``|`` melambangkan **elemen** himpunan.
2. Tanda ``|`` dibaca **"dimana"** atau **"sedemikian sehingga"**.
3. Bagian **kanan** tanda ``|`` menunjukkan **syarat keanggotaan**.
4. Setiap tanda **koma** (``,``) di dalam syarat dibaca **"dan"**.

Contoh
------

**Contoh 1** — himpunan nomor port jaringan yang kurang dari 1024:

.. math::

   P = \{x \mid x \text{ adalah nomor port jaringan}, x < 1024\}

**Contoh 2** — himpunan bilangan genap positif:

.. math::

   G = \{x \mid x \in \mathbb{N}, x \text{ habis dibagi } 2\}

**Contoh 3** — himpunan pengguna dengan usia tertentu:

.. math::

   U = \{u \mid u \text{ adalah pengguna aplikasi}, u.\text{usia} \geq 18\}

**Contoh 4** — himpunan produk kategori elektronik:

.. math::

   E = \{p \mid p \text{ adalah produk dengan kategori "elektronik"}\}

Kapan Dipakai
-------------

Notasi pembentuk himpunan dipakai jika:

- Himpunan **berukuran besar** atau **tak hingga**.
- Elemen-elemennya **mengikuti aturan** tertentu.
- Lebih ringkas menjelaskan **syarat** daripada menuliskan satu per satu.

.. note::

   Dalam pemrograman, notasi pembentuk himpunan setara dengan **comprehension**
   atau **filter/predicate**.

   .. code-block:: python

      # Himpunan bilangan genap positif
      genap = {x for x in range(1, 100) if x % 2 == 0}

      # Himpunan pengguna dengan usia >= 18
      dewasa = {u for u in users if u.usia >= 18}

4. Diagram Venn
===============

**Diagram Venn** menyajikan himpunan secara **grafis**. Setiap himpunan
digambarkan sebagai lingkaran atau elips di dalam **semesta pembicaraan**
(*universal set*).

Komponen Diagram Venn
---------------------

- **Lingkaran/elips** → merepresentasikan himpunan.
- **Persegi panjang** → merepresentasikan semesta pembicaraan ``S`` atau
  ``U``.
- **Titik/label** → merepresentasikan elemen.
- **Irisan** → area yang bertumpuk menunjukkan elemen yang sama.

Contoh
------

Misalkan:

- ``Soccer = {alex, casey, drew, hunter}``
- ``Tennis = {casey, drew, jade}``

Diagram Venn-nya:

.. code-block:: text

   +---------------------------------+
   |            S (Semesta)          |
   |                                 |
   |    +--------+  +--------+       |
   |   / Soccer   \/  Tennis  \      |
   |  |  alex    |casey|  jade |     |
   |  |  hunter  |drew |       |     |
   |   \        / \     /             |
   |    +--------+  +--------+        |
   |                                 |
   +---------------------------------+

Elemen yang berada di **irisan** (``casey``, ``drew``) adalah anggota kedua
himpunan. Elemen ``alex`` dan ``hunter`` hanya ada di *Soccer*, sedangkan
``jade`` hanya ada di *Tennis*.

Kapan Dipakai
-------------

Diagram Venn dipakai jika:

- Perlu memperlihatkan **relasi antar himpunan** secara visual.
- Perlu menjelaskan **irisan, gabungan, atau selisih**.
- Tujuannya **presentasi** atau **edukasi**, bukan komputasi.

.. warning::

   Diagram Venn **tidak efisien** untuk himpunan besar atau berdimensi
   tinggi. Untuk komputasi, gunakan notasi himpunan atau struktur data.

Perbandingan Empat Cara
=======================

.. list-table::
   :name: tbl-perbandingan-notasi
   :header-rows: 1
   :widths: 20 25 25 30

   * - Cara
     - Kelebihan
     - Kekurangan
     - Cocok Untuk
   * - Enumerasi
     - Eksplisit, mudah dibaca
     - Tidak efisien untuk himpunan besar
     - Himpunan kecil dengan elemen terbatas
   * - Simbol baku
     - Ringkas, standar
     - Terbatas pada himpunan bilangan
     - Himpunan bilangan ``ℕ``, ``ℤ``, ``ℚ``, ``ℝ``, ``ℂ``
   * - Notasi pembentuk
     - Ringkas, fleksibel
     - Perlu pemahaman aturan
     - Himpunan besar atau tak hingga
   * - Diagram Venn
     - Visual, intuitif
     - Tidak cocok untuk komputasi
     - Presentasi dan edukasi

Contoh Terpadu
==============

Diberikan permasalahan dari sistem *back-end* e-commerce:

- Kategori A (Produk Terlaris):
  ``A = {101, 102, 105, 108, 112}``
- Kategori B (Produk Promo Flash Sale):
  ``B = {x | x bilangan bulat, 100 ≤ x ≤ 115, dan x habis dibagi 3}``

Penyelesaian
------------

**Langkah 1** — Nyatakan B dengan enumerasi.

Bilangan bulat antara 100 dan 115 yang habis dibagi 3:

``102, 105, 108, 111, 114``

Jadi:

.. math::

   B = \{102, 105, 108, 111, 114\}

**Langkah 2** — Nyatakan A dengan notasi pembentuk himpunan.

.. math::

   A = \{x \mid x \in \{101, 102, 105, 108, 112\}\}

atau lebih deskriptif:

.. math::

   A = \{x \mid x \text{ adalah ID produk terlaris}\}

**Langkah 3** — Hitung kardinalitas gabungan.

.. math::

   A \cup B = \{101, 102, 105, 108, 111, 112, 114\}

.. math::

   |A \cup B| = 7

Implementasi Python
===================

Enumerasi dengan ``set``
------------------------

.. code-block:: python

   # Enumerasi himpunan metode HTTP
   http_methods = {"GET", "POST", "PUT", "DELETE"}
   print(http_methods)

Simbol Baku dalam Konteks Bilangan
----------------------------------

.. code-block:: python

   # ℕ: bilangan asli (1, 2, 3, ...)
   asli = {1, 2, 3, 4, 5}

   # ℤ: bilangan bulat
   bulat = {-2, -1, 0, 1, 2}

   # ℚ: bilangan rasional (contoh)
   rasional = {1/2, 3/4, 5/3}

   # ℝ: bilangan riil (contoh)
   riil = {1.5, 3.14, 2.718}

Notasi Pembentuk sebagai Comprehension
--------------------------------------

.. code-block:: python

   # Notasi pembentuk: {x | x ∈ ℕ, x habis dibagi 2}
   genap = {x for x in range(1, 101) if x % 2 == 0}

   # Notasi pembentuk: {x | x ∈ ℤ, -10 ≤ x ≤ 10, x < 0}
   negatif = {x for x in range(-10, 11) if x < 0}

   # Notasi pembentuk: {u | u pengguna, u.umur ≥ 18}
   # dengan asumsi `users` adalah daftar objek pengguna
   dewasa = {u for u in users if u.umur >= 18}

Filter Produk dengan Notasi Pembentuk
-------------------------------------

.. code-block:: python

   produk = [
       {"id": 101, "nama": "Laptop", "kategori": "elektronik", "stok": 5},
       {"id": 102, "nama": "HP",     "kategori": "elektronik", "stok": 20},
       {"id": 103, "nama": "Kaos",   "kategori": "fashion",    "stok": 100},
       {"id": 104, "nama": "TV",     "kategori": "elektronik", "stok": 3},
   ]

   # {p | p produk, p.kategori = "elektronik"}
   elektronik = {p["nama"] for p in produk if p["kategori"] == "elektronik"}
   print(elektronik)   # {'Laptop', 'HP', 'TV'}

   # {p | p produk, p.stok < 10}
   stok_kritis = {p["nama"] for p in produk if p["stok"] < 10}
   print(stok_kritis)  # {'Laptop', 'TV'}

Aplikasi di RPL
===============

.. list-table::
   :header-rows: 1

   * - Cara
     - Contoh di RPL
   * - Enumerasi
     - Himpunan metode HTTP, himpunan status code, himpunan role
   * - Simbol baku
     - Tipe data numerik: integer (ℤ), float (ℝ), complex (ℂ)
   * - Notasi pembentuk
     - Query filter, comprehension, predicate di ORM
   * - Diagram Venn
     - Dokumentasi relasi antar tabel, visualisasi role/permission

Contoh Query SQL sebagai Notasi Pembentuk
-----------------------------------------

.. code-block:: sql

   -- {u | u pengguna, u.umur >= 18}
   SELECT *
   FROM users
   WHERE umur >= 18;

   -- {p | p produk, p.stok < 10, p.kategori = 'elektronik'}
   SELECT *
   FROM produk
   WHERE stok < 10 AND kategori = 'elektronik';

Kesalahan Umum
==============

1. **Menganggap ``{ }`` adalah notasi pembentuk**

   ``{ }`` adalah himpunan kosong, bukan notasi pembentuk. Notasi
   pembentuk harus memiliki ``x | syarat``.

2. **Menuliskan notasi pembentuk tanpa elemen**

   Salah: ``{ | x > 5}``
   Benar: ``{x | x > 5}``

3. **Menggunakan koma sebagai "atau"**

   Dalam notasi pembentuk, koma dibaca **"dan"**, bukan **"atau"**.

   .. math::

      \{x \mid x > 0, x < 10\}

   Artinya ``x`` lebih dari 0 **dan** kurang dari 10.

4. **Menganggap ``ℕ`` selalu sama di semua buku**

   Beberapa buku memulai ``ℕ`` dari 0, yang lain dari 1. Selalu cek
   referensi.

5. **Menggunakan Diagram Venn untuk komputasi**

   Diagram Venn hanya untuk visualisasi. Untuk komputasi, gunakan notasi
   himpunan, struktur data, atau query.

Latihan
=======

Level 1 — Pemahaman Dasar
-------------------------

**Latihan 1** — Enumerasi

Diketahui ``A = {x | x bilangan prima < 20}``. Nyatakan ``A`` dengan
enumerasi dan tentukan ``|A|``.

**Jawaban:**

.. math::

   A = \{2, 3, 5, 7, 11, 13, 17, 19\}, \quad |A| = 8

**Latihan 2** — Simbol baku

Tentukan simbol baku yang tepat untuk himpunan berikut:

a. Himpunan bilangan cacah.
b. Himpunan bilangan rasional.
c. Himpunan bilangan kompleks.

**Jawaban:**

a. Bilangan cacah: ``{0, 1, 2, 3, ...}`` — sering dinotasikan ``ℕ₀``
   atau ``ℕ`` tergantung konvensi.
b. ``ℚ``
c. ``ℂ``

Level 2 — Manipulasi
--------------------

**Latihan 3** — Notasi pembentuk

Nyatakan himpunan berikut dengan notasi pembentuk:

a. Himpunan bilangan bulat kelipatan 5.
b. Himpunan pengguna dengan saldo ≥ 100.000.
c. Himpunan produk dengan stok < 10.

**Jawaban:**

a. :math:`\{x \mid x \in \mathbb{Z}, x \text{ habis dibagi } 5\}`
b. :math:`\{u \mid u \text{ pengguna}, u.\text{saldo} \geq 100000\}`
c. :math:`\{p \mid p \text{ produk}, p.\text{stok} < 10\}`

**Latihan 4** — Konversi notasi

Diketahui ``P = {2, 3, 5, 7, 11, 13}``. Nyatakan ``P`` dengan:

a. Enumerasi (sudah diberikan).
b. Notasi pembentuk himpunan.

**Jawaban:**

.. math::

   P = \{x \mid x \text{ bilangan prima}, x < 15\}

Level 3 — Aplikasi
------------------

**Latihan 5** — Diagram Venn

Gambarkan diagram Venn untuk:

- ``A = {1, 2, 3, 4}``
- ``B = {3, 4, 5, 6}``

Tentukan ``A ∩ B`` dan ``A ∪ B``.

**Jawaban:**

.. code-block:: text

   +-------------------------------+
   |           S                   |
   |    +--------+  +--------+     |
   |   /    A     \/    B     \    |
   |  | 1, 2   | 3, 4 | 5, 6  |   |
   |   \        / \        /       |
   |    +--------+  +--------+     |
   +-------------------------------+

.. math::

   A \cap B = \{3, 4\}, \quad A \cup B = \{1, 2, 3, 4, 5, 6\}

**Latihan 6** — E-commerce

Diketahui:

- ``Elektronik = {101, 102, 105, 108}``
- ``Fashion = {102, 103, 104, 108, 110}``

a. Tentukan irisan produk yang ada di kedua kategori.
b. Tentukan gabungan semua produk.
c. Tentukan produk yang hanya ada di Elektronik.

**Jawaban:**

a. ``Elektronik ∩ Fashion = {102, 108}``
b. ``Elektronik ∪ Fashion = {101, 102, 103, 104, 105, 108, 110}``
c. ``Elektronik − Fashion = {101, 105}``

Level 4 — Analisis
------------------

**Latihan 7** — Konversi ke Python

Diberikan notasi pembentuk:

.. math::

   S = \{x \mid x \in \mathbb{N}, 10 \leq x \leq 20, x \text{ habis dibagi } 3\}

a. Tentukan ``S`` dengan enumerasi.
b. Tuliskan kode Python yang merepresentasikan ``S``.

**Jawaban:**

a. ``S = {12, 15, 18}``
b. Kode Python:

.. code-block:: python

   S = {x for x in range(10, 21) if x % 3 == 0}
   print(S)   # {12, 15, 18}

**Latihan 8** — Analisis

Mengapa notasi pembentuk himpunan lebih cocok untuk himpunan tak hingga
daripada enumerasi? Jelaskan.

**Jawaban:**

Karena himpunan tak hingga tidak dapat didaftarkan seluruh elemennya satu
per satu. Notasi pembentuk mendeskripsikan himpunan melalui **syarat
keanggotaan**, sehingga himpunan tak hingga tetap dapat dinyatakan secara
ringkas dan jelas.

Ringkasan
=========

- Ada **empat cara** menyajikan himpunan: enumerasi, simbol baku, notasi
  pembentuk, dan diagram Venn.
- **Enumerasi** cocok untuk himpunan kecil.
- **Simbol baku** dipakai untuk himpunan bilangan standar.
- **Notasi pembentuk** cocok untuk himpunan besar atau tak hingga.
- **Diagram Venn** cocok untuk presentasi visual.
- Pemilihan cara bergantung pada **konteks** dan **tujuan penyajian**.

Ringkasan Visual
----------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────┐
   │                   NOTASI HIMPUNAN                       │
   ├──────────────────────────────────────────────────────────┤
   │                                                          │
   │  Enumerasi                                               │
   │  └── A = {1, 2, 3, 4, 5}                                 │
   │                                                          │
   │  Simbol Baku                                             │
   │  └── ℕ, ℤ, ℚ, ℝ, ℂ                                       │
   │                                                          │
   │  Notasi Pembentuk                                        │
   │  └── {x | syarat}                                        │
   │                                                          │
   │  Diagram Venn                                            │
   │  └── Visualisasi grafis                                  │
   │                                                          │
   │  Perbandingan:                                           │
   │  ┌─────────────┬──────────────┬──────────────┐           │
   │  │ Cara        │ Cocok Untuk  │ Sifat        │           │
   │  ├─────────────┼──────────────┼──────────────┤           │
   │  │ Enumerasi   │ Himpunan kecil│ Eksplisit   │           │
   │  │ Simbol baku │ Bilangan     │ Ringkas      │           │
   │  │ Pembentuk   │ Himpunan besar│ Rule-based  │           │
   │  │ Venn        │ Presentasi   │ Visual       │           │
   │  └─────────────┴──────────────┴──────────────┘           │
   │                                                          │
   └──────────────────────────────────────────────────────────┘

Referensi
=========

- Munir, R., *Matematika Diskrit*, Bandung, Informatika, 2012.
- Rosen, K. H., *Discrete Mathematics and Its Applications*, McGraw-Hill.
- Susanna S. Epp, *Discrete Mathematics with Applications*, 4th Edition,
  Brooks Cole, 2010.

Lanjutan
========

- :doc:`konsep_dasar_himpunan` — definisi himpunan dan elemen.
- :doc:`himpunan_khusus` — himpunan kosong, subset, dan himpunan kuasa.
- :doc:`relasi_antar_himpunan` — himpunan sama dan himpunan ekivalen.

Kesimpulan
==========

Modul **Notasi Himpunan** mengajarkan empat cara menyajikan himpunan:

1. **Enumerasi** — eksplisit, untuk himpunan kecil.
2. **Simbol baku** — ringkas, untuk himpunan bilangan standar.
3. **Notasi pembentuk** — rule-based, untuk himpunan besar atau tak hingga.
4. **Diagram Venn** — visual, untuk presentasi dan edukasi.

Pemilihan cara bergantung pada **konteks** dan **tujuan penyajian**.
Dalam pemrograman, notasi pembentuk setara dengan **comprehension**,
enumerasi setara dengan **literal set**, dan simbol baku setara dengan
**tipe data numerik**.

**Pesan kunci:**

> Himpunan dapat disajikan dengan cara yang berbeda, tetapi maknanya
> tetap sama. Pilihlah cara yang paling **efektif**, **efisien**, dan
> **mudah dipahami** sesuai konteks.
