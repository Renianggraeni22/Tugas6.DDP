kendaraan = ["mobil", "suv", "otolix", "hitam"]
print(kendaraan)

kendaraan.append("hitam")
print(kendaraan)

kendaraan.append("empat ban")
print(kendaraan)

kendaraan.append("empat juta")
print(kendaraan)

luas = input("luas bangunan datar")
# match luas;
if luas == "1":
    s = int(input("masukan sisi: "))
    print(s * s)
elif luas == "2":
    v = 3.14
    r = int(input("masukan nilai: "))
    print(v * r * r)
elif luas == "3":
    st = 1 / 2
    a = int(input("masukan nilai: "))
    print(st * a * a)
else:
    print("tidak ditemukan, coba pilih yang lain")

