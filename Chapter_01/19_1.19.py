import turtle
turtle.showturtle()

polygon = [(40, -69.28), (-40, -69.28), (-80, -9.8), (-40, 69), (40, 69), (80, 0)]

turtle.penup()
turtle.goto(80, 0)
turtle.pendown()

for x, y in polygon:
  turtle.goto(x, y)

turtle.done()