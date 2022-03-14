from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


k = np.logspace(-3, 5, 1000)
f = 2 * k * np.exp(1 / 4 / k)

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

ax.plot(k, f, "-k")
ax.axhline(f.min(), c="k", ls="--")
ax.fill_between(k, f, f.max(), color="red", alpha=0.2)
ax.text(5e-1, 1e3, "Trapped particle")

ax.set_xlim(1e-2, k[-1])
ax.set_ylim(1e-1, 1e4)
ax.set_xscale("log")
ax.set_yscale("log")
ax.tick_params(**me.params)
ax.set_xlabel("$E_0/k_BT$")
ax.set_ylabel(r"$\alpha/k_BT$")

fig.savefig("p1c_1.png", dpi=600)
plt.close(fig)


N = 11
T = np.logspace(-4, 4, N)
colors = plt.cm.jet(np.linspace(0, 1, N))
k = np.logspace(-3, 5, 1000)
f = 2 * k * np.exp(1 / 4 / k)

fig, ax = plt.subplots(1, 1)
for i in range(N):
    Fv = -0.5 + 2 * k * (np.exp(1 / 4 / k) - 1) - np.log(
        np.pi * np.sqrt(T[i] / k))
    ax.plot(k, Fv, c=colors[i], label=fr"$T/T_\ast={T[i]}$")

#ax.legend()
ax.plot(k, f, "-k")
ax.axhline(f.min(), c="k", ls="--")
ax.fill_between(k, f, f.max(), color="red", alpha=0.2)
ax.text(5e-1, 1e3, "Trapped particle")


ax.set_xlim(1e-2, k[-1])
ax.set_ylim(1e-1, 1e4)
ax.set_xscale("log")
ax.set_yscale("log")
ax.tick_params(**me.params)
ax.set_xlabel("$E_0/k_BT$")
ax.set_ylabel(r"$\alpha/k_BT$")
fig.savefig("p1c_2.png", dpi=600)


