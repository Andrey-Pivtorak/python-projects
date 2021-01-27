# a task: Stadium Seating
# global constants
CLASS_A_SEATS = 20
CLASS_B_SEATS = 15
CLASS_C_SEATS = 10


# main function
def main():
    print('How many tickets were sold?')
    countAtickets = int(input('Class A: '))
    countBtickets = int(input('Class B: '))
    countCtickets = int(input('Class C: '))
    incomeAtickets = countAtickets * CLASS_A_SEATS
    incomeBtickets = countBtickets * CLASS_B_SEATS
    incomeCtickets = countCtickets * CLASS_C_SEATS
    showIncome(incomeAtickets, incomeBtickets, incomeCtickets)


# showIncome function
def showIncome(incomeAtickets, incomeBtickets, incomeCtickets):
    print('\nReceived income for tickets:')
    print('Class A:', format(incomeAtickets, '.2f'), '$')
    print('Class B:', format(incomeBtickets, '.2f'), '$')
    print('Class C:', format(incomeCtickets, '.2f'), '$')
    totalIncome = incomeAtickets + incomeBtickets + incomeCtickets
    print('Total Income =', format(totalIncome, '.2f'), '$')


# call main function
main()
