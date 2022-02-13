import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


T = np.linspace(0, 4, 10000)

Cv = (1 / 2 / T / np.sinh(1 / 2 / T)) ** 2

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, dpi=300)

ax.plot(T, Cv, "-k", label="")
ax.axvline(1, ls="--", c="k")
ax.axhline(1, ls="--", c="k")

#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlim(T[0], T[-1])
ax.tick_params(which="both", **me.params)
ax.set_xlabel(r"$T/T^\ast$")
ax.set_ylabel(r"$C_v/3Nk_B$")

fig.savefig("p4c.png", dpi=fig.dpi)

