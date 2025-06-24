class Number:
    def __init__(self, value):
        self.value = value
    def is_even(self):
        return self.value % 2 == 0
    def is_odd(self):
        return self.value % 2 != 0

n = int(input("Enter a number for Number class: "))
number = Number(n)
print(f"{n} → Even? {number.is_even()}, Odd? {number.is_odd()}")