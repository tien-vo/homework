import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


nu = np.linspace(0, 5, 1000)


sig = nu / (nu ** 2 + 1)

pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(nu, sig, "-k")

ax.set_xlim(nu[0], nu[-1])
ax.set_xlabel(r"$\nu/\omega_{ci}$")
ax.set_ylabel(r"$\sigma B_z/ne$")
ax.tick_params(**pt.params)
ax.axvline(1, c="k")

fig.savefig("p2.png")
