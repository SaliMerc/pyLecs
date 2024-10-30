#create a class called person with name, age, and gender as the attributes. Have a constructor method, a normal method and three objects
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print(f"My name is {self.name}; my age is {self.age} and my gender is {self.gender}")

person1=Person("Mercy", 23, "Female")
person1.display()
person2=Person("Kate", 21, "Female")
person2.display()
person3=Person("Onyi", 25, "Male")
person3.display()