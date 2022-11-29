# Input data nilai Mahasiswa ( Rhendy Diki Nugraha )
print("====================\nProgram Input Nilai\n====================")
data = {}


while True:
    pilih = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    if pilih.lower() == 't':
        print("\nTambahkan Data Mahasiswa\n========================")
        nim = str(input("NIM            : "))
        nama = input("Nama           : ")
        uts = int(input("Nilai UTS      : "))
        uas = int(input("Nilai UAS      : "))
        tugas = int(input("Nilai Tugas    : "))
        akhir = tugas*30/100 + uts*35/100 + uas*35/100
        data[nim] = [nama, uts, uas, tugas, akhir]

    elif pilih.lower() == 'u':
        print("\nMengubah Data Mahasiswa\n========================")
        nim = str(input("NIM            : "))
        if nim in data.keys():
            nama = input("Nama           : ")
            uts = int(input("Nilai UTS      : "))
            uas = int(input("Nilai UAS      : "))
            tugas = int(input("Nilai Tugas    : "))
            akhir = tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100
            data[nim] = nama, uts, uas, tugas, akhir
        else:
            print("NIM {0} tidak ditemukan".format(nim))

    elif pilih.lower() == 'h':
        print("\nMenghapus Data Mahasiswa\n========================")
        nim = str(input("Masukkan NIM   : "))
        if nim in data.keys():
            del data[nim]
            print("Data berhasil dihapus")
        else:
            print("NIM {0} Tidak Ditemukan".format(nim))

    elif pilih.lower() == 'c':
        print("\nMencari Data Mahasiswa\n========================")
        nim = input("Masukkan NIM  : ")
        if nim in data.keys():
            print("="*77)
            print("|                                Daftar Mahasiswa                           |")
            print("="*77)
            print("| NO |    NIM    |         Nama         |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*77)
            i = 0
            for j in data.items():
                i += 1
            print("| {no:2d} | {0:9s} | {1:20s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(nim, nama, uts, uas, tugas, akhir, no=i ))
            print("="*77)
        else:
            print("NIM  {0} Tidak Ditemukan".format(nim))

    elif pilih.lower() == 'l':
        if data.items():
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("| NO |    NIM    |         Nama         |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            i = 0
            for z in data.items():
                i += 1
                print("| {no:2d} | {0:9s} | {1:20s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
            print("=" * 78)
        else:
            print("="*78)
            print("|                               Daftar Mahasiswa                             |")
            print("="*78)
            print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*78)
            print("|                                TIDAK ADA DATA                              |")
            print("="*78)

    elif pilih. lower() == 'k':
        break

    else:
        print("Pilihan tidak ada! Pilih menu yang tersedia.")