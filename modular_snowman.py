# a task:  turtle graphics: modular snowman

import turtle

# global constants
ANIMATION_SPEED = 0
PEN_SIZE = 3
BASE_X = 0
BASE_Y = -250
BASE_RADIUS = 100
MID_X = 0
MID_Y = -50
MID_RADIUS = 80

LEFT_ARM_X = -80
LEFT_ARM_Y = 30
LEFT_ARM_X1 = -130
LEFT_ARM_Y1 = 40
LEFT_ARM_X2 = -140
LEFT_ARM_Y2 = 80
LEFT_ARM_X3 = -140
LEFT_ARM_Y3 = 95
LEFT_ARM_X4 = -155
LEFT_ARM_Y4 = 82

RIGHT_ARM_X = 80
RIGHT_ARM_Y = 30
RIGHT_ARM_X1 = 140
RIGHT_ARM_Y1 = 60
RIGHT_ARM_X2 = 160
RIGHT_ARM_Y2 = 55
RIGHT_ARM_X3 = 150
RIGHT_ARM_Y3 = 80

HEAD_X = 0
HEAD_Y = 110
HEAD_RADIUS = 50

MOUTH_X = -25
MOUTH_Y = 145
MOUTH_X1 = 25
MOUTH_Y1 = 145

LEFT_EYE_X = -15
LEFT_EYE_Y = 160
LEFT_EYE_RADIUS = 5

RIGHT_EYE_X = 15
RIGHT_EYE_Y = 160
RIGHT_EYE_RADIUS = 5

HAT_X = -70
HAT_Y = 190
HAT_X1 = 70
HAT_Y1 = 190
HAT_X2 = 70
HAT_Y2 = 210
HAT_X3 = -70
HAT_Y3 = 210
HAT_X4 = -40
HAT_Y4 = 210
HAT_X5 = -40
HAT_Y5 = 260
HAT_X6 = 40
HAT_Y6 = 260
HAT_X7 = 40
HAT_Y7 = 210

BUTTONS_NUMB = 5
BUTTON_X = 0
BUTTON_Y = 70
BUTTON_RADIUS = 5


# main function
def main():
    turtle.hideturtle()
    turtle.speed(ANIMATION_SPEED)
    turtle.pensize(PEN_SIZE)
    turtle.bgcolor('lightblue')
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawButtons()
    turtle.done()


# drawBase function
def drawBase():
    turtle.penup()
    turtle.goto(BASE_X, BASE_Y)
    turtle.pendown()
    turtle.circle(BASE_RADIUS)


# drawMidSection function
def drawMidSection():
    turtle.penup()
    turtle.goto(MID_X, MID_Y)
    turtle.pendown()
    turtle.circle(MID_RADIUS)


# drawArms function
def drawArms():

    # left arm
    turtle.penup()
    turtle.goto(LEFT_ARM_X, LEFT_ARM_Y)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X1, LEFT_ARM_Y1)
    turtle.goto(LEFT_ARM_X2, LEFT_ARM_Y2)
    turtle.goto(LEFT_ARM_X3, LEFT_ARM_Y3)
    turtle.penup()
    turtle.goto(LEFT_ARM_X2, LEFT_ARM_Y2)
    turtle.pendown()
    turtle.goto(LEFT_ARM_X4, LEFT_ARM_Y4)

    # right arm
    turtle.penup()
    turtle.goto(RIGHT_ARM_X, RIGHT_ARM_Y)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X1, RIGHT_ARM_Y1)
    turtle.goto(RIGHT_ARM_X2, RIGHT_ARM_Y2)
    turtle.penup()
    turtle.goto(RIGHT_ARM_X1, RIGHT_ARM_Y1)
    turtle.pendown()
    turtle.goto(RIGHT_ARM_X3, RIGHT_ARM_Y3)


# drawHead function
def drawHead():
    turtle.penup()
    turtle.goto(HEAD_X, HEAD_Y)
    turtle.pendown()
    turtle.circle(HEAD_RADIUS)

    # mouth
    turtle.penup()
    turtle.goto(MOUTH_X, MOUTH_Y)
    turtle.pendown()
    turtle.goto(MOUTH_X1, MOUTH_Y1)

    # left eye
    turtle.penup()
    turtle.goto(LEFT_EYE_X, LEFT_EYE_Y)
    turtle.pendown()
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.circle(LEFT_EYE_RADIUS)
    turtle.end_fill()

    # right eye
    turtle.penup()
    turtle.goto(RIGHT_EYE_X, RIGHT_EYE_Y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(RIGHT_EYE_RADIUS)
    turtle.end_fill()

    # hat
    turtle.penup()
    turtle.goto(HAT_X, HAT_Y)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.goto(HAT_X1, HAT_Y1)
    turtle.goto(HAT_X2, HAT_Y2)
    turtle.goto(HAT_X3, HAT_Y3)
    turtle.goto(HAT_X, HAT_Y)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(HAT_X4, HAT_Y4)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(HAT_X5, HAT_Y5)
    turtle.goto(HAT_X6, HAT_Y6)
    turtle.goto(HAT_X7, HAT_Y7)
    turtle.end_fill()


# drawButtons function
def drawButtons():
    y = BUTTON_Y
    for button in range(BUTTONS_NUMB):
        turtle.penup()
        turtle.goto(BUTTON_X, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(BUTTON_RADIUS)
        turtle.end_fill()
        y -= 50


# call main function
main()

