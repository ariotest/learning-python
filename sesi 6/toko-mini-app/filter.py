def filter_produk_murah(produk, batas=100000):
    hasil = [] # list kosong untuk nampung produk
    for p in produk: # loop tiap produk
        if p['harga'] <= batas: # cek harga
            hasil.append(p) # masukkan produk ke ahsil
    return hasil