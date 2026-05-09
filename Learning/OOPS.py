
from Car import car

car1 = car("LFA",2009,"Burgundy",False)
car2 = car("corvette",2019,"blue",True)
car3 = car("mustang",2025,"yellow",True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.describe()
