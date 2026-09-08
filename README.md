# Studi_Kasus_3_Muhammad_Favian_Daffa

Nama: Muhammad Favian Daffa<br>
Kelas: 26A<br>
NIM: 2609116021<br>
<br>
Penjelasan kode :<br>

1. Menyimpan dan Menampilkan Daftar Buku<br>
<img width="256" height="171" alt="image" src="https://github.com/user-attachments/assets/6724cb86-5838-4179-a386-4e043f31d9a1" />

Bagian ini berfungsi untuk menyimpan daftar buku yang tersedia dan membuat list pinjam sebagai tempat menyimpan buku yang dipilih. Setelah itu, perulangan for digunakan untuk menampilkan semua buku yang tersedia<br>

2. Menu dan Proses Peminjaman<br>
<img width="419" height="218" alt="image" src="https://github.com/user-attachments/assets/1ac67846-68c4-4935-8341-4e06d68823b7" />

Bagian ini menggunakan while True agar menu terus ditampilkan sampai pengguna memilih menu 3. Jika memilih menu 1, program meminta judul buku kemudian mengecek ketersediaannya. Jika tersedia, buku dimasukkan ke dalam list pinjam menggunakan append()<br>

3. Proses Menghapus Buku dari Pinjaman<br>
<img width="455" height="231" alt="image" src="https://github.com/user-attachments/assets/f160a2df-c4d0-4f57-aa21-eefa73ead7ce" />

Bagian ini berfungsi untuk menghapus buku yang sudah dipinjam. enumerate() digunakan untuk memberikan nomor pada setiap buku. Setelah pengguna memilih nomor buku, pop() digunakan untuk menghapus buku tersebut dari list pinjam<br>

4. Mengakhiri Program dan Menampilkan Hasil<br>
<img width="282" height="163" alt="image" src="https://github.com/user-attachments/assets/55408136-68fa-427a-9330-fe8b586626f0" />


Bagian terakhir digunakan untuk mengakhiri program dan menampilkan hasil peminjaman. Perintah break menghentikan perulangan ketika pengguna memilih menu 3. Setelah itu, program menampilkan semua buku yang masih berada di dalam list pinjam<br>

OUTPUT :<br>

<img width="341" height="626" alt="Screenshot 2026-09-08 231231" src="https://github.com/user-attachments/assets/7f9ef6f0-7e3d-43a7-8972-cb8f333106fa" />

