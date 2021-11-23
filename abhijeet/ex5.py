class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Are of Rectangle")
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


# if __name__ == "__main__":
#     square = Square(6)
#     print("Area of a square: ", square.area())
#     print("Perimeter of a square: ", square.perimeter())
    
#     cube = Cube(3)
#     print("Area of a cube", cube.area())
#     print("Surface Area of a cube: ", cube.surface_area())
#     print("Volume of a cube: ", cube.volume())
    
    
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

# Create a shape class which has a property number_of_sides
class Shape():
    def __init__(self,no_of_sides):
        self.no_of_sides = no_of_sides

# Create Triangle class which inherits Shape class. Define Area of triangle
class Triangle(Shape):
    def __init__(self, no_of_sides,base,height):
        super().__init__(3)
        self.base = base
        self.height = height
    
    def area_of_triangle(self):
        return((self.base * self.height)/2)

# Create Rectangle class which inherits Shape class. Define Area of Rectangle
class Rectangle(Shape):
    def __init__(self, no_of_sides,length,width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area_of_rect(self):
        return self.length * self.width

    def peri_of_rect(self):
        return 2 * (self.length + self.width)

# Create Square class which inherits Rectangle class. 
class Square(Rectangle):
    def __init__(self, no_of_sides, side):
        super().__init__(4, side, side)
        self.side = side

    #area of square
    def area_of_square(self):
        area_of_square = super().area_of_rect()
        return area_of_square

    #perimeter of square
    def peri_of_square(self):
        return 4 * self.side

# Create Circle class which inherits Shape class. 
class Circle(Shape):
    def __init__(self, no_of_sides,radius):
        super().__init__(0)
        self.radius = radius
    # Define Area and perimeter of circle.
    def area_of_circle(self):
        return 3.14 * (self.radius ** 2)

    def peri_of_circle(self):
        return 2 * 3.14 * self.radius 


# Print number of sides, area of each object and Perimeter of Circle object

triangle = Triangle(3,12,8)
rectangle = Rectangle(4,10,15)
square = Square(4,5)
circle = Circle(0,4)


#no of sides
print(f'number of sides in triangle is {triangle.no_of_sides}')
print(f'number of sides in rectangle is {rectangle.no_of_sides}')
print(f'number of sides in square is {square.no_of_sides}')
print(f'number of sides in circle is {circle.no_of_sides}\n\n')

#area
print(f'area of triangle is {triangle.area_of_triangle()}')
print(f'area of rectangle is {rectangle.area_of_rect()}')
print(f'area of square is {square.area_of_square()}')
print(f'area of circle is {circle.area_of_circle()}\n\n')

#permieter
print(f'perimeter of circle is {circle.peri_of_circle()}')
