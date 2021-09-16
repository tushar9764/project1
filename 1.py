class circle():
  def __init__(self, r):
    self.radius = r
  
  def area(self):
    return self.radius**2*3.14
  
  def perimeter(self):
    return self.radius*2*3.14

A = circle(4)
print("Area of circle is: ", A.area())
print("Perimeter of circle is: ", A.perimeter())