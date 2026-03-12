from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    

class square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2
    

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height
    
    
circle = circle(5)
print("Circle Perimeter:", circle.calculate_perimeter())
print("Circle Area:", circle.calculate_area())

square = square(4)
print("Square Perimeter:", square.calculate_perimeter())
print("Square Area:", square.calculate_area())

rectangle = rectangle(3, 6)
print("Rectangle Perimeter:", rectangle.calculate_perimeter())
print("Rectangle Area:", rectangle.calculate_area())

