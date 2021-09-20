import matplotlib.pyplot as plt
import ptrace as pt
import numpy as np


def s(x, x0, y0):
    return (1 / 2 / np.pi) * (
        - y0 / ((x - x0) ** 2 + y0 ** 2)
        + y0 / ((x + x0) ** 2 + y0 ** 2)
        - y0 / ((x - x0) ** 2 + y0 ** 2)
        + y0 / ((x + x0) ** 2 + y0 ** 2)
    )


x = np.linspace(0, 10, 1000)


pt.mpl(tex=True)

fig, ax = plt.subplots(1, 1, figsize=(8, 6))

ax.plot(x, s(x, 2, 1), "-k", label="$(x_0,y_0)=(2,1)$")
ax.plot(x, s(x, 1, 1), "-r", label="$(x_0,y_0)=(1,1)$")
ax.plot(x, s(x, 1, 2), "-b", label="$(x_0,y_0)=(1,2)$")

ax.set_xlim(x.min(), x.max())
ax.set_xlabel("$x$")
ax.set_ylabel("$\sigma/\lambda$")
ax.tick_params(**pt.params)

ax.legend()


fig.savefig("p3.png")

