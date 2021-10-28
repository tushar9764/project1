from abc import ABC, abstractmethod
class Travel(ABC):
    def _init_(self, num, distance, mode):
        self.__num = num
        self.distance = distance
        self.mode = mode

    @abstractmethod
    def cost(self):
        pass

class Bus(Travel):
    def _init_(self, num, distance):
        Travel._init_(self, num, distance, 'Bus')

    def cost(self):
        return 100*self.Travel_num                    

class Train(Travel):
    def _init_(self, num, distance):
        Travel._init_(self, num, distance, 'Train')

    def cost(self):
        return 60*self.Travel_num

dharwadToBelagavi = 80               #Distance in km
trainTrip = Train(4, dharwadToBelagavi)
print("Cost for traveling by train:", trainTrip.cost())
busTrip = Bus(4, dharwadToBelagavi)
print("Cost for traveling by bus  :", busTrip.cost())