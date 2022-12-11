# -*- coding: utf-8 -*-
"""
Created on Sun May  1 17:47:58 2022.

@author: e_fmaill
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# import math
from num2words import num2words as n2w
 

mpl.rcParams['text.usetex'] = True

x = np.linspace(-5, 5, 40)
y = x

# Solution de l'equa diff


def f(a, x):
    "C'est la solution de y' = ay."
    return np.exp(a*x)


# Parametres
a = -0.25
# Conditions initiales et les couleurs
C = np.array([1, 2, 0.5, 3/2])
color = ['orange', 'green', 'red', 'purple']
lenCw = n2w(len(C),lang="fr")
# Produit un a un
y = np.outer(C, f(a, x))
# Definition de la map
X, Y = np.meshgrid(x, x)
# Definition des vecteurs "vitesses"
u = np.ones(Y.shape)
v = a*Y

fig, ax = plt.subplots(figsize=(7, 3))
plt.grid(which='both')
ax.streamplot(X, Y, u, v, density=1, linewidth=0.5)
for i in range(len(C)):
    ax.plot(x, y[i])
    ax.scatter(0, C[i], marker='^', s=48,
               c=color[i], label=f'$y_\lambda(0)={C[i]}$')
ax.axis([-5, 5, 0, 4])
# ax.set_aspect('equal')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.title(f"{lenCw} solutions de $y'=ay, a={a}$")
plt.tight_layout()
# ax.Axes
# plt.show()
plt.savefig(f'Equa-diff-{np.abs(a)}.png', dpi=200)
