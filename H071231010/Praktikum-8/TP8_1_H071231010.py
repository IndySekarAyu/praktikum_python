import re

def validate_string(input_string):
    regex_pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
    
    if re.findall(regex_pattern, input_string) and len(input_string) == 45:
        return True
    else:
        return False

input_string = input("Masukkan string: ")

if validate_string(input_string):
    print("True")
else:
    print("False")
