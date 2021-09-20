import matplotlib.pyplot as plt
import numpy as np


a = 1
b = 3


def s(theta, a=1, b=3):

    return (a ** 2 + b ** 2 - 2 * a * b * np.cos(theta)) ** (-3 / 2) \
        - (a ** 2 + b ** 2 + 2 * a * b * np.cos(theta)) ** (- 3 / 2)



theta = np.linspace(-np.pi / 2, np.pi / 2)


plt.plot(theta, s(theta), "-k")

plt.show()
