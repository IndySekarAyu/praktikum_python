import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" 
    return re.findall(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z0-9]+\d{2,}@[a-z]+\.(com|co\.id)$" 
    return re.findall(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$" 
    return re.findall(pattern, password)

def validate_registrasion():
    username = input("Masukkan username: ")
    if is_valid_username(username):
        email = input("Masukkan email: ")
        if is_valid_email(email):
            password = input("Masukkan password: ")
            if is_valid_password(password):
                print("\nRegistrasi berhasil! Selamat datang,", username) 
            else:
                print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
        else:
            print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    else:
        print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")

validate_registrasion()
