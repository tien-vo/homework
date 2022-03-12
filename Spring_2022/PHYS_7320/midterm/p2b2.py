import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np


x = np.linspace(-1, 1, 1000)

def sinc(x):
    return np.sin(x) / x


def I(x, k=20):
    kz = 10 * k
    return 1 / 4 / np.pi ** 2 * k / kz * sinc(k * x) ** 2


me.setup_mpl(tex=True)
fig, ax = plt.subplots(1, 1)
fig.suptitle("$|\psi|^2/k^2\hat{E}_0^2$")
ax.plot(x, I(x), "-k")

ax.tick_params(**me.params)
ax.set_xlim(x.min(), x.max())
ax.set_xlabel("$x/z$")

fig.savefig("p2b2.png", dpi=300)
