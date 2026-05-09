import random


#low =1
#high = 100
#options = ("rock","paper", "scissors" )
#cards = ["2","3","4","5","6","7","8","9","J","Q","K","A"]

#number = random.randint(low, high)
#number = random.random()
#option = random.choice(options)
#random.shuffle(cards)

#print(cards)

#NUMBER GUESSING GAME

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses= 0
is_running = True

print("Python Number Game")
print(f"Select a Number Between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter Your Guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if highest_num < guess or guess < lowest_num:
            print("That number is out of range")
            print(f"Please Select a Number Between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low Try Again!")
        elif guess > answer:
            print("Too High Try Again")
        else:
            print(f"Correct!, The answer was {answer}")
            print(f"Number of attempts: {guesses}")
            is_running = False

    else:
     print("Invalid Guess")
     print(f"Please Select a Number Between {lowest_num} and {highest_num}")
 