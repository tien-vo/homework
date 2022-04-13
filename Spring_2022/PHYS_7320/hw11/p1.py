import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


Theta = np.linspace(0, np.pi, 1000)
dPa = np.sin(Theta) ** 2
dPb = (1 - 0.5 * np.sin(Theta) ** 2)


me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)
ax.plot(Theta / np.pi, dPa, "-k")

ax.tick_params(**me.params)
ax.set_xlabel("$\Theta$")
ax.set_ylabel("$dP/d\Omega$ [$\omega_0^4e^2d^2/8\pi c^3$]")
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xticklabels(["", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_xlim(0, 1)

fig.savefig("p1a.png", dpi=600)

plt.close(fig)
#plt.show()

fig, ax = plt.subplots(1, 1)
ax.plot(Theta / np.pi, dPb, "-k")

ax.tick_params(**me.params)
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$dP/d\Omega$ [$\omega_0^4e^2R^2/4\pi c^3$]")
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xticklabels(["", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_xlim(0, 1)

fig.savefig("p1b.png", dpi=600)

plt.show()


