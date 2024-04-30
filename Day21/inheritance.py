
import abc
import math

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water")

    def breathe(self):
        super().breathe()
        print(", but do it underwater")

nemo = Fish()
nemo.swim()
nemo.breathe()

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square(Rectangle):
    def __init__(self, side = 1):
        super().__init__(width = side, height = side)
    
c = Circle(2)

shapes = []
shapes.append(Circle(4))
shapes.append(Rectangle(2, 7))
shapes.append(Square(42))

for shp in shapes:
    print(f"Area of shape: {shp.area()}")

