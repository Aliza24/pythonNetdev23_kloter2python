nilai_tugas = float(input("Masukan nilai tugas: "))
nilai_UTS = float(input("Masukan nilai UTS: "))
nilai_UAS = float(input("Masukan nilai UAS: "))

def itungan():
    hitung = nilai_tugas * (30/100)  + nilai_UAS *(35/100) + nilai_UTS * (35/100)
    print(f"Nilai anda adalah {hitung}")
    if hitung <= 60:
        print("anda tidak lulus")
    else:
        print("anda lulus")

itungan()