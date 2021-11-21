class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle")
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        print("Area of a square")
        # return self.length * self.length
        area = super().area()
        return area - 1

class Cube(Square):
    def surface_area(self):
        face_area = super(Cube, self).area()
        return face_area * 6

    def volume(self):
        face_area = super(Square, self).area()
        return face_area * self.length


if __name__ == "__main__":
    square = Square(6)
    print("Area of a square: ", square.area())
    print("Perimeter of a square: ", square.perimeter())
    # import pdb;pdb.set_trace()
    cube = Cube(3)
    
    print("Area of a cube", cube.area())
    print("Surface Area of a cube: ", cube.surface_area())
    print("Volume of a cube: ", cube.volume())
    
    

"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.

Print number of sides, area of each object and Perimeter of Circle object
"""

class Shape():
    def __init__(self,number_of_sides):
        self.number_of_sides = number_of_sides
        print('number of sides: ',number_of_sides)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        triangle_area = (self.base*self.height)/2
        return triangle_area

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        rectangle_area = self.length*self.breadth
        return rectangle_area

class Square(Rectangle):
    pass

class Circle(Shape):
    def __init__(self,radius):
        self.pi = 3.14
        self.radius = radius

    def area(self):
        return self.pi*(self.radius**2)

    def perimeter(self):
        return 2*self.pi*self.radius

    

if __name__ == "__main__":
    shape = Shape(3)
    triangle = Triangle(10,17)
    rectangle = Rectangle(5,10)
    circle = Circle(15)
    print('Area of Triangle: ', triangle.area())
    print('Area of Rectangle: ', rectangle.area())
    print('Area of Circle: ', circle.area())
    print('Perimeter of Circle: ', circle.perimeter())
