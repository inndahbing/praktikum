
usia = int(input("Masukkan usia anda: "))

if 0 <= usia <= 12:
    print("Kategori: Anak-anak")
elif 13 <= usia <= 17:
    print("Kategori: Remaja")
elif 18 <= usia <= 59:
    print("Kategori: Dewasa")
elif usia >= 60:
    print("Kategori: Lansia")
else:
    print("Usia tidak valid!")