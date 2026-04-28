#Dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {"USA":"Washington DC",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia": "Moscow"}
#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("Russia"))
#if capitals.get("Japan"):
#    print("That capital Exists")
#else:
#    print("That capital Doesn't exists")

#capitals.update({"Germany":"Berlin"})
#capitals.pop("China")
#capitals.popitem()         Removes the latest key item that was inserted
#capitals.clear()
#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)
#values = capitals.values()
#for value in capitals.values():
#    print(value)
#items = capitals.items()
#for key , value in capitals.items():
#    print(f"{key}: {value}")