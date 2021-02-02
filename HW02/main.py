# Author Jacob Hoffer
# EENG427 HW02

import numpy as np

def main():

    # 2.12
    n_s = 100
    s_n = np.ones(n_s)
    u_s = 1
    p_s = (1/n_s) * np.sum(s_n - u_s)**2
    print(p_s)

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
