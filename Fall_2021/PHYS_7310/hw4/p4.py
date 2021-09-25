from scipy.special import eval_legendre
import matplotlib.pyplot as plt
import numpy as np


def f(N):

    s = 0
    for n in range(N):
        s += eval_legendre(n, 0) ** 2

    return s


f_vec = np.vectorize(f)

N = np.logspace(0, 10, 10, dtype=np.int)

plt.scatter(N, f_vec(N), c="k")

plt.show()
