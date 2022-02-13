import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def L(x):
    return np.cosh(x) / np.sinh(x) - 1 / x


T = np.logspace(-3, 3, 10000)
Cv = (1 / T) ** 2 * (T ** 2 - 1 / np.sinh(1 / T) ** 2)
m = L(1 / T)


me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1, dpi=300)


ax.plot(T, Cv, "-r", label="$C_v/Nk_B$")
ax.plot(T, m, "-b", label="$mV/N\mu$")

ax.legend(frameon=False)
ax.tick_params(**me.params)
ax.set_xlabel(r"$T/T^\ast$")
ax.set_xscale("log")
ax.set_xlim(T[0], T[-1])

fig.savefig("p2avii.png", dpi=fig.dpi)
