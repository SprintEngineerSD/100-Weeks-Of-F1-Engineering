
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class  Car(Vehicle):
    def go(self):
        print("go")
    def stop(self):
        print("stop")

class Motorcycle(Vehicle):
    def go(self):
        print("Your motorcycle goes")
    def stop(self):
        print("U stop the motorcycle")

class boat(Vehicle):
    def go(self):
        print("You sail the boat")
    def stop(self):
        pass

car = Car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()


boat = boat()
boat.go()
boat.stop()


