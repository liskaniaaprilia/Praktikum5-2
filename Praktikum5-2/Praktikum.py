print("Liskania Aprilia (312210383)")
print("===================================")

data = {}
while True :
    print()
    lanjut = str(input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: "))
    print()
    if lanjut.lower() == "t":
        print("Tambah Data")
        nama = str(input("Nama\t\t: "))
        nim = str(input("NIM\t\t\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        akhir = round(float((tugas*0.3) + (uts*0.35) + (uas*0.35)),2)
        data[nama]=nim, uts, uas, tugas, akhir

    elif lanjut.lower() == "l":
        if data.items():
            print("Daftar Nilai")
            print("="*84)
            print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
            print("="*84)
            n=0
            for a in data.items():
                n += 1
                print("|{no:^4}|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"
                      .format(a[0][:13], a[1][0], a[1][1], a[1][2], a[1][3], a[1][4], no=n))
                print('=' * 84)
        else:
            print('Daftar Nilai')
            print('=' * 84)
            print(f"|{'NO':^4}|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
            print('=' * 84)
            print(f"|{'TIDAK ADA DATA':^82}|")
            print('=' * 84)

    elif lanjut.lower() == 'u':
        print("Ubah Data")
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            nim = str(input('NIM\t\t: '))
            uts = int(input('Nilai UTS\t: '))
            uas = int(input("Nilai UAS\t: "))
            tugas = int(input('Nilai Tugas\t: '))
            akhir = round(float((tugas * 0.3) + (uts * 0.35) + (uas * 0.35)), 2)
            data[nama] = nim, uts, uas, tugas, akhir
        else:
            print(f"Nama {nama} Tidak Tersedia")

    elif lanjut.lower() == 'h':
        print('Hapus Data')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            del data[nama]
        else:
            print(f"Nama {nama} Tidak Tersedia")

    elif lanjut.lower() == 'c':
        print('Data Cari')
        nama = str(input('Nama\t\t: '))
        if nama in data.keys():
            print('=' * 79)
            print(f"|{'NAMA':^20}|{'NIM':^20}|{'TUGAS':^10}|{'UTS':^6}|{'UAS':^6}|{'AKHIR':^10}|")
            print('=' * 79)
            print("|{0:^20}|{1:^20}|{2:^10}|{3:^6}|{4:^6}|{5:^10}|"
                    .format(nama, nim, tugas, uts, uas, akhir))
            print('=' * 79)
        else:
            print(f"Nama {nama} Tidak Tersedia")
    elif lanjut.lower() == 'k':
        print('Selesai')
        break

    else:
        print('Pilih tindakan yang tersedia')























