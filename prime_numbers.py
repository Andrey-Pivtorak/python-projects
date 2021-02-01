# a task:  prime numbers


# main function
def main():
    number = int(input('Please, enter the number: '))
    if is_prime(number):
        print('The number is prime!')
    else:
        print("The number isn't prime!")


# is_prime function
def is_prime(number):
    if number % 2 != 0 and number % 1 == 0:
        return True
    else:
        return False


# call main function
main()
