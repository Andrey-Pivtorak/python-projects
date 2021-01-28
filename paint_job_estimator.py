# a task: paint job estimator
import math

# global constants
FEET_PER_GALLON = 112
LABOR_HOURS = 8
LABOR_CHARGES = 35


# main function
def main():
    countSquareFeet = float(input('Enter the square feet of wall space to be painted: '))
    priceGallon = float(input('What is the price per gallon: '))
    totalGallonsPaint = countSquareFeet / FEET_PER_GALLON
    totalHoursLabor = totalGallonsPaint * LABOR_HOURS
    totalPaintCost = totalGallonsPaint * priceGallon
    totalLaborCharges = totalHoursLabor * LABOR_CHARGES
    showCostEstimate(totalGallonsPaint, totalHoursLabor, totalPaintCost, totalLaborCharges)


# showCostEstimate function
def showCostEstimate(totalGallonsPaint, totalHoursLabor, totalPaintCost, totalLaborCharges):
    print('\nThe number of gallons of paint required:', math.ceil(totalGallonsPaint))
    print('The hours of labor required:', math.ceil(totalHoursLabor))
    print('The cost of the paint:', format(totalPaintCost, '.2f'), '$')
    print('The labor charges:', format(totalLaborCharges, '.2f'), '$')
    totalCost = totalPaintCost + totalLaborCharges
    print('The total cost of the paint job:', format(totalCost, '.2f'), '$')


# call main function
main()
