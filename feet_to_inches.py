# a task: feet to inches
# global constants
INCHES_TO_FEET = 12


# main function
def main():
    feet = float(input('Please, enter the number of feet: '))
    print('\n', feet_to_inches(feet), 'inches are in', feet, 'feet!')


# feet_to_inches function
def feet_to_inches(feet):
    return feet * INCHES_TO_FEET


# call main function
main()
