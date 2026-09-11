.. _teori-himpunan:

==============
Teori Himpunan
==============

.. contents:: Daftar Isi
   :depth: 2
   :local:

Pengantar
=========

**Teori Himpunan** adalah fondasi utama Matematika Diskrit. Hampir seluruh
topik lanjutan — relasi, fungsi, kombinatorik, logika, hingga teori graf —
dibangun di atas konsep himpunan.

Himpunan (*set*) adalah kumpulan objek-objek berbeda yang terdefinisi dengan
jelas. Objek di dalam himpunan disebut **elemen**, **unsur**, atau **anggota**.
Notasi himpunan menggunakan kurung kurawal ``{}``.

Contoh dalam konteks rekayasa perangkat lunak:

- Himpunan *user* dalam sebuah aplikasi.
- Himpunan tabel dalam sebuah *database*.
- Himpunan mahasiswa Teknik Informatika Angkatan 2025.
- Himpunan metode HTTP: ``H = {GET, POST, PUT, DELETE}``.

.. note::

   Sebelum masuk materi, kerjakan **pre-test** untuk mengukur kemampuan awal
   terkait logika dan analisis dasar.

Tujuan Pembelajaran
===================

Setelah menyelesaikan bagian ini, mahasiswa mampu:

1. Menjelaskan dan memodelkan konsep himpunan ke dalam representasi matematis
   yang sesuai dengan permasalahan teknik informatika.
2. Menunjukkan perilaku profesional (kedisiplinan, tanggung jawab akademik,
   dan ketepatan waktu) dalam penyelesaian tugas serta proyek perkuliahan
   matematika.
3. Berpartisipasi aktif dalam perkuliahan.

Daftar Modul
============

Materi Teori Himpunan dibagi menjadi empat modul berikut. Disarankan dibaca
secara berurutan.

.. toctree::
   :maxdepth: 3

   konsep_dasar_himpunan
   notasi_himpunan
   himpunan_khusus
   relasi_antar_himpunan

Ringkasan Tiap Modul
====================

Konsep Dasar Himpunan
---------------------

:doc:`konsep_dasar_himpunan`

- Definisi himpunan, elemen, dan notasi keanggotaan (``∈``, ``∉``).
- Aturan urutan dan duplikasi dalam himpunan.
- Kardinalitas himpunan (``|A|``).
- Contoh yang bukan himpunan (syarat *well-defined*).

Notasi Himpunan
---------------

:doc:`notasi_himpunan`

- **Enumerasi** — menuliskan semua elemen.
- **Simbol baku** — ``ℕ``, ``ℤ``, ``ℚ``, ``ℝ``, ``ℂ``.
- **Notasi pembentuk himpunan** — ``{x | syarat yang dipenuhi x}``.
- **Diagram Venn** — penyajian grafis.

Himpunan Khusus
---------------

:doc:`himpunan_khusus`

- **Himpunan kosong** ``∅`` — kardinalitas 0.
- **Subset** ``A ⊆ B`` — semua elemen ``A`` ada di ``B``.
- **Subset sejati** ``A ⊂ B``.
- **Himpunan kuasa** ``P(A)`` — jumlah elemen ``2^n``.

Relasi Antar Himpunan
---------------------

:doc:`relasi_antar_himpunan`

- **Himpunan sama** ``A = B`` — elemen identik.
- **Himpunan ekivalen** ``A ~ B`` — kardinalitas sama.
- Perbandingan keduanya.

Peta Konsep
===========

.. mermaid::

   flowchart TD
       A["Konsep Dasar Himpunan<br/>(definisi, elemen, |A|)"]
       B["Notasi Himpunan<br/>(4 cara penyajian)"]
       C["Himpunan Khusus<br/>(∅, ⊆, P(A))"]
       D["Relasi Antar Himpunan<br/>(A = B, A ~ B)"]

       A --> B
       A --> C
       B --> D
       C --> D

Penerapan di Rekayasa Perangkat Lunak
=====================================

Himpunan dipakai di banyak bidang RPL:

- **Basis data relasional** — tabel sebagai himpunan *record*.
- **Analitik web** — menghitung *Unique Active Users* (UAU).
- **Keamanan sistem** — pemodelan *Role-Based Access Control* (RBAC) dengan
  relasi *subset* dan *power set*.
- **Sistem rekomendasi** — *fuzzy set* untuk menyatakan derajat preferensi.
- **Optimasi penyimpanan** — menghindari duplikasi data dengan memanfaatkan
  kardinalitas.
- **Konfigurasi fitur** — *power set* untuk semua kombinasi fitur.
- **Exhaustive testing** — *power set* sebagai dasar pengujian menyeluruh.

Petunjuk Belajar
================

1. Baca modul secara berurutan: konsep dasar → notasi → himpunan khusus →
   relasi.
2. Kerjakan latihan di setiap modul.
3. Untuk topik operasi himpunan, inklusi-eksklusi, dan *fuzzy set*, baca
   materi lanjutan dari referensi.
4. Diskusikan dalam kelompok kecil (2–3 orang) atau sesuai Tim PBL.
5. Siapkan ringkasan 1 halaman (PPT atau PDF) untuk dipresentasikan.

Referensi
=========

- Munir, R., *Matematika Diskrit*, Bandung, Informatika, 2012.
- Rosen, K. H., *Discrete Mathematics and Its Applications*, McGraw-Hill.
- Susanna S. Epp, *Discrete Mathematics with Applications*, 4th Edition,
  Brooks Cole, 2010.
- Seymour Lipschutz, Marc Lipson, *Discrete Mathematics*, McGraw-Hill, 2007.
