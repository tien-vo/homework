import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def coth(x):
    return np.cosh(x) / np.sinh(x)


def B(x, S):
    A = 1 / 2 / S
    return (1 + A) * coth((1 + A) * x) - A * coth(A * x)


S = 1/2
m = np.linspace(-0.5, 0.5, 1000)
T = [0.6, 1, 1.4]
#T = np.logspace(-1, 1, 3)
#lT = np.log10(T)
colors = plt.cm.jet(np.linspace(0, 1, len(T)))
ls = [":k", "--k", "-.k"]

me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1)

ax.plot(m, m, "-r")
for j, _ls in enumerate(ls):
    #lbl = f"$T/T_c=10^{{{lT[j]:.0f}}}$"
    lbl = f"$T/T_c={T[j]}$"
    ax.plot(m, S * B(3 / (S + 1) * m / T[j], S), _ls, label=lbl)


ax.legend(frameon=False)
ax.text(0.3, 0.1, "$SB_S(x)$")
#ax.set_xscale("log")
#ax.set_yscale("log")
ax.set_xlabel("$m/n\mu$")
ax.set_ylabel("$m/n\mu$")
ax.set_xlim(m[0], m[-1])
ax.set_ylim(m[0], m[-1])
ax.tick_params(which="both", **me.params)

fig.savefig("p2ci.png", dpi=600)
plt.show()
