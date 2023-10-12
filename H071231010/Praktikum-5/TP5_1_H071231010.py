def string_campuran(s1, s2):
    mixed = ""
    len_s1 = len(s1)
    len_s2 = len(s2)
    min_len = min(len_s1, len_s2)

    for i in range(min_len):
        mixed += s1[i]
        mixed += s2[-(i+1)]

    return mixed

s1 = input("Masukkan s1: ")
s2 = input("Masukkan s2: ")

hasil_mixed = string_campuran(s1, s2)
print("Hasil mixed:", hasil_mixed)
