#  Author: Jacob Hoffer
#  Purpose: EENG427 HW01
#  Description: Assist in computations for HW01
#  Date: 01/20/2021

from q3 import q3
from q5 import q5
from q11 import q11
from q13 import q13


def main():

    #  Question 3
    h = q3()
    print('The entropy in question 3 is %.4f bits.\n\r' % h)

    #  Question 5
    h = q5()
    print('The entropy in question 5 is %.4f bits.\n\r' % h)

    #  Question 11
    h = q11()
    print('The entropy in question 11 is %.4f bits.\n\r' % h)

    #  Question 13
    q13()

    return


if __name__ == '__main__':
    main()
