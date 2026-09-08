daftar_buku = (
    "Jaringan Komputer",
    "Basis Data",
    "Dasar Pemrograman",
    "Dasar Sistem Informasi",
    "Pemrograman Python",
    "Algoritma dan Pemrograman")
pinjam = []

print ("DAFTAR BUKU PERPUSTAKAAN FT")
for buku in daftar_buku:
    print ("-", buku)

while True:
    print ("--- MENU ---")
    print ("1. Pinjam Buku"
           "\n2. Hapus Buku dari Pinjaman"
           "\n3. Selesai")
    pilih = input("Pilih menu (1/2/3): ")

    if pilih == "1":
        buku = input("Masukkan Judul Buku Yang Ingin Dipinjam: ")

        if buku in daftar_buku:
            pinjam.append(buku)
            print("Buku Berhasil Dipinjam")
        else :
            print ("Buku Tidak Tersedia")

    elif pilih == "2":
    
        if len(pinjam) == 0:
            print ("Belum Ada Buku Yang Dipinjam")
        else:
            print("Buku Yang Sedang Dipinjam : ")
            for i,buku in enumerate(pinjam, start=1):
                print (i,".", buku)

        nomor = int(input("Masukkan Nomor Buku Yang Ingin Dihapus : "))

        if nomor >= 1 and nomor <= len(pinjam):
            buku_dihapus = pinjam.pop(nomor - 1)
            print ("Buku",buku_dihapus, "Berhasil Dihapus")
        else :
            print("Nomor Buku Tidak Ditemukan")

    elif pilih == "3":
        break
    else : 
        print("Pilihan Tidak Valid")

print("DAFTAR BUKU YANG DIPINJAM")
if len(pinjam) == 0:
    print("Tidak Ada Buku Yang Dipinjam")
else :
    for buku in pinjam:
        print ("-", buku)