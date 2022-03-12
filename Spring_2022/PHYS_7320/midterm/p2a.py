from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def I(x, y, k=20):
    kz = 10 * k
    ax = k * x / np.sqrt(x ** 2 + y ** 2 + 1)
    ay = k * y / np.sqrt(x ** 2 + y ** 2 + 1)
    return (1 / np.pi ** 2) * (np.sin(ax) * np.sin(ay) / k ** 2 / x / y) ** 2 \
        * (k ** 2 / kz) ** 2


x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)

X, Y = np.meshgrid(x, y, indexing="ij")
Z = I(X, Y)
Zmax = Z.max()

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(7.2, 6))

im = ax.pcolormesh(X, Y, Z, cmap="binary_r", vmax=Zmax / 200)
cb = fig.colorbar(im, ax=ax, fraction=0.05, pad=0.01)
cb.set_label("$|\psi|^2/\psi_0^2$")

ax.set_xlabel("$x/z$")
ax.set_ylabel("$y/z$")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())
ax.tick_params(**me.params)
ax.set_aspect("equal")

fig.subplots_adjust(left=0, right=0.85)
fig.savefig("p2a.png", dpi=300)

