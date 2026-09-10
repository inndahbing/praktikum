# + -* /

# Operasi aritmatika

a = 10
b = 3

# Operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# Operasi kurang -
hasil = a - b
print(a, '-', b, '=', hasil)

# Operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# Operasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Operasi modulus %
hasil = a % b
print(a, '%', b, '=', hasil)

# Operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

# Latihan konversi satuan temperatur
# Program konversi Celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam Celcius : "))

print("Suhu adalah", celcius, "Celcius")

# Reamur
reamur = (4 / 5) * celcius
print("Suhu dalam Reamur adalah", reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu dalam Fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah", kelvin, "Kelvin")

# Operasi komparasi
# Setiap hasil dari operasi komparasi adalah Boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print("=============== lebih besar dari (>)")

hasil = a > 3
print(a, '>', 3, '=', hasil)

hasil = b > 3
print(b, '>', 3, '=', hasil)

hasil = b > 2
print(b, '>', 2, '=', hasil)


# Kurang dari <
print("=============== kurang dari (<)")

hasil = a < 3
print(a, '<', 3, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

hasil = b < 2
print(b, '<', 2, '=', hasil)


# Lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")

hasil = a >= 3
print(a, '>=', 3, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

hasil = b >= 2
print(b, '>=', 2, '=', hasil)


# Kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")

hasil = a <= 3
print(a, '<=', 3, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

hasil = b <= 2
print(b, '<=', 2, '=', hasil)


# Sama dengan ==
print("=============== sama dengan (==)")

hasil = a == 4
print(a, '==', 4, '=', hasil)

hasil = b == 4
print(b, '==', 4, '=', hasil)


# Tidak sama dengan !=
print("=============== tidak sama dengan (!=)")

hasil = a != 4
print(a, '!=', 4, '=', hasil)

hasil = b != 4
print(b, '!=', 4, '=', hasil)


# 'is' sebagai komparasi object identity
x = 5
y = 5

hasil = x is y
print('x is y =', hasil)


# 'is not' sebagai komparasi object identity
x = 5
y = 6

hasil = x is not y
print('x is not y =', hasil)

