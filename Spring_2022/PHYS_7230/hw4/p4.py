import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np

T = np.logspace(-3, 2, 1000)
x = 1 / np.sqrt(2 * np.tanh(1 / 2 / T))

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

ax.plot(T, x, "-k")
ax.set_xscale("log")
ax.set_xlim(T[0], T[-1])
ax.set_ylim(0, 4)
ax.set_xlabel(r"$T/T_\ast$")
ax.set_ylabel(r"$x_Q/x_0$")
ax.tick_params(**me.params)
ax.axhline(1 / np.sqrt(2), c="k", ls="--")
ax.text(1e1, 0.8, "$\sqrt2/2$")

fig.savefig("p4.png", dpi=600)
plt.show()
