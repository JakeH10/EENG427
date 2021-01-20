#  Author: Jacob Hoffer
#  Purpose: EENG427 HW01 Question 1.13
#  Description: Plot impedance versus dependent variables in equation 1.3. Assume plastic
#  Date: 01/20/2021

import numpy as np
from matplotlib import pyplot as plt


def q13():

    m = 4*3.14*10**-7
    e = 2.2*8.854*10**-12

    x = np.linspace(1, 100, 10000)

    z = np.sqrt(m/e) / 3.14 * np.arccosh(x)

    plt.title("Impedance of a Twin Wire Transmission Line")
    plt.xlabel("s/$d_{ia}$")
    plt.ylabel("$Z_c$ (Ω)")
    plt.plot(x, z)
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#000000', linestyle='-')
    plt.grid(b=True, which='minor', color='#808080', linestyle='--')
    plt.show()

    return
