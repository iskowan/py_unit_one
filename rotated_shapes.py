import turtle
t = turtle.Turtle()
turtle.speed(500)
#rotated squares
def makeASquare():
    for x in range(20):
        turtle.rt(20)
        for x in range(4):
            turtle.rt(90)
            turtle.fd(100)

def hexagon():
    turtle.rt(90)
    # makes hexagon
    for x in range(6):
        turtle.fd(50)
        turtle.rt(60)

def shapeAngle():
    for x in range(1):
        turtle.fd(50)
        turtle.rt(55)
        turtle.fd(50)

def shapeAngle1():
    turtle.rt(-270)
    turtle.fd(50)

# making spiral
def spiral():
    side = 5
    turtle.hideturtle()
    for i in range(100):
        t.forward(side)
        t.right(90)
        side = side + 2

#making rhombus repeated shaped thing
def rhombus():
    for x in range(2):
        t.fd(50)
        t.rt(120)
        t.fd(50)
        t.rt(60)
def makeACube():
    t.rt(30)
    rhombus()
    t.rt(120)
    rhombus()
    t.rt(120)
    rhombus()

def makeAThing():
    for x in range(2):
        t.fd(50)
        t.rt(-60)
    t.fd(50)

def makeAThing2():
    makeACube()
    t.fd(100)
    t.rt(30)
    makeACube()
    makeAThing()
    makeAThing()
    t.rt(-60)
    makeAThing()
    t.rt(-120)
    t.fd(50)
    t.rt(-60)
    t.fd(50)

t.speed(500)
makeAThing2()
t.fd(50)
t.rt(60)
t.fd(50)
t.rt(60)
t.fd(50)
t.rt(60)
t.fd(50)
t.rt(120)
t.fd(50)
t.rt(60)
t.fd(50)
t.rt(-60)
t.fd(50)
t.rt(-60)
t.fd(50)








turtle.exitonclick()
