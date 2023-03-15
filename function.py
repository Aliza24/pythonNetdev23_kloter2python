def resource_full(masukan) :
        for item in masukan :
                if masukan[item] >= resource[item]:
                        print(f"maaf bahan tidak cukup untuk membuat pesanan anda {item}")
        return True


def input_uang():
        total_uang = int(input("masukan uang: Rp."))
        return total_uang


def transaksi_berhasil(masukan_uang,harga_minuman):
        if masukan_uang >= harga_minuman:
                kembalian = masukan_uang-harga_minuman
                print(f"transaksi berhasil, kembalian anda {kembalian}")
