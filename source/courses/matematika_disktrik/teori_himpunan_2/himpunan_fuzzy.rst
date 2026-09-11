===============
Himpunan Fuzzy
===============

Logika Fuzzy
============

* **Penerapan Utama:** Digunakan untuk menangani masalah dengan unsur ketidakpastian *(uncertainty)* melalui konsep kebenaran sebagian.
* **Perbedaan dari Logika Klasik:**
  * **Logika Klasik:** Bernilai biner (0 atau 1, hitam atau putih, ya atau tidak).
  * **Logika Fuzzy:** Menggunakan rentang tingkat kebenaran (kontinu antara 0 dan 1).
* **Fleksibilitas Nilai:** Mengakomodasi tingkat keabuan serta ekspresi linguistik (seperti "sedikit", "lumayan", "sangat").
* **Dasar Teori:** Berhubungan dengan *fuzzy set* dan teori kemungkinan.
* **Sejarah Singkat:** Diperkenalkan oleh Dr. Lotfi Zadeh (UC Berkeley) pada tahun 1965.

Himpunan Fuzzy
==============

Di dalam teori himpunan fuzzy, keanggotaan suatu elemen di dalam himpunan dinyatakan dengan derajat keanggotaan *(membership values)* yang nilainya terletak di dalam selang :math:`[0, 1]`.

Derajat keanggotaan himpunan A ditentukan dengan fungsi keanggotaan:

.. math::

   \mu_A: X \rightarrow [0, 1]

Bandingkan dengan fungsi keanggotaan pada himpunan klasik/tegas:

.. math::

   \chi_A: X \rightarrow \{0, 1\}

Himpunan CRISP
==============

Pada himpunan tegas *(crisp)*, nilai keanggotaan suatu item :math:`x` dalam suatu himpunan himpunan :math:`A`, yang sering ditulis dengan :math:`\mu_A[x]`, memiliki 2 kemungkinan, yaitu:

* Satu (1), artinya :math:`x` adalah anggota :math:`A`.
* Nol (0), artinya :math:`x` bukan anggota :math:`A`.

**Contoh Klasik Suhu:**

Pada himpunan tegas, suhu 70°F mungkin dikategorikan sebagai "Cold" (1) dan "Hot" (0). Sedangkan pada himpunan fuzzy, suhu 70°F memiliki derajat keanggotaan tertentu pada himpunan "Cold" (misal 0.3) dan "Hot" (misal 0.7).

Aplikasi Himpunan Fuzzy dalam Software Engineering
==================================================

1. **Sistem Rekomendasi Film / E-Commerce:**
   * *Crisp:* "Suka" (1) / "Tidak Suka" (0).
   * *Fuzzy:* Derajat Ketertarikan :math:`\mu_{\text{Suka}}(\text{Film A}) = 0.85` (Sangat Disukai).
2. **Pendeteksi Email Spam / Malware Security:**
   * *Crisp:* Flag Spam (1) atau Clean (0).
   * *Fuzzy:* Spam Score Confidence Level :math:`\mu_{\text{Spam}}(\text{Email}) = 0.72` (Kategori Karantina/Suspicious).
3. **Pengukur Kualitas Perangkat Lunak (Code Quality Index):**
   * Mengklasifikasikan kompleksitas kode dari tingkat Low, Medium, hingga High Complexity berdasarkan rentang skor fuzzy.

Contoh Penerapan Himpunan Fuzzy
==============================

Pengelompokan Usia (Crisp vs Fuzzy):

* **MUDA:** umur < 35 tahun
* **PAROBAYA:** 35 ≤ umur ≤ 55 tahun
* **TUA:** umur > 55 tahun

Pada himpunan **Crisp**, usia 40 tahun masuk definitif ke kategori PAROBAYA (nilai 1) dan bukan MUDA (nilai 0).

Pada himpunan **Fuzzy**, usia 40 tahun bisa termasuk dalam himpunan MUDA dengan derajat keanggotaan:

.. math::

   \mu_{\text{MUDA}}[40] = 0.25

Dan juga termasuk dalam himpunan PAROBAYA dengan derajat keanggotaan:

.. math::

   \mu_{\text{PAROBAYA}}[40] = 0.5
