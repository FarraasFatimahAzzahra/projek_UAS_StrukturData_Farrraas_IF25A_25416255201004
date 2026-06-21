Nama : Farraas Fatimah Azzahra
NIM : 25416255201004
Fakultas/Prodi : Ilmu Komputer/Teknik Informatika
Kelas : A
Mata Kuliah : Struktur Data
Dosen Pengampu :
1. Hilda Yulia Novita, S.Kom., M.Kom
2. Cici Emilia Sukmawati, S.Kom., M.Kom

Tugas : Final Project membuat Aplikasi Manajemen dengan Database Flat File (.CSV)

# Deskripsi
Program ini dibuat untuk memenuhi tugas UAS Struktur Data.  
Program berupa aplikasi marketplace sederhana berbasis console/terminal yang bisa melakukan operasi CRUD pada data produk.

# Struktur File
- `marketplace.py` = Kode program utama Python.
- `produk.csv` = Database penyimpanan data produk.
- `Flowchart UAS STRUKDAT MARKETPLACE SED.png` = Flowchart alur program global.
  ![alt text](?raw=true)

# Fitur Program
Program memiliki 9 menu utama:
1. **Tampilkan Data** - Menampilkan seluruh data produk dari file `produk.csv` ke layar.
2. **Tambah Data Baru** - Input data produk baru berupa ID, nama, harga, stok, kategori. Data otomatis disimpan ke CSV.
3. **Edit Data** - Mengubah data produk berdasarkan ID yang dipilih. Perubahan disimpan ke CSV.
4. **Hapus Data** - Menghapus produk berdasarkan ID. Data terhapus disimpan ke CSV.
5. **Cari Produk** - Mencari produk berdasarkan kata kunci nama/kode produk.
6. **Urutkan Harga** - Mengurutkan data produk berdasarkan harga Ascending atau Descending.
7. **Beli Produk** - User memilih produk dan jumlah yang dibeli untuk dimasukkan ke keranjang.
8. **Keranjang** - Menampilkan isi keranjang belanja + total harga keseluruhan.
9. **Keluar** - Keluar dari program dan menampilkan pesan "Terima Kasih! Selamat Berbelanja Kembali".

# Cara Menjalankan Program
1. Pastikan Python 3 sudah terinstall.
2. Pastikan file `marketplace.py`, `produk.csv` dan gambar flowchart ada di folder yang sama
3. Buka terminal/CMD di folder tersebut.
4. Jalankan perintah: `python marketplace.py`.
  
