POUND_IN_KILOGRAMS = 0.45359237
INCH_IN_METERS = 0.0254

weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

weight_in_kilograms = weight * POUND_IN_KILOGRAMS
height_in_meters = height * INCH_IN_METERS

BMI = weight_in_kilograms / (height_in_meters ** 2)

print(f"BMI is {BMI:.4f}")
