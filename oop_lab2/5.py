class Patient:
    def setData(self):
        self.name = input("Enter the name of the patient : ")
        self.dateOfAdmission = input("Enter the date of admission : ")
        self.symptoms = input("Enter all the symptoms with a space in between : ").split(" ")
        self.oxygenLevel = int(input("Enter the oxygen level of the patient : "))
        self.dateOfDischarge = input("Enter the date of discharge : ")

    def getData(self):
        print(f"\nName : {self.name} \nDate of Admission : {self.dateOfAdmission} \nSymptoms : {self.symptoms} \nOxygen Level : {self.oxygenLevel} \nDate of Discharge : {self.dateOfDischarge}\n")
        return self.name, self.dateOfAdmission, self.symptoms, self.oxygenLevel, self.dateOfDischarge

    def checkSeverity(self):
        if self.oxygenLevel < 90:
            print("Patient's condition is severe.")
        else:
            print("Patient is fine.")


class Hospital:    
    def __init__(self):
        self.listOfPatients = []
        self.oxygenSupport = []

    def addPatient(self):
        temp = Patient()
        temp.setData()
        if temp.oxygenLevel < 90:
            self.oxygenSupport.append(1)
        else:
            self.oxygenSupport.append(0)
        self.listOfPatients.append(temp)

    def checkSeverity(self):
        name = input("Enter the name of the patient : ")
        for i in range(0, len(self.listOfPatients)):
            if name == self.listOfPatients[i].name:
              self.listOfPatients[i].checkSeverity()
              return 1
        print("Patient not found")


    def getOxygenSupport(self):
        return self.oxygenSupport.count(1)
    def generalWard(self):
        return self.oxygenSupport.count(0)

    def totalPatients(self):
        return len(self.listOfPatients)


H1 = Hospital()

for i in range(0, 2):
    H1.addPatient()
    H1.listOfPatients[i].getData()
    H1.listOfPatients[i].checkSeverity()

print(H1.getOxygenSupport())
print(H1.generalWard())
print(H1.totalPatients())
H1.checkSeverity()