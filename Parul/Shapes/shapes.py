class Shape(object):
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, height, breadth):
        self.number_of_sides = 3
        self.height = height
        self.breadth = breadth

    def area(self):
        return self.height * self.breadth * 0.5

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.number_of_sides = 4
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        return super().area()

class Circle(Shape):
    def __init__(self, radius):
        self.number_of_sides = 0
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

