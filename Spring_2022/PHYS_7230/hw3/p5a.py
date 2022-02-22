import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def N(T, mu):
    return 1 / (1 + np.exp(-(mu + 1) / T))


t = np.linspace(0, 10, 400)
m = np.linspace(-5, 5, 400)

T, M = np.meshgrid(t, m)
NN = N(T, M)


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1)
fig.suptitle("$N/N_0$")

cs = ax.contour(T, M, NN, colors="k", levels=np.arange(0.1, 1, 0.1))
ax.clabel(cs, inline=1, fontsize=12)

ax.set_yticks(np.arange(-5, 6, 1))
ax.set_xlim(0, 10)
ax.set_xlabel("$k_BT/\epsilon_0$")
ax.set_ylabel("$\mu/\epsilon_0$")
ax.tick_params(**me.params)

fig.savefig("p5a.png", dpi=300)

