# @ property = Decorator used to define a method as a property (it can be accessed as an attribute)
#               Benefits: Add additional logic when read ,write or delete attributes
#               Gives you greater, setter and deleter method.



class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("must be greater than 0")
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("must be greater than 0")


rectangle = Rectangle(3,4)

rectangle.width = 99
rectangle.height = 69
print(rectangle.width)
print(rectangle.height)