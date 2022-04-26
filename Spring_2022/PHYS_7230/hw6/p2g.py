from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


def coth(x):
    return np.cosh(x) / np.sinh(x)


def BS(x, S):
    A = 1 / 2 / S
    return (1 + A) * coth((1 + A) * x) - A * coth(A * x)


def f(B, T):
    fmin = lambda m: m - S * BS(S * B / T + 3 * m / (S + 1) / T, S)
    sol = root_scalar(fmin, x0=np.sign(B), bracket=[-10, 10], method="toms748")
    return sol.root


S = 1/2

T = np.logspace(-1, 2, 1000)
m1 = np.zeros_like(T)
m2 = np.zeros_like(T)
m3 = np.zeros_like(T)
for i in range(len(T)):
    m1[i] = f(-0.1, T[i])
    m3[i] = f(0.1, T[i])
    m2[i] = np.nan if T[i] < 1 else 0


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(T, m1 / S, "-.k", label="$\mu B/k_BT_c=-1$")
ax.plot(T, m2 / S, "-k", label="$\mu B/k_BT_c=0$")
ax.plot(T, m3 / S, "--k", label="$\mu B/k_BT_c=1$")
ax.scatter([1], [0], c="k", s=20)

ax.legend(frameon=False)
ax.set_xscale("log")
ax.set_xlim(T[0], T[-1])
ax.set_xlabel("$T/T_c$")
ax.set_ylabel("$m/n\mu S$")
ax.tick_params(which="both", **me.params)

fig.savefig("p2g.png", dpi=600)
plt.show()

