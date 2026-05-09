#while loop = execute some code while some condition remains true

#name = input('enter your name:')
#while name == "":
 #   print("You did not enter your name")
  #  name = input('enter your name:')
#else:
#    print(f"Hello {name}")


#Compound interest calculator
#principle = 0
#rate = 0
#time = 0
#while True :
#    principle = float(input("Enter principle amount"))
#    if principle <= 0:
#        print("principle cannot be less than or zero")
#    else:
#        break
#while True:
#    rate = float(input("Enter interest rate amount"))
#    if rate <= 0:
#        print("interest rate cannot be less than or zero")
#    else:
#        break
#while True:
#    time = float(input("Enter time in years"))
#    if time <= 0:
#        print("time cannot be less than or zero")
#    else:
#        break
#total = principle * pow((1+ rate / 100), time)
#print(f"Balance after {time} year/s : ${total:.2f} ")


#LIST COMPREHENSION: A concise way to create lists in python
                    # compact and easier to read then traditional loops
                #   [expression for value in iterable if condition]

#doubles = [ x * 2  for x in range(1,11) ]
#triples = [y * 3 for y in range(1,11)]
#print(triples)

#fruits = ["apple", "orange", "banana", "coconut"]
#fruit_chars = [  fruit[0] for fruit in fruits]
#print(fruit_chars)

