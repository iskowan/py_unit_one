import turtle

# defining turtle
t = turtle.Turtle()

# This makes the house
def makeASquare(color, size):
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.fd(size)
        t.rt(90)
    t.end_fill()

# This makes roof
def makeATriangle(color, size):
    t.color(color)
    t.begin_fill()
    t.rt(-60)
    for x in range(3):
        t.fd(size)
        t.rt(120)
    t.end_fill()

# this combines them to make it one definition
def makeHouse(color, size, color2, size2):
    makeASquare(color, size)
    makeATriangle(color2, size2)



t.speed(100)
#this makes a house and states the colors
makeHouse("blue", 100, "red", 100)
t.penup()
t.goto(-100, -50)
t.lt(300)
t.pendown()
makeHouse("green", 50, "yellow", 50)
t.penup()
t.goto(-175,-25)
t.lt(300)
t.pendown()
makeHouse("pink", 75, "orange", 75)
t.penup()
t.goto(175, -0)
t.lt(300)
t.pendown()
makeHouse("purple", 100, "green", 100)

turtle.exitonclick()