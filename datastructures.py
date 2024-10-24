#lists
#cannot have a duplicate
from tkinter import PanedWindow

cars=["Toyota", "Mercedes", "Subaru", "BMW"]
cars.sort()
print(cars)
# print(f"I love {cars[1]}")
cars[1]="Nissan"
cars.sort()
print(f"I love {cars[1]}")
#pop ni kutoa
#sort ni kuziarrange


#tuple data structure
#can be accessed using an index as in a list
#can have a duplicate
#this is not changeable i.e immutable, it is ordered
fruits=("mangoes","bananas","apples")
print(fruits)

#set
#it is not ordered
color={"yellow","blue","green","black"}
print(color)

#dictionary
#it is mutable
#has key value pairs
employees={"name":"saline", "age":23, "salary":100000}
print(f"The age of {employees['name']} is: {employees['age']}")