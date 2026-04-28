# functions = A block of reusable code
#               place() after a function name to invoke it


#def happy_birthday():
#    print("Happy birthday to u!")
#happy_birthday()
#happy_birthday()

#def display_invoice(username, amount,due_date):
#    print(f"Hello {username}")
#   print(f"Your Bill of ${amount:.2f} is due on {due_date} ")
#display_invoice("joe jeff", 100.33, "01/02")




#RETURN = STATEMENT USED TO END A FUNCTION
#           AND SEND A RESULT BACK TO CALLER

#def add(x,y):
#    z = x+y
#    return z
#def subtract(x,y):
#    z = x-y
#    return z
#def multiply(x,y):
#    z = x*y
#    return z
#def divide (x,y):
#    z = x/y
#    return z
#print(add(1,2))
#print(subtract(1,2))
#print(multiply(1,2))
#print(divide(1,2))




#DEFAULT ARGUMENTS: A default value for certain parameters
#                   default is used when argument is omitted
#                   make your functions more flexible, reduces # of arguments
#                  1. positional, 2.DEFAULT, 3.keyword, 4.arbitrary

#def net_price(list_price, discount=0, tax=0.05):
#    return list_price * (1-discount) * (1+tax)

#print(net_price(500))

#print(net_price(500,0.1,))
#print(net_price(500,0.1,0))



#KEYWORD ARGUMENTS: an argument preceded by an identifier
#                   helps with readability
#                   order of argument don't matter

#def hello(greeting,title,first,last):
#    print(f"{greeting} {title}.{first} {last}")

#hello(greeting="Hello", title="Mr", first="Spongebob", last="sqpants")



#ARBITARY ARGUMENTS:
# *args = allow you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#           * unpacking operator


#def display_name(*args):
#    for arg in args:
#        print(arg,end=" ")
#display_name("spongebob","harold", "squarepants")



def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="ajmera",
              city="pune",
              state="MAHA",
              zip="411018")


