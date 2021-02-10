## writing the numbers 1 through 10 to a file

# main function
def main():
    numb_file = open('numbers_file.txt', 'w')
    for count in range(1, 10 + 1):
        numb_file.write(str(count) + ' ')
    numb_file.close()
    print('Number 1 - 10 written to numbers_file.txt')


# call the main function
main()
