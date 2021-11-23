import unittest
import math
from ex1 import Shape
from ex1 import Triangle
from ex1 import Rectangle
from ex1 import Square
from ex1 import Circle

class TestShape(unittest.TestCase):

   def test_areaTriangle(self):
     self.assertEqual(Triangle(10,5).area(), 25.0)     
     
   def test_rectangle(self):
     self.assertEqual(Rectangle(10,5).area(), 50) 

   def test_square(self):
     self.assertEqual(Square(5).area(), 25)

   def test_circle(self):
     self.assertEqual(Circle(3).area(), 28.274333882308138)
     self.assertEqual(Circle(3).perimeter(), 18.84955592153876)

if __name__ == "__main__":
  unittest.main()