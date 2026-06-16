#Versi 1
side = float(input("Enter the side: "))

area = ((3 * (3 ** 0.5)) / 2) * side ** 2

print(f"The area of the hexagon is {area:.4f}")

#Versi 2
import math

side = float(input("Enter the side: "))

area = ((3 * math.sqrt(3)) / 2) * side ** 2

print(f"The area of the hexagon is {area:.4f}")