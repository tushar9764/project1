class student:
  def set_details(self):
    self.name = str(input("Enter the name of student - "))
    self.reg_no = str(input("Enter the reg no - "))
    self.age = int(input("Enter the age - "))
    self.gender = str(input("Enter the gender - "))
    self.branch = str(input("Enter the branch - "))
    self.sem = int(input("enter the semister  - "))
 
  def get_details(self):
    print("Name - ",self.name,"\nReg. No. - ",self.reg_no,"\nAge - ",self.age,"\nGender - ",self.gender,"\nBranch - ",self.branch,"\nSem - ",self.sem)
  
class studentresultinfo(student):
  def set_result(self):
    self.total_marks = int(input("Enter student total marks - "))
    self.percentage = int(input("Enter student percentage - "))
    self.grade = str(input("Enter the grede of student - "))
 
  def get_result(self):
    print("Total marks - ",self.total_marks,"\nPercentage - ",self.percentage,"\nGrade - ",self.grade)
 
print("Display using inherited class")
s1 = studentresultinfo()
s1.set_details()
s1.set_result()
s1.get_details()
s1.get_result()