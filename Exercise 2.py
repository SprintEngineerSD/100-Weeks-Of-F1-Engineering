# exercise : Shopping cart program
from idlelib.run import uninstall_recursionlimit_wrappers

#item = input("What item would u like to buy?:")
#price = float(input("what is the price?: "))
#quantity = int(input("How many would u like?: "))

#Total = price * quantity

#print(f"You have bought {quantity} x {item}/s")
##print(f"The total is: ${Total}")


#Area of circle
#import math

#radius = float(input("Enter radius of circle"))

#area = math.pi  * pow(radius, 2)
#print(f"the area of circle is: {round(area, 2)}cm ")



#Python weight calculator

#weight = float(input("Enter your weight: "))
#unit = input("Enter the unit (Kg/Lb): ")

#if unit == "Kg":
#    weight = weight * 2.205
#    unit = "Lbs."
#    print(f"Your weight is: {round(weight, 2)} {unit}")
#elif unit == "Lb":
#    weight = weight / 2.205
#    unit = "Kgs."
#    print(f"Your weight is: {round(weight, 2)} {unit}")
#else:
#    print(f"{unit} is not valid unit")



#ROCK PAPER SCISSOR GAME
import random

options = ("rock", "paper", 'scissor')

playing = True
while playing:

    player = None
    computer = random.choice(options)

    while  player not in options:
        player = input("Enter a choice (rock , paper, scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a Tie!")
    elif player == "rock" and  computer == "scissor":
        print("You win")
    elif player == "paper" and  computer == "rock":
        print("You win")
    elif player == "scissor" and  computer == "paper":
        print("You win")
    else:
        print("You lose!")

    if not input("play again? y/n: ").lower() == "y":
        playing = False

print("Thanks for Playing!")
