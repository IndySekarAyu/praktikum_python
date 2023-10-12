M = float(input("masukkan derajat "))

total_detik = int((M / 360) * 24 * 60 * 60)

jam = (total_detik // 3600 + 6) % 24
menit = (total_detik % 3600) // 60
detik = total_detik % 60

if 6 <= jam < 12:
    waktu = "Selamat Pagi"
elif 12 <= jam < 18:
    waktu = "Selamat Siang"
elif 18 <= jam < 24:
    waktu = "Selamat Sore"
else:
    waktu = "Selamat Malam"

print(waktu)
print(f"{jam:02d}:{menit:02d}:{detik:02d}")