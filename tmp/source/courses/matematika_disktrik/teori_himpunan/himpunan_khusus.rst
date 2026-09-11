.. _himpunan-khusus:

=================
Himpunan Khusus
=================

.. contents:: Daftar Isi
   :depth: 2
   :local:

Pengantar
=========

Selain himpunan biasa, ada beberapa **himpunan khusus** yang punya peran penting dalam Matematika Diskrit dan rekayasa perangkat lunak:

1. **Himpunan kosong** — himpunan yang tidak memiliki elemen.
2. **Himpunan bagian (subset)** — himpunan yang seluruh elemennya ada di himpunan lain.
3. **Himpunan kuasa (power set)** — himpunan dari semua subset.

Ketiganya menjadi dasar bagi konsep **relasi**, **fungsi**, **logika**, dan **struktur data** seperti *hierarki* dan *role-based access control* (RBAC).

.. admonition:: Driving Question
   :class: tip

   Bagaimana struktur hierarki *Role-Based Access Control* (RBAC) pada sistem informasi akademik dapat dimodelkan secara matematis menggunakan konsep **subset** dan **power set** untuk mencegah kebocoran hak akses?

   Setiap role (admin, dosen, mahasiswa) memiliki hak akses yang berbeda:

   - ``HakAkses = {Input, Edit, Hapus, Lihat}``
   - ``Admin = {Input, Edit, Hapus, Lihat}``
   - ``Dosen = {Input, Lihat}``
   - ``Mahasiswa = {Lihat}``

   Relasi himpunan:

   .. math::

      \text{Mahasiswa} \subseteq \text{Dosen} \subseteq \text{Admin}

   Himpunan kuasa dari ``{Lihat}``:

   .. math::

      P(\{\text{Lihat}\}) = \{\emptyset, \{\text{Lihat}\}\}

   Artinya mahasiswa hanya punya 2 kemungkinan hak akses: tidak ada (``∅``) atau hanya lihat data.

Peta Konsep
===========

.. code-block:: text

   HIMPUNAN KHUSUS
   │
   ├── 1. Himpunan Kosong (∅)
   │     └── Himpunan tanpa elemen, |∅| = 0
   │
   ├── 2. Himpunan Bagian / Subset (⊆)
   │     ├── Definisi: semua elemen A ada di B
   │     ├── Subset sejati (⊂): A ⊆ B tetapi A ≠ B
   │     ├── Sifat: refleksif, transitif, antisimetris
   │     └── Aplikasi: RBAC, hierarki data, tipe data
   │
   └── 3. Himpunan Kuasa / Power Set (P(A))
         ├── Definisi: himpunan semua subset A
         ├── Ukuran: |P(A)| = 2^n
         └── Aplikasi: konfigurasi fitur, exhaustive testing, RBAC

Ketiganya saling terkait:

.. code-block:: text

   ∅  →  selalu subset dari setiap himpunan
   A  →  punya 2^n subset, termasuk ∅ dan A sendiri
   P(A) → himpunan semua subset A

Himpunan Kosong
===============

Definisi Formal
---------------

**Himpunan kosong** adalah himpunan yang tidak memiliki satu pun elemen. Kardinalitasnya nol.

.. math::

   \emptyset = \{\} \quad \text{dan} \quad |\emptyset| = 0

Notasi
------

.. list-table::
   :header-rows: 1

   * - Notasi
     - Penulisan
     - Keterangan
   * - Simbol
     - ``∅``
     - Paling ringkas, umum di buku teks
   * - Kurung kurawal kosong
     - ``{ }``
     - Eksplisit
   * - Unicode
     - ``∅`` (U+2205)
     - Simbol matematika resmi
   * - LaTeX
     - ``\emptyset`` atau ``\varnothing``
     - Untuk dokumen

**Catatan penting:** ``{}`` dan ``{ }`` sama, tetapi ``{∅}`` **BUKAN** himpunan kosong.

Cara Membuktikan Himpunan Kosong
--------------------------------

Sebuah himpunan ``A`` adalah himpunan kosong jika **tidak ada objek** yang memenuhi syarat keanggotaannya.

**Contoh 1 — Kontradiksi internal**

.. math::

   E = \{x \mid x < x\}

Tidak ada bilangan yang lebih kecil dari dirinya sendiri, jadi ``E = ∅``.

**Contoh 2 — Kontradiksi dengan definisi**

.. math::

   F = \{x \mid x \text{ bilangan prima}, x < 2\}

Bilangan prima terkecil adalah 2. Tidak ada bilangan prima < 2, jadi ``F = ∅``.

**Contoh 3 — Kontradiksi dengan rentang**

.. math::

   G = \{x \mid x \in \mathbb{N}, 5 < x < 6\}

Tidak ada bilangan asli antara 5 dan 6, jadi ``G = ∅``.

Perbedaan Krusial: ``∅`` vs ``{∅}``
------------------------------------

Ini **kesalahan paling umum** mahasiswa. Perhatikan:

.. list-table::
   :header-rows: 1

   * - Ekspresi
     - Arti
     - Kardinalitas
     - Elemen
   * - ``∅``
     - Himpunan kosong
     - ``|∅| = 0``
     - Tidak ada
   * - ``{∅}``
     - Himpunan yang berisi himpunan kosong
     - ``|{∅}| = 1``
     - Ada 1, yaitu ``∅``
   * - ``{{∅}}``
     - Himpunan yang berisi himpunan yang berisi himpunan kosong
     - ``|{{∅}}| = 1``
     - Ada 1, yaitu ``{∅}``
   * - ``{∅, {∅}}``
     - Himpunan berisi dua elemen
     - ``2``
     - ``∅`` dan ``{∅}``

**Analogi:**

- ``∅`` = kotak kosong.
- ``{∅}`` = kotak yang berisi kotak kosong.

Kotak kosong dan kotak yang berisi kotak kosong itu **berbeda**.

Himpunan Kosong dalam Python
----------------------------

.. code-block:: python

   # Cara benar membuat himpunan kosong
   kosong = set()
   print(len(kosong))        # 0
   print(type(kosong))       # <class 'set'>

   # Cara SALAH — ini dict kosong
   bukan_set = {}
   print(len(bukan_set))     # 0
   print(type(bukan_set))    # <class 'dict'>

**Kenapa ``{}`` bukan himpunan kosong?**

Karena di Python, ``{}`` dipakai untuk *dictionary* (kamus). Himpunan kosong **harus** dibuat dengan ``set()``.

.. code-block:: python

   print(set() == {})        # False! bukan hal yang sama
   print(bool(set()))        # False (kosong = falsy)
   print(bool({}))           # False (dict kosong juga falsy)

Aplikasi Himpunan Kosong di RPL
-------------------------------

.. list-table::
   :header-rows: 1

   * - Bidang
     - Contoh
   * - Database
     - Hasil query yang tidak mengembalikan baris
   * - Autentikasi
     - User dengan role tidak dikenal = ``∅`` akses
   * - Graf
     - Graf tanpa edge: ``E = ∅``, hanya node
   * - Analitik
     - User yang belum pernah login = himpunan kosong
   * - Testing
     - Input yang tidak valid = himpunan kosong

**Contoh query SQL:**

.. code-block:: sql

   -- Jika tidak ada user dengan nama "Xyz", hasilnya himpunan kosong
   SELECT * FROM users WHERE name = 'Xyz';
   -- → ∅ (empty result set)

Himpunan Bagian / Subset
========================

Definisi Formal
---------------

Himpunan ``A`` disebut **himpunan bagian** (*subset*) dari himpunan ``B`` jika dan hanya jika **setiap elemen ``A``** juga merupakan elemen dari ``B``.

.. math::

   A \subseteq B \iff \forall x \, (x \in A \Rightarrow x \in B)

**Baca:** "Untuk setiap ``x``, jika ``x`` ada di ``A``, maka ``x`` ada di ``B``."

Notasi Terkait
--------------

.. list-table::
   :header-rows: 1

   * - Notasi
     - Arti
   * - ``A ⊆ B``
     - A subset dari B (A bisa sama dengan B)
   * - ``A ⊂ B``
     - A proper subset dari B (A ≠ B)
   * - ``A ⊇ B``
     - A superset dari B
   * - ``A ⊃ B``
     - A proper superset dari B
   * - ``A ⊄ B``
     - A bukan subset dari B

**Penting:** Notasi ``⊂`` di beberapa buku berarti *proper subset*, di buku lain berarti *subset* biasa. Selalu cek konvensi buku. Di dokumen ini, ``⊂`` = proper subset.

Cara Membuktikan ``A ⊆ B``
---------------------------

**Metode 1 — Elemen-per-elemen:**

Ambil elemen sembarang ``x ∈ A``, buktikan ``x ∈ B``.

.. code-block:: text

   Misal A = {1, 2, 3}, B = {1, 2, 3, 4, 5}
   Ambil x ∈ A, berarti x ∈ {1, 2, 3}
   Maka x ∈ {1, 2, 3, 4, 5}
   Jadi A ⊆ B. ∎

**Metode 2 — Bandingkan elemen:**

.. code-block:: text

   A = {1, 2, 3}
   B = {1, 2, 3, 4, 5}
   Semua elemen A ada di B → A ⊆ B

**Metode 3 — Cari counter-example (untuk membantah):**

.. code-block:: text

   A = {1, 2, 3}
   B = {1, 2, 4}
   3 ∈ A tetapi 3 ∉ B → A ⊄ B

Contoh Lengkap
--------------

**Contoh 1 — Subset sejati:**

.. math::

   \{1, 2, 3\} \subset \{1, 2, 3, 4, 5\}

Alasan: ``{1,2,3} ⊆ {1,2,3,4,5}`` dan ``{1,2,3} ≠ {1,2,3,4,5}``.

**Contoh 2 — Subset (bukan sejati):**

.. math::

   \{1, 2, 3\} \subseteq \{1, 2, 3\}

Alasan: setiap himpunan adalah subset dirinya sendiri.

**Contoh 3 — Bukan subset:**

.. math::

   \{1, 2, 3\} \not\subseteq \{1, 2, 4\}

Alasan: ``3`` tidak ada di himpunan kanan.

**Contoh 4 — Himpunan kosong:**

.. math::

   \emptyset \subseteq A \quad \text{untuk setiap himpunan } A

Alasan: tidak ada elemen di ``∅`` yang melanggar syarat subset.

Sifat-Sifat Subset
------------------

Sifat 1: Refleksif
~~~~~~~~~~~~~~~~~~

Setiap himpunan adalah subset dirinya sendiri.

.. math::

   A \subseteq A

**Kenapa?** Karena semua elemen ``A`` ada di ``A``.

Sifat 2: Himpunan kosong adalah subset universal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::

   \emptyset \subseteq A \quad \text{untuk setiap himpunan } A

**Kenapa?** Pernyataan "setiap elemen ``∅`` ada di ``A``" **selalu benar** karena ``∅`` tidak punya elemen. Ini disebut *vacuous truth*.

Sifat 3: Transitif
~~~~~~~~~~~~~~~~~~

Jika ``A ⊆ B`` dan ``B ⊆ C``, maka ``A ⊆ C``.

.. math::

   (A \subseteq B \land B \subseteq C) \Rightarrow A \subseteq C

**Bukti:**

.. code-block:: text

   Ambil x ∈ A.
   Karena A ⊆ B, maka x ∈ B.
   Karena B ⊆ C, maka x ∈ C.
   Jadi setiap elemen A ada di C → A ⊆ C. ∎

Sifat 4: Antisimetris
~~~~~~~~~~~~~~~~~~~~~

Jika ``A ⊆ B`` dan ``B ⊆ A``, maka ``A = B``.

.. math::

   (A \subseteq B \land B \subseteq A) \Rightarrow A = B

Ini adalah definisi himpunan sama.

Sifat 5: Tidak Total
~~~~~~~~~~~~~~~~~~~~

Tidak semua himpunan bisa dibandingkan. Ada ``A`` dan ``B`` di mana ``A ⊄ B`` dan ``B ⊄ A``.

**Contoh:**

.. code-block:: text

   A = {1, 2}
   B = {2, 3}
   A ⊄ B (karena 1 ∉ B)
   B ⊄ A (karena 3 ∉ A)

Jadi subset **bukan relasi total**, melainkan **relasi parsial**.

Subset Sejati (Proper Subset)
-----------------------------

``A`` disebut **proper subset** dari ``B`` jika ``A ⊆ B`` tetapi ``A ≠ B``.

.. math::

   A \subset B \iff (A \subseteq B \land A \neq B)

**Contoh:**

.. math::

   \{1, 2\} \subset \{1, 2, 3\}

**Jumlah proper subset:**

Jika ``|A| = n``, jumlah proper subset (tidak termasuk A sendiri) = ``2^n - 1``.

Aplikasi Subset di RBAC
-----------------------

RBAC (*Role-Based Access Control*) adalah pola keamanan di mana hak akses ditentukan berdasarkan role pengguna. Subset adalah **fondasi matematis** untuk RBAC.

**Contoh sistem akademik:**

.. code-block:: text

   HakAkses  = {Input, Edit, Hapus, Lihat}

   Admin     = {Input, Edit, Hapus, Lihat}   → Admin = HakAkses
   Dosen     = {Input, Lihat}                → Dosen ⊆ Admin
   Mahasiswa = {Lihat}                       → Mahasiswa ⊆ Dosen
   Tamu      = ∅                             → Tamu = ∅

**Relasi hierarki:**

.. code-block:: text

   Mahasiswa ⊆ Dosen ⊆ Admin ⊆ HakAkses
   Tamu = ∅

**Kenapa penting?**

- Untuk memberi admin akses, cukup periksa ``admin ⊆ HakAkses``.
- Untuk mencegah mahasiswa mengedit, cukup periksa apakah ``Edit ∈ Mahasiswa``. Karena tidak, akses ditolak.
- Sistem tidak perlu menulis aturan per-user; cukup per role.

**Implementasi Python:**

.. code-block:: python

   HAK_AKSES = {"Input", "Edit", "Hapus", "Lihat"}

   admin     = {"Input", "Edit", "Hapus", "Lihat"}
   dosen     = {"Input", "Lihat"}
   mahasiswa = {"Lihat"}
   tamu      = set()

   print(admin <= HAK_AKSES)      # True
   print(dosen <= admin)          # True
   print(mahasiswa <= dosen)      # True
   print(tamu <= mahasiswa)       # True (∅ ⊆ everything)

**Implementasi SQL (konsep):**

.. code-block:: sql

   -- Role dengan permission tertentu
   SELECT r.name
   FROM roles r
   WHERE r.id IN (
       SELECT rp.role_id
       FROM role_permissions rp
       WHERE rp.permission_id IN (
           SELECT id FROM permissions WHERE name = 'Edit'
       )
   );
   -- Hasil: Admin (karena Admin punya 'Edit', Mahasiswa tidak)

Aplikasi Lain Subset di RPL
---------------------------

.. list-table::
   :header-rows: 1

   * - Bidang
     - Contoh
   * - Tipe data
     - ``int ⊆ number``, ``Cat ⊆ Animal``
   * - Inheritance OOP
     - ``class Child ⊆ class Parent``
   * - Database
     - Kolom tabel ⊆ skema
   * - API
     - ``endpoint ⊆ router``
   * - Analitik
     - ``user_baru ⊆ user_aktif``
   * - Testing
     - ``input_valid ⊆ input_total``

Himpunan Kuasa / Power Set
==========================

Definisi Formal
---------------

**Himpunan kuasa** (*power set*) dari himpunan ``A`` adalah himpunan yang berisi **semua subset** dari ``A``, termasuk ``∅`` dan ``A`` sendiri.

.. math::

   P(A) = \{S \mid S \subseteq A\}

**Notasi alternatif:** ``2^A`` (dibaca "2 pangkat A").

Jumlah Elemen
-------------

Jika ``|A| = n``, maka:

.. math::

   |P(A)| = 2^n

**Kenapa ``2^n``?** Karena untuk setiap elemen ``A``, ada **2 pilihan**: masuk subset, atau tidak. Total kombinasi = ``2 × 2 × ... × 2`` (n kali) = ``2^n``.

Contoh Lengkap
--------------

**Contoh 1 — ``A = {1, 2}`` (n = 2)**

.. math::

   P(A) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}

``|P(A)| = 2^2 = 4``.

**Enumerasi lengkap:**

.. list-table::
   :header-rows: 1

   * - Subset
     - Elemen
   * - 1
     - ``∅``
   * - 2
     - ``{1}``
   * - 3
     - ``{2}``
   * - 4
     - ``{1, 2}``

**Contoh 2 — ``A = {a, b, c}`` (n = 3)**

.. math::

   P(A) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, \{a,b,c\}\}

``|P(A)| = 2^3 = 8``.

**Enumerasi berdasarkan ukuran:**

.. list-table::
   :header-rows: 1

   * - Ukuran
     - Subset
     - Jumlah
   * - 0
     - ``∅``
     - 1
   * - 1
     - ``{a}``, ``{b}``, ``{c}``
     - 3
   * - 2
     - ``{a,b}``, ``{a,c}``, ``{b,c}``
     - 3
   * - 3
     - ``{a,b,c}``
     - 1
   * - **Total**
     -
     - **8**

Jumlah ini mengikuti **koefisien binomial** (baris ke-3 Pascal):

.. math::

   \binom{3}{0} + \binom{3}{1} + \binom{3}{2} + \binom{3}{3} = 1 + 3 + 3 + 1 = 8

**Contoh 3 — ``A = {Lihat}`` (n = 1)**

.. math::

   P(A) = \{\emptyset, \{\text{Lihat}\}\}

``|P(A)| = 2^1 = 2``.

Sifat-Sifat Power Set
---------------------

1. **Selalu berisi ``∅``** dan **A sendiri**.

   .. math::

      \emptyset \in P(A) \quad \text{dan} \quad A \in P(A)

2. **Jika ``A ⊆ B``, maka ``P(A) ⊆ P(B)``.** *(monoton)*

3. **``|P(A)| = 2^{|A|}``.**

4. **Kardinalitas power set dari himpunan kosong:**

   .. math::

      P(\emptyset) = \{\emptyset\} \quad \text{dan} \quad |P(\emptyset)| = 2^0 = 1

   *Catatan:* ``P(∅)`` bukan himpunan kosong. Ia berisi satu elemen, yaitu ``∅`` sendiri.

5. **Power set adalah himpunan dari himpunan** — elemennya adalah himpunan, bukan bilangan/string.

Implementasi Python
-------------------

**Cara 1 — Manual dengan ``combinations``:**

.. code-block:: python

   from itertools import combinations

   def power_set(s):
       """Menghasilkan semua subset dari himpunan s."""
       s = list(s)
       return [
           set(combo)
           for r in range(len(s) + 1)
           for combo in combinations(s, r)
       ]

   A = {"a", "b", "c"}
   hasil = power_set(A)
   print(len(hasil))   # 8
   for sub in hasil:
       print(sub)

**Output:**

.. code-block:: text

   set()
   {'a'}
   {'b'}
   {'c'}
   {'a', 'b'}
   {'a', 'c'}
   {'b', 'c'}
   {'a', 'b', 'c'}

**Cara 2 — Bitmask (pendekatan matematis):**

.. code-block:: python

   def power_set_bitmask(s):
       """Power set via representasi biner."""
       s = list(s)
       n = len(s)
       result = []
       for i in range(2**n):       # 0 sampai 2^n - 1
           subset = set()
           for j in range(n):
               if i & (1 << j):    # cek bit ke-j
                   subset.add(s[j])
           result.append(subset)
       return result

   A = {"a", "b", "c"}
   print(len(power_set_bitmask(A)))  # 8

**Kenapa bitmask bekerja?**

Setiap subset berkorespondensi dengan bilangan biner ``n`` bit. Bit ke-``j`` = 1 berarti elemen ke-``j`` ada di subset.

Untuk ``A = {a, b, c}``:

.. list-table::
   :header-rows: 1

   * - i
     - Biner
     - Subset
   * - 0
     - 000
     - ``∅``
   * - 1
     - 001
     - ``{a}``
   * - 2
     - 010
     - ``{b}``
   * - 3
     - 011
     - ``{a, b}``
   * - 4
     - 100
     - ``{c}``
   * - 5
     - 101
     - ``{a, c}``
   * - 6
     - 110
     - ``{b, c}``
   * - 7
     - 111
     - ``{a, b, c}``

Aplikasi Power Set di RPL
-------------------------

Aplikasi 1: Konfigurasi Fitur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Misalkan aplikasi punya 3 fitur:

.. code-block:: text

   Fitur = {Chat, Video, Audio}

Power set = semua kombinasi fitur yang bisa diaktifkan:

.. code-block:: text

   ∅                      → semua fitur mati
   {Chat}                 → hanya chat
   {Video}                → hanya video
   {Audio}                → hanya audio
   {Chat, Video}          → chat + video
   {Chat, Audio}          → chat + audio
   {Video, Audio}         → video + audio
   {Chat, Video, Audio}   → semua aktif

Total: ``2^3 = 8`` paket berlangganan.

**Aplikasi nyata:** Netflix, Spotify, Zoom menggunakan *tier pricing* berdasarkan kombinasi fitur.

Aplikasi 2: Exhaustive Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Untuk memastikan software tidak crash, uji **semua kombinasi** input yang mungkin.

.. code-block:: python

   def test_all_combinations(fitur):
       for combo in power_set(fitur):
           # Uji aplikasi dengan fitur aktif = combo
           run_test(combo)

Untuk 3 fitur → 8 test case.
Untuk 10 fitur → 1024 test case.
Untuk 20 fitur → 1 juta test case.
*(Ini kenapa exhaustive testing mahal.)*

Aplikasi 3: RBAC Lanjutan
~~~~~~~~~~~~~~~~~~~~~~~~~

**Power set dari permission = semua role yang mungkin.**

.. code-block:: python

   HAK_AKSES = {"Input", "Edit", "Hapus", "Lihat"}
   semua_role_mungkin = power_set(HAK_AKSES)
   print(len(semua_role_mungkin))  # 16 role

Sistem dengan 4 permission bisa punya sampai 16 role berbeda. Ini menjelaskan kenapa RBAC **skalabel**: dari ``n`` permission, Anda bisa definisikan sampai ``2^n`` role.

Aplikasi 4: Query Database (Index)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Untuk tabel dengan ``n`` kolom, power set kolom = semua kombinasi index yang mungkin.

.. code-block:: text

   Kolom = {user_id, tanggal, status}
   Index = power_set(Kolom)
   # 8 kombinasi index yang bisa dibuat

DBA bisa memilih index optimal dari power set.

Aplikasi 5: Machine Learning (Feature Selection)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dari ``n`` fitur, power set = semua subset fitur yang bisa dicoba.

.. code-block:: text

   Fitur = {x1, x2, x3, x4}
   Subset fitur = power_set(Fitur)   # 16 subset
   # Cari subset terbaik dengan akurasi tertinggi

**Ini adalah dasar dari *exhaustive feature selection*.**

Visualisasi Power Set
---------------------

**Contoh ``A = {a, b, c}`` sebagai diagram Hasse:**

.. code-block:: text

              {a, b, c}
             /    |    \
        {a,b}  {a,c}  {b,c}
          |  \  /  \  /  |
          |   \/    \/   |
          |   /\    /\   |
          |  /  \  /  \  |
         {a}   {b}   {c}
           \    |    /
            \   |   /
               ∅

Setiap level menunjukkan subset dengan ukuran tertentu. Level 0 = ``∅``, level 3 = himpunan penuh.

Hubungan Ketiga Konsep
======================

Ketiga konsep saling terkait erat:

.. code-block:: text

   ∅  ⊆  setiap A
   A  punya 2^n subset
   P(A) = himpunan semua subset A

**Identitas penting:**

.. list-table::
   :header-rows: 1

   * - Identitas
     - Penjelasan
   * - ``∅ ∈ P(A)``
     - Himpunan kosong selalu ada di power set
   * - ``A ∈ P(A)``
     - A sendiri selalu ada di power set
   * - ``P(∅) = {∅}``
     - Power set dari himpunan kosong berisi satu elemen
   * - ``|P(A)| = 2^{|A|}``
     - Ukuran power set
   * - ``A ⊆ B ⟺ P(A) ⊆ P(B)``
     - Monotonisitas
   * - ``∅ ⊆ A ⊆ A``
     - Refleksif

Latihan Komprehensif
====================

Level 1 — Pemahaman Dasar
-------------------------

**Soal 1.** Tentukan benar/salah:

a. ``∅ ⊆ ∅``
b. ``∅ ∈ ∅``
c. ``∅ ∈ {∅}``
d. ``{∅} ⊆ {∅}``
e. ``∅ ⊆ {∅}``

**Jawaban:**

.. list-table::
   :header-rows: 1

   * - Soal
     - Jawaban
     - Alasan
   * - a
     - Benar
     - ∅ selalu subset dari semua himpunan, termasuk ∅
   * - b
     - Salah
     - ∅ tidak punya elemen, jadi tidak ada yang jadi elemennya
   * - c
     - Benar
     - ``{∅}`` berisi satu elemen, yaitu ``∅``
   * - d
     - Benar
     - Setiap himpunan subset dari dirinya sendiri
   * - e
     - Benar
     - ∅ subset dari semua himpunan

Level 2 — Manipulasi
--------------------

**Soal 2.** Tentukan ``P(A)`` dan ``|P(A)|`` untuk:

a. ``A = {1}``
b. ``A = {1, 2}``
c. ``A = {1, 2, 3}``
d. ``A = ∅``

**Jawaban:**

a. ``P({1}) = {∅, {1}}``, ``|P| = 2``
b. ``P({1,2}) = {∅, {1}, {2}, {1,2}}``, ``|P| = 4``
c. ``P({1,2,3}) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}``, ``|P| = 8``
d. ``P(∅) = {∅}``, ``|P| = 1`` *(perhatikan: bukan 0!)*

Level 3 — Aplikasi
------------------

**Soal 3.** Sebuah sistem e-learning punya 4 modul: ``{Materi, Kuis, Tugas, Forum}``. Setiap mahasiswa bisa diberi akses ke subset modul. Berapa banyak konfigurasi akses berbeda yang mungkin?

**Jawaban:** ``2^4 = 16`` konfigurasi.

**Soal 4.** Dari 16 konfigurasi, hitung yang memuat ``Kuis``.

**Jawaban:** Karena ``Kuis`` wajib ada, tinggal 3 modul lain yang bebas: ``2^3 = 8`` konfigurasi.

Level 4 — Analisis
------------------

**Soal 5.** Diketahui ``A = {a, b}`` dan ``B = {a, b, c}``.

a. Apakah ``A ⊆ B``?
b. Apakah ``P(A) ⊆ P(B)``?
c. Berapa ``|P(B)| - |P(A)|``?

**Jawaban:**

a. Ya, semua elemen ``A`` ada di ``B``.
b. Ya, karena ``A ⊆ B`` maka ``P(A) ⊆ P(B)``.
c. ``|P(B)| - |P(A)| = 2^3 - 2^2 = 8 - 4 = 4``.

Elemen tambahan di ``P(B)``:

- ``{c}``
- ``{a, c}``
- ``{b, c}``
- ``{a, b, c}``

Latihan Tambahan
----------------

**Latihan 1**

Diketahui ``A = {1, 2, 3, 4}``. Tentukan:

a. Apakah ``{1, 3} ⊆ A``?
b. Apakah ``{1, 5} ⊆ A``?
c. Apakah ``∅ ⊆ A``?

**Jawaban:**

a. Ya.
b. Tidak, karena ``5 ∉ A``.
c. Ya.

**Latihan 2**

Diketahui ``B = {x, y}``. Tentukan ``P(B)`` dan ``|P(B)|``.

**Jawaban:**

.. math::

   P(B) = \{\emptyset, \{x\}, \{y\}, \{x, y\}\}, \quad |P(B)| = 4

**Latihan 3**

Jika ``|A| = 5``, berapa ``|P(A)|``?

**Jawaban:** ``2^5 = 32``.

**Latihan 4**

Diketahui RBAC:

- ``HakAkses = {baca, tulis, hapus}``
- ``Editor = {baca, tulis}``
- ``Viewer = {baca}``

a. Tuliskan relasi subset antar role.
b. Tentukan ``P(Viewer)``.

**Jawaban:**

a. ``Viewer ⊆ Editor ⊆ HakAkses``.
b. ``P(Viewer) = {∅, {baca}}``.

**Latihan 5**

Mengapa ``{∅}`` bukan himpunan kosong? Jelaskan.

**Jawaban:** Karena ``{∅}`` memiliki satu elemen, yaitu ``∅``. Himpunan kosong ``∅`` tidak memiliki elemen. Jadi ``|∅| = 0``, sedangkan ``|{∅}| = 1``.

Ringkasan
=========

- **Himpunan kosong** ``∅`` = himpunan tanpa elemen, ``|∅| = 0``.
- **Subset** ``A ⊆ B`` = semua elemen ``A`` ada di ``B``.
- **Subset sejati** ``A ⊂ B`` = ``A ⊆ B`` tetapi ``A ≠ B``.
- **Himpunan kuasa** ``P(A)`` = himpunan semua subset ``A``.
- Jika ``|A| = n``, maka ``|P(A)| = 2^n``.
- Konsep ini jadi dasar RBAC, konfigurasi fitur, dan *exhaustive testing*.

Ringkasan Visual
----------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────┐
   │                     HIMPUNAN KHUSUS                      │
   ├──────────────────────────────────────────────────────────┤
   │                                                          │
   │  ∅ (Himpunan Kosong)                                     │
   │  ├── |∅| = 0                                             │
   │  ├── ∅ ⊆ A (untuk setiap A)                              │
   │  ├── ∅ ∈ P(A) (untuk setiap A)                           │
   │  └── P(∅) = {∅}, |P(∅)| = 1                              │
   │                                                          │
   │  A ⊆ B (Subset)                                          │
   │  ├── Refleksif: A ⊆ A                                    │
   │  ├── Transitif: A ⊆ B, B ⊆ C → A ⊆ C                     │
   │  ├── Antisimetris: A ⊆ B, B ⊆ A → A = B                  │
   │  ├── ∅ ⊆ A (untuk setiap A)                              │
   │  └── Aplikasi: RBAC, hierarki kelas, tipe data           │
   │                                                          │
   │  P(A) (Power Set)                                        │
   │  ├── P(A) = {S | S ⊆ A}                                  │
   │  ├── |P(A)| = 2^|A|                                      │
   │  ├── ∅ ∈ P(A) dan A ∈ P(A)                               │
   │  ├── A ⊆ B → P(A) ⊆ P(B)                                 │
   │  └── Aplikasi: konfigurasi fitur, testing, feature sel.  │
   │                                                          │
   └──────────────────────────────────────────────────────────┘

Koneksi ke Modul Berikutnya
===========================

Modul ini adalah **jembatan** menuju topik selanjutnya:

.. list-table::
   :header-rows: 1

   * - Konsep di Modul Ini
     - Dipakai di Modul
   * - ``∅``
     - Relasi (relasi kosong), Fungsi (fungsi tidak terdefinisi)
   * - ``⊆``
     - Relasi antar himpunan, Fungsi injektif/surjektif
   * - ``P(A)``
     - Kombinatorik (koefisien binomial), Boolean (tabel kebenaran)
   * - RBAC
     - Keamanan sistem, basis data
   * - Power set
     - Aljabar Boolean (2^n baris tabel kebenaran)

**Contoh koneksi:**

- **Aljabar Boolean** — tabel kebenaran dengan ``n`` variabel punya ``2^n`` baris. Ini sama dengan ``|P(Variabel)|``.
- **Kombinatorik** — memilih ``k`` dari ``n`` = ``C(n, k)``, yang menjumlah jadi ``2^n``.
- **Relasi** — relasi dari ``A`` ke ``B`` adalah subset dari ``A × B``. Jadi himpunan semua relasi = ``P(A × B)``.

Referensi
=========

- Munir, R., *Matematika Diskrit*, Bandung, Informatika, 2012.
- Rosen, K. H., *Discrete Mathematics and Its Applications*, McGraw-Hill.
- Susanna S. Epp, *Discrete Mathematics with Applications*, 4th Edition, Brooks Cole, 2010.

Lanjutan
========

- :doc:`konsep_dasar_himpunan` — definisi himpunan dan elemen.
- :doc:`notasi_himpunan` — cara menyajikan himpunan.
- :doc:`relasi_antar_himpunan` — himpunan sama dan ekivalen.

Kesimpulan
==========

Modul **Himpunan Khusus** mengajarkan tiga konsep fundamental:

1. **``∅``** — himpunan kosong, titik nol dalam dunia himpunan.
2. **``⊆``** — subset, relasi hierarki yang membentuk dasar RBAC dan inheritance.
3. **``P(A)``** — power set, generator semua kombinasi yang jadi dasar kombinatorik dan exhaustive testing.

Ketiganya adalah **fondasi wajib** sebelum masuk ke topik relasi, fungsi, kombinatorik, dan aljabar Boolean. Kalau tiga konsep ini belum kuat, topik-topik selanjutnya akan terasa sulit.

**Pesan kunci:**

> Himpunan kosong adalah **awal**, subset adalah **hubungan**, dan power set adalah **semua kemungkinan**.

Ketiganya bersama-sama mengajarkan cara berpikir **diskrit, terstruktur, dan menyeluruh** — kemampuan inti seorang software engineer.
