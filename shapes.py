import turtle

def draw_square(side_length, color):
    turtle.color(color)
    turtle.begin_fill()

    for x in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

draw_square(200, "green")
turtle.penup()
turtle.forward(300)
turtle.pendown()
draw_square(50, "gold")

turtle.exitonclick()