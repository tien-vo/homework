from scipy.special import factorial
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np
import warnings


warnings.filterwarnings("ignore")


# Create figure
me.setup_mpl(tex=True, fontsize=18)
fig, axes = plt.subplots(5, 1, figsize=(12, 14))
fig.subplots_adjust(hspace=0.3, top=0.97, bottom=0.05)


# Part b
N = 100
E = np.arange(-N, N + 1)
Omega = factorial(N) / factorial((N - E) / 2) / factorial((N + E) / 2)
axes[0].plot(E, Omega, "-k")
axes[0].set_xlim(E[0], E[-1])
axes[0].set_xlabel("$E/\mu_BB$")
axes[0].set_ylabel("(a) $\Omega$")
me.add_cbar(axes[0], size="2%").remove()

# Part c
T = 2 / np.log((N - E) / (N + E))
axes[1].plot(E, T, "-k")
axes[1].set_xlim(E[0], E[-1])
axes[1].set_ylim(-100, 100)
axes[1].set_xlabel("$E/\mu_BB$")
axes[1].set_ylabel("(b) $k_BT/\mu_BB$")
me.add_cbar(axes[1], size="2%").remove()

# Part d
def m(B, T): return np.tanh(B / T)

N = 100000
Np = 7
B = np.logspace(-4, 8, N)
T = np.logspace(-4, 8, N)
ii = np.arange(-4, 9, dtype=np.float64)
T_ = 10. ** ii
B_ = 10. ** ii
colors = plt.cm.jet(np.linspace(0, 1, len(T_)))

for (j, t) in enumerate(T_): axes[2].plot(B, m(B, t), c=colors[j])
norm = plt.cm.colors.BoundaryNorm(ii, plt.cm.jet.N)
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=norm)
cax = me.add_cbar(axes[2], size="2%")
cb = fig.colorbar(sm, cax=cax)
cb.ax.set_yticklabels([f"$10^{{{int(i_)}}}$" for i_ in ii])
cb.set_label("$k_B T$ [eV]")
axes[2].set_xlabel("$\mu_BB$ [eV]")
axes[2].set_ylabel("(c) $m/\mu_BN$")
axes[2].set_xscale("log")
axes[2].set_xlim(B.min(), B.max())
me.add_cbar(axes[2], size="2%").remove()

for (j, b) in enumerate(B_): axes[3].plot(T, m(b, T), c=colors[j])
cax = me.add_cbar(axes[3], size="2%")
cb = fig.colorbar(sm, cax=cax)
cb.ax.set_yticklabels([f"$10^{{{int(i_)}}}$" for i_ in ii])
cb.set_label("$\mu_BB$ [eV]")
axes[3].set_xlabel("$k_BT$ [eV]")
axes[3].set_ylabel("(d) $m/\mu_BN$")
axes[3].set_xscale("log")
axes[3].set_xlim(B.min(), B.max())
me.add_cbar(axes[3], size="2%").remove()

# Part f
T = np.linspace(0, 10, 1000)
C = (1 / T ** 2) * (1 / np.cosh(1 / T) ** 2)

axes[4].plot(T, C, "-k")
axes[4].set_xlim(T[0], T[-1])
axes[4].set_xlabel(r"$T/T^\ast$")
axes[4].set_ylabel("(e) $C_V/Nk_B$")
me.add_cbar(axes[4], size="2%").remove()

for ax in axes: ax.tick_params(which="both", **me.params)

fig.align_ylabels(axes)

fig.savefig("p2.png")
