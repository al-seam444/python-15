def is_palindrome(s):
    clean = s.replace(" ", "").lower()
    return clean == clean[::-1]

s = input("Enter a string to check palindrome: ")
print(f"\"{s}\" is palindrome? {is_palindrome(s)}")