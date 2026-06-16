import turtle
turtle.showturtle()

s = int(input("Enter the value of hexagons side: "))

start_position = [(0, 0), (2 * s, 0), (0, -2 * s), (2 * s, -2 * s)]

turtle.left(90)

for x, y in start_position:
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	
	for i in range(6):
		turtle.forward(s)
		turtle.left(60)

turtle.done()