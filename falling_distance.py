# a task:  falling distance
# global constants
FREE_FALL = 9.8
TIME_MIN = 1
TIME_MAX = 10


# main function
def main():
    print('Time(sec.)\tDistance')
    print('--------------------')
    for second in range(TIME_MIN, TIME_MAX + 1):
        print(second, '\t\t\t', format(showDistance(second), '.2f'))


# showDistance function
def showDistance(second):
    d = 0.5 * FREE_FALL * (second ** 2)
    return d


# call main function
main()
