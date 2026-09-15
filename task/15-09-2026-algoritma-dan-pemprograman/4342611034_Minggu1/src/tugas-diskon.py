# Tugas 2: Menghitung Harga Setelah Diskon
# 
# Buat sebuah aplikasi untuk menghitung harga sebuah barang setelah diskon. Inputan yang
# diminta ada 4 buah yaitu nama barang, jumlah barang, harga barang dan besaran diskon. Sebagai
# gambaran, hasil eksekusi program dapat menampilkan keluaran aplikasi sebagai berikut:

namaBarang = str(input("Kau Mau Beli Barang Apa ?? : "))
jumlahBarang = int(input("Oke,, Trus Ko Mau Beli Berapa ?? : "))
hargaBarang = int(input("Oke,, Trus Berapa Lah Harga Barang Per Satunya?? : "))
besarDiskon = int(input("Oke,, Trus Ko Mau Diskonya Berapa Persen (0-99) : "))

totalHargaSebelumDiskon = jumlahBarang * hargaBarang
systemBuatNguranginDiskon = besarDiskon / 100
totalYangHarusDiBayar = totalHargaSebelumDiskon * systemBuatNguranginDiskon

msg = "total yang harsu di bayar untuk barang " +namaBarang + " dan sudah terpotong oleh diskon = " +str(besarDiskon) + " adalah = Rp." +str(totalYangHarusDiBayar)
print(msg)