stok_barang = {}

# tambah barang
def tambah_barang():
    kode_barang = input("Masukkan kode barang (atau ketik 'auto' untuk kode otomatis): ")
    nama_barang = input("Masukkan nama barang: ")

    if kode_barang.lower() == 'auto':
        kode_barang = str(len(stok_barang) + 1)
        jumlah = input("Masukkan jumlah stok barang: ")
        harga = input("Masukkan harga barang: ")

    jumlah = int(jumlah)
    harga = int(harga)

    if kode_barang in stok_barang:
        print(f"Barang dengan kode {kode_barang} sudah ada.")
        stok_barang[kode_barang]['jumlah'] += jumlah
        print(f"Stok barang {nama_barang} bertambah menjadi {stok_barang[kode_barang]['jumlah']}.")
    else:
        stok_barang[kode_barang] = {'nama': nama_barang, 'jumlah': jumlah, 'harga': harga}
        print(f"Barang {nama_barang} berhasil ditambahkan.")

# kurangi barang
def kurangi_barang():
    kode_barang = input("Masukkan kode barang yang ingin dikurangi: ")

    if kode_barang in stok_barang:
        jumlah_pengurangan = input("Masukkan jumlah barang yang ingin dikurangi: ")

        jumlah_pengurangan = int(jumlah_pengurangan)

        if jumlah_pengurangan > stok_barang[kode_barang]['jumlah']:
            print("Jumlah pengurangan melebihi stok yang tersedia.")
        else:
            stok_barang[kode_barang]['jumlah'] -= jumlah_pengurangan
            print(f"Stok barang {stok_barang[kode_barang]['nama']} berhasil dikurangi.")
    else:
        print("Barang tidak ditemukan.")

# lihat daftar barang
def lihat_barang():
    if not stok_barang:
        print("Tidak ada barang di dalam stok.")
    else:
        # Menambahkan pembatas '|' antara header kolom
        print(f"{'Kode Barang':<15} | {'Nama Barang':<20} | {'Jumlah':<10} | {'Harga':<10}")
        print('-' * 70)  # Menambahkan garis pembatas setelah header
        for kode, info in stok_barang.items():
            # Menambahkan pembatas '|' antara setiap kolom di baris data
            print(f"{kode:<15} | {info['nama']:<20} | {info['jumlah']:<10} | {info['harga']:<10}")

# cari barang dengan kode
def cari_barang():
    kode_barang = input("Masukkan kode barang yang ingin dicari: ")
    if kode_barang in stok_barang:
        info = stok_barang[kode_barang]
        print(f"Kode Barang: {kode_barang}")
        print(f"Nama Barang: {info['nama']}")
        print(f"Jumlah Stok: {info['jumlah']}")
        print(f"Harga: {info['harga']:}")
    else:
        print("Barang tidak ditemukan.")

# hapus barang
def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    if kode_barang in stok_barang:
        del stok_barang[kode_barang]
        print(f"Barang dengan kode {kode_barang} berhasil dihapus.")
    else:
        print("Barang tidak ditemukan.")

# hitung total stok
def hitung_total_stok():
    total = 0
    for info in stok_barang.values():
        total += info['jumlah'] * info['harga']
    print(f"Total nilai stok barang: {total:}")

# edit stok barang
def edit_stok_barang():
    kode_barang = input("Masukkan kode barang yang ingin diedit: ")
    
    if kode_barang in stok_barang:
        jumlah_baru = input(f"Masukkan jumlah stok baru untuk barang {stok_barang[kode_barang]['nama']}: ")
    
        stok_barang[kode_barang]['jumlah'] = int(jumlah_baru)
        print(f"Stok barang {stok_barang[kode_barang]['nama']} berhasil diperbarui menjadi {stok_barang[kode_barang]['jumlah']}.")
    else:
        print("Barang tidak ditemukan.")

# cari stok terbanyak
def barang_terbanyak():
    if not stok_barang:
        print("Tidak ada barang di dalam stok.")
    else:
        barang_terbanyak = max(stok_barang.items(), key=lambda item: item[1]['jumlah'])
        print(f"Barang dengan stok terbanyak: {barang_terbanyak[1]['nama']} ({barang_terbanyak[1]['jumlah']} unit)")

# cari harga tertinggi
def barang_harga_tertinggi():
    if not stok_barang:
        print("Tidak ada barang di dalam stok.")
    else:
        barang_tertinggi = max(stok_barang.items(), key=lambda item: item[1]['harga'])
        print(f"Barang dengan harga tertinggi: {barang_tertinggi[1]['nama']} ({barang_tertinggi[1]['harga']} )")

def menu():
    while True:
        print("\n===SISTEM MANAJEMEN STOK BARANG TOKO LELE BERGOYANG===")
        print("1. Tambah barang")
        print("2. Kurangi barang")
        print("3. Lihat daftar barang")
        print("4. Cari barang")
        print("5. Hapus barang")
        print("6. Hitung total stok")
        print("7. Edit stok barang")
        print("8. Cari stok terbanyak")
        print("9. Cari harga tertinggi")
        print("10. Keluar")
    
        pilihan = input("Pilih menu (1-10): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            kurangi_barang()
        elif pilihan == '3':
            lihat_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            hapus_barang()
        elif pilihan == '6':
            hitung_total_stok()
        elif pilihan == '7':
            edit_stok_barang()
        elif pilihan == '8':
           barang_terbanyak()
        elif pilihan == '9':
           barang_harga_tertinggi()
        elif pilihan == '10':
            print("Terima kasih! Program telah selesai ^_^ ")
            break
        else:
            print("Pilih 1 sampai 10, Ayo coba lagi!!")

menu()