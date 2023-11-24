import re

class DataManagement:
    def __init__(self):
        self.data = {"Nama"    : "", 
                     "Email"   : "", 
                     "Password": ""}
        self.data_tersimpan_added = False
        
    def menu_detail_anda(self):
        if not any(self.data.values()):
            print("Data saat ini kosong.")
        else:
            print("Detail Anda:")
            for key, value in self.data.items():
                print(f"{key}: {value}")

    def menu_ubah_nama(self):
        if not any(self.data.values()):
            print("Data saat ini kosong.")
        else:
            new_name = input("Masukkan Nama Baru: ")
            self.data["Nama"] = new_name
            print("Nama berhasil diubah!")

    def menu_jumlah_data_pada_file(self):
        file_name = input("Silahkan masukkan nama file : ")
        try:
            with open(file_name + ".txt", 'r') as file:
                data = file.read()
                print(f"Jumlah data pada file {file_name}.txt: {len(data)}")
        except FileNotFoundError:
            print(f"Tidak Terdapat File dengan Nama {file_name}.txt")

    def menu_save_data_pada_file(self):
        if not any(self.data.values()):
            print("Data saat ini kosong.")
        else:
            file_name = input("Masukkan nama file : ")
            with open(file_name + ".txt", 'a') as file:
                # Header tabel
                if file.tell() == 0:
                    header = "+============================================================================"
                    file.write(f"{header}\n")
                    self.data_tersimpan_added = False
                
                if not self.data_tersimpan_added:
                    file.write("|Data yang tersimpan\n")
                    file.write("+============================================================================\n")
                    self.data_tersimpan_added = True
                    
                # Data
                data_row = f"|Nama      : {self.data['Nama']}\n|Email     : {self.data['Email']}\n|Password  : {self.data['Password']}\n"
                file.write(f"{data_row}")
                file.write("+============================================================================\n")
                
            print("Berhasil")

    def menu_buat_data_baru(self):
        while True:
            nama = input("Masukkan Nama: ")
            email = input("Masukkan Email: ")

            if not email.endswith("@student.unhas.ac.id") or re.search('[A-Z_ /-]', email):
                print("=======================================================")
                print("Email yang Anda Masukkan Salah.")
                print("=======================================================")
                continue  # Kembali ke awal loop

            break  # Keluar dari loop jika email sesuai

        while True:
            password = input("Masukkan Password: ")
            
            if not (8 <= len(password) <= 20):
                print("=======================================================")
                print("Pasword harus memiliki panjang 8-20")
                print("=======================================================")
            if not (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
                print("=======================================================")
                print("Password yang anda gunakan terlalu lemah Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                print("=======================================================")
                continue  # Kembali ke awal loop

            break  # Keluar dari loop jika password sesuai

        self.data = {"Nama"    : nama, "Email"   : email, "Password": password}
        print("Data baru berhasil dibuat!")

    def menu_keluar(self):
        print("Sampai Jumpa Lagi")
        exit()

    def run_program(self):
        while True:
            print("=======================================================")
            print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
            print(" a. Detail Anda")
            print(" b. Ubah Nama")
            print(" c. Jumlah Data pada File")
            print(" d. Save Data pada File")
            print(" e. Buat Data Baru")
            print(" f. Keluar")

            choice = input(" Silahkan Pilih Opsi Anda : ").lower()
            print("=======================================================")
            
            if choice == 'a':
                self.menu_detail_anda()
            elif choice == 'b':
                self.menu_ubah_nama()
            elif choice == 'c':
                self.menu_jumlah_data_pada_file()
            elif choice == 'd':
                self.menu_save_data_pada_file()
            elif choice == 'e':
                self.menu_buat_data_baru()
            elif choice == 'f':
                self.menu_keluar()
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang benar.")


data_manager = DataManagement()
data_manager.run_program()
