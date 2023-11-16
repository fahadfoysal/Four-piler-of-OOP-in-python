from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0
    
class Square(Shape):
    side = 4

    def area(self):
        print("Area of square: ", self.side * self.side)

class Recangle(Shape):
    width = 5
    length = 10

    def area(self):
        print("Area of rectangle: ", self.width * self.length)


square = Square()
rectangle = Recangle()
square.area()
rectangle.area()