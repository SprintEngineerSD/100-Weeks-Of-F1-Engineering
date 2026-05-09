class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} {self.position}"

    @staticmethod
    def is_valid (position):
        valid_position = ["Manager","Cook","Janitor"]
        return position in valid_position

employee1 = Employee("Juan","Manager")
employee2 = Employee("squidward","Cook")

print(Employee.is_valid("Cook"))
print(employee1.get_info())
print(employee2.get_info())