import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def nf(eps, mu):
    return 1 / (1 + np.exp(eps - mu))


def dnf(eps, mu):
    return - np.exp(eps - mu) / (1 + np.exp(eps - mu)) ** 2


mu = np.logspace(-5, 2, 6)
eps = np.logspace(-3, 3, 100000)
cs = plt.cm.jet(np.linspace(0, 1, len(mu)))

me.setup_mpl(tex=True)

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 8))
fig.subplots_adjust(hspace=0.05)

for i, _mu in enumerate(mu):
    axes[0].plot(
        eps, nf(eps, _mu), label=f"$\mu/k_BT=10^{{{np.log10(_mu):.0f}}}$",
        color=cs[i],
    )
    axes[1].plot(eps, dnf(eps, _mu), color=cs[i])


fig.legend(frameon=False, loc=9, ncol=len(mu) // 2)
axes[0].set_ylabel("$n_F$")
axes[1].set_ylabel(r"$\partial n_F/\partial x$")
axes[1].set_xlabel("$\epsilon_k/k_BT$")
#axes[1].set_ylim(-1, 0.2)
for (i, ax) in enumerate(axes):
    ax.set_xscale("log")
    ax.set_xlim(eps[0], eps[-1])
    ax.tick_params(which="both", **me.params)

fig.savefig("p6.png", dpi=600)
plt.show()
