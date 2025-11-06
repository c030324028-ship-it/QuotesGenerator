import random
import os
from quotes_kelompok3 import quotesAgama, quotesPendidikan, quotesMotivasi, quotesPercintaan, quotesPolitik
"""
Disini data data yang berisikan quotes dari semua pilihan kami pisah di dalam file yang berbeda
oleh karena itu kita perlu memanggil file tersebut dan di import sesuai dengan variabel yang di
buat untuk masing masing opsi dan isi quotes nya
"""
aktif: bool = True

daftarOpsi = [
    "agama",
    "pendidikan",
    "motivasi",
    "percintaan",
    "politik",
    "random",
    "acak"
]

def QuotesGenerator():
    """
    Function: QuotesGenerator***
    Fungsi utama program yang menjalankan loop selama variabel 'aktif' bernilai True
    Setiap kali loop berjalan, fungsi ini akan memanggil Menu() untuk menampilkan pilihan jenis quotes
    """
    while (aktif):
        Menu()

def Menu():
    """
    Function: Menu
    Menampilkan menu utama kepada pengguna:
    Membersihkan layar dengan command (os.system('cls'))
    Menampilkan daftar jenis quotes yang tersedia
    Meminta input pengguna untuk memilih jenis quotes
    Mengirim input ke fungsi Opsi() untuk diproses lebih lanjut
    """
    os.system('cls')
    print("====== Quotes Generator =======")
    print("# Jenis quotes")
    print("-> Agama")
    print("-> Pendidikan")
    print("-> Motivasi")
    print("-> Percintaan")
    print("-> Politik")
    print("-> Random/Acak")
    print("")
    print("# Lainnya")
    print("-> Keluar")
    print("")

    jenis = str(input("Pilih salah opsi di atas (teks): ")).lower()

    Opsi(jenis)

def Opsi(jenis: str):
    """
    Function: Opsi
    Memeriksa apakah input 'jenis' termasuk dalam daftarOpsi
    Jika tidak valid, meminta pengguna menekan Enter untuk mengulang
    Jika valid, meminta jumlah quotes (1-5)
    Memastikan jumlah berada dalam batas yang benar
    Memanggil fungsi Quotes() untuk menampilkan hasil
    """
    if (jenis in daftarOpsi):
        jumlah = int(input("Berapa jumlah quotes yang anda inginkan hari ini [1-5]?: "))

        if (jumlah > 5 or jumlah < 1):
            input("Harap masukkan batas jumlah yang sesuai! Tekan enter untuk mengulang")
        else:
            Quotes(jenis, jumlah)
    else:
        if (jenis == "keluar"):
            Konfirmasi()
        else:
            input("Harap pilih salah satu opsi di atas! Tekan Enter untuk mengulang")

def Konfirmasi():
    """
    Function: Konfirmasi
    Menanyakan kepada pengguna apakah ingin melanjutkan program atau keluar
    Jika "tidak" atau "t", mengembalikan True agar loop tetap berjalan
    Jika "ya" atau "y", mengubah variabel global 'aktif' menjadi False untuk menghentikan program
    Jika input tidak sesuai, menampilkan pesan kesalahan dan mengulang
    """
    global aktif
    while (True):
        opsi = str(input("Apakah ingin keluar dari program? [ya/tidak]: "))

        if (opsi == "ya" or opsi == "y"):
            aktif = False
            return False
        elif (opsi == "tidak" or opsi == "t"):
            return True
        else:
            print("Harap masukkan opsi yang benar!")

def Quotes(opsi, jumlah):
    os.system("cls")
    """
    Function: Quotes
    Menentukan daftar quotes sesuai pilihan pengguna:
    Jika "random", menggabungkan semua kategori quotes
    Dan jika yang lain, program akan menampilkan sesuai dengan permintaan
    Mengambil sejumlah quotes secara acak menggunakan libray dan commandnya(random.sample)
    Menampilkan quotes beserta tokoh dan jenisnya (jika random)
    Setelah selesai, memanggil Konfirmasi() untuk menanyakan apakah ingin lanjut
    """
    match(opsi):
        case "agama":
            listQuotes = quotesAgama
        case "pendidikan":
            listQuotes = quotesPendidikan
        case "motivasi":
            listQuotes = quotesMotivasi
        case "percintaan":
            listQuotes = quotesPercintaan
        case "politik":
            listQuotes = quotesPolitik
        case "random" | "acak":
            listQuotes = [*quotesAgama, *quotesPendidikan, *quotesMotivasi, *quotesPercintaan, *quotesPolitik]

    quotes = random.sample(listQuotes, k=jumlah)

    for i in range(jumlah):
        quote = quotes[i]

        teksQuote = quote["teks"]
        tokohQuote = quote["tokoh"]
        jenisQuote = quote["jenis"]

        if (opsi == "random"):
            print(f"Quote ke-{i + 1} ({jenisQuote}):")
        else:
            print(f"Quote ke-{i + 1}:")

        print(f'"{teksQuote}"\n~ {tokohQuote}\n')

    Konfirmasi()

QuotesGenerator()
