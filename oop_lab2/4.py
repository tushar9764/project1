class Records:

    def setData(self):
        self.name = input("name of the student : ")
        self.ID = int(input("USN of the student : "))
        self.marks = []
        for i in range(1, 4):
            marks = input(f"Enter the marks for subject {i} : ")
            self.marks.append(marks)

    def getData(self):
        print(f"Name : {self.name}")
        print(f"USN : {self.ID}") 
        print(f"Marks : \nSubject 1 : {self.marks[0]} \nSubject 2 : {self.marks[1]} \nSubject 3 : {self.marks[2]}")
        return self.name, self.ID, self.marks

s1 = Records()
s1.setData()
list_1 = s1.getData()
print(list_1)