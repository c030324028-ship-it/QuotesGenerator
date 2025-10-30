import random
import os
from quotes_kelompok3 import quotesAgama, quotesPendidikan, quotesMotivasi, quotesPercintaan, quotesPolitik

aktif : bool = True

daftarOpsi = [
    "agama",
    "pendidikan",
    "motivasi",
    "percintaan",
    "politik",
    "random"
]

def QuotesGenerator():
    while (aktif):
        Menu()

def Menu():
    os.system('cls')
    print("====== Quotes Generator =======")
    print("Jenis quotes")
    print("1. Agama")
    print("2. Pendidikan")
    print("3. Motivasi")
    print("4. Percintaan")
    print("5. Politik")
    print("6. Random")

    jenis = str(input("Pilih jenis Quotes yang anda inginkan (nama): ")).lower()

    Opsi(jenis)

def Opsi(jenis : str):
    if (jenis not in daftarOpsi):
        input("Harap pilih salah satu opsi di atas! Tekan Enter untuk mengulang")
    else:
        jumlah = int(input("Berapa jumlah quotes yang anda inginkan hari ini [1-5]?: "))

        if (jumlah > 5 or jumlah < 1):
            input("Harap masukkan batas jumlah yang sesuai! Tekan enter untuk mengulang")
        else:
            Quotes(jenis, jumlah)

def Konfirmasi():
    global aktif
    while (True):
        opsi = str(input("Apakah ingin melanjutkan program? [ya/tidak]: "))

        if (opsi == "ya" or opsi == "y"):
            return True
        elif (opsi == "tidak" or opsi == "t"):
            aktif = False
            return False
        else:
            print("Harap masukkan opsi yang benar!")

def Quotes(opsi, jumlah):
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
        case "random":
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