user_input = input("Enter three points for a triangle: ")
x1, y1, x2, y2, x3, y3 = [float(x) for x in user_input.split(",")]

side_1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side_2 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5
side_3 = ((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) ** 0.5

s = (side_1 + side_2 + side_3) / 2

area = (s * (s - side_1) * (s - side_2) * (s - side_3)) ** 0.5

print(f"The area of the triangle is {area:.1f}")