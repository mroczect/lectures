==========================================
Pertemuan 1: Intro to Web Programming
==========================================

.. meta::
   :description: Materi pertemuan 1 Pemrograman Berbasis Web - Pengenalan konsep dasar pemrograman web dan HTML5.
   :keywords: pemrograman web, HTML, client-server, HTTP

---------------------------------
Capaian Pembelajaran Pertemuan 1
---------------------------------

Setelah mengikuti pertemuan ini, mahasiswa mampu:

- Menjelaskan pengertian dan ruang lingkup pemrograman berbasis web.
- Menjelaskan konsep *client*, *server*, *browser*, *web server*, dan
  *internet* dalam aplikasi web.
- Membedakan karakteristik website statis dan aplikasi web dinamis.
- Membuat dokumen HTML sederhana menggunakan struktur dasar HTML5.

-------------------
Materi Teori
-------------------

1. **Pengenalan Pemrograman Web** — Konsep dasar web, website, aplikasi web,
   internet, dan teknologi yang digunakan untuk membangun aplikasi berbasis web.
2. **Cara Kerja Aplikasi Web** — Memahami hubungan antara browser sebagai
   client, web server sebagai penyedia layanan, request, response, dan HTTP.
3. **Web Statis vs Web Dinamis** — Perbedaan berdasarkan pengolahan data,
   interaksi pengguna, dan pemrosesan di server.
4. **Pengantar HTML5** — HTML sebagai bahasa markup untuk menyusun struktur
   dan konten halaman web.

-------------------
Materi Praktikum
-------------------

**Praktikum 1: Hello Web!**

Mahasiswa membuat halaman web pertama menggunakan HTML5 dan menampilkannya
melalui browser.

1. *Setup Environment*: Menyiapkan VS Code, browser, dan folder project.
2. *Create HTML*: Membuat file ``index.html``.
3. *First Page*: Membuat halaman profil sederhana menggunakan heading,
   paragraph, list, dan link.

---------------------
Konsep Inti
---------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Istilah
     - Penjelasan
   * - **Browser**
     - Aplikasi yang digunakan pengguna untuk mengakses dan menampilkan halaman web.
   * - **Web Server**
     - Komputer atau perangkat lunak yang menerima request dan memberikan response kepada client.
   * - **HTTP**
     - Protokol komunikasi yang digunakan dalam pertukaran data antara client dan server.
   * - **HTML**
     - Bahasa markup yang digunakan untuk membentuk struktur konten halaman web.

------------------------------
Alur Sederhana Aplikasi Web
------------------------------

.. code-block:: text

   User → Browser → Web Server → HTML Response → Browser menampilkan halaman

User mengakses URL → Browser mengirim request → Server memproses request
→ Server mengirim response → Browser menampilkan halaman web.

.. mermaid::

   sequenceDiagram
       participant U as User
       participant B as Browser
       participant S as Web Server
       U->>B: Akses URL
       B->>S: HTTP Request
       S->>B: HTML Response
       B->>U: Tampilkan halaman

------------------
Pengantar HTML
------------------

HTML (*HyperText Markup Language*) merupakan bahasa markup yang digunakan
untuk mendefinisikan struktur dan isi sebuah halaman web. HTML **bukan**
bahasa pemrograman karena tidak digunakan untuk membuat algoritma atau
melakukan proses logika.

.. note::

   **Prinsip penting:** HTML berfungsi sebagai **struktur**, CSS mengatur
   **tampilan**, sedangkan JavaScript memberikan **perilaku/interaksi**.

**Struktur HTML Dasar:**

.. code-block:: html

   <!DOCTYPE html>
   <html lang="id">
   <head>
       <meta charset="UTF-8">
       <title>Hello Web!</title>
   </head>
   <body>
       <h1>Hello Web!</h1>
       <p>Ini adalah halaman web pertama saya.</p>
   </body>
   </html>

**Elemen HTML Dasar:**

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Elemen
     - Fungsi
   * - ``<h1>``
     - Heading atau judul.
   * - ``<p>``
     - Paragraf.
   * - ``<a>``
     - Hyperlink.
   * - ``<img>``
     - Menampilkan gambar.
   * - ``<ul>`` / ``<ol>``
     - Membuat daftar.

-----------------------------
PBL Activity — Project Launch
-----------------------------

Pada pertemuan pertama, mahasiswa mulai mengenali proyek yang akan
dikembangkan selama semester. Fokus awal bukan pada menyelesaikan aplikasi,
tetapi memahami masalah, pengguna, dan bentuk aplikasi web yang akan dibangun.

**Driving Question:**

   *"Bagaimana kita dapat membangun sebuah aplikasi web yang mampu
   menyelesaikan permasalahan nyata pengguna?"*

**Aktivitas Kelompok:**

1. Identifikasi masalah sederhana di lingkungan kampus atau masyarakat.
2. Tentukan calon pengguna aplikasi.
3. Tentukan ide awal aplikasi web.
4. Tentukan informasi apa saja yang perlu ditampilkan.
5. Buat rancangan awal halaman utama menggunakan HTML sederhana.

------------------
Rangkuman
------------------

- Pemrograman web digunakan untuk membangun website dan aplikasi yang
  berjalan melalui web.
- Aplikasi web umumnya melibatkan *client*, *browser*, *server*, dan
  komunikasi melalui HTTP.
- Website statis menyajikan konten yang relatif tetap, sedangkan aplikasi web
  dinamis dapat memproses input dan data pengguna.
- HTML digunakan untuk membangun **struktur dan konten** halaman web.
- HTML bukan bahasa pemrograman, melainkan **bahasa markup**.
- Penguasaan HTML merupakan fondasi penting sebelum mempelajari CSS,
  JavaScript, backend, database, dan framework seperti Laravel.

------------------
Next Step
------------------

Pada pertemuan berikutnya, mahasiswa akan mempelajari HTML lebih mendalam,
meliputi struktur dokumen HTML5, heading, paragraph, formatting text,
hyperlink, image, list, table, serta penggunaan atribut pada elemen HTML.