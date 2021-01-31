# a task: test average and grade

# main function
def main():
    print('Please, etner test scores:')
    score1 = float(input('Score 1 - '))
    score2 = float(input('Score 2 - '))
    score3 = float(input('Score 3 - '))
    score4 = float(input('Score 4 - '))
    score5 = float(input('Score 5 - '))
    average = calc_average(score1, score2, score3, score4, score5)
    print('\nScores\t\tLetter Grade')
    print('-------------------------')
    print(score1, '\t\t\t', determine_grade(score1))
    print(score2, '\t\t\t', determine_grade(score2))
    print(score3, '\t\t\t', determine_grade(score3))
    print(score4, '\t\t\t', determine_grade(score4))
    print(score5, '\t\t\t', determine_grade(score5))
    print('--------------------')
    print('Average =', average, '(', determine_grade(average), ')')


# determine_grade function
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


# calc_average function
def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5


# call main function
main()
