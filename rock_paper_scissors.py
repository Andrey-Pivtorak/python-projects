# a task:  rock, paper, scissors game

import random

# global constants
ROCK = 1
PAPER = 2
SCISSORS = 3
MIN_VALUE = 1
MAX_VALUE = 3
COMPUTER_WINS = 1
USER_WINS = 2
EQUALLY = 0


# main function
def main():
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        result = EQUALLY
        while result == EQUALLY:
            computer = random.randint(MIN_VALUE, MAX_VALUE)
            player = int(input("--> Please, enter your choice: '1'-rock, '2'-paper, '3'-scissors "))
            print('\nResults:')
            print('The computer choose', showChoise(computer))
            print('You choose', showChoise(player))
            result = checkChoise(computer, player)
            if result == EQUALLY:
                print('-->> The computer and you made the same choice. Please, try again!')
        if result == COMPUTER_WINS:
            print('The computer wins!')
        elif result == USER_WINS:
            print('You win!')
        answer = input('Do you want to replay: Y/N? ')


# checkChoise function
def checkChoise(computer, player):
    if computer == player:
        return EQUALLY
    elif computer == ROCK and player == PAPER:
        return USER_WINS
    elif computer == ROCK and player == SCISSORS:
        return COMPUTER_WINS
    elif computer == PAPER and player == ROCK:
        return COMPUTER_WINS
    elif computer == PAPER and player == SCISSORS:
        return USER_WINS
    elif computer == SCISSORS and player == ROCK:
        return USER_WINS
    elif computer == SCISSORS and player == PAPER:
        return COMPUTER_WINS


# showChoise function
def showChoise(choice):
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    elif choice == 3:
        return 'scissors'
    else:
        return 'wrong value!'


# call main function
main()
