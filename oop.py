#using classes
class Fruits:
    # class should always be named using a capital letter
    # constructor method
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
        # normal method
    def display(self):
        print(f"I like eating {self.name}, it costs {self.price} and it is {self.color} in color")
# creating instance of a class or object
myobject=Fruits("Apples", 100, "pink")
myobject.display()
myobject2=Fruits("Pineapples", 230, "yellow")
myobject2.display()