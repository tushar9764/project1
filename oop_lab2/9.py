class Student:
    def setData(self):
        self.Name = input("Enter the name : ")
        self.ID = int(input("Enter the Roll Number : "))
        self.sem = int(input("Enter the semester number : "))
        self.nLaptop = int(input("Enter the number of laptops : "))
        self.listLaptop = []
        for i in range (0, self.nLaptop):
            tempObj = self.Laptop()
            self.listLaptop.append(tempObj)

    class Laptop:
        def __init__(self):
            self.cpu = input("Enter the name of the CPU : ")
            self.ram = input("Enter the RAM of the Laptop : ")
            self.hardDisk = input("Enter the size of hard disk : ")
            self.display = input("Enter the display resolution : ")
        
        def getData(self):
            print(f"CPU : {self.cpu}") 
            print(f"RAM : {self.ram}")
            print(f"Hard Disk : {self.hardDisk}")
            print(f"Display Resolution : {self.display}")

    def getData(self):
        print(f"Name : {self.Name}") 
        print(f"USN : {self.ID}")
        print(f"Semester : {self.sem}")
        print(f"Number of Laptops : {self.nLaptop}")
        for i in range(0, self.nLaptop):
            print(f"Details of laptop {i+1}  : ")
            self.listLaptop[i].getData()

S1 = Student()
S1.setData()
S1.getData()