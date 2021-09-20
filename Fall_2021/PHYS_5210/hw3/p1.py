import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def r(xM, Mm):
    return np.sqrt(1 - (1 + Mm) ** 2 * xM ** 2)


xM = np.linspace(-2, 2, int(1e7))

Mms = [0.001, 0.1, 1, 10, 1000]
cs = ["magenta", "k", "r", "b", "g"]


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
fig.subplots_adjust(left=0.05)

for j in range(len(Mms)):
    ax.plot(xM, r(xM, Mms[j]), c=cs[j], label=f"M/m={Mms[j]}")
    ax.plot(xM, -r(xM, Mms[j]), c=cs[j])


ax.set_aspect("equal")
ax.set_xlabel("$x_M/l$")
ax.set_ylabel("$y_M/l$")
ax.tick_params(**pt.params)
fig.legend(ncol=5, loc=9, columnspacing=0.5, handlelength=1, handletextpad=0.2)

fig.savefig("p1.png")

