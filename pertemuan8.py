# data_tuple = (1,2,3,4,5)
# print(data_tuple)
# print(data_tuple[3])

# data_sets = {10,4,3,2}
# print(data_sets)

# data_mahasiswa = ["ucup",66666,"Sastra Mesin","79","Pria","Rombel 1"]
# data_manusia = {
#     "nama" : "ucup",
#     "npm" : 66666,
#     "prodi" :"Sastra Mesin",
#     "usia" : 79,
#     "jk" : "Pria",
#     "rombel" : "Rombel 1"
# }

# print(data_manusia["nama"])

# KEY = "ucup"
# CHECKKEY = KEY in data_manusia
# print (f"apakah {KEY} ada di data_manusia: {CHECKKEY}")

# data_mahasiswa = {
#     "nama" : "Siti",
#     "umur" : 12,
#     "jk" : "Pria",
#     "bb" : 30,
#     "tb" : 90
# }

# for mahasiswa in data_mahasiswa.values():
#     print (mahasiswa)

# for mahasiswa in data_mahasiswa.keys():
#     print (mahasiswa)

# for mahasiswa in data_mahasiswa.items():
#     print (mahasiswa)

# for key, value in data_mahasiswa.values():
#     print ("key = {key}, value = {value}")

# LIST
# menggunakan kurung siku
# data_list = [10, 2, 4, 3, 2]
# print(data_list)

# # TUPLES
# data_tuples = (7, 8, 10, 11)
# print(data_tuples)
# print(data_tuples[1])

# # Tidak bisa dilakukan karena tuple bersifat immutable
# # data_tuples[1] = "ucup"
# # data_tuples.append(1)

# # SETS (himpunan)
# data_sets = {10, 4, 3, 2, 7, 6, 5}
# print(data_sets)

# # Set tidak bisa diakses menggunakan indeks
# # print(data_sets[0])


# # 

# # List
# data_list = ['ucup', 'rendi', 'salsa']
# print(data_list[0])
# # Dictionary
# data_dict = {
#     'key': 'value',
#     'cp': 'ucup',
#     'rd': 'rendi',
#     'sl': 'salsa',
#     'nmbr': 100,
#     'list': data_list
# }
# print(data_dict['cp'])
# print(data_dict['nmbr'])
# print(data_dict['list'])


# data_dict = {
#     "cup": "ucup surucup",
#     "pet": "opet saripet",
#     "ndo": "nando surundo"
# }
# # Menghitung panjang dictionary
# LENDICT = len(data_dict)
# print(f"panjang dictionary: {LENDICT}")
# # Mengecek key
# KEY = "cup"
# CHECKKEY = KEY in data_dict
# print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")
# # Mengakses value
# print(data_dict["cup"])
# print(data_dict.get("cup"))
# print(data_dict.get("kis", "key tidak ditemukan"))
# # Mengubah data
# data_dict["cup"] = "ucup si ganteng"
# print(data_dict)
# # Menambahkan data
# data_dict["de"] = "ade si adek"
# print(data_dict)
# data_dict.update({"cup": "ucup surucup"})
# print(data_dict)
# data_dict.update({"iwn": "iwan mang keren"})
# print(data_dict)
# # Menghapus data
# del data_dict["iwn"]
# print(data_dict)

# teman_teman = {
#     "cup": "ucup surucup",
#     "tong": "sotong surotong",
#     "lur": "lur sedulur",
#     "wel": "bung towel"
# }
# # Menampilkan key
# for teman in teman_teman:
#     print(teman)
# # Mengambil semua key
# keys = teman_teman.keys()
# print(keys)
# for key in teman_teman.keys():
#     print(teman_teman.get(key))
# # Mengambil semua value
# values = teman_teman.values()
# print(values)
# for value in teman_teman.values():
#     print(value)
# # Mengambil key dan value
# items = teman_teman.items()
# print(items)
# for item in teman_teman.items():
#     print(item)
# # Menampilkan key dan value bersamaan
# for key, value in teman_teman.items():
#     print(f"key = {key}, value = {value}")

# Membuat tuple mahasiswa
# mahasiswa = (
#     "Indah Cahya Murti",
#     "2605060020",
#     "Teknologi Informasi"
# )

# # Menampilkan NIM dan Prodi
# print("NIM:", mahasiswa[1])
# print("Prodi:", mahasiswa[2])

# # Mencoba mengubah isi tuple
# # mahasiswa[2] = "Teknologi Informasi"

# # Membuat set angka
# nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}

# print("Nilai angka:", nilai_angka)


# Membuat dictionary mahasiswa
# data_mahasiswa = {
#     "nim": "240101",
#     "nama": "Budi Santoso",
#     "prodi": "Teknologi Informasi"
# }

# # Menampilkan data awal
# print("Data awal:")
# print(data_mahasiswa)

# # Mengubah prodi
# data_mahasiswa["prodi"] = "Sastra Mesin"

# # Menambahkan angkatan
# data_mahasiswa["angkatan"] = 2026

# print("\nData setelah diubah:")
# print(data_mahasiswa)

# # Menghapus data NIM
# del data_mahasiswa["nim"]

# print("\nData akhir:")
# print(data_mahasiswa)

# Membuat dictionary keranjang
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}

# Menampilkan nama buah dan harga
print("Daftar Harga Buah:")

for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")

# Menghitung total belanja
total_belanja = sum(keranjang.values())

print("\nTotal belanja: Rp", total_belanja)