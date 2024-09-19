# Abstraction in Python:
# Ex:1 Basic Example for Abstraction in Python?
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 *(self.width + self.height)
    
rectangle = Rectangle(28,29)
print(rectangle.area())
print(rectangle.perimeter())