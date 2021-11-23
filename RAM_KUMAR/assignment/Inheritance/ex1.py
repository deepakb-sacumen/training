import math

class Shape:
    def __init__(self):
        print ("Use Sub-Class")

    def __sides__(self,number_of_sides):
        self.number_of_sides = number_of_sides     
        print("Total number of sides are...",number_of_sides)


# Here we declare that the Triangle class inherits from the Shape class

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
                   

    def area(self):  
        super().__sides__(3)
        area = 0.5 * self.base * self.height         
        print("Area of a Triangle is...",area)
        return area

# Here we declare that the Rectangle class inherits from the Shape class

class Rectangle (Shape):
    def __init__(self, length, breadth):
      self.length = length
      self.breadth = breadth
    
    def area(self):
         super().__sides__(4)
         area = self.length * self.breadth
         print("Area of a Rectangle is...",area)
         return area

# Here we declare that the Square class inherits from the Rectangle class

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)
        

    def area(self):
        super().__sides__(4)
        area = self.length * self.length
        print("Area of a Square is...",area)
        return area


# Here we declare that the Circle class inherits from the Shape class

class Circle(Shape):    
    def __init__(self,radius):
        self.radius = radius

    def area(self):        
        area = math.pi * self.radius * self.radius
        print("Area of a Cicle is...",area)
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("Perimeter of a Cicle is...",perimeter)
        return perimeter







        

        

    