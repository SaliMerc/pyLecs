#create a program that checks if a number is odd or even
num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#create a program that checks if someone can  vote or not
age= int(input("Enter your age: "))
if age>=18:
    print("You can vote")
else:
    print("Failed! You cannot vote")

#create a program that checks if a student's grade
grades=int(input("Enter Marks: "))
if 100 >= grades >= 80:
    print("You got an A")
elif 79 >= grades >= 60:
    print("You got an B")
elif 59 >= grades >= 40:
    print("You got an C")
elif 39 >= grades >= 0:
    print("Failure")
else:
    print("Wrong input you've put there honey!")
#create a program to calculate your BMI

