import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def s1(rho):
    return 1 - 1 / (rho ** 2)


def s2(phi):
    return 2 * np.sin(phi)


rho = np.linspace(-3, 3, 1000)
phi = np.linspace(0, np.pi, 1000)


pt.mpl(tex=True)
fig, axes = plt.subplots(2, 1, figsize=(8, 8))


axes[0].plot(phi / np.pi, s2(phi), "-k")
axes[1].plot(rho, s1(rho), "-k")

axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 2.1)
axes[0].set_xticks([0, 0.5, 1])
axes[0].set_xticklabels(["0", "$\pi/2$", "$\pi$"])
axes[0].set_xlabel("$\phi$")
axes[0].text(0.5, 0.6, "On the half-cylinder", transform=axes[0].transAxes,
             ha="center")

axes[1].set_xlim(rho[0], rho[-1])
axes[1].set_ylim(0, 1)
axes[1].set_xlabel(r"$\rho/a$")
axes[1].text(0.5, 0.6, "Near the half-cylinder", transform=axes[1].transAxes,
             ha="center")
axes[1].axvspan(-1, 1, color="red", alpha=0.4)

for (j, ax) in enumerate(axes):
    ax.set_ylabel("$\sigma/\sigma_0$")
    ax.tick_params(**pt.params)

fig.savefig("p2.png")
