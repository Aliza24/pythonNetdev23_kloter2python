
#function
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


