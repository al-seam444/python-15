def reverse_string(s):
    return s[::-1]

s = input("Enter a string to reverse: ")
print(f"Reversed string: \"{reverse_string(s)}\"")


# 10. Check leap year
def is_leap_year(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

year = int(input("Enter a year to check leap year: "))
print(f"{year} is leap year? {is_leap_year(year)}")