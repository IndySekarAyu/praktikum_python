import re

def is_valid_ipv4(input_str):
    parts = input_str.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False

    return True

def is_valid_ipv6(input_str):
    parts = input_str.split(':')
    if len(parts) != 8:
        return False

    for part in parts:
        if not re.match(r'^[0-9a-zA-Z]{1,4}$', part):
            return False

    return True

def check_ip_addresses():
    N = int(input("Masukkan jumlah baris input: "))
    results = []

    for i in range(N):
        input_str = input()
        
        if is_valid_ipv4(input_str):
            results.append("IPv4")
        elif is_valid_ipv6(input_str):
            results.append("IPv6")
        else:
            results.append("Bukan IP Address")

    for result in results:
        print(result)

check_ip_addresses()















# import re

# def is_ipv4(input_str):
#     ipv4_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
#     return re.findall(ipv4_pattern, input_str)

# def is_ipv6(input_str):
#     ipv6_pattern = r'^([0-9A-Za-z]{1,4}:){7}[0-9A-Za-z]{1,4}$'
#     return re.findall(ipv6_pattern, input_str)

# def check_ip_addresses():
#     N = int(input("Masukkan jumlah baris input: "))
#     results = []

#     for i in range(N):
#         input_str = input()
#         input_str = input_str.strip()
#         input_str = re.sub(r':0+', ':', input_str)

#         if is_ipv4(input_str):
#             results.append("IPv4")
#         elif is_ipv6(input_str):
#             results.append("IPv6")
#         else:
#             results.append("Bukan IP Address")

#     for result in results:
#         print(result)
        
# check_ip_addresses()












