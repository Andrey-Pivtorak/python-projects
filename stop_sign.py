import turtle

# global variable
START_X = -100
START_Y = -240
LENGHT_LINE = 200
NUMB_LINE = 8
WRITE_X = -120
WRITE_Y = -60
ANGLE = 45
ANIMATION_SPEED = 0
FONT_SIZE = 70

# set parameters turtle
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

# write stop sign
turtle.begin_fill()
turtle.fillcolor('red')
for line in range(NUMB_LINE):
    turtle.pencolor('red')
    turtle.forward(LENGHT_LINE)
    turtle.left(ANGLE)
turtle.end_fill()

# write stop inscription
turtle.penup()
turtle.goto(WRITE_X, WRITE_Y)
turtle.pendown()
turtle.pencolor('white')
turtle.write('STOP', font=('Arial', FONT_SIZE, 'normal', 'bold'))

turtle.done()