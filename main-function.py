#poin2,3,4

on = True
while on: 
        pilihan = input("mau pesen kopi apa (kopi aren/americano/latte): ")
        if pilihan == "off" :
                on = False
        elif pilihan == "report":
                print(f"kopi\t\t: {resource['kopi']}")
                print(f"air\t\t: {resource['air']}")
                print(f"susu\t\t: {resource['susu']}")
                print(f"gula merah\t: {resource['gula_merah']}")
                print(f"uang\t\t:",uang)
        else:
                pilihan_kopi = isi[pilihan]
                if resource_full(pilihan_kopi["bahan"]):
                        bayar = input_uang()
                        if transaksi_berhasil(bayar,pilihan_kopi["harga"]):
                                print("ok")
                                