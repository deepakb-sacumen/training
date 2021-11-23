from ex1 import Shape
from ex1 import Triangle
from ex1 import Rectangle
from ex1 import Square
from ex1 import Circle


if __name__ == "__main__":
    triangle = Triangle(10,5)
    triangle.tri_area()
    rectangle = Rectangle(10,5)
    rectangle.area()
    square = Square(5)
    square.area()
    circle = Circle(3)
    circle.area()
    circle.perimeter()
    