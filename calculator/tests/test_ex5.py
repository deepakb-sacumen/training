from src.ex5 import Triangle,Rectangle,Square,Circle
import pytest

def test_triangle():
    triangle = Triangle(2,5)
    triangle_area = triangle.area()
    assert triangle_area == 5

def test_rectangle():
    rectangle = Rectangle(2,5)
    rectangle_area = rectangle.area()
    assert rectangle_area == 10

def test_square():
    square = Square(5)
    square_area = square.area()
    assert square_area == 25

def test_circle():
    circle = Circle(5)
    circle_area = circle.area()
    circle_perimeter = circle.perimeter()
    assert circle_area == 78.55
    assert circle_perimeter == 31.419999999999998




