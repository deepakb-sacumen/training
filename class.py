"""
Create a shape class which has a property number_of_sides
Create Triangle class which inherits Shape class. Define Area of triangle
Create Rectangle class which inherits Shape class. Define Area of Rectangle
Create Square class which inherits Rectangle class. 
Create Circle class which inherits Shape class. 
Define Area and perimeter of circle.
Print number of sides, area of each object and Perimeter of Circle object
"""
import math
class Shape:
    def __init __(self,sides):
         self.sides=sides
    def area(self):
         print("Area of shape")
    def perimeter(self):
        print ("perimeter of shape")
class Triangle(shape):
    def __init__(self,a,b,c): 
    super().__init__(a,b,c)
        self.a = float(a) 
        self.b = float(b) 
        self.c = float(c) 
    def area(self): 
        s=(self.a + self.b + self.c)/2 
        return((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)         
class Rectangle(Shape):
    def __init __(self,length,width):
    super().__init__(length,width)
        self.length=length
        self.width=width
    def area(self):
        print("Area of rectangle")
        return self.length*self.width
    def perimeter(self):
        return 2 * self.length + 2 *self.width
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def area(self):
        print("Area of a square")
        area = super().area()
        return area - 1
class Circle(Shape):
    def __init__(self,radius):
    super().__init__(radius)
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 if __name__ == "__main__":
    circle=circle(9)
    print("number of sides: ",shape.sides())
    print("area of circlet: ",circle.area())
    print("perimeter of circle: ",circle.perimeter()) 






        
        
        
        
    
        
        
            
    
 
