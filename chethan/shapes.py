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
    def __init__(self,length, width) -> None:
        """Intialize two sides
        :type length: int
        :param length:  length of shape

        :type width: int
        :param width: width of shape

        :return: None
        :rtype: None
        """
        self.length = length
        self.width = width

    def number_0f_sides(self, sides) -> None:
        """Number of sides of shape
        
        :type sides: str
        :param sides: Number of sides

        :return: None
        :rtype: None
        """
        print("number of sides:", sides)
    
    def area(self) -> int:
        """Area of the shape."""
        return self.length * self.width
    
    def perimeter(self) -> int:
        """"Perimeter of shape"""
        return 2 * self.length + 2 * self.width

class Rectangle(Shape):
    def __init__(self, length) -> None:
        super().__init__(length, length)

    def area(self) -> int:
        """Area of the rectangle."""
        area = super().area()
        return area
    
    def perimeter(self) -> int:
        """"Perimeter of rectangle"""
        perimeter = super().perimeter()
        return perimeter

class Triangle(Shape):
    def __init__(self, length):
        super().__init__(length, length)
    
    def area(self) -> int:
        """Area of the triangle."""
        return super().area()/2
    
    def perimeter(self) -> int:
        """"Perimeter of triangle"""
        return super().perimeter() - self.length

class Square(Rectangle):
    def __init__(self, length) -> int:
        super().__init__(length)
    
    def area(self) -> int:
        """Area of the square."""
        return super().area()
    
    def perimeter(self) -> int:
        """"Perimeter of square"""
        return super().perimeter()
    
if __name__ == "__main__":
    """"Main function call"""
    #calculation of rectangle
    rectangle = Rectangle(4)
    print("Rectangle")
    sides = "4"
    rectangle.number_0f_sides(sides)
    print("area of rectangle:", rectangle.area())
    print("area of perimeter:", rectangle.perimeter())

    #calculation of triangle
    triangle = Triangle(4)
    print("Triangle")
    sides = "3"
    triangle.number_0f_sides(sides)
    print("area of triangle:", triangle.area())
    print("area of perimeter:", triangle.perimeter())

    #calculation of square
    square = Square(4)
    print("Square")
    sides = "4"
    square.number_0f_sides(sides)
    print("area of square:", square.area())
    print("perimeter of square:", square.area())

