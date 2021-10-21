import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


eps = 0.01
r0 = 5 / eps
r = np.linspace(-r0, r0, 10000)

Bz = 1 / (1 + (eps * r) ** 2)
Bphi = eps * r / (1 + (eps * r) ** 2)


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(r * eps, Bz, "-k", label="$B_z/B_0$")
ax.plot(r * eps, Bphi, "--k", label="$B_\phi/B_0$")

ax.set_xlim(-5, 5)
ax.set_xlabel("$\epsilon r$")
ax.set_ylabel("$B_z/B_0$ or $B_\phi/B_0$")
ax.tick_params(**pt.params)
ax.legend()

fig.savefig("p3.png")
