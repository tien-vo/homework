import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


t = np.logspace(-4, 4, 1000)
u = t / np.sqrt(1 + t ** 2)

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

ax.plot(t, u, "-k")
ax.set_xscale("log")
ax.axhline(1, c="k", ls="--")
ax.set_xlim(t[0], t[-1])
ax.set_ylim(0, 1.1)
ax.tick_params(**me.params)
ax.set_xlabel("$at/c$")
ax.set_ylabel("$u/c$")

fig.savefig("p1a.png", dpi=300)

