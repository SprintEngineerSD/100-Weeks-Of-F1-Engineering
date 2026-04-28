 # Decorator = A function that extends the behaviour of another function
 #              Pass the base function as an argument to the decorator
 #            EX: @add_sprinkles


def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("you add sprinkles")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("You add fudge")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"here is your {flavour} ice cream")


get_ice_cream("")



