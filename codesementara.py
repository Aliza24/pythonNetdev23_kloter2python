# isi =
#   {"Kopi Gula Aren":
#       {"bahan":
#           {"kopi": 30,
#             "gula_merah": 20,
#             "air": 80,
#           },
#        {"harga": 20000.0,}
#       },
#
#     "Americano": {
#         "bahan": {
#             "kopi": 30,
#             "air": 80,
#         },
#         "harga": 10000.0,
#     },
#
#     "Latte": {
#         "bahan": {
#             "kopi": 150,
#             "susu": 20,
#             "air": 80,
#         },
#         "harga": 15000.0,
#     }
# }



#Resource
kopi = 180
air = 300
susu = 150
gula_merah = 100
uang = 0


def home_screen():
    print("============== MESIN KOPI NETDEV2 ==============")
    print("-- Selamat datang di Coffee Shop PythonKloter2 --")
    print("---------- Tolong Input Pesanan Anda ----------")
    print("               Welcome & Enjoy                 ")
    print("\nMenu kopi:")
    print("1. Kopi Gula Aren\t:Rp 20000")
    print("2. Americano\t\t:Rp 10000")
    print("3. Latte\t\t\t:Rp 15000")
    print("\nUntuk keluar, ketik 'off'")
    print("Untuk melihat laporan bahan dan uang, ketik 'report'")
    print("============================================")
home_screen()
pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")



while pilihan != "off":
    if pilihan == "1":
        if kopi >= 30 and gula_merah >= 20 and air >= 80:
            pembayaran = int(input("Silahkan masukkan uang (Rp 20.000): \nRp "))
            while pembayaran < 20000:
                print("Maaf uang yang anda masukkan tidak cukup")
                pembayaran = int(input("Silahkan masukkan uang (Rp 20.000): \nRp "))
            else:
                kembalian = pembayaran - 20000
                print(f"Transaksi berhasil, kembalian anda adalah Rp {kembalian}")
                kopi -= 30
                gula_merah -= 20
                air -= 80
                uang += 20000
            tambahan_pesanan = input("Apakah anda ingin menambah pesanan anda? (Y/N)")
            if tambahan_pesanan == "Y":
                home_screen()
                pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")
            else:
                print("===========Terima Kasih===========")
                break
        else:
            print("Maaf, bahan untuk membuat Kopi Gula Aren tidak cukup\n")
            home_screen()
            pilihan = input("Masukkan pilihan anda (1/2/3/off/report): \n")

    elif pilihan == "2":
        if kopi >= 30 and air >= 80:
            pembayaran = int(input("Silahkan masukkan uang (Rp 10.000): \nRp "))
            while pembayaran < 10000:
                print("Maaf uang yang anda masukkan tidak cukup")
                pembayaran = int(input("Silahkan masukkan uang (Rp 10.000): \nRp "))
            else:
                kembalian = pembayaran - 10000
                print(f"Transaksi berhasil, kembalian anda adalah Rp {kembalian}")
                kopi -= 30
                air -= 80
                uang += 10000
            tambahan_pesanan = input("Apakah anda ingin menambah pesanan anda? (Y/N)")
            if tambahan_pesanan == "Y":
                home_screen()
                pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")
            else:
                print("===========Terima Kasih===========")
                break
        else:
            print("Maaf, bahan untuk membuat Kopi Gula Aren tidak cukup\n")
            home_screen()
            pilihan = input("Masukkan pilihan anda (1/2/3/off/report): \n")

    elif pilihan == "3":
        if kopi >= 150 and susu>= 20 and air >= 80:
            pembayaran = int(input("Silahkan masukkan uang (Rp 15.000): \nRp "))
            while pembayaran < 15000:
                print("Maaf uang yang anda masukkan tidak cukup")
                pembayaran = int(input("Silahkan masukkan uang (Rp 15.000): \nRp "))
            else:
                kembalian = pembayaran - 15000
                print(f"Transaksi berhasil, kembalian anda adalah Rp {kembalian}")
                kopi -= 30
                air -= 80
                uang += 15000
            tambahan_pesanan = input("Apakah anda ingin menambah pesanan anda? (Y/N)")
            if tambahan_pesanan == "Y":
                home_screen()
                pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")
            else:
                print("===========Terima Kasih===========")
                break
        else:
            print("Maaf, bahan untuk membuat Kopi Gula Aren tidak cukup\n")
            home_screen()
            pilihan = input("Masukkan pilihan anda (1/2/3/off/report): \n")

    elif pilihan == "report":
        print(f"Kopi\t\t: {kopi}gr")
        print(f"Air\t\t\t: {air}ml")
        print(f"Susu\t\t: {susu}ml")
        print(f"Gula Merah\t: {gula_merah}gr")
        print(f"Uang\t\t: Rp {uang}\n")
        enter = input("Tekan enter untuk lanjut >")
        home_screen()
        pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")

    elif pilihan == "off":
        break

    else:
        print("Maaf, kami tidak bisa mendeteksi pilihan anda")
        enter = input("Tekan enter untuk lanjut >")
        home_screen()
        pilihan = input("Masukkan pilihan anda (1/2/3/off/report): ")

