jumlah = int(input("Berapa jumlah barang yang dibeli??\n"))
harga = int(input("Berapa harga barang per item??\n"))

tanyaDiskon = input("Ada membernya kak?? (ya/tidak)\n")

if tanyaDiskon == "ya":
    member = input("Input jenis member ?? (silver/gold/platinum/diamond)\n")
    if member == "platinum":
        diskon = 75
    elif member == "gold":
        diskon = 50
    elif member == "silver":
        diskon = 25
    elif member == "diamond":
        diskon = 90
    else:
        print("Jenis member tidak dikenali. Diskon tidak diberikan")
        diskon = 0
else:
    diskon = 0
    member = ""

total = (jumlah * harga) * (100 - diskon) / 100

if member == "diamond" and total <= 50000:
    print("Selamat pesanan anda gratiss")
else:
    print("Total harga adalah Rp." + str(total))

# Maintainer  : Muhammad Riduwan Khafidi
# NIM         : 4342611034