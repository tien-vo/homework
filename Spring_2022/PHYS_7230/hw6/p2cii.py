from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def coth(x):
    return np.cosh(x) / np.sinh(x)


def BS(x, S):
    A = 1 / 2 / S
    return (1 + A) * coth((1 + A) * x) - A * coth(A * x)


def f(B, T):
    fmin = lambda m: m - S * BS(S * B / T + 3 * m / (S + 1) / T, S)
    sol = root_scalar(fmin, x0=np.sign(B), bracket=[-10, 10], method="toms748")
    return sol.root


S = 1/2

B = np.linspace(-1, 1, 500)
T = np.linspace(0.5, 1.5, 500)

TT, BB = np.meshgrid(T, B, indexing="ij")

MM = np.zeros_like(TT)

for (i, j) in np.ndindex(MM.shape):
    MM[i, j] = f(BB[i, j], TT[i, j])

me.setup_mpl(tex=True)
fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
fig.subplots_adjust(hspace=0.05)

im = axes[0].pcolormesh(BB.T, TT.T, MM.T / S, cmap="jet", vmin=-1, vmax=1)
cax = me.add_cbar(axes[0])
cb = fig.colorbar(im, cax=cax)
cb.set_label("$m/n\mu S$")
axes[0].axhline(T[200], c="k", ls=":")
axes[0].axhline(T[300], c="k", ls="--")

axes[1].plot(B, MM[200, :] / S, ":k", label=f"$T/T_c={T[200]:.1f}$")
axes[1].plot(B, MM[300, :] / S, "--k", label=f"$T/T_c={T[300]:.1f}$")
axes[1].set_yticks([-1, 0, 1])
axes[1].legend(frameon=False)
me.add_cbar(axes[1]).remove()

axes[0].set_ylabel("$T/T_c$")
axes[1].set_ylabel("$m/n\mu S$")
axes[1].set_xlabel("$\mu B/k_BT_c$")
for (j, ax) in enumerate(axes):
    ax.set_xlim(B[0], B[-1])
    ax.tick_params(**me.params)

fig.savefig("p2cii.png", dpi=600)
plt.show()
