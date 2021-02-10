# This program gets employee data from the user and
# saves it as records in the employees.txt file.

# main function
def main():
    num_emps = int(input('How many employees records' 
                         + 'do you want to create? '))
    emp_file = open('employees.txt', 'w')
    for count in range(1, num_emps + 1):
        print('Enter data for employee №', count, sep='')
        name = input('Name: ')

        id_num = input('ID number: ')
        dept = input('Departament: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()

    emp_file.close()
    print('Employees records written to employees.txt')

# call the main function
main()
