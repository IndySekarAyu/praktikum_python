x1 = int(input("masukkan harga:"))
x2 = int(input("masukkan pembayaran:"))
x3 = x2 - x1
x4 = [100000,50000,20000,10000,5000,2000,1000]
for x in x4:
    jumlah = x3 // x
    x3 = x3 % x
    
    print(f"{jumlah} uang sejumlah Rp{x}")