import astropy.constants as c
import astropy.units as u
import numpy as np


Theta = (90 - 23.4) * u.deg
#Theta = 90 * u.deg
T_sd = 23 * u.hr + 56 * u.min + 4 * u.s
Omega = 2 * np.pi / T_sd
y = 1 * u.AU

Fg = c.G * c.M_earth / y ** 2

a = np.sqrt(
    (Fg + (Omega * np.sin(Theta)) ** 2 * y) ** 2
    + (Omega ** 2 * np.sin(Theta) * np.cos(Theta) * y) ** 2
)
print(a.to(u.m / u.s ** 2))

T_s = 2 * np.pi * np.sqrt(y * np.sin(Theta) / a).to(u.hr)
print(T_s, T_sd, (T_s - T_sd).to(u.min))
