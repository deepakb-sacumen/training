import pytest
from oops_shape import Shape,Triangle,Rectangle,Square,Circle

#test case for printing num of sides
def test_shape():
    shape = Shape(3)
    print("Test the num of sides")
    assert shape.num_sides == 3

def test_areatriangle():
    triangle = Triangle(5,3)
    print("Test the area of triangle")
    assert 7.5 == triangle.area_of_triangle()

def test_arearectangle():
    rectangle = Rectangle(5,6)
    print("Test the area of rectangle")
    assert 30 == rectangle.area_of_rectangle()

def test_areacircle():
    circle= Circle(5)
    print("Test the area of circle")
    assert 157 == circle.area_circle()

def test_areasquare():
    square = Square(3,4)
    print("Test the area of Square")
    assert 15 == square.area_of_square()

def test_perimetercircle():
    print("Test the Perimeter of circle")
    circle = Circle(5)
    assert 31 == circle.perimeter_circle()