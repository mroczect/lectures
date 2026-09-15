# Tugas 1: Membuat Program Luas lingkaran
# Buatlah sebuah program sederhana untuk menghitung luas lingkaran dengan inputan jari-dari
# pengguna. Sebagai gambaran, hasil harus dapat menampilkan program yang sama persis dengan
# gambar berikut ini: (Rumus luas lingkaran = 𝞹⨉r²

PHI = 3.14

jari_jari = float(input("Masukan Nilai Buat Jari Jari	:	"))

luas_lingkaran = float(PHI) * jari_jari * jari_jari

hasil = float(luas_lingkaran)

print("Luas Lingkaran	:	"	+str(hasil))
