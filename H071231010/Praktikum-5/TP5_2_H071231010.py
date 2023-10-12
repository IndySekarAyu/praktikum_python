def string_baru(input_string):
    x = len(input_string)
    if x % 2 == 0:
        return"kata tidak boleh genap"
    else:
         middle_index = x // 2
    new_string = input_string[0] + input_string[middle_index] + input_string[-1]
    return new_string

input_string = input("Masukkan kata: ")
new_string = string_baru(input_string)
print(new_string)