Oke, aku jelaskan ulang **semua materi** dari rangkuman itu dari nol. Aku pakai pola:  
**Apa itu? → Kenapa penting? → Gimana cara kerjanya? → Contohnya apa?**  
Jadi kamu bisa paham bukan cuma hafal, tapi ngerti maksudnya.

---

# 1. Matematika Diskrit

## Apa itu Matematika Diskrit?

Matematika Diskrit adalah cabang matematika yang mempelajari **objek-objek diskrit**.

**Diskrit** artinya:

- Terdiri dari elemen-elemen yang terpisah-pisah.
- Jumlahnya berhingga atau bisa dihitung satu per satu.
- Tidak mengalir terus-menerus.

**Contoh diskrit:**

- Bilangan bulat: `{..., -2, -1, 0, 1, 2, ...}`
- Daftar user: `{Ani, Budi, Cici}`
- ID produk: `{101, 102, 105}`

**Lawan diskrit = kontinu.**
Kontinu itu mengalir, misalnya bilangan riil: `1.5`, `2.333...`, `π`, dsb.

## Kenapa penting di ilmu komputer?

Komputer menyimpan data dalam bentuk **diskrit**: bit `0` dan `1`, array, database, tabel, ID, status, dan sebagainya.  
Jadi matematika diskrit itu “bahasa dasar” untuk memodelkan data dan algoritma.

## Contoh persoalan yang pakai Matematika Diskrit

- Database relasional → pakai himpunan dan relasi.
- Enkripsi → pakai teori bilangan.
- Gerbang logika → pakai aljabar Boolean.
- GPS / rute terpendek → pakai teori graf.
- Rekomendasi / pencarian → pakai kombinatorial dan himpunan.

## Alasan belajar

1. Melatih berpikir matematis.
2. Belajar fakta matematika dan cara menerapkannya.
3. Jadi landasan untuk mata kuliah lain.

---

# 2. Gambaran Mata Kuliah

- Mata kuliah wajib, **3 SKS**, tanpa prasyarat.
- Materi: Teori Himpunan, Matriks, Relasi & Fungsi, Logika Matematika, Kombinatorial, Aljabar Boolean, Teori Bilangan, Teori Graf.

## Penilaian

| Komponen          | Persentase |
| ----------------- | ---------: |
| Tugas             |        20% |
| Kuis              |         5% |
| ATS               |        10% |
| AAS               |        15% |
| Keaktifan & sikap |        20% |
| Proyek            |        30% |

**Intinya:** nilai kamu bukan cuma dari ujian, tapi juga dari tugas, proyek, dan sikap.

---

# 3. Software Engineering Butuh Matematika?

**Ya, butuh.** Walaupun tidak semua aplikasi butuh matematika tingkat tinggi, konsep matematika membantu:

- Menganalisis efisiensi algoritma.
- Mengoptimalkan program.
- Merancang struktur data.
- Membuat sistem yang aman dan cepat.

**Contoh:**

- Kalau kamu bikin fitur “rute terdekat” di aplikasi ojek online, itu pakai graf.
- Kalau kamu bikin sistem login dan enkripsi password, itu pakai teori bilangan.
- Kalau kamu bikin filter produk, itu pakai himpunan.
- Kalau kamu bikin kondisi `if-else`, itu pakai logika Boolean.

---

# 4. Teori Himpunan

## 4.1 Apa itu Himpunan?

Himpunan adalah **kumpulan objek berbeda yang terdefinisi dengan jelas**.

- Notasi: `{ }`
- Objek di dalamnya disebut **elemen / anggota**.
- Contoh:
  - `TI = {Ani, Budi, Cici}`
  - `RPL = {Dedi, Eko}`

**Kenapa penting?**  
Karena di sistem informasi, kita sering mengelompokkan data: user, produk, transaksi, hak akses, dsb.

---

## 4.2 Cara Menyajikan Himpunan

### 1. Enumerasi

Tulis semua anggotanya.

Contoh:

```text
H = {GET, POST, PUT, DELETE}
```

**Kapan dipakai?** Kalau anggotanya sedikit dan jelas.

### 2. Simbol Baku

Simbol yang sudah standar:

- `ℕ` = bilangan asli = `{1, 2, 3, ...}`
- `ℤ` = bilangan bulat = `{..., -2, -1, 0, 1, 2, ...}`
- `ℚ` = bilangan rasional
- `ℝ` = bilangan riil
- `ℂ` = bilangan kompleks

### 3. Notasi Pembentuk Himpunan

Tulis aturan/syaratnya.

Contoh:

```text
P = {x | x adalah nomor port jaringan, x < 1024}
```

Artinya:

- `x` adalah elemen.
- `|` dibaca “dimana” atau “sedemikian sehingga”.
- Bagian kanan adalah syarat.

### 4. Diagram Venn

Gambar lingkaran untuk menunjukkan himpunan dan hubungannya.

**Contoh:**  
A = pengguna Instagram, B = pengguna TikTok.  
Irisan A dan B = pengguna yang aktif di dua-duanya.

---

# 5. Kardinalitas Himpunan

## Apa itu?

Kardinalitas = **jumlah elemen unik** dalam himpunan.

Notasi:

```text
n(A) atau |A|
```

Contoh:

```text
A = {2, 3, 5, 7, 11, 13, 17, 19}
|A| = 8
```

**Penting:** kalau ada data login:

```text
{Ani, Budi, Ani, Cici, Budi}
```

Maka himpunan uniknya = `{Ani, Budi, Cici}`.  
Kardinalitas = **3**, bukan 5.

**Kenapa penting?**

- Menghindari duplikasi data.
- Menghemat penyimpanan.
- Mempercepat query.
- Menghitung _Unique Active Users_.

---

# 6. Himpunan Khusus & Relasi Antar Himpunan

## 6.1 Himpunan Kosong

Himpunan yang tidak punya anggota.

Notasi:

```text
∅ atau { }
```

Contoh:

```text
E = {x | x < x}
|E| = 0
```

**Maksudnya:** tidak ada bilangan yang lebih kecil dari dirinya sendiri.

---

## 6.2 Subset / Himpunan Bagian

`A ⊆ B` artinya semua anggota A ada di B.

Contoh:

```text
{1, 2, 3} ⊆ {1, 2, 3, 4, 5}
```

Tapi:

```text
{1, 4} ⊄ {1, 2, 3}
```

Karena 4 tidak ada di himpunan kedua.

**Analogi:**  
Kalau `Dosen = {Input, Lihat}` dan `Admin = {Input, Edit, Hapus, Lihat}`, maka Dosen ⊆ Admin.  
Artinya semua hak akses dosen juga dimiliki admin.

---

## 6.3 Himpunan Kuasa / Power Set

Power set dari A adalah **semua himpunan bagian** dari A, termasuk `∅` dan A sendiri.

Notasi:

```text
P(A) atau 2^A
```

Jika `|A| = n`, maka:

```text
|P(A)| = 2^n
```

Contoh:

```text
A = {1, 2}
P(A) = {∅, {1}, {2}, {1, 2}}
```

**Kenapa 2^n?**  
Karena setiap elemen punya 2 pilihan: masuk atau tidak masuk.  
Kalau ada 2 elemen, total kombinasi = 2 × 2 = 4.

---

## 6.4 Himpunan yang Sama

`A = B` jika:

```text
A ⊆ B dan B ⊆ A
```

Contoh:

```text
A = {0, 1}
B = {x | x(x - 1) = 0}
```

Karena x = 0 atau x = 1, maka B = {0, 1}. Jadi A = B.

---

## 6.5 Himpunan yang Ekivalen

`A ~ B` jika jumlah anggotanya sama.

Contoh:

```text
A = {1, 3, 5, 7}
B = {a, b, c, d}
```

Keduanya punya 4 anggota, jadi A ~ B.  
Tapi isinya beda, jadi tidak sama.

---

## 6.6 Contoh RBAC

RBAC = Role-Based Access Control.

```text
HakAkses = {Input, Edit, Hapus, Lihat}
Admin     = {Input, Edit, Hapus, Lihat}
Dosen     = {Input, Lihat}
Mahasiswa = {Lihat}
```

Relasi:

```text
Mahasiswa ⊆ Dosen ⊆ Admin
```

Power set dari `{Lihat}`:

```text
P({Lihat}) = {∅, {Lihat}}
```

**Maksudnya:** mahasiswa punya 2 kemungkinan:

1. Tidak punya akses (`∅`)
2. Hanya bisa lihat (`{Lihat}`)

Ini penting untuk mencegah kebocoran hak akses.

---

# 7. Operasi Himpunan

Ini dipakai di Tugas 3.

| Operasi       | Simbol  | Arti                          | Contoh                                            |
| ------------- | ------- | ----------------------------- | ------------------------------------------------- |
| Gabungan      | `A ∪ B` | Anggota A atau B              | `{1,2} ∪ {2,3} = {1,2,3}`                         |
| Irisan        | `A ∩ B` | Anggota A dan B               | `{1,2} ∩ {2,3} = {2}`                             |
| Selisih       | `A \ B` | Anggota A yang tidak ada di B | `{1,2} \ {2,3} = {1}`                             |
| Beda simetris | `A △ B` | Hanya di salah satu           | `{1,2} △ {2,3} = {1,3}`                           |
| Komplemen     | `A^c`   | Anggota semesta yang bukan A  | Jika semesta `{1,2,3}`, `A={1}`, maka `A^c={2,3}` |

---

# 8. Prinsip Inklusi–Eksklusi

## Apa itu?

Cara menghitung gabungan himpunan **tanpa menghitung ganda**.

### 2 himpunan:

```text
|A ∪ B| = |A| + |B| - |A ∩ B|
```

### 3 himpunan:

```text
|A ∪ B ∪ C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|
```

## Kenapa?

Karena kalau kita cuma jumlahkan `|A| + |B| + |C|`, anggota yang ada di irisan akan dihitung berkali-kali.

**Contoh Tugas 4:**

```text
|N| = 120
|D| = 80
|V| = 60
|N∩D| = 40
|N∩V| = 25
|D∩V| = 15
|N∩D∩V| = 10
```

Maka:

```text
|N ∪ D ∪ V| = 120 + 80 + 60 - 40 - 25 - 15 + 10
             = 190
```

Jadi total pelanggan unik = **190**.

Kalau hanya dijumlahkan:

```text
120 + 80 + 60 = 260
```

Itu salah, karena orang yang langganan Netflix + Disney+ dihitung dua kali.

---

# 9. Himpunan Fuzzy

## Apa itu?

Himpunan fuzzy adalah himpunan yang anggotanya punya **derajat keanggotaan** antara 0 sampai 1.

- Himpunan biasa: anggota = 1, bukan anggota = 0.
- Himpunan fuzzy: bisa 0.7, 0.5, 0.2, dst.

## Contoh Tugas 5

```text
Suka banget = 1
Suka        = 0.7
Netral      = 0.5
Tidak suka  = 0.2
```

Penilaian:

```text
Film A = Suka        = 0.7
Film B = Netral      = 0.5
Film C = Suka banget = 1
```

Urutan rekomendasi:

```text
Film C > Film A > Film B
```

**Kenapa fuzzy lebih cocok?**  
Karena selera orang tidak hitam-putih. Kadang “suka banget”, kadang “suka”, kadang “netral”. Himpunan biasa tidak bisa menangkap nuansa itu.

---

# 10. Full Review Tugas 1–5

## Tugas 1

Diketahui:

```text
A = {101, 102, 105, 108, 112}
B = {x | x bilangan bulat, 100 ≤ x ≤ 115, x habis dibagi 3}
```

**a. B dengan enumerasi:**

```text
B = {102, 105, 108, 111, 114}
```

**b. A dengan notasi pembentuk himpunan:**

```text
A = {x | x ∈ ℤ, x = 101 ∨ x = 102 ∨ x = 105 ∨ x = 108 ∨ x = 112}
```

**c. Kardinalitas gabungan:**

```text
A ∪ B = {101, 102, 105, 108, 111, 112, 114}
|A ∪ B| = 7
```

---

## Tugas 2

Log:

```text
USR01, USR05, USR02, USR01, USR03, USR05, USR01, USR04, USR02
```

**a. Himpunan unik:**

```text
U = {USR01, USR02, USR03, USR04, USR05}
```

**b. Kardinalitas:**

```text
|U| = 5
```

**c. Kenapa penting?**  
Karena untuk menghitung _Unique Active Users_, user yang sama tidak boleh dihitung berkali-kali. Kalau salah, data analitik jadi kacau.

---

## Tugas 3

Misal:

```text
A = pengguna aktif Instagram
B = pengguna aktif TikTok
```

**a. Aktif di kedua platform:**

```text
A ∩ B
```

**b. Hanya aktif di salah satu:**

```text
A △ B = (A \ B) ∪ (B \ A)
```

---

## Tugas 4

Sudah dijelaskan di bagian Inklusi–Eksklusi.

**a. Total unik:**

```text
|N ∪ D ∪ V| = 190
```

**b. Kalau tanpa irisan:**

```text
260
```

Itu _overestimate_. Analisis jadi salah.

---

## Tugas 5

Urutan rekomendasi:

```text
Film C > Film A > Film B
```

Alasannya: fuzzy cocok untuk preferensi bertingkat.

---

# 11. Kesimpulan Cepat

- **Matematika Diskrit** = dasar ilmu komputer.
- **Himpunan** = cara memodelkan kumpulan data.
- **Kardinalitas** = jumlah elemen unik.
- **Subset, power set, himpunan kosong, sama, ekivalen** = relasi dasar antar himpunan.
- **Operasi himpunan** = gabungan, irisan, selisih, beda simetris.
- **Inklusi–Eksklusi** = menghitung gabungan tanpa double count.
- **Fuzzy** = himpunan dengan derajat keanggotaan.

Kalau kamu paham bagian himpunan ini, materi berikutnya seperti **relasi, fungsi, logika, kombinatorial, aljabar Boolean, teori bilangan, dan graf** akan terasa lebih masuk akal.

Kalau mau, aku bisa lanjut buatkan **versi penjelasan per bagian yang lebih pendek** atau **latihan soal tambahan** untuk tiap topik.
