import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def Phi_c(x):
    return - 1 / x ** 3


def Phi_d(x):
    return 2 * (1 / np.sqrt(x ** 2 + 1) - 1 / x)


x = np.linspace(1, 5, 100000)


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(x, Phi_c(x), "-k")

ax.tick_params(**pt.params)
ax.set_xlim(x.min(), x.max())
ax.set_xlabel("$x/a$")
ax.set_ylabel("$\Phi(x,0,0)/V_0$")

fig.savefig("p2c.png")


fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
fig.subplots_adjust(hspace=0.05)
axes[0].plot(x, Phi_c(x), "-k", label="$\Phi_c$")
axes[0].plot(x, Phi_d(x), "--r", label="$\Phi_d$")
axes[0].set_ylabel("$\Phi(x,0,0)/V_0$")
axes[0].legend()

axes[1].plot(x, Phi_c(x) / Phi_d(x), "-k")
axes[1].set_xlabel("$x/a$")
axes[1].set_ylabel("$\Phi_c/\Phi_d$")
for (j, ax) in enumerate(axes):
    ax.tick_params(**pt.params)
    ax.set_xlim(x.min(), x.max())

fig.savefig("p2d.png")


