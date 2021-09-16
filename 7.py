class Student:
    def __init__(self, name, age, rollNo):
        self.name = name
        self.age = age
        self.rollNo = rollNo

    @classmethod
    def compare(cls, s1, s2):
        if s1.age == s2.age:
            print("Age of the students are equal.")
        else:
            print("Age of the students are not equal.")

S1 = Student("tushar", 19, 55)
S2 = Student("sanket", 20, 56)

Student.compare(S1, S2)