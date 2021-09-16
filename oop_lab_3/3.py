
class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
 
    def total_fare(self):
        return self.capacity * 100
 
class bus(vehicle):
    def __init__(self, name, mileage, capacity=50):
        vehicle.__init__(self, name, mileage, capacity)
        self.final_amount = vehicle.total_fare(self) + vehicle.total_fare(self) * 0.1
 
    def bus_fare(self):
        print("Final amount - ",self.final_amount)
 
c1 = vehicle("Wheel steal", 25, 10)
b1 = bus("Big car", 20)
print("Car Fare - ",c1.total_fare())
b1.bus_fare()