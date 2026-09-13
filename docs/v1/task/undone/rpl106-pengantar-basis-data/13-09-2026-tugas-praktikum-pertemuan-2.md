---
title: Tugas Praktikum Pertemuan 2 — Entity Relationship Diagram
description: Tugas praktikum pemodelan data — ERD untuk sistem rumah sakit dan kantor registrasi universitas.
outline: deep
order: 2
status: Undone
grade: Pending
---

# Tugas Praktikum Pertemuan 2 — Entity Relationship Diagram

**Mata Kuliah:** RPL106 — Pengantar Basis Data  
**Pertemuan:** 2  
**Tipe:** Tugas Praktikum — Laporan + ERD  
**Deadline:** Akhir sesi praktikum  
**Status:** Not Submitted  
**Grade:** Pending

---

## Tujuan Praktikum

1. Memodelkan permasalahan di dunia nyata ke dalam model **ER**.
2. Membuat **Diagram ER** yang benar dan lengkap.

---

## Ketentuan Setoran

::: warning Wajib Dipatuhi

| Aspek          | Ketentuan                                                              |
| -------------- | ---------------------------------------------------------------------- |
| **Laporan**    | Format **Word** (`.docx`)                                              |
| **ER Diagram** | Format **draw.io** (`.drawio`)                                         |
| **Pengiriman** | **Zip/RAR** dengan nama file: `P2_NIM_KelasA/B/C/D_Pagi/Malam.zip/rar` |
| **Contoh**     | `P2_4342611034_KelasB_Malam.zip`                                       |
| **Deadline**   | Akhir sesi praktikum                                                   |

:::

---

## Soal 1 — Primary Key, Candidate Key, Superkey

Jelaskan perbedaan antara istilah:

- **Primary Key**
- **Candidate Key**
- **Superkey**

Berikan contoh untuk masing-masing istilah dalam konteks tabel database.

---

## Soal 2 — ER Diagram Rumah Sakit

Buatlah **E-R Diagram** untuk sebuah **rumah sakit** dengan:

- Himpunan **pasien** (_patients_)
- Himpunan **dokter** (_medical doctors_)

**Ketentuan:**

- Setiap pasien memiliki **log** dari berbagai **tes dan pemeriksaan** (_tests and examinations_) yang dilakukan.
- Tentukan **cardinality** yang sesuai (1:1, 1:N, M:N).
- Sertakan **atribut** yang relevan untuk setiap entitas.
- Tentukan **primary key** untuk setiap entitas.

### Panduan Entitas

| Entitas         | Contoh Atribut                                                 |
| --------------- | -------------------------------------------------------------- |
| **Pasien**      | `id_pasien` (PK), `nama`, `tanggal_lahir`, `alamat`, `no_telp` |
| **Dokter**      | `id_dokter` (PK), `nama`, `spesialisasi`, `no_sip`             |
| **Pemeriksaan** | `id_periksa` (PK), `tanggal`, `jenis`, `hasil`                 |
| **Tes**         | `id_tes` (PK), `nama_tes`, `tanggal`, `hasil`                  |

### Relasi yang Harus Dimodelkan

- Pasien **menjalani** pemeriksaan (1:N atau M:N).
- Dokter **memeriksa** pasien (1:N atau M:N).
- Pemeriksaan **menghasilkan** log tes.

---

## Soal 3 — ER Diagram Kantor Registrasi Universitas

Kantor registrasi universitas memelihara data tentang entitas berikut:

### Entitas dan Atribut

| Entitas              | Atribut                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------- |
| **Courses**          | `course_number`, `title`, `credits`, `syllabus`, `prerequisites`                               |
| **Course Offerings** | `course_number`, `year`, `semester`, `section_number`, `instructor(s)`, `timings`, `classroom` |
| **Students**         | `student_id`, `name`, `program`                                                                |
| **Instructors**      | `identification_number`, `name`, `department`, `title`                                         |

### Ketentuan Tambahan

- **Enrollment** siswa dalam courses dan **nilai** yang diberikan kepada siswa di setiap course yang mereka ikuti harus dimodelkan dengan tepat.
- Tentukan **cardinality** untuk setiap relasi.
- Dokumentasikan **asumsi** yang kamu buat tentang **mapping constraints**.

### Relasi yang Harus Dimodelkan

- Student **mengambil** Course Offering (M:N).
- Instructor **mengajar** Course Offering (1:N atau M:N).
- Course **memiliki** Course Offering (1:N).
- Course **memiliki** prerequisite (rekursif M:N).
- Enrollment **menghasilkan** grade.

---

## Format Laporan

Laporan dalam format **Word** harus memuat:

1. **Cover** — Nama, NIM, Kelas, Kode Dosen, Judul Tugas
2. **Jawaban Soal 1** — Penjelasan Primary Key, Candidate Key, Superkey + contoh
3. **Jawaban Soal 2** — ERD Rumah Sakit
   - Screenshot ERD dari draw.io
   - Penjelasan entitas, atribut, relasi
   - Asumsi yang dibuat
4. **Jawaban Soal 3** — ERD Kantor Registrasi
   - Screenshot ERD dari draw.io
   - Penjelasan entitas, atribut, relasi
   - Asumsi tentang mapping constraints
5. **Lampiran** — File `.drawio` untuk kedua ERD

---

## Konsep Kunci

### Primary Key, Candidate Key, Superkey

| Istilah           | Definisi                                               | Contoh (Mahasiswa)                     |
| ----------------- | ------------------------------------------------------ | -------------------------------------- |
| **Superkey**      | Satu atau lebih atribut yang membedakan setiap entitas | `{NIM}`, `{NIM, Nama}`, `{NIM, Email}` |
| **Candidate Key** | Superkey paling minimal                                | `{NIM}`, `{Email}`                     |
| **Primary Key**   | Candidate key yang dipilih untuk membedakan entitas    | `{NIM}`                                |

::: tip Cara Mengingat
**Superkey** → **Candidate Key** → **Primary Key**

1. Superkey: semua kombinasi atribut unik.
2. Candidate Key: yang paling minimal.
3. Primary Key: yang dipilih.
   :::

### Cardinality Notation

| Notasi | Arti         |
| :----: | ------------ |
| `1:1`  | One-to-One   |
| `1:N`  | One-to-Many  |
| `M:N`  | Many-to-Many |

### Participation Constraint

- **Total** → wajib → garis ganda.
- **Partial** → opsional → garis tunggal.

---

## Checklist Pengerjaan

### Soal 1

- [ ] Definisikan Primary Key
- [ ] Definisikan Candidate Key
- [ ] Definisikan Superkey
- [ ] Berikan contoh untuk masing-masing
- [ ] Jelaskan perbedaannya

### Soal 2 — Rumah Sakit

- [ ] Identifikasi entitas: Pasien, Dokter, Pemeriksaan, Tes
- [ ] Tentukan atribut untuk setiap entitas
- [ ] Tentukan primary key
- [ ] Tentukan relasi antar entitas
- [ ] Tentukan cardinality
- [ ] Gambar ERD di draw.io
- [ ] Screenshot dan masukkan ke laporan

### Soal 3 — Kantor Registrasi

- [ ] Identifikasi entitas: Course, Course Offering, Student, Instructor
- [ ] Tentukan atribut (termasuk multivalued: prerequisites)
- [ ] Tentukan primary key
- [ ] Tentukan relasi antar entitas
- [ ] Tentukan cardinality
- [ ] Dokumentasikan asumsi mapping constraints
- [ ] Gambar ERD di draw.io
- [ ] Screenshot dan masukkan ke laporan

### Submission

- [ ] Laporan Word (`.docx`)
- [ ] File draw.io (`.drawio`) untuk Soal 2
- [ ] File draw.io (`.drawio`) untuk Soal 3
- [ ] Zip dengan nama `P2_NIM_KelasB_Malam.zip`
- [ ] Submit sebelum akhir sesi praktikum

---

## Submission Details

| Field               | Value                            |
| ------------------- | -------------------------------- |
| **Nama**            | Muhammad Riduwan Khafidi         |
| **NIM**             | 4342611034                       |
| **Kelas**           | B Malam                          |
| **Kode Dosen**      | [Kode Dosen Praktikum]           |
| **Platform**        | E-Learning IF Polibatam          |
| **Link Submission** | [Link pengumpulan]               |
| **File Zip**        | `P2_4342611034_KelasB_Malam.zip` |

---

## Referensi

- Silberschatz, Korth, Sudarshan — _Database System Concept_, Bab 6.
- Materi Pertemuan 2 — [Data Modelling: ER-Diagram](/v1/courses/rpl106-pengantar-basis-data/materi-02-er-diagram)
- [Draw.io](https://app.diagrams.net/) — tools gratis untuk membuat ERD.

---

## Info Tugas

| Field           | Value                                     |
| --------------- | ----------------------------------------- |
| **Mata Kuliah** | RPL106 — Pengantar Basis Data             |
| **Pertemuan**   | 2                                         |
| **Topik**       | Entity-Relationship Diagram (E-R Diagram) |
| **Tipe**        | Praktikum — Laporan + ERD                 |
| **Luaran**      | Laporan Word + File draw.io               |

::: warning Pengingat
Presensi praktikum pertemuan 2 **hanya divalidasi** bagi yang mengumpulkan tugas ini. Screenshot bukti submit sebagai backup.
:::

---

## Halaman Terkait

| Halaman                                                                                                   | Deskripsi                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------- |
| [Materi Pertemuan 2 — ER-Diagram](/v1/courses/rpl106-pengantar-basis-data/materi-02-er-diagram)           | Materi lengkap ERD.         |
| [Tugas Teori Pertemuan 2](/v1/task/undone/rpl106-pengantar-basis-data/13-09-2026-tugas-teori-pertemuan-2) | Tugas teori (resume video). |
| [Tugas Aktif](/v1/task/undone/)                                                                           | Daftar semua tugas aktif.   |
| [Tugas Selesai](/v1/task/done/)                                                                           | Arsip tugas selesai.        |

---

Task index. Last updated: 2026-09-13.
