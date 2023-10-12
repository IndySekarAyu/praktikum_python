def permutasi(kata):
    try:
        permutasi = []
        for i in range(len(kata)):
            permutasi.append(kata)
            kata = kata [1:] + kata [0]

        permutasi.reverse() 
        return permutasi
    except:
        print("error")
          
#Test Case 1
kata_input  = "Mobil" 
hasil_permutasi = permutasi(kata_input) 
for hasil in hasil_permutasi:
    print(hasil, end = " | ")  


kata = "mobil"
kata1 = kata [1:] + kata [0]
print(kata1)