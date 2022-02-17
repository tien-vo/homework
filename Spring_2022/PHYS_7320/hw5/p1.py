from scipy.special import fresnel
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


xi = np.linspace(-5, 20, 1000)
S, C = fresnel(xi)
I = 0.5 * ((C + 0.5) ** 2 + (S + 0.5) ** 2)

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1)

ax.plot(xi, I, "-k")
ax.axhline(1, c="k", ls="--")
ax.axhline(1/4, c="k", ls="--")
ax.axvline(0, c="k", ls="--")

ax.set_xlim(xi[0], xi[-1])
ax.set_ylim(0, 1.5)
ax.set_yticks(np.arange(0, 1.6, 0.25))
ax.set_xlabel(r"$\xi$")
ax.set_ylabel(r"$I/I_0$")

ax.tick_params(**me.params)

fig.savefig("p1b.png")
