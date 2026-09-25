nt = float(input("Input nilai tugas: "))
nts = float(input("Input nilai UTS: "))
nuas = float(input("Input nilai UAS: "))

nt_ps = nt * 20 / 100
nts_ps = nts * 40 / 100
nuas_ps = nuas * 40 / 100

nilai_akhir = nt_ps + nts_ps + nuas_ps

print("Nilai akhir mahasiswa adalah " + str(nilai_akhir))

if nilai_akhir >= 85:
    print("Grade = A")
elif nilai_akhir >= 75 and nilai_akhir <= 84:
    print("Grade = B")
elif nilai_akhir >= 60 and nilai_akhir <= 74:
    print("Grade = C")
elif nilai_akhir >= 46 and nilai_akhir <= 59:
    print("Grade = D")
elif nilai_akhir <= 45:
    print("Grade = E")

# Maintainer  : Muhammad Riduwan Khafidi
# NIM         : 4342611034