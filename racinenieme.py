# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:08:44 2022

@author: e_fmaill
"""
# import pdb; pdb.set_trace()
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams["text.usetex"] = True


theta = np.linspace(0, 2 * np.pi, 360)
r = 1
a = r * np.cos(theta)
b = r * np.sin(theta)


def racine_nieme(n):
    """Definit la racine nieme d'un nombre."""
    racine = np.zeros(n, dtype=complex)
    for k in np.arange(n):
        racine[k] = np.exp(2j * np.pi * k / n)
    return racine


def trace_un(n):
    """Methode qui trace Un."""
    data = racine_nieme(n)
    annotations = []
    for i in np.arange(n):
        annotations.append(r"$e^{{2\pi\times \frac{{{K}}}{{{N}}}}}$".format(K=i, N=n))

    # extract real part
    x = [ele.real for ele in data]
    # extract imaginary part
    y = [ele.imag for ele in data]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.set_aspect('equal', adjustable='box')
    ax.axhline(y=0, color="k")
    ax.axvline(x=0, color="k")
    ax.set_aspect(1)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    plt.scatter(x, y)
    plt.ylabel(r"$\Im(z)$")
    plt.xlabel(r"$\Re(z)$")
    for i, label in enumerate(annotations):
        ax.annotate(label, (x[i], y[i]))
    ax.plot(a, b)
    plt.grid("True", which="both")
    plt.savefig(f"U_{n}.png")
    plt.close()


for i in np.arange(3, 8 + 1):
    trace_un(i)
plt.close("all")
