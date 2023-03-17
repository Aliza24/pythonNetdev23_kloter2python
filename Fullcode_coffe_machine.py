isi = {
    "Kopi_aren": { 
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
    
    "latte": { 
        "bahan": {
            "kopi": 30,
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

def resource_full(masukan):
    for item in masukan:
        if masukan[item] >= resource[item]:
            print(f"Maaf bahan tidak cukup untuk membuat pesanan Anda {item}")
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
        return False


def kurangin_resource(nama_kopi, bahan):
    for item in bahan:
        resource[item] -= bahan[item]
    print(f"Silakan nikmati {nama_kopi}")


on = True
while on: 
    pilihan = input("Mau pesan kopi apa (Kopi Aren/Americano/Latte): ")
    if pilihan == "off":
        on = False
    elif pilihan == "report":
        print(f"Kopi\t\t: {resource['kopi']}ml")
        print(f"Air\t\t: {resource['air']}ml")
        print(f"Susu\t\t: {resource['susu']}ml")
        print(f"Gula Merah\t: {resource['gula_merah']}ml")
        print(f"Uang\t\t: {uang}")
    else:
        pilihan_kopi = isi[pilihan]
        if resource_full(pilihan_kopi["bahan"]):
            continue
        bayar = input_uang()
        if transaksi_berhasil(bayar, pilihan_kopi["harga"]):
            kurangin_resource(pilihan, pilihan_kopi["bahan"])
            uang += pilihan_kopi["harga"]
