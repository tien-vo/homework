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
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
fig.suptitle("$m(T,B)/n\mu$")

im = ax.pcolormesh(TT, BB, MM, cmap="jet")
fig.colorbar(im, ax=ax, fraction=0.05, pad=0.05)

ax.set_xlim(T[0], T[-1])
ax.set_ylim(B[0], B[-1])
ax.set_xlabel("$T/T_c$")
ax.set_ylabel("$\mu B/k_BT_c$")
ax.tick_params(**me.params)

fig.savefig("p2cii.png", dpi=600)
plt.show()
