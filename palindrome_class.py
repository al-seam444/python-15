class Palindrome:
    def __init__(self, word):
        self.word = word
    def is_palindrome(self):
        clean = self.word.replace(" ", "").lower()
        return clean == clean[::-1]

s = input("Enter a word/string for Palindrome check: ")
p = Palindrome(s)
print(f"Is palindrome? {p.is_palindrome()}")