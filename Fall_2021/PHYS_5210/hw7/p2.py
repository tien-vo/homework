from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def f(t, u, alpha):

    # Unpack
    u1, u2 = u
    du = np.zeros(u.shape)

    du[0] = u2
    du[1] = - np.sin(alpha) ** 2 * np.sin(2 * u1) / u2 ** 2

    return du


def solve(T, phi0=np.pi / 10, alpha=np.radians(30), dt=1e-4):

    Nt = int(T // dt)
    t = dt * np.arange(Nt)
    u = np.zeros((Nt, 2))
    u[0, 0] = phi0
    u[0, 1] = np.radians(1)

    for n in range(1, Nt):
        k1 = f(t[n - 1], u[n - 1], alpha)
        k2 = f(t[n - 1] + dt / 2, u[n - 1] + dt * k1 / 2, alpha)
        k3 = f(t[n - 1] + dt / 2, u[n - 1] + dt * k2 / 2, alpha)

        k4 = f(t[n - 1] + dt, u[n - 1] + dt * k3, alpha)
        u[n] = u[n - 1] + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print(f"{n}/{Nt}")

    return t, u


t, u = solve(10, phi0=np.radians(10))

plt.plot(t, u[:, 0] / np.pi, "-k")
plt.plot(t, u[:, 1] / np.pi, "--r")

plt.show()
