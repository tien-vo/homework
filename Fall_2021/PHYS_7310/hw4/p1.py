import numpy as np

V = 1
a = 1
x = a / 2
y = a / 2
z = 0


def Phi_nm(n, m):
    g = np.pi / a * np.sqrt(n ** 2 + m ** 2)
    return 4 * V / (np.pi ** 2) * (1 - (-1) ** n) * (1 - (-1) ** m) \
        / n / m * np.sin(n * np.pi * x / a) * np.sin(m * np.pi * y / a) \
        * np.cosh(g * z) / np.cosh(g * a / 2)


def Phi(N=1, M=1):
    y = 0
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            y += Phi_nm(n, m)

    return y


for N in range(1, 7):
    for M in range(1, 7):
        print(f"(N,M)=({N},{M}): Phi={Phi(N,M):.5f}")

