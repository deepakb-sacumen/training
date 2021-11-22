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
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def number_0f_sides(self, sides):
        print("number of sides:", sides)
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Rectangle(Shape):
    def __init__(self, length):
        super().__init__(length, length)

    def area(self):
        area = super().area()
        return area
    
    def perimeter(self):
        perimeter = super().perimeter()
        return perimeter

class Triangle(Shape):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self):
        return super().area()/2
    
    def perimeter(self):
        return super().perimeter() - self.length

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length)
    
    def area(self):
        return super().area()
    
    def perimeter(self):
        return super().perimeter()
    
if __name__ == "__main__":
    rectangle = Rectangle(4)
    print("Rectangle")
    sides = "4"
    rectangle.number_0f_sides(sides)
    print("area of rectangle:", rectangle.area())
    print("area of perimeter:", rectangle.perimeter())

    triangle = Triangle(4)
    print("Triangle")
    sides = "3"
    triangle.number_0f_sides(sides)
    print("area of triangle:", triangle.area())
    print("area of perimeter:", triangle.perimeter())

    square = Square(4)
    print("Square")
    sides = "4"
    square.number_0f_sides(sides)
    print("area of square:", square.area())
    print("perimeter of square:", square.area())

