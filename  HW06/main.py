#  Author: Jacob Hoffer
#  Purpose: EENG427 Homework 6
#  Date: 4/14/21

import numpy as np
import matplotlib.pyplot as plt


class Signal:
    index_incident = 0
    index_transmit = 0
    theta_transmit = 0
    theta_incident = 0
    tm = 0
    te = 0

    def __init__(self, ni, nt):
        self.index_incident = ni
        self.index_transmit = nt

    def snells_law(self, find_transmit, theta):
        if find_transmit:
            self.theta_incident = theta
            self.theta_transmit = np.arcsin(self.index_incident * np.sin(theta) / self.index_transmit)
        else:
            self.theta_incident = np.arcsin(self.index_transmit * np.sin(theta) / self.index_incident)
            self.theta_transmit = theta

    def fresnel_reflection(self, using_theta_incident, theta):
        self.snells_law(using_theta_incident, theta)

        self.tm = (self.index_transmit * np.cos(self.theta_incident) -
                   self.index_incident * np.cos(self.theta_transmit)) / \
                  (self.index_transmit * np.cos(self.theta_incident) +
                   self.index_incident * np.cos(self.theta_transmit))

        self.te = (self.index_incident * np.cos(self.theta_incident) -
                   self.index_transmit * np.cos(self.theta_transmit)) / \
                  (self.index_incident * np.cos(self.theta_incident) +
                   self.index_transmit * np.cos(self.theta_transmit))


def main():

    #  Question 1
    print("Question 1")

    theta = np.arange(0, 90, 1)   # Increment by 0.1 degrees from 0 to 90
    theta = np.deg2rad(theta)   # Convert degrees to radians

    signal = Signal(1.5, 1.0)

    signal.fresnel_reflection(True, theta)

    return


if __name__ == '__main__':
    main()
