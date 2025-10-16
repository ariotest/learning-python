from produk import produk
from tampilkan import tampilkan_produk
from sorting import selection_sort_by_harga, selection_sort_by_nama
from filter import filter_produk_murah

def main():
    # skema app
    print("---Selamat Datang di Toko Online Mini----")
    # tampilkan menu
    while True:
        print("\n1. Urutkan Berdasarkan Harga")
        print("2. Urutkan Berdasarkan Nama")
        print("3. Tampilkan Data Produk")
        print("4. Tampilkan Produk Murah (<=Rp100.000)")
        print("5. Keluar/exit")
        
        pilihan = input("Pilih Menu (1/2/3/4/5): ")
        # break ->berhenti
        # kondisi 
        if pilihan == "1":
            # urutkan harga produk
            hasil = selection_sort_by_harga(produk)
            tampilkan_produk(hasil)
        elif pilihan == "2":
            #urukan nama produk
            hasil = selection_sort_by_nama(produk)
            tampilkan_produk(hasil)
        elif pilihan == "3":
            # tampilkan data produk
            tampilkan_produk(produk)
        elif pilihan == "4":
            hasil = filter_produk_murah(produk)
            tampilkan_produk(hasil)
        elif pilihan == "5":
            # tampilkan pesan sampai jumpa
            print("Terima Kasih 👋")
            break
        else:
            print("Pilihan tidak valid. Coba lagi!")

# panggil main function
if __name__ == "__main__":
    main()