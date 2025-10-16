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