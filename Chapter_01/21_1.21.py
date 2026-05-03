import turtle
turtle.showturtle()

coordinate_time = [(-5, 83, 12), (87, -7, 3), (-2, -93, 6), (-87, -7, 9)]

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(100)
turtle.penup()

for x, y, z in coordinate_time:
  turtle.goto(x, y)
  turtle.write(z)

turtle.goto(0, 0)
turtle.pendown()
turtle.forward(80)
turtle.penup()
turtle.goto(0, 0)
turtle.right(187.5)
turtle.pendown()
turtle.pensize(3)
turtle.forward(60)

turtle.penup()
turtle.goto(-15, -120)
turtle.write("9:15:00")

turtle.done()