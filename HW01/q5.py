#  Author: Jacob Hoffer
#  Purpose: EENG427 HW01 Question 1.5
#  Description: Calculate the entropy of the Scrabble.
#               See Table 1.1 in the textbook
#  Date: 01/20/2021

from entropy import entropy


def q5():

    char_freq_dict = {
        'k': 1,
        'j': 1,
        'x': 1,
        'q': 1,
        'z': 1,
        ' ': 2,
        'b': 2,
        'c': 2,
        'm': 2,
        'p': 2,
        'f': 2,
        'h': 2,
        'v': 2,
        'w': 2,
        'y': 2,
        'g': 3,
        'l': 4,
        's': 4,
        'u': 4,
        'd': 4,
        'n': 6,
        'r': 6,
        't': 6,
        'o': 8,
        'a': 9,
        'i': 9,
        'e': 12
    }

    total = sum(char_freq_dict.values())
    h = entropy([freq/total for freq in char_freq_dict.values()])

    return h
