# a task: turtle graphics: city skyline

import turtle
import random

# global constants
ANIMATION_SPEED = 0
SCREEN_WEIDTH = 600
SCREEN_HEIGHT = SCREEN_WEIDTH
NUMB_STARS = 50
MIN_X = -(int(SCREEN_WEIDTH / 2))
MAX_X = int((SCREEN_WEIDTH / 2) - 1)
MIN_Y = -(int(SCREEN_HEIGHT / 2))
MAX_Y = int(SCREEN_HEIGHT / 2)
BUILDS_X1 = MIN_X
BUILDS_Y1 = -70
WINDOW_SIZE = 15
WINDOW_COLOR = 'khaki'
W_X1 = -210
W_Y1 = 0
W_X2 = -125
W_Y2 = 180
W_X3 = -125
W_Y3 = 155
W_X4 = -20
W_Y4 = 100
W_X5 = -50
W_Y5 = -90
W_X6 = 95
W_Y6 = 90
W_X7 = 200
W_Y7 = -15


# square function
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()


# screen_setup function
def screen_setup():
    turtle.setup(SCREEN_WEIDTH, SCREEN_HEIGHT)
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    turtle.bgcolor('black')


# drawStars function
def drawStars():
    for star in range(NUMB_STARS):
        x = random.randint(MIN_X, MAX_X)
        y = random.randint(MIN_Y, MAX_Y)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(3, 'yellow')


# draw_buildings function
def draw_buildings():
    turtle.pencolor('gray')
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(BUILDS_X1, BUILDS_Y1)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(170)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(55)
    turtle.right(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.goto(MAX_X, turtle.ycor())
    turtle.goto(MAX_X, MIN_Y)
    turtle.goto(MIN_X, MIN_Y)
    turtle.goto(BUILDS_X1, BUILDS_Y1)
    turtle.end_fill()


# draw_windows function
def draw_windows():
    square(W_X1, W_Y1, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X2, W_Y2, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X3, W_Y3, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X4, W_Y4, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X5, W_Y5, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X6, W_Y6, WINDOW_SIZE, WINDOW_COLOR)
    square(W_X7, W_Y7, WINDOW_SIZE, WINDOW_COLOR)


# main function
def main():
    screen_setup()
    drawStars()
    draw_buildings()
    draw_windows()
    turtle.done()


# call main function
main()
