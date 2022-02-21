from scipy.special import erf
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def C3(x):
    return - 0.5 * np.sqrt(x) * np.exp(-x)


def C1(x):
    return -2 * C3(x) + np.sqrt(np.pi / 2) * (1 + x) * (1 + erf(np.sqrt(x / 2)))


def C2(x):
    return (
        -2 * C3(x) + x * np.sqrt(np.pi / 2) * (1 + erf(np.sqrt(x / 2)))) ** 2


def Cv(x):
    return 9 / 2 + (C1(x) * C3(x) - C2(x)) / (C1(x) ** 2)


T = np.logspace(-5, 5, 1000)

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6), dpi=300)

ax.plot(T, 2 * Cv(1 / T), "-k")
ax.axhline(7, c="k", ls="--")
ax.axhline(9, c="k", ls="--")
ax.axvline(1, c="k", ls="--")

ax.set_xscale("log")
ax.set_xlim(T[0], T[-1])

ax.tick_params(**me.params)
ax.set_xlabel(r"$T/T_\ast$")
ax.set_ylabel(r"$n_{dof}=2c_v/k_B$")
fig.savefig("p3a.png", dpi=fig.dpi)
