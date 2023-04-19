# Weight Converter
# This program converts weight from pounds to kilograms and vice versa

weight = float(input("Enter weight: "))
unit = input("Enter unit (pounds or kilograms): ")

if unit.lower() == "pounds":
    converted_weight = weight / 2.205
    print("Weight in kilograms:", round(converted_weight, 2), "kg.")
elif unit.lower() == "kilograms":
    converted_weight = weight * 2.205
    print("Weight in pounds:", round(converted_weight, 2), "lbs.")
else:
    print("Invalid unit. Please enter 'pounds' or 'kilograms'.")
