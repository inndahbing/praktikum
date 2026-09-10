#luas balok
# \(L = 2 * (p * l + p * t + l * t)\)



# Program menghitung luas, volume, dan keliling bangunan

panjang = 12
lebar = 5
tinggi = 8

# Menghitung luas permukaan balok
luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Menghitung volume
volume = panjang * lebar * tinggi

# Menghitung keliling alas
keliling = 2 * (panjang + lebar)

# Menampilkan hasil
print("Panjang =", panjang)
print("Lebar =", lebar)
print("Tinggi =", tinggi)

print("Luas =", luas)
print("Volume =", volume)
print("Keliling =", keliling)

# Operasi komparasi
print("Apakah luas lebih dari 50?", luas > 50)
print("Apakah volume bernilai 480?", volume == 480)
