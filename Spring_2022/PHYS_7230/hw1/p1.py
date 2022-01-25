from scipy.special import factorial
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


N = 100
E = np.arange(-N, N + 1)
Omega = factorial(N) / factorial((N-E)/2) / factorial((N+E)/2)

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(E, Omega, "-k")

ax.set_xlim(E[0], E[-1])
ax.tick_params(**me.params)
ax.set_xlabel("$E/h$")
ax.set_ylabel("$\Omega(E)$")

fig.savefig("p1b.png")

T = 2 / np.log((N - E) / (N + E))
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(E, T, "-k")

ax.set_xlim(E[0], E[-1])
ax.set_ylim(-100, 100)
ax.tick_params(**me.params)
ax.set_xlabel("$E/h$")
ax.set_ylabel("$k_BT/h$")

fig.savefig("p1c.png")


def m(B, T):
    return np.tanh(B / T)

N = 100000
Np = 7
B = np.logspace(-4, 8, N)
T = np.logspace(-4, 8, N)
n = np.arange(-4, 9, dtype=np.float64)
T_ = 10.0 ** n
B_ = 10.0 ** n
colors = plt.cm.jet(np.linspace(0, 1, len(T_)))

fig, axes = plt.subplots(2, 1, figsize=(8, 6), dpi=400)
fig.subplots_adjust(hspace=0.3, right=0.98)

for (j, t) in enumerate(T_):
    axes[0].plot(B, m(B, t), c=colors[j])

norm = plt.cm.colors.BoundaryNorm(n, plt.cm.jet.N)
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=norm)
cb = fig.colorbar(sm, ax=axes[0])
cb.ax.set_yticklabels([f"$10^{{{int(n_)}}}$" for n_ in n])
cb.set_label("$k_B T$ [eV]")

for (j, b) in enumerate(B_):
    axes[1].plot(T, m(b, T), c=colors[j])

axes[0].set_xlabel("$\mu_BB$ [eV]")
axes[1].set_xlabel("$k_BT$ [eV]")
for (j, ax) in enumerate(axes):
    ax.set_xscale("log")
    ax.set_xlim(B.min(), B.max())
    ax.tick_params(which="both", **me.params)
    ax.set_ylabel("$m/\mu_BN$")

cb = fig.colorbar(sm, ax=axes[1])
cb.ax.set_yticklabels([f"$10^{{{int(n_)}}}$" for n_ in n])
cb.set_label("$\mu_BB$ [eV]")

fig.savefig("p1d.png", dpi=fig.dpi)


T = np.linspace(0, 10, 1000)
C = (1 / T ** 2) * (1 / np.cosh(1 / T) ** 2)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(T, C, "-k")

ax.tick_params(**me.params)
ax.set_xlim(T[0], T[-1])
ax.set_xlabel(r"$T/T^\ast$")
ax.set_ylabel("$C_V/Nk_B$")

fig.savefig("p1f.png")
