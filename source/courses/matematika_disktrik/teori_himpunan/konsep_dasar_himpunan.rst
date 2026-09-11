.. _konsep-dasar-himpunan:

=======================
Konsep Dasar Himpunan
=======================

.. contents:: Daftar Isi
   :depth: 2
   :local:

Pengantar
=========

**Himpunan** (*set*) adalah kumpulan objek-objek berbeda yang terdefinisi
dengan jelas. Objek yang berada di dalam himpunan disebut **elemen**,
**unsur**, atau **anggota**. Notasi himpunan menggunakan **kurung kurawal**
``{}``.

Analogi sederhana:

- Himpunan itu seperti **kotak berlabel**.
- Elemen itu seperti **isi kotak**.
- Label kotak adalah nama himpunan.
- Isi kotak adalah anggota himpunan.

.. note::

   Suatu kumpulan objek disebut **himpunan** jika memenuhi dua syarat:

   1. Objek-objeknya **berbeda** (tidak ada duplikasi).
   2. Objek-objeknya **terdefinisi dengan jelas** (*well-defined*), artinya
      kita dapat menentukan dengan pasti apakah suatu objek termasuk anggota
      atau bukan.

.. admonition:: Driving Question
   :class: tip

   Bagaimana konsep dasar himpunan dapat digunakan untuk memodelkan kumpulan
   data dalam sebuah sistem informasi mahasiswa?

   Misalkan:

   - ``TI`` = himpunan mahasiswa prodi Teknik Informatika
   - ``RPL`` = himpunan mahasiswa prodi Rekayasa Perangkat Lunak

   .. math::

      TI = \{Ani, Budi, Cici\}

      RPL = \{Dedi, Eko\}

   Apakah dengan merepresentasikan kelompok mahasiswa berdasarkan prodi,
   angkatan, atau kelasnya akan lebih memudahkan pengelolaan dalam sistem
   informasi?

Peta Konsep
===========

.. code-block:: text

   KONSEP DASAR HIMPUNAN
   │
   ├── Definisi & Syarat
   │     ├── Objek berbeda (tanpa duplikasi)
   │     └── Terdefinisi jelas (well-defined)
   │
   ├── Elemen & Keanggotaan
   │     ├── ∈ (anggota)
   │     └── ∉ (bukan anggota)
   │
   ├── Penulisan Himpunan
   │     ├── Enumerasi
   │     ├── Deskripsi
   │     ├── Notasi pembentuk
   │     └── Simbol baku (ℕ, ℤ, ℚ, ℝ, ℂ)
   │
   ├── Urutan & Duplikasi
   │     ├── Urutan tidak penting
   │     └── Duplikasi diabaikan
   │
   ├── Kardinalitas
   │     └── |A| = banyak elemen berbeda
   │
   ├── Himpunan Semesta & Kosong
   │     ├── S = himpunan semesta
   │     └── ∅ = himpunan kosong
   │
   ├── Diagram Venn
   │     └── Visualisasi himpunan
   │
   ├── Implementasi Python
   │     ├── set()
   │     ├── in / not in
   │     ├── len()
   │     └── operasi dasar
   │
   └── Aplikasi RPL
         ├── Basis data (unique users)
         ├── Analitik (UAU)
         ├── Keamanan (RBAC)
         └── Testing

Definisi Formal
===============

Secara matematis, himpunan dituliskan sebagai:

.. math::

   A = \{a_1, a_2, a_3, \dots, a_n\}

dengan:

- ``A`` = nama himpunan.
- ``a_1, a_2, \dots, a_n`` = elemen-elemen himpunan.
- ``{ }`` = kurung kurawal sebagai penanda himpunan.

Contoh
======

Himpunan dalam konteks umum:

- ``A = {1, 2, 3, 4, 5}``
- ``B = {a, i, u, e, o}``
- ``C = {merah, kuning, hijau}``

Himpunan dalam konteks rekayasa perangkat lunak:

- Himpunan *user* dalam sebuah aplikasi.
- Himpunan tabel dalam sebuah basis data.
- Himpunan mahasiswa Teknik Informatika Angkatan 2025.
- Himpunan metode HTTP: ``H = {GET, POST, PUT, DELETE}``.

Contoh yang Bukan Himpunan
==========================

Agar disebut himpunan, objeknya harus **terdefinisi dengan jelas**:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Bukan Himpunan
     - Alasan
   * - "Kumpulan mahasiswa yang pintar."
     - *Pintar* bersifat subjektif, tidak jelas batasnya.
   * - "Kumpulan bilangan kecil."
     - *Kecil* tidak jelas batasnya.
   * - "Kumpulan film yang menarik."
     - *Menarik* bersifat subjektif.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Himpunan
     - Alasan
   * - "Kumpulan mahasiswa dengan IPK ≥ 3,50."
     - Jelas dan terukur.
   * - "Kumpulan bilangan bulat kurang dari 10."
     - Jelas dan terdefinisi.
   * - "Kumpulan film dengan rating ≥ 8.0."
     - Jelas dan terukur.

Elemen Himpunan
===============

Notasi Keanggotaan
------------------

Untuk menyatakan bahwa ``x`` adalah elemen dari himpunan ``A``:

.. math::

   x \in A

Untuk menyatakan bahwa ``x`` **bukan** elemen dari ``A``:

.. math::

   x \notin A

Cara Membaca
------------

- ``x ∈ A`` dibaca: "x anggota A" atau "x elemen A".
- ``x ∉ A`` dibaca: "x bukan anggota A" atau "x tidak elemen A".

Contoh
------

Diketahui ``A = {1, 2, 3, 4, 5}``:

- ``1 ∈ A`` → benar
- ``3 ∈ A`` → benar
- ``6 ∉ A`` → benar
- ``0 ∉ A`` → benar

Diketahui ``H = {GET, POST, PUT, DELETE}``:

- ``GET ∈ H`` → benar
- ``PATCH ∉ H`` → benar

Penulisan Himpunan
==================

Ada empat cara umum untuk menuliskan himpunan.

1. Enumerasi (Tabulasi)
-----------------------

Semua elemen ditulis satu per satu.

.. math::

   A = \{1, 2, 3, 4, 5\}

2. Deskripsi
------------

Menuliskan aturan atau ciri-ciri elemennya.

.. math::

   B = \text{himpunan bilangan prima kurang dari 20}

3. Notasi Pembentuk Himpunan
----------------------------

Menuliskan syarat keanggotaan.

.. math::

   C = \{x \mid x \text{ bilangan prima}, x < 20\}

4. Simbol Baku
--------------

Menggunakan simbol yang sudah disepakati.

.. list-table::
   :header-rows: 1

   * - Simbol
     - Arti
   * - ``ℕ``
     - Himpunan bilangan asli
   * - ``ℤ``
     - Himpunan bilangan bulat
   * - ``ℚ``
     - Himpunan bilangan rasional
   * - ``ℝ``
     - Himpunan bilangan real
   * - ``ℂ``
     - Himpunan bilangan kompleks
   * - ``∅``
     - Himpunan kosong

.. warning::

   Perhatikan perbedaan berikut:

   - ``a`` → elemen (anggota) himpunan.
   - ``{a}`` → himpunan yang berisi satu elemen ``a``.

   ``a`` dan ``{a}`` adalah dua hal yang **berbeda**.

   .. math::

      a \in \{a\}, \quad \text{tetapi} \quad a \neq \{a\}

Urutan dan Duplikasi
====================

Dalam himpunan, berlaku dua aturan penting:

1. **Urutan tidak penting**

   .. math::

      \{1, 2, 3\} = \{3, 1, 2\} = \{2, 3, 1\}

2. **Duplikasi diabaikan**

   .. math::

      \{1, 1, 2, 2, 3\} = \{1, 2, 3\}

Artinya, himpunan hanya peduli pada **keberadaan** elemen, bukan pada
urutan atau pengulangannya.

Analogi
-------

Bayangkan himpunan seperti **kantong kelereng**:

- Urutan kelereng di dalam kantong tidak penting.
- Kelereng yang sama tidak dihitung dua kali.
- Yang penting adalah kelereng apa saja yang ada di dalam kantong.

Contoh Penerapan
----------------

Pada sistem analitik web, data log klik pengguna sering berisi duplikasi:

.. code-block:: text

   [USR01, USR05, USR02, USR01, USR03, USR05, USR01, USR04, USR02]

Jika diubah menjadi himpunan pengguna unik:

.. code-block:: text

   U = {USR01, USR02, USR03, USR04, USR05}

Maka ``|U| = 5``. Konsep ini menjadi dasar perhitungan **Unique Active
Users (UAU)** dalam analitik aplikasi.

Kardinalitas Himpunan
=====================

**Kardinalitas** himpunan ``A`` adalah banyaknya elemen berbeda di dalam
``A``. Notasinya:

.. math::

   n(A) \quad \text{atau} \quad |A|

Contoh
------

.. list-table::
   :header-rows: 1

   * - Himpunan
     - Kardinalitas
   * - ``A = {1, 2, 3, 4, 5}``
     - ``|A| = 5``
   * - ``B = {a, i, u, e, o}``
     - ``|B| = 5``
   * - ``C = {merah, kuning, hijau}``
     - ``|C| = 3``
   * - ``D = {2, 3, 5, 7, 11, 13, 17, 19}``
     - ``|D| = 8``

.. admonition:: Driving Question
   :class: tip

   Dalam sistem basis data pelanggan, bagaimana menghitung banyaknya elemen
   unik (*unique users*) dan apa dampaknya terhadap optimasi penyimpanan
   data?

   Setiap akun pengguna hanya boleh dihitung sekali meski login berkali-kali.
   Misalnya data login:

   .. code-block:: text

      {Ani, Budi, Ani, Cici, Budi}

   Kardinalitas = 3, yaitu ``{Ani, Budi, Cici}``.

   Dampaknya:

   - Menghindari duplikasi data.
   - Menghemat ruang penyimpanan.
   - Meningkatkan performa *query*.

Himpunan Semesta dan Himpunan Kosong (Pengantar)
=================================================

Himpunan Semesta
----------------

**Himpunan semesta** (*universal set*) adalah himpunan yang memuat semua
objek yang sedang dibicarakan. Notasinya biasanya ``S`` atau ``U``.

Contoh:

.. math::

   S = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}

Jika ``A = {2, 4, 6, 8, 10}``, maka ``A`` adalah himpunan bagian dari ``S``.

Himpunan Kosong
---------------

**Himpunan kosong** adalah himpunan yang tidak memiliki elemen. Notasinya:

.. math::

   \emptyset \quad \text{atau} \quad \{\}

Kardinalitasnya nol:

.. math::

   |\emptyset| = 0

.. warning::

   ``{∅}`` **bukan** himpunan kosong. ``{∅}`` adalah himpunan yang berisi
   satu elemen, yaitu himpunan kosong.

   .. math::

      |\emptyset| = 0, \quad |\{\emptyset\}| = 1

Diagram Venn
============

**Diagram Venn** adalah cara visual untuk menggambarkan himpunan.

Contoh sederhana:

.. code-block:: text

   S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
   A = {2, 4, 6, 8, 10}
   B = {1, 2, 3, 4, 5}

   ┌─────────────────────────────────────┐
   │ S                                   │
   │   ┌───────────────┐                 │
   │   │ A             │                 │
   │   │   2, 4, 6     │                 │
   │   │   8, 10       │                 │
   │   └───────────────┘                 │
   │   ┌───────────────┐                 │
   │   │ B             │                 │
   │   │   1, 2, 3     │                 │
   │   │   4, 5        │                 │
   │   └───────────────┘                 │
   │   7, 9                              │
   └─────────────────────────────────────┘

Diagram Venn membantu memahami:

- Anggota himpunan.
- Irisan (*intersection*).
- Gabungan (*union*).
- Selisih (*difference*).
- Himpunan bagian (*subset*).

Implementasi Python
===================

Membuat Himpunan
----------------

.. code-block:: python

   # Himpunan kosong harus dibuat dengan set()
   kosong = set()
   print(kosong)          # set()
   print(len(kosong))     # 0

   # Himpunan dengan elemen
   A = {1, 2, 3, 4, 5}
   print(A)               # {1, 2, 3, 4, 5}
   print(type(A))         # <class 'set'>

   # Duplikasi otomatis dihapus
   B = {1, 1, 2, 2, 3}
   print(B)               # {1, 2, 3}

   # Urutan tidak dijamin
   C = {3, 1, 2}
   print(C)               # {1, 2, 3} atau urutan lain

Keanggotaan
-----------

.. code-block:: python

   A = {1, 2, 3, 4, 5}

   print(1 in A)          # True
   print(6 in A)          # False
   print(6 not in A)      # True

Kardinalitas
------------

.. code-block:: python

   A = {1, 2, 3, 4, 5}
   print(len(A))          # 5

Operasi Dasar
-------------

.. code-block:: python

   A = {1, 2, 3, 4}
   B = {3, 4, 5, 6}

   print(A | B)           # union: {1, 2, 3, 4, 5, 6}
   print(A & B)           # intersection: {3, 4}
   print(A - B)           # difference: {1, 2}
   print(B - A)           # difference: {5, 6}
   print(A ^ B)           # symmetric difference: {1, 2, 5, 6}

Mengubah Data Log Menjadi Himpunan Unik
----------------------------------------

.. code-block:: python

   log = ["USR01", "USR05", "USR02", "USR01", "USR03", "USR05"]
   unique_users = set(log)
   print(unique_users)    # {'USR01', 'USR02', 'USR03', 'USR05'}
   print(len(unique_users))  # 4

Aplikasi di RPL
===============

.. list-table::
   :header-rows: 1

   * - Bidang
     - Contoh Penggunaan
   * - Basis Data
     - Menghitung *unique users*, menghapus duplikasi.
   * - Analitik
     - Unique Active Users (UAU), unique page views.
   * - Keamanan
     - Hak akses role, permission.
   * - API
     - Himpunan endpoint yang tersedia.
   * - Testing
     - Himpunan input valid, input invalid.
   * - Machine Learning
     - Himpunan fitur, himpunan label.

Contoh SQL: Menghitung Unique Users
-----------------------------------

.. code-block:: sql

   SELECT COUNT(DISTINCT user_id) AS unique_users
   FROM login_log;

Contoh SQL: Menghapus Duplikasi
-------------------------------

.. code-block:: sql

   SELECT DISTINCT user_id
   FROM login_log;

Contoh RBAC Sederhana
---------------------

.. code-block:: python

   HAK_AKSES = {"baca", "tulis", "hapus"}

   admin = {"baca", "tulis", "hapus"}
   editor = {"baca", "tulis"}
   viewer = {"baca"}

   print(admin <= HAK_AKSES)     # True
   print(editor <= admin)        # True
   print(viewer <= editor)       # True

Kesalahan Umum
==============

1. **Menganggap ``a`` sama dengan ``{a}``**

   .. math::

      a \neq \{a\}

2. **Menganggap ``{}`` sebagai himpunan kosong di Python**

   .. code-block:: python

      salah = {}       # ini dict kosong, bukan set
      benar = set()    # ini set kosong

3. **Menganggap urutan penting**

   .. math::

      \{1, 2, 3\} = \{3, 2, 1\}

4. **Menghitung duplikasi**

   .. math::

      |\{1, 1, 2, 2, 3\}| = 3

5. **Menganggap ``{∅}`` sama dengan ``∅``**

   .. math::

      \emptyset \neq \{\emptyset\}

Latihan
=======

Level 1 — Pemahaman Dasar
-------------------------

**Latihan 1**

Diketahui himpunan ``A = {2, 4, 6, 8, 10}``. Tentukan:

a. Apakah ``4 ∈ A``?
b. Apakah ``5 ∈ A``?
c. Berapa ``|A|``?

**Jawaban:**

a. Ya.
b. Tidak.
c. ``|A| = 5``.

**Latihan 2**

Ubah data log berikut menjadi himpunan unik dan tentukan kardinalitasnya:

.. code-block:: text

   [A1, A2, A1, A3, A2, A4, A1, A5]

**Jawaban:**

.. code-block:: text

   Himpunan unik = {A1, A2, A3, A4, A5}
   Kardinalitas = 5

**Latihan 3**

Mengapa kumpulan berikut **bukan** himpunan?

a. "Kumpulan makanan enak."
b. "Kumpulan film yang menarik."

Jelaskan berdasarkan syarat *well-defined*.

**Jawaban:**

a. *Enak* bersifat subjektif, tidak ada batas yang jelas.
b. *Menarik* juga subjektif, tidak terdefinisi dengan pasti.

**Latihan 4**

Diketahui himpunan ``P`` berisi bilangan bulat antara 1 dan 15 yang habis
dibagi 3. Tentukan ``P`` dengan enumerasi dan hitung ``|P|``.

**Jawaban:**

.. math::

   P = \{3, 6, 9, 12, 15\}, \quad |P| = 5

**Latihan 5**

Diketahui ``A = {a, b, c}`` dan ``B = {c, b, a, a}``. Apakah ``A = B``?
Jelaskan berdasarkan aturan urutan dan duplikasi.

**Jawaban:**

Ya, ``A = B``. Urutan tidak penting dan duplikasi diabaikan, sehingga
``{c, b, a, a} = {a, b, c}``.

Level 2 — Manipulasi
--------------------

**Latihan 6**

Diketahui ``S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}``.

a. Tuliskan himpunan ``A`` berisi bilangan genap di ``S``.
b. Tuliskan himpunan ``B`` berisi bilangan prima di ``S``.
c. Hitung ``|A|`` dan ``|B|``.

**Jawaban:**

a. ``A = {2, 4, 6, 8, 10}``
b. ``B = {2, 3, 5, 7}``
c. ``|A| = 5``, ``|B| = 4``

**Latihan 7**

Diketahui ``A = {1, 2, 3}`` dan ``B = {3, 4, 5}``. Tentukan:

a. ``A ∪ B``
b. ``A ∩ B``
c. ``A - B``
d. ``A ^ B``

**Jawaban:**

a. ``{1, 2, 3, 4, 5}``
b. ``{3}``
c. ``{1, 2}``
d. ``{1, 2, 4, 5}``

Level 3 — Aplikasi
------------------

**Latihan 8**

Sebuah aplikasi mencatat log kunjungan halaman:

.. code-block:: text

   [/home, /produk, /home, /kontak, /produk, /tentang, /home]

a. Ubah menjadi himpunan halaman unik.
b. Berapa banyak halaman unik yang dikunjungi?

**Jawaban:**

a. ``{/home, /produk, /kontak, /tentang}``
b. 4 halaman unik.

**Latihan 9**

Diberikan tabel ``login_log`` dengan kolom ``user_id``. Tulis query SQL
untuk menghitung jumlah *unique user* yang pernah login.

**Jawaban:**

.. code-block:: sql

   SELECT COUNT(DISTINCT user_id) AS unique_users
   FROM login_log;

Level 4 — Analisis
------------------

**Latihan 10**

Mengapa konsep himpunan penting dalam optimasi basis data? Jelaskan
kaitannya dengan operasi ``DISTINCT``.

**Jawaban:**

Konsep himpunan memastikan setiap elemen dihitung sekali. Operasi
``DISTINCT`` pada SQL menghilangkan duplikasi, sehingga menghasilkan
himpunan unik. Ini menghemat ruang penyimpanan, mempercepat query, dan
menghindari kesalahan analitik.

Ringkasan
=========

- Himpunan = kumpulan objek berbeda yang terdefinisi dengan jelas.
- Elemen ditulis dengan notasi ``∈`` (anggota) atau ``∉`` (bukan anggota).
- Notasi himpunan memakai kurung kurawal ``{}``.
- Urutan dan duplikasi tidak berpengaruh dalam himpunan.
- Kardinalitas ``|A|`` = banyaknya elemen berbeda dalam ``A``.
- Himpunan semesta ``S`` memuat semua objek yang dibicarakan.
- Himpunan kosong ``∅`` tidak memiliki elemen, ``|∅| = 0``.
- Konsep himpunan menjadi dasar analitik data (UAU) dan optimasi basis data.

Ringkasan Visual
----------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────┐
   │                 KONSEP DASAR HIMPUNAN                    │
   ├──────────────────────────────────────────────────────────┤
   │                                                          │
   │  Definisi: kumpulan objek berbeda & well-defined         │
   │                                                          │
   │  Notasi: A = {a₁, a₂, ..., aₙ}                           │
   │                                                          │
   │  Keanggotaan: x ∈ A  |  x ∉ A                            │
   │                                                          │
   │  Urutan & duplikasi: tidak berpengaruh                   │
   │                                                          │
   │  Kardinalitas: |A| = banyak elemen berbeda               │
   │                                                          │
   │  Himpunan semesta: S                                     │
   │  Himpunan kosong: ∅, |∅| = 0                             │
   │                                                          │
   │  Diagram Venn: visualisasi himpunan                      │
   │                                                          │
   │  Python: set(), in, len(), |, &, -, ^                    │
   │                                                          │
   │  Aplikasi: unique users, UAU, RBAC, testing              │
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

- :doc:`notasi_himpunan` — cara menyajikan himpunan (enumerasi, simbol
  baku, notasi pembentuk, diagram Venn).
- :doc:`himpunan_khusus` — himpunan kosong, subset, dan himpunan kuasa.
- :doc:`relasi_antar_himpunan` — himpunan sama dan himpunan ekivalen.
