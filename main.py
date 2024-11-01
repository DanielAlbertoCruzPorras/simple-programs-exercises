# Get user inputs
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
age = int(input("Enter age in years: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine risk level based on age and BMI
if age < 45:
    if bmi < 22.0:
        risk = "low"
    else:
        risk = "medium"
else:
    if bmi < 22.0:
        risk = "medium"
    else:
        risk = "high"

print(f"Your risk level is {risk}.")

