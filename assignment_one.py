# remember to use comments!
import turtle

# moving turtle to fit everything
turtle.penup()
turtle.fd(-100)
turtle.pendown()

# making tirangle (you can also loop but this is an example w/o loops)
turtle.forward(100)
turtle.rt(120)
turtle.forward(100)
turtle.rt(120)
turtle.forward(100)
turtle.rt(120)

# moving turtle to make square
turtle.penup()
turtle.forward(120)
turtle.pendown()

# using a loop to create a square
for x in range(4):
    turtle.forward(100)
    turtle.rt(90)

# moving turtle
turtle.penup()
turtle.left(90)
turtle.fd(50)
turtle.pendown()

# creating a pentagon with loops
for x in range(5):
    turtle.fd(50)
    turtle.rt(72)

# moving turtle
turtle.penup()
turtle.left(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(50)
turtle.pendown()

turtle.circle(90)

turtle.exitonclick()
