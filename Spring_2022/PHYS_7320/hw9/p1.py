import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def x(y, b):
    return np.cosh(y / b) - 1

y = np.linspace(0, 2, 1000)
b = np.linspace(0, 1, 10)
colors = plt.cm.jet(np.linspace(0, 1, len(b)))


me.setup_mpl(tex=True, fontsize=18)
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
fig.subplots_adjust(right=0.8)

for i, _b in enumerate(b):
    ax.plot(y, x(y, b=_b), c=colors[i], label=fr"$\beta_0={_b:.1f}$")

fig.legend(frameon=False, handlelength=1, loc=7)
ax.set_xlim(y[0], y[-1])
#ax.set_yscale("log")
ax.set_ylim(0, 10)
ax.tick_params(**me.params)
ax.set_xlabel("$eE_0y/\gamma_0mc^2$")
ax.set_ylabel("$eE_0x/\gamma_0mc^2$")

fig.savefig("p1.png", dpi=600)
plt.show()
