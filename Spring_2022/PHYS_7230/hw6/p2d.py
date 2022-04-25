import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def f(m, B, T):
    A = 1 / 2 / S
    x = S * B / T + 3 * m / T / (S + 1)
    return 3 * m ** 2 / 2 / S / (S + 1) - \
        np.log(np.sinh((1 + A) * x) / np.sinh(A * x))


S = 1 / 2

B = [-1, 0, 1]
T = [0.5, 1, 1.5]
m = np.linspace(-2, 2, 1000)


me.setup_mpl(tex=True)
fig, axes = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
fig.subplots_adjust(hspace=0.1)


for (j, _B) in enumerate(B):
    if j == 0:
        l1 = f"$T/T_c={T[0]}$"
        l2 = f"$T/T_c={T[1]}$"
        l3 = f"$T/T_c={T[2]}$"
    else:
        l1 = None
        l2 = None
        l3 = None
    axes[j].text(-0.4, 0.5, f"$\mu B/k_BT_c={_B}$")
    axes[j].plot(m, f(m, _B, T[0]), "-k", label=l1)
    axes[j].plot(m, f(m, _B, T[1]), "--k", label=l2)
    axes[j].plot(m, f(m, _B, T[2]), "-.k", label=l3)

fig.legend(loc=9, ncol=3, frameon=False)
axes[1].set_ylabel("$f/nk_BT_c$")
axes[2].set_xlabel("$m/n\mu$")
for (j, ax) in enumerate(axes):
    ax.set_xlim(m[0], m[-1])
    ax.set_ylim(-3, 1)
    ax.tick_params(**me.params)

fig.savefig("p2d.png", dpi=600)
plt.show()

