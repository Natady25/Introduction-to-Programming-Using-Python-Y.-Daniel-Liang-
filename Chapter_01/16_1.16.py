# Versi 1
import turtle
turtle.showturtle()

turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.circle(50)
turtle.right(180)
turtle.circle(50)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.circle(50)
turtle.right(180)
turtle.circle(50)
turtle.done()

# Versi 2
import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(-50,0)
for i in range(2):
  turtle.penup()
  turtle.forward(100)
  turtle.pendown()
  for j in range(2):
    turtle.circle(50)
    turtle.right(180)
  turtle.right(180)    
turtle.done()

# Versi 3
import turtle
turtle.showturtle()

initial_position = [(-50, 0), (50, 0), (-50, -100), (50, -100)]

for x, y in initial_position:
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.circle(50)   
turtle.done()
