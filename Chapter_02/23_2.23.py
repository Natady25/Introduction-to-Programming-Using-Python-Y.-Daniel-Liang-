# Versi 1
import turtle
turtle.showturtle()

r = int(input("Enter radius for circle: "))

turtle.penup()
turtle.goto(-1 * r,0)
for i in range(2):
  turtle.penup()
  turtle.forward(2 * r)
  turtle.pendown()
  for j in range(2):
    turtle.circle(r)
    turtle.right(180)
  turtle.right(180)    
turtle.done()

# Versi 2
import turtle
turtle.showturtle()

r = int(input("Enter radius for circle: "))

initial_position = [(-1 * r, 0), (r, 0), (-1 * r, -2 * r), (r, -2 * r)]

for x, y in initial_position:
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	turtle.circle(r)

turtle.done()
