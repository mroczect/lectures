---
title: Pemrograman Berbasis Web
description: Materi, praktikum, dan referensi mata kuliah RPL105 — TRPL Politeknik Negeri Batam.
outline: deep
---

# RPL105 — Pemrograman Berbasis Web

Dari HTML, CSS, dan JavaScript di klien hingga PHP, MySQL, session, dan autentikasi di server — bangun aplikasi web utuh dari nol.

::: tip E-Learning
[**Buka E-Learning →**](https://learningif.polibatam.ac.id)
:::

## Peta Mata Kuliah

Dua dunia pemrograman web:

| Sisi       | Pertemuan | Fokus                                       |
| ---------- | :-------: | ------------------------------------------- |
| **Klien**  |    1–7    | HTML, CSS, JavaScript, Bootstrap, responsif |
| **Server** |   8–14    | PHP, MySQL, CRUD, session, autentikasi      |

**Benang merah:** Sisi klien = antarmuka yang dilihat pengguna. Sisi server = logika, data, dan keamanan di belakangnya. Di akhir semester keduanya bertemu dalam satu aplikasi web utuh dengan CRUD, autentikasi, dan otorisasi.

## Informasi Umum

|  Kode  | SKS |     Semester     | Status |
| :----: | :-: | :--------------: | :----: |
| RPL105 |  4  | Ganjil 2026/2027 | Wajib  |

| Bidang        | Keterangan                                 |
| ------------- | ------------------------------------------ |
| **Nama**      | Pemrograman Berbasis Web                   |
| **Prasyarat** | Tidak ada                                  |
| **Dosen**     | Noper Ardi (Koord.), Gilang Bagus Ramadhan |
| **Email**     | noperardi@polibatam.ac.id                  |

### Deskripsi

Konsep dasar web dengan **client side** (HTML, CSS, JavaScript, responsif) dan **server side** (PHP, MySQL) programming.

## Tujuan Pembelajaran

| No. | Tujuan                                                                       |
| :-: | ---------------------------------------------------------------------------- |
|  1  | Menjelaskan teknologi web & membedakan client-side vs server-side            |
|  2  | Mengimplementasikan HTML, CSS, JS untuk antarmuka interaktif                 |
|  3  | Menerapkan standar coding (deskripsi file, penamaan, dll)                    |
|  4  | Menggunakan framework front-end untuk web responsif                          |
|  5  | Menggunakan bahasa pemrograman untuk mengolah & memvalidasi data             |
|  6  | Mengimplementasikan CRUD dengan bahasa pemrograman web & basis data          |
|  7  | Mengimplementasikan pengolahan file, autentikasi, otorisasi (session/cookie) |

## Rencana Pembelajaran

### Timeline 14 Pertemuan

|    Sisi    | Pertemuan | Materi                              |
| :--------: | :-------: | ----------------------------------- |
| **Klien**  |     1     | Pengenalan Pemrograman Web          |
|            |     2     | HTML Fundamental & Form             |
|            |    3–4    | CSS Fundamental & Layout            |
|            |     5     | JavaScript Fundamental              |
|            |    6–7    | Framework Front-End & Web Responsif |
| **Server** |     8     | Dasar PHP & Method Form             |
|            |   9–10    | PHP MySQL: Koneksi & CRUD           |
|            |   11–12   | Session, Cookie & Pengolahan File   |
|            |   13–14   | Enkripsi, Autentikasi & Otorisasi   |

### Detail Per Pertemuan

| Pertemuan | Topik                 | Sub Topik                                                                  |
| :-------: | --------------------- | -------------------------------------------------------------------------- |
|     1     | Pengenalan Web        | RPS, dasar aplikasi web, tools, client vs server side                      |
|     2     | HTML & Form           | Struktur, sintaks, atribut, elemen umum, HTML5                             |
|    3–4    | CSS & Layout          | Struktur CSS, inline/internal/external, selector/class/ID, design & layout |
|     5     | JavaScript            | Struktur, tipe data, variabel, ekspresi, operator, konstanta               |
|    6–7    | Front-End & Responsif | Bootstrap, Web UI, Font Awesome, Grid, Media Query                         |
|     8     | Dasar PHP             | Variabel, kontrol, array, function, GET/POST                               |
|   9–10    | PHP + MySQL           | SQL, koneksi, CRUD, validasi, pagination, pencarian                        |
|   11–12   | Session & File        | Session/cookie, perbedaan, upload/download file                            |
|   13–14   | Auth & Otorisasi      | Konsep, implementasi PHP, hashing password                                 |

::: details Contoh Kode — HTML Form

```html
<form action="proses.php" method="POST">
  <label for="nama">Nama:</label>
  <input type="text" id="nama" name="nama" required />
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required />
  <button type="submit">Kirim</button>
</form>
```

:::

::: details Contoh Kode — CRUD PHP + MySQL

```php
<?php
// koneksi
$conn = new mysqli('localhost', 'root', '', 'rpl105');

// CREATE
$stmt = $conn->prepare("INSERT INTO mahasiswa (nama, email) VALUES (?, ?)");
$stmt->bind_param("ss", $nama, $email);
$stmt->execute();

// READ
$result = $conn->query("SELECT * FROM mahasiswa ORDER BY id DESC");

// UPDATE
$stmt = $conn->prepare("UPDATE mahasiswa SET nama = ? WHERE id = ?");
$stmt->bind_param("si", $nama, $id);
$stmt->execute();

// DELETE
$stmt = $conn->prepare("DELETE FROM mahasiswa WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
?>
```

:::

::: details Contoh Kode — Login dengan Hashing

```php
<?php
// register
$hash = password_hash($_POST['password'], PASSWORD_BCRYPT);
$stmt = $conn->prepare("INSERT INTO users (username, password_hash) VALUES (?, ?)");
$stmt->bind_param("ss", $_POST['username'], $hash);
$stmt->execute();

// login
$stmt = $conn->prepare("SELECT id, username, password_hash FROM users WHERE username = ?");
$stmt->bind_param("s", $_POST['username']);
$stmt->execute();
$user = $stmt->get_result()->fetch_assoc();

if ($user && password_verify($_POST['password'], $user['password_hash'])) {
    session_start();
    $_SESSION['user_id'] = $user['id'];
    header('Location: dashboard.php');
    exit;
}
?>
```

:::

## Proyek PBL

**Metode:** PBL + CDIO. Proyek semester 1 = _cornerstone project_.

**Kontribusi:** **Motor implementasi** — mengubah SRS dari RPL104 menjadi kode berjalan. Semua yang kamu pelajari di sini langsung dipakai di proyek PBL.

### Luaran

| Luaran                 | Deskripsi                                |
| ---------------------- | ---------------------------------------- |
| Halaman Web Statis     | HTML & CSS responsif                     |
| Halaman Web Interaktif | + JavaScript                             |
| Framework Front-End    | Bootstrap                                |
| Aplikasi CRUD          | PHP + MySQL (form, validasi, pagination) |
| Sistem Autentikasi     | Login/logout, session, password hashing  |
| Pengolahan File        | Upload/download dengan validasi MIME     |

::: warning
**Praktikum disertai aset wajib dikompres ZIP** dengan format nama: `NIM_NamaLengkap.zip`.
:::

## Metode Evaluasi

| Komponen                   | Keterangan              |
| -------------------------- | ----------------------- |
| Tugas Tertulis             | Minimal 2 per semester  |
| Ujian Lisan (Presentasi)   | 2 sesi (tengah & akhir) |
| Observasi Praktikum/Proyek | 4 sesi di laboratorium  |
| Kuis                       | Kuis 1 & 2              |

| Aktivitas           | Bobot |
| ------------------- | :---: |
| Observasi Praktikum |  40%  |
| Tugas Tertulis      |  25%  |
| Ujian Lisan         |  25%  |
| Kuis                |  10%  |

::: info
RPL105 menekankan **praktik langsung** — 4 sesi observasi praktikum adalah momen penilaian utama.
:::

### Kriteria Nilai

| Angka | Huruf | Angka | Huruf |
| :---: | :---: | :---: | :---: |
|  ≥85  |   A   | 60–64 |  C+   |
| 80–84 |  A-   | 55–59 |   C   |
| 75–79 |  B+   | 50–54 |  C-   |
| 70–74 |   B   | 45–49 |  D+   |
| 65–69 |  B-   | 40–44 |   D   |
|       |       |  <40  |   E   |

## Sarana & Prasarana

| No. | Sarana               | Jumlah |
| :-: | -------------------- | :----: |
|  1  | Komputer/PC          |   30   |
|  2  | Laboratorium         |   1    |
|  3  | VS Code / editor web |   30   |
|  4  | XAMPP / Laragon      |   30   |
|  5  | MySQL                |   30   |
|  6  | Koneksi Internet     |   1    |

## Kesepakatan

1. Wajib ikut semua kegiatan (toleransi keterlambatan maks **15 menit**).
2. Tugas dikumpulkan via e-learning.
3. **Praktikum disertai aset wajib di-ZIP** dengan nama `NIM_NamaLengkap.zip`.
4. Jaga etika moral & akademik.

## Pustaka

### Utama

1. Supono & Putratama, V. _Pemrograman Web dengan PHP dan Framework Codeigniter_. Deepublish, 2016.
2. _Responsive Web Design dengan PHP dan Bootstrap_. 2013.
3. Sianipar. _HTML 5 & CSS 3: Belajar dari Kasus_. Informatika, 2015.
4. Sunyoto, A. _AJAX: Membangun Web dengan Teknologi Asynchronous JavaScript and XML_. ANDI, 2007.
5. Sibero, A. F. K. _Kitab Suci Web Programming_. Mediakom, 2011.
6. Silver, A. H. _WordPress 3 Complete_. Packt, 2011.
7. Jubilee Enterprise. _Buku Pintar HTML5 dan CSS3_. Elex, 2012.
8. Pavlopoulos, D. _Practical Progressive Web Apps_. Packt, 2018.

### Bacaan Pendukung

- **MDN Web Docs** — referensi HTML/CSS/JS
- **PHP Manual** — dokumentasi resmi PHP
- **MySQL Documentation**
- **Bootstrap Documentation**

## Info Tambahan

Menggunakan **PBL** dengan framework **CDIO**. Proyek semester 1 = _cornerstone project_. Kontribusi utama: memberikan kemampuan dasar pemrograman berbasis web untuk proyek perangkat lunak.

## Sumber Online

### Dokumentasi Resmi

| Sumber       | Tautan                                  |
| ------------ | --------------------------------------- |
| MDN Web Docs | [Buka →](https://developer.mozilla.org) |
| PHP Manual   | [Buka →](https://www.php.net/manual)    |
| MySQL Docs   | [Buka →](https://dev.mysql.com/doc)     |
| Bootstrap    | [Buka →](https://getbootstrap.com)      |
| W3Schools    | [Buka →](https://www.w3schools.com)     |

### Tools

| Tools        | Tautan                                  |
| ------------ | --------------------------------------- |
| VS Code      | [Buka →](https://code.visualstudio.com) |
| XAMPP        | [Buka →](https://www.apachefriends.org) |
| Laragon      | [Buka →](https://laragon.org)           |
| Composer     | [Buka →](https://getcomposer.org)       |
| Google Fonts | [Buka →](https://fonts.google.com)      |

### Bacaan Tambahan

- **FreeCodeCamp — Responsive Web Design** — kursus gratis HTML/CSS terstruktur.
- **The Odin Project** — kurikulum full-stack open source.
- **Laracasts** — video pembelajaran web development.
- **PHP The Right Way** — panduan praktik terbaik PHP modern.

## Halaman Terkait

| Halaman                                        | Deskripsi                        |
| ---------------------------------------------- | -------------------------------- |
| [Mata Kuliah](/v1/courses/)                    | Daftar mata kuliah semester ini. |
| [Tugas](/v1/task/)                             | Daftar tugas.                    |
| [Jadwal Kuliah](/v1/information/jadwal-kuliah) | Jadwal mingguan.                 |
| [Info Tim PBL](/v1/information/info-team-pbl)  | Deskripsi proyek PBL.            |
