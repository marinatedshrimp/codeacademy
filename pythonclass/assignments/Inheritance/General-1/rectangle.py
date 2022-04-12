import math

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def display(self):
        print(f"length: {self.length}\n width: {self.width}\n")
        print(f"perimeter: {self.perimeter()}")
        print(f"area: {self.area()}")

class Parallelepipede(Rectangle):
    def __init__(self, width, length, height):
        Rectangle.__init__(self, width, length)
        self.height = height

    def volume(self):
        return self.width * self.length * self.height

a = Rectangle(4, 5)
print(a.area())