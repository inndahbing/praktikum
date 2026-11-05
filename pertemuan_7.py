# # daftar = list (range(0,20,5))
# # print (daftar)

# # data_gado_gad0 = (3,"indah",True)
# # print(data_gado_gad0)

# # data = list (range(0,10,3))
# # print(data)

# list = [i ** 2 for i in range (0,10) if i !=5]
# print(list)

# list_mod = [i ** 2 for i in range (0,10) if i%2 ==0]
# print (list_mod)

# list_ganjil = [i ** 2 for i in range (0,10) if i%2 !=0]
# print (list_ganjil)
 
#  manipulasi
## --- Operasi LIST ---
# index       0(-3)    1(-2)   2(-1)
# data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
# print(f"data angka = \n{data_angka}")

# # count data
# jumlah_data_4 = data_angka.count(4)
# jumlah_data_3 = data_angka.count(3)
# print(f"jumlah angka 4 = {jumlah_data_4}")
# print(f"jumlah angka 3 = {jumlah_data_3}")

# # ambil posisi data
# data = ["Rendi", "Iqbal", "Gana", "Khairil"]
# print(f"data = {data}")

# index_Iqbal = data.index("Iqbal")
# index_Gana = data.index("Gana")

# print(f"index si Iqbal = {index_Iqbal}")
# print(f"index si Gana = {index_Gana}")

# # mengurutkan list
# print(f"data angka sebelum sort = \n{data_angka}")
# data_angka.sort()
# print(f"data angka sort = \n{data_angka}")

# print(f"data = {data}")
# data.sort()
# print(f"data sort = {data}")

# # balik listnya
# data_angka.reverse()
# data.reverse()
# print(f"data di reverse \n{data_angka}")
# print(f"data di reverse \n{data}")

#menambahkan data
#insert ((posisi,item)
# bajak_laut = ["luffy","zoro","nami"]
# print(bajak_laut)

# bajak_laut.extend(bajak_laut)
# print (bajak_laut)

# kendaraan = ['motor','mobil','sepeda','bus']
# kendaraan.append ('truck')

# print(kendaraan)

# kendaraan.insert (0,'becak')
# print (kendaraan)

# kendaraan.pop()
# print (kendaraan)

# kendaraan.reverse()
# print (kendaraan)

# index_sepeda = kendaraan.index ('sepeda')
# kendaraan[index_sepeda]= 'skuter'

# jumlah_total = len(kendaraan)
# print(f"List kendaraan akhir: {kendaraan}")
# print(f"Jumlah total data di dalam list: {jumlah_total}")

## --- LIST ---

# Kumpulan data numbers
# data_angka = [1,5,2,3]
# print(data_angka)

# # Kumpulan data_string
# data_string = ["ucup","adit","siti"]
# print(data_string)

# # Kumpulan data boolean
# data_boolean = [True, False, True, True]
# print(data_boolean)

# # Kumpulan campuran
# data_campuran = [1,"bakwan",2,"cireng","ucup",True,"adit",False]
# print(data_campuran)


# ## cara alternatif membuat list
# data_range = range(0,10,2) # range(start,stop,step)
# print(data_range)
# data_list = list(data_range)
# print(data_list)

# membuat list dengan for loop, list comprehension
# list_for = [i **2 for i in range(0,10)]
# print(list_for)

# # membuat list pake for pake if
# list_for_if = [i for i in range(0,10) if i !=5]
# print(list_for_if)

# list_for_if = [i for i in range(0,10) if i %2 == 0]
# print(list_for_if)

# list_for_if = [i for i in range(0,10) if i %2 != 0]
# print(list_for_if)

# index 0(-3)  1(-2)  2(-1)
# data = ["Ucup","Adit","Dudung"]
# # Mengambil data dari list
# data_0 = data[0]
# print(f"data pertama (index 0) = {data_0}")
# data_terakhir = data[-1]
# print(f"data terakhir adalah = {data_terakhir}")
# # Mengambil jumlah data dalam list
# panjang_data = len(data)
# print(f"panjang data = {panjang_data}")

# data = ["Ucup","Adit","Dudung"]

# # Menambahkan item sesuai posisi
# print(f"data sebelum ditambah = \n{data}")

# data.insert(1,"Asep")
# print(f"data sesudah ditambah = \n{data}")

# # Menambah data di akhir list
# data.append("Ririn")
# print(f"data ditambah lagi = \n{data}")

# # Menambahkan list dengan list
# data_baru = ["Luffy","Zoro","Nami"]
# data.extend(data_baru)
# print(f"data gabungan = \n{data}")

# # Mengubah data
# data[2] = "jarwo"
# print(f"data rubah = \n{data}")

# # Menghapus data
# data.remove("Ucup")
# print(f"data hapus = \n{data}")

# # Menghapus data paling belakang
# data.pop()
# print(f"data akhir = \n{data}")

# Operasi LIST

# data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

# print(f"data angka = \n{data_angka}")

# # Count data
# jumlah_data_4 = data_angka.count(4)
# jumlah_data_3 = data_angka.count(3)

# print(f"jumlah angka 4 = {jumlah_data_4}")
# print(f"jumlah angka 3 = {jumlah_data_3}")

# # Mengambil posisi data
# data = ["Rendi","Iqbal","Gana","Khairil"]

# print(f"data = {data}")

# index_Iqbal = data.index("Iqbal")
# index_Gana = data.index("Gana")

# print(f"index si Iqbal = {index_Iqbal}")
# print(f"index si Gana = {index_Gana}")

# # Mengurutkan list
# print(f"data angka sebelum sort = \n{data_angka}")
# data_angka.sort()
# print(f"data angka sort = \n{data_angka}")

# print(f"data = {data}")
# data.sort()
# print(f"data sort = {data}")

# # Membalikkan list
# data_angka.reverse()
# data.reverse()

# print(f"data di reverse \n{data_angka}")
# print(f"data di reverse \n{data}")

# Nested LIST

# data_0 = [1,2]
# data_1 = [3,4]

# data_list_biasa = [1,2,3,4]

# print(f"list biasa = {data_list_biasa}")

# list_2D = [data_0, data_1, 6,7]
# print(f"list 2D = {list_2D}")

# # Contoh penggunaan

# peserta_0 = ["Rendi", 25, "Laki-laki"]
# peserta_1 = ["Joni", 10, "Laki-laki"]
# peserta_2 = ["Eka", 50, "Wanita"]

# list_peserta = [peserta_0, peserta_1, peserta_2]
# print(f"peserta = {list_peserta}")

# for peserta in list_peserta:
#     print(f"nama\t : {peserta[0]}")
#     print(f"umur\t : {peserta[1]}")
#     print(f"Gender\t : {peserta[2]}\n")

# kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# # a. Tambahkan truk di akhir list
# kendaraan.append('truk')
# print(kendaraan)

# # b. Sisipkan becak pada index ke-1
# kendaraan.insert(1, 'becak')
# print(kendaraan)

# # c. Hapus data paling belakang
# kendaraan.pop()
# print(kendaraan)

# # d. Ubah sepeda menjadi skuter
# kendaraan[2] = 'skuter'
# print(kendaraan)

# # e. Tampilkan jumlah total data
# panjang_data = len(kendaraan)
# print(f"Jumlah data = {panjang_data}")

# angka = [75, 80, 90, 75, 85, 100, 65]

# # a. Mencari index skor 100
# index_100 = angka.index(100)
# print(f"Index nilai 100 = {index_100}")

# # b. Menghitung jumlah skor 75
# jumlah_75 = angka.count(75)
# print(f"Jumlah nilai 75 = {jumlah_75}")

# # c. Mengurutkan list dari terkecil ke terbesar
# angka.sort()
# print(f"Angka setelah sort = {angka}")

# # d. Membalikkan urutan list
# angka.reverse()
# print(f"Angka setelah reverse = {angka}")

# menu_utama = ["Nasi Goreng", "Mie Ayam"]
# menu_tambahan = ["Kerupuk", "Es Teh"]

# # Menggabungkan list menggunakan extend()
# menu_utama.extend(menu_tambahan)

# # Menampilkan hasil gabungan
# print(f"menu gabungan = {menu_utama}")

data_barang = [
    ["Buku", 5000],
    ["Pensil", 2000],
    ["Penggaris", 3000]
]

# a. Menampilkan harga Pensil
harga_pensil = data_barang[1][1]
print(f"Harga Pensil = {harga_pensil}")

# b. Menampilkan data menggunakan perulangan
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")