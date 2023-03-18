import os

isi = {
    "Kopi Gula Aren": { 
        "bahan": {
            "kopi": 30,
            "gula_merah": 20,
            "air": 80,
        },
        "harga": 20000.0,
    },      
    
    "Americano": {
        "bahan": {
            "kopi": 30,
            "air": 80,
        },
        "harga": 10000.0,
    },
    
    "Latte": { 
        "bahan": {
            "kopi": 150,
            "susu": 20,
            "air": 80,
        },
        "harga": 15000.0,
    }
}

uang = 0

resource = {
    "kopi": 180,
    "air": 300,
    "susu": 150,
    "gula_merah": 100
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def resource_full(masukan):
    for item in masukan:
        if masukan[item] >= resource[item]:
            print(f"\nMaaf, bahan tidak cukup untuk membuat pesanan {item} Anda ")
            return True
    return False


def input_uang():
    total_uang = int(input("Masukan uang: Rp."))
    return total_uang


def transaksi_berhasil(masukan_uang, harga_minuman):
    if masukan_uang >= harga_minuman:
        kembalian = masukan_uang - harga_minuman
        print(f"Transaksi berhasil, kembalian Anda {kembalian}")
        return True
    else:
        print("Maaf uang Anda tidak cukup")
        input("Tekan enter untuk melanjutkan...")
        return False


def kurangin_resource(nama_kopi, bahan):
    for item in bahan:
        resource[item] -= bahan[item]
    print(f"Silakan nikmati {nama_kopi}")


def home_screen():
    clear_screen()
    print("Selamat datang di Coffee Shop PythonKloter2")
    print("\nMenu kopi:")
    print("1. Kopi Aren")
    print("2. Americano")
    print("3. Latte")
    print("\nUntuk keluar, ketik 'off'")
    print("Untuk melihat laporan bahan dan uang, ketik 'report'")
    print("============================================")
    input("\nTekan enter untuk melanjutkan...")
  

on = True
while on: 
    home_screen()
    clear_screen
    print("\nMau pesan kopi apa?")
    print("\nPilih:")
    print("1. Kopi Gula Aren")
    print("2. Americano")
    print("3. Latte")
    pilihan = input("(Kopi Gula Aren / Americano / Latte): ")
    if pilihan == "off":
        on = False
    elif pilihan == "report":
        print(f"Kopi\t\t: {resource['kopi']}ml")
        print(f"Air\t\t: {resource['air']}ml")
        print(f"Susu\t\t: {resource['susu']}ml")
        print(f"Gula Merah\t: {resource['gula_merah']}ml")
        print(f"Uang\t\t: {uang}")
        input("\nTekan enter untuk melanjutkan...")
    else:
        pilihan_kopi = isi[pilihan]
        if resource_full(pilihan_kopi["bahan"]):
            input("\nTekan enter untuk melanjutkan...")
            continue
        bayar = input_uang()
        if transaksi_berhasil(bayar, pilihan_kopi["harga"]):
            kurangin_resource(pilihan, pilihan_kopi["bahan"])
            uang += pilihan_kopi["harga"]
            input("\nTekan enter untuk melanjutkan...")

            