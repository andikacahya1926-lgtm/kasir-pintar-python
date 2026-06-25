# status awal untuk menjalankan perulangan
melayani_pembeli = True

print("===PROGRAM KASIR PINTAR===")

while melayani_pembeli:
    # 1. input total belanja
    total_belanja = int(input("\nMasukkan total belanjaan pembeli (Rp): "))
    
    # 2. logika diskon bertingkat
    if total_belanja >= 500000:
        print("mantap kamu dapat diskon 20%")
        bayar = total_belanja - (total_belanja * 0.20)
        print(f"total yang harus dibayar = Rp {bayar}")
        
    elif total_belanja >= 100000:
        print("selamat anda dapat diskon 10%.")
        bayar = total_belanja - (total_belanja * 0.10)
        print(f"total yang harus anda bayar = Rp {bayar}")
        
    else:
        print("Maaf belum dapat diskon ya.")
        print(f"Total yang harus dibayar: Rp {total_belanja}")
        
    # 3. Tanya apakah mau lanjut melayani pembeli berikutnya
    lagi = input("Ada pembeli lagi? (ketik 'ya' untuk lanjut, atau ketik 'tidak' untuk selesai): ")
    
    if lagi.lower() == 'tidak':
        melayani_pembeli = False
        print("\nTransaksi selesai. Toko tutup!")
