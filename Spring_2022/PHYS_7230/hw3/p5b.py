import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np
import warnings

warnings.filterwarnings("ignore")


def N(T, mu):
    return 1 / (1 - np.exp(-(mu + 1) / T))


m = np.linspace(-1 - 2, -1 + 2, 400)
t = np.linspace(0, 10, 400)

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(m, N(0.1, m), "-k", label="$k_BT/\epsilon_0=0.1$")
ax.plot(m, N(1, m), "-r", label="$k_BT/\epsilon_0=1$")
ax.plot(m, N(10, m), "-b", label="$k_BT/\epsilon_0=10$")

ax.legend(frameon=False)
ax.set_ylim(-100, 100)
ax.set_xlim(m[0], m[-1])
ax.set_ylabel("$N/N_0$")
ax.set_xlabel("$\mu/\epsilon_0$")
ax.tick_params(**me.params)

fig.savefig("p5b.png", dpi=300)

plt.show()



