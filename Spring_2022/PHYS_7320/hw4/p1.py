import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def j1(x):
    return (np.sin(x) - x * np.cos(x)) / (x ** 2)


x = np.logspace(-4, 4, 10000)
y = j1(x) ** 2 / x ** 2

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

fig.suptitle("$j_1^2(qa)/(qa)^2$")
ax.plot(x, y, "-k")

ax.tick_params(**me.params)
ax.set_xscale("log")

ax.set_xlim(x.min(), x.max())
ax.set_xlabel("$qa$")

fig.savefig("p1.png")
