# Versi 1
import turtle
turtle.showturtle()

turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.done()

# Versi 2
import turtle
turtle.showturtle()

turtle.right(60)
for i in range(2):
  for j in range(3):
    turtle.forward(100)
    turtle.right(120)
  turtle.left(180)
turtle.done()
