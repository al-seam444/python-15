def sum_of_list(lst):
    return sum(lst)

lst_input = input("Enter numbers separated by space to sum: ")
lst = list(map(float, lst_input.split()))
print(f"Sum of {lst} is {sum_of_list(lst)}")