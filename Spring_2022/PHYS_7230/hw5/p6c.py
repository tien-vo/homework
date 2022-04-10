import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np

T = np.logspace(-2, 2, 1000)
mu = T * np.log(np.exp(1 / T) - 1)


me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

ax.plot(T, mu, "-k")

ax.set_ylabel(r"$\mu/k_BT_\ast$")
ax.set_xlabel(r"$T/T_\ast$")
ax.set_xscale("log")
ax.set_ylim(-2, 2)
ax.set_xlim(T[0], T[-1])
ax.tick_params(which="both", **me.params)

fig.savefig("p6c.png", dpi=600)
plt.show()
