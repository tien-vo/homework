from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def A(theta):
    return (1 - np.cos(theta)) / np.sin(theta)


theta = np.linspace(0, np.pi, 1000)
Ap = (1 - np.cos(theta)) / np.sin(theta)
Am = (-1 - np.cos(theta)) / np.sin(theta)

pt.mpl(tex=True)


fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(theta / np.pi, Ap, "-k", label="$(r/g)A$")
ax.plot(theta / np.pi, Am, "--k", label="$(r/g)A'$")


ax.set_xlim(0, 1)
ax.set_ylim(-10, 10)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
ax.set_xlabel(r"$\theta$")
#ax.set_ylabel(r"$(r/g)A$")
ax.legend()
ax.tick_params(**pt.params)
fig.savefig("p1.png")
