# -*- coding: utf-8 -*-
"""Plot the Folium."""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["text.usetex"] = True
params = {"text.latex.preamble": r"\usepackage{amsmath}"}
plt.rcParams.update(params)

eps = 1e-1
a = -1
b = 100
N = int(10 * (b - a))
A = 3 / 2
t1 = np.linspace(-b, a - eps, N)
t2 = np.linspace(a + eps, b, N)
x1 = A * t1 / (1 + t1**3)
y1 = t1 * x1
x2 = A * t2 / (1 + t2**3)
y2 = t2 * x2

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.set_aspect('equal', adjustable='box')
ax.axhline(y=0, color="k")
ax.axvline(x=0, color="k")
ax.set_aspect(1)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

x = np.linspace(-2, 2)
y = -x - 1 / 3 * A

ax.plot(
    x1,
    y1,
    color="orange",
    label=r"$x(t) = \frac{3at}{1+t^3}, y(t) = t x(t), a = \frac{3}{2}$",
)
ax.plot(x2, y2, color="orange")
ax.plot(x, y, "--", color="red", label=r"$y = -x-1$")
# ax.text(-3/2, 3/2, r"$x(t) = \frac{3at}{1+t^3}, a = \frac{3}{2}$", fontdict=None)
# ax.text(-3/2, 1.2, r"$y(t) = t x(t)$", fontdict=None)
# ax.text(0.45, -1.8, r"$y = -x-1$", fontdict=None)
plt.legend(loc="best")
ax.grid("True")
plt.savefig("folium.png")
plt.close(fig)
