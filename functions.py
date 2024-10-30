# creating a function in python
def sal():
    print("My name is Saline")
# the below is callng a function
sal()
def addnums():
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(f"The sume of {num1} and {num2} is {num1+num2}")
addnums()
# function with parameters
def java_class(name,age,gender):
    print(f"Student name is: {name}, age is: {age}, and gender is {gender}")
java_class("saline", 34, "female")