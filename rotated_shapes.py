import turtle

turtle.speed(500)
def makeASquare():
    for x in range(20):
        turtle.rt(20)
        for x in range(4):
            turtle.rt(90)
            turtle.fd(100)


makeASquare()
turtle.exitonclick()
