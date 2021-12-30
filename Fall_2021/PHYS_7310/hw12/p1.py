import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


n = 1.3
theta_c = np.arcsin(1 / n)
theta_i = np.radians(60)

d = np.linspace(0, 2, 1000)

psi = 2 * np.pi * np.sqrt((n * np.sin(theta_i)) ** 2 - 1) * d

N = (2 * n * np.cos(theta_i)) ** 2 * (1 - (n * np.sin(theta_i)) ** 2)

T = N / (
    N * np.cosh(psi) ** 2
    - ((n * np.cos(theta_i)) ** 2 + 1 - (n * np.sin(theta_i)) ** 2) *
    np.sinh(psi) ** 2)


pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(d, T, "-k")

ax.set_xlabel("$d/\lambda$")
ax.set_ylabel("$T$")

ax.set_xlim(d.min(), d.max())
ax.tick_params(**pt.params)
ax.set_title(r"$n=1.3,\theta_i=60^\circ$")

fig.savefig("p1.png")
