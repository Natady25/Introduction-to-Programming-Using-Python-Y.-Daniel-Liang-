import turtle
turtle.showturtle()

line = [(-50, 25), (50, 25), (75, 50), (75, 0), (50, -25), (-50, -25), (-25, 0)]

turtle.penup()
turtle.goto(-50, 25)
turtle.pendown()

for i in range(2):
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)

turtle.penup()
turtle.goto(-25, 50)
turtle.pendown()

for i in range(2):
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)
  turtle.right(90)

for x,y in line:
  turtle.goto(x, y)

turtle.done()