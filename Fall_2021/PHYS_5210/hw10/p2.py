import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


phi = np.linspace(0, 2 * np.pi, 1000)

x = 2 * phi + np.sin(2 * phi)
y = 1 - np.cos(2 * phi)

cond = np.abs(phi) <= np.pi / 2


fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(x, y, "-k")
ax.plot(x[cond], y[cond], "-r")

fig.savefig("p2.png")
