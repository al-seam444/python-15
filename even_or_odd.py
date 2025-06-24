def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

num = int(input("Enter a number to check even/odd: "))
print(f"{num} is {check_even_odd(num)}")