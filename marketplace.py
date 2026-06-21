import csv
import os

FILE_PRODUK = 'produk.csv'

def baca_produk():
    produk = {}
    if not os.path.exists(FILE_PRODUK):
        return produk
    with open(FILE_PRODUK, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produk[row['id']] = row
    return produk

def simpan_produk(produk):
    with open(FILE_PRODUK, mode='w', encoding='utf-8', newline='') as file:
        fieldnames = ['id', 'nama', 'harga', 'stok', 'kategori']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for p in produk.values():
            writer.writerow(p)

def read():
    produk = baca_produk()
    if not produk:
        print("Belum ada produk")
        return
    print("\n=== DAFTAR PRODUK ===")
    for id, p in produk.items():
        print(f"ID:{id} | {p['nama']} | Rp{int(p['harga']):,} | Stok:{p['stok']} | {p['kategori']}")
    print("=====================")

def create():
    produk = baca_produk()
    id_baru = str(len(produk) + 1)
    nama = input("Nama produk: ")
    harga = input("Harga: ")
    stok = input("Stok: ")
    kategori = input("Kategori Buku/Penghapus/Pulpen/Alat: ")
    produk[id_baru] = {'id': id_baru, 'nama': nama, 'harga': harga, 'stok': stok, 'kategori': kategori}
    simpan_produk(produk)
    print("Produk berhasil ditambah!")

def update():
    read()
    produk = baca_produk()
    id_edit = input("ID yg mau diedit: ")
    if id_edit in produk:
        produk[id_edit]['harga'] = input("Harga baru: ")
        produk[id_edit]['stok'] = input("Stok baru: ")
        simpan_produk(produk)
        print("Produk berhasil diupdate!")
    else:
        print("ID tidak ditemukan")

def delete():
    read()
    produk = baca_produk()
    id_hapus = input("ID yg mau dihapus: ")
    if id_hapus in produk:
        del produk[id_hapus]
        simpan_produk(produk)
        print("Produk berhasil dihapus!")
    else:
        print("ID tidak ditemukan")

def cari():
    produk = baca_produk()
    keyword = input("Cari nama produk: ").lower()
    ketemu = False
    print("\n=== HASIL PENCARIAN ===")
    for id, p in produk.items():
        if keyword in p['nama'].lower():
            print(f"ID:{id} | {p['nama']} | Rp{int(p['harga']):,} | Stok:{p['stok']}")
            ketemu = True
    if not ketemu:
        print("Produk tidak ditemukan")
    print("=======================")

keranjang = []

def beli():
    read()
    produk = baca_produk()
    id_beli = input("Masukkan ID produk yg mau dibeli: ")
    if id_beli in produk:
        qty = int(input("Jumlah: "))
        if int(produk[id_beli]['stok']) >= qty:
            produk[id_beli]['stok'] = str(int(produk[id_beli]['stok']) - qty)
            keranjang.append({'nama': produk[id_beli]['nama'], 'qty': qty, 'harga': int(produk[id_beli]['harga'])})
            simpan_produk(produk)
            print(f"{produk[id_beli]['nama']} x{qty} masuk keranjang!")
        else:
            print("Stok tidak cukup")
    else:
        print("ID tidak ditemukan")

def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong")
        return
    total = 0
    print("\n=== KERANJANG BELANJA ===")
    for item in keranjang:
        subtotal = item['qty'] * item['harga']
        print(f"{item['nama']} x{item['qty']} = Rp{subtotal:,}")
        total += subtotal
    print(f"TOTAL: Rp{total:,}")
    print("=========================")

def urut_harga():
    produk = baca_produk()
    urut = sorted(produk.values(), key=lambda x: int(x['harga']))
    print("\n=== URUT HARGA TERMURAH ===")
    for p in urut:
        print(f"{p['nama']} | Rp{int(p['harga']):,}")
    print("===========================")

print("="*50)
print("    Selamat Datang Di Marketplace FarraasIF25A")
print("="*50)

while True:
    print("\n=== MARKETPLACE BUKU & ALAT TULIS ===")
    print("1.Lihat 2.Tambah 3.Edit 4.Hapus 5.Cari 6.UrutHarga 7.Beli 8.Keranjang 9.Keluar")
    pilih = input("Pilih menu: ")
    
    if pilih == '1': read()
    elif pilih == '2': create()
    elif pilih == '3': update()
    elif pilih == '4': delete()
    elif pilih == '5': cari()
    elif pilih == '6': urut_harga()
    elif pilih == '7': beli()
    elif pilih == '8': lihat_keranjang()
    elif pilih == '9': 
        print("Terima kasih sudah berkunjung!")
        break
    else: print("Menu tidak ada")