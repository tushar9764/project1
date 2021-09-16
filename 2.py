class Faculty:

    def setData(self):
        self.name = input("Enter the name : ") 
        self.emp_ID = int(input("Enter  employee ID : "))
        self.branch = input("Enter branch : ")
        self.salary = int(input("Enter  salary : "))

    def getData(self):
      print(f"Name: ", {self.name})
      print(f"Employee ID: ", {self.emp_ID})
      print(f"Branch: ", {self.branch})
      print(f"Salary: ", {self.salary})

      return self.name, self.emp_ID, self.branch, self.salary

list_Faculty = []
for i in range(1, 6):
    temp = Faculty()
    print(f"\nEnter  data for employee {i}  : ")
    temp.setData()
    list_Faculty.append(temp)

for i in range(0, 5):
    print(f"\nData of employee {i+1}  : ")
    list_Faculty[i].getData()