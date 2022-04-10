import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


x = np.linspace(0, 10, 1000)
y = x / (1 - np.exp(-x))

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)
ax.plot(x, y, "-k")
ax.axhline(3, c="r")
ax.axvline(2.82, c="k", ls="--")
ax.text(3, 1, "$x=2.82$")
ax.text(0.5, 3.2, "$y=d$", c="r")
ax.set_xlim(x.min(), x.max())
ax.tick_params(**me.params)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
fig.savefig("p4.png", dpi=600)
plt.show()
