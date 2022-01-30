import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np

def dP(theta):
    u = np.cos(theta)
    return (np.sin(np.pi * u) ** 2) / (1 - u ** 2) / 8 / np.pi ** 2


def dP_p3(theta):
    return (np.sin(theta) * np.cos(theta)) ** 2 / 32


theta = np.linspace(0, np.pi, 1000)


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(theta / np.pi, dP(theta), "-k")
ax.plot(theta / np.pi, dP_p3(theta), "--r")

ax.tick_params(**me.params)
ax.set_xlabel(r"$\theta$")
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xticklabels(["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_ylabel("$dP/d\Omega$ [$Z_0I_0^2$]")
ax.set_xlim(0, 1)

fig.savefig("p2.png")

