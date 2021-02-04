import turtle


# main function
def main():
    turtle.bgcolor('grey')
    turtle.hideturtle()
    turtle.speed(0)
    triangle(100, 0, 0, 130, -100, 0, 'green')
    triangle(-100, 0, -200, -120, 0, -120, 'red')
    triangle(100, 0, 0, -120, 200, -120, 'blue')
    circle(0, 0, 47)
    turtle.done()


# triangle function
def triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.fillcolor(color)
    turtle.pensize(2)
    turtle.pencolor('magenta')
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()


# circle function
def circle(x, y, radius):
    turtle.pensize(2)
    turtle.pencolor('magenta')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(180)
    turtle.circle(radius)
    for count in range(4):
        y -= 10
        radius -= 10
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(radius)


# call main function
main()
