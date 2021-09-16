class Student:
    sem = 3
    institute = "IIIT DWD"
    
    def setData(self):
        self.name = input("Enter the name of the student : ")
        self.id = int(input("Enter the USN of student : "))

    def getInstanceData(self):
        print(f"Name : {self.name}")
        print(f"USN = {self.id}")

    @classmethod
    def getClassData(cls):
        print(f"Semester : {cls.sem}")
        print(f"Institute : {cls.institute}")

    @staticmethod
    def getExplanation():
        print("Class variables (sem, institute) are printed using ClassMethod and Instance variables (name, id) are printed using Instance Method")


s1 = Student()
s1.setData()
s1.getInstanceData()
Student.getClassData()
Student.getExplanation()