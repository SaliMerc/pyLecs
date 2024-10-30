#a function for calculating BMI
weight=float(input("Enter your weight in Kilograms: "))
height=float(input("Enter your height in meters: "))
#formula
bmi=weight/(height**2)
print(f"Your BMI is{bmi: .2f}")
#conditions
if bmi<18.5:
    print("You are underweight")
elif 18.5<=bmi<24.9:
    print("You are normal weight")
elif 24.9<=bmi<29.9:
    print("You are overweight")
else:
    print("You are obese")