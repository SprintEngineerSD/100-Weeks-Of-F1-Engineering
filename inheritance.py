#Inheritance = allows a class to inherit attributes and methods from another class
#               helps with code reusability and extensibility
#               class Child(Parent)



#class Animal:
#    def __init__(self,name):
#        self.name = name
#        self.is_alive = True
#    def eat(self):
#        print(f"{self.name} is eating ")
#    def sleep(self):
#        print(f"{self.name} is sleeping")
#class Dog(Animal):
#       pass
#class Cat(Animal):
#    pass
#class Mouse(Animal):
#    pass
#dog = Dog("Scooby")
#cat = Cat("Garfield")
#mouse = Mouse("Mickey")



#MULTIPLE INHERITANCE:
#class Animal():
#    def eat(self):
#        print("This animal is Eating")
#class Predator(Animal):
#    def hunt(self):
#        print("This animal is hunting")
#class Prey(Animal):
#    def flee(self):
#        print("This animal is fleeing")
#class Fish(Prey,Predator):
#    pass
#fish = Fish()
#fish.hunt()
#fish.flee()
#fish.eat()


#super() = Function used in a child class to call methods from a parent class (superclass)
#          Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        print(f"it is a circle of radius {self.radius} and area of {3.14 * self.radius * self.radius:.2f}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled,side_length):
        super().__init__(color, is_filled)
        self.side_length = side_length

    def describe(self):
        print(f" it is a square of area of {self.side_length * self.side_length:.2f}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f" it is a triangle of area of {self.width * self.height:.2f}cm^2")
        super().describe()

circle = Circle("red",True,5)
square = Square("blue",False,6)
triangle = Triangle("yellow",True,4,7)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()

print(square.color)
print(square.is_filled)
print(square.side_length)
square.describe()

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()