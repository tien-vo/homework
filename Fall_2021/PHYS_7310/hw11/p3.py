import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def T(x, n1, n2, n3):
    return 4 * n1 * n2 ** 2 * n3 / (
        (n2 * (n1 + n3)) ** 2 +
        (n2 ** 2 * (n2 ** 2 - n3 ** 2) + n1 ** 2 * (n3 ** 2 - n2 ** 2)) *
        np.sin(x) ** 2
    )


def R(x, n1, n2, n3):
    return 1 - T(x, n1, n2, n3)


x = np.linspace(0, np.pi)


N = [(1, 2, 3), (3, 2, 1), (2, 4, 1)]
ls = ["-k", "-r", "-b"]
ls2 = [":k", ":r", ":b"]

pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
for j, (n1, n2, n3) in enumerate(N):

    ax.plot(
        x / np.pi, T(x, n1, n2, n3), ls[j], lw=2,
        label=fr"$(n_1,n_2,n_3)=({n1},{n2},{n3})$"
    )
    ax.plot(
        x / np.pi, R(x, n1, n2, n3), ls2[j], lw=2,
    )



ax.legend()
ax.set_xlim(0, 1)
ax.set_xticks([0, 0.5, 1])
ax.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"])
ax.set_xlabel("$x$")
ax.tick_params(**pt.params)

fig.savefig("p3.png")
