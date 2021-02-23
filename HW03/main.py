# Author: Jacob Hoffer
# Purpose: EENG427 Homework 3
# Date: 2/22/21

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert
from scipy.io import wavfile
import math


def main():

    # Problem 3.5
    # https://stackoverflow.com/questions/37968221/similar-function-envelope-matlab-in-python

    v_c = 12
    v_m = 6
    f_c = 300000
    f_m = 20000
    t = np.arange(0, 100*10**-6, 1*10**-7)

    carrier = v_c * np.cos(2*np.pi*f_c*t)
    lower_sideband = (v_m / 2) * np.cos(2*np.pi*(f_c - f_m)*t)
    upper_sideband = (v_m / 2) * np.cos(2*np.pi*(f_c + f_m)*t)

    st = carrier + lower_sideband + upper_sideband
    temp = hilbert(st)
    envelope = np.abs(temp)

    plt.figure()
    plt.plot(t*10**6, st, label='s(t)')
    plt.plot(t*10**6, envelope, label='envelope')
    plt.xlabel('time ($\mu$s)')
    plt.ylabel('voltage (V)')
    plt.title('Signal Envelope')
    plt.legend()
    # plt.show()

    # Problem 3.7
    fs, data = wavfile.read('Recording.wav')
    signal = data / np.max(data)
    b_am_s = [0.33, 0.67, 1.0, 1.33]
    t = np.arange(0, np.size(signal) / fs, 1 / fs)
    carrier = np.cos(2*np.pi*300000*t)
    v_am_s = [1 + b_am * signal * carrier for b_am in b_am_s]
    plt.figure()
    for i in range(0, 4):
        plt.subplot(4, 1, i+1)
        plt.plot(t, v_am_s[i], label=r'$\beta_{AM} = $' + str(b_am_s[i]))
        plt.ylabel(r'$v_{AM}$')
        plt.legend()
    plt.xlabel('time (second)')
    plt.suptitle('Time domain signal')
    #plt.show()

    # Problem 3.14
    f_c = 300000
    f_m = fs
    b_fm_s = [0.67, 1.33, 2.67]
    plt.figure()
    for i in range(0, np.size(b_fm_s)):
        plt.subplot(3, 1, i+1)
        v_fm = np.cos(2*np.pi*f_c*t + b_fm_s[i] * np.sin(2*np.pi*f_m*t))
        plt.plot(t[30000:30500], v_fm[30000:30500], label='FM-modulated carrier')
        plt.plot(t[30000:30500], signal[30000:30500], label='voice signal')
        plt.ylabel(r'$v_{FM}$')
        plt.legend()
    plt.xlabel('time (second)')
    plt.suptitle('Time domain signal')
    #plt.show()

    # Problem 3.16

    # Problem 3.21
    ebno = np.arange(0, 15, 0.1)
    ber = [0.5 * math.erfc(math.sqrt(2*10**(val/10))) for val in ebno]
    plt.figure()
    plt.plot(ebno, ber)
    plt.minorticks_on()
    plt.yscale('log')
    plt.grid(True, which='major', linestyle='-')
    plt.grid(True, which='minor', linestyle='--')
    plt.xlabel(r'$E_b/N_0 (dB)$')
    plt.ylabel('BER')
    plt.title('QPSK')

    # Problem 3.23
    x = np.arange(0, 5, 0.01)
    plt.figure()
    plt.plot(x, x * np.exp(-2*x), label='ALOHA')
    plt.plot(x, x * np.exp(-x), label='Slotted ALOHA')
    plt.legend()
    plt.xlabel(r'Load, $\lambda_p \tau_p$')
    plt.ylabel(r'Throughput, $\gamma_p$')
    plt.title('Throughput of ALOHA and slotted ALOHA')
    plt.grid()
    plt.minorticks_on()
    plt.show()

    return


if __name__ == '__main__':
    main()
