import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


N = 1
alpha = 1
k0 = alpha
Nx = 1000
x = np.linspace(-5, 5, Nx)
k = np.linspace(-3, 3, Nx)

u2 = N * np.exp(-alpha * abs(x))
A2 = 8 / np.pi * 1 / (4 * (k - k0) ** 2 + 1) ** 2

pt.mpl(tex=True)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(hspace=0.1)

axes[0].plot(x, u2, "-k")
axes[1].plot(k, A2, "-k")

axes[0].set_xlim(x[0], x[-1])
axes[0].set_xlabel("$x$")
axes[0].set_ylabel("$|u|^2$")
axes[1].set_xlim(k[0], k[-1])
axes[1].set_xlabel("$k$")
axes[1].set_ylabel("$|A|^2$")
for (j, ax) in enumerate(axes):
    ax.tick_params(**pt.params)

fig.savefig("p1.png")
