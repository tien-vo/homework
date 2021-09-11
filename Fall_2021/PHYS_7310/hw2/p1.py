import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def f(x, d=1):
    return - d * (x ** 2 + d ** 2) ** (-3/2) / 2 / np.pi


x = np.linspace(-4, 4, 1000)


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(x, f(x), "-k")

ax.set_xlabel("$x/d$")
ax.set_ylabel("$\sigma/q$")
ax.set_xlim(x.min(), x.max())
ax.tick_params(**pt.params)

fig.savefig("p1a.png")
