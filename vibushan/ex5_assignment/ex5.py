# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Are of Rectangle")
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
    
#     def area(self):
#         print("Area of a square")
#         # return self.length * self.length
#         area = super().area()
#         return area - 1

# class Cube(Square):
#     def surface_area(self):
#         face_area = super(Cube, self).area()
#         return face_area * 6

#     def volume(self):
#         face_area = super(Square, self).area()
#         return face_area * self.length



# if __name__ == "__main__":
#     square = Square(6)
#     print("Area of a square: ", square.area())
#     print("Perimeter of a square: ", square.perimeter())
    
#     cube = Cube(3)
#     print("Area of a cube", cube.area())
#     print("Surface Area of a cube: ", cube.surface_area())
#     print("Volume of a cube: ", cube.volume())
    
    

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
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def area(self):
        return ((self.base*self.height)/2)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.number_of_sides = 4
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(1)
        self.radius = radius

    def area(self):
        pi = 3.141592653589793
        return pi * self.radius**2

    def perimeter(self):
        pi = 3.141592653589793
        return 2 * pi * self.radius

if __name__ == "__main__":

    tri = Triangle(2,3)
    rect = Rectangle(3,4)
    sqr = Square(4)
    circle = Circle(4)

    print(f"Number of sides of Triangle is {tri.number_of_sides}")
    print(f"Area of Triangle is {tri.area()}")

    print(f"Number of sides of Rectangle is {rect.number_of_sides}")
    print(f"Area of Rectangle is {rect.area()}")    

    print(f"Number of sides of Square is {sqr.number_of_sides}")
    print(f"Area of Square is {sqr.area()}")

    print(f"Number of sides of circle is {circle.number_of_sides}")
    print(f"Area of circle is {circle.area()}")
    print(f"Perimeter of circle is {circle.perimeter()}")