import matplotlib.pyplot as plt
import numpy as np


R = 0.5
beta = 0.001


def phi_1(r):
    y = 2 / (1 - R) * (1 / r - (1 + R) / 2)

    return - np.arcsin(y)


def phi_2(r):

    y = 2 / (1 - R) * (1 / r - (1 + R) / 2)
    dphi = - beta * (-np.arcsin(y) + 2 / (1 - R) ** 2 * (
        np.sqrt((1 + y) / (1 - y)) - 1 / R ** 2 * np.sqrt((1 - y) / (1 + y))
    ))

    return phi_1(r) + dphi


r = np.linspace(0, 4, 1000)
fig, ax = plt.subplots(1, 1)

phi1 = phi_1(r)
x1 = r * np.cos(phi1)
y1 = r * np.sin(phi1)

phi2 = phi_2(r)
x2 = r * np.cos(phi2)
y2 = r * np.sin(phi2)


ax.plot(x1, y1, "-k")
ax.plot(x2, y2, "-r")

ax.set_aspect("equal")

plt.show()

