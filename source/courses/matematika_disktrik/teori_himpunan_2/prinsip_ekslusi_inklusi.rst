.. _prinsip-inklusi-eksklusi:

====================================
Prinsip Inklusi-Eksklusi (Bagian 2)
====================================

Prinsip Inklusi-Eksklusi dalam Analisis Log Data
================================================

Studi Kasus RPL (Unique Traffic Analytics)
-----------------------------------------

Sebuah sistem e-commerce ingin menganalisis total pengguna unik *(Unique Active Users)* yang mengunjungi platform dalam satu hari:

* :math:`A` = Himpunan User yang mengakses via Mobile App, :math:`(|A| = 3500)`
* :math:`B` = Himpunan User yang mengakses via Web Browser, :math:`(|B| = 2100)`
* :math:`A \cap B` = User yang mengakses via Mobile App dan Web, :math:`(|A \cap B| = 800)`

Perhitungan Total Pengguna Unik :math:`(|A \cup B|)`:

Misalkan A dan B adalah himpunan berhingga, maka :math:`A \cup B` juga berhingga, yaitu:

.. math::

   |A \cup B| = |A| + |B| - |A \cap B|

.. math::

   |A \cup B| = 3500 + 2100 - 800 = 4800 \text{ pengguna unik}

.. tip::

   Dalam SQL, operasi ini sering diimplementasikan menggunakan ``COUNT(DISTINCT user_id)`` atau dengan ``UNION`` yang otomatis menghilangkan duplikat. Namun, memahami matematika di baliknya penting untuk optimasi query dan *indexing* basis data.
