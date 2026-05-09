#Madlibs Game
#word game where u create story with fill in the blanks

#adjective1 = input("enter and adjective: ")
#noun1 = input("Enter a noun: ")
#adjective2 = input("enter and adjective: ")
#verb1 = input("Enter a verb ending with 'ing' ")
#adjective3 = input("enter and adjective: ")



#print(f"Today i went to a { adjective1} zoo.")
#print(f"In an exhibit, I saw a {noun1}")
#print(f"{noun1} was {adjective2} and {verb1}")
#print(f"I was {adjective3}! ")

# Hypotenuse of right angle triangle

#import math

#a = float (input("enter side A :"))
#b = float (input("enter side B :"))
#c = math.sqrt(pow(a,2)+ pow(b,2))

#print(f"side c equals {round(c,2)}cm")


# Temperature converter

unit = input("Enter the Unit C/F:")
Temp = float(input("Enter the Temperature: "))

if unit == "C":
    Temp = round((Temp * 9) / 5 + 32, 1)
    print(f"The Temperature is {Temp}°F")

elif unit == "F":
    Temp = round((Temp -32) * 5 / 9 , 1)
    print(f"The Temperature is {Temp}°C ")

else:
    print(f"{unit} this unit is invalid")
