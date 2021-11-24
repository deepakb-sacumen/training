class Shape():
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base   = base

    def area(self):
        return 0.5*self.height*self.base   # Triangle Area = 1/2(height*base)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width    # Rectangle Area = length*width

class Square(Rectangle):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length*self.length  # Square area = length^2

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.142* self.radius* self.radius  # Circle area = pi*radius^2      # Note: pi = 3.142

    def perimeter(self):
        return 2*3.142*self.radius             # Circle Perimeter = 2*pi*radius  # Note: pi = 3.142


if __name__ == "__main__":
    shape = Shape(5)
    triangle = Triangle(2,5)
    rectangle = Rectangle(2,5)
    square = Square(5)
    circle = Circle(5)

    print('Shape function is working        -->', shape.number_of_sides)
    print('Area of Triangle is Triangle     -->', triangle.area())
    print('Area of Rectangle is Rectangle   -->', rectangle.area())
    print('Area of Square is Square         -->', square.area())
    print('Circle of Square is Circle       -->', circle.area())
    print('Circle of Square is Perimeter    -->', circle.perimeter())
