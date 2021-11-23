import pytest
from shape.ex5 import Shape,Triangle,Rectangle,Square,Circle


def test_triangle():
    Triangle1 = Triangle(3,10,8)
    assert Triangle1.no_of_sides == 3
    assert Triangle1.area_of_triangle() == 40

def test_rectangle():
    rectangle1 = Rectangle(4,10,5)
    assert rectangle1.no_of_sides == 4
    assert rectangle1.area_of_rect() == 50
    assert rectangle1.peri_of_rect() == 30


def test_square():
    square1 = Square(4,10)
    assert square1.no_of_sides == 4
    assert square1.area_of_square() == 100
    assert square1.peri_of_square() == 40

def test_circle():
    circle1 = Circle(0,4)
    assert circle1.no_of_sides == 0
    assert circle1.area_of_circle() == 50.24
    assert circle1.peri_of_circle() == 25.12
