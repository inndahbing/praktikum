# import datetime
# mahasiswa1 = {
#     'nama': 'Ucup Surucup',
#     'nim': '19022001',
#     'sks_lulus': 130,
#     'beasiswa': False,
#     'lahir': datetime.datetime(2001, 4, 10)  # tahun, bulan, tanggal
# }
# mahasiswa2 = {
#     'nama': 'Azan Magrib',
#     'nim': '19022002',
#     'sks_lulus': 140,
#     'beasiswa': True,
#     'lahir': datetime.datetime(2002, 10, 10)  # tahun, bulan, tanggal
# }
# mahasiswa3 = {
#     'nama': 'Slamet Dunia Akhirat',
#     'nim': '19022003',
#     'sks_lulus': 100,
#     'beasiswa': True,
#     'lahir': datetime.datetime(1977, 5, 10)  # tahun, bulan, tanggal
# }
# data_mahasiswa = {
#     'MAH001': mahasiswa1,
#     'MAH002': mahasiswa2,
#     'MAH003': mahasiswa3,
# }
# print(f"{'KEY':<6} {'Nama':<20} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
# print("-" * 55)
# for mahasiswa in data_mahasiswa:
#     KEY = mahasiswa
#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM = data_mahasiswa[KEY]['nim']
#     SKS = data_mahasiswa[KEY]['sks_lulus']
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
#     print(f"{KEY:<6} {NAMA:<20} {SKS:<5} {str(BEASISWA):<9} {LAHIR:<10}")

# import datetime
# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }
# data_mahasiswa = {}
# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-" * 20)
# mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# print(mahasiswa)
# mahasiswa['nama'] = input("Nama Mahasiswa: ")
# mahasiswa['nim'] = input("NIM Mahasiswa: ")
# mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
# TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
# BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
# mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
# print(mahasiswa)


# import datetime
# import os
# import string
# import random

# # template dict mahasiswa
# mahasiswa_template = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }
# data_mahasiswa = {}
# while True:
#     # os.system("cls")  # untuk windows
#     os.system("clear")
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print("-" * 20)
#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())
#     mahasiswa['nama'] = input("Nama Mahasiswa: ")
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")
#     mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
#     TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
#     mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
#     KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
#     data_mahasiswa.update({KEY: mahasiswa})
#     print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
#     print('-' * 60)
#     for mahasiswa in data_mahasiswa:
#         KEY = mahasiswa
#         NAMA = data_mahasiswa[KEY]['nama']
#         NIM = data_mahasiswa[KEY]['nim']
#         SKS = data_mahasiswa[KEY]['sks_lulus']
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
#         print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
#     print("\n")
#     is_done = input("Mau tambah lagi bro (y/n)? ")
#     if is_done == "n":
#         break
# print("\nAkhir dari program, terima kasih")


import datetime
import os
import string
import random

# Template dictionary buku
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 2000,
    'tanggal_pinjam': datetime.datetime(2000, 1, 1),
    'status': 'TERSEDIA'
}
data_buku = {}        # Nesting dictionary untuk menyimpan semua data buku
indeks_buku = {}      # Multi-keys (tuple judul & tahun terbit) untuk indeks pencarian
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^50}")
    print("=" * 50)
    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku       : ")
    buku['penulis'] = input("Penulis          : ")
    buku['tahun_terbit'] = int(input("Tahun Terbit     : "))
    TAHUN_PINJAM = int(input("Tahun Terakhir Pinjam (YYYY)  : "))
    BULAN_PINJAM = int(input("Bulan Terakhir Pinjam (1-12)  : "))
    TANGGAL_PINJAM = int(input("Tanggal Terakhir Pinjam (1-31): "))
    buku['tanggal_pinjam'] = datetime.datetime(TAHUN_PINJAM, BULAN_PINJAM, TANGGAL_PINJAM)
    status_input = input("Status (TERSEDIA / TIDAK)     : ").upper()
    buku['status'] = status_input if status_input in ["TERSEDIA", "TIDAK"] else "TERSEDIA"
    # Membuat KEY acak 6 huruf kapital
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_buku.update({KEY: buku})
    # Menerapkan konsep Multi-keys menggunakan tuple (judul, tahun_terbit)
    multi_key = (buku['judul'], buku['tahun_terbit'])
    indeks_buku.update({multi_key: KEY})
    # Menampilkan tabel daftar buku
    print(f"\n{'KEYS':<8} {'JUDUL BUKU':<22} {'PENULIS':<18} {'TAHUN':<6} {'TGL PINJAM':<12} {'STATUS':<10}")
    print("-" * 82)
    for key in data_buku:
        JUDUL = data_buku[key]['judul']
        PENULIS = data_buku[key]['penulis']
        TAHUN = data_buku[key]['tahun_terbit']
        TGL_PINJAM = data_buku[key]['tanggal_pinjam'].strftime("%x")
        STATUS = data_buku[key]['status']
        print(f"{key:<8} {JUDUL:<22} {PENULIS:<18} {TAHUN:<6} {TGL_PINJAM:<12} {STATUS:<10}")
    print("\nData Multi-keys (Judul, Tahun Terbit) -> KEYS:")
    for mk, k in indeks_buku.items():
        print(f"- {mk} : {k}")
    print("\n")
    is_done = input("Mau tambah buku lagi (y/n)? ").lower()
    if is_done == "n":
        break
print("\nTerima kasih telah menggunakan Sistem Manajemen Perpustakaan!")