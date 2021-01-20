#  Author: Jacob Hoffer
#  Purpose: EENG427 HW01 Question 1.3
#  Description: Calculate the entropy of the English alphabet using Figure 1.6.
#               (Figure 1.6 in the class book has a typo; Instead, I used the equivalent
#               Figure in the lecture slides)
#  Date: 01/20/2021

from entropy import entropy


def q3():

    char_freq_dict = {
        'a': 0.08167,
        'b': 0.01492,
        'c': 0.02782,
        'd': 0.04253,
        'e': 0.12702,
        'f': 0.02228,
        'g': 0.02015,
        'h': 0.06094,
        'i': 0.06966,
        'j': 0.00153,
        'k': 0.00772,
        'l': 0.04025,
        'm': 0.02406,
        'n': 0.06749,
        'o': 0.07507,
        'p': 0.01929,
        'q': 0.00095,
        'r': 0.05987,
        's': 0.06327,
        't': 0.09056,
        'u': 0.02758,
        'v': 0.00978,
        'w': 0.02360,
        'x': 0.00150,
        'y': 0.01974,
        'z': 0.00074
    }

    h = entropy(char_freq_dict.values())

    return h
