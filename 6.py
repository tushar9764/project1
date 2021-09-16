
class Time:
    def Default(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def Value(self, hours, minutes, seconds):
        if seconds > 59:
            tempMinutes = seconds // 60
            seconds = seconds % 60
            self.seconds = seconds
            self.minutes = tempMinutes + minutes
        else:
            self.seconds = seconds
            self.minutes = minutes

        if self.minutes > 59:
            tempHours = self.minutes // 60
            self.minutes = self.minutes % 60
            self.hours = tempHours + hours
        else:
            self.minutes = minutes
            self.hours = hours

    def display(self):
        print(f"Time : {self.hours}::{self.minutes}::{self.seconds}")

T1 = Time()
T1.Default()
T1.display()
T1.Value(20, 59, 59)
T1.display()
T1.Value(20, 140, 250)
T1.display()
T1.Value(20, 140, 50)
T1.display()