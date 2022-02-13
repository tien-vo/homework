import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


v = np.linspace(-4, 4, 1000)
f = np.exp(-v ** 2)

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, dpi=300)

fig.suptitle(r"$f_{1D}(v)$ [$\sqrt{m/2\pi k_BT}$]")

ax.plot(v, f, "-k")

ax.set_xlabel(r"$v/v^\ast$")
ax.set_xlim(v[0], v[-1])
ax.tick_params(**me.params)

fig.savefig("p5a.png", dpi=fig.dpi)

