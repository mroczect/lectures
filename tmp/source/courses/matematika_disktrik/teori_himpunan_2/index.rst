=========================
Teori Himpunan (Bagian 2)
=========================

.. meta::
   :description: Materi Matematika Diskrit - Teori Himpunan Bagian 2 (Operasi, Inklusi-Eksklusi, dan Fuzzy).
   :keywords: matematika diskrit, himpunan, fuzzy, inklusi eksklusi, RPL

**JURUSAN TEKNIK INFORMATIKA**
Siskha Handayani

Sub Capaian Pembelajaran
=======================

Setelah menyelesaikan mata kuliah ini, mahasiswa mampu menerapkan teori himpunan untuk memodelkan data RPL dengan ketepatan ≥80%.

.. note::

   Materi ini berfokus pada bagaimana operasi himpunan dapat digunakan untuk menyelesaikan masalah rekayasa perangkat lunak (RPL) seperti analisis log data, pengujian perangkat lunak, dan sistem rekomendasi.

Sub Pokok Bahasan
=================

.. contents::
   :local:
   :depth: 1

1. :ref:`operasi-himpunan`
2. :ref:`prinsip-inklusi-eksklusi`
3. :ref:`himpunan-fuzzy`

Driving Question
================

Bagaimana seorang *software engineer* dapat menggunakan teori himpunan untuk mengubah data pengguna dan skenario pengujian menjadi informasi yang dapat digunakan oleh sistem perangkat lunak?

.. admonition:: Pertanyaan Panduan

   1. **Data pengguna:** Bagaimana menentukan pengguna yang memenuhi lebih dari satu kriteria?
   2. **Seleksi pengguna:** Bagaimana menemukan pengguna yang memenuhi kriteria tertentu tetapi tidak memenuhi kriteria lainnya?
   3. **Data testing:** Bagaimana menghasilkan seluruh kombinasi input untuk membuat test case?
   4. **Analisis data:** Bagaimana menghitung jumlah pengguna unik tanpa *double counting*?

Studi Kasus: Menganalisis Pengguna Platform Digital
===================================================

Sebuah aplikasi e-commerce mencatat aktivitas 10.000 pengguna. Dari data bulan ini:

* 6.000 pengguna mengakses melalui Mobile App
* 4.500 pengguna mengakses melalui Web
* 2.000 pengguna menggunakan keduanya
* 5.500 pengguna melakukan pembelian
* 1.500 pengguna menggunakan Mobile App dan Web serta melakukan pembelian

Tim pengembang ingin membuat dashboard analitik pengguna.

.. admonition:: Pertanyaan Analitik

   a. Berapa pengguna unik yang mengakses platform?
   b. Berapa pengguna yang hanya menggunakan Mobile App?
   c. Berapa pengguna yang hanya menggunakan Web?
   d. Bagaimana memodelkan pengguna yang menggunakan Mobile App atau Web tetapi tidak keduanya?
   e. Operasi himpunan apa yang digunakan untuk menjawab setiap pertanyaan?

.. toctree::
   :maxdepth: 2
   :caption: Materi Bagian 2

   operasi_himpunan
   prinsip_ekslusi_inklusi
   himpunan_fuzzy
