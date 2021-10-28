class Car:

  def _init_(self, model_no):
    self.model_no = model_no

  def print_model_no(self):
    print(self.model_no)

c1 = Car("model no. of c1 = z001")
c1.print_model_no()

c2 = Car("model no. of c2 = z002")
c2.print_model_no()
print("\n")

var = c1
c1 = c2
c2 = var

c1.print_model_no()
c2.print_model_no()