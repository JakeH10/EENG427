#  Author: Jacob Hoffer
#  Purpose: EENG427 HW01 Question 1.11
#  Description: Find the average information (entropy) of five messages with given probabilities
#  Date: 01/20/2021

from entropy import entropy
import numpy as np


def q11():

    pn = np.array([1/2, 1/4, 1/8, 1/16, 1/16])

    h = entropy(pn)

    return h
