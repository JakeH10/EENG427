#  Author: Jacob Hoffer
#  Purpose: EENG 427 - Homework 5
#  April 4, 2021

import numpy as np
import matplotlib.pyplot as plt


class Array:

    def uniform(self):
        self.theta = np.arange(-np.pi/2, np.pi/2, 0.001)
        n_l = np.arange(1, self.elements+1, 1)
        self.array_factor = np.sum([np.exp(1j * 2 * np.pi * (n - 1) * self.spacing * np.sin(self.theta)) for n in n_l], axis=0)
        # psi = 2 * np.pi * self.spacing * np.sin(self.theta)
        # num = 1 - np.exp(1j * self.elements * psi)
        # den = 1 - np.exp(1j * psi)
        # self.array_factor = num / den

    def __init__(self, n, d):
        self.elements = n
        self.spacing = d
        self.theta = []
        self.array_factor = []

        self.uniform()


def main():

    #  Question 4.19
    d_l = [0.5, 1.0, 2.0]
    n = 8
    array_list = [Array(n, d) for d in d_l]

    plt.figure()
    plt.grid()

    plt.title(r'Array Factor at different element spacings')
    plt.xlabel(r'$\theta$ (degrees)')
    plt.ylabel(r'|AP|')

    [plt.plot(np.rad2deg(array.theta), np.abs(array.array_factor)) for array in array_list]

    plt.legend([r'%3.1f $\lambda$' % d for d in d_l])

    # plt.show()

    #  Question 4.22

    #  Question 4.24
    array = Array(4, 0.5)

    plt.figure()
    plt.grid()

    plt.title(r'Array Factor at different element spacings')
    plt.xlabel(r'$\theta$ (degrees)')
    plt.ylabel(r'|AP|')

    plt.plot(np.rad2deg(array.theta), 10*np.log10(np.abs(array.array_factor)))

    plt.show()

    return


if __name__ == '__main__':
    main()
