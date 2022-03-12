import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


x = np.linspace(-50, 50, 1000)

def sinc(x):
    return np.sin(x) / x



me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1)
fig.suptitle("sinc($x$)")
ax.plot(x, sinc(x), "-k")

ax.tick_params(**me.params)
ax.set_xlim(-50, 50)
ax.set_xlabel("$x$")

fig.savefig("p2b.png", dpi=300)
