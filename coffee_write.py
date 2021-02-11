# This program adds coffee inventory records to
# the coffee.txt file.

# main function
def main():
    # Create a variable to control the loop
    another = 'y'
    coffee_file = open('coffee.txt', 'a')
    while another == 'y' or another == 'Y':
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = float(input('Quantity (in pounds): '))

        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')
        print()
        print('Do you want to add another record?')
        another = input('Y - yes, anything else = no: ')

    coffee_file.close()
    print('Data appended to coffee.txt')

# call the main function
main()
