# a task:  prime numbers list
# global constants
MIN_VALUE = 1
MAX_VALUE = 100


# main function
def main():
    print('Prime Number List:')
    print('------------------')
    for number in range(MIN_VALUE, MAX_VALUE + 1):
        if is_prime(number):
            print('\t', number)


# is_prime function
def is_prime(number):
    if number % 2 != 0 and number % 1 == 0:
        return True
    else:
        return False


# call main function
main()
