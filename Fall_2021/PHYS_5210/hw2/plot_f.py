from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def f(x, theta):
    y = x + 1 + np.cos(theta)
    return -2 * (1 + x) + 2 * (1 - np.cos(theta)) * np.cos(theta) / y \
        + np.sin(theta) ** 2 * (x + 2) / y ** 2


def g(x, theta):

    P = np.sin(theta)
    return ((x + 2 * (x + 1) * P - (3 * x + 4) * P ** 2 + 2 * P ** 3) \
        / (x + 1 - P) ** 2) - 2 * (x + 1)


#x = np.linspace(0, 1.5, 1000)
x = np.linspace(0, 0.1, 1000)
theta = np.linspace(0, 2 * np.pi, 1000)
#x = np.linspace(0, 10, 1000)
#theta = np.linspace(-np.pi / 2, np.pi / 2, 1000)

X, THETA = np.meshgrid(x, theta, indexing="ij")


pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
fig.suptitle(r"$\lambda(\xi,\theta)$")

G = g(X, THETA)

im = ax.imshow(
    f(X, THETA), origin="lower", aspect="auto", cmap="jet",
    extent=[theta[0] / np.pi, theta[-1] / np.pi, x[0], x[-1]],
    norm=LogNorm(1e-5, 1e-0)
)
ax.axhline(1 / 13, c="k")
#ax.axvline(np.radians(113) / np.pi, c="k")

fig.colorbar(im, ax=ax, fraction=0.05, pad=0.05)

ax.text(0.05 * np.pi, 0.08, "$m/M=1/13$")
ax.set_xticks([0, 0.5, 1, 1.5, 2])
ax.set_xticklabels(["0", "$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$\xi=m/M$")
ax.tick_params(**pt.params)


#plt.show()
fig.savefig("fig.png")
