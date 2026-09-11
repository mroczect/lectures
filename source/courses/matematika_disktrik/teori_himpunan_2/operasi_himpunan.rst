.. _operasi-himpunan:

================
Operasi Himpunan
================

1. Irisan (Intersection)
========================

Irisan (Intersection) dari himpunan A dan B adalah sebuah himpunan yang setiap elemennya merupakan elemen dari himpunan A dan himpunan B.

.. math::

   A \cap B = \{x \mid x \in A \text{ dan } x \in B\}

**Contoh:**

Jika :math:`A = \{2, 4, 6, 8, 10, 11\}`, dan :math:`B = \{4, 10, 11, 14, 18\}`, maka :math:`A \cap B = \{4, 10, 11\}`.

2. Gabungan (Union)
===================

Gabungan (union) dari himpunan A dan B adalah himpunan yang setiap anggotanya merupakan anggota himpunan A atau himpunan B.

.. math::

   A \cup B = \{x \mid x \in A \text{ atau } x \in B\}

**Contoh:**

Jika :math:`A = \{2, 5, 8\}` dan :math:`B = \{7, 5, 22\}`, maka :math:`A \cup B = \{2, 5, 7, 8, 22\}`.

3. Komplemen (Complement)
=========================

Komplemen dari suatu himpunan A terhadap suatu himpunan semesta U adalah suatu himpunan yang elemennya merupakan elemen U tapi bukan elemen A.

.. math::

   \bar{A} = \{x \mid x \in U \text{ dan } x \notin A\}

**Contoh:**

Misalkan :math:`U = \{1, 2, \dots, 9\}`. Jika :math:`A = \{1, 3, 5, 7, 9\}`, maka :math:`\bar{A} = \{2, 4, 6, 8\}`.

4. Selisih (Difference)
=======================

Selisih dua himpunan A dan B adalah suatu himpunan yang elemennya merupakan elemen A tapi bukan elemen B.

.. math::

   A - B = \{x \mid x \in A \text{ dan } x \notin B\}

**Contoh:**

Dalam basis data relasional (SQL), operasi selisih ini setara dengan perintah ``EXCEPT`` atau ``NOT IN``.

.. code-block:: sql

   -- A = Pengguna Aktif Bulan Ini
   -- B = Pengguna yang Sudah Membayar Tagihan
   SELECT user_id FROM active_users
   EXCEPT
   SELECT user_id FROM paid_users;

   -- Hasil: Daftar pengguna aktif yang belum bayar tagihan

5. Beda Simetris (Symmetric Difference)
======================================

Beda simetris dari himpunan A dan B adalah suatu himpunan yang elemennya ada pada himpunan A atau B, tapi tidak pada keduanya.

.. math::

   A \oplus B = (A \cup B) - (A \cap B)

**Contoh:**

Jika :math:`A = \{2, 4, 6\}` dan :math:`B = \{2, 3, 5\}`, maka :math:`A \oplus B = \{3, 4, 5, 6\}`.

6. Cartesian Product
====================

Cartesian product dari himpunan A dan B adalah himpunan yang elemennya semua pasangan berurutan *(ordered pairs)* yang dibentuk dari komponen pertama dari himpunan A dan komponen kedua dari himpunan B.

.. math::

   A \times B = \{(a, b) \mid a \in A \text{ dan } b \in B\}

.. sidebar:: Konteks Rekayasa Perangkat Lunak (RPL)

   * **Database Query:** Identik dengan operasi ``CROSS JOIN`` antar dua tabel.
   * **Software Testing:** Digunakan untuk *Combinatorial Test Case Generation* (menguji seluruh kombinasi matriks masukan).

**Contoh Studi Kasus RPL:**

Misalkan:
* :math:`A = \text{Himpunan Browser} = \{\text{"Chrome"}, \text{"Firefox"}\}`
* :math:`B = \text{Himpunan OS} = \{\text{"Windows"}, \text{"Linux"}, \text{"MacOS"}\}`

Maka:

.. math::

   A \times B = \{ &(\text{"Chrome"}, \text{"Windows"}), (\text{"Chrome"}, \text{"Linux"}), (\text{"Chrome"}, \text{"MacOS"}), \\
   &(\text{"Firefox"}, \text{"Windows"}), (\text{"Firefox"}, \text{"Linux"}), (\text{"Firefox"}, \text{"MacOS"})\}

*(Total 6 kombinasi skenario pengujian aplikasi web)*

.. seealso::

   Materi mengenai prinsip perhitungan kombinasi dapat dilihat di :ref:`prinsip-inklusi-eksklusi`.
