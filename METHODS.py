#STATIC METHOD = A method that belong to a class rather than any object from that class
#               used for general utility functions

#Instance methods = best for operations on instances of class (objects)
#Static methods = Best for utility functions that do not need access to class data
#class Employee:
#    def __init__(self,name,position):
#        self.name = name
#        self.position = position
#    def get_info(self):
#        return f"{self.name} = {self.position}"
#    @staticmethod
#    def is_valid_position(position):
#        valid_position = ["Manager","Cashier","Cook","Janitor"]
#        return position in valid_position
#employee1 = Employee("Sponge","Manager")
#print(Employee.is_valid_position("Manager"))
#print(employee1.get_info())



#CLASS METHOD: Allows operations related to class itself
#              take (cls) as the first parameter, which represents the class itself
#class Student:
#    count = 0
#    def __init__(self,name,gpa):
#        self.name = name
#        self.gpa = gpa
#        Student.count += 1
#INSTANCE METHOD
#    def get_info(self):
#        return f"{self.name} {self.gpa}"
#    @classmethod
#    def get_count(cls):
#        return f"total number of students: {cls.count}"

#MAGIC METHODS: Dunder methods __init__,__str__,__eq__
#               They are automatically called by many of Python's built-in operations
#               They allow developers to define or customise the behaviour of objects

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} was not found"



book1 = Book("The Hobbit","J.R.R. Tolkein", 510)
book3 = Book("The Hobbit","J.R.R. Tolkein", 223)
book2 = Book("Harry Potter","J.K.Rowling",172)

print(book1)
print(book1 == book3)
print(book3 < book1)
print(book3 > book2)
print(book1 + book3)
print("J.R.R." in book1)
print(book1['title'])