import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


eps = 0.1
x = 2 / eps * np.linspace(-np.pi, np.pi, 1000)


def B_low_k(t):
    return np.exp(-eps ** 2 * t) * np.cos(eps * x)


def B_high_k(t):
    return np.exp(-t) * np.cos(x)


def B(t):
    return B_low_k(t) + B_high_k(t)


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
fig.suptitle("$\epsilon=k_1/k_2=0.1$")
ax.plot(x, B(0), "-k", label=r"$k_2^2t/\sigma\mu_0=0$")
ax.plot(x, B(5), "-r", label=r"$k_2^2t/\sigma\mu_0=5$")

ax.set_xlabel("$k_2x$")
ax.set_ylabel("$B/B_0$")
ax.tick_params(**pt.params)
ax.legend()
ax.set_xlim(x.min(), x.max())

fig.savefig("p5.png")

