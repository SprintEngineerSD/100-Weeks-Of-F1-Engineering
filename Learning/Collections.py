#Collections = single "variable" used to store multiple values
# List   = [] ordered and changeable . Duplicates OK
# set    = {} unordered and immutable but add/remove OK. no Duplicates
# Tuples = ()   ordered and unchangeable \. Duplicates OK , Faster
#from loop import total

#fruits = ["apple", "orange", "banana", "coconut"]
#print(dir(fruits)) for list of what we can do with the collections

#fruits[0] = "pineapple" (we can reassign values with this [] )

#fruits.append("pineapple") # to add items to the list we can use append
#fruits.remove("apple") # to remove items from the list
#fruits.insert(0, "pineapple") # to insert something within a list at a location
#fruits.sort() # To make them alphabetical order
#fruits.reverse() # To reverse the list
#fruits.clear() # to clear the elements
#print(fruits.index("coconut")) # to find the location of the item placed
#print(fruits.count("apple")) # to count the  item placed in the list


#print(fruits)


#print(fruits[::1])
#for fruit in fruits:
 #   print(x)


#SHOPPING CART PROGRAM
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----Your cart-----")

for food in foods:
    print(food,end=" ")

for price in prices:
    total += price

print()

print(f"Your total is ${total} : ")



