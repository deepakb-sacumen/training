"""This file contains test cases of ex5.py file"""
import pytest
from ex5_assignment.ex5 import Triangle, Rectangle, Square, Circle

def test_triangle_func():
    res = Triangle(int(2),int(3))
    assert res.area() == 3
    assert res.number_of_sides == 3

def test_restangle_func():
    res = Rectangle(2,3)
    assert res.area() == 6
    assert res.number_of_sides == 4

def test_square_func():
    res = Square(2)
    assert res.area() == 4
    assert res.number_of_sides == 4

def test_circle_func():
    res = Circle(3)
    assert res.area() == 28.274333882308138
    assert res.perimeter() == 18.84955592153876
    assert res.number_of_sides == 1
