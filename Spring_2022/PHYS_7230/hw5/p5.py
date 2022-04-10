from scipy.integrate import quad
import matplotlib.pyplot as plt
import mpl_extras as me
import numpy as np

d = 1

def Cv(T):
    integrand = lambda x: x ** (d + 1) * np.exp(x) / (np.exp(x) - 1) ** 2
    re = quad(integrand, 0, T ** d, limit=100, epsabs=1e-12, epsrel=1e-12)
    return (d ** 2) * (T ** d) * re[0]


Cv_vec = np.vectorize(Cv)


T = np.logspace(-2, 2, 1000, dtype=np.float64)

me.setup_mpl(tex=True)

fig, ax = plt.subplots(1, 1)

ax.plot(T, Cv_vec(T), "-k")
ax.plot(T, 4 * T, "--k")

ax.text(1e-1, 5e0, "$C_v\sim T^d$")
ax.set_xlim(T[0], T[-1])
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("$k_BT/\hbar\omega_D$")
ax.set_ylabel("$C_v/Nk_B$")
ax.tick_params(which="both", **me.params)

fig.savefig("p5.png", dpi=600)
plt.show()
