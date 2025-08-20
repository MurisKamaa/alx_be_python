import math

class Shape:
    def area():
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        computed_area = self.length * self.width
        return computed_area

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        computed_area = math.pi * self.radius**2
        return computed_area