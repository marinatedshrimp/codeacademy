import math

class Circle:
    def __init__(self, a, b, r):
        self.a = a         
        self.b = b         
        self.r = r
    
    def area(self):
        return self.r ** 2 * math.pi

    def perimeter(self):
        return 2 * self.r * math.pi
    
    def testBelongs(self, x, y):
        dx = abs(x - self.r)
        dy = abs(y - self.r)
        if dx <= self.r and dy <= self.r:
            return "the point is in the circle"
        else:
            return "the point is not in the circle"

a = Circle(2, 3, 6)
print(a.testBelongs(14,2))
        