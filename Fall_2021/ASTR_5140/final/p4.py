import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


x = np.linspace(-5, 5, 1000)


By = 1 / np.cosh(x)
Bz = -np.tanh(x)
P_mag = By ** 2 + Bz ** 2


pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(x, By, "-r", label=r"$B_y/B_0$")
ax.plot(x, Bz, "-b", label=r"$B_z/B_0$")
ax.plot(x, P_mag, "-k", label=r"$B^2/B_0^2$")

ax.legend()
ax.set_xlim(x[0], x[-1])
ax.set_xlabel(r"$x/x_0$")
ax.tick_params(**pt.params)

fig.savefig("p4.png")
