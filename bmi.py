# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)  # BMI formula: weight (kg) / height^2 (m^2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

# Input weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Print the BMI result
print(f"Your BMI is: {bmi:.2f}")

# Interpret the BMI result
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
