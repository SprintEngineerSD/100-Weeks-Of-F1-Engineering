
class Engine:
    def __init__(self,HP):
        self.HP=HP

class Wheel:
    def __init__(self,size):
        self.size=size

class Car:
    def __init__(self, make,model,HP,wheel_size):
        self.make=make
        self.model=model
        self.engine=Engine(HP)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_parametrs(self):
        return f"{self.make} {self.model} {self.engine.HP} hp {self.wheels[0].size} inches"

car =Car("FORD","MUSTANG",1001,18)

print(car.display_parametrs())



