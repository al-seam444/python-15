class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
st = Student(name, age)
st.print_info()
