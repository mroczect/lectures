---
title: Pengantar Basis Data
description: Materi, praktikum, dan referensi mata kuliah RPL106 — TRPL Politeknik Negeri Batam.
layout: home

hero:
  name: RPL106
  text: Pengantar Basis Data
  tagline: Dari konsep data hingga query SQL kompleks — rancang, bangun, dan kelola basis data relasional sebagai solusi nyata.
  actions:
    - theme: brand
      text: Rencana Belajar
      link: '#rencana-pembelajaran'
    - theme: alt
      text: Tujuan
      link: '#tujuan-pembelajaran'
    - theme: alt
      text: E-Learning
      link: https://learningif.polibatam.ac.id

features:
  - title: 3 SKS
    details: Mata kuliah wajib Semester 1 (Ganjil 2026/2027), tanpa prasyarat.
  - title: ERD, EERD & SQL
    details: Cakupan lengkap pemodelan data, pemetaan relasional, dan SQL (DDL, DML, DCL).
  - title: Mini Project PBL
    details: Proyek cornerstone — dari ERD hingga query SQL untuk aplikasi nyata.
---

::: tip E-Learning
[**Buka E-Learning →**](https://learningif.polibatam.ac.id)
:::

## Peta Mata Kuliah

| Fase          | Pertemuan | Fokus                                 |
| ------------- | :-------: | ------------------------------------- |
| **Konsep**    |     1     | Basis data relasional                 |
| **Pemodelan** |    2–5    | ER, EER, pemetaan ke skema relasional |
| **SQL**       |   6–10    | DDL, DML, query lanjut, DCL           |
| **Lanjutan**  |   11–14   | Multimedia database, mini project PBL |

**Benang merah:** Memahami (Konsep) → Merancang (Pemodelan) → Membangun & mengelola (SQL) → Menerapkan (Lanjutan + Mini Project).

## Informasi Umum

|  Kode  | SKS |     Semester     | Status |
| :----: | :-: | :--------------: | :----: |
| RPL106 |  3  | Ganjil 2026/2027 | Wajib  |

| Bidang         | Keterangan                                            |
| -------------- | ----------------------------------------------------- |
| **Nama**       | Pengantar Basis Data                                  |
| **Prasyarat**  | Tidak ada                                             |
| **Dosen**      | Ahmadi Irmansyah Lubis (Koord.), Muhamad Sahrul Nizan |
| **Email / HP** | ahmadi@polibatam.ac.id / 082273083850                 |

### Deskripsi

Membangun pemahaman konsep dasar basis data dan kemampuan membangun basis data sebagai solusi. Meliputi: pengenalan basis data, konsep relational table, pemodelan data (ERD, EERD), pemetaan ke skema relasional, dan SQL (DDL, DML, DCL).

## Tujuan Pembelajaran

| No. | Tujuan                                                           |
| :-: | ---------------------------------------------------------------- |
|  1  | Menjelaskan konsep data, basis data, dan teknologi terkini       |
|  2  | Menjelaskan konsep pemodelan data relasional                     |
|  3  | Memodelkan permasalahan ke model data relasional                 |
|  4  | Merancang & mengimplementasikan basis data relasional            |
|  5  | Menjelaskan, mengoperasikan, menerapkan konsep query             |
|  6  | Mengimplementasikan query untuk membangun & mengelola basis data |
|  7  | Menganalisis permasalahan untuk memilih solusi basis data tepat  |

## Rencana Pembelajaran

### Timeline 14 Pertemuan

|     Fase      | Pertemuan | Materi                              |
| :-----------: | :-------: | ----------------------------------- |
|  **Konsep**   |     1     | Pengenalan Basis Data               |
| **Pemodelan** |     2     | Pemodelan Data (ER)                 |
|               |     3     | Pemodelan Data Lanjut (EER)         |
|               |    4–5    | Pemodelan Data Relasional           |
|    **SQL**    |     6     | DDL — CREATE, ALTER, DROP           |
|               |     7     | DML Dasar — INSERT, UPDATE, DELETE  |
|               |    8–9    | DML Lanjut — SELECT, JOIN, GROUP BY |
|               |    10     | DCL — VIEW, GRANT, REVOKE           |
| **Lanjutan**  |   11–12   | Multimedia Database                 |
|               |   13–14   | Review Mini Project PBL             |

### Detail Per Pertemuan

| Pertemuan | Topik                  | Sub Topik                                             |
| :-------: | ---------------------- | ----------------------------------------------------- |
|     1     | Pengenalan Basis Data  | Konsep dasar, basis data relasional                   |
|     2     | Pemodelan Data (ER)    | Kategorisasi, model ER, komponen, studi kasus         |
|     3     | Pemodelan Lanjut (EER) | Enhanced ER, inheritance, specialization, aggregation |
|    4–5    | Pemodelan Relasional   | Model relasional, pemetaan ER/EER ke skema            |
|     6     | SQL — DDL              | CREATE, ALTER, DROP                                   |
|     7     | SQL — DML Dasar        | INSERT, UPDATE, DELETE                                |
|    8–9    | SQL — DML Lanjut       | SELECT, JOIN, GROUP BY, HAVING, subquery, CASE        |
|    10     | SQL — DCL              | VIEW, GRANT, REVOKE                                   |
|   11–12   | Multimedia Database    | Manage type data file (BLOB/path)                     |
|   13–14   | Mini Project PBL       | Finalisasi & presentasi                               |

::: details Contoh Kode — Pemetaan ER ke Skema Relasional

```sql
CREATE TABLE mahasiswa (
    nim     VARCHAR(10) PRIMARY KEY,
    nama    VARCHAR(100) NOT NULL,
    prodi   VARCHAR(50)
);

CREATE TABLE mata_kuliah (
    kode_mk VARCHAR(10) PRIMARY KEY,
    nama_mk VARCHAR(100) NOT NULL,
    sks     INT CHECK (sks BETWEEN 1 AND 6)
);

CREATE TABLE krs (
    nim     VARCHAR(10),
    kode_mk VARCHAR(10),
    nilai   CHAR(2),
    PRIMARY KEY (nim, kode_mk),
    FOREIGN KEY (nim) REFERENCES mahasiswa(nim),
    FOREIGN KEY (kode_mk) REFERENCES mata_kuliah(kode_mk)
);
```

:::

::: details Contoh Kode — Query Kompleks

```sql
-- INNER JOIN
SELECT m.nim, m.nama, k.nama_mk, krs.nilai
FROM mahasiswa m
INNER JOIN krs ON m.nim = krs.nim
INNER JOIN mata_kuliah k ON krs.kode_mk = k.kode_mk;

-- LEFT JOIN + GROUP BY
SELECT m.nim, m.nama, COUNT(krs.kode_mk) AS jumlah_mk
FROM mahasiswa m
LEFT JOIN krs ON m.nim = krs.nim
GROUP BY m.nim, m.nama;

-- Subquery
SELECT nama FROM mahasiswa WHERE nim IN (
    SELECT nim FROM krs WHERE nilai = 'A'
);

-- CASE
SELECT nama, nilai,
       CASE
           WHEN nilai = 'A' THEN 'Sangat Baik'
           WHEN nilai = 'B' THEN 'Baik'
           ELSE 'Perlu Perbaikan'
       END AS kategori
FROM krs;
```

:::

::: details Contoh Kode — DCL & View

```sql
CREATE VIEW v_mahasiswa_trpl AS
SELECT nim, nama, angkatan
FROM mahasiswa WHERE prodi = 'TRPL';

CREATE USER 'asisten'@'localhost' IDENTIFIED BY 'password_kuat';
GRANT SELECT, INSERT ON akademik.mahasiswa TO 'asisten'@'localhost';
REVOKE INSERT ON akademik.mahasiswa FROM 'asisten'@'localhost';
```

:::

## Proyek PBL

**Metode:** PBL + CDIO. Semester 1 fokus pada tahap **Implement** & **Operate**.

**Kontribusi:** **Tulang punggung data** — semua entitas di SRS dari RPL104 dimodelkan di sini, lalu diimplementasikan sebagai database nyata untuk RPL105.

### Luaran

| Luaran               | Deskripsi                                    |
| -------------------- | -------------------------------------------- |
| **ERD**              | Entity-Relationship Diagram lengkap          |
| **EERD**             | Enhanced ER jika ada inheritance/aggregation |
| **Skema Relasional** | Pemetaan ER/EER ke tabel                     |
| **Script DDL**       | SQL untuk struktur database                  |
| **Script DML**       | Sample data & query aplikasi                 |
| **View**             | Menyederhanakan query kompleks               |
| **Dokumentasi**      | Laporan lengkap                              |
| **Presentasi Demo**  | Demonstrasi database                         |

::: warning
Mini Project **wajib menyertakan script SQL yang dapat dijalankan ulang dari nol** — memastikan database dapat direproduksi.
:::

## Metode Evaluasi

| Metode                                          | Bobot | Penilai        |
| ----------------------------------------------- | :---: | -------------- |
| Partisipasi aktif (teamwork, kontribusi, etika) |  40%  | Manajer Proyek |
| Hasil proyek (laporan, presentasi, produk)      |  60%  | Dosen Pengajar |
| Kognitif Tugas                                  |  15%  | Dosen          |
| Kognitif ATS                                    |  10%  | Dosen          |
| Kognitif AAS                                    |  10%  | Dosen          |
| Kuis                                            |  5%   | Dosen          |

::: danger Kebijakan Khusus — Wajib Dibaca
**Jika ada komponen penilaian bernilai nol (0), nilai akhir otomatis E.**

**Jika lebih dari satu komponen nol, mahasiswa harus mengulang mata kuliah di tahun ajaran baru.**

Jangan mengosongkan komponen apa pun — termasuk partisipasi, tugas, kuis, ATS, dan AAS.
:::

### Bentuk Asesmen

::: details Kognitif ATS (Teori & Praktik)
**Fokus:** Konsep pertemuan 1–7 (pengenalan, pemodelan ER/EER, pemetaan relasional, DDL, DML dasar).

**Bentuk:** Teori (pilihan ganda/esai) + Praktik (ERD, skema relasional, query SQL).
:::

::: details Kognitif AAS (Teori & Praktik)
**Fokus:** Konsep pertemuan 8–14 (DML lanjut, DCL, multimedia database, mini project).

**Bentuk:** Teori + Praktik (query kompleks, demo mini project).
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

| No. | Sarana                       |   Jumlah   |
| :-: | ---------------------------- | :--------: |
|  1  | Komputer/PC                  |     30     |
|  2  | Laboratorium                 |     1      |
|  3  | XAMPP (Apache + MySQL + PHP) |     30     |
|  4  | Visual Studio Code           |     30     |
|  5  | draw.io (untuk ERD/EERD)     | 1 (online) |
|  6  | Koneksi Internet             |     1      |

## Tools

| Tool                                                         | Fungsi                         |
| ------------------------------------------------------------ | ------------------------------ |
| [XAMPP](https://www.apachefriends.org/)                      | Database & Web Server          |
| [VS Code](https://code.visualstudio.com/)                    | Text Editor                    |
| [draw.io](https://app.diagrams.net/)                         | Diagramming & ERD              |
| [MySQL Workbench](https://www.mysql.com/products/workbench/) | GUI MySQL (opsional)           |
| [DBeaver](https://dbeaver.io/)                               | Universal DB Client (opsional) |

## Kesepakatan

1. Wajib ikut semua kegiatan (toleransi keterlambatan maks **15 menit**).
2. Tugas dikumpulkan via e-learning.
3. **Setiap komponen penilaian wajib diisi** — nilai nol di komponen manapun → nilai akhir E.
4. Jaga etika moral & akademik.

::: tip Tips Belajar

- **Praktik setiap minggu** — jangan hanya baca SQL, jalankan di XAMPP.
- **Mulai proyek dari ERD** — kesalahan di sini merambat ke seluruh implementasi.
- **Biasakan SQL dengan format rapi** — indentasi dan komentar.
- **Simpan semua script** (DDL, DML, query) dalam satu folder terstruktur.

:::

## Pustaka

### Utama

1. Silberschatz, A. et al. _Database System Concepts_. McGraw-Hill, 1997.
2. Yanto, R. _Manajemen Basis Data Menggunakan MySQL_. Deepublish, 2016.
3. Jayanti, N. K. D. A. & Sumiari, N. K. _Teori Basis Data_. Andi, 2018.
4. Connolly, T. & Begg, C. _Database Systems_, 6th ed. Pearson, 2015.
5. Lubis, A. I. et al. _Kitab Basis Data_. Polibatam Press, 2025.

### Pendukung

- Tiwari, S. _Professional NoSQL_. Wiley, 2011.
- Widodo, A. W. & Kurnianingtyas, D. _Sistem Basis Data_. UB Press, 2017.
- Taylor, A. G. _SQL for Dummies_. Wiley, 2018.
- Sianipar, R. H. _Pemrograman Database Menggunakan MySQL_. ANDI, 2016.

## Sumber Online

### Dokumentasi Resmi

| Sumber          | Tautan                                             |
| --------------- | -------------------------------------------------- |
| MySQL Docs      | [Buka →](https://dev.mysql.com/doc/)               |
| MariaDB Docs    | [Buka →](https://mariadb.com/kb/en/documentation/) |
| PostgreSQL Docs | [Buka →](https://www.postgresql.org/docs/)         |
| MongoDB Docs    | [Buka →](https://docs.mongodb.com/)                |
| W3Schools SQL   | [Buka →](https://www.w3schools.com/sql/)           |

### Tools & Playground

| Tools                                                        | Kegunaan              |
| ------------------------------------------------------------ | --------------------- |
| [XAMPP](https://www.apachefriends.org/)                      | DB + Web Server lokal |
| [Laragon](https://laragon.org/)                              | Alternatif XAMPP      |
| [MySQL Workbench](https://www.mysql.com/products/workbench/) | GUI MySQL             |
| [DBeaver](https://dbeaver.io/)                               | Universal DB Client   |
| [draw.io](https://app.diagrams.net/)                         | ERD online            |
| [dbdiagram.io](https://dbdiagram.io/)                        | ERD berbasis teks     |
| [SQL Fiddle](http://sqlfiddle.com/)                          | Playground SQL        |

### Bacaan Tambahan

- **SQLBolt** — tutorial SQL interaktif untuk pemula.
- **Mode Analytics — SQL Tutorial** — untuk analisis data.
- **Use The Index, Luke!** — panduan index & performa SQL.
- **Vertabelo Academy** — kursus desain database.

## Halaman Terkait

| Halaman                                                                      | Deskripsi                        |
| ---------------------------------------------------------------------------- | -------------------------------- |
| [Mata Kuliah](/v1/courses/)                                                  | Daftar mata kuliah semester ini. |
| [Tugas RPL106](/v1/task/semester-1-rpl106-introduction-to-database-concepts) | Tugas Resume Video Pertemuan 1.  |
| [Info Tim PBL](/v1/information/info-team-pbl)                                | Deskripsi proyek PBL.            |
| [Jadwal Kuliah](/v1/information/jadwal-kuliah)                               | Jadwal mingguan.                 |
