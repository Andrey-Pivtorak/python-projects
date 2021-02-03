# a task:  random number guessing game

import random

# global constants
MIN_VALUE = 1
MAX_VALUE = 10


# main function
def main():
    number = random.randint(MIN_VALUE, MAX_VALUE)
    user_guess(number)
    print('Thank you for game!')


# user_guess function
def user_guess(number):
    userNumber = int(input('Please, enter your number: '))
    attemptСounter = 1
    while userNumber != number:
        if userNumber > number:
            print('Too high, try again!')
            userNumber = int(input('Please, enter your number: '))
            attemptСounter += 1
        elif userNumber < number:
            print('Too low, try again!')
            userNumber = int(input('Please, enter your number: '))
            attemptСounter += 1
    print('\nCongratulations. You guessed the number!')
    print('You made', attemptСounter, 'attempts!')


# call main function
main()
