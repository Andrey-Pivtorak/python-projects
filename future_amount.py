# a task:  future amount on the account

# main function
def main():
    amountLoan = float(input('Please, enter the amount of the loan, $: '))
    monthlyRate = float(input('Please, enter the monthly interest rate, %: '))
    numberMonths = int(input('Please, enter the number of months: '))
    print('\nYour payment amount per month is',
          format(monthly_payment(amountLoan, monthlyRate, numberMonths), '.2f'), '$')


# monthly_payment function
def monthly_payment(amountLoan, monthlyRate, numberMonths):
    paymentAmount = ((monthlyRate / 100) * amountLoan) \
                    / (1 - (1 / (1 + (monthlyRate / 100)) ** numberMonths))
    return paymentAmount


# call main function
main()
