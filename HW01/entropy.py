#  Author: Jacob Hoffer
#  Purpose: EENG427
#  Description: Find the entropy (average information)
#  Date: 01/20/2021

import numpy as np


def entropy(pn):

    h = sum([p * np.log2(1/p) for p in pn])

    return h
