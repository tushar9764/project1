import math as mt

class Shape:

  def _init_(self, shape):
    self.shape = shape

  def area(self):
    pass  

class circle(Shape):

   1........def _init_(self, radius):
    self.radius = radius

  def area(self):
    print((mt.pi)(self.radius)*2)

class square(Shape):
  
  def _init_(self, side):
    self.side = side

  def area(self):
    print((self.side)**2)

class rectangle(Shape):

  def _init_(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def area(self):
    print(self.length*self.breadth)

shape1 = circle(3)
shape1.area()  

shape2 = square(8)
shape2.area()

shape3 = rectangle(10,12)
shape3.area()