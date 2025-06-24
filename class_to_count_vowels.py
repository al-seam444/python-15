class VowelCounter:
    def __init__(self, text):
        self.text = text
    def count(self):
        return sum(1 for ch in self.text.lower() if ch in "aeiou")

s = input("Enter a string for vowel counting: ")
vc = VowelCounter(s)
print(f"Vowel count: {vc.count()}")