class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self._nama = nama
        self._nim = nim
        self._jurusan = jurusan
        self._ipk = ipk
        
    def get_nama(self):
        return self._nama
    def set_nama(self, nama):
        self._nama = nama
        
    def get_nim(self):
        return self._nim
    def set_nim(self, nim):
        self._nim = nim
        
    def get_jurusan(self):
        return self._jurusan
    def set_jurusan(self, jurusan):
        self._jurusan = jurusan
    
    def get_ipk(self):
        return self._ipk
    def set_ipk(self, ipk):
        self._ipk = ipk
        
        
    def _tampilkan_info(self):
        print("Nama:", self._nama)
        print("NIM:", self._nim)
        print("Jurusan:", self._jurusan)
        print("IPK:", self._ipk)

    def _hitung_predikat(self):
        if self._ipk >= 3.5:
            return "Cumlaude"
        elif self._ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self._ipk >= 2.5:
            return "Memuaskan"
        elif self._ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

mahasiswa = Mahasiswa("Indy Sekar Ayu", "H071231010", "Sistem Informasi", 3.75)
mahasiswa2 = Mahasiswa("Diza", "H071234", "matematika", 3.55)
mahasiswa3 = Mahasiswa("Sisy", "H01234562", "kimia", 2.33)

mahasiswa._tampilkan_info()
mahasiswa2._tampilkan_info()
mahasiswa3._tampilkan_info()

print("Predikat:", mahasiswa._hitung_predikat())
print("Predikat:", mahasiswa2._hitung_predikat())
print("Predikat:", mahasiswa3._hitung_predikat())