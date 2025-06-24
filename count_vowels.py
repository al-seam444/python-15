def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

s = input("Enter a string to count vowels: ")
print(f"Number of vowels in \"{s}\" is {count_vowels(s)}")