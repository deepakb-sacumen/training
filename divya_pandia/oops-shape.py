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
    def __init__(self,num_sides):
        self.num_sides = num_sides

class Triangle(Shape):
    def __init__(self,height,base):
        self.height = height
        self.base = base


    def area_of_triangle(self):
        return (self.height*self.base)/2

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area_of_rectangle(self):
        return self.length*self.breadth


class Square(Rectangle):
    def __init__(self,length,breadth):
        super().__init__(length,length)
        super().__init__(breadth,breadth)

    def area_of_square(self):
        area = super().area_of_rectangle()
        return area - 1

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14

    def area_circle(self):
        return 2*self.pi*self.radius*self.radius

    def perimeter_circle(self):
        return 2*self.pi*self.radius

if __name__ == "__main__":
    circle = Circle(5)
    shape = Shape(3)
    rectangle = Rectangle(5,6)
    triangle = Triangle(5,3)
    square = Square(3,4)

    print("Number of sides",shape.num_sides)
    print("Area of Circle",circle.area_circle())
    print("Area of Rectangle",rectangle.area_of_rectangle())
    print("Area of Triangle",triangle.area_of_triangle())
    print("Area of Square",square.area_of_square())
    print("Perimeter of Circle",circle.perimeter_circle())