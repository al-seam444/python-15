class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

w = float(input("Enter rectangle width: "))
h = float(input("Enter rectangle height: "))
rect = Rectangle(w, h)
print(f"Area of rectangle: {rect.area()}")