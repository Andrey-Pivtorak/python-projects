# a task:  turtle graphics: сheckerboard

import turtle

# global constants
ANIMATION_SPEED = 2
WIDTH_BOARD = 500
HEIGHT_BOARD = WIDTH_BOARD
NUM_SQUARES_IN_ROW = 5
NUM_SQUARES_IN_COL = 5
CELL_SIZE = int(WIDTH_BOARD / NUM_SQUARES_IN_ROW) = 100
BOARD_LEFT_EDGE_X = int(-(WIDTH_BOARD / 2)) = -250
BOARD_TOP_EDGE_Y = int(HEIGHT_BOARD / 2) = 250
FIRST_X = BOARD_LEFT_EDGE_X = -250
LAST_X = FIRST_X + (NUM_SQUARES_IN_ROW * CELL_SIZE) = 250
FIRST_Y = BOARD_TOP_EDGE_Y - CELL_SIZE = 150
LAST_Y = FIRST_Y - (NUM_SQUARES_IN_COL * CELL_SIZE) = -750


# main function
def main():
    turtle.setup(WIDTH_BOARD, HEIGHT_BOARD)
    turtle.speed(ANIMATION_SPEED)
    color = 'black'
    for y in range(FIRST_Y, LAST_Y, -CELL_SIZE):
        for x in range(FIRST_X, LAST_X, CELL_SIZE):
            square(x, y, CELL_SIZE, color)
            if color == 'black':
                color = 'white'
            else:
                color = 'black'
    turtle.done()


# square function
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()


# call main function
main()
