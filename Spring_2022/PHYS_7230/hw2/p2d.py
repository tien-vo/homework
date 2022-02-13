import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def coth(x):
    return np.cosh(x) / np.sinh(x)


s = 100

T = np.logspace(-2, 3, 10000)

Cv = (1 / 4) * (1 / T) ** 2 * (
    (1 / np.sinh(1 / 2 / T) ** 2)
    -((2 * s + 1) / np.sinh((2 * s + 1) / 2 / T)) ** 2
)

m = (1 / 2) * (2 * s + 1) * coth((2 * s + 1) / 2 / T) - coth(1 / 2 / T)


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, dpi=300)

ax.plot(T, Cv, "-r", label="$C_v/Nk_B$")
ax.plot(T, m, "-b", label="$mV/N\mu$")
ax.legend(frameon=False, loc=8, bbox_to_anchor=(0.5, 0.2))
ax.axvline(1, ls="--", c="k")
ax.text(1.3, 3e-4, r"$T_1^\ast$")
ax.axvline(s, ls="--", c="k")
ax.text(1.3 * s, 3e-4, r"$T_2^\ast$")
ax.axhline(1, ls="--", c="k")
ax.text(1e-1, 2, "1")
ax.axhline(s, ls="--", c="k")
ax.text(1e-1, 2 * s, "$s$")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_ylim(1e-4, 1e3)
ax.set_xlim(5 * T[0], T[-1])
ax.tick_params(which="both", **me.params)
ax.set_yticklabels([0])
ax.set_xlabel(r"$T/T_1^\ast$")

fig.savefig("p2d.png", dpi=fig.dpi)

