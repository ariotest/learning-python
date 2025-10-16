'''
Tokok Online Mini
- produk (harga, nama)
- untuk urutkan harga termurah - termahal
- untuk urutkan nama produk kita (A - Z)

=> fitur app
- menampilkan menu
- memilih menu

'''

# data produk -> list -> int, string, dictionary, boolean
produk = [
    {"nama": "mouse", "harga": 75000},
    {"nama": "keyboard", "harga": 150000},
    {"nama": "flasdisk", "harga": 50000},
    {"nama": "monitor", "harga": 975000},
    {"nama": "Charger", "harga": 125000},
    {"nama": "cable usb", "harga": 25000},
]

# function tampilkan data produk
def tampilkan_produk(produk):
    print("\nDaftar Produk: ")
    for p in produk:
        print(f"- {p['nama']}: Rp{p['harga']}") #->untuk cetak nama dan harga

# function sort harga
def selection_sort_by_harga(produk):
    n = len(produk) #ambil pjg arr/list
    for i in range(0, n - 1):
        min_idx = i      
        for j in range(i + 1, n):
            if produk[j]['harga'] < produk[min_idx]['harga']:
                min_idx = j
        produk[i], produk[min_idx] = produk[min_idx], produk[i]
    return produk

# function sort harga
def selection_sort_by_nama(produk):
    n = len(produk) #ambil pjg arr/list
    for i in range(0, n - 1):
        min_idx = i      
        for j in range(i + 1, n):
            if produk[j]['nama'].lower() < produk[min_idx]['nama'].lower():
                min_idx = j
        produk[i], produk[min_idx] = produk[min_idx], produk[i]
    return produk

def main():
    # skema app
    print("---Selamat Datang di Toko Online Mini----")
    # tampilkan menu
    while True:
        print("\n1. Urutkan Berdasarkan Harga")
        print("2. Urutkan Berdasarkan Nama")
        print("3. Tampilkan Data Produk")
        print("4. Keluar/exit")
        
        pilihan = input("Pilih Menu (1/2/3/4): ")
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
            # tampilkan pesan sampai jumpa
            print("Terima Kasih 👋")
            break
        else:
            print("Pilihan tidak valid. Coba lagi!")

# panggil main function
main()