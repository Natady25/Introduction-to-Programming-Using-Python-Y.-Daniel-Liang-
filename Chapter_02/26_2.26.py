import math
import turtle
turtle.showturtle()

coordinate = input("Enter the center of a circle: ")
x, y = [float(x) for x in coordinate.split(",")]
radius = float(input("Enter the radius of a circle: "))

turtle.penup()
turtle.goto(x , y - radius)
turtle.pendown()
turtle.circle(radius)

area = math.pi * (radius ** 2)

turtle.penup()
turtle.goto(x,y)
turtle.write(f"{area:.2f}")

turtle.done()