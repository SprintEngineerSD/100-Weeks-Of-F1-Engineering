#variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> enclosed -> Global -> Built-In

#def func1():
#    x = 1
#    print(x)                                 # this is local functions where one cannot see inside each other function
#def func2():
#    x = 2
#    print(x)
#func1()
#func2()



#def func1():
#    print(x)                                # This is global version
#def func2():
#    print(x)
#x = 3
#func1()
#func2()


#from math import e
#def func1():
#    print(e)                            #here we have both global and built-in but the priority wise global is taken
                                       #                    ( LEGB )sequence
#e = 3
#func1()