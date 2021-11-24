"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class.
Create Circle class which inherits Shape class.
Define Area and perimeter of circle.
Print number of sides, area of each object and Perimeter of Circle object
"""

class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Triangle(Shape):
    def __init__(self, height, width):
        super().__init__(3)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width * 0.5


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        return super().area()


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    triangle = Triangle(2, 4)
    print("Number of sides in a triangle: ", triangle.number_of_sides)
    print("Area of a triangle: ", triangle.area())

    rectangle = Rectangle(2, 6)
    print("Number of sides in a rectangle: ", rectangle.number_of_sides)
    print("Area of a rectangle: ", rectangle.area())

    square = Square(6)
    print("Number of sides in a square: ", square.number_of_sides)
    print("Area of a square: ", square.area())

    circle = Circle(3)
    print("Number of sides in a circle: ", circle.number_of_sides)
    print("Area of a circle: ", circle.area())
    print("Perimeter of a circle: ", circle.perimeter())