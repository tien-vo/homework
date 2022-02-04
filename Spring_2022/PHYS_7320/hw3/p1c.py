import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


theta = np.linspace(0, np.pi, 1000)
Pi = 3 / (5 * np.cos(theta) ** 2 - 8 * np.cos(theta) + 5)


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(np.degrees(theta), Pi, "-k")

ax.tick_params(**me.params)
ax.set_xlabel(r"$\theta$ [deg]")
ax.set_ylabel(r"$\Pi(\theta)$")
ax.set_xlim(0, 180)
fig.savefig("p1c.png")

