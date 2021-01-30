# a task:  maximum of two values
# main function
def main():
    number1 = int(input('Please, input the first number: '))
    number2 = int(input('Please, input the second number: '))
    print('\nThe greater of the two is', maximum(number1, number2))


# maximum function
def maximum(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


# call main function
main()
