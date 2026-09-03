print("hello world")

#program 2.2
#variabel adalah tempat untuk menyimpan nilai
#tipe data

#1.string = menyimpan suatu karakter
#2.intenger = menyimpan bilangan bulat
#3.doublle = menyimpan bilangan desimal
#4.boolean = menyimpan true atau false

#tipe data pada python

# penamaan      
nilai_y = 15 # dengan menggunakan underscore   
juta10 = 10000000 # ini boleh   
nilaiZ = 17.5 # ini boleh    



# pemanggilan
print("Nilai y = ", nilai_y)
print("Juta 10 = ", juta10)
print("NilaiZ = ", nilaiZ)


 
#program 2.3
# a = 10, a adalah variable dengan nilai 10

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 1

print("data : ", data_integer)
print("- bertipe ", type(data_integer))


# tipe data: Angka dengan koma (float)
data_float = 1.5

print("data : ", data_float)
print("- bertipe ", type(data_float))


# tipe data: kumpulan karakter (string)
data_string = "indah"

print("data : ", data_string)
print("- bertipe ", type(data_string))


# tipe data: biner true/false (boolean)
data_bool = True

print("data : ", data_bool)
print("- bertipe ", type(data_bool))


# tipe data khusus
# bilangan kompleks
data_complex = complex(5, 6)

print("data : ", data_complex)
print("- bertipe ", type(data_complex))

#tipe data dari bahasa c
from ctypes import c_double

data_c_double = c_double (10.5)
print("data : ", data_c_double)
print("- bertipe ", type(data_c_double))

#program 2.4
#kita belajar casting
#merubah tipe data ke tipe data lain
#tipe data = int,float,str,bool

#intenger ke tipe data lain
data_integer = 9 

data_float = float(data_integer)
data_string = str(data_integer)
data_bool = bool(data_integer) #akan false jika nilai integer = 0

print("data =", data_integer, "type =", type(data_integer))
print("data =", data_string, "type =", type(data_string))
print("data =", data_bool, "type =", type(data_bool))

#ffloat ke tipe data lain
data_float = 9.2

data_integer = int(data_float)
data_string = str(data_float)
data_bool = bool(data_float) #akan false jika integer = 0

print("data =", data_integer, "type =", type(data_integer))
print("data =", data_string, "type =", type(data_string))
print("data =", data_bool, "type =", type(data_bool))

#string ke tipe data lain

data_string = "10"

data_int = int(data_string)  
data_float = float(data_string) 
data_bool = bool(data_string)    

print("data = ", data_int,",type =", type(data_int))
print("data = ", data_float,",type =", type(data_float))
print("data = ", data_bool,",type =", type(data_bool))

# input data user 
# # data yang dimasukan pasti string 
data = input("Masukkan data: ")
print("data ",data,",type =",type(data)) 
#jika kita ingin mengambil int, maka 
angka = int(input("masukkan angka: ")) 
print("data ",angka,",type =",type(angka))  