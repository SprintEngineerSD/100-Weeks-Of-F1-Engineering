# if = Do some code only IF sone condition is TRUE
    #else do something else

#age = int(input("Enter your Age:"))

#if age >= 90:
 #   print("You are too old to sign up")
#elif age >= 18:
  #  print("You are now signed up")
#elif age < 0:
 #   print("You haven't been born yet")
#else:
   # print("You are not eligible")




#response = input("Would u like some food? (Y/N):")

#if response == "Y":
#    print("Have some food")

#else:
#    print("no food for u")


#CONDITIONAL EXPRESSIONS = a one line shortcut for if else statements (ternary operator)
#                            Print of assign one of two values based on conditions
#                            X if condition else Y
#num = 6
#a = 8
#b = 7
#print("positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"
#max_num =  if a>b else b
#min_num = if a<b else b
#print(min_num)



#MATCH-CASE STATEMENT: an alternative to using many elif statements
#                       execute some code if value matches 'case'
#                   Benefits: cleaner and syntax more readable
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))
