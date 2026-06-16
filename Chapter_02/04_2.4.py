#Versi 1
poundToKilogram = 0.454

pound = eval(input("Enter a value in pounds: "))

kilogram = pound * poundToKilogram

print(pound, "pounds is", kilogram, "kilograms")

#Versi 2
poundToKilogram = 0.454

pound = float(input("Enter a value in pounds: "))

kilogram = pound * poundToKilogram

print(f"{pound} pounds is {kilogram} kilograms")