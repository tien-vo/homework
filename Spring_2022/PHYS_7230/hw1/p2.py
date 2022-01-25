from scipy.special import factorial
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np

me.setup_mpl(tex=True)

T = np.linspace(0, 1)
E = 1 / (np.exp(1 / T) - 1)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(T, E, "-k")
ax.tick_params(**me.params)
ax.set_xlabel(r"$T/T^\ast$")
ax.set_ylabel(r"$E/3Nk_BT$")
ax.set_xlim(T[0], T[-1])
fig.savefig("p3c.png")

T = np.linspace(0, 5, 1000)
C = (1 / T ** 2) * np.exp(1 / T) / (np.exp(1 / T) - 1) ** 2

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(T, C, "-k")
ax.tick_params(**me.params)
ax.set_xlabel(r"$T/T^\ast$")
ax.set_ylabel(r"$C_v/3Nk_B$")
ax.set_xlim(T[0], T[-1])
fig.savefig("p3d.png")
