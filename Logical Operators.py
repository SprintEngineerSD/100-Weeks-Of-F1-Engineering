#Locigal Operators= To evaluate multiple conditions (or, and , not)
                 # or = At least one must be true
                 # and = both conditions are ture
                 # not = inverts the condition (not false , not true)

temp = 25

#is_raining = True
is_sunny = False

#if temp > 35 or temp <= 0 or is_raining:
  #  print("The Event is cancelled")
#else:
  #  print("The event is still scheduled")

if temp >= 28 and is_sunny:
    print("Outside is Hot and Sunny")
elif temp <= 0 and is_sunny:
    print("It is Cold Outside but sunny")
elif 28>temp>0 and is_sunny:
    print("It is perfect weather")

elif temp >= 28 and not is_sunny:
    print("Outside is Hot and not Sunny")
elif temp <= 0 and not is_sunny:
    print("It is Cold Outside and not sunny")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm")
    print("It is Cloudy")
