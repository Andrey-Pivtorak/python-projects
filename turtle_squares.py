import turtle

# global variable
START_X = 250
START_Y = -260
NUMB_SQUARES = 100
SIDES = 4
ANGLE = 90
LINE_LENGHT = 10
ANIMATION_SPEED = 0

# set parameters turtle
turtle.hideturtle()
turtle.penup()
turtle.speed(ANIMATION_SPEED)
turtle.pensize(3)
turtle.goto(START_X, START_Y)
turtle.pendown()
turtle.left(ANGLE)
turtle.pencolor('blue')
turtle.bgcolor('yellow')

# show squares
for square in range(NUMB_SQUARES):
    for side in range(SIDES):
        turtle.forward(LINE_LENGHT)
        turtle.left(ANGLE)
    LINE_LENGHT = LINE_LENGHT + 5

turtle.done()