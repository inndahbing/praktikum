# ==========================================
# BAGIAN 5 - PERULANGAN DAN KONTROL ALUR
# ==========================================


# ==========================================
# PROGRAM 5.1 - FOR
# ==========================================

# Perulangan (loop)
angka = 1
print(angka)

angka = angka + 1
print(angka)

angka = angka + 1
print(angka)


# Dengan list
angka2 = [0, 1, 2, 3, 4]

print(angka2)

for i in angka2:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")


# Dengan range
angka3 = range(5)

for i in angka3:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")


# Range dari 1 sampai 9
angka4 = range(1, 10)

for i in angka4:
    print(f"i sekarang → {i}")

print("akhiri dari program\n")


# Menggunakan string
data_str = "saya ganteng abiies"

for huruf in data_str:
    print(huruf)

print("akhiri dari program\n")


# ==========================================
# PROGRAM 5.2 - WHILE LOOP
# ==========================================

# Contoh 1
print("=== contoh 1 ===")

angka = 10

# Catatan:
# Kalau kondisi ini dijalankan apa adanya,
# angka tidak berubah sehingga loop tidak berhenti.
# Jadi dibuat contoh yang aman dengan angka berkurang.

while angka > 5:
    print("ipin lari ipin!!!")
    angka -= 1


# Contoh 2
print("\n=== contoh 2 ===")

angka = 0

print(f"angka sekarang → {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang → {angka}")
    print("ipin lari ipin")

print("program berakhir, ipin sudah jauh\n")


# ==========================================
# PROGRAM 5.3 - PASS DAN CONTINUE
# ==========================================

# PASS
# pass digunakan sebagai dummy / tidak melakukan aksi

angka = 0

while angka < 5:
    angka = angka + 1

    if angka == 3:
        pass

    print(angka)


# CONTINUE
angka = 0

print(f"\nangka sekarang → {angka}")

while angka < 5:
    angka = angka + 1

    print(f"angka sekarang → {angka}")  # aksi 1

    if angka == 3:
        print("nice")
        continue

    print("whasssup")  # aksi 2

print("Pinish\n")


# ==========================================
# PROGRAM 5.4 - BREAK
# ==========================================

angka = 0

print(f"angka sekarang → {angka}")

while angka < 5:
    angka = angka + 1

    print(f"angka sekarang → {angka}")  # aksi 1

    if angka == 3:
        print("nice")
        break

    print("whasssup")  # aksi 2

print("cukup mass\n")


# ==========================================
# PROGRAM 5.5 - LATIHAN PERULANGAN
# ==========================================

# Hasil yang diinginkan:
# *
# **
# ***
# ****


# ------------------------------------------
# 1. Menggunakan FOR
# ------------------------------------------

sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1


# ------------------------------------------
# 2. Menggunakan WHILE
# ------------------------------------------

sisi = 4
count = 1

while True:
    print("*" * count)

    count += 1

    if count > sisi:
        break


# ==========================================
# LATIHAN 1
# Menampilkan bilangan ganjil dan genap
# dari 1 sampai 50
# ==========================================

print("\n=== BILANGAN GANJIL DAN GENAP ===")

print("Bilangan genap:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nBilangan ganjil:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")


# ==========================================
# LATIHAN 2
# Menampilkan bilangan prima 1 sampai 100
# ==========================================

print("\n\n=== BILANGAN PRIMA 1 - 100 ===")

for angka in range(2, 101):

    prima = True

    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            prima = False
            break

    if prima:
        print(angka, end=" ")

    