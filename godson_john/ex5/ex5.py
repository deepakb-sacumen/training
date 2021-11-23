"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.

Print number of sides, area of each object and Perimeter of Circle object
"""

class Shape:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        print("No of sides: ", number_of_sides)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area_triangle = (self.base*self.height)/2
        return area_triangle

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area_rectangle = self.length*self.breadth
        return area_rectangle

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        area = super().area()
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius

    def area(self):
        return self.pi*(self.radius**2)

    def perimeter(self):
        return 2*self.pi*self.radius


if __name__ == "__main__":
    shape = Shape(5)
    triangle = Triangle(2,5)
    rectangle = Rectangle(7,3)
    square = Square(5)
    circle = Circle(7)
    
    print('Area of the Triangle: ', triangle.area())
    print('Area of the Rectangle: ', rectangle.area())
    print('Area of the Square: ', square.area())
    print('Area of the Circle: ', circle.area())
    print('Perimeter of the Circle: ', circle.perimeter())
    