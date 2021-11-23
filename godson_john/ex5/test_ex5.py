import pytest
from ex5 import Triangle, Rectangle, Square, Circle

def test_triangle():
    """
    Test case for the Triangle class
    """
    triangle = Triangle(2, 5)
    area = triangle.area()
    assert area == 5

def test_rectangle():
    """
    Test case for the Rectangle class
    """
    rectangle = Rectangle(3, 4)
    area = rectangle.area()
    assert area == 12

def test_square():
    """
    Test case for the Square class
    """
    square = Square(5)
    area = square.area()
    assert area == 25

def test_circle():
    """
    Test case for the Circle class
    """
    circle = Circle(7)
    area = circle.area()
    perimeter = circle.perimeter()
    assert area == 153.86
    assert perimeter == 43.96
    