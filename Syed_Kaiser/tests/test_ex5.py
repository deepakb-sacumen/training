import pytest
from ex5.ex5 import (Circle, Rectangle, Shape, Square, Triangle)

def test_shape():
    shape = Shape(3)
    assert shape.number_of_sides == 3

def test_traingle():
    triangle = Triangle(10,17,3)
    assert triangle.number_of_sides == 3
    assert triangle.base == 10
    assert triangle.height == 17

def test_triangle_area():
    triangle = Triangle(10,17,3)
    res = triangle.area()
    assert res == 85.0

def test_rectangle_area():
    rectangle = Rectangle(5,10,2)
    res = rectangle.area()
    assert res == 50

def test_square_area():
    square = Square(18,2)
    res = square.area()
    assert res == 324

def test_perimeter():
    circle = Circle(15,0)
    res = circle.perimeter()
    assert res == 94.2