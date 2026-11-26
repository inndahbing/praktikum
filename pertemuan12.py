import math


# ==========================================
# 1. PENGENALAN FUNGSI
# ==========================================
def hello_world():
    # menampilkan hello world
    print("hello world")
    print("Kepada Fauzan Zein")
    print("Dan juga kepada Faza Biri Biri")


hello_world()


# ==========================================
# 2. FUNGSI DENGAN ARGUMEN
# ==========================================
def hello_world_nama(nama):
    # fungsi hello world menerima input dengan variabel nama
    print(f"Selamat datang di Dunia, {nama}")


hello_world_nama("ucup")


def tambah_cetak(angka_1, angka_2):
    # fungsi tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah_cetak(1, 8)


def say_hi(list_peserta):
    # fungsi say hi
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Selamat datang {peserta}")


kumpulan_mahasiswa = ["Budi", "Tono", "Joko"]
say_hi(kumpulan_mahasiswa)


# ==========================================
# 3. FUNGSI DENGAN RETURN
# ==========================================
def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat


y = kuadrat(5)
print(y)
print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)


def fungsi_tambah(angka_1, angka_2):
    # fungsi return dengan multi input
    return angka_1 + angka_2


a = fungsi_tambah(10, 8)
print(a)


def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah, kurang, kali, bagi


k, l, m, n = operasi_matematika(9, 5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")


# ==========================================
# 4. DEFAULT ARGUMEN & LATIHAN TAMBAHAN
# ==========================================
# contoh 1
def say_hello(nama="Ojul"):
    print(f"Hello {nama}")


say_hello("Ucup")
say_hello()


# contoh 2
def sapa_dia(nama, pesan="Apa kabar?"):
    # fungsi dengan satu input biasa, dan satu default arg
    print(f"hai {nama}, {pesan}")


sapa_dia("Nanda", "Selamat pagi")
sapa_dia("Budi")


# contoh 3
def hitung_pangkat(angka, pangkat):
    hasil = angka ** pangkat
    return hasil


print(hitung_pangkat(2, 4))
hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)


# contoh 4
def faktorial(input_1=1, input_2=2, input_3=3, input_4=4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil


print(faktorial())
print(faktorial(input_3=10))


# latihan / percobaan tambahan
def sapa_orang(siapa="pak awan", pesan="mie ayam"):
    print(f"Hello {siapa}! Aku mau titip {pesan}")


sapa_orang("Izzudin", "jangan bolos")
sapa_orang(pesan="bakso")


def tambah(x, y):
    hasil = x + y
    return hasil


akhir = tambah(3, 7)
print(akhir)


def titip_pesan(pesan):
    kalimat = f"ada pesan nihh: {pesan}"
    return kalimat


hasil = titip_pesan("Bangunn!")
print(hasil)


def operasi_matematika_lengkap(angka_pertama, angka_kedua):
    tambah = angka_pertama + angka_kedua
    kurang = angka_pertama - angka_kedua
    bagi = angka_pertama / angka_kedua
    kali = angka_pertama * angka_kedua
    return tambah, kurang, kali, bagi


# ==========================================
# 5. LATIHAN LUAS & VOLUME
# ==========================================
# a. Luas persegi panjang = panjang * lebar
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar



# b. Volume persegi panjang (balok) = panjang * lebar * tinggi
def volume_persegi_panjang(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


# c. Luas lingkaran = pi * r^2
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)


# d. Volume bola = (4/3) * pi * r^3
def volume_bola(jari_jari):
    return (4 / 3) * math.pi * (jari_jari ** 3)


def main():
    print("\n=== Program Hitung Luas & Volume ===")

    # a. Luas persegi panjang
    print("\n--- a. Luas Persegi Panjang ---")
    p_luas = float(input("Masukkan panjang: "))
    l_luas = float(input("Masukkan lebar: "))
    print(f"Luas persegi panjang = {luas_persegi_panjang(p_luas, l_luas):.2f}")

# b. Volume persegi panj
    print("\n--- b, Volume Persegi Panjang ---")
    p_vol = float(input("Masukkan panjang: "))
    l_vol = float(input("Masukkan lebar: "))
    t_vol = float(input("Masukkan tinggi: "))
    print(f"Volume persegi panjang = {volume_persegi_panjang(p_vol, l_vol, t_vol):.2f}")

    # c. Luas lingkaran
    print("\n--- c. Luas Lingkaran ---")
    r_luas = float(input("Masukkan jari-jari: "))
    print(f"Luas lingkaran = {luas_lingkaran(r_luas):.2f}")

    # d. Volume bola
    print("\n--- d. Volume Bola ---")
    r_vol = float(input("Masukkan jari-jari: "))
    print(f"Volume bola = {volume_bola(r_vol):.2f}")


if __name__ == "__main__":
    main()