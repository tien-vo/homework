import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)

X, Y = np.meshgrid(x, y, indexing="ij")

H = np.cos(np.pi * X) * np.cos(np.pi * Y)

plt.pcolormesh(X, Y, H, cmap="seismic")
plt.show()
