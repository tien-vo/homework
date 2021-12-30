import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np

x = np.linspace(-5, 5, 1000)
B = -np.tanh(x)
P = 1 / (np.cosh(x) ** 2)
J = 1 / (np.cosh(x) ** 2)


pt.mpl(tex=True)
fig, axes = plt.subplots(3, 1, figsize=(8, 6), sharex=True)

axes[0].plot(x, B, "-k")
axes[1].plot(x, P, "-k")
axes[2].plot(x, J, "-k")


axes[0].set_ylabel("$B$ $[B_0]$")
axes[1].set_ylabel("$P$ $[B_0^2/2\mu_0]$")
axes[2].set_ylabel("$J$ $[B_0/\mu_0L]$")
axes[2].set_xlabel("$x/L$")
for (j, ax) in enumerate(axes):
    ax.tick_params(**pt.params)
    ax.set_xlim(x[0], x[-1])

fig.savefig("p4.png")
