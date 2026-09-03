# 1. Variabel dan Tipe Data

nama = "Indah Cahya Murti"  # contoh data string
print("Nama :", nama)

umur = 17  # contoh data integer
print("Umur :", umur, "Th")

berat = 50  # contoh data float
print("Berat :", berat, "Kg")


# 2. Konversi Data


angka_string = "123456789"
angka_float = 45.67
angka_integer = 89

# Konversi string menjadi integer
angka_integer1 = int(angka_string)
print("Angka =", angka_integer1, ", type =", type(angka_integer1))

# Konversi float menjadi integer
angka_integer2 = int(angka_float)
print("Angka =", angka_integer2, ", type =", type(angka_integer2))

# Konversi integer menjadi float
angka_float1 = float(angka_integer)
print("Angka =", angka_float1, ", type =", type(angka_float1))

# Konversi integer menjadi string
angka_string1 = str(angka_integer)
print("Angka =", angka_string1, ", type =", type(angka_string1))


# ==============================
# 3. Program Input
# ==============================

Usia = int(input("Masukkan Usia: "))
print("Data", Usia, ", type =", type(Usia))

Tinggi_Badan = float(input("Masukkan Tinggi Badan: "))
print("Data", Tinggi_Badan, ", type =", type(Tinggi_Badan))

Nama = str(input("Masukkan Nama: "))
print("Data", Nama, ", type =", type(Nama))


# ==========================================
# PROGRAM 2.1
# Menampilkan output ke konsol
# ==========================================

print("Hello World")


# ==========================================
# PROGRAM 2.2
# Variabel dan Assignment
# ==========================================

# Variabel adalah tempat untuk menyimpan data
# Di Python tidak perlu melakukan deklarasi variabel terlebih dahulu

a = 10
x = 5
panjang = 1000

# Pemanggilan variabel
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)


# ==========================================
# PROGRAM 2.3
# Mengenal Tipe Data
# ==========================================

# Integer
# Tipe data berupa bilangan bulat
data_integer = 1
print("data :", data_integer)
print("- bertipe", type(data_integer))

# Float
# Tipe data berupa bilangan desimal
data_float = 1.5
print("data :", data_float)
print("- bertipe", type(data_float))

# String
# Tipe data berupa kumpulan karakter atau teks
data_string = "ucup"
print("data :", data_string)
print("- bertipe", type(data_string))

# Boolean
# Tipe data yang memiliki nilai True atau False
data_bool = True
print("data :", data_bool)
print("- bertipe", type(data_bool))

# Complex
# Tipe data untuk bilangan kompleks
data_complex = complex(5, 6)
print("data :", data_complex)
print("- bertipe", type(data_complex))


# PENAMAAN VARIABEL / IDENTIFIER

nilai_y = 15       # menggunakan underscore
juta10 = 10000000  # boleh menggunakan angka, tetapi tidak di awal
nilaiZ = 17.5      # boleh menggunakan huruf kapital

print("Nilai y =", nilai_y)
print("Juta10 =", juta10)
print("Nilai Z =", nilaiZ)


# ==========================================
# ASSIGNMENT ULANG
# ==========================================

print("Nilai a =", a)

a = 7

print("Nilai a setelah diubah =", a)


# ==========================================
# ASSIGNMENT INDIRECT
# ==========================================

b = a

print("Nilai b =", b)


# ==========================================
# PROGRAM 2.4
# KONVERSI / CASTING TIPE DATA
# ==========================================

# Casting digunakan untuk mengubah
# suatu tipe data ke tipe data lainnya

# INTEGER ke tipe data lain

data_int = 9

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data =", data_float, ", type =", type(data_float))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))


# FLOAT ke tipe data lain

data_float = 9.2

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("data =", data_int, ", type =", type(data_int))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))


# STRING ke tipe data lain

data_str = "10"

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)

print("data =", data_int, ", type =", type(data_int))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_bool, ", type =", type(data_bool))


# ==========================================
# TIPE DATA DARI BAHASA C
# ==========================================

from ctypes import c_double

data_c_double = c_double(10.5)

print("data :", data_c_double)
print("- bertipe", type(data_c_double))


# ==========================================
# PROGRAM 2.5
# MENGAMBIL INPUT DATA DARI USER
# ==========================================

# Input yang dimasukkan oleh user
# secara default akan dibaca sebagai string

data = input("Masukkan data: ")

print("data =", data, ", type =", type(data))


# Jika ingin mengambil input berupa integer,
# maka input harus dikonversi menggunakan int()

angka = int(input("Masukkan angka: "))

print("data =", angka, ", type =", type(angka))