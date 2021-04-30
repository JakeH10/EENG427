# Author: Jacob Hoffer

from scipy import special
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def q01():
    theta = np.arange(-90, 90, 0.1)

    antenna_pattern = np.sinc(10 * np.sin(np.deg2rad(theta)))

    ret = np.array([antenna_pattern,
                    np.abs(antenna_pattern),
                    20 * np.log10(np.abs(antenna_pattern)),
                    np.abs(antenna_pattern)])

    ax1 = plt.subplot(111)

    ax1.set_title('Part A')
    ax1.set_xlabel('angle (Degrees)')
    ax1.set_ylabel(r'AP')
    ax1.grid()
    ax1.plot(theta, ret[0])

    plt.show()

    ax2 = plt.subplot(111)

    ax2.set_title('Part B')
    ax2.set_xlabel('angle (Degrees)')
    ax2.set_ylabel(r'|AP|')
    ax2.grid()
    ax2.plot(theta, ret[1])

    plt.show()

    ax3 = plt.subplot(111)

    ax3.set_title('Part C')
    ax3.set_xlabel('angle (Degrees)')
    ax3.set_ylabel(r'$20 \log|AP|$')
    ax3.grid()
    ax3.plot(theta, ret[2])

    plt.show()

    ax4 = plt.subplot(111, projection='polar')

    ax4.set_title('Part D')
    ax4.grid(True)
    ax4.plot(np.deg2rad(theta), ret[3])

    plt.show()

    return


def q14():

    N = np.arange(1, 20, 1)

    AR = (2*N + 1) / 2*N

    AR_dB = 10*np.log10(AR)

    plt.figure()

    plt.title('AR of an Axial Cable')
    plt.xlabel('N (turns)')
    plt.ylabel('AR (dB)')

    plt.plot(N, AR_dB, '-')

    plt.grid()

    plt.show()


def q17():
    f = 2.4e+9
    wavelength = 3e+8 / f

    e_r = np.arange(1, 10, 0.1)

    length = 0.49 * wavelength / np.sqrt(e_r)
    width = wavelength / np.sqrt(2 * (e_r + 1))

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Length and Width of Patch')

    ax1.set_title('Length')
    ax1.set_ylabel('Meters')
    ax1.set_xlabel('$\epsilon_r$')
    ax1.grid()

    ax2.set_title('Width')
    ax2.set_xlabel('$\epsilon_r$')
    ax2.grid()

    ax1.plot(e_r, length)
    ax2.plot(e_r, width)

    plt.show()


def q36():
    z_0 = 10e+3
    f = 7e+9
    a_p = 4


def q37():
    n = np.arange(1, 20, 1)

    g_exact = [np.sum(1/np.arange(1, e, 1)) for e in n]
    g_aprox = 0.5772 + np.log(n) + 0.5 / n

    ax1 = plt.subplot(111)
    ax1.set_title('Selection Diversity')
    ax1.set_ylabel(r'$G_{sd}$')
    ax1.set_xlabel('N')
    ax1.grid()

    ax1.plot(n, g_exact, '-')
    ax1.plot(n, g_aprox, '-')

    plt.legend(['Exact', 'Approx'])

    plt.show()


def main():

    q37()


if __name__ == '__main__':
    main()
