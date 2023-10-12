def is_palindrome(x: str):
    x = x.replace(" ", "").lower()
    
    if x == x[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

# Test Case 1
print(is_palindrome("radar")) 

# Test Case 2
print(is_palindrome("Step on no pets"))  
