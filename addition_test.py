# a task:  addition test
import random

# global constants
MIN_VALUE_EXERCISE = 1
MAX_VALUE_EXERCISE = 5
MIN_NUMBER = 1
MAX_NUMBER = 99


# main function
def main():
    rightAnswer = 0
    wrongAnswer = 0
    print('You need to solve', MAX_VALUE_EXERCISE, 'exercises.')
    for exercise in range(MIN_VALUE_EXERCISE, MAX_VALUE_EXERCISE + 1):
        print('\nYour exercise №', exercise, sep='')
        number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        number2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        showExercise(number1, number2)
        userAnswer = getAnswer()
        correctAnswer = number1 + number2
        checkAnswer(userAnswer, correctAnswer)
        if userAnswer == correctAnswer:
            rightAnswer += 1
        else:
            wrongAnswer += 1
    print('\nTotal right answer=', rightAnswer)
    print('Total wrong answer=', wrongAnswer)
    print()
    showMark(rightAnswer)


# showExercise function
def showExercise(number1, number2):
    print(number1, '+', number2, '= ', )


# getAnswer function
def getAnswer():
    inputAnswer = int(input())
    return inputAnswer


# checkAnswer function
def checkAnswer(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        print('-->> Right!')
    else:
        print('-->> Wrong!')


# showMark function
def showMark(rightAnswer):
    if rightAnswer == MAX_VALUE_EXERCISE:
        print("Your mark's A.")
    elif rightAnswer == MAX_VALUE_EXERCISE - 1:
        print("Your mark's B.")
    elif rightAnswer == MAX_VALUE_EXERCISE - 2:
        print("Your mark's C.")
    else:
        print("Your mark's D. You should study better!!!")


# call main function
main()
