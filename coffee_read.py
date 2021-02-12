# This program displays the records in the
# coffee.txt file.


def main():
    coffee_file = open('coffee.txt', 'r')
    descr = coffee_file.readline()
    while descr != '':
        qty = float(coffee_file.readline())
        descr = descr.rstrip('\n')
        print('Description: ', descr)
        print('Quantity: ', qty)
        print()
        descr = coffee_file.readline()

    coffee_file.close()


main()
