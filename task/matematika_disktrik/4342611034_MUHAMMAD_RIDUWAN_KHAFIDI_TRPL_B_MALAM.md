# Matematika Diskrit/RPL103

## Tugas 1 Himpunan

### Jawaban Soal No 1

---

#### Point A

Diketahui :

```
𝐵 = {𝑥∣𝑥" adalah bilangan bulat" ,100 ≤ 𝑥 ≤115" dan "𝑥" habis dibagi 3" }.
```

Jawaban :

```
B : {101,102,105,108,112}
```

Untuk Menentukan himpunan B Secara enumerasi,, kita melihat semua bilangan bulat dari 100 sampe ke 115 yg habis di bagi 3

---

#### Point B

Pertanyaannya : Nyatakan himpunan 𝐴menggunakan Notasi Pembentuk Himpunan (rule-based)!

Jawaban :

```
A = {101,102,105,108,112}

A = {x | x = 101, x = 102, x = 105, x = 105, x = 112}
```

Notasi pembentukan himpunan di gunakan untuk menjelaskan anggota himpunan menggunakan suatu aturan atau kondisi tertentu kayak di data di atas itu

---

#### Point C

Soal :

Jika pengembang ingin membuat struktur data array untuk menyimpan seluruh produk unik dari
gabungan Kategori A dan B, hitung nilai kardinalitasnya!

Jawaban :

![gambar](<[image_1.png](https://raw.githubusercontent.com/mroczect/lectures/refs/heads/master/task/matematika_disktrik/image_1.png)>)

- "U" union atau gabungan

Karena kita ingin menyimpan Semua produk dan kategori A dan B, kita menggunalcen union, dan data Yang muncul tidak boleh ditulis ulang.

---

### Jawaban Soal No 2

#### Point A

Soal :

Transformasikan data log mentah di atas menjadi sebuah Himpunan yang
melambangkan himpunan pengguna unik (𝑈)!

Jawaban :

```
U =  { USR01 , USR02, USR03, USR04, USRO5)
```

Data awal merupakon log alktivitas. Jadi satu pengguna bisa muncul beberapa kali karena Melakukan klik berkali-kali karena Setiap Id di hitung 1 kali

---

#### Point B

Soal :

Tentukan nilai kardinalitasdari himpunan U tersebut

Jawaban :

```
U = 5
```

kardınalitas adalan jumlah angota dalam satu himpunan, di dalam himpuran U terdapat 5 Input yarg berbeda maka Jawabannya adalan 5

---

#### Point C

Soal :

Jelaskan secara singkat mengapa konsep kardinalitas himpunan penting dalam
perhitungan Unique Active Users (UAU) dan optimasi penyimpanan basis data!

jawban :

Yang pertama menghindari duplikasi data, Meningkatkan Query

---

### Jawaban Soal No 3

#### Point A

Soal :

Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang aktif di kedua platform sekaligus

Jawaban :

```
A n B
```

n = irison atau intersection ,Kalau kita mau cari pengguna yang aktig Kita hanya perlu menggunakan Irisan, Seperri A Irisan B

---

#### Point B

Soal :

Tuliskan notasi dan operasi himpunan untuk menentukan pengguna yang hanya aktif di salah satu platform saja.

Jawaban :

```
(A-B) U(B-A)
```

U : Union atau Gabungan untuk mencari Pengguna yang hanga aktif di Salah satu platform aja, Gunakan rumus kayak di atas trus hasilnya di gabungin.

---

### Jawaban Soal No 4

#### Point A

soal :

Hitung total jumlah pelanggan unik menggunakan Prinsip Inklusi-Eksklusi (|𝑁 ∪ 𝐷 ∪ 𝑉|).

Jawban :

```
- |N ∪ D ∪ V| = |N| + |D| + |V| - |NnV| - |DnV| + |NnDnV|

kalau udah,, suptitusikan

= 120 + 80 + 60 - 40 - 25 - 15 + 10
= 260 - 80 + 10
= 190
```

---

#### Point B

Soal :

Apa akibatnya jika kita hanya menjumlahkan total pelanggan (|𝑁| + |𝐷| + |𝑉|) tanpa memperhitungkan irisan? Jelaskan dampaknya terhadap analisis data!

Jawaban :

```
kalau kita mau jumlahin

120 + 80 + 60 = 260

jadi hasill hasilnya kan = 260

nah padahal harsunya itu = 190

Kenapa ??

karena kalau irisan ngak di perhitungkan, dia bisa jadi overcounting, atau perhitungan ganda

Jadi Prinsip inklusi - eksklusi dibuat biar jumlah pelangan itu bener bener nunjukin jumlah orng yang unik.

```

---

### Jawaban Soal No 5

Soal :

![soalno5](<[image.png](https://raw.githubusercontent.com/mroczect/lectures/refs/heads/master/task/matematika_disktrik/image.png)>)

Jawaban :

A. jadi urutan rekomendasi film itu :

```
Film C(7.0) -> Film A(0.7) -> Film C(0.5)
```

di himpunan fuzzy set, Setiap Film mempunyai nilai derajat keanggotaan antara 0 sampe 1

---

B. Karena, Fuzzy set Lebih cocok untuk system rekomendasi. karna tinggakt kesukaan manusia yang samar, atau ngak selalu, atau ngak selalu suka, atau ngak suka, dan netral.
