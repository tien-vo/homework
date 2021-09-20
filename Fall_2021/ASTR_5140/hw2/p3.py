from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
import astropy.constants as c
import astropy.units as u
import ptrace as pt
import numpy as np


B0 = 10 * u.nT
vsw = 350 * u.km / u.s
E0 = vsw * B0

vperp = (E0 / B0 / vsw).decompose()

t = np.linspace(0, 3 * 2 * np.pi, 1000)

x = vperp * t - vperp * np.sin(t)
y = vperp * np.cos(t) - vperp
dydx = t
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)


pt.mpl(tex=True)
fig, ax = plt.subplots(1, 1, figsize=(8, 2.5))
fig.subplots_adjust(top=0.7)

ax.plot(x, y, "-w", alpha=0)
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap="jet", norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
line = ax.add_collection(lc)
cb = fig.colorbar(
    line, ax=ax, orientation="horizontal", location="top",
    shrink=0.5, ticks=np.round(np.linspace(x[0], x[-1], 4), decimals=1)
)
cb.set_label("$t\Omega_c$")

ax.set_xlabel("$x\Omega_c/v_{sw}$")
ax.set_ylabel("$y\Omega_c/v_{sw}$")
ax.set_aspect("equal")
ax.tick_params(**pt.params)
ax.set_xlim(x.min(), x.max())
ax.set_xticks(np.round(np.linspace(x[0], x[-1], 8), decimals=1))

fig.savefig("p3.png")
