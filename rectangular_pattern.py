# a task:  turtle graphics: rectangular pattern

import turtle

# global constants
ANIMATION_SPEED = 0
START_X = 0
START_Y = 0


# main function
def main():
    turtle.hideturtle()
    turtle.speed(ANIMATION_SPEED)
    turtle.pensize(2)
    width = int(input('Please, enter the width of figure: '))
    height = int(input('Please, enter the height of figure: '))
    drawPattern(width, height)
    turtle.done()


# drawRectangle function
def drawRectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


# drawPattern function
def drawPattern(width, height):
    # outer rectangle
    drawRectangle(START_X, START_Y, width, height, 'red')

    # middle rectangle
    x_middle = START_X + width / 8
    y_middle = START_Y + height / 8
    width_middle = width - width / 4
    height_middle = height - height / 4
    drawRectangle(x_middle, y_middle, width_middle, height_middle, 'blue')

    # inner rectangle
    x_inner = START_X + width / 4
    y_inner = START_Y + height / 4
    width_inner = width - width / 2
    height_inner = height - height / 2
    drawRectangle(x_inner, y_inner, width_inner, height_inner, 'black')

    # diagonal 1_1
    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.pendown()
    turtle.goto(x_inner, y_inner)

    # diagonal 1_2
    turtle.penup()
    turtle.goto(x_inner + width_inner, y_inner + height_inner)
    turtle.pendown()
    turtle.goto(START_X + width, START_Y + height)

    # diagonal 2_1
    turtle.penup()
    turtle.goto(START_X + width, START_Y)
    turtle.pendown()
    turtle.goto(x_inner + width_inner, y_inner)

    # diagonal 2_2
    turtle.penup()
    turtle.goto(x_inner, y_inner + height_inner)
    turtle.pendown()
    turtle.goto(START_X, START_Y + height)

    # line 1_1
    turtle.penup()
    turtle.goto(START_X, START_Y + height / 2)
    turtle.pendown()
    turtle.goto(x_inner, y_inner + height_inner / 2)

    # line 1_2
    turtle.penup()
    turtle.goto(x_inner + width_inner, y_inner + height_inner / 2)
    turtle.pendown()
    turtle.goto(START_X + width, START_Y + height / 2)

    # line 2_1
    turtle.penup()
    turtle.goto(START_X + width / 2, START_Y)
    turtle.pendown()
    turtle.goto(x_inner + width_inner / 2, y_inner)

    # line 2_2
    turtle.penup()
    turtle.goto(x_inner + width_inner / 2, y_inner + height_inner)
    turtle.pendown()
    turtle.goto(START_X + width / 2, START_Y + height)


# call main function
main()
