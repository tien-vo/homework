import matplotlib.pyplot as plt
import numpy as np


def y(x, a, b):
    return 0.5 * a * x ** 2 + 0.25 * b * x ** 4


x = np.linspace(0.1, 2, 1000)

num = np.sqrt(x - 1)
den = np.sqrt(x ** 3)

fig, ax = plt.subplots(1, 1)

ax.plot(x, num, "-k")
ax.plot(x, den, "-r")

plt.show()
