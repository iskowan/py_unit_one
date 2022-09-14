import turtle

# defining turtle
t = turtle.Turtle()

def makeASquare(color):
    t.color(color)
    t.begin_fill()
    for x in range(4):
        t.fd(100)
        t.rt(90)
    t.end_fill()

def makeATriangle(color):
    t.color(color)
    t.begin_fill()
    t.rt(-60)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.end_fill()


t.hideturtle()

makeASquare("blue")
makeATriangle("red")

turtle.exitonclick()