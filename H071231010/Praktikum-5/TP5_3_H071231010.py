def is_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    sorted_kata1 = sorted(kata1)
    sorted_kata2 = sorted(kata2)

    return sorted_kata1 == sorted_kata2

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if is_anagram(kata1, kata2):
    print("True")
else:
    print("False")
