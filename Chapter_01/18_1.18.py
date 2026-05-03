# Versi 1
import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(0, 50)
turtle.down()
turtle.goto(-30, -30)
turtle.goto(40, 25)
turtle.goto(-40, 25)
turtle.goto(30, -30)
turtle.goto(0, 50)
turtle.done()

# Versi 2
import turtle
turtle.showturtle()

turtle.penup()
turtle.goto(0, 50)
turtle.down()

star = [(-30, -30), (40, 25), (-40, 25), (30, -30), (0, 50)]
for x, y in star:
  turtle.goto(x, y)

turtle.done()

# Versi 3
import turtle
turtle.showturtle()

turtle.right(72)
for i in range(5):
  turtle.forward(100)
  turtle.right(144)

turtle.done()