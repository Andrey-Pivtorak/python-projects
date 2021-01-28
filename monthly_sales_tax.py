# global constants
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025


# main function
def main():
    totalSales = float(input('Please, enter the total sales for the month: '))
    countyTax = totalSales * COUNTY_TAX_RATE
    stateTax = totalSales * STATE_TAX_RATE
    showTotalTax(countyTax, stateTax)


# showTotalTax function
def showTotalTax(countyTax, stateTax):
    print('The amount of county sales tax', format(countyTax, '.2f'), '$')
    print('The amount of state sales tax', format(stateTax, '.2f'), '$')
    totalTax = countyTax + stateTax
    print('The total sales tax:', format(totalTax, '.2f'), '$')


# call main function
main()
