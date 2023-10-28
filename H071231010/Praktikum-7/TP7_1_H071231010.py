import os
import random
import datetime

# Fungsi untuk menghasilkan ID transaksi
def generate_transaction_id(full_name):
    tanggal = datetime.datetime.now()
    date_str = tanggal.strftime("%y%m%d%H%M")
    random_number = random.randint(100,999)
    words = full_name.split()

    # Initialize an empty string to store the initials
    initials = ""

    # Iterate through the words and add the first character of each word to the initials
    for word in words:
        initials += word[0]

    # Convert the initials to uppercase
    initials = initials.upper()
    transaction_id =f"{initials}{date_str}{random_number}"
    return transaction_id

# Fungsi untuk mencetak invoice dan menyimpannya
def print_invoice(transaction_id, cashier_name, products):
    invoice_filename = f"invoices/{transaction_id}.txt"
    with open(invoice_filename, "w") as invoice_file:
        invoice_file.write(f"Invoice ID: {transaction_id}\n")
        invoice_file.write(f"Kasir: {cashier_name}\n\n")
        invoice_file.write("Produk yang dibeli:\n")
        invoice_file.write("Product================Price====Qty====Subtotal\n")
        
        total_price = 0
        for product in products:
            product_name, price, quantity = product
            subtotal = price * quantity
            total_price += subtotal
            
            # Write product information in a tabular format
            table_row = f"{product_name}============{price:.2f}===={quantity}===={subtotal:.2f}\n"
            invoice_file.write(table_row)
        invoice_file.write("\nTotal Harga: " + str(total_price))

# Fungsi untuk mencatat riwayat transaksi
def log_transaction(transaction_id, total_price):
    log_filename = "trx_history.txt"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(log_filename, "a") as log_file:
        log_file.write(f"{now}, {transaction_id}, {total_price}\n")

# Fungsi untuk menampilkan invoice berdasarkan ID transaksi
def display_invoice(transaction_id):
    invoice_filename = f"invoices/{transaction_id}.txt"
    if os.path.exists(invoice_filename):
        with open(invoice_filename, "r") as invoice_file:
            print(invoice_file.read())
    else:
        print(f"Invoice dengan ID {transaction_id} tidak ditemukan.")

# Main program
if not os.path.exists("invoices"):
    os.mkdir("invoices")

while True:
    print("Selamat datang di program kasir sederhana!")
    cashier_name = input("Masukkan nama kasir: ")
    products = []
    
    while True:
        product_name = input("Nama Produk (ketik 'selesai' untuk menyelesaikan transaksi): ")
        if product_name.lower() == 'selesai':
            break
        price = float(input("Harga: "))
        quantity = int(input("Jumlah: "))
        products.append((product_name, price, quantity))
    
    if len(products) > 0:
        transaction_id = generate_transaction_id(cashier_name)
        print_invoice(transaction_id, cashier_name, products)
        total_price = sum(price * quantity for _, price, quantity in products)
        log_transaction(transaction_id, total_price)
        print(f"Transaksi berhasil. Invoice ID: {transaction_id}")
    
    choice = input("Apakah Anda ingin menampilkan invoice? (y/n): ")
    if choice.lower() == 'y':
        transaction_id = input("Masukkan ID transaksi: ")
        display_invoice(transaction_id)
    
    another_transaction = input("Apakah Anda ingin melakukan transaksi lainnya? (y/n): ")
    if another_transaction.lower() != 'y':
        break
    

