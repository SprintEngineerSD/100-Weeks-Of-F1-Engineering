# object = A "bundle" of related attributes (variables) and methods ( functions)
#          ex. phone, cup, book
#          you need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"you stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("Mustang",2024,"red", False)
car2 = Car("Corvette", 2025, "blue",True)
#print(car1.model)
#print(car1.year)
#print(car1.color)
#print(car1.for_sale)
#print(car2.model)
#car1.drive()
#car1.stop()
#car2.drive()
#car2.stop()
#car1.describe()