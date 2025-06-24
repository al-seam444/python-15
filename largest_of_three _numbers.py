a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

def largest_of_three(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

print(f"Largest of {a}, {b}, {c} is {largest_of_three(a, b, c)}")
