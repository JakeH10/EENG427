import numpy as np
import scipy
import matplotlib.pyplot as plt

def antenna_pattern_plot():

    theta = np.arange(-90, 90, 0.1)

    antenna_pattern = np.sinc(10 * np.sin(np.deg2rad(theta)))

    ret = np.array([[antenna_pattern],
                    [np.abs(antenna_pattern)],
                    [20*np.log10(np.abs(antenna_pattern))],
                    [np.abs(antenna_pattern)]])

    ax1 = plt.subplot(221)
    ax2 = plt.subplot(222)
    ax3 = plt.subplot(223)
    ax4 = plt.subplot(224, projection='polar')

    ax1.set_title('Part A')
    ax1.set_xlabel('angle (Degrees)')
    ax1.set_ylabel(r'AP')
    ax1.grid()
    ax1.plot(theta, antenna_pattern)

    ax2.set_title('Part B')
    ax2.set_xlabel('angle (Degrees)')
    ax1.set_ylabel(r'AP')
    ax1.grid()
    ax1.plot(theta, antenna_pattern)

    ax3.set_title('Part C')
    ax1.set_xlabel('angle (Degrees)')
    ax1.set_ylabel(r'AP')
    ax1.grid()
    ax1.plot(theta, antenna_pattern)

    ax4.set_title('Part D')
    ax1.set_xlabel('angle (Degrees)')
    ax1.set_ylabel(r'AP')
    ax1.grid()
    ax1.plot(theta, antenna_pattern)
    plt.show()

    return


def main():

    antenna_pattern_plot()

    return


if __name__ == '__main__':
    main()
