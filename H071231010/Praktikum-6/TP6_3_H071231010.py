angka_input = input("Masukkan angka-angka : ")
angka_list = angka_input.split()

angka_ganjil = []
angka_genap = []
angka_habis_dibagi_5 = []

for angka in angka_list:
    angka = int(angka)
    if angka % 2 == 1:  
        angka_ganjil.append(angka)
    elif angka % 2 == 0:  
        angka_genap.append(angka)
    if angka % 5 == 0:  
        angka_habis_dibagi_5.append(angka)

print("Angka Ganjil:", angka_ganjil)
print("Angka Genap:", angka_genap)
print("Angka yang Habis Dibagi 5:", angka_habis_dibagi_5)
