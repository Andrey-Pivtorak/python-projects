# a task:  odd/even counter
import random

# global constants
MIN_VALUE = 1
MAX_VALUE = 100
AMOUNT_NUMBERS = 100


# main function
def main():
    count_even = 0
    count_odd = 0
    for count in range(1, AMOUNT_NUMBERS + 1):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=' ')
        keep_Eved_Odd(number)
        if keep_Eved_Odd(number):
            count_even += 1
        else:
            count_odd += 1
    print('\nEven numbers:', count_even, '. Odd numbers:', count_odd)


# keep_Eved_Odd function
def keep_Eved_Odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


# call main function
main()
