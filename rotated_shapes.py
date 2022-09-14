import turtle

turtle.speed(500)
def makeASquare():
    for x in range(20):
        turtle.rt(20)
        for x in range(4):
            turtle.rt(90)
            turtle.fd(100)

turtle.rt(270)
def shapeAngle():
    for x in range(1):
        turtle.fd(50)
        turtle.rt(55)
        turtle.fd(50)
def shapeAngle1():
    turtle.rt(-270)
    turtle.fd(50)

turtle.speed(5000)

t = turtle.Turtle()
side = 5
for i in range(100):
    t.forward(side)
    t.right(90)
    side = side + 2

turtle.exitonclick()
