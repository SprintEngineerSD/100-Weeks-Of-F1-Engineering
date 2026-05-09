# EXERCISE calculate area of rectangle

#Length = float(input("Enter the Length:"))
#Width = float(input("Enter the Width:"))
#Area = Length * Width
#print(f"The area is {Area} cm²")

#MATH FUNC EXERCISE 1
#import math
#radius = float(input('Enter the radius of a circle: '))

#circumference = 2 * math.pi * radius

#print(f"The circumference is : {round(circumference, 2)}")



#Python calculator

#operator = input("Enter an operator (+ - * /):")
#num1 = float(input("Enter the first number:"))
#num2 = float(input("Enter the Second number:"))

#if operator == "+":
#    result = num1 + num2
#   print(result)
#elif operator == "-":
#    result = num1 - num2
#    print(result)
#elif operator == "*":
#    result = num1 * num2
#    print(result)
#elif operator == "/":
#    result = num1 / num2
#    print(result)

#else:
#    print(f"{operator} is not valid")

#CONCESSION STAND PROGRAM (ASSOCIATED WITH DICTIONARY)
menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":5.00,
        "fries":2.50}

cart =[]
total = 0
print("-------Menu------- ")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: ${total:.2f}")

