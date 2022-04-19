import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


T = np.logspace(-3, 3, 1000)


E = - np.tanh(1 / T)
Cv = (1 / T) ** 2 / np.cosh(1 / T) ** 2


me.setup_mpl(tex=True)
fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
fig.subplots_adjust(hspace=0.05)

axes[0].plot(T, E, "-k")
axes[1].plot(T, Cv, "-k")

axes[1].set_xlabel(r"$T/T_\ast$")
axes[0].set_ylabel(r"$E/Nk_BT_\ast$")
axes[1].set_ylabel(r"$C_V/Nk_B$")
for (j, ax) in enumerate(axes):
    ax.set_xscale("log")
    ax.set_xlim(T[0], T[-1])
    ax.tick_params(which="both", **me.params)

fig.savefig("p1.png", dpi=600)
plt.show()
