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
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
        print('number of sides: ',number_of_sides)

class Triangle(Shape):
    def __init__(self, base, height, number_of_sides):
        super().__init__(number_of_sides)
        self.base = base
        self.height = height

    def area(self):
        triangle_area = (self.base*self.height)/2
        return triangle_area

class Rectangle(Shape):
    def __init__(self, length, breadth, number_of_sides):
        super().__init__(number_of_sides)
        self.length = length
        self.breadth = breadth

    def area(self):
        rectangle_area = self.length*self.breadth
        return rectangle_area

class Square(Rectangle):
    def __init__(self,length,number_of_sides):
        super().__init__(length, length, number_of_sides)
    
    def area(self):
        square_area = super(Square, self).area()
        return square_area

class Circle(Shape):
    def __init__(self,radius, number_of_sides):
        super().__init__(number_of_sides)
        self.pi = 3.14
        self.radius = radius

    def area(self):
        return self.pi*(self.radius**2)

    def perimeter(self):
        return 2*self.pi*self.radius

    

if __name__ == "__main__":
    shape = Shape(3)
    triangle = Triangle(10,17,3)
    rectangle = Rectangle(5,10,2)
    square = Square(18,2)
    circle = Circle(15,0)
    print('Area of Triangle: ', triangle.area())
    print('Area of Rectangle: ', rectangle.area())
    print('Area of Square: ', square.area())
    print('Area of Circle: ', circle.area())
    print('Perimeter of Circle: ', circle.perimeter())
