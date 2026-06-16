coordinate = input("Enter the center of the rectangle: ")
x, y = [int(x) for x in coordinate.split(",")]
width_height = input("Enter the width and height: ")
w, h = [int(x) for x in width_height.split(",")]

import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(x - w/2, y + h/2)
turtle.pendown()

for i in range (2):
	turtle.forward(w)
	turtle.right(90)
	turtle.forward(h)
	turtle.right(90)

turtle.done()