#Versi 1
import math

radius, length = eval(input("Enter the radius and length of a cylinder: "))

area = radius * radius * math.pi

volume = area * length

print("The area is", int(area * 100) / 100)
print("The volume is", int(volume * 100) / 100)


#Versi 2
import math

userInput = input("Enter the radius and length of a cylinder: ")
radius, length = [float(x) for x in userInput.split(",")]

area = radius * radius * math.pi
volume = area * length

print(f"The area is {area:.4f}")
print(f"The volume is {volume:.1f}")