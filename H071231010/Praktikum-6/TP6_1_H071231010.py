dicti= {
'nama' : input('Masukkan nama : '),
'umur' : input('Masukkan umur : '),
'alamat' : input('Masukkan alamat : ')
}

def tampilkan_opsi():
    print("=" * 50)
    print(f"Selmat datang {dicti['nama']} silahkan pilih opsi anda")
    print("=" * 50)
    print("Menu")
    print("1. Tampilkan detail data")
    print("2. Ubah Nama")
    print("3. Ubah umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    pilihan = input("pilih opsi : ")
    return pilihan


def tampilkan_detail():
    print(f"nama anda adalah : {dicti['nama']}")
    print(f"umur anda adalah : {dicti['umur']}")
    print(f"alamat anda adalah : {dicti['alamat']}")
    
def ubah_nama():
    dicti['nama'] = input("Silahkan Input nama baru: ")
    print("Data anda sukses di diperbarui")

def ubah_umur():
    dicti["umur"] = input("Silahkan Input umur baru: ")
    print("Data anda sukses di diperbarui")

def ubah_alamat():
    dicti['alamat']= input("Silahkan Input alamat baru: ")
    print("Data anda sukses di diperbarui")


while True:
    opsi = tampilkan_opsi()
    if opsi == "1":
        tampilkan_detail()
    elif opsi == "2":
        ubah_nama()
    elif opsi == "3":
        ubah_umur()
    elif opsi == "4":
        ubah_alamat()
    elif opsi == "5":
        print("Selamat Tinggal", nama)
        break
    else:
        print("Opsi tidak valid. Silahkan coba lagi.")
